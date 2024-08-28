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
    }

    static class customException extends Exception {
        public customException(){

        }

        public customException(String message){
            super(message);
        }
    }
}