#include "LCD.h"

/*...........................................................................
  Name: 		keyPadStatus
 Purpose:  	Comprobe if a button was pressed on the keypad
  Entry:    	Nothing
  Exit:     		A number between 1-12
  Notes:    	
			1 for 1     --- 2 for 2    --- 3 for 3 --- 
			4 for 4     --- 5 for 5    --- 6 for 6 --- 
			7 for 7     --- 8 for 8    --- 9 for 9 --- 
			10 for "*" --- 11 for 0  --- 12 for "#" 
			
			-- 0 means that the keypad don't return nothing--
*/

int  keyPadStatus(  );

/*...........................................................................
  Name: 		keyPadSetVar
  Purpose:  	Pass the value of the bottom in KeyPad to a variable 
			on main program
  Entry:    	Variable Direction (Pointer)
  Exit:     		Nothing
  Notes:    	Example: keyPadSetVar(&var_name)
			This function use keyPadStatus function.
			
*/
void  keyPadSetVar( int* v );
