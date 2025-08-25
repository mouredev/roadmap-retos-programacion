/**
 * #01 OPERADORES Y ESTRUCTURAS DE CONTROL
 * @author clarancedev
 * @version 1.0
 * @date 2025-04-05
 */

public class Clarancedev {

    public static void main(String[] args) {

        //VARIABLES
        double double1 = 7.0;
        double double2 = 9.0;
        double double3 = 13.0;
        int int1 = 5;
        int int2 = 10;
        String str = "Hola";

        //OPERADORES

            //ARITMETICOS
            System.out.println("Suma: " + double1 + " + " + double2 + " = " + (double1 + double2));
            System.out.println("Resta: " + double1 + " - " + double2 + " = " + (double1 - double2));
            System.out.println("Multiplicación: " + double1 + " * " + double2 + " = " + (double1 * double2));
            System.out.println("División: " + double1 + " / " + double2 + " = " + (double1 / double2));
            System.out.println("Módulo: " + double1 + " % " + double2 + " = " + (double1 % double2));

            //LÓGICOS
            System.out.println("AND: " + double1 + " > " + double2 + " && " + double1 + " < " + double3 + " = " + (double1 > double2 && double1 < double3));
            System.out.println("OR: " + double1 + " > " + double2 + " || " + double1 + " < " + double3 + " = " + (double1 > double2 || double1 < double3));
            System.out.println("NOT: !" + double1 + " > " + double2 + " = " + !(double1 > double2));

            //DE COMPARACIÓN
            System.out.println("Mayor que: " + double1 + " > " + double2 + " = " + (double1 > double2));
            System.out.println("Menor que: " + double1 + " < " + double2 + " = " + (double1 < double2));
            System.out.println("Mayor o igual que: " + double1 + " >= " + double2 + " = " + (double1 >= double2));
            System.out.println("Menor o igual que: " + double1 + " <= " + double2 + " = " + (double1 <= double2));
            System.out.println("Igual a: " + double1 + " == " + double2 + " = " + (double1 == double2));
            System.out.println("Diferente de: " + double1 + " != " + double2 + " = " + (double1 != double2));

            //INSTANCEOF
            boolean esString = str instanceof String;
            System.out.println("El objeto str \"" + str + "\" es una instancia de String? " + esString);

            //DE ASIGNACION
            System.out.println("Asignación simple: " + double1 + " = " + double2 + " = " + (double1 = double2));
            System.out.println("Asignación suma: " + double1 + " += " + double2 + " = " + (double1 += double2));
            System.out.println("Asignación resta: " + double1 + " -= " + double2 + " = " + (double1 -= double2));
            System.out.println("Asignación multiplicación: " + double1 + " *= " + double2 + " = " + (double1 *= double2));
            System.out.println("Asignación división: " + double1 + " /= " + double2 + " = " + (double1 /= double2));
            System.out.println("Asignación módulo: " + double1 + " %= " + double2 + " = " + (double1 %= double2));
            System.out.println("Asignación AND: " + int1 + " &= " + int2 + " = " + (int1 &= int2));
            System.out.println("Asignación OR: " + int1 + " |= " + int2 + " = " + (int1 |= int2));
            System.out.println("Asignación XOR: " + int1 + " ^= " + int2 + " = " + (int1 ^= int2));
            System.out.println("Asignación desplazamiento a la izquierda: " + int1 + " <<= " + int2 + " = " + (int1 <<= int2));
            System.out.println("Asignación desplazamiento a la derecha: " + int1 + " >>= " + int2 + " = " + (int1 >>= int2));
            System.out.println("Asignación desplazamiento a la derecha sin signo: " + int1 + " >>>= " + int2 + " = " + (int1 >>>= int2));

            //RESETEANDO VALORES
            double1 = 7.0;
            int1 = 5;

            //UNARIOS
            System.out.println("Unario positivo: +" + double1 + " = " + (+double1));
            System.out.println("Unario negativo: -" + double1 + " = " + (-double1));
            System.out.println("Incremento: ++" + double1 + " = " + (++double1));
            System.out.println("Decremento: --" + double1 + " = " + (--double1));
            System.out.println("Incremento postfijo: " + double1 + "++ (cambio aplicado después de la operación)");
            System.out.println("Decremento postfijo: " + double1 + "-- (cambio aplicado después de la operación)");

            //DE TIPO BITWISE
            System.out.println("AND bitwise: " + int1 + " & " + int2 + " = " + (int1 & int2));
            System.out.println("OR bitwise: " + int1 + " | " + int2 + " = " + (int1 | int2));
            System.out.println("XOR bitwise: " + int1 + " ^ " + int2 + " = " + (int1 ^ int2));
            System.out.println("Complemento bitwise: ~" + int1 + " = " + (~int1));

            //DE DESPLAZAMIENTO
            System.out.println("Desplazamiento a la izquierda: " + int1 + " << " + int2 + " = " + (int1 << int2));
            System.out.println("Desplazamiento a la derecha: " + int1 + " >> " + int2 + " = " + (int1 >> int2));
            System.out.println("Desplazamiento a la derecha sin signo: " + int1 + " >>> " + int2 + " = " + (int1 >>> int2));

            //TERNARIO
            String resultado = (double1 > double2) ? "es true" : "es false";
            System.out.println("Resultado: " + resultado);


        //ESTRUCTURAS DE CONTROL

            //CONDICIONALES (if, if-else, if-else-if, switch)
            if (int1 > 0) {
                System.out.println("La condición int1 > 0 se cumple.");
            }

            if (int1 > 0) {
                System.out.println("La condición int1 > 0 se cumple.");
            } else {
                System.out.println("La condición int1 > 0 no se cumple.");
            }

            if (int1 > 0) {
                System.out.println("La condición int1 > 0 se cumple.");
            } else if (int1 < 0) {
                System.out.println("La condición int1 < 0 se cumple.");
            } else {
                System.out.println("Ninguna de las condiciones anteriores se cumple.");
            }

            switch (int1) {
                case 0:
                    System.out.println("La condición int1 = 0 se cumple.");
                    break;
                case 1:
                    System.out.println("La condición int1 = 1 se cumple.");
                    break;
                default:
                    System.out.println("Ninguna de las condiciones anteriores se cumple.");
                    break;
            }

            //ITERATIVAS / BUCLES (for, while, do-while)
            for (int i = 1; i < 5; i++) {
                System.out.println("Iteración for: " + (i));
            }

            int1 = 0;
            while (int1 < 5) {
                System.out.println("Iteración while: " + int1);
                int1++;
            }

            int1 = 0;
            do {
                System.out.println("Iteración do-while: " + int1);
                int1++;
            } while (int1 < 5);

            //EXCEPCIONES (try-catch-finally)
            try {
                int division = int1 / 0;
            } catch (ArithmeticException e) {
                System.out.println("Error: La división por 0 es matemáticamente imposible.");
            } finally {
                System.out.println("Ejecutando el bloque finally.");
            }

            //BREAK
            for (int i = 1; i < 10; i++) {
                if (i == 5) {
                    System.out.println("Se ha alcanzado el valor 5, saliendo del bucle.");
                    break;
                }
                System.out.println("Iteración for con break: " + (i));
            }

            //CONTINUE
            for (int i = 1; i < 10; i++) {
                if (i == 5) {
                    System.out.println("Se ha alcanzado el valor 5, saltando esta iteración.");
                    continue;
                }
                System.out.println("Iteración for con continue: " + (i));
            }

        //DIFICULTAD EXTRA
            System.out.println("Entre el rango de números del 10 al 55, estos son los números pares (excluyendo el 16) que no son múltiplos de 3:");
            for (int i = 10; i < 56; i++) {
                if ((i % 2 == 0) && (i != 16) && (i % 3 != 0)) {
                    System.out.println(i);
                }
            }


    }
}