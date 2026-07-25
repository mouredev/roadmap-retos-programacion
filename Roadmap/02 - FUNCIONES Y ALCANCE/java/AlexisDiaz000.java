public class AlexisDiaz000 {
     // 1. Función sin parámetros ni retorno
     public static void saludo() {
        System.out.println("¡Hola! Soy Alexis Diaz");
    }

    // 2. Función con un parámetro y sin retorno
    public static void mostrarMensaje(String mensaje) {
        System.out.println("Mensaje recibido: " + mensaje);
    }

    // 3. Función con varios parámetros y con retorno
    public static int sumar(int a, int b) {
        return a + b;
    }

    // 4. Función con retorno sin parámetros
    public static double obtenerPi() {
        return 3.1415;
    }

    // 5. Uso de una función ya existente en Java
    public static void ejemploFuncionJava() {
        String texto = "Hola, mundo alexis diaz aqui!";
        System.out.println("Texto en mayúsculas: " + texto.toUpperCase());
    }

    // 6. Variables Locales vs Globales
    static int variableGlobal = 100; // Variable global

    public static void mostrarVariables() {
        int variableLocal = 50; // Variable local
        System.out.println("Variable global: " + variableGlobal);
        System.out.println("Variable local: " + variableLocal);
    }

    public static void main(String[] args) {
        // Llamar a cada función para ver su resultado
        saludo();

        mostrarMensaje("Soy yo de nuevo Alexis diaz.");

        int resultadoSuma = sumar(20, 8);
        System.out.println("Resultado de la suma es la cantidad de años que tengo actualmente: " + resultadoSuma);

        double valorPi = obtenerPi();
        System.out.println("El valor de Pi es: " + valorPi);

        ejemploFuncionJava();

        mostrarVariables();

        int solucion = transformador("alexis","diaz");
        System.out.println("NUMERO DE VECES QUE SE IMPRESO EL NUMERO Y NO EL TEXTO: " + solucion);

        // 7. ¿Se pueden definir funciones dentro de funciones en Java?
        // Java NO permite definir funciones dentro de otras funciones directamente.
        // Sin embargo, podemos usar clases anónimas o funciones lambda en ciertos casos.
    }

    /*    DIFICULTAD EXTRA (opcional):
    *     Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    *   - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
    *
    * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
    * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.*/



        public static int transformador (String cadena1, String cadena2){
            int contadorNumeros = 0;
            for (int i = 1; i <= 100; i++) {
                if (i % 3 == 0 && i % 5 == 0) {
                    System.out.println(cadena1 + cadena2);
                } else if (i % 3 == 0) {
                    System.out.println(cadena1);
                } else if (i % 5 == 0) {
                    System.out.println(cadena2);
                }else {
                    System.out.println(i);
                    contadorNumeros++;
                }
            }
            return contadorNumeros;

        }
    
}
