

public class Meir {
    public static void main(String[] args) {

      recursion(100);
      System.out.println(factorial(20));
      System.out.println(fibonacci(30));
    }
    static void recursion(int n){
        if(n<0) return;
        System.out.println(n);
        recursion(n-1);
    }

    static long factorial(int n){
        if(n==0) return 1;
        return n*factorial(n-1);
    }

    static long fibonacci(int n){
        if(n==0) return 0;
        if(n==1) return 1;
        return fibonacci(n-1)+fibonacci(n-2);
    }
}
