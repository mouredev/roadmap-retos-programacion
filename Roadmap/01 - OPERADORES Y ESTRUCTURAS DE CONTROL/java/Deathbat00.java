//DeathbatO 
import java.util.Scanner;

public class Reto1 {
    public static void main(String[] args) {
        // Declaracion de variables que se usaran en el codigo
        Scanner sc = new Scanner(System.in);
        int a, b, c, d, t, x, k, num;
        boolean bite1, bite2;
        char vocal;

        ////-------- Operadores ---------////

        //-- Aritmeticos --//
        a = 5;
        b = 10;
        int sum = a + b;
        int res = a - b;
        int mult = a * b;
        int div = a / b;
        int mod = a % b;
        /* Con el siguiente print se podra visualizar el resultado de cualquier
        operacion realizada en esta seccion reemplazando la que esta como ejemplo*/
        System.out.println("Ejemplo de Operador Aritmetico: "+mult);


        //-- Comparacion --//
        c = 5;
        d = 9;
        boolean OpIgual = c == d;
        boolean OpDesigualdad = c != d;
        boolean OpMayorQue = c > d;
        boolean OpMenorQue = c < d;
        boolean OpMayoroIgual = c >= d;
        boolean OpMenoroIgual = c <= d;
        /* Con el siguiente print se podra visualizar el resultado de cualquier
        operacion realizada en esta seccion reemplazando la que esta como ejemplo*/
        System.out.println("Ejemplo de Operdaor de Comparacion (Mayor)"+OpMayorQue);


         //-- Logicos --//
        bite1 = true;
        bite2 = false;
        boolean OperadorAnd = bite1 && bite1;
        boolean OperdorOr = bite1 || bite2;
        boolean OperdaorNot = !bite1;
        /* Con el siguiente print se podra visualizar el resultado de cualquier
        operacion realizada en esta seccion reemplazando la que esta como ejemplo*/
        System.out.println("Ejemplo de Operador Logico (Not): "+OperdaorNot);


        //-- Asignacion --//
        //Asignacion simple
        t = 100; // se asigna un valor de 100 a la variable 't'
        //Asignacion de suma
        t += 2; // Toma el valor que ya tenia y le suma 2
        //Asignacion de resta
        t -= 2; // Toma el valor que ya tenia y le resta 2
        //Asignacion de multiplicacion
        t *= 2; //Toma el valor que ya tenia y le multiplica 2
        //Asignacion de division
        t /= 2; // Toma el valor que ya tiene y lo divide entre 2
        //Asignacion de modulo
        t %= 2; // Toma el valor que ya tiene y hace la operacion de modulo
        //Asignacion de multiplicacion exponencial
        t <<= 2; //Toma el valor que ya tiene y multiplica por 2 elevado a la 2



        //-- Bits --//
        boolean OpBitAnd = bite1 & bite2;
        boolean OpBitOr = bite1 | bite2;
        boolean OpBitXor = bite1 ^ bite2;
        boolean OpBitNot = !bite1;
        /* Con el siguiente print se podra visualizar el resultado de cualquier
        operacion realizada en esta seccion reemplazando la que esta como ejemplo*/
        System.out.println("Ejemplo de Operador de Bits (Xor): "+OpBitXor);


        ////-------- Estructuras de Control ---------////

        //-- Condicionales --//
        System.out.print("Por favor digita un numero entero para compararlo con 20: ");
        x = sc.nextInt(); sc.nextLine();
        if(x > 20){
            System.out.print("\nEl numero es mayor a 20");
        }else if(x < 20){
            System.out.print("\nEl numero es menor a 20");
        }else{
            System.out.print("\nEl numero es 20");
        }


        System.out.println("\nAhora por favor digita una volcal: ");
        vocal = sc.nextLine().toUpperCase().charAt(0);

        switch(vocal){
            case 'A':
                System.out.println("Vocal A");
                break;
            case 'E':
                System.err.println("Vocal E");
                break;
            case 'I':
                System.out.println("Vocal I");
                break;
            case 'O':
                System.out.println("Vocal O");
                break;
            case 'U':
                System.out.println("Vocal U");
                break;
            default:
                System.out.println("Eso no es una vocal");
                break;
        }

        //-- Iterativas --//
        
        //Imprime los numero pares desde el 0 hasta el 12
        for(int i = 0; i <= 12; i++){
            if(i % 2 == 0){
                System.out.print(i+" ");
            }
        }
        System.out.println("");
        //Imprime los numeros multiplos de 3 desde el 0 hasta el 15
        k = 0;
        while(k <= 15){
            if(k % 3 == 0){
                System.out.print(k+" ");
            }
            k++;
        }
        System.out.println("");

        //-- Excepciones --//
        
        try{
            System.out.print("Por favor ingrese un numero entero: ");
            num = sc.nextInt(); 
            System.out.print("\nEl numero que ingreso es la mitad de: "+(num*2)+"\n");
        }catch(Exception e){
            System.out.println("ERROR---. Eso no era un numero\n");
        }finally{
            sc.close();
        }

        ////-------- Reto Extra ---------////

        //-- Ejercicio con For --//

        System.out.println("Ejercicio con For");

        for(int i = 10; i < 56; i++){
            if(i % 2 == 0 && i != 16 && i % 3 == 0){
                System.out.print(i+" ");
            }
        }
        System.out.println("");

        //-- Ejercicio con while --//

        System.out.println("ejercicio con while");
        k = 10;
        while(k <= 55){
            if(k % 2 == 0 && k != 16 && k % 3 == 0){
                System.out.print(k+" ");
            }
            k++;
        }
    }
}
