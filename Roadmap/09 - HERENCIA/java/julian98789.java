package MauroDevRetos;

import java.util.ArrayList;
import java.util.List;

public class reto_9_Animal {

     

     public void sonido( ){

        System.out.println("el sonido de tu animal es ");


     }

}

class perro extends reto_9_Animal{


    @Override
    public void sonido( ){

        System.out.println("el sonido de tu animal es guau");

     }
    
    
}

class gato extends reto_9_Animal{

    
    @Override
    public void sonido( ){

        System.out.println("el sonido de tu animal es miau");

     }

}

class Empleado {
    private int id;
    private String nombre;

    // Constructor
    public Empleado(int id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

  
    public int getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

   
    public void mostrarInfo() {
        System.out.println("ID: " + id + ", Nombre: " + nombre);
    }
}

class Gerente extends Empleado {
    private List<Empleado> empleadosACargo;

    // Constructor
    public Gerente(int id, String nombre) {
        super(id, nombre);
        this.empleadosACargo = new ArrayList<>();
    }

    public void agregarEmpleado(Empleado empleado) {
        empleadosACargo.add(empleado);
    }

  
    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Empleados a cargo:");
        for (Empleado e : empleadosACargo) {
            System.out.println("\t- " + e.getNombre());
        }
    }
}

class GerenteDeProyecto extends Gerente {
    private String proyecto;

    public GerenteDeProyecto(int id, String nombre, String proyecto) {
        super(id, nombre);
        this.proyecto = proyecto;
    }

    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Proyecto: " + proyecto);
    }
}


class Programador extends Empleado {
    private String lenguajePrincipal;


    public Programador(int id, String nombre, String lenguajePrincipal) {
        super(id, nombre);
        this.lenguajePrincipal = lenguajePrincipal;
    }
    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Lenguaje Principal: " + lenguajePrincipal);
    }
}

class principal {

    public static void mostrarSonido(reto_9_Animal animal){
        animal.sonido();
    }

   




    public static void main(String[] args) {

        perro perro = new perro();
        gato gato = new gato();

        mostrarSonido(gato);
        mostrarSonido(perro);
        
        Programador prog1 = new Programador(1, "Ana", "Java");
        Programador prog2 = new Programador(2, "Luis", "Python");

    
        GerenteDeProyecto gerenteProy = new GerenteDeProyecto(3, "Marta", "Proyecto X");
        gerenteProy.agregarEmpleado(prog1);
        gerenteProy.agregarEmpleado(prog2);

  
        Gerente gerenteGen = new Gerente(4, "Carlos");
        gerenteGen.agregarEmpleado(gerenteProy);

 
        prog1.mostrarInfo();
        System.out.println();
        prog2.mostrarInfo();
        System.out.println();
        gerenteProy.mostrarInfo();
        System.out.println();
        gerenteGen.mostrarInfo();
    }

}
