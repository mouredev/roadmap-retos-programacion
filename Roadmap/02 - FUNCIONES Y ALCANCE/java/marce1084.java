import java.util.Scanner;

public class marce1084 {
    public static void main(String[] args) {

        //a)
        saludar();

        //b)
        saludar2("Juan");

        //c)
        sumar(4,7,2);

        //d)
        int numero = obtenerNumero();
        System.out.println("El número es: " + numero);

        //e)
        int numero2 = cuadrado(4);
        System.out.println("El cuadrado es: " + numero2);

        //f)
        int operacion = cuenta (3,7,1);
        System.out.println("El resultado es: " + operacion);

        //g)
        String resultado = concatenar("Saludos ",2024);
        System.out.println("El resultado es: " + resultado);

        //2)
        marce1084 marce1084 = new marce1084();
        marce1084.primeraFcion();

        //3) Ejemplo de funciones ya creadas en el lenguaje.
        //a) Clase Math
        double a = 5.3;
        double b = 1.2;
        //Exponenciación
        double potencia = Math.pow(a,b);
        System.out.println(a + " elevado a " + b + " es = " + potencia);

        //Valor absoluto
        double negativo = -5.0;
        double absoluto = Math.abs(negativo);
        System.out.println("El valor absoluto de " + negativo + " es " + absoluto);

        //b) Clase String
        String texto = "Hola, mundo!";

        // Longitud de la cadena
        int longitud = texto.length();
        System.out.println("Longitud: " + longitud);

        // Subcadena
        String subcadena = texto.substring(0, 4);
        System.out.println("Subcadena: " + subcadena);

        // 4) Funciones Global y Local
        //a) Local: variableLocal es una variable local al método Funciones. No puede ser accesible fuera de este método.
        marce1084 ejemploVariableLocal = new marce1084();
        ejemploVariableLocal.variableLocal();

        //b) Global: Variables estáticas es similar a las variables globales
        marce1084.incrementar(); //La invoco para incrementar la variable
        marce1084.mostrarValor(); //El valor de la variable global es 1

        // 8) Ejercicio extra
        System.out.println(contarCaracteres("texto1 ","texto2"));

    }

    //1) Ejemplos de funciones básicas

    //a) Función sin parámetros y sin retorno
    public static void saludar() {
        System.out.println("Hola a todos");
    };
    //b) Función con un parámetro y sin retorno
    static void saludar2(String nombre) {
        System.out.println("Hola " + nombre);
    }
    //c) Función con varios parámetros y sin retorno
    public static void sumar(int a, int b, int c) {
        System.out.println(a + b + c);
    }
    //d) Función sin parámetros y con retorno
    public static int obtenerNumero() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el numero: ");
        int numero = sc.nextInt();
        return numero;
    }
    //e) Función con un parámetro y con retorno
    public static int cuadrado(int n) {
        return (n * n);
    }
    //f) Función con varios parámetros y con retorno
    public static int cuenta(int a, int b, int c) {
        return (a + b + c);
    }
    //g) Función con parámetros de diferentes tipos y con retorno
    public static String concatenar(String a, int b) {
        return a + b;
    }

    /*2) Las funciones dentro de funciones en JAVA no existen tal como en PYTHON. Algo similar es hacer la llamada de función, donde
    una función invoca a otra*/
    public void primeraFcion() {
        System.out.println("Hola, soy la primera función");
        segundaFcion();
    }
    public void segundaFcion() {
        System.out.println("Y yo soy la segunda función");
    }

    /*4) En Java técnicamente no existen variables globales como en Python, las variables de instancia y las variables estáticas
     se consideran como variables "globales" debido a su alcance dentro de una clase y entre instancias. */
    //a) Local
    public void variableLocal() {
        int local = 32; //variable local
        System.out.println("El valor de una variable local es: " + local);
    }
    //b) Global
    private static int estatica; //variable global
    public static void incrementar(){
        estatica++;
    }
    public static void mostrarValor(){
        System.out.println("El valor de la variable global es: " + estatica);
    }

    //8)
    /*Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
     * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
     *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
     *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
     *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
     *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
     */
    public static int contarCaracteres(String text1, String text2) {
        int count = 0;
        for (int i = 0; i <= 100; i++) {
            if (i %3 == 0 && i %5 == 0) {
                System.out.println(text1 + text2);
            } else if (i %3 == 0){
                System.out.println(text1);
            } else if (i %5 == 0) {
                System.out.println(text2);
            } else {
                System.out.println(i);
                count ++;
            }
        }
        return count;
    }
}
