public class IsidroJNG {

	public static void main(String[] args) {
		// Operadores aritméticos
        int a = 10;
        int b = 20;
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Módulo: " + (a % b));

        // Operadores de comparación
        System.out.println("Mayor que: " + (a > b));
        System.out.println("Menor que: " + (a < b));
        System.out.println("Igual a: " + (a == b));
        System.out.println("No igual a: " + (a != b));

        // Operadores lógicos
        boolean x = true;
        boolean y = false;
        System.out.println("AND lógico: " + (x && y));
        System.out.println("OR lógico: " + (x || y));
        System.out.println("NOT lógico: " + (!x));

        // Operadores de asignación
        int c = a;
        System.out.println("Asignación: " + c);

        // Operadores de bits
        System.out.println("AND bit a bit: " + (a & b));
        System.out.println("OR bit a bit: " + (a | b));
        System.out.println("XOR bit a bit: " + (a ^ b));
        System.out.println("Desplazamiento a la izquierda: " + (a << 2));
        System.out.println("Desplazamiento a la derecha: " + (a >> 2));
        
        // Operadores combinados de asignación
        a += b;
        System.out.println("Suma y asignación: " + a);
        a -= b;
        System.out.println("Resta y asignación: " + a);
        a *= b;
        System.out.println("Multiplicación y asignación: " + a);
        a /= b;
        System.out.println("División y asignación: " + a);
        a %= b;
        System.out.println("Módulo y asignación: " + a);

        // Estructuras de control
        // Condicionales
        if (a > b) {
            System.out.println("a es mayor que b");
        } else {
            System.out.println("a no es mayor que b");
        }

        // Iterativas
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteración: " + i);
        }

        // Excepciones
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[4]);
        } catch (Exception e) {
            System.out.println("Algo salió mal.");
        }
		
		// Concatenar cadenas
		String cadena1 = "Operadores";
		String cadena2 = "estructuras de control";
		
		System.out.println(cadena1 + " y " + cadena2);
		
		/*
		 * Crea un programa que imprima por consola todos los números comprendidos
		 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
		 */
		System.out.println("Números pares excepto 16 y múltiplos de 3:");
		for (int i = 10; i <= 55; i++) {
			if ((i % 2 == 0) && i !=16 && (i % 3 != 0)) {
				System.out.println(i);
			}
		}
		
	}

}
