package Retos_2024.roadmap-retos-programacion.Roadmap.08 - CLASES.java;


public class Persona {
    private String nombre;
    private int edad;
    
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    
    public void imprimirInformacion() {
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Edad: " + this.edad);
    }

}

public class mensius87 {
    public static void main(String[] args) {
        // Crear una instancia de la clase Persona
        Persona persona1 = new Persona("Juan", 30);

        // Imprimir la información utilizando el método de la clase
        persona1.imprimirInformacion();

        // Modificar los atributos y volver a imprimir la información
        persona1.nombre = "María";
        persona1.edad = 25;
        persona1.imprimirInformacion();
    }
}