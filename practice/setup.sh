#!/usr/bin/env bash
#
# Creates the practice repository as it is at the start of a chapter,
# so that you can follow the "Hands-on" section of any chapter.
#
#   bash practice/setup.sh <chapter> [folder]
#
#   chapter  2 to 10
#   folder   where to create it (default: ~/git-practice/fan-controller)
#
# Works in Git Bash on Windows, and in the terminal on macOS and Linux.

set -euo pipefail

usage() {
    echo "Usage: bash practice/setup.sh <chapter 2-10> [folder]"
}

chapter="${1:-}"
case "$chapter" in
    2|3|4|5|6|7|8|9|10) ;;
    *) usage; exit 1 ;;
esac

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
target="${2:-$HOME/git-practice/fan-controller}"

if [ -e "$target" ]; then
    echo "The folder already exists: $target"
    echo "Delete it first, or give another folder as the second argument."
    exit 1
fi

if ! command -v git >/dev/null 2>&1; then
    echo "Git is not installed. See Chapter 1."
    exit 1
fi

if [ "$chapter" -ge 3 ]; then
    if [ -z "$(git config user.name || true)" ] || [ -z "$(git config user.email || true)" ]; then
        echo "Set your name and email first (Chapter 1):"
        echo '  git config --global user.name "Your Name"'
        echo '  git config --global user.email "you@example.com"'
        exit 1
    fi
fi

# Replace the first occurrence of a text on each line, in place.
replace() {
    awk -v old="$2" -v new="$3" '{
        i = index($0, old)
        if (i) $0 = substr($0, 1, i - 1) new substr($0, i + length(old))
        print
    }' "$1" > "$1.tmp"
    mv "$1.tmp" "$1"
}

# A commit made by a teammate, so the history shows two authors.
teammate_commit() {
    GIT_AUTHOR_NAME="Teammate" GIT_AUTHOR_EMAIL="teammate@example.com" \
    GIT_COMMITTER_NAME="Teammate" GIT_COMMITTER_EMAIL="teammate@example.com" \
        git commit -q -am "$1"
}

mkdir -p "$(dirname "$target")"
cp -R "$here/fan-controller" "$target"
cd "$target"

# Chapter 2 starts from a plain folder, before Git.
if [ "$chapter" -eq 2 ]; then
    echo "Ready: $target (Chapter 2)"
    exit 0
fi

# --- Chapter 2: the first commit, and the fix is staged ---------------------
git init -q
git symbolic-ref HEAD refs/heads/main
git add .
git commit -q -m "Initial commit"
replace sensor.c "(mv - 600)" "(mv - 500)"
git add sensor.c

# --- Chapter 3 only looks inside commits, so chapter 4 starts the same -------

# --- Chapter 4: two branches ---------------------------------------------------
if [ "$chapter" -ge 5 ]; then
    git switch -q -c fix-temperature
    git commit -q -m "Fix temperature sensor offset"
    git switch -q main
    git switch -q -c night-mode
    replace sensor.c "return (mv - 600) / 10.0f;" "return smooth((mv - 600) / 10.0f);"
    git commit -q -am "Smooth temperature readings for night mode"
    git switch -q main
fi

# --- Chapter 5: fast-forward, then a conflict on the fix branch --------------
if [ "$chapter" -ge 6 ]; then
    git merge -q night-mode
    git branch -q -d night-mode
    git switch -q fix-temperature
    git merge -q main >/dev/null 2>&1 || true
    git show main:sensor.c > sensor.c
    replace sensor.c "(mv - 600)" "(mv - 500)"
    git add sensor.c
    git commit -q --no-edit
    git switch -q main
fi

# --- Chapter 6: a teammate pushes to main --------------------------------------
if [ "$chapter" -ge 7 ]; then
    replace fan.c "FAN_PWM_HZ       1000" "FAN_PWM_HZ       25000"
    teammate_commit "Raise fan PWM frequency to 25 kHz"
fi

# --- Chapter 7: review changes, then the pull request is merged --------------
if [ "$chapter" -ge 8 ]; then
    git switch -q fix-temperature
    cat > sensor.c <<'EOF'
#include "board.h"
#include "filter.h"
#include "sensor.h"

#define SENSOR_OFFSET_MV  500   /* output at 0 °C */
#define SENSOR_MV_PER_C   10    /* change per °C */

/* Analog temperature sensor: 500 mV at 0 °C, plus 10 mV per °C. */
float sensor_read_celsius(void)
{
    int mv = adc_read_mv();
    return smooth((mv - SENSOR_OFFSET_MV) / (float)SENSOR_MV_PER_C);
}
EOF
    git commit -q -am "Use named constants for sensor conversion"
    git switch -q main
    git merge -q --no-ff fix-temperature -m "Merge pull request #1 from fix-temperature"
    git branch -q -d fix-temperature
fi

# --- Chapter 8: release v1.0.0, then a hotfix v1.0.1 ---------------------------
if [ "$chapter" -ge 9 ]; then
    git tag -a v1.0.0 -m "Version 1.0.0"
    git switch -q -c hotfix-filter v1.0.0
    replace filter.c "static float average = 0.0f;" "static float average = 25.0f;"
    git commit -q -am "Start temperature filter at room temperature"
    git switch -q main
    git merge -q --no-ff hotfix-filter -m "Merge branch 'hotfix-filter'"
    git tag -a v1.0.1 -m "Version 1.0.1"
    git branch -q -d hotfix-filter
fi

# --- Chapter 9: an experiment that was reverted --------------------------------
if [ "$chapter" -ge 10 ]; then
    replace main.c "delay_ms(1000);" "delay_ms(10);"
    git commit -q -am "Read temperature every 10 ms"
    git revert --no-edit HEAD >/dev/null
fi

echo "Ready: $target (Chapter $chapter)"
git log --oneline --graph --all
