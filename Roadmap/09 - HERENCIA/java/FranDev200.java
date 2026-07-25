import java.util.ArrayList;

public class FranDev200 {

    static void main() {

        /*
            EJERCICIO:
            * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
            * implemente una superclase Animal y un par de subclases Perro y Gato,
            * junto con una función que sirva para imprimir el sonido que emite cada Animal.
         */

        ArrayList<Animal> animales = new ArrayList<>();
        animales.add(new Gato("Hipatia"));
        animales.add(new Perro("Rubi"));
        animales.add(new Gato("Cleo"));
        animales.add(new Perro("Indi"));
        animales.add(new Perro("Mark"));

        for(Animal a : animales){

            System.out.print(a.getNombre() + " hace ");
            a.getSonido();

        }


        // EJERCICIO EXTRA

        ArrayList<Empleado>  empleados = new ArrayList<>();

        Gerente g1 = new Gerente( 1, "Laura Gomez", 45, "Tecnología", 150000.00 );
        Gerente g2 = new Gerente( 2, "Carlos Diaz", 50, "Operaciones", 200000.00 );

        GerenteProyecto gp1 = new GerenteProyecto(3, "Mario Ruiz", 38, "Proyecto Atlas", "2026-06-30");
        GerenteProyecto gp2 = new GerenteProyecto(4, "Ana Torres", 35, "Proyecto Orion", "2026-09-15");
        GerenteProyecto gp3 = new GerenteProyecto(5, "Sergio Lopez", 40, "Proyecto Nova", "2027-01-20");

        Programador p1 = new Programador(6, "Ana Torres", 27, "Java", "Junior");
        Programador p2 = new Programador(7, "Sergio Lopez", 30, "Kotlin", "Mid");
        Programador p3 = new Programador(8, "Lucia Perez", 32, "C#", "Senior");
        Programador p4 = new Programador(9, "David Hernandez", 35, "Python", "Senior");
        Programador p5 = new Programador(10, "Elena Navarro", 26, "JavaScript", "Junior");
        Programador p6 = new Programador(11, "Carlos Diaz", 38, "TypeScript", "Senior");
        Programador p7 = new Programador(12, "Mario Ruiz", 33, "SQL", "Mid");
        Programador p8 = new Programador(13, "Raquel Gomez", 29, "Go", "Mid");

        g1.aniadirEmpleado(gp1);
        g1.aniadirEmpleado(gp2);
        g1.aniadirEmpleado(p1);
        g1.aniadirEmpleado(p2);

        g2.aniadirEmpleado(gp3);
        g2.aniadirEmpleado(p3);

        gp1.aniadirProgramador(p4);
        gp2.aniadirProgramador(p5);
        gp2.aniadirProgramador(p6);
        gp3.aniadirProgramador(p7);
        gp3.aniadirProgramador(p8);

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

        System.out.println("\n\nINFORMACION DE LOS EMPLEADOS DE LA EMPRESA.");
        System.out.println("===========================================");

        for (Empleado empleado :  empleados) {

            empleado.infoEmpleado();

        };

        System.out.println("\n\nEMPLEADOS ASIGANDOS A " + g1.getNombre());
        g1.infoEmpleadosASuCargo();

        System.out.println("\n\nEMPLEADOS ASIGANDOS A " + gp3.getNombre());
        gp3.infoProgramadoresASuCargo();

        g2.reunirseConDirectivos();
        gp2.planificarSprint();
        gp3.planificarSprint();

        p2.programando();
        p6.programando();
        p1.programando();
        p8.programando();
    }

    static abstract class Animal {
        private String nombre;

        public Animal() { }

        public Animal(String nombre) {

            setNombre(nombre);


        }

        public String getNombre() { return nombre; }

        public void setNombre(String nombre) { this.nombre = nombre; }

        public void getSonido() {
            System.out.println("");
        }

    }

    static class Gato extends Animal {

        public Gato(String name) {
            super(name);
        }

        @Override
        public void getSonido() {
            System.out.println("MIAU MIAU");
        }
    }

    static class Perro extends Animal {

        public Perro(String name) {
            super(name);
        }

        @Override
        public void getSonido() {
            System.out.println("GUAU GUAU");
        }
    }

    /*

        DIFICULTAD EXTRA (opcional):
        * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
        * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
        * Cada empleado tiene un identificador y un nombre.
        * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
        * actividad, y almacenan los empleados a su cargo.

     */

    static abstract class Empleado{

        private int id;
        private String nombre;
        private int edad;

