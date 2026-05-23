public class Meir {
    public static void main(String[] args) {

        Perro p = new Perro("Perro");
        p.sonido();
        Gato g = new Gato("Gato");
        g.sonido();

        //Extra
        Manager manager  = new Manager("Mark", 1);
        ProjectManager projectManager= new ProjectManager("Eva", 2, "Proyecto1");
        ProjectManager projectManager2 = new ProjectManager("Carlos", 3, "Proyecto2");
        Programmer programmer = new Programmer("Juan", 3, "Java");
        Programmer programmer2 = new Programmer("Pedro", 4, "Python");
        Programmer programmer3 = new Programmer("Ana", 5, "C#");
        Programmer programmer4 = new Programmer("Maria", 6, "C++");

        manager.añadirEmpleado(projectManager);
        manager.añadirEmpleado(projectManager2);

        projectManager.añadirEmpleado(programmer);
        projectManager.añadirEmpleado(programmer2);

        projectManager2.añadirEmpleado(programmer3);
        projectManager2.añadirEmpleado(programmer4);

        programmer.añadirEmpleado(programmer2);

        programmer2.programar();
        projectManager.cordinaProyectos();
        manager.cordinaProyectos();

        manager.mostrarEmpleados();
        projectManager.mostrarEmpleados();
        programmer.mostrarEmpleados();
    }
}

class Animal{
    String nombre;

    Animal(String nombre){
        this.nombre = nombre;
    }

    void sonido(){
    }
}

class Perro extends Animal{

    Perro(String nombre) {
        super(nombre);
    }

    void sonido(){
        System.out.println("Guau");
    }
}

class Gato extends Animal{
    Gato(String nombre){
        super(nombre);
    }

    void sonido(){
        System.out.println("Miau");
    }
}


// Extra
class Empleado{
    String nombre;
    int id;
    Empleado[] empleados;
    int cantidadEmpleados= 0;

    Empleado(String nombre, int id){
        this.nombre = nombre;
        this.id = id;
        this.empleados = new Empleado[5];
        this.cantidadEmpleados = 0;
    }

    void añadirEmpleado( Empleado empleado){
        this.empleados[cantidadEmpleados] = empleado;
        cantidadEmpleados++;
    }

    void mostrarEmpleados(){
        System.out.println("Empleados de " + nombre);
        for(int i = 0; i < cantidadEmpleados; i++){
            System.out.println(empleados[i].nombre);
        }
    }
}

class Manager extends Empleado{
    Manager(String nombre, int id){
        super(nombre, id);
    }

    void cordinaProyectos(){
        System.out.println(nombre + " Cordina los proyectos");
    }

}

class ProjectManager extends Empleado{
    String proyecto;
    ProjectManager(String nombre, int id, String proyecto){
        super(nombre, id);
        this.proyecto = proyecto;
    }

    void cordinaProyectos(){
        System.out.println(nombre + " Cordina su proyecto");
    }
}

class Programmer extends Empleado{
    String lenguaje;
    Programmer(String nombre, int id, String lenguaje){
        super(nombre, id);
        this.lenguaje = lenguaje;
    }
    void programar(){
        System.out.println(nombre + " Esta programando en: " + this.lenguaje);
    }

    @Override
    void añadirEmpleado(Empleado empleado) {
        System.out.println(nombre + " No tiene empleados a su cargo, " + empleado.nombre+ " No se añadira");
    }

    @Override
    void mostrarEmpleados() {
        System.out.println(nombre + " No tiene empleados a su cargo");
    }
}


