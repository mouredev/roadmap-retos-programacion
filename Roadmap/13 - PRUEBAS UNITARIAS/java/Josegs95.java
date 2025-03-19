import org.junit.BeforeClass;
import org.junit.Test;

import java.util.*;

import static org.junit.Assert.*;

public class Josegs95 {
    public static void main(String[] args) {}

    //Ejercicio

    public static int sum(int n1, int n2){
        return n1 + n2;
    }

    @Test
    public void testSumMethod(){
        assertEquals("Comprobación suma estandar", 10, sum(3, 7));
        assertEquals("Comprobación suma con números negativos", 2, sum(8, -6));
        assertEquals("Comprobación suma con ceros", 5, sum(5, 0));
    }

    //Reto

    static Map<String, Object> data;

    @BeforeClass
    public static void initData(){
        data = new HashMap<>();

        data.put("name", "Jose");
        data.put("age", 29);
        data.put("birth_date", "28-02-1995");
        data.put("programming_languages", Arrays.asList("Java", "Python"));
    }

    @Test
    public void testDataExistence(){
        assertNotNull("¿Campo name es nulo?", data.get("name"));
        assertNotNull("¿Campo age es nulo?", data.get("age"));
        assertNotNull("¿Campo birth_date es nulo?", data.get("birth_date"));
        assertNotNull("¿Campo programming_languages es nulo?", data.get("programming_languages"));
    }

    @Test
    public void testDataCorrectValues(){
        assertEquals("Valor de name", String.class, data.get("name").getClass());
        assertEquals("Valor de age", Integer.class, data.get("age").getClass());
        assertTrue("Valor de birth_date", data.get("birth_date") instanceof String);
        assertTrue("Valor de programming_languages", data.get("programming_languages") instanceof List);
    }
}
