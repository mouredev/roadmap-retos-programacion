public class AndrewCodev {
    public static void main(String args[]) {

		int num1 = 100;
		int num2 = 5;

		System.out.println("OPERADORES ARITMETICOS");
		int suma = num1 + num2;
		System.out.println("(+): " + num1 + " + " + num2 + " = " + suma);

		int resta = num1 - num2;
		;
		System.out.println("(-): " + num1 + " - " + num2 + " = " + resta);

		int multip = num1 * num2;
		System.out.println("(*): " + num1 + " * " + num2 + " = " + multip);
		int division = num1 / num2;
		System.out.println("(/): " + num1 + " / " + num2 + " = " + division);

		int resto = num1 % 2;

		if (resto == 0) {
			System.out.println("(%) El numero: " + num1 + " es par");
		} else {
			System.out.println("(%) El número: " + num1 + " es impar");
		}

		System.out.println("\nOPERADORES DE COMPARACION");
		boolean esIgual = (num1 == num2); // Igual a
		boolean esMayor = (num1 > num2); // Mayor que
		boolean esMenorIgual = (num1 <= num1); // Menor o igual que

		if (esIgual) {
			System.out.println("(==) Los numeros: " + num1 + " y " + num2 + " Son iguales");
		} else {
			System.out.println("(!=) Los numeros: " + num1 + " y " + num2 + " Son diferentes");
		}

		if (esMayor) {
			System.out.println("(>): " + num1 + " > " + num2 + " Es mayor");
		} else if (esMenorIgual) {
			System.out.println("(<=): " + num1 + " <= " + num2 + " es menor o igual");
		}

		System.out.println("\nOPERADORES DE ASIGNACION");
		int edad = 25; // Operador de asignación simple
		System.out.println("Asignación simple: int edad = " + edad + ";");
		edad += 5; // Operador de asignación compuesta (edad = edad + 5)
		System.out.println("Asignación compusta: int edad += 5; (edad = edad + 5) = " + edad);

		System.out.println("\nOPERADORES DE LOGICOS");
		boolean resultadoAnd = (true && false); // Operador AND
		System.out.println("AND (&&): resultadoAnd = (true && false); - " + resultadoAnd);
		boolean resultadoOr = (true || false); // Operador OR
		System.out.println("OR (||): resultadoOr = (true || false); - " + resultadoOr);
		boolean resultadoNot = !true; // Operador NOT
		System.out.println("NOT (!): resultadoNot = !true; - " + resultadoNot);

		System.out.println("\nOPERADORES DE INCREMENTO Y DECREMENTO");
		int contador = 0;
		System.out.println("int contador= " + contador);
		contador++; // Operador de incremento (equivale a contador = contador + 1)
		System.out.println("INCREMENTO (++): contador++ = " + contador);
		contador--; // Operador de decremento (equivale a contador = contador - 1)
		System.out.println("DECREMENTO (--): contador-- = " + contador);

		// DIFICULTAD EXTRA
        System.out.println("\nEste código imprimirá todos los números pares entre 10 y 55 (incluidos), que no sean 16 y no sean múltiplos de 3");
		for (int i = 10; i <= 55; i++) {
			if(i % 2 == 0 && i != 16 && i % 3 != 0 ) {
				System.out.println(i);
			}
		}
	}
}
