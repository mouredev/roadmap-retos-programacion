import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

/**
 * #13 PRUEBAS UNITARIAS
 * <dependencies>
 * <dependency>
 * <groupId>org.junit.jupiter</groupId>
 * <artifactId>junit-jupiter</artifactId>
 * <version>5.10.3</version>
 * </dependency>
 * </dependencies>
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    public static void main(String[] args) throws Exception {
        System.out.println(sum(23, 19));
    }

    private static Object sum(Object a, Object b) throws Exception {
        if (!(a instanceof Integer) || !(b instanceof Integer))
            throw new Exception("Los argumentos deben ser enteros positivos!");
        return ((Integer) a) + ((Integer) b);
    }

    /*
     * DIFICULTAD EXTRA
     */
    private static Map<String, String> programmer() {
        Map<String, String> programmer = new HashMap<>();
        programmer.put("name", "Martin");
        Integer age = 29;
        programmer.put("age", String.valueOf(age));
        LocalDate birthDate = LocalDate.of(1994, 9, 26);
        programmer.put("birthDate", String.valueOf(birthDate));
        ArrayList<String> programmingLanguage = new ArrayList<>(Arrays.asList("Java", "Typescript", "Python"));
        programmer.put("programmingLanguage", String.valueOf(programmingLanguage));
        return programmer;
    }

    @Nested
    class TestMain {

        Map<String, String> data;
        Map<String, String> programmer = programmer();

        @BeforeEach
        void setUp() {
            data = new HashMap<>();
            data.put("name", "Martin");
            Integer age = 29;
            data.put("age", String.valueOf(age));
            LocalDate birthDate = LocalDate.of(1994, 9, 26);
            data.put("birthDate", String.valueOf(birthDate));
            ArrayList<String> programmingLanguage = new ArrayList<>(Arrays.asList("Java", "Typescript", "Python"));
            data.put("programmingLanguage", String.valueOf(programmingLanguage));
        }

        @Test
        void testSum() throws Exception {
            assertEquals(37, sum(14, 23));
            assertEquals(10, sum(15, -5));
            assertEquals(25, sum(-10, 35));
            assertEquals(-15, sum(-20, 5));
            assertEquals(-5, sum(20, -25));
            assertEquals(-20, sum(-15, -5));
        }

        @Test
        void testSumTypes() throws Exception {
            String esperado = "Los argumentos deben ser enteros positivos!";
            Exception exceptionDouble = assertThrows(Exception.class, () -> sum(5, 2.5));
            String actual = exceptionDouble.getMessage();
            assertEquals(esperado, actual);
            Exception exceptionString = assertThrows(Exception.class, () -> sum("5", 2));
            actual = exceptionString.getMessage();
            assertEquals(esperado, actual);
        }

        @Test
        void testMapSize() {
            assertEquals(programmer.size(), data.size());
        }

        @Test
        void testKeysExist() {
            programmer.keySet().forEach(key -> assertTrue(data.containsKey(key)));
        }

        @Test
        void testValuesCorrect() {
            programmer.keySet().forEach(key -> assertEquals(programmer.get(key), data.get(key)));
        }

        @Test
        void testValuesInstance() {
            programmer.keySet().forEach(key -> assertInstanceOf(programmer.get(key).getClass(), data.get(key)));
        }

    }
}
