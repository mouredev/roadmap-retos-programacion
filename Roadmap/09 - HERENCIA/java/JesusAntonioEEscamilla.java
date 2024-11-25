import java.util.UUID;
import java.util.ArrayList;
import java.util.List;

/** #09 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        Animal perro = new Perro();
        Animal gato = new Gato();
        Animal pajaro = new Pajaro();

        System.out.println("Herencia");
        imprimirSonido(perro);
        imprimirSonido(gato);
        imprimirSonido(pajaro);

        System.out.println("\n");

        System.out.println("Extra Métodos");
        // Extra: Mostrar acciones adicionales
        ((Perro) perro).correr();
        ((Gato) gato).cazar();
        ((Pajaro) pajaro).volar();
    //---EXTRA---
        System.out.println("\n");
        // Crear Gerente
        Manager gerente = new Manager("Jesus");

        // Crear Gerente de Proyecto
        ProjectManager gerenteProyecto1 = new ProjectManager("Antonio", "Proyecto1");
        ProjectManager gerenteProyecto2 = new ProjectManager("Faty", "Proyecto2");

        // Crear Programadores
        Programmer programmer1 = new Programmer("Adolfo", "Python");
        Programmer programmer2 = new Programmer("Naty", "C#");
        Programmer programmer3 = new Programmer("Ruben", "Kotlin");
        Programmer programmer4 = new Programmer("Axel", "JavaScript");

        // Agregar empleados a cargo del gerente
        gerente.agregarEmpleado(gerenteProyecto1);
        gerente.agregarEmpleado(gerenteProyecto2);
        gerente.agregarEmpleado(programmer1);
        gerente.agregarEmpleado(programmer2);
        gerente.agregarEmpleado(programmer3);
        gerente.agregarEmpleado(programmer4);

        // Mostrar detalle de los empleados
        gerente.showDetails();
        gerenteProyecto1.showDetails();
        gerenteProyecto2.showDetails();
        programmer1.showDetails();
        programmer2.showDetails();
        programmer3.showDetails();
        programmer4.showDetails();
    }

    //---EJERCIÓ---
    // Superclase Animal
    static class Animal {
        public void hacerSonido(){
            System.out.println("El animal hace ruido");
        }
    }

    // Subclases Perro
    static class Perro extends Animal {
        @Override
        public void hacerSonido(){
            System.out.println("El perro ladra: ¡Guau Guau!");
        }

        // Método adicional para perro
        public void correr(){
            System.out.println("Esta corriendo felizmente");
        }
    }

    // Subclases Gato
    static class Gato extends Animal {
        @Override
        public void hacerSonido(){
            System.out.println("El gato maúlla: ¡Miau Miau!");
        }

        // Método adicional para gato
        public void cazar(){
            System.out.println("Esta cazando un ratón");
        }
    }

    // Nueva Subclases Pájaro
    static class Pajaro extends Animal {
        @Override
        public void hacerSonido(){
            System.out.println("El pájaro canta: ¡Pio Pio!");
        }

        // Método adicional para gato
        public void volar(){
            System.out.println("Esta volando alto en el cielo");
        }
    }

    // Función que recibe un objeto de tipo Animal y llama a su método hacerSonido
    public static void imprimirSonido(Animal animal){
        animal.hacerSonido();
    }



    /**-----DIFICULTAD EXTRA-----*/


    // Clase empleado
    public static abstract class Employ {
        private String id;
        private String nombre;

        // Constructor
        public Employ(String nombre){
            this.id = generarIdentificador();
            this.nombre = nombre;
        }

        // Método para generar un identificador único
        private String generarIdentificador() {
            return UUID.randomUUID().toString();
        }

        public String getId(){
            return id;
        }

        public String getNombre(){
            return nombre;
        }

        // Método abstracto que debe ser implementado por las subclases
        public abstract void showDetails();
    }

    // Clase Gerente
    public static class Manager extends Employ {
        private List<Employ> empleadosACargo;

        // Constructor
        public Manager(String nombre){
            super(nombre);
            this.empleadosACargo = new ArrayList<>();
        }

        // Añadir empleados a cargo
        public void agregarEmpleado(Employ empleado) {
            empleadosACargo.add(empleado);
        }

        // Método especifico para mostrar los empleados a cargo
        public void showEmployToPosition(){
            System.out.println("\nGerente: " + getNombre() + " tiene a cargo los siguientes empleados:");
            for (Employ e : empleadosACargo) {
                System.out.println("- " + e.getNombre());
            }
        }

        @Override
        public void showDetails() {
            System.out.println("\nGerente: " + getNombre() + " (ID: " + getId() + ")");
            showEmployToPosition();
        }
    }

    // Clase Gerente de Proyecto
    public static class ProjectManager extends Employ {
        private String currentProject;

        // Constructor
        public ProjectManager(String nombre, String currentProject){
            super(nombre);
            this.currentProject = currentProject;
        }

        // Método específico para mostrar el proyecto actual
        public void showProject() {
            System.out.println("\nGerente de Proyecto: " + getNombre() + " está gestionando el proyecto: " + currentProject);
        }

        @Override
        public void showDetails() {
            System.out.println("\nGerente de Proyecto: " + getNombre() + " (ID: " + getId() + ")");
            showProject();
        }
    }

    // Clase Programador
    public static class Programmer extends Employ {
        private String lenguajeDominante;

        // Constructor
        public Programmer(String nombre, String lenguajeDominante){
            super(nombre);
            this.lenguajeDominante = lenguajeDominante;
        }

        // Método específico para mostrar el lenguaje dominante del programador
        public void showLenguaje() {
            System.out.println("\nProgramador: " + getNombre() + " domina el lenguaje: " + lenguajeDominante);
        }

        @Override
        public void showDetails() {
            System.out.println("\nGerente: " + getNombre() + " (ID: " + getId() + ")");
            showLenguaje();
        }
    }

    /**-----DIFICULTAD EXTRA-----*/
}