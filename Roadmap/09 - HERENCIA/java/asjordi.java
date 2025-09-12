import java.util.LinkedList;
import java.util.List;

public class Main {

    /**
     * La herencia es la capacidad de una clase para heredar o extender los atributos y métodos de otra clase.
     * Esto permite crear clases más especializadas a partir de clases más generales.
     * Es uno de los conceptos fundamentales de la programación orientada a objetos.
     * La clase hija o subclase puede tener atributos y métodos que no existen en la clase padre o superclase.
     * Con extends se indica que una clase hereda de otra.
     * La palabra clave super en Java se utiliza para referirse a la clase padre de la clase actual.
     * Se puede utilizar para llamar a métodos de la clase padre, acceder a variables de instancia de la clase padre y crear instancias de la clase padre.
     */

    public static void main(String[] args) {
        new Animal().hacerRuido();
        new Perro().hacerRuido();
        new Gato().hacerRuido();

        Gerente gerente = new Gerente(1, "Gerente");
        GerenteProyecto gerenteProyecto = new GerenteProyecto(2, "Gerente de Proyecto");
        Programador programador1 = new Programador(3, "Programador Java Back", "Java");
        Programador programador2 = new Programador(4, "Programador Python Back", "Python");
        Programador programador3 = new Programador(5, "Programador Js Front", "JavaScript");

        gerente.contratarEmpleado(gerenteProyecto);
        gerente.contratarEmpleado(programador1);
        gerente.contratarEmpleado(programador2);
        gerente.contratarEmpleado(programador3);

        gerente.mostrarEmpleados();

        gerenteProyecto.contratarEmpleado(programador1);
        gerenteProyecto.contratarEmpleado(programador2);
        gerenteProyecto.contratarEmpleado(programador3);

        gerenteProyecto.mostrarEmpleados();
    }

    static class Animal {
        public void hacerRuido() {
            System.out.println("Haciendo ruido");
        }
    }

    static class Perro extends Animal {
        public void hacerRuido() {
            System.out.println("Guau");
        }
    }

    static class Gato extends Animal {
        public void hacerRuido() {
            System.out.println("Miau");
        }
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
     * pueden ser Gerentes, Gerentes de Proyecto o Programadores.
     * Cada empleado tiene un identificador y un nombre.
     * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
     * actividad, y almacenan los empleados a su cargo.
     */

    static class Empleado {
        private int id;
        private String nombre;
        List<Empleado> empleados;

        public Empleado(int id, String nombre) {
            this.id = id;
            this.nombre = nombre;
            this.empleados = new LinkedList<>();
        }

        public int getId() {
            return id;
        }

        public String getNombre() {
            return nombre;
        }

        public void contratarEmpleado(Empleado empleado) {
            empleados.add(empleado);
        }

        public void mostrarEmpleados() {
            System.out.println("Empleados a cargo de " + getNombre() + ":");
            for (Empleado empleado : empleados) {
                System.out.println(empleado.getNombre());
            }
        }
    }

    static class Gerente extends Empleado {
        public Gerente(int id, String nombre) {
            super(id, nombre);
        }
    }

    static class GerenteProyecto extends Empleado {
        public GerenteProyecto(int id, String nombre) {
            super(id, nombre);
            empleados = new LinkedList<>();
        }
    }

    static class Programador extends Empleado {
        String lenguaje;

        public Programador(int id, String nombre, String lenguaje) {
            super(id, nombre);
            this.lenguaje = lenguaje;
        }

        public String getLenguaje() {
            return lenguaje;
        }
    }

}
