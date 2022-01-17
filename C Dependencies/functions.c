#include "functions.h"

char* int_to_string(int num)
{ 
   char *string = malloc (sizeof (char) * (int)((ceil(log10(num))+1)*sizeof(char)));
 
   sprintf(string, "%d", num);
   
   return string;
}

int pot(int n,int p)
{
   int i=0;
   int r=1;
   for(i=0;i<p;i++)
   {
      r*=n;
   }
    return r;
}  