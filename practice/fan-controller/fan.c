#include "board.h"
#include "fan.h"

#define FAN_PWM_HZ       1000
#define FAN_ON_CELSIUS   45.0f
#define FAN_OFF_CELSIUS  40.0f

void fan_init(void)
{
    board_pwm_init(FAN_PWM_HZ);
}

void fan_update(float celsius)
{
    if (celsius >= FAN_ON_CELSIUS)
        fan_set_duty(100);
    else if (celsius < FAN_OFF_CELSIUS)
        fan_set_duty(0);
}
