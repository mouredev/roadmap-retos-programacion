import java.util.ArrayList;

public class SDM29GH {
    public static void main(String[] args) {
        
        System.out.println("***** Valor y Referencia *****");

        // Asignación de variables por valor
        System.out.println("Asignación de variables por Valor");
        int a = 5;
        int b = a;
        a = 10;
        System.out.println(b);
        
        // Asignación de variables por referencia
        System.out.println("Asignación de variables por Referencia");
        ArrayList<Integer> lista1 = new ArrayList<>();
        lista1.add(100);
        ArrayList<Integer> lista2 = lista1;
        lista1.add(200);
        System.out.println(lista2);
    }
}