        public Empleado() { }
        public Empleado(int id, String nombre, int edad) {

            this.id = id;
            this.nombre = nombre;
            this.edad = edad;

        }

        public int getId() { return id; }

        public void setId(int id) { this.id = id; }

        public String getNombre() { return nombre; }

        public void setNombre(String nombre) { this.nombre = nombre; }

        public int getEdad() { return edad; }

        public void setEdad(int edad) { this.edad = edad; }

        public void infoEmpleado(){}
    }
    static class Gerente extends Empleado{

        private String departamento;
        private double presupuesto;
        private ArrayList<Empleado> empleadosACargo = new ArrayList<>();

        public Gerente() {
            super();
        }

        public Gerente(int id, String nombre, int edad, String departamento,  double presupuesto) {
            super(id, nombre, edad);
            this.departamento = departamento;
            this.presupuesto = presupuesto;
        }

        public String getDepartamento() { return departamento; }

        public void setDepartamento(String departamento) { this.departamento = departamento; }

        public double getPresupuesto() { return presupuesto; }

        public void setPresupuesto(double presupuesto) { this.presupuesto = presupuesto; }

        public void aniadirEmpleado(Empleado empleado) {
            empleadosACargo.add(empleado);
        }

        public void reunirseConDirectivos(){
            System.out.println(getNombre() + " se está reuniendo con los directivos.");
        }

        @Override
        public void infoEmpleado(){
            System.out.println(getNombre() + "[" +getId() + "]: " + getEdad() + " años.");
            System.out.println("-----------------");
            System.out.println("Gerente del departamento de " +  getDepartamento());
            System.out.println("Su presupuesto asignado para el proyecto es: " + getPresupuesto());
            System.out.println("=================");
        }

        public void infoEmpleadosASuCargo(){
            for(Empleado empleado : empleadosACargo){

                empleado.infoEmpleado();

            }
        }
    }
    static class GerenteProyecto extends Empleado{

        private String proyectoAsignado;
        private String fechaEntrega;
        private ArrayList<Programador> programadoresACargo = new ArrayList<>();

        public GerenteProyecto() {
            super();
        }

        public GerenteProyecto(int id, String nombre, int edad, String departamento, String fechaEntrega) {
            super(id, nombre, edad);
            this.proyectoAsignado = departamento;
            this.fechaEntrega = fechaEntrega;
        }

        public String getProyectoAsignado() { return proyectoAsignado; }

        public void setProyectoAsignado(String proyectoAsignado) { this.proyectoAsignado = proyectoAsignado; }

        public String getFechaEntrega() { return fechaEntrega; }

        public void setFechaEntrega(String fechaEntrega) { this.fechaEntrega = fechaEntrega; }

        public void aniadirProgramador(Programador programador) {
            programadoresACargo.add(programador);
        }

        public void planificarSprint(){
            System.out.println(getNombre() + " ha planificado una sprint para hablar sobre el " +
                    "de " + getProyectoAsignado() + ". Su fecha de entrega es el " + getFechaEntrega());
        }

        @Override
        public void infoEmpleado(){
            System.out.println(getNombre() + "[" +getId() + "]: " + getEdad() + " años.");
            System.out.println("-----------------");
            System.out.println("Gerente del " +  getProyectoAsignado());
            System.out.println("La fecha máxima de entrega es el: " +  getFechaEntrega());
            System.out.println("=================");
        }

        public void infoProgramadoresASuCargo(){
            for(Programador programador : programadoresACargo){

                programador.infoEmpleado();

            }
        }

    }
    static class Programador extends Empleado{

        private String lenguajePrincipal;
        private String nivel;

        public Programador() { }

        public Programador(int id, String nombre, int edad, String lenguajePrincipal, String nivel) {
            super(id, nombre, edad);
            this.lenguajePrincipal = lenguajePrincipal;
            this.nivel = nivel;
        }

        public String getLenguajePrincipal() { return lenguajePrincipal; }

        public void setLenguajePrincipal(String lenguajePrincipal) { this.lenguajePrincipal = lenguajePrincipal; }

        public String getNivel() { return nivel; }

        public void setNivel(String nivel) { this.nivel = nivel; }

        public void programando(){

            System.out.println(getNombre() + " esta desarrollando una nueva funcionalidad para el proyecto.");

        }

        @Override
        public void infoEmpleado(){
            System.out.println(getNombre() + "[" +getId() + "]: " + getEdad() + " años.");
            System.out.println("-----------------");
            System.out.println("Programador " +  getNivel());
            System.out.println("Su lenguaje principal es " +  getLenguajePrincipal());
            System.out.println("=================");
        }
    }

}
