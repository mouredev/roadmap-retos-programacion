/**
 * Solución del reto #02 FUNCIONES Y ALCANCE.
 *
 * @author AbelADE
 */
public abstract class AbelADE {  

    /**
     * Diferentes típos de funciones (en Java, métodos, que suelen estar asociados a objetos.): 
     *       -- Estructura: modificador retorno nombre (parámetros). 
     *       -- Tipos de métodos: 
     *              * Métodos sin retorno. 
     *              * Métodos con retorno.         
     *              * Métodos sin parámetros 
     *              * Métodos con parámetros. 
     *              * Métodos estáticos (no están asociados a objetos). 
     *              * Métodos constructores: Se utilizan para inicializar un objeto cuando se crea. 
     *              * Métodos abstractos: Se declaran en clases abstractas y deben ser implementados por las subclases.
     */
    
    
    /**
     * Ejemplo de Método sin retorno y sin parámetros.
     */
    public void hola() {
        System.out.println("Hola!");
    }
    
    /**
     * Ejemplo de Método sin retorno, con parámetros.
     * 
     * @param hola un texto.
     */
    public void hola(String hola) {
        System.out.println(hola);
    }

    /**
     * Ejemplo de Método con retorno y sin parámetros.
     *
     * @return un texto con un hola mundo.
     */
    public String holaMundo() {
        return "¡Hola, Mundo!";
    }
    
    /**
     * Ejemplo de Método con retorno y parámetros.
     *
     * @param hola un texto.
     * @return un texto con un hola mundo.
     */
    public String holaMundo(String hola) {
        return hola + ", Mundo!";
    }

    /**
     * Ejemplo de un método estático que devuelve el número PI. 
     * @return el número PI.
     */
    public static double calcularPI() {
        return Math.PI;
    }

    /**
     * Ejemplo de método constructor sin parámetros. 
     * Se utilizan para inicializar un objeto cuando se crea.
     */
    public AbelADE() {
    }
    
    /**
     * Ejemplo de un método abstracto. 
     * No se implementa ninguna lógica en estos métodos, pero una clase que
     * quiera ser hija desta, deberá implementarlo.
     * 
     * @return un texto.
     */
    public abstract String adios(); 
    
   /**
    * En java no se pueden crear métodos dentro de métodos (anidados).
    * Lo que se puede hacer es crear un objeto que tenga un método abstracto
    * (lo cual te obliga a tener que implementar ese método). 
    * Las clases que pueden tener métodos abstractos son las clases abstractas
    * y las interfaces.
    * 
    * @return un texto de despedida.
    */
    public String despedida(){
        //Creo una clase abstracta
        AbelADE claseAbstracta = new AbelADE() {
            @Override
            //Sobrescribo su método
            public String adios() {
                //Variable local o de método.
                String adios = "adios";
                return adios;
            }
        };
        
        /*No podemos devolver la variable adios, ya que sólo existe
        dentro del método adios de la claseAbstracta. Hacer lo siguiente:
        return adios; 
        sería un error*/
        
        //Uso el método anterior en el método actual.
        return claseAbstracta.adios();
    }
    
    //Variable a nivel de clase, conocida cómo atributo o variable global.
    private String nombre = "AbelAde";
    
    /**
     * DIFICULTAD EXTRA (Ejercicio fizz buzz)
     * 
     * Una función que imprima los números del 1 al 100, pero si el número es
     * múltiplo de 3, muestre una palabra, si es múltiplo de 5 muestre otra 
     * y si es múltiplo de los dos muestre las dos palabras.
     *
     * @param texto1 el texto para los divisores de 3.
     * @param texto2 el texto para los divisores de 5.
     * @return el número de veces que mostró números y no texto.
     */
    public int funcion(String texto1, String texto2){
        int counter = 0;
        for (int i = 0; i < 100; i++) {
            String result = "";
            result += i%3==0? texto1 + " " : "";
            result += i%5==0? texto2 : "";
            if (result.isBlank()) {
                result = Integer.toString(i);
                counter ++;
            }
            System.out.println(result);
        }
        return counter;
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        /**
        * Java es un lenguaje orientado a objetos que trae
        * una serie de clases y métodos incorporados. Una de las clases
        * más usadas es la clase String. Vamos a usar una función de 
        * esta clase.
        */
        String hola = "hola";
        
        //Devuelve el primer carácter del texto.
        char caracter = hola.charAt(0);
        
        AbelADE abelADE = new AbelADE() {
            @Override
            public String adios() {
                return "adios";
            }
        };
        
        //Imprimimos la variable global
        System.out.println(abelADE.nombre);
        
        //Sacamos por pantalla el valor de los métodos anteriores
        System.out.println(abelADE.adios());
        abelADE.hola();
        abelADE.hola("hola2");
        System.out.println(abelADE.holaMundo());
        System.out.println(abelADE.holaMundo("hola"));
        System.out.println(calcularPI());
        System.out.println(abelADE.despedida());
        
        System.out.println();
        
        System.out.println("DIFICULTAD EXTRA");
        int numeros = abelADE.funcion("fizz", "buzz");
        System.out.println("numeros: " + numeros);
    }
    
}
