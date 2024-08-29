import java.util.ArrayList;
import java.util.List;

public class TofeDev {
    public static void main(String[] args) {
        Gato gato = new Gato("Miri", 3);
        Perro perro = new Perro("Firulais", 5);
    
        System.out.println("Un gato llamado " + gato.nombre + " hace: ");
        gato.sonido();
        System.out.println("y tiene " + gato.edad + " años de edad.");
        System.out.println("Un perro llamado " + perro.nombre + " hace: ");
        perro.sonido();
        System.out.println("y tiene " + perro.edad + " años de edad.");

        //Extra
        Gerente jefe = new Gerente(1, "Ricardo Gonzales");
        jefe.coordEmpresa();

        JefeProyecto projectManager1 = new JefeProyecto(2, "Marta Rodriguez", "Proyecto 1");
        projectManager1.coordProyecto();

        JefeProyecto projectManager2 = new JefeProyecto(3, "Carolina Espíndola", "Proyecto 2");
        projectManager2.coordProyecto();
    
        Programador programador1 = new Programador(4, "Mauricio Villanueva", "Backend");
        programador1.trabajo();
        Programador programador2 = new Programador(5, "Carlos Lopez", "Frontend");
        programador2.trabajo();
        Programador programador3 = new Programador(6, "Rubén Gutierrez", "Backend");
        programador3.trabajo();
        Programador programador4 = new Programador(7, "Guadalupe del Valle", "DevOps");
        programador4.trabajo();

        projectManager1.agregarEmpleado(programador1);
        projectManager1.agregarEmpleado(programador2);
        projectManager2.agregarEmpleado(programador3);
        projectManager2.agregarEmpleado(programador4);

        projectManager1.listarEmpleados();
        projectManager2.listarEmpleados();
    }
    
    static class Animal {
        String nombre;
        int edad;
        
        public Animal(String nombre, int edad) {
            this.nombre = nombre;
            this.edad = edad;
        }
        
        public void sonido() {
        }
    }

    static class Gato extends Animal {

        public Gato(String nombre, int edad) {
            super(nombre, edad);
        }
        
        @Override
        public void sonido() {
            System.out.println("Miau");
        }
    }

    static class Perro extends Animal {
        public Perro(String nombre, int edad) {
            super(nombre, edad);
        }
        
        @Override
        public void sonido() {
            System.out.println("Guau");
        }
    }

    /* DIFICULTAD EXTRA (opcional):
    * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
    * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
    * Cada empleado tiene un identificador y un nombre.
    * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
    * actividad, y almacenan los empleados a su cargo.
    */

    static class Empleado {
        int id;
        String nombre;
        List<Empleado> empleados;
        
        public Empleado(int id, String nombre) {
            this.id = id;
            this.nombre = nombre;
            this.empleados = new ArrayList<>();
        }

        public void agregarEmpleado(Empleado empleado) {
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
        public void coordEmpresa(){
            System.out.println(this.nombre + " está a cargo de todos los proyectos de la empresa");
        }
    }

    static class JefeProyecto extends Empleado{
        String proyecto;
        public JefeProyecto(int id, String nombre, String proyecto){
            super(id, nombre);
            this.proyecto = proyecto;
        }
        public void coordProyecto(){
            System.out.println(this.nombre + " tiene a cargo el " + this.proyecto);
        }

    }

    static class Programador extends Empleado{
        String tipo;
        public Programador(int id, String nombre, String tipo){
            super(id, nombre);
            this.tipo = tipo;
        }

        public void trabajo(){
            System.out.println(this.nombre + " es un desarrollador " + tipo + ".");
        }
    }
}
