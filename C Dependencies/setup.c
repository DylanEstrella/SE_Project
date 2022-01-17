#include "setup.h"

void main_init()
{
   LCD_init();
   serial_begin();
   DDRC=30;
   // Power-up delay
    _delay_ms(100);   
}