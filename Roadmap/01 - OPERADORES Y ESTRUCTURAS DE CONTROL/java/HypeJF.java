import java.util.Scanner;
public class HypeJF {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //OPERADORES ARITMETICOS
        int suma = 5+2;
        int diferencia = 10-2;
        int producto = 3*3;
        int cociente= 20/2;
        int modulo= 20%2;

        //OPERADORES DE COMPARACION
        if(3== suma){
            System.out.println("3 es igual a " + suma);
        } else if (3 != suma){
            System.out.println("3 es diferente  a " + suma);
        }
        if (3 > diferencia){
            System.out.println("3 es mayor que " + diferencia);
        } else if (3 < diferencia){
            System.out.println("3 es menor que " + diferencia);
        }
        if (9 <= modulo){
            System.out.println("9 es menor o igual a " + modulo);
        } else if (9 >= modulo){
            System.out.println("9 es mayor o igual a " + modulo);
        }

        //OPERADORES LOGICOS O ANIDADOS

        if (3 == suma && 5 >= diferencia){
            System.out.println("Conjuncion verdadera");
        }
        if (3 == suma || 5 >= diferencia){
            System.out.println("Disyuncion verdadera");
        }
        if (!(3>=suma)){
            System.out.println("Negación verdadera");
        }

        //IDENTIDAD/PERTENENCIA

        String mensaje = "hola, mi nombre es HypeJF";
        if(mensaje.equals("hola, mi nombre es HypeJF")){
            System.out.println("El mensaje es igual");
        }

        if(mensaje instanceof String){
            System.out.println("El mensaje es un String");
        }

        //OPERADORES DE BITS (BITWISE)
        int a = 5;
        int b = 3;

        System.out.println("AND " + (a & b));
        //si ambos bits son 1, devuelve 1
        System.out.println("OR " + (a | b));
        //si almenos uno de ambos bits es 1, devuelve 1
        System.out.println("XOR " + (a ^ b));
        /* si ambos bits son diferentes, devuelve 1
        * pero si ambos bits son iguales, devuelve 0*/
        System.out.println("NOT" + ~a);
        // los 1 pasan a 0 y viceversa, invirtiendo el bit
        System.out.println("Desplazar a la izquierda " + (a << 1));
        // el bit se desplaza a la izquierda, rellena el resto con ceros

        //ESTRUCTURAS DE CONTROL
        //CONDICIONALES
        int entero = sc.nextInt();
        if(entero>3){
            System.out.println("El condicional es verdadero");
        } else if(entero<3){
            System.out.println("El condicional alterno es verdadero");
        } else {
            System.out.println("El condicional no es verdadero");
        }

        switch(suma) {
            case 1:
                System.out.println("El entero escogido es 1");
                break;
            case 2:
                System.out.println("El entero escogido es 2");
                break;
            default:
                System.out.println("El entero escogido no es 1 ni 2");
                break;
        }

        //ITERATIVOS O BUCLES
        //CONTROL DE FLUJO (BREAK Y CONTINUE)
        int i = 0;
        int[] numeros = {1,2,3};
        for(i=0;i<5;i++){
            System.out.println("ciclo for:" + i);
            if (i==3) break;
        }

        while(i<5){
            System.out.println("ciclo while:" + i);
            i++;
        }

        do {
            System.out.println("ciclo do-while:" + i);
            i++;
            if (i==2) continue;
        } while(i<5);

        for (int n :numeros){
            System.out.println("ciclo for-each:" + n);
        }

        //MANEJO DE EXCEPCIONES

        try{
            int x = 10/0;
        } catch(ArithmeticException e){
            System.out.println("Error, el entero no es divisible entre cero");
        } finally {
            System.out.println("Siempre se ejecuta");
        }

        //EJERCICIO DE DIFICULTAD EXTRA
        for (int e = 10; e < 56; e++ ){
            if(e%2==0 || e==55){
                if (e%3!=0 && e!=16){
                    System.out.println(e);
                }
            }
        }

        //NOTA: soy consciente de que es mala praxis usar variables dispersas y no al inicio.
    }
}
