public class llonardo798 {

    public static void main(String[] args) {
        // 1. Tipos de operadores por categoría:

        // 1. Operadores Aritméticos:

        int suma = 5 + 5 + 5; // Suma
        System.out.println(suma); // Imprime 15
        int resta = 10 - 5; // Resta
        System.out.println(resta); // Imprime 5
        int multiplicacion = 5 * 5; // Multiplicación
        System.out.println(multiplicacion); // Imprime 25
        int division = 10 / 2; // División
        System.out.println(division); // Imprime 5
        int modulo = 10 % 3; // Módulo (resto o sobrante de la división) 10 % 3 = 1 se puede considerar como
                             // 10/3 = 3 y sobra 1
        System.out.println(modulo); // Imprime 1
        suma++; // Incremento en 1
        System.out.println(suma); // Imprime 16
        resta--; // Decremento en 1
        System.out.println(resta); // Imprime 4

        // 2. Operadores de Asignación:

        String nombre = "Leonardo"; // Asignación simple: =
        System.out.println(nombre); // Imprime "Leonardo"
        suma += 5; // Suma y asignación
        System.out.println(suma); // Imprime 21
        resta -= 5; // Resta y asignación
        System.out.println(resta); // Imprime -1
        multiplicacion *= 5; // Multiplicación y asignación
        System.out.println(multiplicacion); // Imprime 125
        division /= 2; // División y asignación
        System.out.println(division); // Imprime 2 - el valorse recorta en el decimal porque es int y no float
        modulo %= 3; // Módulo y asignación
        System.out.println(modulo); // Imprime 1 porque 10 % 3 = 0.99999... y se redondea a 1 por ser int

        // 3. Operadores de Comparación:

        boolean igual = 5 == 5; // Igual a
        System.out.println(igual); // Imprime true - 5 es igual a 5
        boolean diferente = 5 != 5; // Diferente de
        System.out.println(diferente); // Imprime false - 5 no es diferente de 5
        boolean mayor = 10 > 5; // Mayor que
        System.out.println(mayor); // Imprime true - 10 es mayor que 5
        boolean menor = 5 < 10; // Menor que
        System.out.println(menor); // Imprime true - 5 es menor que 10
        boolean mayorIgual = 10 >= 5; // Mayor o igual que
        System.out.println(mayorIgual); // Imprime true - 10 es mayor o igual que 5
        boolean menorIgual = 5 <= 10; // Menor o igual que
        System.out.println(menorIgual); // Imprime true - 5 es menor o igual que 10

        // 4. Operadores Lógicos:

        boolean and = true && true; // AND lógico - ambas condiciones deben ser verdaderas
        System.out.println(and); // Imprime true
        boolean or = true || false; // OR lógico - al menos una condición debe ser verdadera
        System.out.println(or); // Imprime true
        boolean not = !true; // NOT lógico - niega la condición
        System.out.println(not); // Imprime false

        // 5. Operadores Bit a Bit (a nivel de bits):

        // AND bit a bit & - valida los numeros bit a bit como un AND.
        // Si compara 0 y 0 = 0, 0 y 1 = 0, 1 y 0 = 0, 1 y 1 = 1
        int a = 60; // En binario: 0011 1100
        int b = 13; // En binario: 0000 1101
        int resultadoAnd = a & b;
        System.out.println(resultadoAnd); // Resultado: 0000 1100 (Imprime 12 en decimal)
        // Explicación:
        // 0011 1100 - Valor a
        // 0000 1101 - Valor b
        // --------- & (AND)
        // 0000 1100 - 12 en decimal

        // OR bit a bit: | - valida los numeros bit a bit como un OR.
        // Si compara 0 y 0 = 0, 0 y 1 = 1, 1 y 0 = 1, 1 y 1 = 1
        int resultadoOr = a | b;
        System.out.println(resultadoOr); // Resultado: 0011 1101 (Imprime 61 en decimal)
        // Explicación:
        // 0011 1100
        // 0000 1101
        // --------- | (OR)
        // 0011 1101 - 61 en decimal

        // XOR bit a bit: ^ - valida los numeros bit a bit como un XOR.
        // Si compara 0 y 0 = 0, 0 y 1 = 1, 1 y 0 = 1, 1 y 1 = 0
        int resultadoXor = a ^ b;
        System.out.println(resultadoXor); // Resultado: 0011 0001 (Imprime 49 en decimal)
        // Explicación:
        // 0011 1100
        // 0000 1101
        // --------- ^ (XOR)
        // 0011 0001

        // Complemento bit a bit: ~ - cambia los bits de 0 a 1 y de 1 a 0
        a = 60; // En binario: 0011 1100
        int resultadoComplemento = ~a;
        System.out.println(resultadoComplemento); // Resultado: 1100 0011 (Imprime 195 en decimal)
        // Explicación:
        // 0011 1100 - Valor a = 60
        // --------- ~ (Complemento)
        // 1100 0011 - 195 en decimal

        // Desplazamiento a la izquierda: << - desplaza los bits a la izquierda
        a = 33; // En binario: 0010 0001
        int resultadoDesplazamientoIzquierda = a << 2;
        System.out.println(resultadoDesplazamientoIzquierda); // Resultado: 1000 0100 (132 en decimal)
        // Mover el número 33 dos posiciones a la izquierda.
        // moviendo los bits en 1 dos posiciones a la izquierda
        // Explicación:
        // 0010 0001 - Valor a = 33
        // --------- << (Desplazamiento a la izquierda)
        // 1000 0100 - 132 en decimal

        // Desplazamiento a la derecha: >> - desplaza los bits a la derecha
        a = 33; // En binario: 0010 0001
        int resultadoDesplazamientoDerecha = a >> 2;
        System.out.println(resultadoDesplazamientoDerecha); // Resultado: 0000 1000 (8 en decimal)
        // Mover el número 33 dos posiciones a la derecha.
        // moviendo los bits en 1 dos posiciones a la derecha
        // Explicación:
        // 0010 0001 - Valor a = 33
        // --------- >> (Desplazamiento a la derecha)
        // 0000 1000 - 8 en decimal

        // Desplazamiento a la derecha sin signo: >> - desplaza los bits a la derecha
        // sin importar si el numero es positivo o negativo para lo cual agrerga 0 a
        // la izquierda
        a = -10; // En binario (complemento a dos): 1111 1111 1111 1111 1111 1111 1111 0110
        int resultadoDesplazamientoIzquierdaSinSigno = a >>> 1;
        System.out.println(resultadoDesplazamientoIzquierdaSinSigno); // Resultado: 0111 1111 1111 1111 1111 1111 1111
                                                                      // 1011 (2147483643 en decimal)

        // 6. Operadores Ternarios:

        // Operador condicional ternario: ?:
        a = 5;
        int edad = (a == 10) ? 10 : 20; // Si a es igual a 10, entonces edad es igual a 10, de lo contrario, edad es
                                        // igual a 20
        System.out.println(edad); // Imprime 20

        // 7. Otros Operadores:

        String nombreCompleto = "Leonardo " + "Aedo"; // Concatenación de cadenas
        System.out.println(nombreCompleto); // Imprime "Leonardo Aedo"
        byte[] bytes = nombreCompleto.getBytes(); // Operador de acceso a miembros de clase "."
        System.out.println(bytes); // Imprime [B@6d06d69c
        int[] numeros = { 1, 3, 7, 2, 5 };
        int numero = numeros[2]; // Operador de acceso a elementos de arreglo "[]"
        System.out.println(numero); // Imprime 7
        double numeroDecimal = 10.5;
        int numeroEntero = (int) numeroDecimal; // Operador de cast (conversión de tipos)
        System.out.println(numeroEntero); // Imprime 10 - se recorta el decimal porque se convierte de double a int
        boolean esInstancia = nombre instanceof String; // Operador instanceof (verifica si un objeto es una instancia
        // de una clase) esInstancia devuelve true si nombre es una instancia de la
        // clase String, de lo contrario, devuelve false
        System.out.println(esInstancia); // Imprime true ya que nombre es una instancia de la clase String

        // DIFICULTAD EXTRA - Crea un programa que imprima por consola todos los números
        // comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni
        // múltiplos de 3.
        System.out.println("Números pares entre 10 y 55 que son pares, que no son 16 y no es múltiplos de 3:");
        for (int i = 10; i < 56; i++) {
            if ( i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }

}
