public class Maynor06 {
    // esta funcion recibe la copia de la variable y no recibe la variable en si.
    public void modificacionPorValor(int valor) {
        valor = 10;
    }

    // esta funcion recibe el dato en si, osea que si modifica el valor del array
    // no recibe una copia recibe la variable en si.
    public void modificacionPorRefencia(int[] valorPorReferencia){
        for(int i = 0; i < valorPorReferencia.length; i++){
            valorPorReferencia[i] = i+10;
        }
    }

    public void ejemploAsignacionValorReferencia(){

        Maynor06 m = new Maynor06();
        //ejemplo de la asignacion de una variable que pasa por valor
        int porValor = 20;

        //ejemplo de la asignacion de una variable que se pasa por referencia.
        int[] porReferencia = new int[5];
        porReferencia[0] = 1;
        porReferencia[1] = 5;
        porReferencia[2] = 8;
        porReferencia[3] = 9;
        porReferencia[4] = 100;

        //modificamos el valor de la variable
        m.modificacionPorValor(porValor);

        // modificamos el valor del Array
        m.modificacionPorRefencia(porReferencia);

        System.out.println( "Valor de la variable por valor: " + porValor);
        for(int i = 0; i < porReferencia.length; i++){
            System.out.println( "Valor de la variable por refernecia: " + porReferencia[i]);
        }

    }

    public int[] inverParamByValue(int value, int value2){
        int[] response = {value2, value};

        return response ;
    }

    public Person[] changePerson(Person person1, Person person2){
        Person[] response = {person2, person1};
        return response;
    }

    public static void main(String[] args) {

        Maynor06 m = new Maynor06();
        int number1 = 5;
        int number2 = 10;
        Person person1 = new Person("Damaris", 19);
        Person person2 = new Person("Isabel", 16);

        int[] aux = m.inverParamByValue(number1, number2);
        int changeNumber1 = aux[0];
        int changeNumber2 = aux[1];

        Person[] persons = m.changePerson(person1, person2);
        Person changePerson1 = persons[0];
        Person changePerson2 = persons[1];

        System.out.println("Numeros originales: " + number1 + number2);
        System.out.println(" ");
        System.out.println("Intercambio de numeros: " + changeNumber1 + changeNumber2);
        System.out.println(" ");
        System.out.println("Personas originales: ");
        System.out.println( person1.toString());
        System.out.println(person2.toString());
        System.out.println(" ");
        System.out.println("Personas intercambiadas: ");
        System.out.println( changePerson1.toString());
        System.out.println(changePerson2.toString());

    }


    public static class Person{

        private String nombre;
        private int edad;
        public Person(String nombre, int edad){
            this.nombre = nombre;
            this.edad = edad;
        }
        public String getNombre() {
            return nombre;
        }
        public void setNombre(String nombre) {
            this.nombre = nombre;
        }
        public int getEdad() {
            return edad;
        }
        public void setEdad(int edad) {
            this.edad = edad;
        }

        public String toString(){
            return "Nombre: " + this.nombre + ", Edad: " + this.edad;
        }
    }
}
