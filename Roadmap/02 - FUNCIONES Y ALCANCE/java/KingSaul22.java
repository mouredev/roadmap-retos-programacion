/**
 * Resolución del ejercicio #02 FUNCIONES Y ALCANCE de la web Retos de Programación
 * @see <a href="https://retosdeprogramacion.com/roadmap">Retos de Programación</a>
 * @see <a href="https://github.com/KingSaul22">GitHub de KingSaul22</a>
 */
public class KingSaul22 {
    private static int variableGlobal = 10;
    //Variable creada a nivel global a la que se podrá acceder desde toda la clase

    public static void main(String[] args) {
        //Variable local, solo se podrá acceder a su valor en main
        int variableLocal = 22;

        //Un método sin parametros ni retorno
        buenosDias();

        //Un método que devuelve un entero pero no acepta parametros
        System.out.println(numeroAleatorio());

        //Un método que acepta parametros pero no devuelve nada
        setVariableGlobal(variableLocal);

        //Un método que acepta parametros y devuelve un booleano
        if (compararNumeros(variableLocal, variableGlobal)) System.out.println("Yes");

        //Método que accede a otro método
        asegurarIgualdadVariableGlobal(77);

        //DIFICULTAD EXTRA
        String a = "Sal", b = "Azúcar";
        System.out.println("\nNúmeros impresos: " + dificultadExtra(a, b));
    }

    /**
     * Imprime por pantalla "Buenos días"
     */
    private static void buenosDias() {
        System.out.println("Buenos días");
    }

    /**
     * @return Número aleatorio entre 1 y 100
     */
    private static int numeroAleatorio() {
        return (int) (Math.random() * 100 + 1);
    }

    /**
     * En esté método le damos a la variable Global el valor del número recogido por parametro
     *
     * @param numero
     */
    private static void setVariableGlobal(int numero) {
        variableGlobal = numero;
    }

    /**
     * Método que comprueba si dos números son iguales
     *
     * @param numeroA
     * @param numeroB
     * @return Devuelve True cuando numeroA y numeroB son iguales
     */
    private static boolean compararNumeros(int numeroA, int numeroB) {
        return numeroA == numeroB;
    }

    /**
     * Método que valida que la variableGlobal sea igual a un número introducido usando el método {@link KingSaul22#compararNumeros compararNumeros()}
     * y en caso de no ser iguales las iguala
     * @param numero
     */
    private static void asegurarIgualdadVariableGlobal(int numero) {
        if (compararNumeros(variableGlobal, numero)) {
            System.out.println("La variableGlobal ya es igual a " + numero);
        } else {
            variableGlobal = numero;
            System.out.println("Se ha actualizado el valor de la variableGlobal a " + numero);
        }
    }

    /**
     * Este método imprime los números del 1 al 100 siempre y cuando no sea múltiplo de 2 o 5
     * <p>
     * Cuando sea multiplo de 5 y 3 se imprimen las dos cadenas; en caso de solo ser multiplo de 3 la cadena1 y en caso de solo ser multiplo de 5 la cadena2
     *
     * @param cadena1
     * @param cadena2
     * @return El número de veces que se han imprimido números
     */
    private static int dificultadExtra(String cadena1, String cadena2) {
        int contNumero = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 5 == 0 && i % 3 == 0) {
                System.out.println(cadena1 + " y " + cadena2);
            } else if (i % 3 == 0) {
                System.out.println(cadena1);
            } else if (i % 5 == 0) {
                System.out.println(cadena2);
            } else {
                System.out.println(i);
                contNumero++;
            }
        }

        return contNumero;
    }
}
