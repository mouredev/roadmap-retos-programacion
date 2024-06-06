import java.util.ArrayList;
import java.util.List;

public class estuardodev {
    public static void main(String[] args) {
        int valor1 = 3;
        int valor2 = valor1;

        valor2 += 2;

        System.out.println("Valor 1: " + valor1);
        System.out.println("Valor 2: " + valor2);

        List<String> strings = new ArrayList<>();
        strings.add("Python");
        strings.add("C#");
        strings.add("Java");

        List<String> strings2 = new ArrayList<>(strings);
        strings2.add("C++");

        for (String i : strings) {
            System.out.println("Valores de Strings 1: " + i);
        }

        for (String i : strings2) {
            System.out.println("Valores de Strings 2: " + i);
        }

        valor(5, 10);

        List<String> lista1 = new ArrayList<>();
        lista1.add("C#");
        List<String> lista2 = new ArrayList<>();
        lista2.add("Python");
        referencia(lista1, lista2);

    }

    private static void valor(int val1, int val2) {
        int valor = val1;
        val1 = val2;
        val2 = valor;

        System.out.println("Valor del parámetro 1: " + val1);
        System.out.println("Valor del parámetro 2: " + val2);
    }

    private static void referencia(List<String> lista1, List<String> lista2) {
        List<String> refuerzo = new ArrayList<>(lista1);
        lista1.clear();
        lista1.addAll(lista2);
        lista2.clear();
        lista2.addAll(refuerzo);
        lista1.add("Lista 1");
        lista2.add("Lista 2");

        for (String s : lista1) {
            System.out.println("Valor lista 1: " + s);
        }
        for (String s : lista2) {
            System.out.println("Valor lista 2: " + s);
        }
    }
}
