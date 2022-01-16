#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <avr/io.h>
#include <util/delay.h>
#include <stdbool.h>
#include <inttypes.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

char* int_to_string(int);
int pot(int n,int p);