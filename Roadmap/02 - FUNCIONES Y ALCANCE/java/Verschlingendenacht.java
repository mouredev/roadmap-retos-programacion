public class Verschlingendenacht {

    public static void main(String[] args) {
        /*
         * TIPOS DE FUNCIONES (METODOS) EN JAVA:
         *
         * 1- Funciones void (no retornan valor)
         * 2- Funciones que retornan un tipo (int, String, etc).
         * 3- Sin parametros y sin valor de retorno
         * 4- Con parametros y sin valor de retorno
         * 5- Sin parametros y con valor de retorno
         * 6- Con parametros y con valor de retorno
         * 7- Funciones estaticas (static)
         * 8- Funciones no estaticas
         * 9- Expresiones Lambda
         * 10- Sobrecarga de Metodos o Constructores
         * */

        /*
         * SINTAXIS GENERAL DE UNA FUNCION (METODO)
         *
         * modificador_de_acceso [static] tipo_de_retorno nombreFuncion(parametros) {
         *   //Cuerpo de la funcion
         *   //return valor; (si no es void)
         * }
         * */

        /*
         * MODIFICADORES DE ACCESO
         *
         * public - accesible desde cualquier clase
         * private - accesible solo dentro de la misma clase
         * protected - accesible desde la misma clase y subclases
         * */

        imprimirResultadosPorConsola();

    }

    static public void imprimirResultadosPorConsola(){

        //ESTA FUNCION IMPRIME LOS RESULTADOS DE TODOS LOS EJERCICIOS DE ABAJO EN ORDEN

        mostrarMensaje();
        System.out.println(obtenerNombreCompleto("Juan", "Roberto"));
        saludar();
        mostrarSuma(2,4);
        System.out.println(obtenerMensaje());
        System.out.println(multiplicar(9,9));
        System.out.println(cuadrado(2));

        //CONTINUACION EJEMPLO NO ESTATICO
        Verschlingendenacht ejemploNoEstatico = new Verschlingendenacht();
        int resultado = ejemploNoEstatico.restar(10, 4);
        System.out.println(resultado);

        //CONTINUACION EJEMPLO LAMBDA
        System.out.println(suma.ejecutar(3, 4));

        //CONTINUACION EJEMPLO SOBRECARGA
        Verschlingendenacht objetoSobrecargado = new Verschlingendenacht("Alejandro", 14, 1.67f);
        objetoSobrecargado.imprimirAtributos();
        Verschlingendenacht objetoSobrecargado2 = new Verschlingendenacht("Santiago", 27);
        objetoSobrecargado2.imprimirAtributos();
        Verschlingendenacht objetoSobrecargado3 = new Verschlingendenacht("Pedro");
        objetoSobrecargado3.imprimirAtributos();

        funcionesPredefinidasJava();

        //CONTINUACION EJEMPLO LOCAL Y GLOBAL
        Verschlingendenacht obj = new Verschlingendenacht();
        obj.mostrarNumeros();  // Muestra valores antes del cambio
        obj.cambiarGlobal();   // Cambia la variable global
        obj.mostrarNumeros();  // Muestra valores después del cambio

        //EJERCICIO EXTRA
        System.out.println(ejercicioExtra("Hola", "Mundo"));
        
    }

    //EJEMPLOS

    //1- Funcion void (no retorna nada)
    //En Java usamos palabras clave que indican lo que se espera salga de nuestra funcion
    //Por ejemplo, si queremos indicar que no queremos retornar nada, usamos 'void' (vacio)
    public static void mostrarMensaje() {
        System.out.println("Hola, estamos en Java!");
    }

    //2- Funcion que retorna algo
    //Tenemos acceso a otras palabras claves para indicar el tipo de dato a retornar como:
    //void, int, String, float, etc
    public static String obtenerNombreCompleto(String nombre, String apellido) {
        return nombre + apellido;
    }

    //3- Funcion sin parametros y sin retorno
    public static void saludar() {
        System.out.println("Hola!");
    }

    //4- Funcion con parametros y sin retorno
    public static void mostrarSuma(int a, int b){
        System.out.println("La suma es: " + (a + b));
    }

    //5- Funcion sin parametros y con retorno
    public static String obtenerMensaje(){
        return "Hola mundo";
    }

    //6- Funcion con parametros y con retorno
    public static int multiplicar(int x, int y){
        return x * y;
    }

    //7- Funcion estatica
    //static se refiere a que se puede llamar sin crear un objeto de la clase en donde esta definida
    public static int cuadrado(int n){
        return n * n;
    }

    //8- Funcion no estatica (de instancia)
    //Para llamar a una funcion no estatica se requiere crear un objeto de la clase para poder llamarla
    //Instanciaremos un objeto de la clase y llamaremos este metodo de ejemplo dentro de la funcion imprirmirResultadosPorConsola
    public int restar(int a, int b){
        return a - b;
    }

    //9- Expresiones Lambda
    //Son una forma compacta y funcional de escribir funciones anonimas (es decir, sin nombre)
    //Permiten que podamos definir funciones sin nombre que podemos usar como si fuesen valores
    /*
    * SINTAXIS BASICA:
    * (parametros) -> { cuerpo de la funcion }
    *
    * REQUISITOS:
    * Para que pueda funcionar, debemos definir una interfaz
    * Haremos esto fuera de la clase
    */
    static Operacion suma = (a, b) -> a + b; //Veamos el resultado de esta expresion imprimiendo el resultado desde la funcion imprimirResultadosPorConsola

    //10- Sobrecarga de Metodos o Constructores
    //Java directamente no soporta conceptos como argumentos por defecto, en cambio, podemos obtener un efecto simulado por medio de sobrecarga de funciones
    //Definamos algunos atributos para el ejemplo
    private String nombre;
    private int edad;
    private float altura;

    public Verschlingendenacht(String nombre){
        this.nombre = nombre;
        this.edad = 24;
        this.altura = 1.74f;
    }

    public Verschlingendenacht(String nombre, int edad){
        this.nombre = nombre;
        this.edad = edad;
        this.altura = 1.74f;
    }

    public Verschlingendenacht(String nombre, int edad, float altura){
        this.nombre = nombre;
        this.edad = edad;
        this.altura = altura;
    }

    public void imprimirAtributos(){
        System.out.println(this.nombre);
        System.out.println(this.edad);
        System.out.println(this.altura);
    }

    //FUNCIONES ANIDADAS
    //Java NO permite declarar un metodo dentro de otro metodo, como si ocurre en otros lenguajes como Python o JavaScript
    //¿Pero que se usa en su lugar entonces?
    /*
    * 1- Clases internas
    * 2- Expresiones lambda (desde Java 8)
    * 3- Funciones auxiliares privadas llamadas dentro de otras funciones
    * */

    static void funcionesPredefinidasJava(){

        //EJEMPLOS DE FUNCIONES PREDEFINIDAS EN JAVA
        //Como en muchos otros lenguajes de programacion, Java tambien cuenta con funciones ya definidas dentro del lenguaje como:
        String miCadena = "Esta Es Una Cadena Para Nuestro Ejemplo";
        System.out.println(miCadena.charAt(0)); //Trata a la cadena como un arreglo y retorna el caracter almacenado en el indice especificado
        System.out.println(miCadena.toUpperCase()); //Retorna la misma cadena en mayusculas
        System.out.println(miCadena.toLowerCase()); //Retorna la misma cadena en minusculas
        System.out.println(miCadena.equals("Esta es una cadena para nuestro ejemplo")); //Retorna verdadero si la cadena equivale al parametro de la funcion

    }

    //ENFOQUE LOCAL Y GLOBAL EN JAVA
    // Variable global (de instancia)
    int numero = 10;

    public void mostrarNumeros() {
        // Variable local
        int numero = 5;

        System.out.println("Número local: " + numero);         // Imprime 5
        System.out.println("Número global: " + this.numero);   // Imprime 10
    }

    public void cambiarGlobal() {
        // Modifica la variable global
        this.numero = 20;
    }

    public Verschlingendenacht(){
    }
    //Ahora ejecutemos este ejemplo desde la funcion imprimirResultadosPorPantalla

    //DIFICULTAD EXTRA
    public static int ejercicioExtra(String cadena1, String cadena2){
        int numeroVeces = 0;
        for(int i = 1; i < 101; i++){
            if(i%3==0){
                System.out.println(cadena1);
                if(i%5==0){
                    System.out.println(cadena1+cadena2);
                }
            }else if(i%5==0){
                System.out.println(cadena2);
            }else{
                System.out.println(i);
                numeroVeces++;
            }
        }
        return numeroVeces;
    }

}


//Interfaz de soporte para ejemplo de expresiones lambda
interface Operacion {
    int ejecutar(int a, int b);
}
