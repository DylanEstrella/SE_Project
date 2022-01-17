#include  "menu.h"
#define MAX_STR 50
#define BAUD 9600

void serial_begin();
unsigned char serial_read_char();
void serial_print_char(unsigned char caracter);
void serial_println_str(char *cadena);
char* get_RX_buffer();
bool is_data_ready();
int recibir_encender_led();
void enviar2raspi1();