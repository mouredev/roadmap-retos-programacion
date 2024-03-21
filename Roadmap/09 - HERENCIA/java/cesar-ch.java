import java.util.ArrayList;
import java.util.List;

/*
    #09 HERENCIA Y POLIMORFISMO
*/

class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    public void sound() {
        System.out.println(name + " makes a sound.");
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    public void sound() {
        System.out.println("Guau, guau!");
    }
}

class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    public void sound() {
        System.out.println("Miau, miau!");
    }
}

/* 
    DIFICULTAD EXTRA 
*/

class Empleado {
    protected int id;
    protected String nombre;
    protected List<Empleado> empleadosACargo;

    public Empleado(int id, String nombre) {
        this.id = id;
        this.nombre = nombre;
        this.empleadosACargo = new ArrayList<>();
    }

    public void agregarEmpleado(Empleado empleado) {
        this.empleadosACargo.add(empleado);
    }

    public void imprimirEmpleados() {
        for (Empleado empleado : empleadosACargo) {
            System.out.println(empleado.nombre);
        }
    }
}

class Gerente extends Empleado {
    public Gerente(int id, String nombre) {
        super(id, nombre);
    }

    public void actividad() {
        System.out.println("Gerente");
    }
}

class GerenteProyecto extends Empleado {
    public GerenteProyecto(int id, String nombre) {
        super(id, nombre);
    }

    public void actividad() {
        System.out.println("Gerente de Proyecto");
    }
}

class Programador extends Empleado {
    public Programador(int id, String nombre) {
        super(id, nombre);
    }

    public void actividad() {
        System.out.println("Programador");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog("Fido");
        dog.sound();
        Cat cat = new Cat("Mishi");
        cat.sound();

        Gerente gerente = new Gerente(1, "Juan");
        GerenteProyecto gerenteProyecto = new GerenteProyecto(2, "Pedro");
        GerenteProyecto gerenteProyecto2 = new GerenteProyecto(3, "Luis");
        Programador programador = new Programador(4, "Maria");
        Programador programador2 = new Programador(5, "Ana");
        Programador programador3 = new Programador(6, "Jorge");
        Programador programador4 = new Programador(7, "Carlos");

        gerente.agregarEmpleado(gerenteProyecto);
        gerente.agregarEmpleado(gerenteProyecto2);

        gerenteProyecto.agregarEmpleado(programador);
        gerenteProyecto.agregarEmpleado(programador2);
        gerenteProyecto2.agregarEmpleado(programador3);
        gerenteProyecto2.agregarEmpleado(programador4);

        gerente.imprimirEmpleados();
        gerenteProyecto.imprimirEmpleados();
        gerenteProyecto2.imprimirEmpleados();
        programador.imprimirEmpleados();

        gerente.actividad();
        gerenteProyecto.actividad();
        programador.actividad();
    }
}
