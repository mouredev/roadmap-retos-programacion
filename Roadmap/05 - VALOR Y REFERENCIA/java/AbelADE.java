public class Main {

    public static void value(int number) {
        System.out.println("El valor del número recibido es: " + number);
        number += 5;
        System.out.println("Sumado a 5 es igual a " + (number));
    }

    public static void value(User user) {
        System.out.println("El usuario recibido es: " + user);
        user.setName("Marcos");
        System.out.println("El nuevo nombre del usuario es: " + user);
    }

    public static void main(String[] args) {

        /*
         * Paso de variables por valor: pasan 'una copia' de su valor a un parámetro, sin ser ella misma modificada.
         */
        int variable = 15;
        value(variable);
        System.out.println("El valor de la variable enviada cómo parámetro es: " + variable + "\n");

        /*
         * Paso de variables por referencia: en Java no existe el paso por referencia, aunque algo muy similar ocurre
         * con los objetos, ya que se guardan cómo una dirección de memoria y al pasarla cómo parámetro, se envía la
         * dirección de memoria y se trabaja sobre esos datos (lo que significa que cambiamos el objeto al cambiar los
         * datos asociados con una dirección de memoria concreta).
         */

        User user = new User("Abel",29);
        value(user);
        System.out.println("El valor del objeto enviado cómo parámetro es: " + user + "\n");

    }
}

class User {
    //Atributos
    String name;
    int age;

    //Métodos de acceso
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

    //Constructor
    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    //Método que se invoca de forma automática al querer mostrar el objeto por consola.
    @Override
    public String toString() {
        return name;
    }
}
