public class JoseEsmil04 {
    public static void main(String[] args) {
        int num1 = 45;
        int num2 = 13;
        boolean a;
        boolean b;

        System.out.println("*-*-* Operadores Aritmeticos *-*-*\n");
        // Suma
        System.out.println("Suma (+): " + (num1 + num2));
        // Resta
        System.out.println("Resta (-): " + (num2 - num1));
        // Multiplicacion
        System.out.println("Multiplicacion (*): " + (num1 * num2));
        // Division
        System.out.println("Division (/): " + (num1 / num2));
        // Resto
        System.out.println("Resto (%): " + (num1 % num2));

        System.out.println("\n*-*-* Operadores de Asignacion *-*-*\n");
        // Asignacion basico
        num1 = 500;
        num2 = 1000;
        System.out.println("Despues de usar la asignacion(=) el num1: " + num1);
        // Asignacion compuesto con Suma
        System.out.println("Asignacion con suma (+=): " + (num1 += num2));
        // Asignacion compuesto con Resta
        System.out.println("Asignacion con resta (-=): " + (num1 -= num2));
        // Asignacion compuesto con Multiplicacion
        System.out.println("Asignacion con multiplicacion (*=): " + (num2 *= num1));
        // Asignacion compuesto con Division
        System.out.println("Asignacion con division (/=): " + (num2 /= num1));
        // Asignacion compuesto con Resto
        System.out.println("Asignacion con resto (%=): " + (num1 %= num2));

        System.out.println("\n*-*-* Operadores de Identidad *-*-*\n");
        // Operador de igualdad
        System.out.println("Igualdad: " + ("Esmil" == "Esmil"));
        // Operador de desigualdad
        System.out.println("Desigualdad: " + (23 != 44));

        System.out.println("\n*-*-* Operadores Logicos *-*-*\n");
        a = true;
        b = true;
        // Operador AND
        System.out.println("AND(&&): " + (a && b));
        // Operador OR
        a = true;
        b = false;
        System.out.println("OR(||): " + (a || b));
        // Operador NOT
        System.out.println("NOT(!): " + (!b));

        System.out.println("\n*-*-* Operadores de Comparacion *-*-*\n");
        num1 = 70;
        num2 = 43;
        // Mayor que
        System.out.println("Mayor que: " + (num1 > num2));
        // Menor que
        System.out.println("Menor que: " + (num2 < num1));
        // Mayor o Igual que
        System.out.println("Mayor o igual que: " + (num1 >= num1));
        // Menor o Igual que
        System.out.println("Menor o igual que: " + (num2 <= num1));

        System.out.println("\n*-*-* Operadores de Bits *-*-*\n");
        int num3 = 5; // 0000 0101
        int num4 = 3; // 0000 0011
        // AND bit
        System.out.println("AND bit a bit: " + (num3 & num4));
        // OR bit
        System.out.println("OR bit a bit: " + (num3 | num4));
        // NOT bit
        System.out.println("NOT bit a bit de m: " + (~num4));

        System.out.println("\n*-*-* Estructuras de control *-*-*\n");
        // Condicionales if, else if, else
        num1 = 100;
        num2 = 99;
        num3 = 101;

        if (num1 > num2) {
            System.out.println(num1 + " es mayor que " + num2);
        } else if (num2 <= num3){
            System.out.println(num2 + " a es menor o igual que " + num3);
        } else {
            System.out.println("Si lo de arriba no se cumple, llegamos aqui!");
        }

        // Condicional switch
        int opcion = 2;

        switch (opcion) {
            case 1:
                System.out.println("La opción es 1");
                break;
            case 2:
                System.out.println("La opción es 2");
                break;
            case 3:
                System.out.println("La opción es 3");
                break;
            default:
                System.out.println("Opción no válida");
        }

        // Iterativa While
        int vuelta = 0;

        while(vuelta < 5) {
            System.out.println("Vuelta! " + vuelta);

            vuelta++;
        }

        // Iterativa for
        for (int i = 0; i < 10; i++) {
            System.out.println("FOR " + i);
        }

        // Excepcion try catch
        try {
            int resultado = 10 / 0; // Intenta dividir por cero
            System.out.println("El resultado es: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: División por cero");
        }

        // DIFICULTAD EXTRA (opcional):
        // Crea un programa que imprima por consola todos los números comprendidos
        // entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
        for(int i = 10; i <= 55; i++) {
            if(i != 16 && (i % 3 != 0) && (i % 2 == 0)) {
                System.out.println(i);
            }

            if(i == 55) System.out.println(i);
        }
    }
}