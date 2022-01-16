#include  "Keypad.h"

int  keyPadStatus(  )
{
   int k,p;
   int num=0;
   for(k=0;k<4;k++)
   {
	 PORTC=pot(2,k+1);
	 for(p=0;p<3;p++)
	 {
	       switch(p)
	       {
		  case 0:
		     if(PINC & (1<<0))
			num=3*k+3;
		     break;
		  case 1:
		     if( PIND & (1<<2) )
			num=3*k + 1;
		     break;
		  case 2:
		     if( PIND & (1<<3) )
			num=3*k+2;
		     break;
	       }
	 }
	 //_delay_ms(100);
   }
   
   
   return num;
}

void  keyPadSetVar( int* var )
{
      int kp=keyPadStatus( );
      var[ 0 ]=(  kp==var[ 0 ] || kp==0)?var[ 0 ]:kp;
      
}