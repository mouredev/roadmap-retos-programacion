import java.util.List;

public class frangarmez21 {

    public static void main(String[] args) {

        System.out.println("##Ejercicio valor/referencia##");
        /*
         * EJERCICIO:
         * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
         *   su tipo de dato.
         *
         * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
         *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
         * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
         */

        System.out.println();
        System.out.println("##Asignación por valor##");
        System.out.println();
        //Cualquier variable de tipo primitivo y de la clase String como caso excepcional se les realiza una asignacion por valor.
        System.out.println("Creamos una variable de tipo entero y le damos un valor");
        int miNumero = 5;
        System.out.println(miNumero);
        System.out.println("LLamamos a una función que modifica el valor de la variable");
        modificarNumero(miNumero);
        System.out.println("Imprimimos el valor de la variable inicial");
        System.out.println(miNumero);

        System.out.println("Creamos una variable de tipo String y le damos un valor");
        String miCadena = "Hola Mundo";
        System.out.println(miCadena);

        System.out.println("LLamamos a una función que modifica el valor de la variable");
        modificarCadena(miCadena);

        System.out.println("Imprimimos el valor de la variable inicial");
        System.out.println(miCadena);


        System.out.println("##Asignación por referencia##");
        /*Cualquier variable de tipo Array y la mayoría de los objetos se les realiza una asignación por valor, es decir,
        se les asigna una dirección de memoria por lo que cualquier cambio sobre estos afecta a esa dirección de memoria
        y por lo tanto verá modificado su valor inicial.*/
        System.out.println("Creamos un Array de enteros de 3 posiciones");
        int[] misNumeros = new int[3];

        System.out.println("Asignamos valores a nuestro Array");
        misNumeros[0] = 10;
        misNumeros[1] = 20;
        misNumeros[2] = 30;

        System.out.println("Imprimimos el contenido de nuestro Array");
        for (int numero : misNumeros) {
            System.out.println(numero);
        }

        System.out.println("Modificamos en valor de nuestro Array en la función");
        modificarArray(misNumeros);

        System.out.println("Imprimimos el contenido de nuestro Array");
        for (int numero : misNumeros) {
            System.out.println(numero);
        }

        System.out.println();
        System.out.println("##Dificultad Extra##");
        System.out.println();

        /* DIFICULTAD EXTRA (opcional):
         * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
         * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
         *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
         *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
         *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
         *   Comprueba también que se ha conservado el valor original en las primeras.
         */

        System.out.println("Programa 1: parámetros por valor");
        System.out.println();

        int numberOne = 1;
        System.out.println("Variable inicial 1: " + numberOne);
        int numberTwo = 2;
        System.out.println("Variable inicial 2: " + numberTwo);
        System.out.println("Llamamos a la funcion de intercambio de valor");
        List<Integer> resulList = changeVariableByValue(numberOne, numberTwo);
        int contador = 1;
        for (int numero : resulList) {
            System.out.println("Variable " + contador + ": " + numero);
            contador++;
        }
        System.out.println("Variable inicial 1: " + numberOne);
        System.out.println("Variable inicial 2: " + numberTwo);

        System.out.println();
        System.out.println("Programa 2: parámetros por referencia");
        System.out.println();

        Integer integerOne = 1;
        System.out.println("Variable inicial 1: " + numberOne);
        Integer integerTwo = 2;
        System.out.println("Variable inicial 2: " + numberTwo);
        System.out.println("Llamamos a la funcion de intercambio de valor");
        List<Integer> resultList = changeVariableByReference(numberOne, numberTwo);
        contador = 1;
        for (Integer numero : resultList) {
            System.out.println("Variable " + contador + ": " + numero);
            contador++;
        }
        System.out.println("Variable inicial 1: " + numberOne);
        System.out.println("Variable inicial 2: " + numberTwo);

    }

    private static List<Integer> changeVariableByReference(Integer number1, Integer number2) {
        System.out.println("Dentro de la funcion:");
        System.out.println("Cambiamos el valor de variable 1");
        Integer numberOne = number2;
        System.out.println("Cambiamos el valor de variable 2");
        Integer numberTwo = number1;
        System.out.println("Salimos de la función");
        return List.of(numberOne, numberTwo);
    }

    private static List<Integer> changeVariableByValue(int number1, int number2) {
        System.out.println("Dentro de la funcion:");
        System.out.println("Cambiamos el valor de variable 1");
        int numberOne = number2;
        System.out.println("Cambiamos el valor de variable 2");
        int numberTwo = number1;
        System.out.println("Salimos de la función");
        return List.of(numberOne, numberTwo);
    }

    private static void modificarNumero(int miNumero) {
        //Modificamos el valor de la variable a 2
        miNumero = 2;
        System.out.println("valor dentro de la funcion: " + miNumero);
    }

    private static void modificarCadena(String miCadena) {
        miCadena = "Esto es un String cuya referencia se hace por valor";
        System.out.println("valor dentro de la funcion: " + miCadena);
    }

    private static void modificarArray(int[] miArray) {
        miArray[0] = 1;
        miArray[1] = 2;
        miArray[2] = 3;
    }
}
