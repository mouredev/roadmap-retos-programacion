public class maldo2324 {
    public static void main(String[] args) {
        //Operadores y estructuras de control

        System.out.println("\n*** OPERADORES ***\n");
        System.out.println("* Operadores aritmeticos *\n");

        int num1 = 35;
        int num2 = 14;

        //Operadores Aritmeticos
        System.out.println("Suma (+): " + (num1 + num2));
        System.out.println("Resta (-): " + (num1 - num2));
        System.out.println("Multiplicacion (*): " + (num1 * num2));
        System.out.println("Division (+): " + (num1 / num2));
        System.out.println("modulo (+): " + (num1 / num2));

        //Operadores de Asignacion
        System.out.println("\n* Operadores de Asignacion *\n");
        num1 = 10;
        num2 = 5;
        System.out.println("Asignamos nuevo valor a num1 y num2 con (=) " + num1 + " , " + num2);
        System.out.println("suma y asignacion (+=) " + (num1 += 1));
        System.out.println("resta y asignacion (-=) " + (num1 -= 1));
        System.out.println("multiplicacion y asignacion (*=) " + (num1 *= 2));
        System.out.println("division y asignacion (/=) " + (num1 /= 2));
        System.out.println("modulo y asignacion (%=) " + (num1 /= 2));

        //Operadores de incremento y decremento
        System.out.println("\n* Operadores de incremento y decremento *\n");
        //Incremento
        int numIncremento = ++num1;
        System.out.println("num1 con PREincremento= " + numIncremento);
        numIncremento = num1++;
        System.out.println("num1 con POSTincremento= " + num1);
        //Decremento
        int numDecremento = --num1;
        System.out.println("PREdecremento = " + numDecremento);
        numDecremento = num1--;
        System.out.println("POSTdecremento = " + num1);

        //Operadores relacionales
        System.out.println("\n* Operadores relacionales *\n");

        System.out.println("Son Iguales?: " + (num1 == num2));
        System.out.println("num1 NO es Igual a num2?: " + (num1 != num2));
        System.out.println("num1 Mayor igual que num2?: " + (num1 >= num2));
        System.out.println("num1 Menor igual que num2?: " + (num1 <= num2));
        num1 = ++num1;
        System.out.println("num1 Mayor que num2?: " + (num1 > num2));
        System.out.println("num1 Menor que num2: " + (num1 < num2));

        //Operadores logicos
        System.out.println("\n* Operadores logicos *\n");
        boolean a = true;
        boolean b = true;
        System.out.println("AND(&&): " + (a && b));
        System.out.println("OR(||): " + (a || b));
        System.out.println("NOT(!): " + (!b));

        //Operadores bit a bit
        System.out.println("\n* Operadores bit a bit *\n");
        int num3 = 5; // 1111
        int num4 = 2; // 0011
        System.out.println("AND bit a bit: " + (num3 & num4));
        System.out.println("OR bit a bit: " + (num3 | num4));
        System.out.println("NOT bit a bit de : " + (~num4));
        System.out.println("XOR bit a bit de : " + (num3 ^ num4));
        System.out.println("Desplazamiento bit a bit a la izq de : " + (num3 << num4));
        System.out.println("Desplazamiento bit a bit a la der de : " + (num3 >> num4));
        System.out.println("Desplazamiento bit a bit a la izq de : " + (num3 >>> num4));

        //ESTRUCTURAS DE CONTROL
        System.out.println("\n*** EJERCICIO CON ESTRUCTURAS DE CONTROL ***\n");
        //Condicionales if, else if, else

        // Numero positivo
        if (num1 > 0) {
            System.out.println("El número es positivo.");
        } else if (num1 < 0) {
            System.out.println("El número es negativo.");
        } else {
            System.out.println("El número es cero.");
        }
        //Numero negativo
        num1 = -1;
        if (num1 > 0) {
            System.out.println("El número es positivo.");
        } else if (num1 < 0) {
            System.out.println("El número es negativo.");
        } else {
            System.out.println("El número es cero.");
        }
        //Numero es cero
        num1 = 0;
        if (num1 > 0) {
            System.out.println("El número es positivo.");
        } else if (num1 < 0) {
            System.out.println("El número es negativo.");
        } else {
            System.out.println("El número es cero.");
        }

        //Condicional Switch

        System.out.println("\n* Condicional Switch *\n");
        System.out.println("¿Que dia de la semana puedes descansar?\n");

        int diaDescanso = 8;

        switch (diaDescanso){
            case 1:
                System.out.println("Lunes");
            case 2:
                System.out.println("Martes");
            case 3:
                System.out.println("Miercoles");
            case 4:
                System.out.println("Jueves");
            case 5:
                System.out.println("Viernes");
            case 6:
                System.out.println("Sabado");
            case 7:
                System.out.println("Domingo");
            case 8:
                System.out.println("Ninguno, ponte a programar!");
                break;
            default:
                System.out.println("opcion no valida");

        }

        System.out.println("\n* Estructura de control de Bucles *");
        // for
        System.out.println("\nfor");
        for (int x = 0; x < 4; ++x){
            System.out.println("x = " + x);
        }
        //while
        System.out.println("\nwhile");
        int p = 0;
        while (p < 4){
            System.out.println("p = " + p);p++;
        };
        //do-while
        System.out.println("\ndo-while");
        int z = 0;
        do {
            System.out.println("z =" + z);
            z++;
        } while (z < 4);

        //break
        System.out.println("\nbreak");
        for (int y = 0; y < 10; y++) {
            if (y == 4) {
                break;
            }
            System.out.println("y = " + y);
        }

        //continue
        System.out.println("\ncontinue");
        for (int m = 0; m < 8; m++) {
            if (m % 2 == 0) {
                continue;
            }
            System.out.println("m = " + m);
        }

        System.out.println("\n* Estructura de control de Excepciones *");
        //try-catch
        System.out.println("\ntry-catch");
        try {
            int resultado = 10 / 0; // Intenta dividir por cero
            System.out.println("El resultado es: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: División por cero");
        }
        System.out.println("\ntry-catch-finally");
        try {
            int resultado = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("División por cero.");
        } finally {
            System.out.println("Operacion de division finalizada.");
        }
        System.out.println("\n*** EJERCICIO DIFICULTAD EXTRA ***\n");
        /* DIFICULTAD EXTRA (opcional):
        Crea un programa que imprima por consola todos los números comprendidos
        entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */

        for(int e = 10; e <= 55; e++) {
            if(e != 16 && (e % 3 != 0) &&(e % 2 == 0)) {
                System.out.println(e);
            }

            if(e == 55) System.out.println(e);
        }


    }
}
