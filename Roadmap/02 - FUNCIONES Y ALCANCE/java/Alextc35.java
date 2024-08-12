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

// Clase abstracta con un método abstracto
abstract class Animal {
    // Método abstracto (sin implementación)
    public abstract void hacerSonido();

    // Método no abstracto (con implementación)
    public void dormir() {
        System.out.println("El animal está durmiendo.");
    }
}

// Clase concreta que extiende la clase abstracta
class Perro extends Animal {
    // Implementación del método abstracto
    @Override
    public void hacerSonido() {
        System.out.println("El perro dice: ¡Guau!");
    }
}

// Otra clase concreta que extiende la clase abstracta
class Gato extends Animal {
    // Implementación del método abstracto
    @Override
    public void hacerSonido() {
        System.out.println("El gato dice: ¡Miau!");
    }
}

// Clase con método sincronizado
class Contador {
    private int cuenta = 0;

    public synchronized void incrementar() {
        cuenta++;
    }

    public int getCuenta() {
        return cuenta;
    }
}

// Clase con métodos de diferentes tipos
public class Alextc35 {

    // Variable global
    static int variableGlobal = 777;

    // Constructor explícito sin parámetros
    public Alextc35() {
        System.out.println("Constructor de objetos");
    }

    // Constructor con parámetros
    public Alextc35(String nombre, int edad) {
        System.out.println("Nombre: " + nombre + "\nEdad: " + edad);
    }

    // Método estático
    public static void metodoStatic() {
        System.out.println("Método estático.");
    }

    // Método final
    public final void metodoFinal() {
        System.out.println("Método final.");
    }

    public static void main(String[] args) {
        Alextc35 yo = new Alextc35(); // Constructor sin parámetros
        Alextc35 miOtroYo = new Alextc35("Alejandro", 23); // Constructor con parámetros

        // 1. Funciones básicas
        funcionVoidNoParams();
        funcionVoidSiParams("cat");
        funcionVoidTwoParams(13, 22);
        System.out.println("La suma de 21 + 196 es = " + funcionIntTwoParams(21, 196));
        System.out.println("Mi nombre es: " + funcionStringSiParams("Alejandro"));

        // Ejemplo de clases abstractas y métodos abstractos
        Animal miPerro = new Perro();
        Animal miGato = new Gato();

        miPerro.hacerSonido(); // Debería imprimir: El perro dice: ¡Guau!
        miPerro.dormir(); // Debería imprimir: El animal está durmiendo.

        miGato.hacerSonido(); // Debería imprimir: El gato dice: ¡Miau!
        miGato.dormir(); // Debería imprimir: El animal está durmiendo.

        // 2. Función dentro de otra función
        funcionDos();

        // 3. Ejemplo de función ya existente
        Integer a = 217;
        Integer b = 217;
        System.out.println("a: " + a + "\nb: " + b + "\n¿Son iguales?: " + a.equals(b));

        // 4. Variables globales y locales
        System.out.println("Variable global: " + variableGlobal);
        int variableLocal = obtenerVariableLocal();
        System.out.println("Variable local: " + variableLocal);

        // Ejemplos de métodos adicionales
        metodoStatic(); // Llamada al método estático
        Alextc35 instance = new Alextc35();
        instance.metodoFinal(); // Llamada al método final

        // Ejemplo de método con sincronización
        Contador contador = new Contador();
        contador.incrementar();
        System.out.println("Contador después de incrementar: " + contador.getCuenta());

        // Opcional
        System.out.println("Número de veces que se imprimió un número: " + funcionOpcional("Alejandro", "Tellez"));
    }

    // 1. Funciones básicas

    public static void funcionVoidNoParams() {
        System.out.println("Función que no tiene parámetros y no retorna nada.");
    }

    public static void funcionVoidSiParams(String word) {
        System.out.println("La palabra es " + word + ".");
    }

    public static void funcionVoidTwoParams(int number1, int number2) {
        System.out.println("La suma de " + number1 + " + " + number2 + " es = " + (number1 + number2));
    }

    public static int funcionIntTwoParams(int number1, int number2) {
        return number1 + number2; // Retorna la suma de los parámetros.
    }

    public static String funcionStringSiParams(String name) {
        return name; // Retorna la cadena de texto.
    }

    // 2. Función dentro de otra función

    public static void funcionUno() {
        System.out.println("Soy la función uno!");
    }

    public static void funcionDos() {
        funcionUno(); // Llama a la función uno dentro de la función dos.
        System.out.println("Soy la función dos!");
    }

    // 4. Variables globales y locales

    public static int obtenerVariableLocal() {
        int variableLocal = 666; // Variable local
        return variableLocal;
    }

    // Opcional

    public static int funcionOpcional(String cadena1, String cadena2) {
        int num = 0;

        // Bucle del 1 al 100
        for (int i = 1; i <= 100; i++) {
            if (i % 15 == 0) {
                System.out.println(cadena1 + cadena2); // Múltiplo de 3 y 5
            } else if (i % 3 == 0) {
                System.out.println(cadena1); // Múltiplo de 3
            } else if (i % 5 == 0) {
                System.out.println(cadena2); // Múltiplo de 5
            } else {
                System.out.println(i); // Otro caso
                num++;
            }
        }
        return num;
    }
}