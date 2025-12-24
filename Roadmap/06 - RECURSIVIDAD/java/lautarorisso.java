public class LogicaJava06 {
    
    public static void main(String[] args) {
        // 1.
        cuentaAtras(10);
        
        // EXTRA
        factorial(3);
        
        fibonacci(3);
    }
    
    // 1.
    public static int cuentaAtras(int num) {
        if (num>=0) {
            System.out.println(num);
            cuentaAtras(num - 1);
        }
        return num;
    }
    
    // EXTRA    
    public static int factorial(int num) {
        if (num<0) {
            return 0;
        } else if (num==0 || num==1) {
            return 1;
        } else {
            return num * factorial(num-1);
        }
    }
    
    // en fibonacci hablamos de posiciones
    public static int fibonacci(int num) {
        if (num<=1) {
            return 0;
        } else if (num==2) {
            return 1;
        } else {
            return fibonacci(num-1) + fibonacci(num-2);
        }
    }
}
