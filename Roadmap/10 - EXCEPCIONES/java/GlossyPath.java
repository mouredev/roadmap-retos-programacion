/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 * 
 * @author GlossyPath
 * 
 * @version v1.0
 * 
 * @since 09/10/2024
 * 
 */

class ExcepcionSigno extends Exception{

    public ExcepcionSigno (String msg){
        super(msg);
    }
}




public class GlossyPath {

    public static double operacionesAritmeticas(String signo, int num1, int num2) throws ExcepcionSigno, ArithmeticException, IllegalArgumentException{

        double total;

        if( !signo.equals("+") && !signo.equals("-") && !signo.equals("*") && !signo.equals("/")) {
            throw new ExcepcionSigno ("El signo introducido no es valido");
        }

        if(signo.equals("/") && num2 == 0 ) {
            throw new ArithmeticException ("No se puede dividir por 0");
        }

        if (num1 < 0 || num2 < 0) {
            throw new IllegalArgumentException("Los números no pueden ser negativos");
        }

        switch(signo){

            case("+"):
                return total = num1 + num2;
            
            case("-"):
                return total= num1 - num2;

            case "*":
                return total = num1 * num2;
    
            case "/":
                return total = num1 / num2; 
        
            default:
                throw new Error("Error: Operador no válido.");
            }   
        }




    public static void division(double num1, double num2) throws ArithmeticException {

        double total;

        if(num2 == 0){
            throw new ArithmeticException (" No se puede dividir por 0");
        }

        total = num1 / num2;

       System.out.println("El resultado es: " + total); 
    }




    public static void main(String[] args) {

        double resultadoOperaciones = 0;
        
        boolean errores = false;

        try {
          division(10, 0);

        } catch (ArithmeticException e) {
            e.printStackTrace();
        }

        try {
            //resultadoOperaciones = operacionesAritmeticas("+", 10, 20);
            //resultadoOperaciones = operacionesAritmeticas("a", 10, 20);
            resultadoOperaciones = operacionesAritmeticas("/", 20, 0);


        } catch (ExcepcionSigno e) {
            System.err.println("Error en el signo: " + e.getMessage());
            errores = true; 

        } catch (ArithmeticException e) {
            System.err.println("Error aritmético: " + e.getMessage());
            errores = true; 

        } catch (IllegalArgumentException e) {
            System.err.println("Error de argumento: " + e.getMessage());
            errores = true; 

        }

        if (!errores) {
            System.out.println("\nEl resultado del método operacionesAritmeticas es: " + resultadoOperaciones);
            System.out.println("No se ha producido ningún error.");
        }

        System.out.println("\nLa ejecución ha finalizado.");

    }
}


