public class LogicaJava05 {
    
    public static void main(String[] args) {
        // 1.
        // Por valor
        int a = 10;
        int b = a;

        b = 20;

        System.out.println(a); // 10
        System.out.println(b); // 20
        
        // Por "referencia"
        Persona p1 = new Persona();
        p1.nombre = "Alberto";

        Persona p2 = p1; // se copia la REFERENCIA, no el objeto

        p2.nombre = "Pedro";

        System.out.println(p1.nombre); // Pedro
        System.out.println(p2.nombre); // Pedro

        // 2.
        // Por valor
        int n = 5;
        cambiarNumero(n);
        System.out.println(n); // 5 porque se pasó una copia, se modifica la copia
        
        // Por "referencia"
        Persona persona = new Persona();
        persona.nombre = "Ana";

        cambiarNombre(persona);

        System.out.println(persona.nombre); // Carlos
    }
    // 2.
    // Por valor
    public static void cambiarNumero(int x) {
        x = 100;
    }
    
    // Por "referencia"
    public static void cambiarNombre(Persona p) {
    p.nombre = "Carlos";
    }
}
class Persona {
    String nombre;
}
