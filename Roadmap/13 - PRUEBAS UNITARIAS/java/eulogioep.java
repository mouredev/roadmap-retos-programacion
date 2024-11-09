import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Clase principal que contiene la función de suma y el diccionario de datos personales.
 */
public class eulogioep {

    /**
     * Función que suma dos números y retorna el resultado.
     * @param a Primer número a sumar.
     * @param b Segundo número a sumar.
     * @return La suma de a y b.
     */
    public static int suma(int a, int b) {
        return a + b;
    }

    /**
     * Crea y retorna un diccionario (Map en Java) con datos personales.
     * @return Map con datos personales.
     */
    public static Map<String, Object> crearDiccionario() {
        Map<String, Object> diccionario = new HashMap<>();
        diccionario.put("name", "Tu nombre");
        diccionario.put("age", 30);
        diccionario.put("birth_date", "1993-01-01");
        diccionario.put("programming_languages", Arrays.asList("Java", "Python", "JavaScript"));
        return diccionario;
    }

    /**
     * Clase interna para las pruebas unitarias.
     */
    public static class Tests {

        @Test
        public void testSuma() {
            assertEquals(5, suma(2, 3), "La suma de 2 y 3 debería ser 5");
            assertEquals(0, suma(-1, 1), "La suma de -1 y 1 debería ser 0");
            assertEquals(-5, suma(-2, -3), "La suma de -2 y -3 debería ser -5");
        }

        @Test
        public void testExistenciaCamposDiccionario() {
            Map<String, Object> diccionario = crearDiccionario();
            assertTrue(diccionario.containsKey("name"), "El diccionario debe contener la clave 'name'");
            assertTrue(diccionario.containsKey("age"), "El diccionario debe contener la clave 'age'");
            assertTrue(diccionario.containsKey("birth_date"), "El diccionario debe contener la clave 'birth_date'");
            assertTrue(diccionario.containsKey("programming_languages"), "El diccionario debe contener la clave 'programming_languages'");
        }

        @Test
        public void testDatosCorrectosDiccionario() {
            Map<String, Object> diccionario = crearDiccionario();
            assertEquals("Tu nombre", diccionario.get("name"), "El nombre debe ser 'Tu nombre'");
            assertTrue(diccionario.get("age") instanceof Integer, "La edad debe ser un entero");
            assertTrue(((String) diccionario.get("birth_date")).matches("\\d{4}-\\d{2}-\\d{2}"), "La fecha de nacimiento debe tener el formato YYYY-MM-DD");
            assertTrue(diccionario.get("programming_languages") instanceof java.util.List, "Los lenguajes de programación deben ser una lista");
            assertTrue(((java.util.List<?>) diccionario.get("programming_languages")).size() > 0, "La lista de lenguajes de programación no debe estar vacía");
        }
    }
}