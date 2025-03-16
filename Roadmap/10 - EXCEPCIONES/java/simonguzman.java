import java.util.ArrayList;
import java.util.List;

public class simonguzman{
    public static void main(String[] args) {

        //Manejo de excepciones basicas
        try {
            //Excepcion forzada: Division por cero
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("ERROR: Division por cero..."+e.getMessage());
        }

        try {
            //Indice fuera de los limites
            List<String> list = new ArrayList<>();
            list.add("Simon");
            String item = list.get(1);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("ERROR: Indice fuera de los limites..."+e.getMessage());
        }

        //Manejo de excepciones personalizadas
        try {
            throw new customException("Mensaje personalizado para una excepcion personalizada");
        } catch (customException e) {
            System.out.println("Se ha producido una excepcion personalizada..."+e.getMessage());
        }

        executeProcessParameters();
    }

    static void executeProcessParameters(){
        try {
            processParameters(10, 2, "test");
        } catch (ArithmeticException e){
            System.out.println("ERROR: Excepcion aritmetica..."+e.getMessage());
        } catch(ArrayIndexOutOfBoundsException e){
            System.out.println("ERROR: Indice fuera de los limites..."+e.getMessage());
        } catch(customException e){
            System.out.println("ERROR: Excepcion general..."+e.getMessage());
        }finally{
            System.out.println("La ejecucion a finalizado.");
        }
    }

    static void processParameters(int num1, int num2, String str) throws ArithmeticException, ArrayIndexOutOfBoundsException, customException{
        if (num2 == 0){
            throw new ArithmeticException("ERROR: Division por cero");
        }
        int result = num1/num2;
        System.out.println("Resultado: "+result);

        if(str.length() < 3){
            throw new ArrayIndexOutOfBoundsException("Cadena de texto muy corta");
        }

        if(str.equals("test")){
            throw new customException("Cadena no permitida");
        }

        System.out.println("Parametros procesados correctamente");
    }

    static class customException extends Exception {
        public customException(){

        }

        public customException(String message){
            super(message);
        }
    }
}