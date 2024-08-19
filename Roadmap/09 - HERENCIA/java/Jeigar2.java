import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Jeigar {
    /*
     * EJERCICIO:
     * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
     * implemente una superclase Animal y un par de subclases Perro y Gato,
     * junto con una función que sirva para imprimir el sonido que emite cada Animal.
     *
     * DIFICULTAD EXTRA (opcional):
     * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
     * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
     * Cada empleado tiene un identificador y un nombre.
     * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
     * actividad, y almacenan los empleados a su cargo.
     */

    public static void main(String[] args) {
        MiGato gato = new MiGato();
        MiPerro perro = new MiPerro();
        gato.sonido();
        perro.sonido();

        Programador p1 = new Programador("R2D2", "C");
        Programador p2 = new Programador("C3P0", "COBOL");
        Programador p3 = new Programador("Spok", "FORTRAN");
        Programador p4 = new Programador("Bender", "GO");
        Programador p5 = new Programador("WALL-E", "KOTRLIN");
        Programador p6 = new Programador("HAL 9000", "PYTHON");
        GerenteProyecto neo = new GerenteProyecto("Neo", "Sion");
        neo.setProyecto("Defender la base");
        neo.setPresupuesto(2000.00);
        neo.contratarProgramador(p1);
        neo.contratarProgramador(p2);
        GerenteProyecto trinity = new GerenteProyecto("Trinity", "Matrix");
        trinity.setProyecto("Buscar a Morfeo");
        trinity.setPresupuesto(3000.00);
        trinity.contratarProgramador(p3);
        trinity.contratarProgramador(p4);
        trinity.contratarProgramador(p5);

        System.out.println(neo);
        System.out.println(trinity);
        System.out.println(p3);
        trinity.liberarProgramador(p6);
        trinity.liberarProgramador(p3);
        System.out.println(p3);
        System.out.println(p6);
        if(!p6.isAsignado()){
            System.out.println("Puedes dar formación al Empleado: " + p6.getNombre());
        }
    }
}

abstract class MiAnimal {
    public MiAnimal(){
        super();
    }
    public void sonido(){
        System.out.print("Mi animalito hace un sonido :");
    }
}

class MiGato extends MiAnimal{
    @Override
    public void sonido() {
        super.sonido();
        System.out.println("¡Miau!");
    }
}

class MiPerro extends MiAnimal{
    @Override
    public void sonido() {
        super.sonido();
        System.out.println("¡Guau!");
    }
}

abstract class Empleado {
    private long identificador;
    private String nombre;
    private String departamento;

    public Empleado(String nombre) {
        this.nombre = nombre;
        this.identificador = Math.abs(new Random().nextLong());
    }

    public long getIdentificador() {
        return identificador;
    }

    public void setIdentificador(long identificador) {
        this.identificador = identificador;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Empleado{" +
                "identificador=" + identificador +
                ", nombre='" + nombre + '\'' +
                ", departamento='" + departamento + '\'' +
                '}';
    }
}

class Programador extends Empleado {
    private String lenguaje;
    private boolean asignado;

    public Programador(String nombre) {
        super(nombre);
    }
    public Programador(String nombre, String lenguaje) {
        super(nombre);
        this.lenguaje = lenguaje;
    }

    public String getLenguaje() {
        return lenguaje;
    }

    public void setLenguaje(String lenguaje) {
        this.lenguaje = lenguaje;
    }

    public boolean isAsignado() {
        return asignado;
    }

    public void asignar() {
        this.asignado = true;
    }
    public void liberar() {
        this.asignado = false;
    }

    @Override
    public String toString() {
        return "Programador{" + super.toString() +
                ", lenguaje='" + lenguaje + '\'' +
                ", asignado=" + asignado +
                '}';
    }
}

abstract class Gerente extends Empleado {

    private double presupuesto;

    public Gerente(String nombre) {
        super(nombre);
    }

    public double getPresupuesto() {
        return presupuesto;
    }

    public void setPresupuesto(double presupuesto) {
        this.presupuesto = presupuesto;
    }

    @Override
    public String toString() {
        return super.toString() + ", presupuesto=" + presupuesto;
    }
}

class GerenteProyecto extends Gerente {

    private String proyecto;
    private List<Programador> programadores;


    public GerenteProyecto(String nombre, String departamento) {
        super(nombre);
        super.setDepartamento(departamento);
        programadores = new ArrayList<>();
    }

    public void contratarProgramador(Programador programador){
        if (!programadores.contains(programador)){
            programadores.add(programador);
            programador.asignar();
            programador.setDepartamento(getDepartamento());
        }
    }

    public Programador liberarProgramador (Programador programador){
        if(programadores.contains(programador)){
            programadores.remove(programador);
            programador.liberar();
            programador.setDepartamento(null);
            return programador;
        } else {
            System.out.println(programador.getIdentificador() + " " + programador.getNombre() + " No está contratado por ti");
            return null;
        }
    }

    public String getProyecto() {
        return proyecto;
    }

    public void setProyecto(String proyecto) {
        this.proyecto = proyecto;
    }

    @Override
    public String toString() {
        return "GerenteProyecto{" + super.toString() +
                ", proyecto='" + proyecto + '\'' +
                ", programadores (" + programadores.size() + ")=" + programadores +
                '}';
    }
}
