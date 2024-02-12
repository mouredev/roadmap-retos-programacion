public class miguelex {

    static class Persona {
        private String nombre;
        private int edad;

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
    }

    public static int[] intercambioporValor(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
        return new int[]{a, b};
    }

    public static void intercambioporReferencia(Persona a, Persona b) {
        Persona temp = a;
        a = b;
        b = temp;
    }

    public static void main(String[] args) {
        
        int a = 10;
        int b = a;

        System.out.println("Variables por valor");
        System.out.println("a original = " + a);
        System.out.println("b copia = " + b);
        //Cambiamos el valor de una variable y verificamos que no afect
        a = 20;
        System.out.println("variable a modificada = " + a);
        System.out.println("variable b = " + b);

        System.out.println("\n\nVariables por referencia");
        Persona personaOriginal = new Persona();
        personaOriginal.setNombre("Miguel");
        personaOriginal.setEdad(48);

        Persona personaCopia = personaOriginal;

        System.out.println("persona original = " + personaOriginal.getNombre() + " " + personaOriginal.getEdad());
        System.out.println("persona copia = " + personaCopia.getNombre() + " " + personaCopia.getEdad());

        personaOriginal.setNombre("Miguel Angel");
        personaOriginal.setEdad(49);

        System.out.println("persona original modificada = " + personaOriginal.getNombre() + " " + personaOriginal.getEdad());
        System.out.println("persona copia = " + personaCopia.getNombre() + " " + personaCopia.getEdad());

        System.out.println("\n\nExtra");

        a = 5;
        b = 10;

        System.out.println("a = " + a);
        System.out.println("b = " + b);

        int[] valores = intercambioporValor(a, b);
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("a intercambiada = " + valores[0]);
        System.out.println("b intercambiada = " + valores[1]);

        Persona personaA = new Persona();
        personaA.setNombre("Juan");
        personaA.setEdad(30);

        Persona personaB = new Persona();
        personaB.setNombre("Pedro");
        personaB.setEdad(40);
    
        System.out.println("personaA = " + personaA.getNombre() + " " + personaA.getEdad());
        System.out.println("personaB = " + personaB.getNombre() + " " + personaB.getEdad());

        intercambioporReferencia(personaA, personaB);

        System.out.println("personaA = " + personaA.getNombre() + " " + personaA.getEdad());
        System.out.println("personaB = " + personaB.getNombre() + " " + personaB.getEdad());
    }
}
