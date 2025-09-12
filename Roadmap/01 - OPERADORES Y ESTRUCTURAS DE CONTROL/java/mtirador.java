import java.util.Scanner;

public class mtirador {
    public static void main(String[] args) {

    int a=5,b=4;
     //operadores aritméticos
    
     int resta=a-b;
     int suma=a+b;
     int mult=a*b;
     int div=a/b;
     int resto=a%b;

     System.out.println("Resta: "+resta+"\nSuma: "+suma+"\nMultiplicación: "+ mult
     +"\nDivisión: "+ div+"\nResto: "+resto);

     //Operadores comparación
    
     
     System.out.println("Distinto: "+ (a!=b));
     System.out.println("Igual: "+(a==b));
     System.out.println("Menor que: "+ (a<b));
     System.out.println("Mayor que: "+ (a>b));
    
     //Operadores Asignación
     a+=9;
     System.out.println("Valor de a ahora: "+ a);
     //Identidad
     String frase= "Hola Mundo";
     System.out.println("Cadena: "+ frase);

    // Operadores de Bits
    int numBits = 5; // Representación binaria: 101
    int opAnd = numBits & 3; // Resultado: 1 (1 en binario)

    System.out.println("\nOperadores de Bits:");
    System.out.println("Operación AND Bit a Bit: " + opAnd);

    /*Estructuras de control */
    //Condicionales

    if(a>b){
        System.out.println(a+" es mayor que "+ b);
    }else{
        System.out.println(a +" es menor que "+ b);
    }

    //Iterativas

    for(int i=0;i<b;i++){
        System.out.println("Resultado del For: "+ i);

    }

    //control excepciones
    Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Ingrese el numerador: ");
            int numerador = scanner.nextInt();

            System.out.print("Ingrese el denominador: ");
            int denominador = scanner.nextInt();

            double resultado = dividir(numerador, denominador);
            System.out.println("Resultado de la división: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: División por cero no permitida");
        } catch (Exception e) {
            System.out.println("NO HA INGRESADO UN NÚMERO: " + e.getMessage());
        } finally {
            scanner.close();
        }


/** Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */ //OPCIONAL
        for(int i=10;i<=55;i++){
            if(i%2==0 && i%3!=0 && i!=16){
                System.out.println(i);

            }

        }
      

    }//fin main

    // Método para realizar la división y lanzar una excepción si se intenta dividir por cero
    private static double dividir(int numerador, int denominador) {
        if (denominador == 0) {
            throw new ArithmeticException("Intento de división por cero");
        }
        return (double) numerador / denominador;
    }


    }//fin class

   
   
    

