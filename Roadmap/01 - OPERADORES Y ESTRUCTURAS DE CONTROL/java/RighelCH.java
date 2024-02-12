package retos;

public class Uno {

	public static void main(String[] args) {
	int a=5, b=7;               
	boolean x = true, y = false;
	OperacionesAritméticas(a,b);
	OperadoresLógicos(x,y);
	OperadorComparación(a,b);
	Asignación(a);
	OperadorBit(a,b); //5 en binario=0101    7 en binario=111
	Condicional(a,b);
	Iterativas(a);
	//Excepciones
	try {
	     //operación aritmética que podría generar una excepción
	    int resultado = 10 / 0; // Esto generará una ArithmeticException
	} catch (ArithmeticException e) {
	    //  Si se genera una excepción, captura y maneja la excepción aquí
	    System.out.println("Error aritmético: " + e.getMessage());
	}
//--------------EJERCICIO EXTRA---------------------------------------------------
		/*Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/
		for(int i=10;i<=55;i+=2) {
			if(i!=16 && i%3!=0)
				System.out.print(i+ " ");
		}
	}
	
		static void OperacionesAritméticas (int a, int b) {
			 int suma = a + b;
		        int resta = a - b;
		        int multiplicacion = a * b;
		        int division = a / b;
		        int modulo = a % b;

		        System.out.println("Suma: " + suma);
		        System.out.println("Resta: " + resta);
		        System.out.println("Multiplicación: " + multiplicacion);
		        System.out.println("División: " + division);
		        System.out.println("Módulo: " + modulo);
		}
		static void OperadoresLógicos(boolean x, boolean y) {
	
			boolean and = x && y;
			boolean or = x || y;
			boolean not = !x;

			System.out.println("AND: " + and);
			System.out.println("OR: " + or);
			System.out.println("NOT: " + not);
		}
		static void OperadorComparación(int a, int b) {
			
			boolean igual = (a == b);
			boolean noIgual = (a != b);
			boolean mayor = (a > b);
			boolean menor = (a < b);

			System.out.println("Igual: " + igual);
			System.out.println("No Igual: " + noIgual);
			System.out.println("Mayor: " + mayor);
			System.out.println("Menor: " + menor);

		}
		static void Asignación(int a) {
			System.out.println("Variable: " + a);
			a += 10;
			System.out.println("Variable: " + a);
			a -= 7;
			System.out.println("Variable: " + a);
		}
		static void OperadorBit(int a, int b) {
	
			int andBits = a & b;
			int orBits = a | b;
			int xorBits = a ^ b;
			int complemento = ~a;

			System.out.println("AND Bits: " + andBits);
			System.out.println("OR Bits: " + orBits);
			System.out.println("XOR Bits: " + xorBits);
			System.out.println("Complemento: " + complemento);

		}
		static void Condicional(int edad,int numero) {
			
			if (edad >= 18) {
			    System.out.println("Es mayor de edad");
			} else {
			    System.out.println("Es menor de edad");
			}
			switch(numero) {
			case 1,2,3,4,5,6: System.out.println("Es un numero menor que 7");
			case 7: System.out.println("El número es 7");
			default: System.out.println("Es un numero mayor que 7");
			}

		}
		static void Iterativas(int a) {
			for (int i = 0; i < a; i++) {
			    System.out.println("Iteración: " + i);
			}

			int j = 0;
			while (j < a) {
			    System.out.println("Iteración while: " + j);
			    j++;
			}

		}
	

}
