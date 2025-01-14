import java.util.HashMap;
import java.util.Map;

public class EjemploPruebasUnitarias {

    /**
     * Función que suma dos números enteros y devuelve el resultado.
     */
    public static int sumar(int a, int b) {
		return a + b;
    }

    /**
     * Test para la función sumar
     */

//    @Test
//    void testSumar() {
//        assertEquals(5, EjemploPruebasUnitarias.sumar(2, 3), "2 + 3 = 5");
//        assertEquals(0, EjemploPruebasUnitarias.sumar(-2, 2), "-2 + 2 = 0");
//        assertEquals(0, EjemploPruebasUnitarias.sumar(0, 0), "0 + 0 = 0");
//    }

    /**
     * Función que devuelve un Map con datos de ejemplo.
     */
    public static Map<String, String> obtenerDatos() {
        Map<String, String> datos = new HashMap<>();
        datos.put("name", "Jordi");
        datos.put("age", "20");
        datos.put("birth_date", "2000-01-01");
        datos.put("programming_languages", "Java, Python, JavaScript");
        return datos;
    }

    /**
     * Test para la función obtenerDatos
     */

//    @Nested
//    @DisplayName("Test para la función obtenerDatos")
//    class ObtenerDatosTest {
//
//        Map<String, String> datos = EjemploPruebasUnitarias.obtenerDatos();
//
//        @Test
//        void testContieneTodosLosCampos() {
//            assertEquals(4, datos.size());
//            assertTrue(datos.containsKey("name"));
//            assertTrue(datos.containsKey("age"));
//            assertTrue(datos.containsKey("birth_date"));
//            assertTrue(datos.containsKey("programming_languages"));
//        }
//
//        @Test
//        void testCampoName() {
//            assertEquals("Jordi", datos.get("name"));
//        }
//
//        @Test
//        void testCampoAge() {
//            assertEquals("20", datos.get("age"));
//        }
//
//        @Test
//        void testCampoBirthDate() {
//            assertEquals("2000-01-01", datos.get("birth_date"));
//        }
//
//        @Test
//        void testCampoProgrammingLanguages() {
//            assertEquals("Java, Python, JavaScript", datos.get("programming_languages"));
//        }
//
//    }

    /**
     * Maven dependency for JUnit 5:
     * <dependency>
     *     <groupId>org.junit.jupiter</groupId>
     *     <artifactId>junit-jupiter</artifactId>
     *     <version>5.10.2</version>
     *     <scope>test</scope>
     * </dependency>
     */

}
