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
public class Davidr1594 {
    public static void main(String[] args) {
        
        //Funciones basicas en java:
        //Pueden retornar o un un valor a la vez que pueden llevar o no parametros
        // se forman de un accesso - modificador -si va retornar o es void - tipo - nombre. 
        //Tambien se le puede asignar el valor retornado de una funcion a una variable.

        //Funciones estaticas
        funcionSinParam();
        funcionConParam("Soy una función con 2 parametros");
        funcionCon2Param(2,5);
        funcionConRetorno(false,"Soy verdadero");
        //LLamando metodo(Se le llama metodo cunado proviene de un objeto si es un funcion propia de la clase se define con el modificador static).
        Davidr1594.metodoLLamado();
        //Llamando a una funcion desde otra funcion
        mostrarEnPantalla();
        //Ejercicio Extra
        System.out.println(ejercicioExtra("Texto1","Texto2"));

    

    }

    private static int ejercicioExtra(String cadena1, String cadena2) {
        int contador = 0;
        for (int i = 1; i <= 100; i++) {
            if(i%3 == 0){
                System.out.println(cadena1);
                contador +=1;
            }else if(i%5 == 0){
                System.out.println(cadena2);
                contador +=1;
            }else if((i%3 == 0) && (i%5 == 0)){
                System.out.print(cadena1.concat(" "+ cadena2));
                contador += 1;
            }

        }
    return contador;
    }

    private static void mostrarEnPantalla() {
        int a = 5 ,b =5;

        System.out.println(suma(a,b));
    }

    private static int suma(int a, int b) {

        return a+b;
    }

    private static void metodoLLamado() {
        System.out.println("Soy un metodo proveniente del objeto Davidr1594");
    }

    private static void funcionCon2Param(int a, int b) {
        System.out.println("Funcion con 2 parametros, se sumaran:"+ (a+b));
    }

    private static void funcionConParam(String mensaje) {
        System.out.println(mensaje);
    }

    private static void funcionSinParam() {

        System.out.println("Soy una función sin parametros");
    }
    private static boolean funcionConRetorno(boolean a, String mensaje){
        if (a == true){
            System.out.println(mensaje);
        }
        return a;
    }
    
    
}
