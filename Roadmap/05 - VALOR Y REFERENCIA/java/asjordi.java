public class Main {

    /**
     * Java utiliza el mecanismo de "paso por valor".
     * Esto significa que cuando pasas una variable a un método,
     * se pasa una copia del valor de la variable, no la variable en sí.
     * Esto es cierto tanto para tipos primitivos como para referencias a objetos.
     * Para los tipos primitivos, el valor que se pasa es el contenido de la variable.
     * Para las referencias a objetos, el valor que se pasa es la referencia al objeto, no el objeto en sí.
     * Por lo tanto, puedes modificar el objeto al que apunta la referencia,
     * pero no puedes cambiar la referencia en sí para que apunte a un objeto diferente.
     * @param args
     */

    public static void main(String[] args) {

        // Asignación de valores a las variables
        int numero = 5; // Asignación por valor
        double decimal = 5.0; // Asignación por valor
        boolean bool = true; // Asignación por valor

        int[] numeros = {1, 2, 3}; // Asignación por referencia
        int[] numeros2 = numeros; // Asignación por referencia
        int[] numeros3 = {1, 2, 3}; // Asignación por referencia

        System.out.println(numeros == numeros2); // true
        System.out.println(numeros == numeros3); // false

        // Funciones por valor
        /**
         * Cuando se pasa un parámetro por valor a un método,
         * se crea una copia del valor pasado a ese método.
         * Esto significa que cualquier cambio realizado en el parámetro dentro del método
         * no afectará a la variable original fuera del mismo.
         */
        int a = 5;
        duplicar(a);
        System.out.println("El valor de a después de llamar al método duplicar es: " + a);

        // Funciones por referencia
        /**
         * En Java, los parámetros por referencia se utilizan para transmitir información a un método de referencia.
         * Cuando se pasa un parámetro de referencia a un método, se pasa la dirección de memoria del objeto o la referencia al objeto en sí mismo.
         * Esto permite que el método pueda acceder y modificar el estado del objeto original.
         */

        String[] personas = {"Juan", "Pedro", "Luis"};
        System.out.println("El nombre de la persona en la posición 1 es: " + personas[1]);
        cambiarNombre(personas, 1, "Carlos");
        System.out.println("El nombre de la persona en la posición 1 después de llamar al método cambiarNombre es: " + personas[1]);

        System.out.println("-".repeat(50));

        int o1 = 7;
        int o2 = 3;

        int n1 = intercambiarPorValor(o1, o2);
        int n2 = intercambiarPorValor(o2, o1);

        StringBuilder o3 = new StringBuilder("Hola");
        StringBuilder o4 = new StringBuilder("Adiós");

        StringBuilder n3 = intercambiarPorReferencia(o3, o4);
        StringBuilder n4 = intercambiarPorReferencia(o4, o3);

        System.out.println("El valor de o1 es: " + o1);
        System.out.println("El valor de o2 es: " + o2);
        System.out.println("El valor de n1 es: " + n1);
        System.out.println("El valor de n2 es: " + n2);

        System.out.println("El valor de o3 es: " + o3);
        System.out.println("El valor de o4 es: " + o4);
        System.out.println("El valor de n3 es: " + n3);
        System.out.println("El valor de n4 es: " + n4);



    }

    public static void duplicar(int a) {
        a = a * 2;
        System.out.println("El valor de a dentro del método duplicar es: " + a);
    }

    public static void cambiarNombre(String[] nombres, int pos, String nuevoNombre) {
        nombres[pos] = nuevoNombre;
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
     * Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
     * Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
     * se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
     * variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
     * Comprueba también que se ha conservado el valor original en las primeras.
     */

    public static int intercambiarPorValor(int original, int intercambio) {
        original = intercambio;
        return original;
    }

    public static StringBuilder intercambiarPorReferencia(StringBuilder original, StringBuilder intercambio) {
        original = intercambio;
        return original;
    }

}
