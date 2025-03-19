public class ExampleUnitTesting {
    public static int addition(int... numbers) throws Exception {
        if (numbers.length == 0)
            throw new Exception();
        int result = Arrays.stream(numbers).reduce((cum, num) -> cum + num).getAsInt();

        return result;
    }

    public static Map<String, String> myData() {
        Map<String, String> data = new HashMap<>();
        data.put("name", "Amador");
        data.put("age", "31");
        data.put("birth_date", "1992-07-13");
        data.put("programming_languages", "Java, Go, JavaScript");
        data.put("web", "amsoft.dev");
        return data;
    }

}

//Dependecia para test
/*
<dependency>
	<groupId>org.junit.jupiter</groupId>
	<artifactId>junit-jupiter-engine</artifactId>
	<version>5.10.2</version>
	<scope>test</scope>
</dependency>
*/

// Clase test

public class ExampleUnitTest {
    @Test
    void additionWithNumbers() {
        try {
            assertEquals(6, ExampleUnitTesting.addition(1, 2, 3));
            assertEquals(20, ExampleUnitTesting.addition(20));
            assertEquals(7, ExampleUnitTesting.addition(-1, 5, 3));
            assertEquals(-3, ExampleUnitTesting.addition(-1, -5, 3));
        } catch (Exception e) {
            fail("No se debe lanzar una excepción para una entrada válida");
        }
    }

    @Test
    void additionWithNoNumbers() {
        assertThrows(Exception.class, () -> {
            ExampleUnitTesting.addition();
        });
    }

    Map<String, String> data = ExampleUnitTesting.myData();

    @Test
    void testKeysExist() {
        assertEquals(5, data.size());
        assertTrue(data.containsKey("name"));
        assertTrue(data.containsKey("age"));
        assertTrue(data.containsKey("birth_date"));
        assertTrue(data.containsKey("programming_languages"));
        assertTrue(data.containsKey("web"));
    }

    @Test
    void testMyDataCorrect() {
        assertTrue(data.get("name").equals("Amador"));
        assertTrue(data.get("age").equals("31"));
        assertTrue(data.get("birth_date").equals("1992-07-13"));
        assertTrue(data.get("programming_languages").equals("Java, Go, JavaScript"));
        assertTrue(data.get("web").equals("amsoft.dev"));
    }

}
