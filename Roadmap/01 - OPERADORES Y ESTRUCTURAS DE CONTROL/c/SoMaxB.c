#include <stdio.h>
#include <stdbool.h>

int	main(void) {
		// Operadores Aritméticos
		int suma = 1 + 1;
		int resta = 2 - 1;
		int multiplicacion = 3 * 2;
		int division = 4 / 2;
		int modulo = 5 % 2;

		printf("Suma = %d\n", suma);
		printf("Resta = %d\n", resta);
		printf("Multiplicación = %d\n", multiplicacion);
		printf("Division = %d\n", division);
		printf("Modulo = %d\n\n", modulo);

		// Operadores lógicos
		bool and = 3 && 4;
		bool or = 3 || 4;
		bool not = !(3 && 4);

		printf("And = %d\n", and);
		printf("Or = %d\n", or);
		printf("Not = %d\n\n", not);

		// Operadores bit a bit
		int a = 6;  // 6 en binario es 0000 0110
		int b = 3;  // 3 en binario es 0000 0011
    
		int andBB = a & b;  // 0000 0110 & 0000 0011 = 0000 0010 (2)
		int orBB = a | b;   // 0000 0110 | 0000 0011 = 0000 0111 (7)
		int compBB = ~a;    // ~0000 0110 = 1111 1001 (-7 en complemento a 2)
		int xorBB = a ^ b;  // 0000 0110 ^ 0000 0011 = 0000 0101 (5)
    
		printf("And bit a bit: %d\n", andBB);    // Imprime 2
		printf("Or bit a bit: %d\n", orBB);      // Imprime 7
		printf("Complemento a uno: %d\n", compBB); // Imprime -7
		printf("O-exclusiva bit a bit: %d\n\n", xorBB); // Imprime 5

		// Operadores de asignación
		int uno = 1;
		printf("Igual = %d\n", uno);
		uno += 1;
		printf("Mas igual = %d\n", uno);
		uno -= 1;
		printf("Menos igual = %d\n", uno);
		uno *= 4;
		printf("Por igual = %d\n", uno);
		uno /= 2;
		printf("Dividido igual = %d\n", uno);
		uno &= 1;
		printf("Y igual = %d\n", uno);
		uno++;
		printf("Incremento = %d\n", uno);
		uno--;
		printf("Decremento = %d\n\n", uno);

		// Operadores relacionales
		int mayor = 4 > 3;
		int menor = 3 < 4;
		int mayor_o_igual = 4 >= 2;
		int menor_o_igual = 3 <= 4;
		int igual = 6 == 6;
		int diferente = 8 != 5;

		printf("Mayor = %d\n", mayor);
		printf("Menor = %d\n", menor);
		printf("Mayor o igual = %d\n", mayor_o_igual);
		printf("Menor o igual = %d\n", menor_o_igual);
		printf("Igual = %d\n", igual);
		printf("Diferente = %d\n\n", diferente);

		// Operador condicional o ternario
		int x = 4;

		printf("x >= 5 ? 1 : 0 = %d\n\n", x >= 5 ? 1 : 0);

		//Bonus
		int i = 10;
    
		while (i < 55) {
				if (i % 2 == 0 && i != 16 && i % 3 != 0)
					printf("%d\n\n", i);
				i++;
				}
		return 0;
}
