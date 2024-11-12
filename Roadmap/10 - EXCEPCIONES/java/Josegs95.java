import java.util.ArrayList;
import java.util.List;

public class Josegs95 {
    public static void main(String[] args) {
        //Excepciones
        try{
            int a = 10 / 0; //Comentar esta línea para comprobar el caso de abajo

            List<Object> list = new ArrayList<>();
            list.get(8);
        } catch (Exception e){
            System.out.println("Se ha producido un error: " + e.getMessage());
        }

        //Reto
        System.out.println("\n");
        retoFinal();
    }

    public static void retoFinal(){
        Object[] params = {"git", "commit", "-m", "'#10 - Java'"};
        //Object[] params = {"git", "commit", "-m", 85};
        //Object[] params = {"ls", "commit", "-m", "'#10 - Java'"};
        boolean error = false;

        try{

            processParams(params);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("El número de parametros debe ser de 4 o mas.");
            error = true;
        } catch (ClassCastException e) {
            System.out.println("El elemento número 4 deber ser una cadena de texto");
            error = true;
        } catch (NotRightCommandException e) {
            System.out.println("El elemento número 1 deber ser el comando 'git'");
            error = true;
        } catch (Exception e) {
            System.out.println("Se ha producido un error inesperado: " + e.getMessage());
            error = true;
        } finally {
            if (!error)
                System.out.println("El programa no ha tenido ningún error");
            System.out.println("El programa finaliza.");
        }

    }

    private static void processParams(Object[] params) throws Exception{
        if (params.length < 4)
            throw new IndexOutOfBoundsException();

        if (!(params[3] instanceof String)){
            throw new ClassCastException();
        }

        if (!params[0].toString().toLowerCase().equals("git"))
            throw new NotRightCommandException();

        String message = (String) params[3];
        System.out.println("El mensaje del commit es: " + message);
    }

    public static class NotRightCommandException extends Exception{

    }
}
