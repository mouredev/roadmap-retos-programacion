import java.util.List;
import java.util.ArrayList;

public class miguelex {
    public static void main(String[] args) {
        Perro perro = new Perro("Milú", "Guau, guau");
        Gato gato = new Gato("Garfield", "Miauuuuu");

        perro.hacerSonido();
        gato.hacerSonido();

        Gerente gerente = new Gerente(1, "Miguel", List.of(new Empleado(101, "Juan"), new Empleado(102, "Pedro"), new Empleado(103, "Luis")));
        gerente.mostrarPersonas();

        Programador programador = new Programador(2, "Juan", List.of("Java", "Python", "C++"));
        programador.mostrarLenguajes();

        GerenteProyecto gerenteP = new GerenteProyecto(3, "Pedro", List.of(new Empleado(104, "Juan"), new Empleado(105, "Rebeca")));
        gerenteP.mostrarPersonas();
    }
}

class Animal {
    private String nombre;
    private String sonido;

    public Animal(String nombre, String sonido) {
        this.nombre = nombre;
        this.sonido = sonido;
    }

    public void hacerSonido() {
        System.out.println("El animal con nombre " + this.nombre + " está diciendo " + this.sonido);
    }
}

class Perro extends Animal {
    public Perro(String nombre, String sonido) {
        super(nombre, sonido);
    }
}

class Gato extends Animal {
    public Gato(String nombre, String sonido) {
        super(nombre, sonido);
    }
}

class Empleado {
    public int id;
    public String nombre;

    public Empleado(int id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Empleado [id=" + id + ", nombre=" + nombre + "]";
    }
}

class Gerente extends Empleado {
    public List<Empleado> personas;

    public Gerente(int id, String nombre, List<Empleado> personas) {
        super(id, nombre);
        this.personas = personas;
    }

    public void mostrarPersonas() {
        for (Empleado persona : this.personas) {
            System.out.println(persona);
        }
    }
}

class GerenteProyecto extends Empleado {
    public List<Empleado> programadores;

    public GerenteProyecto(int id, String nombre, List<Empleado> programadores) {
        super(id, nombre);
        this.programadores = programadores;
    }

    public void mostrarPersonas() {
        for (Empleado persona : this.programadores) {
            System.out.println(persona.nombre);
        }
    }
}

class Programador extends Empleado {
    public List<String> lenguajes;

    public Programador(int id, String nombre, List<String> lenguajes) {
        super(id, nombre);
        this.lenguajes = lenguajes;
    }

    public void mostrarLenguajes() {
        for (String lenguaje : this.lenguajes) {
            System.out.println(lenguaje);
        }
    }
}
