import java.util.ArrayList;

public class FranDev200 {

/*

    EJERCICIO:
    * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
    * implemente una superclase Animal y un par de subclases Perro y Gato,
    * junto con una función que sirva para imprimir el sonido que emite cada Animal.

    */

    static void main() {

        ArrayList<AnimalFran> animales = new ArrayList<AnimalFran>();
        animales.add(new PerroFran("Rubi", "Bodegero"));
        animales.add(new GatoFran("Hipatia", "Ragdoll"));
        animales.add(new PerroFran("Indi", "Terrier"));
        animales.add(new PerroFran("Beny", "Golden Retriever"));
        animales.add(new GatoFran("Lili", "Persa"));

        for (AnimalFran animal: animales){
            System.out.println(animal.getNombre() + " (" + animal.getRaza() + ") --> " + animal.sonido());
        }


        // EJERCICIO EXTRA

        // Crear y añadir empleados

        ArrayList<EmpleadoFran> empleados = new ArrayList<>();

        GerenteFran g1 = new GerenteFran(1, "Laura Gomez", 4200.00);
        GerenteFran g2 = new GerenteFran(2, "Carlos Diaz", 4500.00);

        GerenteDeProyectosFran gp1 = new GerenteDeProyectosFran(6, "Mario Ruiz", 3400.00);
        GerenteDeProyectosFran gp2 = new GerenteDeProyectosFran(7, "Ana Torres", 3300.00);
        GerenteDeProyectosFran gp3 = new GerenteDeProyectosFran(8, "Sergio Lopez", 3200.00);

        ProgramadorFran p1  = new ProgramadorFran(1,  "Ana Torres",       2200.00, "Java",        2);
        ProgramadorFran p2  = new ProgramadorFran(2,  "Sergio Lopez",     2400.00, "Kotlin",      3);
        ProgramadorFran p3  = new ProgramadorFran(3,  "Lucia Perez",      2600.00, "C#",          4);
        ProgramadorFran p4  = new ProgramadorFran(4,  "David Hernandez",  2800.00, "Python",      5);
        ProgramadorFran p5  = new ProgramadorFran(5,  "Elena Navarro",    2300.00, "JavaScript",  2);
        ProgramadorFran p6  = new ProgramadorFran(6,  "Carlos Diaz",      3000.00, "TypeScript",  6);
        ProgramadorFran p7  = new ProgramadorFran(7,  "Mario Ruiz",       2700.00, "SQL",         4);
        ProgramadorFran p8  = new ProgramadorFran(8,  "Paula Sanchez",    2900.00, "Java",        5);
        ProgramadorFran p9  = new ProgramadorFran(9,  "Borja Martin",     2500.00, "C++",         3);
        ProgramadorFran p10 = new ProgramadorFran(10, "Raquel Gomez",     3100.00, "Go",          7);

        empleados.add(g1);
        empleados.add(g2);

        empleados.add(gp1);
        empleados.add(gp2);
        empleados.add(gp3);

        empleados.add(p1);
        empleados.add(p2);
        empleados.add(p3);
        empleados.add(p4);
        empleados.add(p5);
        empleados.add(p6);
        empleados.add(p7);
        empleados.add(p8);
        empleados.add(p9);
        empleados.add(p10);

        g1.aniadirGerenteDeProyecto(gp1);
        g1.aniadirGerenteDeProyecto(gp2);
        g2.aniadirGerenteDeProyecto(gp3);

        gp1.aniadirProgramador(p1);
        gp1.aniadirProgramador(p2);
        gp1.aniadirProgramador(p5);
        gp1.aniadirProgramador(p6);

        gp2.aniadirProgramador(p3);
        gp2.aniadirProgramador(p8);
        gp2.aniadirProgramador(p10);

        gp3.aniadirProgramador(p4);
        gp3.aniadirProgramador(p7);
        gp3.aniadirProgramador(p9);

        System.out.println("\n\nEMPLEADOS DE LA EMPRESA");
        System.out.println("-----------------------");
        for (EmpleadoFran empleado: empleados){
            System.out.println(empleado.getId() + " - " + empleado.getNombre() + ": " + empleado.getSalario() + "€ brutos al año.");
        }
        System.out.println("-----------------------");

        System.out.println("[ 8:00 AM ]");
        for (EmpleadoFran empleado: empleados){
            empleado.ficharEntrada();
        }
        System.out.println("============");
        System.out.println("\n[ 17:00 PM ]");
        for (EmpleadoFran empleado: empleados){
            empleado.ficharSalida();
        }

        System.out.println("\n- - - - - - - - - - - - -");
        g1.listarGerentesACargo();
        System.out.println("\n- - - - - - - - - - - - -");
        g2.listarGerentesACargo();
        System.out.println("- - - - - - - - - - - - -");
        g1.asignarProyecto(gp1, "Pagina web empresa");
        System.out.println("\n- - - - - - - - - - - - -");
        gp1.listarProgramadoresACargo();
        System.out.println("\n- - - - - - - - - - - - -");
        gp2.listarProgramadoresACargo();
        System.out.println("\n- - - - - - - - - - - - -");
        gp3.listarProgramadoresACargo();
        System.out.println("- - - - - - - - - - - - -");

        System.out.println();

        gp2.planificarTareas();
        gp1.realizarDaily();
        gp3.planificarTareas();

        System.out.println();

        System.out.println("-_".repeat(25));
        for(ProgramadorFran programador: gp1.listaProgramadores()){
            programador.documentar();
        }

        System.out.println("-_".repeat(25));
        for(ProgramadorFran programador: gp2.listaProgramadores()){
            programador.programar();
        }

        System.out.println("-_".repeat(25));
        for(ProgramadorFran programador: gp3.listaProgramadores()){
            programador.ejecutarTests();
        }

    }

}

