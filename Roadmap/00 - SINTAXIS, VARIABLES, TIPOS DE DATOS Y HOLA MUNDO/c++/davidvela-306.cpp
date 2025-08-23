// Libraries
#include <iostream> // this library let us work with input and output objects such as cout
#include <string>

// https://isocpp.org/
/*
 * Este es un 
 * comentario en 
 * varias lineas
 * */

// Variable
std:: string name = "My name is David"; //std:: show that we'll use standar librarie's string specifically
// Constant
const float PI = 3.1415; // Unchangable, read-only

/*
 * PRIMITIVE DATA TYPES
 * */
int number = 1; // 4 bytes
short int short_number = 1; // 2 bytes
long int long_number = 12312938793847; // 4 u 8 bytes
long long int super_long_number =239482983748927; // more than 8 bytes
						 //
float float_number = 1.22f; // 4 bytes
double double_number = 1.29303920; // 8 bytes
long double long_double_number = 1.230948023984023894; // 10 or 16 bytes
std:: string text = "Hi";
char letter = 'd';

bool my_boolean = true; // only needs one bite but it is defined with 1 byte

/*
 * PRINT HELLO [ LANGUAGE]
 * */

int main(){
	std:: cout << "Hello, C++ \n"; // \n is a line break
return 0;
}
// it is not necesary call main function because is the entry point's program.

/*
 * TO RUN THE PROGRAM I NEEDED TO USE g++
 * Create the executable with g++ ./davidvela-306.cpp -o davidvela-306
 * Then run ./davidvela-306
 * */

