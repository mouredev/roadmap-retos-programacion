import java.math.*;

public class simonguzman {

    static int validarParImpar = 2;
    public static void main(String[] args) {
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
        //presentation();
        //menu();
        
        /*double sum = suma(1.2, 2.4);
        System.out.println("Suma = "+sum);
        double div = division(3, 2);
        System.out.println("Division = "+div);*/
        //int fact = factorial(4);
        //System.out.println("Factorial = "+fact);
        //numeroPrimo(11);
        //double pot = potenciacion(2, 3);
        //System.out.println(pot);
        //double raiz = raizCuadrada(10);
        //System.out.println(raiz);
        numParImpar(3);
    }

    public static void presentation(){
        System.out.println("*************************");
        System.out.println("Bienvenido a la calculadora");
        System.out.println("*************************");
    }

    public static void menu(){
        System.out.println("**********MENU**********");
        System.out.println("1. Suma");
        System.out.println("2. Resta");
        System.out.println("3. Multiplicacion");
        System.out.println("4. Division");
        System.out.println("5. Modulo");
        System.out.println("6. Factorial");
        System.out.println("7. Numero par o impar");
        System.out.println("8. Raiz cuadrada");
        System.out.println("9. Potenciacion");
        System.out.println("10. Numero primo");
    }

    public static double suma(double num1, double num2){
        double sum = num1 + num2;
        return sum;
    }

    public static double resta(double num1, double num2){
        double res = num1 - num2;
        return res;
    }

    public static double multiplicacion(double num1, double num2){
        double multi = num1 * num2;
        return multi;
    }

    public static double division(double num1, double num2){
        double div = 0;
        if(num2 == 0){
            System.out.println("ERROR: no se puede realizar una division por 0");
        }else{
            div = num1 / num2;
        }
        return div;
    }

    public static double modulo(double num1, double num2){
        double mod = 0;
        if(num2 == 0){
            System.out.println("Error: modulo por cero");
        }else{
            mod = num1 % num2;
        }
        return mod;
    }

    public static int factorial(int num){
        int factorial = 1;
        if (num < 0){
            System.out.println("ERROR: No se puede hallar el factorial de un numero negativo");
        }else if (num == 0){ 
            factorial = 1;
        }else{
            for (int i = 1; i <= num; i++){
                factorial = factorial * i;
            }   
        }
        return factorial;
    }

    public static void numeroPrimo(int num1){
        boolean numprimo = true;
        for (int i = 2; i < num1; i++){
            if(num1 % i == 0){
                numprimo = false;
                break;
            }
        }
        if (numprimo) {
            System.out.println("El numero "+num1+" es primo");
        }else{
            System.out.println("El numero "+num1+" NO es primo");
        }
    }

    public static double potenciacion(int base, int exponente){
        double resultado = Math.pow(base, exponente);
        return resultado;
    }

    public static double raizCuadrada(int num){
        double raiz = Math.sqrt(num);
        return raiz;
    }

    public static void numParImpar(int num){
        if(num % validarParImpar == 0){
            System.out.println("El numero "+num+" es par");
        }else{
            System.out.println("El numero "+num+" es impar");
        }
    }   
}
