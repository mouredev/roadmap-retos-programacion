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
public class Main {


    public static void main(String[] args) {
        int num1 = 73;
        int num2 = 42;
        double num3 = 9.0;
        double nume4 = 7.0;
        String var1 = "coca ";
        String var2 = "- cola";
        boolean verdadero = true;
        boolean falso = false;
        int a = 73, b = 73, c = 3, d = 5;

        /*
        Operacioes aritméticos
         */
        // Concatenación de cadenas y/o suma 	+
        System.out.println(num1 + num2);
        System.out.println(var1 + var2);
        // Resta
        System.out.println(num1 - num2);
        //División entera
        System.out.println(num1 / num2);
        // División real
        System.out.println(num3 / nume4);
        // Resto o residuo
        System.out.println(num1 % num2);
        // Potencia Math,pow(base, exponente)
        System.out.println(Math.pow(num3, nume4));
        // Incremento ++
        System.out.println("42 incremento en 1 =" + (++ num2));
        // Decremento --
        System.out.println("73 Decremento en 1 =" + (-- num1));
        /*
        Operadores de Negación y Comparación
        */
        // Negación !
        System.out.println("Negacion " + (!verdadero));
        // Igualdad ==
        System.out.println("Igualdad, b igual que a " + (b == a));
        // Desigualdad 	!=
        System.out.println("Desigualdad, 73 no es igual 74 " + (a != num1));
        // Mayor que 	>
        System.out.println("73 mayor que 43 " + (num1 > num2));
        // Menor que 	<
        System.out.println("43 menor que 73 " + (num2 < num1));
        // Mayor o igual que 	>=
        System.out.println("73 mayor o igual que 73 " + (a >= num1));
        // Menor o igual que 	<=
        System.out.println("73 menor o igual que 73 " + (num1 <= b));
        /*
        Operadores Lógicos
        */
        // AND lógico 	&&
        System.out.println("ambos son verdaderos?: " + (verdadero && falso));
        // OR lógico 	||
        System.out.println("uno es verdader?: " + (verdadero || falso));
        /*
        Operadores Bit a Bit
        */
        // AND bit a bit 	&
        System.out.println("\"5 binario = 101, 3 binari0 = 011\"");
        System.out.println("Resultado: 001 (equivalente a 1 en decimal ) " + (c & d));
        // OR bit a bit 	|
        System.out.println("Resultado: 111 (equivalente a 7 en decimal )" + (c | d));
        // XOR bit a bit 	^
        System.out.println("Resultado: 110 (equivalente a 6 en decimal )" + (c ^ d));
        // Complemento bit a bit    ~
        System.out.println("Complemento bit a bit: " + (~c));
        // Desplazamiento izquierdo     <<
        System.out.println("Desplazamiento izquierdo: " + (d << 1));
        // Desplazamiento derecho    >>
        System.out.println("Desplazamiento derecho: " + (d >> 1));
        // Desplazamiento sin signo 	>>>
        System.out.println("Desplazamiento sin signo: " + (c >>> 1));
        /*
        Operadores de Asignación
         */
        // Asignación    =
        System.out.println("asignacion " +(a = b));
        // Asignación con suma	 +=
        System.out.println("Asignación con suma: " + (b += c));
        // Asignación con resta  -=
        System.out.println("Asignación con resta: " + (a -= c));
        // Asignación con multiplicación 	*=
        System.out.println("Asignación con multiplicacion: " + (a *= c));
        // Asignación con división 	/=
        System.out.println("Asignación con división: " + (a /= c));
        // Asignación con resto 	%=
        System.out.println("Asignación con resto: " + (a %= c));
        // Asignación con desplazamiento izquierdo 	<<=
        System.out.println("Asignación con desplazamiento izquierdo: " + (a <<= c));
        // Asignación con desplazamiento derecho 	>>=
        System.out.println("Asignación con desplazamiento derecho: " + (a >>= c));
        // Asignación con desplazamiento sin signo 	>>>=
        System.out.println("Asignación con desplazamiento sin signo: " + (b >>>= c));
        // Asignación con AND bit a bit 	&=
        System.out.println("Asignación con AND bit a bit: " + (a &= c));
        // Asignación con OR bit a bit 	|=
        System.out.println("Asignación con OR bit a bit: " + (a |= c));
        //    Asignación con XOR bit a bit 	^=
        System.out.println("Asignación con XOR bit a bit: " + (b ^= c));
        /*
        Otros Operadores
         */
        // Operador ternario 	? :
        int valor = (a > b) ? a : b;
        System.out.println("Operador ternario: " + valor);
        // Condicionales
        int myInt1 = 5;
        int myInt2 = 5;
        int myInt3 = 4;
        // if
        if (myInt1 == myInt2) {
            System.out.println("ok");
        }

        //if-else
        if (myInt1 == myInt3) {
            System.out.println("ok");
        } else {
            System.out.println("error");
        }
        // if-else-if
        if (myInt1 == myInt2) {
            System.out.println("ok");
        } else {
            System.out.println("error");
        }
        if (myInt2 >= myInt3) {
            System.out.println("es mayor");
        }
        // switch
        int opcion = 2;

        switch (opcion) {
            case 1:
                System.out.println("Seleccionaste la opción 1");
                break;
            case 2:
                System.out.println("Seleccionaste la opción 2");
                break;
            case 3:
                System.out.println("Seleccionaste la opción 3");
                break;
            default:
                System.out.println("Opción no válida");
        }
        // Iterativas

        // for
        for (int i = 0; i <= 10; i++) {
            System.out.print(i);
        }
        int contador = 0;
        while (contador < 6) {
            System.out.println("numero " + contador);
            contador++;
        }
        // do while
        do {
            int num5 = 5;
            num5++;
            System.out.println(num5);
            if (num5 >= 6) {
                break;
            }
        } while (true);
        // try catch
        try {
            int dividendo = 10;
            int divisor = 0;

            int resultado = dividendo / divisor;
            System.out.println("Resultado de la división: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: División por cero no permitida. Mensaje de la excepción: " + e.getMessage());

        }
        // try catch finally
        try {
            int di = 10;
            int divis = 0;

            int result = di / divis;
            System.out.println("Resultado de la división: " + result);
        } catch (ArithmeticException e){
            System.out.println("Error2: División por cero no permitida. Mensaje de la excepción: " + e.getMessage());
        }
        finally {
            System.out.println("java Dev");
        }

    }
        /*
        reto extra
         */
        for (int i = 10; i <= 55; i++){
            if (i % 2 == 0 && i != 16 && i % 3 != 0)
                System.out.println(i);
        }

    }
}