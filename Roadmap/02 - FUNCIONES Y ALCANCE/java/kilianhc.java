package retosProgramacion;

public class RetoTres {

    //Variable global (Variables de instancia y estáticas)
    String variableInstancia = "Esto es una variable de instancia";
    static String variableEstatica = "Esto es una variable estática";
    
    public static void main(String[] args) {
        saludar(); //Llamar a la función sin parámetros ni retorno
        System.out.println(saludar2()); //Llamar a la función sin parámetros pero con retorno
        saludar3("¿Cómo ", "estás?"); //Llamar a la función con parámetros y sin retorno
        System.out.println("El resultado es: " + suma(3, 5)); //Llamar a la función con parámetros y retorno
        System.out.println(mayorEdad(30)); //Llamar a la función recursiva
        datos("Kilian"); //Llamar a funcion 
        datos(30); //con sobrecarga
        RetoTres ejemplo = new RetoTres(); //Llamada
        ejemplo.local(); //a una variable local
        RetoTres instancia = new RetoTres(); //Instanciar una variable
        System.out.println(instancia.variableInstancia); //de instancia
        System.out.println(RetoTres.variableEstatica); //Acceso a la variable estática
       // instancia.local();
       ejemplos();
        System.out.println(imprimir("Mostrar ", "Texto"));
    }

    //Funciones definidas por el usuario
    //Función sin parámetros ni retorno
    public static void saludar() {
        System.out.println("Hola, Java");
    }

    //Función sin parámetros pero con retorno
    public static String saludar2() {
        return ("Hola, Kilian");
    }

    //Función con parámetros y sin retorno
    public static void saludar3(String a, String b) {
        String frase = (a + b);
        System.out.println("La frase es: " + frase);
    }

    //Función con parámetros y retorno
    public static int suma(int a, int b) {
        return a + b;
    }

    //Funcione recursiva
    public static String mayorEdad(int num) {
        if (num < 18) {
            return ("La persona es menor de edad");
        } else {
            return ("La persona es mayor de edad");
        }
    }

    //Función con sobrecarga
    public static void datos(String nombre) {
        System.out.println("Mi nombre es: " + nombre);
    }

    public static void datos(int edad) {
        System.out.println("Y mi edad es: " + edad);
    }

    //Variable local
    public void local() {
        String mensaje = "Esto es una variable local";
        System.out.println(mensaje);
    }
    
    //Algunas funciones propias del lenguaje
    public static void ejemplos() {
    String nombre = "Kilian Hernández";
        System.out.println(nombre.charAt(3));   
        System.out.println(nombre.length());
        System.out.println(nombre.toUpperCase());
        System.out.println(nombre.toLowerCase());
        System.out.println(nombre.concat(" Chirino"));
    }
    
    //Dificultad Extra
    public static int imprimir (String a, String b){
        int contador = 0;
        for (int num = 1; num <= 100; num++) {
            if (num%3 == 0 && num%5 == 0) {
                System.out.println(a+b);
            }else if (num%5 == 0) {
                System.out.println(b);
            }else if (num%3 == 0) {
                System.out.println(a);
            }else {
                System.out.println(num);
                contador++;
            }
        }
        return contador;
    }
    
}



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
