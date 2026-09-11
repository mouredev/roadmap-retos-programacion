

public class DennisGD94 {
    public static void main(String[] args) {

        System.out.println("FUNCIÓN SIN PARÁMETROS NI RETORNO");

        sayHello();

        System.out.println("FUNCIÓN CON UN PARÁMETRO");

        sayHelloTo("Dennis");

        System.out.println("FUNCIÓN CON VARIOS PARÁMETROS");

        sum(12, 8);

        System.out.println("FUNCIÓN CON RETORNO");

        System.out.println(multiplicar(7, 4));

        System.out.println("FUNCIÓN DENTRO DE UNA FUNCIÓN: " + "Java no permite métodos anidados");

        System.out.println("FUNCIÓN YA CREADAS EN JAVA");

        System.out.println(Math.max(12, 34));
        System.out.println(Math.sqrt(67.9));
        System.out.println("Java".toUpperCase());
        System.out.println(Integer.parseInt("25"));

        System.out.println("RETO EXTRA");
        System.out.println(printFizzBuzz("Fizz ", "Buzz"));






    }
    public static void sayHello(){
        System.out.println("Hello Java!");
    }

    public static void sayHelloTo(String name){
        System.out.println("Hello " + name);
    }

    public static void sum(int a, int b){
        System.out.println(a + b);
    }

    public static int multiplicar(int a, int b){
        return a * b;
    }

    public static int printFizzBuzz(String num1, String num2){

        int count = 0;
        for(int i = 1; i <= 100; i++){
            if((i % 3 == 0) && (i % 5 == 0)){
                System.out.println(num1 + num2);
            } else if (i % 3 == 0) {
                System.out.println(num1);
            }else if(i % 5 == 0){
                System.out.println(num2);
            }else {
                System.out.println(i);
                count++;
            }

        }
        return count;

    }


}
