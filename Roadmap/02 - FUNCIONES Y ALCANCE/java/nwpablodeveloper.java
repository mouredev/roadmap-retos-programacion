import java.time.LocalDate;
import java.time.LocalTime;
import java.util.Arrays;
import java.util.Scanner;

public class nwpablodeveloper {
    
    // variable global 
    public static int globalNumber = 98;

    // Variable local usada en la función 1. 
    
    public static void main(String[] args) {

        // 1. Función básica
        basicFunction();

        // 2. Función con retorno
        System.out.println(returnFunction());

        // 3. Función con argumentos
        argFunction( "3. Esta función recibe un String como argumento" );

        // 4. Función que recibe varios argumentos 
        argsFunction("Pablo", 35, 120.35);

        // NOTA ! JAVA NO ADMINTE ARGUMENTOS CON VALORES POR DEFECTO

        // 5. Función con argumento y retorno
        System.out.println(returnArgsFunction("Pablo", 35));

        // 6. Variables del mismo tipo
        functionVar("Mnazana", "Pera", "Kiwi", "banana", "mandarina");

        
        // 7. Función embebida
        Calculos calculo = ( nro1, nro2 ) -> nro1 + nro2;
        int resultado = calculo.sumar(35, 8);
        System.out.println("7. Función embebida");
        System.out.println("   - Resultado:  " + resultado);

        // 8. Funciones creadas de Java
        System.out.println("8. Funciones prediseñadas Java");
        System.out.println("   - De String a int: " + Integer.parseInt("2024"));
        System.out.println("   - Nro min: "         + Math.min(15, 4) );
        System.out.println("   - Nro aleatorio: "   +  Math.random() );
        System.out.println("   - texto a mayusculas".toUpperCase());
        System.out.println("   - TEXTO A MINISCULAS".toLowerCase());
        System.out.println("   - Fecha Actual: "    +  LocalDate.now() );
        System.out.println("   - Hora Actual: "     +  LocalTime.now() );

        int[] numbers = { 35, 8, 17, 53, 80, 70 };
        Arrays.sort(numbers); // Ordena el array de menor a mayor
        for( int i = 0 ; i < numbers.length; i++ ){
            System.out.println(numbers[i]);
        }

        // Funcion Scanner para leer datos ingresados por el usuario
        System.out.println("Ingres algo a la consola");
        Scanner consola = new Scanner(System.in);
        String textIn = consola.nextLine();
        System.out.println("El usuario ingreso: " + textIn);

        // EXTRA
        System.out.println(extraFunction("multipo de 3", "multiplo de 5"));

    }
    
    // 1. Función básica
    public static void basicFunction() {
        // Variable local
        String localVariable = "Esto es una variable local";
        // Esta variable solo se puede usar y modificar adentro de este scope
        localVariable = "1. Esto es un a función básica"; 
        System.out.println(localVariable);
        System.out.println("   - Esta es la variable global:  " + globalNumber);
    }
    
    // 2. Función con retorno
    public static String returnFunction(){
        return "2. Esto es un texto que retorna desde una función";
    }
    
    // 3. Función con argumentos
    public static void argFunction(String arg){
        System.out.println ( arg );
    }
    
    // 4. Función que recibe varios argumentos 
    public static void argsFunction(String name, int age, double priceWork){
        System.out.println("4. Esta funcion recibe vario argumentos de diferentes tipos");
        System.out.println("   - Me llamo " + name + " y tengo " + age + " años. El valor de mi trabajo es de " + priceWork + " el minuto");
    }

    // 5. Función con argumento y retorno
    public static String returnArgsFunction(String name, int age){
        System.out.println("5. Funcion con argumentos y retorno");
        return "   - Mi nombre es " + name + " y tengo " + age;
    }

    // 6. Función con varios argumnetos del mismo tipo
    public static void functionVar(String... fruits){
        System.out.println("6. Función con varios argumnetos del mismo tipo");
        for(String fruit : fruits ){
            System.out.println("   - " + fruit);
        }
        
    }
    
    // 7. Función embebida
    interface Calculos {
        int sumar( int nro1, int nro2 );
    }

    // EXTRA
    public static int extraFunction(String dato1, String dato2){
        int count = 0;
        for( int i = 1; i <= 100; i++ ){
            if( i % 3 == 0 && i % 5 == 0 ){
                System.out.println( i + " => Es " + dato1 + " y " + dato2);
            }else if ( i % 3 == 0) {
                System.out.println( i + " => Es " + dato1);
            }else if( i % 5 == 0){
                System.out.println( i + " => Es " + dato2);
            }else{
                System.out.println(i);
                count++;
            }
        }
        return count;
    }
}
