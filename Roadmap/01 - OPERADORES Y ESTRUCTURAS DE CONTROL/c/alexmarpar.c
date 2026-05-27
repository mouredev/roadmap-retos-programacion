#include <stdio.h>

int main() {

	printf("------------------------->Operadores aritmeticos\n");
	
	printf("Operador + (5+5): 10 = %d\n", 5+5);
	printf("Operador - (20-10): 10 = %d\n", 20-10);
	printf("Operador * (5*2): 10 = %d\n", 5*2);
	printf("Operador / (40/4): 10 = %d\n", 40/4);
	printf("Operador % (10%3): 1 = 1 %d\n", 10%3);	// C nos proporciona el resto de la división con este Operador
	
	printf("---------------------------> Operadores de Comparación\n");

	// Operadores de comparación	
	printf("Operador ==  (Igualdad): 10 == 10 %d\n", 10==10); // 1 
	printf("Operador !=  (Distinto de ): 10 != 10 %d\n", 10!=10); // 0 
	printf("Operador <  (Menor que): 10 < 20 %d\n", 10<20); // 1 
	printf("Operador >  (Mayor que): 10 > 20 %d\n", 10>20); // 0 
	printf("Operador <=  (Menor o igual a que): 10 <= 10 %d\n", 10<=10); // 1 
	printf("Operador >=  (Mayor o igual a que): 10 >= 11 %d\n", 10>=11); // 0
	
	printf("---------------------> Operadores lógicos\n");

	// Operadores lógicos:
	printf("Operador &&  (AND): 1 && 0 %d\n", 1 && 0); // 0 
	printf("Operador &&  (AND): 1 && 1 %d\n", 1 && 1); // 1 
	printf("Operador &&  (AND): 0 && 1 %d\n", 0 && 1);  // 0
	printf("Operador &&  (AND): 0 && 0 %d\n", 0 && 0);  // 0
	
	printf("------|| OR ------------\n");
	
	printf("Operador ||  (OR): 0 || 0 %d\n", 0 || 0); // 0
	printf("Operador ||  (OR): 0 || 1 %d\n", 0 || 1); // 1 
	printf("Operador ||  (OR): 1 || 0 %d\n", 1 || 0); // 1 
        printf("Operador ||  (OR): 1 || 1 %d\n", 1 || 1); // 1 
	
	printf("------! NOT --------------\n");			// (Invierte el valor lógico) Syntax: !value (if not value, then")
	
	printf("Operador !  (NOT): !0 %d\n", !0); // 1
	printf("Operador !  (NOT):  !1 %d\n", !1); // 0 
	
	
	printf("---------------------------> Operadores de identidad\n");

	// Operadores de identidad:
	int a = 10;
	printf("Operador =  (igual): a = 10 %d\n", a); // 10 
	printf("Operador +=  (más es igual a ): a+=10 %d\n", a+=4); // 14 
	printf("Operador -=  (menos es igual a ): a-=10 %d\n", a-=10); // 4
	printf("Operador *=  (por es igual a ): a*=2 %d\n", a*=2); // 8
	printf("Operador /=  (entre es igual a ): a/=4 %d\n", a/=4); // 2
	
	printf("--------------------------_> Operadores de bit\n");

	// Aparte de los operadores AND y OR que se pueden utilizar para bits (Ya que recordemos que no hay booleanos)
	// Tenemos los siguientes
	
	printf("Operador ^  (XOR): 5^2%d\n", 5^2); // 111 (7)   (si almenos uno es 1, uno)
	printf("Operador ~  (NOT): ~8 %d\n", ~8); // -9 (invierte)
	printf("Operador <<  (Desplazamiento a la izquierda): 6<<1 %d\n", 6<<1); // 1100 (12)
	printf("Operador >>  (Desplazamiento a la derecha): 1>>6 %d\n", 1>>6); //   ?
	
								 
	int control=3;

	if (control==3) {
		printf("Control es igual a 3 así que imprimos");
	} else if (control<5) {
		printf("Control no es igual a 3 pero es menor a 5");
	} else {
		printf("Control es >10");
	}
	
	switch (control) {
		case 1: printf("Control tiene valor a 1");
			break;
		case 2: printf("Control tiene valor a 2");
			break;
		case 3: printf("Control tiene valor a 3");
			break;
	}


	for (int i = 0; i<10; i++) {
		printf("Valor de i: %d\n", i);
	}
	while (control==3) {
		printf("Control ha entrado en nuestro while, control++");
		control++;
	}

	do {
   		printf("Checkeo de la variable control"); // Esto imprime 2 por do while
		control--;
	}
	while (control>3);
	
	// Desafio:
	for (int i = 10; i<=55; i++) {

		if (i%2==0 && i!=16 && i%3!=0) {
			printf("Números: %d\n",i);
		}
	}
	return 0;


}
