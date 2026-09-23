public class JDPinillaa {
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

    static void sinParametros(){
        System.out.println("Esto es una funcion sin parametros ni retorno");
    }

    static void conParametros(String param){
        System.out.println(param);
    }

    static String conRetorno(){
        return "Esta es una funcion con retorno";
    }

    //En java no podemos crear metodos dentro de otros

    //Ejemplo de funcion ya creada
    static double raizCuadrada(double num){
        return Math.sqrt(num);
    }


    String valGlobal = "Esto es una variable global";

    static void demostrarLocal(){
        int edad = 20; //Esto es una variable local
        System.out.println("Mi edad es "+edad);
    }


    /**
     * Ejercicio de dificultad extra
     */
    static int dificultadExtra(String frase1, String frase2){
        int contador=0;
        for (int i=0; i<100; i++){
            if (i%3 == 0 && i%5 ==0){
                System.out.println(frase1 + frase2);
            } else if (i%3 == 0) {
                System.out.println(frase1);
            } else if (i%5 == 0) {
                System.out.println(frase2);
            }
            contador++;
        }
        return contador;
    }



    static void main() {
        sinParametros();
        conParametros("Esta es una funcion que recibe un parametro");
        System.out.println(conRetorno());
        raizCuadrada(16);
        dificultadExtra("soy multiplo de 3", "soy multiplo de 5");
    }
}
