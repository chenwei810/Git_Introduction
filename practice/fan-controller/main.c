#include "board.h"
#include "fan.h"
#include "sensor.h"

int main(void)
{
    board_init();
    fan_init();

    for (;;) {
        float celsius = sensor_read_celsius();
        fan_update(celsius);
        delay_ms(1000);
    }
}
