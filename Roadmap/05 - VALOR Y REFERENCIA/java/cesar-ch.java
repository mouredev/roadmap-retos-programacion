import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Asignación de variables por valor
        int a = 10;
        int b = a;

        a = 5;

        System.out.println(a); // 5
        System.out.println(b); // 10

        // Asignación de variables por referencia
        Map<String, Integer> x = new HashMap<>();
        x.put("a", 10);
        x.put("b", 20);
        Map<String, Integer> y = x;

        x.put("a", 12);
        x.put("b", 24);
        
        System.out.println(x); // [12, 24]
        System.out.println(y); // [12, 24]

        // Función con parámetro por valor
        int numero = 5;
        cambiarValor(numero);

        System.out.println(numero); // 5

        // Función con parámetro por referencia
        Map<String, Integer> objeto = new HashMap<>();
        objeto.put("a", 5);
        cambiarReferencia(objeto);

        System.out.println(objeto); // {a=100}

        // Ejemplo que intercambia los valores de dos variables por valor
        int c = 10;
        int d = 5;

        int[] newValues = intercambiarValores(c, d);
        System.out.println("Valores iniciales: " + c + ", " + d); // 10, 5
        System.out.println("Valores por valor: " + newValues[0] + ", " + newValues[1]); // 5, 10

        // Ejemplo que intercambia los valores de dos variables por referencia
        Map<String, Integer> objA = new HashMap<>();
        objA.put("a", 10);
        Map<String, Integer> objB = new HashMap<>();
        objB.put("a", 5);

        Map<String, Integer>[] newObjects = intercambiarReferencias(objA, objB);
        System.out.println("Valores iniciales: " + objA + ", " + objB); // {a=10}, {a=5}
        System.out.println(
                "Valores por referencia: " + newObjects[0] + ", " + newObjects[1]); // {a=5}, {a=10}
    }

    static void cambiarValor(int numero) {
        numero = 100;
        System.out.println(numero); // 100
    }

    static void cambiarReferencia(Map<String, Integer> objeto) {
        objeto.put("a", 100);
        System.out.println(objeto); // {a=100}

    }

    static int[] intercambiarValores(int c, int d) {
        int temp = c;
        c = d;
        d = temp;

        return new int[] { c, d };
    }

    static Map<String, Integer>[] intercambiarReferencias(Map<String, Integer> obj1, Map<String, Integer> obj2) {
        Map<String, Integer> temp1 = new HashMap<>(obj1);
        Map<String, Integer> temp2 = new HashMap<>(obj2);
        Map<String, Integer> temp = new HashMap<>(obj1);
        temp1.clear();
        temp1.putAll(temp2);
        temp2.clear();
        temp2.putAll(temp);

        return new Map[] { temp1, temp2 };
    }
}