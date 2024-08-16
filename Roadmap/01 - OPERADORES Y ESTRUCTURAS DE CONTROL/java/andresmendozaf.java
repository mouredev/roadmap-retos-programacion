
public class andresmendozaf {

    public static void main(String[] args) {

        /*
         * Operadores 
         */
        // Operadores aritméticos
        int a = 10;
        int b = 3;
        int suma = 10 + 5;
        System.out.println(suma);
        System.out.println("Suma: 10 + 3 = " + (a + b));
        System.out.println("Resta: 10 - 3 = " + (a - b));
        System.out.println("Multiplicación: 10 * 3 = " + (a * b));
        System.out.println("División: 10 / 3 = " + (double) a / b);
        System.out.println("Módulo: 10 % 3 = " + (a % b));
        System.out.println("Exponente: Math.pow(10, 3) = " + Math.pow(a, b));
        System.out.println("División exacta: 10 / 3 = " + (a / b));

        // Operadores de comparación # devuelve un valor True o False
        System.out.println("Igual a: 10 == 3 es " + (10 == 3));
        System.out.println("No es igual: 10 != 3 es " + (10 != 3));
        System.out.println("Es mayor que: 10 > 3 es " + (10 > 3));
        System.out.println("Es menor que: 10 < 3 es " + (10 < 3));
        System.out.println("Es mayor o igual que: 10 >= 10 es " + (10 >= 10));
        System.out.println("Es menor o igual que: 10 <= 8 es " + (10 <= 8));

        // Operadores lógicos
        int c = 5;
        int d = 1;

        System.out.println("AND: (10 + 3 == 13) && (5 - 1 == 4) es: " + ((a + b == 13) && (c - d == 4)));
        System.out.println("OR: (10 + 9 == 19) || (5 - 1 == 6) es: " + ((10 + 9 == 19) || (c - d == 6)));
        System.out.println("NOT: 20 + 7 != 24 es: " + (20 + 7 != 24));

        // Operadores de asigmación
        int numero = 12; // = asignación
        System.out.println("Mi número es: " + numero);
        numero += 5; // + suma y asignación
        System.out.println(numero);
        numero -= 5; // - resta y asignación
        System.out.println(numero);
        numero *= 5; // * multiplicación y asignación
        System.out.println(numero);
        numero /= (double) 4; // / división y asignación
        System.out.println(numero);
        numero %= 2; // % módulo y asignación
        System.out.println(numero);
        numero = (int) Math.pow(numero, 8); // ** exponente y asignación
        System.out.println(numero);
        numero /= 3; //= 12 # división exacta y asignación 
        System.out.println(numero);

        // Operadores de identidad
        int nuevo_numero = 0;
        System.out.println("numero == nuevo_numero es: " + (numero == nuevo_numero)); //referencia al valor
        System.out.println("numero != nuevo_numero es: " + (numero != nuevo_numero));
        String str1 = "Hola";
        String str2 = "hola";
        System.out.println("str1.equals(str2) es: " + (str1.equals(str2)));

        // Operadores unarios
        int positivo = +a;
        System.out.println("Positivo (+a): " + positivo);
        int negativo = -a;
        System.out.println("Negativo (-a): " + negativo);
        a++;
        System.out.println("Incremento (a++): " + a);
        a--;
        System.out.println("Decremento (a--): " + a);

        boolean verdadero = true;
        boolean negado = !verdadero;
        System.out.println("Negación lógica (!verdadero): " + negado);

        // Operadores bit a bit
        int x = 10; //1010
        int y = 3; //0011
        System.out.println("AND (&): " + (x & y)); //0010
        System.out.println("OR (|): " + (x | y)); //1011
        System.out.println("XOR (^): " + (x ^ y)); //1001
        System.out.println("COMPLEMENTO (~): " + (~y)); //1111 1100 da vuelta los 0 y 1
        System.out.println("Desplazamiento a la derecha (>>): " + (8 >> 2)); //0000 0010
        System.out.println("Desplazamiento a la izquierda (<<): " + (3 << 2)); //0000 1100

        // Operador ternario
        String ternario = (a > (b += 15)) ? "a es mayor que b" : "a no es mayor que b";
        System.out.println(ternario);

        boolean esString = ternario instanceof String;
        System.out.println("¿ternario es una instancia de String? " + esString);
        Integer prueba = 42;
        boolean esInteger = prueba instanceof Integer;
        System.out.println("¿numero es una instancia de Integer? " + esInteger);

        /*
         * Estrucuras de Control 
         */
        //Condicionales
        String mi_cadena = "AndresMendoza";
        if (mi_cadena == "AndresMendoza") {
            System.out.println("mi_cadena es 'AndresMendoza'");
        } else if (mi_cadena == "Figueroa") {
            System.out.println("mi_cadena es 'Figueroa'");
        } else {
            System.out.println("mi_cadena no es ni 'AndresMendoza' ni tampoco 'Figueroa'");
        }

        int dia = 3;
        String nombreDia;

        switch (dia) {
            case 1:
                nombreDia = "Lunes";
                break;
            case 2:
                nombreDia = "Martes";
                break;
            case 3:
                nombreDia = "Miércoles";
                break;
            case 4:
                nombreDia = "Jueves";
                break;
            case 5:
                nombreDia = "Viernes";
                break;
            case 6:
                nombreDia = "Sábado";
                break;
            case 7:
                nombreDia = "Domingo";
                break;
            default:
                nombreDia = "Día inválido";
                break;
        }
        System.out.println("El día seleccionado es: " + nombreDia);

        // Iterativas
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " - ");
        }

        System.out.println();
        int k = 1;
        while (k <= 7) {
            System.out.print(k + " - ");
            k++;
        }

        System.out.println();
        for (int i = 1; i <= 8; i++) {
            if (i == 5) {
                break; // Sale del bucle cuando i es igual a 5
            }
            System.out.print(i + " ");
        }

        System.out.println();
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) {
                continue; // Omite la impresión para números pares
            }
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println();
        // Excepciones 

        try {
            int resultado = dividir(10, 5);
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Este bloque se ejecuta siempre.");
        }

        try {
            lanzarExcepcion();
        } catch (Exception e) {
            System.out.println("Excepción capturada: " + e.getMessage());
        }

        /*
         * Ejercicio extra 
         */

         for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0){
                System.out.print(i + " ");
            }
        }
    }

    public static int dividir(int numerador, int divisor) {
        if (divisor == 0) {
            throw new ArithmeticException("No se puede dividir por cero.");
        }
        return numerador / divisor;
    }

    public static void lanzarExcepcion() throws Exception {
        throw new Exception("Excepción lanzada explícitamente.");
    }

}
