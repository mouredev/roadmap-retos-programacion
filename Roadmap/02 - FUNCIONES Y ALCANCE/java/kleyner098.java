
/**
 * kleyner098
 */

import java.time.LocalDateTime;


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

public class kleyner098 {

    public static void main(String[] args) {

        // Función/método que muestra la hora actual
        mostrarHora();

        // Función/método que calcula la potencia de un número de forma iterativa
        aElevadoNIterativa(2, 8);

        // Función/método que calcula la potencia de un número de forma recursiva
        double base = 2.00;
        int exponete = 8;
        double resultado = aElevadoNRecursiva(base, exponete);
        System.out.println(base + "^" + exponete + "=" + resultado);

        // Función/método que calcula la potencia utilizando la clase Math
        System.out.println(base + "^" + exponete + "=" + Math.pow(base, exponete));

        // Ámbito/alcance de variable
        int mismoNombre = 10;
        int variableFuncion = ambitoVariable();
        System.out.println("Variable local dentro de main: "+ mismoNombre);
        System.out.println("Variable local dentro de la función: "+ variableFuncion);

        //Ejercicio extra
        int num = fizzBuzz("fizz", "buzz");
        System.out.println("Se ha imprimido impreso " + num + " veces en vez del texto");


    }

    // Función/método que mustra la hora. Es una función sin parámetros ni delvuelve
    // ningún valor
    // Se utiliza el clase LocalDateTime
    static void mostrarHora() {
        // Se crea un objeto LocalTime que muestra la fecha y la hora
        LocalDateTime localDate = LocalDateTime.now();
        // Utilizamos métodos de LocalDateTime para conseguir la hora, minutos y
        // segundos y se guardan en variables
        int hours = localDate.getHour();
        int minutes = localDate.getMinute();
        int seconds = localDate.getSecond();
        // Mostramos la hora
        System.out.printf("La hora es %1$d:%2$d:%3$d\n", hours, minutes, seconds);
    }

    // Función/método que calcula la potencia de un número pasando los parámetros
    // base y
    // exponete (Solo con exponentes positivos)
    // de forma iterativas. La función no devuelve ningún valor y utiliza dos
    // parámetros
    static void aElevadoNIterativa(double base, int exponente) {
        // Declaración de variables
        double resultado = base;
        // Comprobar que el exponente es no es negativo
        if (exponente < 0) {
            System.out.println("Error. Introduce un numero entero positivo o cero para el exponente\n");
        } else if (exponente == 0) {
            System.out.printf("%1$.2f^%2$d = 1.00\n", base, exponente);
        } else {
            // Realiza la multiplitación x veces
            for (int i = 1; i < exponente; i++) {
                resultado = resultado * base;
            }
            // Imprime por pantalla el resultado
            System.out.printf("%1$.2f^%2$d = %3$.2f\n", base, exponente, resultado);
        }
    };

    // Función/método que calcula la potencia de un número pasando los parámetros
    // base y y
    // exponete (Solo con exponentes positivos)
    // de forma recursiva. La función devuelve un valor tipo double y utuliza dos
    // parámetros.
    static double aElevadoNRecursiva(double base, int exponente) {
        // Declaración de variables
        double resultado;
        if (exponente == 0) {
            resultado = 1; // caso base
        } else {
            resultado = base * aElevadoNRecursiva(base, exponente - 1); // Llamada recursiva de la función
        }
        return (resultado);
    }

    // En java no se pude crear una función dentro de otra, pero si se pude llamar
    // a otra función, incluso la misma función detro de si misma, como en el caso
    // de las funciones
    // recursivas

    // Ámbitos/alcance de variable: Las variable se puden utilizar dependiendo de donde se
    // declaren. Por ejemplo, si creamos una variable dendro de una función no
    // podemos utilizarla fuera de ella.
    // Dos variables pueden tener el mismo nombre si estan en ámbitos diferentes y ningún ámbito engloba al otro
    static int ambitoVariable() {
        int mismoNombre = 0;
        return mismoNombre;
    }

    //Eercicio extra
    static int fizzBuzz(String fizz, String buzz){
        int count = 0;
        for(int i = 1; i <= 100 ; i++){
            if(i % 3 == 0){
                System.out.println(fizz);
            }else if( i % 5 == 0){
                System.out.println(buzz);
            }else if (i % 5 == 0 && i % 3 == 0){
                System.out.println(fizz + buzz);
            }else{
                System.out.println(i);
                count++;
            }
        }
        return count;
    }
}