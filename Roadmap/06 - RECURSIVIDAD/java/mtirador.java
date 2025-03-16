public class mtirador {
    public static void main(String[] args) {
        
      
        

        /*Del 100 al 0 */
        int dato=100;
        ejemplo(dato);

      
        /*Factorial */
         int num=5;
         factorial(num); 

        /*fibonacci */
         int pos=4;
         int resultado = fibonacci(pos);
         System.out.println("El término en la posición " + pos + " de la secuencia de Fibonacci es: " + resultado);
     }
        
        static int fibonacci(int pos) {
            
            if (pos <= 0) {
            } else if (pos == 1) {
                 return 0; 
            } else if (pos == 2) {
                   return 1; 
            } else {
                return fibonacci(pos - 1) + fibonacci(pos - 2); 
            }
            return pos;
        }
        
        

        static void factorial(int a){
          int factorial=1;

          for(int i=1;i<=a;i++){
                factorial*=i;
                
          }
          System.out.println("factorial es "+ factorial);
        }

      static void ejemplo(int a){
            if(a>=0){
                System.out.println(a);
                ejemplo(a-1);
            }
        }


        
}
