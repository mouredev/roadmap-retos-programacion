import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class martinbohorquez {
    public static void main(String[] args) {
        try {
//            int num = 10 / 0;
            List<Integer> lista = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
            System.out.println(lista.get(6));
        } catch (ArithmeticException e) {
//            e.printStackTrace();
            System.out.printf("No puede dividirse por cero: %s%n", e.getMessage());
        } catch (IndexOutOfBoundsException e) {
            System.out.printf("Indice fuera de límites: %s%n", e.getMessage());
        }
        System.out.println("Continuando con el programa...!");

        /*
         * DIFICULTAD EXTRA
         */
        processParams(Arrays.asList(10, 0, 30));
    }

    private static void processParams(List<Integer> lista) {
        List<Integer> list = new ArrayList<>(lista);
        try {
            System.out.printf("La división es: %d%n", (list.get(2) / list.get(0)));
            System.out.println(list.get(2));
            if (list.get(1) == 0) throw new MartinException("elemento con valor zero!");
        } catch (ArithmeticException e) {
            System.out.printf("No puede dividirse por cero: %s%n", e.getMessage());
        } catch (IndexOutOfBoundsException e) {
            System.out.printf("Indice fuera de límites: %s%n", e.getMessage());
        } catch (MartinException e) {
            System.out.printf("Se ha producido un error personalizado: %s%n", e.getMessage());
        } catch (Exception e) {
            System.out.printf("Se ha producido un error inesperado: %s%n", e.getMessage());
        } finally {
            System.out.println("Programa finalizado!");
        }
    }

    private static class MartinException extends Exception {
        public MartinException(String message) {
            super(message);
        }
    }
}
