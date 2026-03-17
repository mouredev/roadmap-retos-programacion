public class GuillermoMunoz {
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

    // Variables globales (ámbito de clase)
    static String variableGlobal = "Java";
    static int contadorGlobal = 0;
    public static void main(String[] args) {
        // VARIABLES LOCALES (ámbito de main)
        int contadorLocal = 0;
        System.out.println("=== EJEMPLOS DE FUNCIONES ===\n");
        
        // 1. Función sin parámetros y sin retorno
        System.out.println("1. Función sin parámetros y sin retorno:");
        andar();

        // 2. Funcion con parametros y sin retorno
        System.out.println("\n2. Función con parámetros y sin retorno:");
        andar("la ciudad"); 

        // 3. Función con retorno y sin parametros
        System.out.println("\n3. Función con retorno y sin parámetros:");       
        String saludo = saludar();
        System.out.println(saludo);

        // 4. Funcion con retorno y con parametros
        System.out.println("\n4. Función con retorno y con parámetros:");
        System.out.println(saludar("Guillermo"));

        // 5. Funcion con numero variable dce argumentos
        System.out.println("\n5. Función con número variable de argumentos:");
        variosSaludos("Ana", "Luis", "Carlos");

        // 6. Funciones dentro de funciones
        System.out.println("\n6. Funciones dentro de funciones:");
        funcionPrincipal();

        // 7. Funciones ya creadas en el lenguaje
        System.out.println("\n7. Funciones ya creadas en el lenguaje:");
        String texto = "Hola MoureDev";
        System.out.println("Longitud del texto: " + texto.length());
        
        // 8. Variable global y local
        System.out.println("\n8. Variable global y local:");
        System.out.println("Variable global: " + variableGlobal);
        System.out.println("Contador global antes: " + contadorGlobal);
        contadorGlobal++;
        System.out.println("Contador global después: " + contadorGlobal);
        System.out.println("Contador local: " + contadorLocal);

        // Ejercicio extra
        System.out.println("\n=== EJERCICIO EXTRA ===");
        int vecesImpresas = ejercicioExtra("hola", "mundo");
        System.out.println("Número de veces que se imprime un número en lugar de texto: " + vecesImpresas);


    }
    // Función sin parametros y sin retorno
        static void andar() {
            System.out.println("Estoy andando");
        }

        // Funcion con parametros y sin retorno
        static void andar(String lugar) {
            System.out.println("Estoy andando en; " + lugar);
        }

        // Función con retorno y sin parametros
        static String saludar() {
            return "Hola, soy una función con retorno";
        }

        // Función con retorno y con parametros
        static String saludar(String name) {
            return "hola,  " + name;
        }

        // Función con número variable de argumentos
        static void variosSaludos(String... nameStrings) {
            for (String name: nameStrings) {
                System.out.println("Hola, " + name );
            }
        }

        // Fuynciones dentro de funciones
        static void funcionPrincipal(){
            andar();
            System.out.println("Funcion interna");
        }

        // Ejercicio estra

        static int ejercicioExtra(String texto1, String texto2) {
            int contadorNumeros = 0;
        
            for ( int i = 1; i <= 100; i++) {

                if(i % 3 == 0 && i % 5 == 0){
                    System.out.println(texto1 + texto2);
                        contadorNumeros++;
                }else if (i % 3 == 0){
                    System.out.println(texto1);
                    contadorNumeros++;
                }else if(i % 5 == 0){
                    System.out.println(texto2);
                    contadorNumeros++;
                }else{
                    System.out.println(i);
                }
        }
        return contadorNumeros;
        }


    }

