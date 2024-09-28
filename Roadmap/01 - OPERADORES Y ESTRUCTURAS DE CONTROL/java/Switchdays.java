/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
public class Switchdays {

    public static void main(String[] args) {

        // aritmeticos: suma (+), resta (-), multiplicación (*), división (/)

        int number1 = 5;
        int number2 = 10;
        int suma = number1 + number2;
        System.out.println(suma);
        int resta = number1 - number2;
        System.out.println(resta);
        int multiplicacion = number1 * number2;
        System.out.println(multiplicacion);
        double division = (double) number1 / number2;
        System.out.println(division);

        // comparadores: igual (==), mayor (>), menor (<), mayor o igual (>=), menor o igual (<=)

        boolean result1 = number1 == number2;
        System.out.println(result1);
        boolean result2 = number1 <= number2;
        System.out.println(result2);
        boolean result3 = number1 >= number2;
        System.out.println(result3);
        boolean result4 = number1 > number2;
        System.out.println(result4);
        boolean result5 = number1 < number2;
        System.out.println(result5);

        // lógicos: and(&&), or (||), not (!)

        int edad = 14;
        boolean carnetJoven1 = edad < 25 && edad > 15;
        System.out.println(carnetJoven1);
        boolean carnetJoven2 = edad < 25 || edad == 15;
        System.out.println(carnetJoven2);
        boolean carnetJoven3 = !carnetJoven2;
        System.out.println(carnetJoven3);

        // Estructuras de control:

        //if
        boolean esMayorDeEdad = edad >= 18;
        boolean esMenorDeEdad = edad < 18;
        if (esMayorDeEdad) {
            System.out.println("Es mayor de edad");
        }
        if (esMenorDeEdad) {
            System.out.println("Es menor de edad");
        }

        //ifElse
        if (edad >= 18) {
            System.out.println("Es mayor de edad");
        } else {
            System.out.println("Es menor de edad");
        }

        //ifElseif
        String dia = "Sabado";
        if (dia.equals("Lunes")) {
            System.out.println("animo con la semana maquina monstruous");
        } else if ("dia".equals("Martes")) {
            System.out.println("Martes con M de me besas bb");
        } else if ("dia".equals("Miercoles")) {
            System.out.println("Puto miercoles");
        } else if ("dia".equals("Jueves")) {
            System.out.println("Venga que ya queda poco");
        } else if ("dia".equals("Viernes")) {
            System.out.println("Hoy no es jueves mamawevo, HOY ES VIERNESSS!!!!");
        }else if ("dia".equals("Sabado")) {
            System.out.println("Buen finde");
        } else if ("dia".equals("Domingo")) {
            System.out.println("Buen finde");
        } else {
            System.out.println("El día introducido no es válido");
        }

        //switch
        switch (dia) {
            case "Lunes":
                System.out.println("animo con la semana maquina monstruous");
                break;
            case "Martes":
                System.out.println("Martes con M de me besas bb");
                break;
            case "Miercoles":
                System.out.println("Puto miercoles");
                break;
            case "Jueves":
                System.out.println("Venga que ya queda poco");
                break;
            case "Viernes":
                System.out.println("Hoy no es jueves mamawevo, HOY ES VIERNESSS!!!!");
                break;
            case "Sabado":
                System.out.println("Buen finde");
                break;
            case "Domingo":
                System.out.println("Buen finde");
                break;
            default:
                System.out.println("El día introducido no es válido");
        }

        // while
        int contador = 0;
        while (contador < 10) {
            System.out.println(contador);
            contador++;
            if (contador == 5) {
                break;
            }
        }

        //doWhile
        int contador2 = 10;
        do {
            System.out.println(contador2);
            contador2--;
        } while (contador2 > 10);

        //for
        for (int i = 0; i < 10; i++) {
            System.out.println("El valor de i es " + i);
        }

        //forEach
        String[] names = {"Víctor", "Natalia", "Miliki"};
        for (String name : names) {
            System.out.println(name);
        }


        //Ejercicio opcional: Crea un programa que imprima por consola todos los números comprendidos
        //entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

        for (int i = 10; i <=55; i++) {

            if (i != 16 && i % 2 == 0 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }
}
