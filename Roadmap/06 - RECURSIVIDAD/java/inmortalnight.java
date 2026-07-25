// 06 - Recursividad

public class inmortalnight {
    public static void main(String[] args){
        print();
        System.out.println(factorial(3));
        System.out.println(fibonacci(30));
    }
    //Función de recursividad que imprime los números 100-0
    public static void print(){
        for(int i=100; i>=0; i--){      
            System.out.println(i);
        }
    }
    //EXTRA 1: Calcular factorial
    public static int factorial(int number){
        if (number == 0) {
            return 1;
        } else {
            return number * factorial(number - 1);
        }
    }
    //EXTRA 2: Calcular el valor según la posición introducida en la sucesión de Fibonacci
    public static int fibonacci(int position){
        if(position < 2){
            return position;
        } else {
            return fibonacci(position - 1) + fibonacci(position - 2);
        }
    }
}