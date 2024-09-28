public class DanielBelenguer {
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

public static void main(String[] args) {
    // Función sin parámetros y sin retorno
    funcionsinparametrosinretorno();
    // Función con un parámetro de entrada y sin retorno
    funcionunparametrosinretorno(5);
    // Función con varios parámetros de entrada y con retorno
    System.out.println(funcionvariosparametrosconretorno(5, 10));
    // Función dentro de función
    funciondentrodefuncion();
    // Función que utiliza una función ya creada en el lenguaje
    System.out.println(Math.random());
    // Función para comprobar el alcanze de las variables
    int num = 5; // Esta variable es global
    System.out.println("El valor de la variable global es: " + num);
    // Función extra
    System.out.println((int)funcionextra("Hola","mundo!"));
}

static public void funcionsinparametrosinretorno () {
    System.out.println("Esto es una función sin parámetros de entrada y sin retorno");
}

static public void funcionunparametrosinretorno (int a) {
    System.out.println("Esto es una función con un parámetro de entrada y sin retorno");
    System.out.println("El parametro de entrada es: " + a);
}

static public int funcionvariosparametrosconretorno (int a, int b) {
    System.out.println("Esto es una función con varios parámetros de entrada y con retorno");
    System.out.println("Los parámetros de entrada son: " + a + " y " + b);
    System.out.println("Los parámetros de entada se van a sumar.");
    return a + b;
}

static public void funciondentrodefuncion () {
    System.out.println("Esto es una función dentro de otra función");
    System.out.println("Vamos a llamar a otra función desde esta función");
    funcionsinparametrosinretorno();
}

static public void funcionalcancevariables () {
    int num2 = 10; // Esta variable es local
    System.out.println("El valor de la variable local es: " + num2);
}

static public int funcionextra (String cadena1, String cadena2) {
    int repeticion = 0;
    for (int i = 1; i <= 100; i++) {
        if ( i % 3 == 0) {
            System.out.println(cadena1);
            repeticion++;
        }else if (i%5==0) {
            System.out.println(cadena2);
            repeticion++;
        }else if (i%3==0 && i%5==5 ){
            repeticion++;
            System.out.println(cadena1 + " " + cadena2);
        }
    }
    return repeticion;
}
}
