import java.util.HashMap;

public class PruebasJUNIT {
    HashMap<String, String> map = new HashMap<>();

    public int sumar(int num1, int num2) {
        return num1 + num2;
    }

    public void setMap() {
        map.put("name", "Michael");
        map.put("age", "31");
        map.put("birth_date", "06/02/1993");
        map.put("programming_languages", "JAVA");
    }
}

// TESTS

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class TestJUNIT {
    private PruebasJUNIT pruebasJUNIT;

    @Before
    public void setUp() {
        pruebasJUNIT = new PruebasJUNIT();
        pruebasJUNIT.setMap();
    }

    @Test
    public void testSum() {
        assertEquals(5, pruebasJUNIT.sumar(2, 3));
    }

    @Test
    public void testMapKeys() {
        assertTrue(pruebasJUNIT.map.containsKey("name"));
        assertTrue(pruebasJUNIT.map.containsKey("age"));
        assertTrue(pruebasJUNIT.map.containsKey("birth_date"));
        assertTrue(pruebasJUNIT.map.containsKey("programming_languages"));
    }

    @Test
    public void testMapValues() {
        assertTrue(pruebasJUNIT.map.containsValue("Michael"));
        assertTrue(pruebasJUNIT.map.containsValue("31"));
        assertTrue(pruebasJUNIT.map.containsValue("06/02/1993"));
        assertTrue(pruebasJUNIT.map.containsValue("JAVA"));
    }
}