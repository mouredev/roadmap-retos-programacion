import java.util.*;

public class AnaLauDB {

    // Función para sumar
    public static int sumar(int a, int b) {
        return a + b;
    }

    // Diccionario con tus datos
    public static Map<String, Object> crearDiccionario() {
        Map<String, Object> datos = new HashMap<>();
        datos.put("name", "Ana Laura");
        datos.put("age", 28);
        datos.put("birth_date", "1997-05-20");
        datos.put("programming_languages", Arrays.asList("Java", "Python", "JavaScript"));
        return datos;
    }

    // Función que simula los tests
    public static void ejecutarTests() {
        System.out.println("=== Test función sumar ===");
        System.out.println("2 + 3 = " + (sumar(2, 3) == 5 ? "PASÓ" : "FALLÓ"));
        System.out.println("-2 + 2 = " + (sumar(-2, 2) == 0 ? "PASÓ" : "FALLÓ"));
        System.out.println("-3 + -4 = " + (sumar(-3, -4) == -7 ? "PASÓ" : "FALLÓ"));

        System.out.println("\n=== Test diccionario ===");
        Map<String, Object> datos = crearDiccionario();
        boolean camposOk = datos.containsKey("name") && datos.containsKey("age") &&
                datos.containsKey("birth_date") && datos.containsKey("programming_languages");
        System.out.println("Campos existentes: " + (camposOk ? "PASÓ" : "FALLÓ"));

        boolean valoresOk = datos.get("name").equals("Ana Laura") &&
                (int) datos.get("age") == 28 &&
                datos.get("birth_date").equals("1997-05-20");
        System.out.println("Valores correctos: " + (valoresOk ? "PASÓ" : "FALLÓ"));
    }

    public static void main(String[] args) {
        ejecutarTests();
    }
}
