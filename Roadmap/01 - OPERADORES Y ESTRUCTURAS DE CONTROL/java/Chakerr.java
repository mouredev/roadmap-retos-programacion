/**
 * EJERCICIO: - Crea ejemplos utilizando todos los tipos de operadores de tu
 * lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad,
 * pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer unos
 * diferentes) - Utilizando las operaciones con operadores que tú quieras, crea
 * ejemplos que representen todos los tipos de estructuras de control que
 * existan en tu lenguaje: Condicionales, iterativas, excepciones... - Debes
 * hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional): Crea un programa que imprima por consola todos
 * los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el
 * 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo
 * nuevo.
 */
public class Chakerr {

    public static void main(String[] args) {
        //Operadores aritmeticos
        int a = 5;
        int b = 8;
        //Suma
        System.out.println(a + b);
        //Resta
        System.out.println(a - b);
        //Multiplicación
        System.out.println(a * b);
        //Divicion
        System.out.println(a / b);
        //Módulo
        System.out.println(a % b);

        //Operadores Unarios
        //Positivo
        int c = 5;
        System.out.println(+c);
        //Negativo
        System.out.println(-c);
        //Incremento
        c++;
        System.out.println(c);
        ++c;
        System.out.println(c);
        //Decremento
        c--;
        System.out.println(c);
        --c;
        System.out.println(c);

        //Operadores Relacionales
        //Igual a
        if (5 == 5) {
            System.out.println("5 si es igual a 5");
        }
        //Diferente de
        if (5 != 3) {
            System.out.println("5 es diferente de 3");
        }
        //Mayor que
        if (5 > 3) {
            System.out.println("5 es mayor que tres");
        }
        //Menor que
        if (5 < 10) {
            System.out.println("5 es menor que tres");
        }
        //Mayor o igual que
        if (5 >= 5) {
            System.out.println("5 es igual a 5");
        }
        //Menor o igual que
        if (3 <= 5) {
            System.out.println("3 es menor a 5");
        }

        //Operadores Logicos
        //AND ( devuelve verdadero si ambos operandos son verdaderos)
        if (true && false) {
            System.out.println("verdadero");
        } else {
            System.out.println("falso");
        }
        //OR ( devuelve true si al menos uno de los operandos es verdadero)
        if (true || false) {
            System.out.println("verdadero");
        } else {
            System.out.println("falso");
        }
        //NOT (invierte el valor booleano)
        if (!true) {
            System.out.println("false");
        }

        //Operadores de asignación
        //Asignación simple
        int d = 10;
        System.out.println(d);
        //Asignación con suma
        d += 3;
        System.out.println(d);
        //Asignación con resta
        d -= 2;
        System.out.println(d);
        //Asignación con multiplicación
        d *= 2;
        System.out.println(d);
        //Asignación con division
        d /= 2;
        System.out.println(d);
        //Asignación con módulo
        d %= 2;
    }

}