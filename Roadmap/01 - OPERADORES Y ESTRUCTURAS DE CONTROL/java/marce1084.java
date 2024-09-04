public class marce1084 {
    public static void main(String[] args) {
        int a = 3;
        int b = 7;
        boolean c = true;
        boolean d = false;

        //Operadores Aritméticos
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicacion: " + (a * b));
        System.out.println("Division: " + (a / b));
        System.out.println("Modulo: " + (a % b));

        //Operadores Lógicos
        System.out.println("AND &&: " + (c && d));
        System.out.println("OR ||: " + (c || d));
        System.out.println("Not !c: " + !c);
        System.out.println("Not !d: " + !d);

        //Operadores de Comparación
        System.out.println("Igual a: " + (a == b));
        System.out.println("Mayor que: " + (a > b));
        System.out.println("Menor que: " + (a < b));
        System.out.println("Distinto a: " + (a != b));
        System.out.println("Mayor o igual a: " + (a >= b));
        System.out.println("Menor o igual a: " + (a <= b));

        //Operadores de asignación
        System.out.println("Asignación y suma: " + (a += 1));
        System.out.println("Asignación y resta: " + (b -= 1));
        System.out.println("Asignación y multiplicación: " + (a *= 2));
        System.out.println("Asignación y division: " + (a /= 2));
        System.out.println("Asignación y modulo: " + (a %= 2));
        System.out.println("Asignación: " + (a = 5));
        System.out.println("Asignación y AND bit a bit: " + (a &= 3));
        System.out.println("Asignación y OR bit a bit: " + (a |= 3));

        //Operadores Bits
        System.out.println("AND BIT: " + (c & d));
        System.out.println("OR BIT: " + (c | d));
        System.out.println("XOR BIT: " + (c ^ d));
        System.out.println("NOT BIT: " + ~a);
        System.out.println("Desplazamiento izquierda: " + (a << 1 ));
        System.out.println("Desplazamiento derecha: " + (a >> 1 ));

        //Operadores indentidad
        String str1 = new String("Hola");
        String str2 = new String("Hola");
        System.out.println("Referencia de igualdad: " + (str1 == str2));
        System.out.println("Referencia de desigualdad: " + (str1 != str2));
        System.out.println("Comparacion de contenido: " + (str1.equals(str2)));

        /*Estructuras de control*/

        //Condicionales
        int edad = 17;
        if (edad > 18) {
            System.out.println("Es mayor de edad");
        } else System.out.println("La edad debe ser mayor o igual a 18");

        //Iterativas
        for (int i = 0; i <= 10; i++) {
            System.out.println("Numero: " + i);
        }

        int i = 11;
        while (i > 0){
            System.out.println("Numero: " + i);
            i--;
        }

        //Excepciones
        try {
            System.out.println(10/0);
        } catch (ArithmeticException e) {
            System.out.println("Se produjo error por la división");
        } finally {
            System.out.println("Finalizó el manejo de excepciones");
        }

        //Ramificación
        for (int j = 0; j <= 7 ; j++) {
            if (j == 3 ){
                break;
            }
            System.out.println("Numero: " + j);
        }

        //EXTRA
        /*Crea un programa que imprima por consola todos los números comprendidos
        entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
        Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.*/

        for (int j = 10; j <= 55 ; j++) {
            if (j %2 == 0 && j != 16 && j%3 != 0){
                System.out.println("Number: " + j);
            }
        }
    }
}