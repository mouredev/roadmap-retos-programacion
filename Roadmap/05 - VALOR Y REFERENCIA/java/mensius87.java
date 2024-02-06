import java.util.*;

public class mensius87 {

    // Asignación de variables por valor
    static int numero1 = 23;
    static double numero2 = 3.14;
    static String color = "rojo";
    static Object[] agenda = {1, "hola", numero2};

    // Asignación de variables por referencia
    static List<String> colores = Arrays.asList("rojo", "verde", "azul");
    static Map<String, String> inglesEspanol = new HashMap<>();
    static {
        inglesEspanol.put("hello", "hola");
        inglesEspanol.put("red", "rojo");
        inglesEspanol.put("green", "verde");
        inglesEspanol.put("blue", "azul");
    }
    static Set<Integer> miSet = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));

    // Ejemplos de funciones con variables de paso por valor
    static void suma(double num1, double num2) {
        double resultado = num1 + num2;
        System.out.println("El valor de 'numero1' es " + num1 + "+" + num2 + " es " + resultado);
    }

    static void datosAgenda(Object[] datos) {
        System.out.println(Arrays.toString(datos));
    }

    // Ejemplos de funciones con variables de paso por referencia
    static void imprimirVocabulario(Map<String, String> vocabulario) {
        for (Map.Entry<String, String> entry : vocabulario.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    // Programa principal
    public static void main(String[] args) {
        // Ejemplos de funciones con variables de paso por valor
        suma(numero1, numero2);
        System.out.println();

        // Ejemplos de funciones con variables de paso por referencia
        datosAgenda(agenda);
        System.out.println();

        imprimirVocabulario(inglesEspanol);
    }
}
