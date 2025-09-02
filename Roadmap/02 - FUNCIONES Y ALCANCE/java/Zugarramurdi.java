/**
 * En la clase Zugarramurdi se implementaará la solucion al ejercicio #02 - FUNCIONES Y ALCANCE
 * @author Zugarramurdi
 * @version 1.0 08/04/2025
 */
public class Zugarramurdi {

    // Variables locales y globales

    /* Las variables locales son aquellas que se declaran dentro de una funcion y solo se pueden usar dentro de esa funcion,
     * incluso si se declaran dentro de un bloque de codigo, como un if o un for, por ejemplo todas las variables de las funciones
     * creadas mas abajo o incluso las del propio metodo main
     *
     * Las variables globales son aquellas que se declaran fuera de una funcion y se pueden usar en cualquier parte del programa,
     * incluso dentro de las funciones, por ejemplo las variables que se declaran, en este caso, dentro de la clase Zugarramurdi
     * se les llama tambien variables de instancia, por declararse dentro de una clase
     */

    static String texto1 = "Pipo", texto2 = "Pepo"; // variables globales

    public static void main(String[] args) {

        // Llamada a las funciones

        funcion1(); // Funcion sin parametros ni retorno
        funcion2("Hola a todos"); // Funcion con un parametro y sin retorno
        funcion3(5, 10); // Funcion con dos parametros y sin retorno
        int resultado = funcion4(5, 10); // Funcion con dos parametros y retorno
        System.out.println("\nEl resultado de la suma de funcion4 es: " + resultado+"\n"); // Imprime el resultado de la funcion 4
        extra(texto1, texto2); // Llamamos a la funcion de ejercicio extra con variables globales




    }

    // Funcion sin parametros ni retorno
    public static void funcion1() {
        System.out.println("\nEsta es una funcion sin parametros ni retorno\n");
    }

    // Funcion con un parametro y sin retorno
    public static void funcion2(String mensaje) {
        System.out.println("\nEsta es una funcion con un parametro: " + mensaje+"\n");
    }

    // Funcion con dos parametros y sin retorno
    public static void funcion3(int numero1, int numero2) {
        System.out.println("\nEsta es una funcion con dos parametros: " + numero1 + " y " + numero2);
        System.out.println("Se pueden realizar operaciones con los parametros: " + (numero1 + numero2)+"\n");
    }

    // Funcion con dos parametros y retorno
    public static int funcion4(int numero1, int numero2) {
        return numero1 + numero2;
    }

    // Funcion dentro de funcion

    /* En java no se pueden declarar funciones dentro de otras funciones, pero se pueden llamar a otras funciones dentro de una funcion,
     * de hecho, en las funciones 1,2 y 3 se llama a la funcion System.out.println(); *que es una funcion ya creada por el lenguaje*
     * lo mas comun es que se declaren funciones dentro de una clase y se llamen desde el main
     * aqui por ejemplo estamos declarando funciones dentro de la clase Zugarramurdi y llamandolas desde el main
     */

    // Funcion ya creada por el lenguaje

    /* Las funciones ya creadas por el lenguaje son funciones que ya vienen incluidas en el lenguaje y se pueden usar directamente
     * Java tiene muchas funciones ya creadas, como por ejemplo la funcion System.out.println(); que se usa para imprimir en pantalla
     * tambien existen funciones matematicas de la clase Math, como Math.random(); que genera un numero aleatorio o Math.sqrt(); que calcula la raiz cuadrada
     * la clase String tambien tiene funciones ya creadas, como String.length(); que devuelve la longitud de una cadena de texto
     */

    // Ejercicio Extra

    public static int extra(String mensaje1, String mensaje2) {
        int contador = 0;
        System.out.println("\n\tEjercicio Extra\n");
        for (int i = 1; i <= 100; i++){
            if(i % 3 == 0 && i % 5 == 0){
                System.out.println(mensaje1 + " " + mensaje2);
            }else if(i % 3 == 0){
                System.out.println(mensaje1);
            }else if(i % 5 == 0){
                System.out.println(mensaje2);
            }else{
                System.out.println(i);
                contador++;
            }
        }
        return contador;
    }

}
