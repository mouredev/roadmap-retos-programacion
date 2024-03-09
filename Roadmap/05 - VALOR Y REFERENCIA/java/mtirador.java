import java.util.Arrays;

public class mtirador {
    public static void main(String[] args) {
        

 /*ASIGNACIÓN POR VALOR */

    int a= 3;
    int b=a; //se copia el valor de a en b
    b=10; //se cambia el valor de b
    System.out.println("a ---> "+a); //a sigue siendo 3
    System.out.println("b ---> "+ b);

    /*ASIGNACIÓN POR REFERENCIA */
    //cuando trabajamos con arreglos  int[] arr2= arr1; lo que hacemos es apuntar a la misma ubicación de memoria,entonces cualquier cambio en arr2 se refleja en arr1

    int[] arr1= {3,6,1};
    int[] arr2= arr1;
    System.out.println("arr1--> "+ Arrays.toString(arr1));
    System.out.println("arr2---> "+ Arrays.toString(arr2));
    arr2[0] =7;
    System.out.println("arr1--> "+ Arrays.toString(arr1));
    System.out.println("arr2---> "+ Arrays.toString(arr2));



/*Ejercicio extra */

 // Intercambio por valor
    int z = 3;
    int x = 7;

    int[] nuevosValores = cambioVariables(z, x);
    int newZ = nuevosValores[0];
    int newX= nuevosValores[1];

    System.out.println("Valores originales: z = " + z + ", x = " + x);
    System.out.println("Nuevos valores después del intercambio: nuevo Z = " + newZ + ", nuevo X = " + newX);


// Intercambio por referencia
    int[] num1 = {5};
    int[] num2 = {10};
    System.out.println("Valores originales : num1[0] = " + num1[0] + ", num2[0] = " + num2[0]);  
 
    intercambiarPorReferencia(num1, num2);
    int newNum1 = num1[0];
    int newNum2 = num2[0];
            
 
    System.out.println("Nuevos valores después del intercambio: newNum1 = " + newNum1 + ", newNum2 = " + newNum2);

    }//fin main

    static int[] cambioVariables(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    return new int[] {a, b};
    }

 
   static void intercambiarPorReferencia(int[] array1, int[] array2) {
     int temp = array1[0];
     array1[0] = array2[0];
     array2[0] = temp;
   }

    
        
       
    
    
   
    
}
