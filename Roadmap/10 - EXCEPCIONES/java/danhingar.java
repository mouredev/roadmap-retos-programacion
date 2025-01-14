import java.util.List;

public class danhingar {

    public static void main(String[] args) {
        System.out.println(divide(10, 0));
        List<String> list = List.of("A","B","C");
        System.out.println(search(list,4));

        try {
            processParams(List.of(1,4,"a"));
            System.out.println("No se ha producido ningún error.");
        } catch (IndexOutOfBoundsException e) {
            System.out.println("El número de elementos de la lista debe ser mayor que dos.");
        } catch (ArithmeticException e){
            System.out.println("El segundo elemento de la lista no puede ser un cero.");
        }catch(StrTypeError e){
            System.out.println(e);
        }catch(Exception e){
            System.out.println("Se ha producido un error inesperado: "+e);
        }finally{
            System.out.println("El programa finaliza sin detenerse.");
        }
    }

    private static Integer divide(int number1, int number2){
        try {
            return number1/number2;
        } catch (Exception e) {
            System.out.println("No se ha podido realizar la división");
            return null;
        }
    }

    private static String search(List<String> list,Integer index) {
        try {
            return list.get(index);
        } catch (Exception e) {
            System.out.println("No se ha podido recuperar el elemento del ídice :"+index);
            return null;
        }
    }

    //EXTRA
    private static void processParams(List<Object> numbers) throws danhingar.StrTypeError{
        if(numbers.size()<3){
            throw new IndexOutOfBoundsException();
        }else if(numbers.get(1).equals(0)){
            throw new ArithmeticException();
        }else if(numbers.get(2).getClass().equals(String.class)){
            throw new StrTypeError("El tercer elemento no puede ser una cadena de texto.");
        }
    }

    private static class StrTypeError extends Exception {
        
        public StrTypeError(String message){
            super(message);
        }
        
    }

}
