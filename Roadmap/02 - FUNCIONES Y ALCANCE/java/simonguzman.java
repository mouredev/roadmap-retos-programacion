import java.math.*;
import java.util.Scanner;

public class simonguzman {

    //Variable global utilizada para el calculo del numero par e impar
    static int validarParImpar = 2;
    public static void main(String[] args) {
        //Prueba del ejercicio extra
        int numImpreso = ejercicioExtra("multiplo de 3", "multiplo de 5");
        System.out.println("Numero de veces que se ha impreso numero en lugar de las cadenas de texto: " + numImpreso);
        
        //Prueba de la calculadora en la que se encuentran todas las funciones que se puedian de requerimiento
        iniciarCalculadora();
    }

    //Funcion sin parametros ni retorno
    public static void presentation(){
        System.out.println("*************************");
        System.out.println("Bienvenido a la calculadora");
        System.out.println("*************************");
    }

    //Funcion sin parametros ni retorno
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
        System.out.println("11. Salir");
    }

    //Funcion con retorno y 2 parametros
    public static double suma(double num1, double num2){
        double sum = num1 + num2;
        return sum;
    }

    //Funcion con retorno y 2 parametros
    public static double resta(double num1, double num2){
        double res = num1 - num2;
        return res;
    }

    //Funcion con retorno y 2 parametros
    public static double multiplicacion(double num1, double num2){
        double multi = num1 * num2;
        return multi;
    }

    //Funcion con retorno y 2 parametros
    public static double division(double num1, double num2){
        double div = 0;
        if(num2 == 0){
            System.out.println("ERROR: no se puede realizar una division por 0");
        }else{
            div = num1 / num2;
        }
        return div;
    }

    //Funcion con retorno y 2 parametros
    public static double modulo(double num1, double num2){
        double mod = 0;
        if(num2 == 0){
            System.out.println("Error: modulo por cero");
        }else{
            mod = num1 % num2;
        }
        return mod;
    }

    //Funcion con retorno y 1 parametros
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

    //Funcion con 1 parametro pero sin retorno
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

    //Funcion con 2 parametros, retorno y utilizando funciones del lenguaje
    public static double potenciacion(int base, int exponente){
        double resultado = Math.pow(base, exponente);
        return resultado;
    }

    //Funcion con 1 parametro, retorno y utilizando funciones del lenguaje
    public static double raizCuadrada(int num){
        double raiz = Math.sqrt(num);
        return raiz;
    }

    //Fncion con 1 prametro y sin retorno
    public static void numParImpar(int num){
        if(num % validarParImpar == 0){
            System.out.println("El numero "+num+" es par");
        }else{
            System.out.println("El numero "+num+" es impar");
        }
    } 
    
    //Funcion con 2 parametros y sin retorno, utilizando las funciones creadas anteriormente
    public static void menuOperaciones(int opcion, Scanner scanner){
        switch (opcion) {
            case 1:
                System.out.println("Ingrese el primer sumando: ");
                double sumando1 = scanner.nextDouble();
                System.out.println("Ingrese el segundo sumando: ");
                double sumando2 = scanner.nextDouble();
                System.out.println("Resultado: "+suma(sumando1, sumando2)); 
                break;
            case 2:
                System.out.println("Ingrese el primer valor: ");
                double minuendo = scanner.nextDouble();
                System.out.println("Ingrese el segundo valor: ");
                double sustraendo = scanner.nextDouble();
                System.out.println("Diferencia: "+resta(minuendo, sustraendo));
                break;
            case 3:
                System.out.println("Ingrese el primer valor: ");
                double multiplicando = scanner.nextDouble();
                System.out.println("Ingrese el segundo valor: ");
                double multiplicador = scanner.nextDouble();
                System.out.println("Producto: "+multiplicacion(multiplicando, multiplicador));
                break;
            case 4:
                System.out.println("Ingrese el primer valor: ");
                double dividendo = scanner.nextDouble();
                System.out.println("Ingrese el segundo valor: ");
                double divisor = scanner.nextDouble();
                System.out.println("cociente: "+division(dividendo, divisor));
                break;
            case 5:
                System.out.println("Ingrese el primer valor: ");
                double dividendoModulo = scanner.nextDouble();
                System.out.println("Ingrese el segundo valor: ");
                double divisorModulo = scanner.nextDouble();
                System.out.println("Resto: "+modulo(dividendoModulo, divisorModulo));
                break;
            case 6:
                System.out.println("Ingrese el valor: ");
                int numFactorial = scanner.nextInt();
                System.out.println("Factorial: "+factorial(numFactorial));
                break;
            case 7:
                System.out.println("Ingrese el valor: ");
                int numParImpar = scanner.nextInt();
                numParImpar(numParImpar);
                break;
            case 8:
                System.out.println("Ingrese el valor: ");
                int numeroRaiz = scanner.nextInt();
                System.out.println("Raiz: "+raizCuadrada(numeroRaiz));
                break;
            case 9:
                System.out.println("Ingrese el valor de la base: ");
                int base = scanner.nextInt();
                System.out.println("Ingrese el valor del exponente: ");
                int exponente = scanner.nextInt();
                System.out.println("Potencia: "+potenciacion(base, exponente));
                break;
            case 10:
                System.out.println("Ingrese el valor: ");
                int numeroPrimo = scanner.nextInt();
                numeroPrimo(numeroPrimo);
                break;
            case 11:
                System.out.println("Saliendo de la calculadora...");
                break;
            default:
                System.out.println("ERROR: opcion no valida, ingrese un valor correcto" );
                break;
        }
    }

    //Funcion con 1 parametro y sin retonro utilizando las funciones creadas con anterioridad
    public static void menuCompleto(Scanner scanner){
        int opcion = 0;
        do{
            presentation();
            menu();
            System.out.println("Elija una opcion: ");
            opcion = scanner.nextInt();

            menuOperaciones(opcion, scanner);
        }while(opcion != 11);
    }

    //Funcion sin parametros ni retorno, utilizando funciones creadas con anterioridad
    public static void iniciarCalculadora(){
        Scanner scanner = new Scanner(System.in);
        menuCompleto(scanner);
        scanner.close();
    }

    //Ejercicio extra propuesta en la actividad, 2 parametros de texto con un retorno entero
    public static int ejercicioExtra(String text1, String text2){
        int count = 0;
        for(int i=0; i<=100; i++){
            if(i % 3 == 0){
                System.out.println(text1);
            }else if (i % 5 == 0) {
                System.out.println(text2);
            }else if(i % 3 == 0 && i % 5 ==0){
                System.out.println(text1 + " y " + text2);
            }else{
                System.out.println(i);
                count++;
            }
        }
        return count;
    }

}

