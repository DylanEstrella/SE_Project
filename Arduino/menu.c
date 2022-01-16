#include  "menu.h"

int menu_TipoResiduo( )
{
   LCD_clear();
   bool menu2=1;
   bool menu=1;
   int response=0;
   while(menu)
    {
	 menu2=1;
       
	 LCD_setRow(0);
	 LCD_writeString("Tipo de residuo:");
	 LCD_setRow(1);
	 LCD_writeString(" 1.Industrial");
	 LCD_setRow(2);
	 LCD_writeString(" 2.NO Industrial"); 
	 
	 while(menu2)
	 {   
	    keyPadSetVar(  &response );
	    menu2=(response<11 &&  response>0)?0:1;
	    menu=(response>0 && response<3 )?0:1;
	    while(keyPadStatus()!=0);
	 }
    }
    LCD_clear();
   return response;
}


int menu_Peso( )
{
   bool menu2=1;
   bool menu=1;
   int response=0;

   while(menu)
    {
	 menu2=1;
	 
	 LCD_clear();
	 LCD_setRow(0);
	 LCD_writeString("Ingrese el peso:");
       
	 while(menu2)
	 {
	    int key=keyPadStatus( );
	    
	    if( ( key>0 && key<10) || key==11 )
	    {
	       key=(key==11)?0:key;
	       int res=response*10+key;
	       
	       if( res>=0 && res<22001 )
	       {
		  response=res;
	       }
	       else
	       {
		  LCD_clear();
		  LCD_setRow(0);
		  LCD_writeString("   - Error -");
		  LCD_setRow(1);
		  LCD_writeString(" El numero debe ");
		  LCD_setRow(2);
		  LCD_writeString("      estar ");
		  LCD_setRow(3);
		  LCD_writeString(" Entre 0 y 22000");
		  
		  _delay_ms(400);
	       }
	       menu2=0;

	       while(keyPadStatus()!=0);
	    }
	    
	    else if(  key==10 )
	    {
	       
	       response=(int) ( response )/10;
	       menu2=0;
	       
	       while(keyPadStatus()!=0);
	    }
	    
	    else if(  key==12 )
	    {
	       
	       menu=0;
	       menu2=0;
	       
	       while(keyPadStatus()!=0);
	    }
	    
	    LCD_setXY(2,4 );
	    LCD_writeInt(response);
	        
	 }

    }
   LCD_clear();
   return response;
}