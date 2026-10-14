#include "board.h"
#include "filter.h"
#include "sensor.h"

/* Analog temperature sensor: 500 mV at 0 °C, plus 10 mV per °C. */
float sensor_read_celsius(void)
{
    int mv = adc_read_mv();
    return (mv - 600) / 10.0f;
}
