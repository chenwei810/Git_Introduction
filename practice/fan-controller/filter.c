#include "filter.h"

static float average = 0.0f;

/* Moving average, so the fan does not change speed too often. */
float smooth(float x)
{
    average = average * 0.9f + x * 0.1f;
    return average;
}
