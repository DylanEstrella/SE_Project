#include "setup.h"

int main(void)
{
   main_init();
   
   int num=0;
   
   while(1)
   {

      LCD_setRow(1);
      LCD_writeString("Presione * para"); 
      LCD_setRow(2);
      LCD_writeString(" Ingresar Datos");
      
      keyPadSetVar( &num );
      
      if(num==10)
      {
	 int tipo=menu_TipoResiduo( );
	 int peso=menu_Peso( );     
	 int precio;
	 
	 char str[80];
	 sprintf(str, "%d,%d", tipo,peso);
	 serial_println_str(str);	 
	 
	 precio=tipo*peso;
	 LCD_clear();
	 LCD_setRow(0);
	 LCD_writeString("Precio a pagar:");  
	 LCD_setXY(2,3);
	 LCD_writeInt(precio);
	 
	 
	 _delay_ms(5000);
	 LCD_clear();
	 LCD_setRow(1);
	 LCD_writeString("Esperado al"); 
	 LCD_setRow(2);
	 LCD_writeString("  Servidor");
	 _delay_ms(10000);
	 LCD_clear();
	 
	 num=0;
      } 
      
      
   }
   
    return 0;
}
