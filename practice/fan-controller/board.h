#ifndef BOARD_H
#define BOARD_H

/* Hardware access, provided by the board support package. */
void board_init(void);
int  adc_read_mv(void);
void board_pwm_init(int hz);
void fan_set_duty(int percent);
void delay_ms(int ms);

#endif
