import java.util.ArrayList;
import java.util.List;

public class simonguzman{
    public static void main(String[] args) {
        try {
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
    }
}