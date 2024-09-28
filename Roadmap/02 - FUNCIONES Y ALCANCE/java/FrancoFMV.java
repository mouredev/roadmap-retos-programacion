import java.time.LocalDateTime;
import java.util.Random;
import java.util.Scanner;

public class FrancoFMV {
    public static void main(String[] args) {
        holaMundo();
        suma(2,2);
        saludo("Franco");
        edad("Juan",18);
        System.out.println(por5(10));
        int x = 4;
        int y = 5;
        int z = multiplicacion(x,y);
        System.out.println("la multiplicacion entre "+x+"*"+y+"="+z);
        checkEdad(20);
        checkEdad(15);
        LocalDateTime ahora = LocalDateTime.now();
        System.out.println("La fecha es: " +ahora);
        System.out.println("un numero random entre 1 y 10: "+random());
        multiplScanner(y, z);
        String str1 = "Fizz";
        String str2 = "Buzz";
        ejExtra(str1, str2);
    }

    static void holaMundo(){
        System.out.println("¡Hola Mundo!");
    }

    static void suma(int a, int b){
        System.out.println("La suma de "+a+" + "+b+" es: " + (a+b));
    }

    static void saludo(String nombre){
        System.out.println("Hola, "+nombre); 
    }

    static void edad(String nombre, int edad){
        System.out.println("Mi nombre es "+nombre+", tengo "+edad+" años.");
    }

    static int por5(int x){
        return x * 5;
    }

    static int multiplicacion(int x, int y){
        return x*y;
    }

    static void checkEdad(int edad){
        if  (edad < 18) {
            System.out.println("Acceso denegado, eres menor de edad");
        }else{
            System.out.println("Acceso consedido, ya eres mayor de edad");
        }
    }

    static void localDateTime(){
        LocalDateTime now = LocalDateTime.now();
        System.out.println("Fecha y Hora actual: " + now);
    }

    static int random(){
        Random rnd = new Random();
        int n = rnd.nextInt(10) + 1; 
        return n;
    }

    static void multiplScanner(int a,int b){
        Scanner sc=new Scanner(System.in);
        System.out.print("Ingrese el primer numero: ");
        a=sc.nextInt();
        System.out.print("Ingrese el segundo numero: ");
        b=sc.nextInt();
        System.out.println("La multiplicacion es: " +multiplicacion(a,b));
        sc.close();
    }

    static void ejExtra(String str1, String str2){
        int cont=0;
        for(int i=1; i<=100; i++){
            if (i%3==0 && i%5==0){
                System.out.println(str1+str2);
            }else if(i%3==0){
                System.out.println(str1);
            }else if(i%5==0){
                System.out.println(str2);
            }else{
                System.out.println(i);
                cont++;
            }
        }
        System.out.println("Se imprimió el numero una cantidad de: "+cont+" veces");
    }
    
        
}

