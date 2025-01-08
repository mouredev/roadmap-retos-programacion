/*
    * #13 PRUEBAS UNITARIAS 
*/
import java.util.Arrays;

public class Main13 {
    public static void main(String[] args) {
        int result1 = sum(2, 3);
        if (result1 == 5) {
            System.out.println("Test passed");
        } else {
            System.err.println("Error: The sum of 2 and 3 is not equal to 5");
        }

        Person person = new Person("cesar-ch", 3, "2021-02-03", new String[]{"Javascript", "Python", "Java"});

        String[] expectedKeys = {"name", "age", "birthDate", "programmingLanguages"};
        boolean allKeysExist = Arrays.stream(expectedKeys).allMatch(person::containsKey);
        if (allKeysExist) {
            System.out.println("Test passed");
        } else {
            System.err.println("Error: The person object does not have the expected keys");
        }

        if (!(person.getName() instanceof String)) {
            System.err.println("Error: The name field is not a string");
        }

        if (person.getAge() < 0) {
            System.err.println("Error: Age must be a positive number");
        }

        if (!person.getBirthDate().matches("\\d{4}-\\d{2}-\\d{2}")) {
            System.err.println("Error: Birth date is not in the expected format");
        }

        if (!(person.getProgrammingLanguages() instanceof String[])) {
            System.err.println("Error: Programming languages is not an array");
        }
    }

    public static int sum(int num1, int num2) {
        return num1 + num2;
    }
}

/*
    * DIFICULTAD EXTRA
*/

class Person {
    private String name;
    private int age;
    private String birthDate;
    private String[] programmingLanguages;

    public Person(String name, int age, String birthDate, String[] programmingLanguages) {
        this.name = name;
        this.age = age;
        this.birthDate = birthDate;
        this.programmingLanguages = programmingLanguages;
    }

    public boolean containsKey(String key) {
        switch (key) {
            case "name":
                return name != null;
            case "age":
                return true; // age is always present
            case "birthDate":
                return birthDate != null;
            case "programmingLanguages":
                return programmingLanguages != null;
            default:
                return false;
        }
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getBirthDate() {
        return birthDate;
    }

    public String[] getProgrammingLanguages() {
        return programmingLanguages;
    }
}