abstract class AnimalFran {

    private String nombre;
    private String raza;

    public AnimalFran(String nombre, String raza){
        setNombre(nombre);
        setRaza(raza);
    }

    public String getNombre() { return nombre; }

    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getRaza() { return raza; }

    public void setRaza(String raza) { this.raza = raza; }

    public String sonido(){ return null;}

}
class PerroFran extends AnimalFran {

    public PerroFran(String nombre, String raza){
        super(nombre, raza);
    }

    @Override
    public String sonido(){
        return "Woof Woof!";
    }

}
class GatoFran extends AnimalFran {

    public GatoFran(String nombre, String raza){
        super(nombre, raza);
    }

    @Override
    public String sonido(){
        return "Miau Miau!";
    }

}

/*

DIFICULTAD EXTRA (opcional):
* Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
* pueden ser Gerentes, Gerentes de Proyectos o Programadores.
* Cada empleado tiene un identificador y un nombre.
* Dependiendo de su labor, tienen propiedades y funciones exclusivas de su actividad, y almacenan los empleados a su cargo.

*/

class EmpleadoFran {

    private int id;
    private String nombre;
    private double salario;

    public EmpleadoFran(int id, String nombre, double salario){
        setId(id);
        setNombre(nombre);
        setSalario(salario);

    }

    public String getNombre() { return nombre; }

    public void setNombre(String nombre) { this.nombre = nombre; }

    public int getId() { return id; }

    public void setId(int id) { this.id = id; }

    public double getSalario() { return salario; }

    public void setSalario(double salario) { this.salario = salario; }

    public void ficharEntrada(){
        System.out.println(getNombre() + " ha entrado a trabajar.");
    }

    public void ficharSalida(){
        System.out.println(getNombre() + " ha salido de trabajar.");
    }

}

class GerenteFran extends EmpleadoFran {

    public GerenteFran(int id, String nombre, double salario){
        super(id, nombre, salario);
    }

    private ArrayList<GerenteDeProyectosFran> gerenteDeProyectosArrayList = new ArrayList<>();

    public void aniadirGerenteDeProyecto(GerenteDeProyectosFran gerenteDeProyectos){
        gerenteDeProyectosArrayList.add(gerenteDeProyectos);
    }

    public void listarGerentesACargo(){

        System.out.println("Gerentes de proyectos a cargo de " + getNombre());

        for(GerenteDeProyectosFran gerenteDeProyectos: gerenteDeProyectosArrayList){
            System.out.println(gerenteDeProyectos.getId() + " - " + gerenteDeProyectos.getNombre());
        }
    }

    public void asignarProyecto(GerenteDeProyectosFran gerenteAsignado, String proyecto){
        System.out.println("El proyecto de " + proyecto + " ha sido asignado a " + gerenteAsignado.getNombre());
    }

}

class GerenteDeProyectosFran extends EmpleadoFran {

    public GerenteDeProyectosFran(int id, String nombre, double salario){
        super(id, nombre, salario);
    }

    private ArrayList<ProgramadorFran> plantillaProgramadores = new ArrayList<>();

    public void aniadirProgramador(ProgramadorFran p){
        plantillaProgramadores.add(p);
    }

    public void listarProgramadoresACargo(){

        System.out.println("Programadores a cargo de " + getNombre());

        for(ProgramadorFran programador: plantillaProgramadores){
            System.out.println("=====================");
            System.out.println(programador.getId() + " - " + programador.getNombre());
            System.out.println("Años de experiencia: " + programador.getExperiencia());
            System.out.println("Lenguaje principal: " + programador.getLenguajePrincipal());
            System.out.println("=====================");
        }
    }

    public void planificarTareas(){
        System.out.println(getNombre() + " ha dividido las tareas entre sus programadores a cargo.");
    }

    public void realizarDaily(){
        System.out.println(getNombre() + " ha comenzado la reunion diaria a las 9:00 AM.");
    }

    public ArrayList<ProgramadorFran> listaProgramadores(){
        return plantillaProgramadores;
    }

}

class ProgramadorFran extends EmpleadoFran {

    private String lenguajePrincipal;
    private int experiencia;

    public ProgramadorFran(int id, String nombre, double salario, String lenguajePrincipal, int experiencia){
        super(id, nombre, salario);
        setExperiencia(experiencia);
        setLenguajePrincipal(lenguajePrincipal);
    }

    public String getLenguajePrincipal() {
        return lenguajePrincipal;
    }

    public void setLenguajePrincipal(String lenguajePrincipal) {
        this.lenguajePrincipal = lenguajePrincipal;
    }

    public int getExperiencia() {
        return experiencia;
    }

    public void setExperiencia(int experiencia) {
        this.experiencia = experiencia;
    }

    public void programar(){
        System.out.println(getId() + " - " + getNombre() + " esta desarrollando una nueva funcionalidad.");
    }

    public void documentar(){
        System.out.println(getId() + " - " + getNombre() + " esta documentando las tareas realizadas hoy.");
    }

    public void ejecutarTests(){
        System.out.println(getId() + " - " + getNombre() + " esta ejecutando los tests sobre la nueva funcionalidad.");
    }

}
