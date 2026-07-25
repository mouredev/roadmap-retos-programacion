import java.util.ArrayList;

public class AnaLauDB {
    public static void main(String[] args) {
        // Animales
        Animal perro = new Perro("Toby");
        Animal gato = new Gato("Garfield");

        perro.hacerSonido();
        gato.hacerSonido();

        // Empleados
        Gerente jefe = new Gerente(1, "Laura");
        GerenteDeProyecto gproyecto = new GerenteDeProyecto(2, "Leonel", "App Móvil");
        Programador prog1 = new Programador(3, "Abril", "Java");
        Programador prog2 = new Programador(4, "Angie", "Python");

        jefe.agregarEmpleado(gproyecto);
        jefe.agregarEmpleado(prog1);
        jefe.agregarEmpleado(prog2);

        jefe.mostrarInfo();
        gproyecto.mostrarInfo();
        prog1.mostrarInfo();
        prog2.mostrarInfo();
    }

    // ==================
    // EJERCICIO ANIMALES
    // ==================
    public static class Animal {
        String nombre;

        public Animal(String nombre) {
            this.nombre = nombre;
        }

        public void hacerSonido() {
            System.out.println("El animal hace un sonido.");
        }
    }

    public static class Perro extends Animal {
        public Perro(String nombre) {
            super(nombre);
        }

        @Override
        public void hacerSonido() {
            System.out.println(nombre + " el perro hace ¡Guau guau!");
        }
    }

    public static class Gato extends Animal {
        public Gato(String nombre) {
            super(nombre);
        }

        @Override
        public void hacerSonido() {
            System.out.println(nombre + " el gato hace ¡Miau miau!");
        }
    }

    // ==================
    // EXTRA EMPLEADOS
    // ==================
    public static class Empleado {
        int id;
        String nombre;

        public Empleado(int id, String nombre) {
            this.id = id;
            this.nombre = nombre;
        }

        public void mostrarInfo() {
            System.out.println("ID: " + id + ", Nombre: " + nombre);
        }
    }

    public static class Gerente extends Empleado {
        ArrayList<Empleado> empleadosACargo = new ArrayList<>();

        public Gerente(int id, String nombre) {
            super(id, nombre);
        }

        public void agregarEmpleado(Empleado e) {
            empleadosACargo.add(e);
        }

        @Override
        public void mostrarInfo() {
            System.out.println("Gerente: " + id + " - " + nombre);
            System.out.println("Empleados a cargo:");
            for (Empleado e : empleadosACargo) {
                System.out.println("   - " + e.nombre);
            }
        }
    }

    public static class GerenteDeProyecto extends Empleado {
        String proyecto;

        public GerenteDeProyecto(int id, String nombre, String proyecto) {
            super(id, nombre);
            this.proyecto = proyecto;
        }

        @Override
        public void mostrarInfo() {
            System.out.println("Gerente de Proyecto: " + id + " - " + nombre + " (Proyecto: " + proyecto + ")");
        }
    }

    public static class Programador extends Empleado {
        String lenguaje;

        public Programador(int id, String nombre, String lenguaje) {
            super(id, nombre);
            this.lenguaje = lenguaje;
        }

        @Override
        public void mostrarInfo() {
            System.out.println("Programador: " + id + " - " + nombre + " (Lenguaje: " + lenguaje + ")");
        }
    }
}
