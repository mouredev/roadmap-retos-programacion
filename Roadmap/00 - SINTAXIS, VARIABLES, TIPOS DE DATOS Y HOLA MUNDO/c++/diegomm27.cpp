/*
    WEBSITE OFFICIAL URL: https://isocpp.org/
*/

/*
    Code comments can be made by different ways:

        1. For a long piece of code, we can use '/*' to start a comment and the reverse to finish it.
        2. Using two slices slashes '//' to comment all the code in a line.

*/

#include <iostream>
#include <string>
using namespace std;

/*

    Character types: They can represent a single character, such as 'A' or '$'. The most basic type is char, which is a one-byte character. Other types are also provided for wider characters.
    Numerical integer types: They can store a whole number value, such as 7 or 1024. They exist in a variety of sizes, and can either be signed or unsigned, depending on whether they support negative values or not.
    Floating-point types: They can represent real values, such as 3.14 or 0.01, with different levels of precision, depending on which of the three floating-point types is used.
    Boolean type: The boolean type, known in C++ as bool, can only represent one of two states, true or false.

*/


const string lenguaje = "C++"; // Variable tipo constante

// Character types:
string mystring = "¡Hola Mundo!"; 

char character = 'D'; // Exactly one byte in size. At least 8 bits.
char16_t char16 = '!'; // Not smaller than char. At least 16 bits.
char32_t char32 = '!'; // Not smaller than char16_t. At least 32 bits.
wchar_t wchar = '!'; // Can represent the largest supported character set

// Numerical integer types
signed char signedChar = 5; // Same size as char. At least 8 bits.
signed short int signedShortInt= 5; // 	Not smaller than char. At least 16 bits.
signed int signedInt = 5; // Not smaller than short. At least 16 bits.
signed long int signedLongInt= 5; // 	Not smaller than int. At least 32 bits.
signed long long int signedLong2int = 5; // Not smaller than long. At least 64 bits.

// Just as we have for the numerical SIGNED integer types, we would have the UNSIGNED ones

// Floating-point types
float floatValue = 16.5;
double doubleFloat = 16.5;
long double longDoubleFloat = 16.5;

// Boolean type
bool booleano = true;


int main()
{
    cout << "Hola, " + lenguaje + "!"<< endl;
}