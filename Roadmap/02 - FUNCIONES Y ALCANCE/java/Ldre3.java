import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

public class Ldre3 {

    public static void main(String[] args) {
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
         */
        funcion1();
        System.out.println(funcion2("Luis"));
        int numero = 1;
        System.out.println(numero);
        System.out.println(funcion3());
        fizzBuzz("Fizz","Buzz");




    }
    public static void funcion1() {
        System.out.println("Hola mundo!");
    }
    public static String funcion2(String nombre) {
        return "Hola " + nombre + "!";
    }
    public static int funcion3() {
        int numero = 0;
        return numero;
    }
    /*
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

    public static int fizzBuzz(String cadena1, String cadena2){
        AtomicInteger numero = new AtomicInteger(0);
        IntStream.range(1,101).forEach(v ->{
            String cadena = "";
            if (v%3==0) cadena+= cadena1;
            if (v%5==0) cadena+= cadena2;
            if (cadena.isBlank()){
                cadena+=v;
                numero.getAndIncrement();
            }
            System.out.println(cadena);
        });
        return numero.intValue();
    }

}