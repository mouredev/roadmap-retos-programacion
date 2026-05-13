// No existe página oficial de c
	// Lenguaje de programacion: c 
	
	// Forma 1,comentario lineal
	
	/*
	 Forma 2, comentario multilineal
	*/ 
	
#include <stdio.h>


#define CONSTANTE 30

void main() {	
	
	char *x = "Hola";
	const char *b = "Esto es una constante"; // Forma de constante 2

	printf("%s\n",b);
	printf("%d\n",CONSTANTE);

	// Datos primitivos en c:
	int entero = 10;
	char *caracter = "a";
	float decimal = 1.4999;
	double decimal_ochobytes_mas = 1.49998888;
	// No obstante, tenemos modificadores para estos datos:
	
	signed int enterob = 10; // (valores entre -10 y 10) 
	unsigned int enteroc = 10;// Nunca es negativo 

	short int enterod = 8; // Rango de 16 bits

	long int enteroe = 8; // Rango de 32 bits

	long long int enterof = 8; // Rango de 64 bits!
	
	printf("¡Hola, c!\n");
}
