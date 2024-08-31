public class FrancoFMV{

    public static void main(String[] args) {
        
        //Operadores de asignación
        System.out.println("---Operadores de asignación---");
        int num1 = 5;
        int num2 = 2;
        int num3 = 5;
        int x = 10;
        System.out.println("num1 = "+ num1);
        System.out.println("num2 = "+ num2);
        System.out.println("num3 = "+ num3);
        System.out.println("x = "+ x);

        //Operadores arimetricos (+; -; *; /; %; ++; --) 
        System.out.println("---Operadores arimetricos (+; -; *; /; %; ++; --) ---");
        int suma= num1+num2; 
        int resta= num1-num2;
        int multipli= num1*num2;
        int divid= num1/num2;
        double mod= num1%num2;
        int sum1=  num1++;
        int rest1=  num1--;
        
        System.out.println("El resultado de " + num1 +" + "+ num2+" es: "+suma);
        System.out.println("El resultado de "+ num1 +" - "+ num2+" es: "+resta);
        System.out.println("El resultado de "+ num1 +" * "+ num2+" es: "+multipli);
        System.out.println("El resultado de "+ num1 +" / "+ num2+" es: "+divid);
        System.out.println("El resultado de "+ num1 +" % "+ num2+" es: "+mod);
        System.out.println( "El valor de "+ num1 +" incrementado en 1 es: "+sum1);
        System.out.println( "El valor de "+ num1 +" decrementado en 1 es: "+rest1);

        //Operador de comparación (==; !=; >; <; >=; <=) 
        System.out.println("---Operador de comparación (==; !=; >; <; >=; <=) ---");
        System.out.println(num1 + " == " + num3 + "? " + (num1==num3)); 
        System.out.println(num1 + " != " + num3 + "? " + (num1!=num3));
        System.out.println(num1 + " < " + num2 + "? " + (num1<num2));
        System.out.println(num2 + " > " + num3 + "? " + (num1>num2));
        System.out.println(num1 + " >= " + num2 + "? " + (num1>=num2));
        System.out.println(num1 + " <= " + num2 + "? " + (num1<=num2));

        //Operadores logicos (&&; ||; !)
        System.out.println("---Operadores logicos (&&; ||; !)---");
        System.out.println( x > 5 &&  x <= 10 ); // && = and
        System.out.println( x < 5 || x < 4 ); // || = or
        System.out.println( !(x < 5 && x < 10) ); // ! = not

        System.out.println("---Ejercicio Extra---");
        ejExtra();
    }

    public static void ejExtra(){
        for (int i = 10; i < 56; i++) {
            if((i!=16) && (i%3!=0) && (i%2==0)){
                System.err.println(i);
            }
        }
    }

}