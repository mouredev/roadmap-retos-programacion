public class ricarditodev {
    public static void main(String[] args) {
        //ejemplos utilizando todos los operadores de Java
        //operadores aritméticos

        //operador suma (adición)
        int suma = 1 + 1;

        //operador resta (sustracción)
        int resta = 2 - 1;

        //operador multiplicación
        int multi = 2 * 2;

        //operador división
        int division = 10 / 5;

        //operador módulo o resto (resto de la división)
        double modulo = 11 % 5;

        //operador incremento - incrementa el valor en 1
        int incremento = ++suma;

        //operador decremento - decrementa el valor en 1
        int decremento = --suma;

        //----------------------------------------------------------------------------

        //operadores de asignación
        //operador de asignación simple - asigna un valor o dato a una variable
        double x = 5;

        //operador suma y asigna - suma el valor de la variable con lo que está después del += y lo asigna a la misma variable
        x += 3;

        //operador resta y asigna - resta el valor de la variable con lo que está después del -= y lo asigna a la misma variable
        x -= 1;

        //operador múltiplica y asigna - ídem
        x *= 5;

        //operador división y asigna - ídem
        x /=  2;

        //operador módulo y asigna - ídem
        x %= 5;

        //----------------------------------------------------------------------------//

        //operadores relacionales o de comparación - devuelve siempre un boolean (true o false)
        //operador igual a
        System.out.println(x == suma);

        //operador diferente de
        System.out.println(x != suma);

        //operador mayor que
        System.out.println(x > suma);

        //operador menor que
        System.out.println(x < suma);

        //operador mayor o igual que
        System.out.println(x >= suma);

        //operador menor o igual que
        System.out.println(x <= suma);

        //----------------------------------------------------------------------------//

        //operadores lógicos - siempre devuelve un boolean (true o false)
        //operador AND (&&) retorna true solo si ambas condiciones son true
        System.out.println(suma < 10 && resta < 10);

        //operador OR (||) retorna true si al menos una condicion es true
        System.out.println(suma > 0 || suma > 10);

        //operador NOT (!) invierte el valor booleano
        System.out.println(!(multi == 4 || multi > 0));

        //----------------------------------------------------------------------------//

        //operadores bit a bit (bitwise) - operan sobre los bits de enteros (no variables double ni float)
        //operador AND (&) - compara cada bit de dos números, si ambos bits son 1 devuelve 1, sino devuelve 0
        int a = 6; //110
        int b = 3; //011
        int c = a & b;
        System.out.println(c);

        //operador OR (|) - compara cada bit de dos números, si al menos un bit es 1 devuelve 1, si ambos son 0 devuelve 0
        int aa = 6; //110
        int bb = 3; //011
        int cc = aa | bb;
        System.out.println(cc); // 7 (111)

        //operador XOR (^) (OR exclusivo) - compara cada bit de dos números y devuelve 1 si los bits son diferentes
        int aaa = 6; //110
        int bbb = 3; //011
        int ccc = aaa ^ bbb;
        System.out.println(ccc); // 5 (101)

        //operador NOT (~) - invierte todos los bits de un número - para cualquier entero n lo converte en su opuesto menos 1 / -(n + 1)
        int aNegativo = ~a; // 00000000 00000000 00000000 00000110 --> 11111111 11111111 11111111 11111001
        // ~6 = -(6 + 1) = -7
        System.out.println(aNegativo);

        /*operador desplazamiento a la izquierda (<<)
        mueve todos los bits de un número hacia la izquierda un número determinado de posiciones
        los bits que se “abren” a la derecha se llenan con 0.
        cada desplazamiento hacia la izquierda equivale a multiplicar por 2
        n << 1  → n * 2
        n << 2  → n * 4
        n << 3  → n * 8
        */

        int tres = 3; // 3 en binario = 00000011
        int ejemplo = tres << 2; // desplazamos 2 posiciones a la izquierda --> 00001100
        System.out.println(ejemplo); // 00001100 == 12

        /*operador desplazamiento a la derecha con signo (>>)
        desplaza todos los bits hacia la derecha un número determinado de posiciones, el bit de signo (MSB) se mantiene y se copia a la izquierda
        es decir, extiende el signo
        matemáticamente, equivale a dividir entre 2^n y redondear hacia abajo (pero manteniendo el signo)
         */

        int veinte = 20; //20 = 00010100 en binario
        int ejemploVeinte = veinte >> 2; // desplazamos 2 posiciones a la derecha --> 00000101
        System.out.println(ejemploVeinte); //00000101 == 5

        int veinteNegativo = -20; //-20 = 11101100 en binario
        int  ejemploVeinteNegativo = veinteNegativo >> 2; //desplazamos 2 posiciones a la derecha --> 11111011
        System.out.println(ejemploVeinteNegativo); //11111011 == -5

        /*operador desplazamiento a la derecha sin signo (>>>)
        desplaza todos los bits hacia la derecha un número determinado de posiciones
        rellena con ceros a la izquierda, sin importar el signo
        no conserva el bit de signo
        eso significa que, si el número era negativo, se convierte en un número muy grande positivo
        porque el bit más a la izquierda deja de ser 1 (negativo) y pasa a ser 0 (positivo)
         */

        int veinteNegativoSinSigno = -20; //11111111 11111111 11111111 11101100   → -20
        int ejemploVeinteNegativoSinSigno = veinteNegativoSinSigno >>> 2; //desplazamos 2 posiciones a la derecha --> 00111111 11111111 11111111 11111011
        System.out.println(ejemploVeinteNegativoSinSigno); //ya no representa un número negativo, sino un positivo muy grande = 00111111 11111111 11111111 11111011 == 1073741819

        //----------------------------------------------------------------------------//

        //operador condicional (ternario) - Una forma compacta de un if-else
        //condicion ? valorSiTrue : valorSiFalse
        int velocidad = 60;
        String mensaje = velocidad > 100 ? "reduce la velocidad" : "continúa manejando";
        System.out.println(mensaje);

        //----------------------------------------------------------------------------//

        //operadores instanceof y new
        //instanceof → verifica si un objeto es de cierta clase
        //new → crea un nuevo objeto
        String s = new String("Hola");
        System.out.println(s instanceof String);

        //----------------------------------------------------------------------------//

        //ejemplos utilizando todas las estructuras de control de java
        //estructuras condicionales
        //estructura if
        boolean estoyAprendiendo = true;

        if (estoyAprendiendo) {
            System.out.println("no pares de aprender");
        }

        //estructura else
        boolean noEstoyAprendiendo = true;

        if (noEstoyAprendiendo) {
            System.out.println("ponte a aprender ya!");
        } else {
            System.out.println("no pares de aprender");
        }

        //estructura else-if
        boolean estoyAprendiendoPHP = false;
        boolean estoyAprendiendoJava = true;

        if (estoyAprendiendoPHP) {
            System.out.println("mejor ponte a aprender Java :P");
        } else if (estoyAprendiendoJava) {
            System.out.println("continúa aprendiendo Java");
        } else {
            System.out.println("aprende algún lenguaje");
        }

        //estructura switch
        int dayOfTheWeek = 5;
        switch (dayOfTheWeek) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println(false);
        }

        //----------------------------------------------------------------------------//

        //estructura iterativas
        //estructura for
        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }

        //estructura while
        int num = 5;
        while (num > 0) {
            System.out.println(num);
            num--;
        }

        //estructura do-while - ejecuta el loop una vez antes de comprobar si la condición es verdadera
        //si es verdadera sigue ejecutando el bucle hasta que sea falsa, y si al inicio es falsa de igual manera se ejecuta una vez
        int n = 0;
        do {
            System.out.println(n);
            n++;
        } while (n <= 5);

        //estructura for-each - para recorrer arrays o estructuras de datos
        String[] seniority = {"Junior", "Semi-Senior", "Senior"};
        for (String i : seniority) {
            System.out.println(i);
        }

        //----------------------------------------------------------------------------//

        //estructuras de salto
        //estructura break - interrumpe un bucle o un switch
        for (int i = 0; i <= 5; i++) {
            if (i == 3) {
                break;
            }
            System.out.println(i);
        }

        //estructura continue - salta a la siguiente iteración de un bucle, omitiendo el resto del código en la iteración actual
        for (int i = 0; i <= 5; i++) {
            if (i == 1) {
                continue;
            }
            System.out.println(i);
        }

        //estructura return - termina la ejecución de un método y, opcionalmente, devuelve un valor


        //----------------------------------------------------------------------------//

        //programa que imprime por consola todos los números comprendidos
        //entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

        for (int i = 10; i <= 55; i++) {
            if (i % 3 == 0) {
                continue;
            }

            if (i == 16) {
                continue;
            }

            if (i % 2 == 0) {
                System.out.println(i);
            }
        }
    }
}
