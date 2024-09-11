

/** #07 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        Persona persona = new Persona("Jesus Antonio", 24, "Programador");
        persona.imprimirDetalles();
    //---EXTRA---
        
    }

    //---EJERCIÓ---
    // Definición de la clase Persona
    static class Persona {
        // Atributos de la clase
        private String nombre;
        private int edad;
        private String ocupacion;

        // Constructor de la clase Persona
        public Persona(String nombre, int edad, String ocupacion) {
            this.nombre = nombre;       // Inicializa el atributo nombre
            this.edad = edad;           // Inicializa el atributo edad
            this.ocupacion = ocupacion; // Inicializa el atributo ocupacion
        }

        // Método para imprimir los atributos de la clase
        public void imprimirDetalles() {
            System.out.println("Nombre: " + nombre);
            System.out.println("Edad: " + edad);
            System.out.println("Profesión: " + ocupacion);
        }
    }



    /**-----DIFICULTAD EXTRA-----*/

    // Pendiente

    /**-----DIFICULTAD EXTRA-----*/
}