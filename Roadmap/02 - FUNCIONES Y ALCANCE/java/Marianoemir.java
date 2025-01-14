import java.util.Scanner;
class Marianoemir{
    
 /*
    @author Marianoemir
    
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
 */
    /*Variables Globales
    Variables de Instancia: Se usan para almacenar datos específicos de cada objeto.
    Variables Estáticas: Se usan para almacenar información o comportamientos que deben ser comunes a todas las instancias, 
    como contadores globales, configuraciones comunes, o constantes.*/
    int variglobal = 20;
    static int varglobalconstatic = 30;

    //Las funciones en java se llaman 'metodos' tambien
    
    //Función sin retorno ni parametros
    
    //Con void y public es necesario crear un Objeto para poder ejecutarla.
    public void mostrar(){
        System.out.println("Este es un msj con public y void");
    }
    
    //Calcular valor elevado de un numero con clases predefinidas en java
    public double potencia (double a ,double b){
        return Math.pow(a, b);
    }
    
    
    //Sin static no es necesario iniciarlizar un Obj solamente hay que llamar a la función
    public static void salidadeconsola(){
        System.out.println("Msj con Static no hace falta crear ni inicializar un Obj");
    }
    //Metodo con 'parametros' y 'retornos'
    public int suma(int a, int b, int c){
        return a + b + c;
    }

    /*Ejemplo de Variables locales
    Variables Locales: Limitadas al método o bloque donde se declaran; no son accesibles fuera de ese ámbito.*/
    public int multi (int num1,int num2){
        int resultado = num1 * num2;
        return resultado;
    }

    /*DIFICULTAD EXTRA (opcional):
    * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
    * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
    * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.*/

     public int difiextar (String cade1 ,String cade2){

        int contador = 0;

       for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(cade1 + cade2);
            } else if (i % 3 == 0) {
                System.out.println(cade1);
            } else if (i % 5 == 0) {
                System.out.println(cade2);
            } else {
                contador++;  
            }
        }
        return contador;
     }
      

    public static void main(String[] args) {
        Marianoemir imprimir = new Marianoemir();
        imprimir.mostrar();
        salidadeconsola();
        int operacion = imprimir.suma(10,20,30);
        System.out.println("Metodo con retorno y parametros: "+operacion);
        
        
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduce el primer numero(la base): ");
        double  base = scanner.nextDouble();
        
        
        System.out.println("Introduce el segundo numero(el exponente): ");
        double  exponente = scanner.nextDouble();
        System.out.println("");
        System.out.println("El resultado de tu numero elevado es: "+imprimir.potencia(base, exponente));

        /* EJemplo con variables locales

        Se declaran dentro de un método, constructor o bloque de código.
        Solo son accesibles dentro del método, constructor o bloque donde se declaran.
        Se crean cuando se entra en el bloque de código y se destruyen cuando se sale.*/

        System.out.println("El resultado de la multiplicacion entre variables locales es: "+imprimir.multi(5, 5));

        //Ejemplos de variables globales

        System.out.println("Variable global accedida desde instancia de clase: "+imprimir.variglobal);
        System.out.println("Ejemplo de variable global con static: "+varglobalconstatic);

        //Ejercicio extra ejecución

        int resulfunc = imprimir.difiextar("Hola", " Espero que tengas un buen dia");

        System.out.println("El numero de veces que se imprimio el numero es: "+resulfunc);
        

        
        
    }
}