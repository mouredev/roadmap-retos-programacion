package practicas;

public class Main {
    public static void main(String[] args) {
        

        //Función sin parametro ni retorno
        System.out.println("\nFunción sin parametro ni retorno");
        saludar();

        //Función con uno o varios parametros y sin retorno
        System.out.println("\nFunción con uno o varios parametros y sin retorno");
        sumar(5, 3);

        //Función con uno o varios parametros y con retorno
        System.out.println("\nFunción con uno o varios parametros y con retorno");
        System.out.println(saludarPersona("Manolo"));

        //Función privada
        System.out.println("\nFunción privada");
        funcionPrivada(); //No se puede llamar a una función privada desde fuera de la clase, es decir, desde fuera de este archivo.

        //Función que retorna el número de letras de una palabra, haciendo uso del método ya creado .length()
        System.out.println("\nFunción que retorna el número de letras de una palabra");
        System.out.println(contarLetras("Esternocleidomastoideo"));


        /**
         * DIFICULTAD EXTRA (opcional):
         * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
         * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
         *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
         *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
         *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
         *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
         */
        System.out.println("\nDIFICULTAD EXTRA (opcional):");
        System.out.println("\nLas veces que se ha devuelto un número son: " + reto("Hola", "Adiós"));

    }
    //Función sin parametro ni retorno
    public static void saludar(){
        System.out.println("\nHola");
    }

    //Función con uno o varios parametros y sin retorno
    public static void sumar(int a, int b){
        System.out.println("\nEl resultado de la suma es: " + (a+b));
    }

    //Función con uno o varios parametros y con retorno
    public static String saludarPersona(String nombre){
        return "\nHola " + nombre;
    }

    /**
     * Si usamos public como antes son funciones a nivel global,
     * pero a continuación, vamos a hacer una función privada que solo se puede usar dentro de la clase.
     * Para ello vamos a hacer uso de la palabra reservada private.
     */

    private static void funcionPrivada(){
        System.out.println("\nSoy una función privada");
    }

    //Función que retorna el número de letras de una palabra, haciendo uso de una función ya creada, llamada .length()
    public static String contarLetras(String palabra){
        return ("\nLa palabra " + palabra + " tiene " + palabra.length() + " letras");
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
     * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
     *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
     *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
     *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
     *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
     */

    public static Integer reto(String palabra1, String palabra2){
        int contadorNumerosMostrados = 0;
        for(int i = 1; i <= 100; i++){
            if(i% 5 == 0 && i % 3 == 0){
                System.out.println(palabra1 + palabra2);
            }else if(i % 5 == 0 && i % 3 != 0){
                System.out.println(palabra2);
            }else if(i % 5 != 0 && i % 3 == 0){
                System.out.println(palabra1);
            }else{ 
                System.out.println(i);
                contadorNumerosMostrados++;
            }
        }
        return contadorNumerosMostrados;
    }
}
