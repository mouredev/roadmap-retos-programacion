import java.util.Arrays;
import java.util.Collections;
import java.util.List;

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

public class mysterio_wil {

    // --- Variable "Global" (campo estático de la clase) ---
    private static String globalVar = "Soy una variable global";

    public static void main(String[] args) {
        System.out.println("===> Funciones básicas <===");

        // Sin parámetros ni retorno
        greet();

        // Con un parámetro
        greetPerson("Wilmer");

        // Con varios parámetros
        add(5, 3);

        // Con retorno
        int result = multiply(5, 3);
        System.out.println("El resultado de la multiplicación es " + result);

        // Simulación de parámetros por defecto con sobrecarga de métodos
        System.out.println("Java no tiene parámetros por defecto, se usa sobrecarga:");
        greetDefault("MoureDev");
        greetDefault("Wilmer", "Hello");

        // Con parámetros de longitud variable (varargs)
        System.out.println("Argumentos variables (varargs):");
        printArgs(1, "texto", true, 12.99);


        System.out.println("\n===> Funciones dentro de funciones <===");
        System.out.println("Java no soporta funciones anidadas, pero tiene clases locales y anónimas.");
        outerMethod();


        System.out.println("\n===> Funciones de la Librería Estándar de Java <===");
        List<Integer> myList = Arrays.asList(1, 2, 3, 4, 5);
        System.out.println("Usando el método size() de una Lista: La lista tiene " + myList.size() + " elementos.");
        System.out.println("Usando Collections.max(): El valor máximo es " + Collections.max(myList));


        System.out.println("\n===> Variable LOCAL y GLOBAL <===");
        myFunctionScope();

        // Modificar una variable global (campo estático)
        System.out.println("Antes de modificar: " + globalVar);
        modifyGlobal();
        System.out.println("Después de modificar: " + globalVar);


        /*
         * DIFICULTAD EXTRA (opcional):
         */
        System.out.println("\n====> DIFICULTAD EXTRA <====");
        int timesPrintedNumber = fizzBuzzExtra("Fizz", "Buzz");
        System.out.println("\nEl número se imprimió un total de " + timesPrintedNumber + " veces.");
    }

    // --- Definiciones de las funciones (métodos estáticos) ---

    static void greet() {
        System.out.println("Hola, Java!");
    }

    static void greetPerson(String name) {
        System.out.println("Hola, " + name + "!");
    }

    static void add(int a, int b) {
        System.out.println("La suma de " + a + " y " + b + " es " + (a + b));
    }

    static int multiply(int a, int b) {
        return a * b;
    }

    // Sobrecarga para simular parámetro por defecto
    static void greetDefault(String name) {
        greetDefault(name, "Hola");
    }

    static void greetDefault(String name, String greeting) {
        System.out.println(greeting + ", " + name + "!");
    }

    static void printArgs(Object... args) {
        for (Object arg : args) {
            System.out.println("- " + arg);
        }
    }

    static void outerMethod() {
        System.out.println("Este es el método externo.");
        // Clase local como ejemplo de anidamiento
        class InnerClass {
            void display() {
                System.out.println("Este es un método en una clase local (interna).");
            }
        }
        InnerClass inner = new InnerClass();
        inner.display();
    }

    static void myFunctionScope() {
        String localVar = "Soy una variable local";
        System.out.println(globalVar); // Acceso a la variable "global" (campo estático)
        System.out.println(localVar);
    }

    static void modifyGlobal() {
        globalVar = "He modificado la variable global";
    }

    static int fizzBuzzExtra(String text1, String text2) {
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            boolean isMultipleOf3 = (i % 3 == 0);
            boolean isMultipleOf5 = (i % 5 == 0);

            if (isMultipleOf3 && isMultipleOf5) {
                System.out.println(text1 + text2);
            } else if (isMultipleOf3) {
                System.out.println(text1);
            } else if (isMultipleOf5) {
                System.out.println(text2);
            } else {
                System.out.println(i);
                count++;
            }
        }
        return count;
    }
}
