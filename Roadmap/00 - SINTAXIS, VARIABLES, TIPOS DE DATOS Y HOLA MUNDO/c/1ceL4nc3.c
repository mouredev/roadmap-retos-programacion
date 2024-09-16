https://www.cprogramming.com

Types of comments
// // = // comment // 
/* */ = /* comment */

// constant value = const + type of variable + name of variable //
const int n = 5;

//Data types //
char character = 'a';                            // Single character, 1 byte //
int integer = 9;                                 // Signed integer in base 10, 4 bytes//
float decimal = 1.5;                             // Floating point number with six digits of precision, 4 bytes //
double decimalDouble = -2456.4452;               // Hold about 15 to 16 digits after and before any given decimal point, 8 bytes //
long longinteger = 132344546L;                   // Signed long integer, 4 bytes //
short shortinteger = 128;                        // Short signed integer, 2 bytes //
unsigned unsignedinteger = 50;                   // Unsigned integer in base 10, 4 bytes //
unsigned long unsignedlonginteger = 451345245UL; // Unsigned long long integer, 8 bytes // 
unsigned short unsignedshortinteger = 256;       // Short unsigned integer, 2 bytes //

#include <stdio.h>                 // header function

int main()                         // main function
{                                  // indicates the beginning and end of functions and other code blocks // 
    char l_name = 'C';             // create a variable named l_name and assign it the character C //

    printf("!Hola %c!\n", l_name); // print the string !Hola + variable l_name// // %c indicates that the funtion is printing a character// // \n print another line//

}
