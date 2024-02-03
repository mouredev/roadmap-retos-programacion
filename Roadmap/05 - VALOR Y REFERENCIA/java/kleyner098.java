import java.util.Arrays;

public class kleyner098 {
    /*
     * EJERCICIO:
     * - Muestra ejemplos de asignación de variables "por valor" y "por referencia",
     * según su tipo de dato.
     * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
     * "por referencia", y cómo se comportan en cada caso en el momento de ser
     * modificadas.
     * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
     */

    public static void main(String[] args) {

        // Los tipos primitivos en Java simpre toman su valor por copia
        int num1 = 1; // Creamos una variable primitiva con un valor
        int num2 = num1; // Se copia el mismo valor de num1 en num2
        num1++; // Se modifica num1 y no afecta a num2
        System.out.println("Valor de variable num1:" + num1);
        System.out.println("Valor de variable num2:" + num2);
        // Las dos varaibles tienen espacio de memoria diferentes
        // Función
        cambiar(num2);
        // No se ha modificado el valor de num2
        System.out.println("Valor de variable num2, después de pasarla como argumento de una función:" + num2); 

        // Los demás tipos de variable tomarán el valor por referencia
        // Los arrays se concideran un tipo de dato entre primitivo y objeto
        int[] array1 = { 1, 2, 3, 4 }; // Creamos un array de tipo int
        int[] array2 = array1; // Copiamos la array1 en la array dos
        // Modificamos la array1
        for (int i = 0; i < array1.length; i++) {
            array1[i] = array1.length - i;
        }
        // Se ha realizado las modificaciones en las dos arrays
        System.out.println("Array1: " + Arrays.toString(array1));
        System.out.println("Array2: " + Arrays.toString(array2));

        // Lo que en realidad ocurre es que lo que copiamos en la array2 es la
        // referencia en memoria de la array1, por lo que en realidad las dos variables
        // apunta a la misma arrays, es decir, al mismo espacio de memoria.
        // En Java, en realidad todas las asignaciones son por copia, pero en el caso de
        // los objetos, lo que se copia es la referencia de memoria y no los valores que
        // contiene
        System.out.println("Dirección de memoria de array1 " + array1);
        System.out.println("Dirección de memoria de array2 " + array2);

        // Función
        cambiarArrays(array2);
        System.out.println("Arrays2 después de pasarla como argumento de una función:" + Arrays.toString(array2));

        // Existen casos especiales de objetos, llamado objetos inmutables cuyo estado
        // no puede ser modificado, es decir, una vez asignado un valor a un objeto este
        // no se puede realizar cambios en sus atributos. El ejemplo más típico en Java
        // son las clase String o la mayoría de las clases Wrappers(Integer, Double...)

        String cadena1 = "Hola mundo"; // Creamos un objeto string
        String cadena2 = cadena1; // Copiamos el valor del objeto cadena1 en cadena2 (Referencia al mismo objeto)
        cadena1 = "Adios Java"; // Se crea otro objeto con el nuevo valor y se le asiga la referencia de cadena1
        System.out.println(cadena1);
        System.out.println(cadena2);

        // Al principio, ambas cadena1 y cadena2 apuntan al objeto "Hola mundo".
        // Después cadena1 apunta a un nuevo objeto "Adios Java" pareciendo que se ha
        // modificado, pero en realidad crea un nuevo objeto con la referencia cadena1
        // y cadena2 sigue apuntando al objeto original "Hola mundo".
        // No se crea un nuevo objeto para cadena2 en este caso.
        // Java utiliza un mecanismo llamado "pool de cadenas" o "String pool" para
        // optimizar el uso de memoria y permitir que variables String con el mismo
        // contenido referencien los mismos literales de cadena.

        // Ejercicio extra

        int numero1 = 5;
        int numero2 = 7;
        int[] arrryNum = cambiarOrden(numero1, numero2);
        System.out.println("Valores originales: " + numero1 + " | " + numero2);
        System.out.println("Valores intercambiados: " + arrryNum[0] +" | " + arrryNum[1]);
        int[] tabla1 = {1,2,3};
        int[] tabla2 = {4,3,2,1};
        int[][] resultado = cambiarOrdenArray(tabla1, tabla2);
        System.out.println("Valores originales: " + Arrays.toString(tabla1) + " | " + Arrays.toString(tabla2));
        System.out.println("Valores intercambiados: " + Arrays.toString(resultado[0]) + " | " + Arrays.toString(resultado[1]));
    }

    // La función toma el valor por copia, lo que significa que se crea un espacion
    // nuevo en memoria y copia el valor pasado en el argumento
    static void cambiar(int a) {
        a++;
    }

    // La función copia el valor de referencia de la array pasada en el argumento,
    // por lo que hace referencia a la misma array
    static void cambiarArrays(int[] array) {
        for (int i = 0; i < array.length; i++) {
            array[i] = -i;
        }
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea dos programas que reciban dos parámetros (cada uno) definidos como
     * variables anteriormente.
     * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso,
     * por referencia.
     * Estos parámetros los intercambia entre ellos en su interior, los retorna, y
     * su retorno se asigna a dos variables diferentes a las originales. A
     * continuación, imprime el valor de las variables originales y las nuevas,
     * comprobando que se ha invertido su valor en las segundas.
     * Comprueba también que se ha conservado el valor original en las primeras.
     */

     static int[] cambiarOrden(int num1, int num2){
        int[] arrayNum = {num2, num1};
        return arrayNum;
     }

     static int[][] cambiarOrdenArray(int[] array1, int[] array2){
        int[][] arrayResult = new int[2][];
        arrayResult[0] = new int[array2.length];
        arrayResult[1] = new int[array1.length];
        for (int i = 0; i < arrayResult[0].length; i++) {
            arrayResult[0][i] = array2[i];
        }
        for (int i = 0; i < arrayResult[1].length; i++) {
            arrayResult[1][i] = array1[i];
        }
        return arrayResult;
     }
}
