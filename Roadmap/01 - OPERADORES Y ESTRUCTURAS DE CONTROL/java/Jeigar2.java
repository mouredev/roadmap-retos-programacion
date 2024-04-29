import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

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
public class Jeigar2 {
    public static void main(String[] args) throws Exception {
        testOperadoresAritmeticos();
        testOperadoresLogicos();
        testOperadoresComparacion();
        testOperadoresAsignacion();
        testOperadoresIdentidad();
        testOperadoresPertenencia();
        testOperadoresBits();
        testCondicionales();
        testIterativas();
        testExcepciones();
        extra();
    }

    private static void testExcepciones() {
        try {
            throw new RuntimeException("prueba");
        } catch (RuntimeException e){
            System.out.println("capturado Error: " + e.getMessage());
        } finally {
            System.out.println("Parte finally");
        }
    }

    private static void testIterativas() {
        List<Integer> numeros = Arrays.asList(3,2,9,4);
        System.out.println("for each");
        for (Integer numero : numeros){
            System.out.println("numero: " + numero);
        }

        System.out.println("for i");
        for (int i = 0; i < numeros.size(); i++) {
            System.out.println("numero: " + numeros.get(i));
        }

        System.out.println("Iterable stream");
        numeros.stream().forEach(System.out::println);

        System.out.println("do...while");
        if (numeros.size()>0) {
            int i = 0;
            System.out.println("numero:" + numeros.get(i));
            do {
                System.out.println("numero:" + numeros.get(++i));
            } while (i < numeros.size()-1);
        }
        System.out.println("while");
        int j = 0;
        while (j < numeros.size()){
            System.out.println(numeros.get(j++));
        }

    }

    private static void testCondicionales() throws Exception {
        if(true){
            System.out.println("Es TRUE");
        }
        if(!true){

        } else {
            System.out.println("Es FALSE");
        }
        enum DiaSemana { LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO }

        DiaSemana dia = DiaSemana.MIERCOLES;

        String nombreDia = switch (dia){
            case LUNES -> "lunes";
            case MARTES -> "martes";
            case MIERCOLES -> "miercoles";
            case JUEVES -> "jueves";
            case VIERNES -> "viernes";
            case SABADO, DOMINGO -> "festivo";
            default -> throw new Exception("no es un día de la semana");
        };
        System.out.println("hoy es " + nombreDia);
    }

    public static void extra(){
        System.out.println("Extra\n----------");
        IntStream.range(10,55)
                .filter(n -> n % 2 == 0 && n != 16)
                .forEach(System.out::println);
    }

    public static void assertEquals(int expected, int actual, String message) {
        if (expected != actual) {
            throw new RuntimeException(String.format("ERROR: %s. Se esperaba %d y ha dado %d", message, expected, actual));
        } else {
            System.out.println(String.format("Resultado correcto %s se esperaba %d y ha dado %d", message, expected, actual));
        }
    }

    public static void assertTrue(boolean condition, String message) {
        if (!condition) {
            throw new RuntimeException(String.format("ERROR: %s, ha dado FALSE", message));
        } else {
            System.out.println(String.format("Resultado correcto %s, ha dado TRUE", message));
        }
    }

    public static void testOperadoresAritmeticos() {
        int a = 10;
        int b = 5;
        assertEquals(15, Operadores.suma(a, b), "en la operación de suma");
        assertEquals(5, Operadores.resta(a, b), "en la operación de resta");
        assertEquals(50, Operadores.multiplicacion(a, b), "en la operación de multiplicacion");
        assertEquals(2, Operadores.division(a, b), "en la operación de division");
        assertEquals(0, Operadores.modulo(a, b) , "en la operación de modulo");
    }

    public static void testOperadoresLogicos() {
        assertTrue(Operadores.and(true, true), "en la operación lógica AND");
        assertTrue(Operadores.or(true, false), "en la operación lógica OR");
        assertTrue(!Operadores.not(true), "en la operación lógica NOT");
    }

    public static void testOperadoresComparacion() {
        assertTrue(Operadores.igualdad(5, 5), "en la operación de igualdad");
        assertTrue(Operadores.diferencia(5, 10), "en la operación de diferencia");
        assertTrue(Operadores.mayorQue(10, 5), "en la operación mayorQue");
        assertTrue(Operadores.menorIgualQue(5, 10), "en la operación menorQue");
    }

    public static void testOperadoresAsignacion() {
        assertEquals(15, Operadores.asignacionSuma(10, 5) , "en la operación de asignación");
    }

    public static void testOperadoresIdentidad() {
        Integer obj1 = Integer.valueOf(10);
        Integer obj2 = Integer.valueOf(10);
        assertTrue(Operadores.identidad(obj1, obj2), "no tienen la misma identidad");
    }

    public static void testOperadoresPertenencia() {
        int[] array = {1, 2, 3, 4, 5};
        assertTrue(Operadores.pertenencia(array, 3),"el valor buscado no pertenece");
        assertTrue(!Operadores.pertenencia(array, 6), "el valor buscado si pertenece");
    }

    public static void testOperadoresBits() {
        assertEquals(1,Operadores.andBit(5, 3),"en el operado and de Bit");
        assertEquals(7,Operadores.orBit(5, 3), "en el operador or de Bit");
        assertEquals(10, Operadores.desplazamientoIzquierda(5), "en el desplazamiento a la Izquierda");
        assertEquals(2, Operadores.desplazamientoDerecha(5), "en el desplazamiento a la derecha");
    }

    class Operadores {
        public static int suma(int a, int b) {
            return a + b;
        }

        public static int resta(int a, int b) {
            return a - b;
        }

        public static int multiplicacion(int a, int b) {
            return a * b;
        }

        public static int division(int a, int b) {
            return a / b;
        }

        public static int modulo(int a, int b) {
            return a % b;
        }

        public static boolean and(boolean x, boolean y) {
            return x && y;
        }

        public static boolean or(boolean x, boolean y) {
            return x || y;
        }

        public static boolean not(boolean x) {
            return !x;
        }

        public static boolean igualdad(int num1, int num2) {
            return num1 == num2;
        }

        public static boolean diferencia(int num1, int num2) {
            return num1 != num2;
        }

        public static boolean mayorQue(int num1, int num2) {
            return num1 > num2;
        }

        public static boolean menorIgualQue(int num1, int num2) {
            return num1 <= num2;
        }

        public static int asignacionSuma(int a, int b) {
            return a += b;
        }

        public static boolean identidad(Integer obj1, Integer obj2) {
            return obj1 == obj2;
        }

        public static boolean pertenencia(int[] array, int search) {
            for (int i : array) {
                if (i == search) {
                    return true;
                }
            }
            return false;
        }

        public static int andBit(int m, int n) {
            return m & n;
        }

        public static int orBit(int m, int n) {
            return m | n;
        }

        public static int desplazamientoIzquierda(int m) {
            return m << 1;
        }

        public static int desplazamientoDerecha(int m) {
            return m >> 1;
        }
    }
}
