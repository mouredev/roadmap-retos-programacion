/* 
* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
*/


/*
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
*/

/*
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
*/

import java.util.ArrayList;

public class kuroz00{
    public static void aritmetics(int numero_a,int numero_b){
        System.out.println(numero_a + numero_b);
        System.out.println(numero_a - numero_b);
        System.out.println(numero_a * numero_b);
        System.out.println(numero_a / numero_b);
        System.out.println(numero_a % numero_b);

        System.out.println("---------"); //Tambien se puede trabajar de la sig forma:
        
      //  System.out.println(numero_a += numero_b);
      //  System.out.println(numero_a -= numero_b);
      //  System.out.println(numero_a *= numero_b);
      //  System.out.println(numero_a /= numero_b);
      //  System.out.println(numero_a %= numero_b);
    }

    public static void logics(boolean bool_a,boolean bool_b){
        if (bool_a && bool_b == true){
            System.out.println("Resultado segun parametros otorgados: AND");
        }  else if(bool_a || bool_b != true ){
            System.out.println("Resultado segun parametros otorgados: OR");
        } //Tambien esta el NOT, cuya funcion es negar el booleano entregado.
    }

    public static void compareishon(int num1, int num2){      
        if (num1 > num2){
            System.out.println("Numero1: " + num1 + " > " + "Numero 2:" + num2);             
        } 
        else{
            System.out.println("Numero1: " + num1 + " < " + "Numero 2:" + num2);              
        }     
    }
    public static void teneichon(){
        try{
            String[] days = {"lunes", "martes", "miercoles", "jueves", "sabado", "domingo" }; //List cn dias de la semana, sin el viernes
            System.out.println(days[6]); //Intero imprimir el indice del ultimo dia (sup que son 7)
        } catch(Exception e){
            System.out.println("Excepcion detectada");
        }
    }

    public static void biteichon(){
        int x = 25; //11001
        int a = 5; //0101
        int b = 9; //1001
        //Desplazamiento a la izquierda
        System.out.println(x << 2);
        //Desplazamiento a la derecha
        System.out.println(x >> 2);
        //AND
        System.out.println(a & b);
        //OR
        System.out.println(a | b);
        //XOR
        System.out.println(a ^ b);
        //NOT
        System.out.println(~a);
        System.out.println(~b);
    }

    public static void main(String[] args){
        //Aritmeticos
        int numero_a = 5;
        int numero_b = 2;
        System.out.println("°°°°°°°°°°°°°°°°.-.-Aritmetics-.-°°°°°°°°°°°°°°°°°");
        aritmetics(numero_a, numero_b);

        //Logicos
        System.out.println("°°°°°°°°°°°°°°°-.-Logicos-.-°°°°°°°°°°°°°°°°°°");
        logics(false, false);

        //Comparacion y asignacion
        System.out.println("°°°°°°°°°°°°°°°-.-Comparacion.-°°°°°°°°°°°°°°°°°°");
        compareishon(numero_a, numero_b);

        //Pertenencia
        System.out.println("°°°°°°°°°°°°°°°-.-Pertenencia.-°°°°°°°°°°°°°°°°°°");
        teneichon();

        //Bits
        System.out.println("°°°°°°°°°°°°°°°-.-Bits.-°°°°°°°°°°°°°°°°°°");
        biteichon();


        //Dificultad extra ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
        System.out.println("°°°°°°°°°°°°°°°-.-D.F.-°°°°°°°°°°°°°°°°°°");
        for(int i = 0; i < 50; i++){
            if ((i % 2 == 0) && (i % 3 != 0) && (i != 16)){
                System.out.print(i + " ");
            } 
        }


    }
}

/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *~`^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */