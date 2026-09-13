public class YassellMiranda50Boop {

    // Metodo sin parametros ni retorno.
    public static void mostrarMensaje() {
        System.out.println("Hola mundo!, bienvenido a Java");
    }

    // Metodos que reciben parametros(num1, num2) y dan un valor de retorno.
    public static int sumar(int a, int b) {
        return a + b;
    }

    public static int restar(int num1, int num2) {
        return num1 - num2;
    }

    /*
     * Funcion dentro de funcion:
     * public static void funcionDoble(){
     * public static Mostrar(){
     * System.out.println("No se puede crear un metodo dentro de otro");
     * }
     * }
     * En Java no es permitido la declaracion de un metodo/funcion dentro de otro.
     */

    public static void main(String[] args) {
        // llamare a los metodos que voy creando:
        mostrarMensaje(); // Muestra un mensaje.
        System.out.println(sumar(7, 23));
        System.out.println(restar(10, 5));

        // Utiliza algún ejemplo de funciones ya creadas en el lenguaje:
        // metodo utilizado: Math, del paquete: java.lang
        int mayorDeDos = Math.max(70, 85);
        System.out.println("El mayor entre 70 y 85 es: " + mayorDeDos);

        // En el main se llaman a los metodos para mostrarlos en consola
        mostrarVariableLocal();

        // Creamos las variables y llamamos al metodo:
        String texto1 = "El numero es multiplo de 3. ";
        String texto2 = "El numero es multiplo de 5";
        System.out.println(resolviendoDificultadExtra(texto1, texto2));
    }

    // Ejemplo de variable local
    public static void mostrarVariableLocal() {
        String texto = "Un variable local existe solamente dentro de las llaves {} de un metodo";
        System.out.println(texto);

        // llamamos a el metodo mostrarTextosFinales
        mostrarTextosFinales();
    }

    // Ejemplo de variable global
    static String textoFinal = "Esta es una variable global, no se encuentra dentro de ningun metodo. Se declara dentro de la misma clase";

    public static void mostrarTextosFinales() {
        System.out.println(textoFinal);
    }

    public static int resolviendoDificultadExtra(String texto1, String texto2) {
        int contador = 0;

        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(i + ": " + texto1 + texto2);
            } else if (i % 3 == 0) {
                System.out.println(i + ": " + texto1);
            } else if (i % 5 == 0) {
                System.out.println(i + ": " + texto2);
            } else {
                System.out.println(i);
                contador++;
            }
        }
        return contador;
    }
}
