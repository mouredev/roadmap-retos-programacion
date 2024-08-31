/**
 * kleyner098
 */
import java.util.ArrayList;

public class kleyner098 {
    
        /*
         * EJERCICIO:
         * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
         * implemente una superclase Animal y un par de subclases Perro y Gato,
         * junto con una función que sirva para imprimir el sonido que emite cada
         * Animal.
         *
         * DIFICULTAD EXTRA (opcional):
         * Implementa la jerarquía de una empresa de desarrollo formada por Empleados
         * que pueden ser Gerentes, Gerentes de Proyectos o Programadores.
         * Cada empleado tiene un identificador y un nombre.
         * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
         * actividad, y almacenan los empleados a su cargo.
         */
        public static void main(String[] args) {
    
            Animal animal = new Animal("Alberto", "humano");
            animal.sonido();
            Perro estrella = new Perro("Estrella","Yorkshire");
            estrella.sonido();
            Gato tony = new Gato("Tony", "Siamés");
            tony.sonido();

            System.out.println("---------------");

            Programador programador1 = new Programador(987654321, "Maria", "Java");
            Programador programador2 = new Programador(8423212, "Celia", "Kotlin");
            Programador programador3 = new Programador(6234234, "Daniel", "Phyton");
            Programador programador4 = new Programador(454232, "CArlos", "C++");

            GerenteProyecto gerenteProyecto1 = new GerenteProyecto(1111111, "Sara");
            GerenteProyecto gerenteProyecto2 = new GerenteProyecto(2222222, "Antonio");

            Gerente gerente1 = new Gerente(123456789, "Juan");
            
            gerente1.supervisar(gerenteProyecto1);
            gerente1.supervisar(gerenteProyecto2);

            gerenteProyecto1.supervisar(programador1);
            gerenteProyecto1.supervisar(programador4);
            gerenteProyecto2.supervisar(programador2);
            gerenteProyecto2.supervisar(programador3);

            System.out.println(gerente1);
            gerente1.supervisados();
            System.out.println("\n");

            System.out.println(gerenteProyecto1);
            System.out.println(gerenteProyecto2);
            gerenteProyecto1.supervisados();
            gerenteProyecto2.supervisados();
            System.out.println("\n");

            System.out.println(programador1);
            System.out.println(programador2);
            System.out.println(programador3);
            System.out.println(programador4);
        }
}

class Animal{
    
    String nombre;
    String raza;

    Animal(String nombre, String raza){
        this.nombre = nombre;
        this.raza = raza;
    }

    public void sonido(){
        System.out.println("Sonido genérico de animal");
    }
}

class Perro extends Animal{

    Perro(String nombre, String raza){
        super(nombre, raza);
    }

    @Override
    public void sonido() {
        System.out.println("Gua guau guauuuuuu");
    }
}

class Gato extends Animal{

    Gato(String nombre, String raza){
        super(nombre, raza);
    }

    @Override
    public void sonido() {
        System.out.println("Miau miel miauuuu");
    }
}

class Empleado{
    private int identificador;
    private String nombre;

    Empleado(int identificador, String nombre){
        this.identificador = identificador;
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Indentidicación: " + identificador + " | Nombre: " + nombre;  
    }
}

class Gerente extends Empleado{

    private ArrayList<GerenteProyecto> gerenteProyectos;

    Gerente(int identificador, String nombre){
        super(identificador, nombre);
        gerenteProyectos = new ArrayList<GerenteProyecto>();
    }

    @Override
    public String toString() {
        return "Gerente " + super.toString();
    }

    public void supervisar(GerenteProyecto nuevoGerenteProyecto){
        gerenteProyectos.add(nuevoGerenteProyecto);
    }

    public void supervisados(){
        System.out.println(this.toString() + " está a cargo de :");
        System.out.println(gerenteProyectos);
    }
}

class GerenteProyecto extends Empleado{
    private ArrayList<Programador> programadores;

    GerenteProyecto(int identificador, String nombre){
        super(identificador, nombre);
        programadores = new ArrayList<Programador>();
    }

    @Override
    public String toString() {
        return "Gerente de proyecto " + super.toString();
    }

    public void supervisar(Programador nuevoProgramador){
        programadores.add(nuevoProgramador);
    }

    public void supervisados(){
        System.out.println(this.toString() + "está a cargo de :");
        System.out.println(programadores);
    }
}

class Programador extends Empleado{
    private String leguaje;

    Programador(int identificador, String nombre, String lenguaje){
        super(identificador, nombre);
        this.leguaje = lenguaje;
    }

    @Override
    public String toString() {
        return "Programador " + super.toString() + " | Lenguaje de programación: " + leguaje;
    }
}