import java.time.LocalTime;
import java.util.Timer;
import java.util.TimerTask;
import java.util.stream.IntStream;

/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
public class Jeigar2 {
    // Son variables "Globales"
    private static final int SEGUNDO = 1000; // milisegundos
    private static int cuentaAtras = 0;
    private static boolean activaCuentaAtras = false;
    private static Timer timer;

    public static void main(String[] args) {
        int segundos = 3; // variable local
        timer = new Timer();
        mostrarHoraActual();
        if(!isActivaCuentaAtras()) {
            configurarCuentaAtras(segundos);
            System.out.println("Total segundos para configurar la cuenta atrás " + segundos); // función ya creada en el sistema
            if(isActivaCuentaAtras()){
                mostrarMensajeInicializarCuentaAtras();
                iniciarCuentaAtrás();
            }
        }
        mostrarHoraActual();
        System.out.println( "Total numero no primos de 3 y 5 son: " + extra("solo uno", "ambos"));
    }

    // funcion con uno parámetro sin retorno
    public static void configurarCuentaAtras (int segundos){
        cuentaAtras = segundos;
        activarCuentaAtras();
    }

    // funcion sin parámetros ni retorno
    private static void activarCuentaAtras(){
        activaCuentaAtras = true;
    }

    // funcion sin parámetros ni retorno
    public static void iniciarCuentaAtrás(){
        // No puedo crear una función dentro de una función
        // Pero puedo desde un método llamar a de una clase anónima que tiene su propia función.
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                activaCuentaAtras = false;
                mostrarMensajeFinalizadaCuentaAtras();
                timer.cancel(); // función ya creada en el sistema
                System.out.println("si te fijas bien han pasado " + cuentaAtras + " segundos");
            }
        }, cuentaAtras * SEGUNDO);
    }

    // funcion sin parámetros con retorno
    public static boolean isActivaCuentaAtras() {
        return activaCuentaAtras;
    }

    // funcion sin parámetros ni retorno
    public static void mostrarHoraActual () {
        System.out.println("Son las " + LocalTime.now());  // función ya creada en el sistema
    }

    // funcion sin parámetros ni retorno que llama a una función que tiene un parametro y a otra funcion que no tiene parametros
    public static void mostrarMensajeFinalizadaCuentaAtras(){
        mostrarMensajeCuentaAtrasConTexto("finalizado");
        mostrarHoraActual();
    }

    // funcion sin parámetros ni retorno que llama a una función que tiene un parametro
    public static void mostrarMensajeInicializarCuentaAtras(){
        mostrarMensajeCuentaAtrasConTexto("iniciado");
    }

    // funcion con parámetros sin retorno
    private static void mostrarMensajeCuentaAtrasConTexto (String texto){
        System.out.println("La cuenta atrás ha " + texto);  // función ya creada en el sistema
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
     * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
     *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
     *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
     *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
     *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
     */

    private static int extra(String cadena1, String cadena2){
        int inicioRango = 1;
        int finRango = 100;
        long totaMultiplos = IntStream.rangeClosed(inicioRango,finRango)
                .filter( number -> number % 3 == 0 || number % 5 == 0 ) // solo quiero los múltiplos de 3 y 5
                .peek(number -> {
                    if(number % 3 == 0 && number % 5 == 0) { // si es múltiplo de ambos
                        System.out.println(number + " " + cadena2);
                    } else if (number % 3 == 0 || number % 5 == 0 ) { // si es solo múltiplo de uno de los dos
                        System.out.println(number + " " + cadena1);
                    }
                })
                .count(); // total de múltiplos
        return (int) (finRango - totaMultiplos);
    }

}
