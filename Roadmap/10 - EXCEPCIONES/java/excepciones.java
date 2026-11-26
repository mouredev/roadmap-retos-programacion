public class excepciones {

    public static void main(String[] args) {
        
        try {
            var result = 10/0;
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("Error al dividir: " + e.getMessage());
        }

        int[] myNumbers = {1,0,3};

        try {
            System.out.println(myNumbers[3]);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Error, índicie no existente: " + e.toString());
        }

        /*
         Dificultad extra
        */
       System.out.println("\n");
        System.out.println("--- Dificultad extra ---");
        int [] datosExtras ={10, 0, 5};

        try {
            processParams(datosExtras);
            System.out.println("No se ha producido ningún error.");
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Error, índice fuera de límites: " + e.toString());
        }catch(ArithmeticException e){
            System.out.println("Error al dividir por cero: " + e.toString());
        }catch(CustomException e){
            System.out.println("Error numero negativo: " + e.toString());
        }finally{
            System.out.println("La ejecucuión ha finalizado");
        }

        

    }

        /*
         Dificultad extra
        */

        public static void processParams(int[] numbers) throws CustomException{
            if(numbers.length < 3){
                throw new IndexOutOfBoundsException("El índice es incorrecto");
            }
            if(numbers[1] == 0) {
                throw new ArithmeticException("No se puede dividir entre 0");
            }
            if(numbers[0] < 0){
                throw new CustomException("El primer número no puede ser negativo");
            }
            System.out.println("El tercer número es: " + numbers[2]);
            System.out.println("La división es: " + (numbers[0]/numbers[1]));
            
            
        }
}

    class CustomException extends Exception {
        public CustomException(String mensaje){
            super(mensaje);
        }
    
}

