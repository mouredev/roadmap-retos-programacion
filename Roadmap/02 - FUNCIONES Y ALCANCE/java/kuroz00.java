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

public class kuroz00 {

    static String varGlobal = "String en una var global";
    public static void conceptosVar(){
        String varLocal = "String en un ATRIBUTO de instancia, o var local";
        System.out.println(varLocal);
    }

     //Funcion que solo arroja un saludo, no recibe parametros ni retorna nada.
    public static void impresionSimple(){
        System.out.println("Hola a todos.");
    }

    //F complementando el saludo, recibe datos de tipo str/int e imprime el resto de la presentacion
    public static void presentacion(String nombre, int edad){
        System.out.printf("Soy %s y tengo %d !", nombre, edad);
    }

    //F que recibe parametros para realizar una suma y retorna la var en que se guardo.
    public static int suma(int numero1, int numero2){
        int valorSumado = numero1 + numero2;
        return valorSumado; 
    }

    //.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..--..-.--....--.-.-.-.-.-.-..-

    public class ff{
        public static void miFuncion(){
            System.out.println(" (holi, soy una funcion dentro de una clase)"); //F dentro de otra f, en java es dentro de una clase
        }
    }

    public static void df(String palabra1, String palabra2){
        int excepciones = 0;
        for (int i = 1; i <= 100; i++){
            if((i % 3 == 0) && (i % 5 == 0)){
                System.out.println(palabra1 + palabra2);
            } else if (i % 3 == 0){
                System.out.println(palabra1);
            } else if (i % 5 == 0){
                System.out.println(palabra2);
            } else {
                System.out.println("---excepciones +1---");
                excepciones += 1;
            }
        }
        System.out.println("Cantidad de excepciones ->" + excepciones);
    }

    public static void main(String[] args){
        //Llamada a las funciones y establecimiento de parametros requeridos.
        impresionSimple();
        presentacion("manuel", 26);
        suma(2, 2);
        
        ff.miFuncion();

        conceptosVar();
        System.out.println(varGlobal);

        // df
        df("Hola ", "mundo");
        //.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-
    }
}
