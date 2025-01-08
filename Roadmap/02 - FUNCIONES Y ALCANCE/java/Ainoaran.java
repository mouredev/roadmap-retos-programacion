//RETO #02 - Funciones y alcance.

public abstract class Ainoaran {

    //Funciones:

    //Función básica sin parámetros:
    public void hello() {
        System.out.print("¡Hi, Java!");
    }

    //Función básica con parámetros:
    public void hola(String java) {
        System.out.print("¡Hola, " + java);
    }

    //Función básica sin parámetro y retorno:
    public String konnichiwa() {
        return "こんにちは, Java";
    }

    //Función básica con parámetro y retorno:
    public String bonjour(String java) {
        return "Bonjour, " + java;
    }

    //Método static - Permite invocar funcionalidad sin crear objetos:
    public class operacion {
        public static int sumar(int a, int b) {
            return a + b;
        }
    }
    int resultado = operacion.sumar(5,10);

    //Método abstracto - Se declaran en una clase abstracta.
    //Su propósito es definir un "contrato" que las clases hijas deben cumplir.
    public abstract class despedida {
        public abstract void goodbye();
    }

    //Método constructor - se utiliza para inicializar objetos de una clase:

    public class Persona {
        private String nombre;
        private int edad;

        // Constructor por defecto
        public Persona() {
            nombre = "Desconocido";
            edad = 30;
        }

        // Constructor con parámetros
        public Persona(String nombre, int edad) {
            this.nombre = nombre;
            this.edad = edad;
        }
    }
    /*Funciones anidadas:
     *Java no soporta la definición anidada de funciones como en algunos otros lenguajes de programación.
     *Cada función debe definirse a nivel de clase.
     */

    //Variables Locales - Se declaran dentro de un bloque de código específico.
    public void varLocal() {
        int num = 10;
        System.out.println(num);
    }

    //Variable Global - Se declaran dentro de una clase, pero fuera de cualquier método, constructor o bloque de código.
    public class global {
        int num = 10; // Variable global (de instancia)

        public void varGlobal() {
            System.out.println(num);
        }
    }

    /*DIFICULTAD EXTRA (opcional):
     * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
     * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
     *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
     *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
     *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
     *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
     */

    public static int difExtra(String text1, String text2) {
        int counter = 0;

        for (int i = 0; i < 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(i + ": " + text1 + " " + text2);
                counter++;
            } else if (i % 3 == 0) {
                System.out.println(i + ": " + text1);
                counter++;
            } else if (i % 5 == 0) {
                System.out.println(i + ": " + text2);
                counter++;
            }
        }

        return counter;
    }

    public static void main(String[] args) {

        String text1 = "Fizz";
        String text2 = "Buzz";
        int finalCounter = difExtra(text1, text2);
        System.out.print("Contador: " + finalCounter);

    }
}
