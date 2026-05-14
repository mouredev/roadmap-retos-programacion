public class mariovelascodev {
    public static void main(String[] args) {
        //Recursividad

        countdown(100);
        System.out.println("\n-----Factorial-----\n");
        System.out.println(factorial(4));
        System.out.println(factorial(-7));
        System.out.println("\n-----Fibonacci-----\n");
        System.out.println(fibonacci(9));
        System.out.println(fibonacci(-3));

    }

    public static void countdown(int number){
        System.out.println(number);
        //Resta 1 al número introducido
        number -= 1;
        //Si el número es mayor o igual a 0, se vuelve a llamar a la función
        if (number >= 0){
            countdown(number);
        }
    }

    public static int factorial(int number){

        // Si el número introducido es menor que 0 retornamos 0, ya que los números negativos no son validos
        if (number < 0){
            return 0;
            //Si número es igual a 0 ó 1 retorna 1
        } else if (number == 0 || number == 1) {
            return 1;
            //Si número es mayor que uno se multiplica el número por el resultado de aplicar la función menos 1
        }else {
            return number * factorial(number - 1);
        }
    }

    public static int fibonacci(int numberPosition){
        //Si la posición es menor que 0 devuelve 0, ya que el número de posición no puede ser negativo
        if (numberPosition < 0){
            return 0;
            //Si la posición es menor o igual a 1 devuelve su número de posición
        } else if (numberPosition <= 1) {
            return numberPosition;
            /*Si el número de posición es mayor que 1, la función se llama a sí misma dos veces,
            para sumar los dos resultados y devolver el total*/
        }else{
            return fibonacci(numberPosition - 1) + fibonacci(numberPosition - 2);
        }
    }
}
