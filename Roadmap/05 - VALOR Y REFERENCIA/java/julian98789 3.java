
public class reto_5 {
    public static void main(String[] args) {
        // Ejemplo de asignación por valor (datos primitivos)
        int a = 5;
        int b = a; // 'b' obtiene una copia del valor de 'a'
        b = 10; // Cambiamos 'b', pero 'a' permanece igual

        System.out.println("Asignación por valor:");
        System.out.println("a: " + a); // Imprime 5
        System.out.println("b: " + b); // Imprime 10

        // Ejemplo de asignación por referencia (objetos)
        Persona persona1 = new Persona("Juan");
        Persona persona2 = persona1; // 'persona2' obtiene la referencia de 'persona1'
        persona2.nombre1 = "Pedro"; // Cambiamos el nombre usando 'persona2'

        System.out.println("\nAsignación por referencia:");
        System.out.println("persona1.nombre: " + persona1.nombre1); // Imprime "Pedro"
        System.out.println("persona2.nombre: " + persona2.nombre1); // Imprime "Pedro"

        // Ejemplo de paso de parámetros por valor (datos primitivos)
        int numero = 5;
        cambiarValor(numero);
        System.out.println("\nPaso por valor:");
        System.out.println("numero: " + numero); // Imprime 5, porque se pasa una copia

        // Ejemplo de paso de parámetros por referencia (objetos)
        Persona persona = new Persona("Juan");
        cambiarNombre(persona);
        System.out.println("\nPaso por referencia:");
        System.out.println("persona.nombre: " + persona.nombre1); // Imprime "Pedro"

        // **********reto****************
        System.out.println("\nReto:");
        int numeroOriginal1 = 5;
        int numeroOriginal2 = 10;
        Persona personaOriginal1 = new Persona("Juan");
        Persona personaOriginal2 = new Persona("andres");

        System.out.println("Nombre 1: " + personaOriginal1.nombre1 + " nombre 2 " + personaOriginal2.nombre1);

        System.out.println("Antes de cambiar:");
        System.out.println("numeroOriginal1: " + numeroOriginal1); 
        System.out.println("numeroOriginal2: " + numeroOriginal2); 
        System.out.println("personaOriginal1.nombre: " + personaOriginal1.nombre1);
        System.out.println("personaOriginal2.nombre: " + personaOriginal2.nombre1); 

        System.out.println("Después de cambiar:");

        cambiarValor(numeroOriginal1,numeroOriginal2);
        cambiarNombre(personaOriginal1,personaOriginal2);

        
    }

    public static void cambiarValor(int numeroOriginal1, int numeroOriginal2 ) {
        int aux = numeroOriginal1;
        numeroOriginal1 = numeroOriginal2;
        numeroOriginal2 = aux;

        System.out.println("valores cambiados numero 1: "+ numeroOriginal1 + " numero 2: " +numeroOriginal2 );

    }

    public static void cambiarNombre(Persona p1, Persona p2) {
        String aux = p1.nombre1;
        p1.nombre1 = p2.nombre1 ;
        p2.nombre2 = aux;

        System.out.println("valores cambiados p1.nombre1: "+ p1.nombre1 + " p2.nombre2: " +p2.nombre2 );
    }

    public static void cambiarValor(int n) {
        n = 10;
    }

    public static void cambiarNombre(Persona p1) {
        p1.nombre1 = "Pedro";
    }

    static class Persona {
        String nombre1;
        String nombre2;

        Persona(String nombre) {
            this.nombre1 = nombre;
        }

       

    }
}

