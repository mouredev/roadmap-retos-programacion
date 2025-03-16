import java.util.ArrayList;
import java.util.List;


public class GustavoGomez19 {

    /*
     * EJERCICIO:
     * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
     * implemente una superclase Animal y un par de subclases Perro y Gato,
     * junto con una función que sirva para imprimir el sonido que emite cada
     * Animal.
     */
    public static void main(String[] args) {

        Perro p1 = new Perro("Roko");
        p1.sonido();
        Gato g1 = new Gato("Gael");
        g1.sonido();

        // Ejercicio extra
        Gerente gerente = new Gerente(1, "Gustavo");
        gerente.coordinarProyectos();

        GerenteProyecto gerenteProyecto1 = new GerenteProyecto(2, "Katerine", "Proyecto 1");
        GerenteProyecto gerenteProyecto2 = new GerenteProyecto(3, "Javier", "Proyecto 2");
        gerenteProyecto1.coordinarProyecto();
        gerenteProyecto2.coordinarProyecto();

        Programador programador1 = new Programador(4, "María José", "Java");
        Programador programador2 = new Programador(5, "Adolfo", "JavaScript");
        Programador programador3 = new Programador(6, "Johnny", "Pytho");
        Programador programador4 = new Programador(7, "Joan", "Ruby");

        programador1.codificar();
        programador2.codificar();
        programador3.codificar();
        programador4.codificar();

        gerente.agregarEmpleado(gerenteProyecto1);
        gerente.agregarEmpleado(gerenteProyecto2);

        gerenteProyecto1.agregarEmpleado(programador1);
        gerenteProyecto1.agregarEmpleado(programador4);
        gerenteProyecto2.agregarEmpleado(programador2);
        gerenteProyecto2.agregarEmpleado(programador3);

        gerente.listarEmpleados();
        gerenteProyecto1.listarEmpleados();
        programador1.agregarEmpleado(programador4);
    }

    static class Animal {
        String nombre;

        public Animal(String nombre) {
            this.nombre = nombre;
        }

        public void sonido() {

        }
    }

    static class Perro extends Animal {
        public Perro(String nombre) {
            super(nombre);
        }

        @Override
        public void sonido() {
            System.out.println("!Guau¡");
        }
    }

    static class Gato extends Animal {
        public Gato(String nombre) {
            super(nombre);
        }

        public void sonido() {
            System.out.println("!Miau¡");
        }
    }

    // Ejercicio extra
    /*
     * Implementa la jerarquía de una empresa de desarrollo formada por Empleados
     * que
     * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
     * Cada empleado tiene un identificador y un nombre.
     * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
     * actividad, y almacenan los empleados a su cargo.
     */
    /**
     
     */
    static class Empleado{
        int id;
        String nombre;
        List<Empleado> empleados;
        

        public Empleado(int id, String nombre){
            this.id = id;
            this.nombre = nombre;
            this.empleados = new ArrayList<>();
        }

        public void agregarEmpleado(Empleado empleado){
            this.empleados.add(empleado);
        }

        public void listarEmpleados(){
            for (Empleado empleado : empleados) {
                System.out.println("El empleado " + empleado.nombre + " está bajo el mando de " + nombre);
            }
        }        
    }

    static class Gerente extends Empleado{
        public Gerente(int id, String nombre){
            super(id, nombre);
        }
        public void coordinarProyectos(){
            System.out.println(this.nombre + " está coordinando todos los proyectos de la empresa");
        }
    }

    static class GerenteProyecto extends Empleado{
        String proyecto;
        public GerenteProyecto(int id, String nombre, String proyecto){
            super(id, nombre);
            this.proyecto = proyecto;
        }
        public void coordinarProyecto(){
            System.out.println(this.nombre + " está coordinando su proyecto " + this.proyecto);
        }

    }

    static class Programador extends Empleado{
        String lenguaje;
        public Programador(int id, String nombre, String lenguaje){
            super(id, nombre);
            this.lenguaje = lenguaje;
        }

        public void codificar(){
            System.out.println(this.nombre + " etsá codificando la aplicación con el lenguaje " + lenguaje + ".");
        } 
        
        public void agregarEmpleado(Empleado empleado){
            System.out.println("El programador " + this.nombre + " no puede tener personal a cargo.");
        }


    }
    
}
