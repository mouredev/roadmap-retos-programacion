public class AmadorQuispe {
    public static void main(String[] args) {
        /*
         * Todos los tipos primitivos se pasan por valor
         */
        int age;
        age = 35;
        System.out.println(age);
        changeAge(age); // pasamos a una función que asigna otro valor
        System.out.println(age); // observamos que no cambia por se pasa copia (valor)

        /*
         * Todos los arreglos y objetos se pasan por referencia
         */
        // Ejemplo con arreglo
        double[] prices = { 10.23, 34.00, 12.00 };
        System.out.println("Precios");
        for (double price : prices) {
            System.out.println(price);
        }
        changeArray(prices); // Se pasa a una función donde se cambia
        System.out.println("Precios despues de cambio");
        for (double price : prices) {
            System.out.println(price);
        }
        // Ejemplo con objeto
        Person person = new Person();
        person.setName("Amador");
        person.setAge(29);

        System.out.println(person);
        changePerson(person);

        /*
         * las clases Wrappers(String, Integer, Double...) son inmutables, quiere decir
         * que una vezasignado no su valor no se puede cambiar
         */
        Double d = 89.00;
        System.out.println(d);
        changeAge(d);
        System.out.println("post" + d);
    }

    static void changeAge(int age) {
        age = 40;
    }

    static void changeArray(double[] prices) {
        for (int i = 0; i < prices.length; i++) {
            prices[i] = prices[i] + 10;
        }
    }

    static void changePerson(Person person) {
        System.out.println(person);
    }

    static void changeAge(Double d) {
        d = 23.00;
    }
}

class Person {
    private String name;
    private int age;

    public Person() {
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

}
