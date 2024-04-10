package _09_Herencia;
import java.util.Stack;
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
public class _09_Herencia {

    public static void main (String[] args){
        Perro Animal1 = new Perro ("Kinder","Ladrando");
        Gato Animal2 = new Gato("Manchita","Maullando");
        System.out.println(Animal1.ladrar());
        System.out.println(Animal2.maullar());
        //Dificultad EXTRA
        Programador programador1 = new Programador(1,"Alexdevrep",null);
        System.out.println(programador1.desarrollar());
        Stack<String> personas = new Stack<>();
        personas.push("Alexdevrep"); //Añdimos personas a cargo del gerente
        Gerente_Proyecto gerenteProyecto1 = new Gerente_Proyecto(2,"Brais",personas);
        System.out.println(gerenteProyecto1.supervisar());
        Stack<String> personas2 = new Stack<>();
        personas2.push("Brais");
        Gerente gerente1 =new Gerente(3,"MoureDev",personas2);
        System.out.println(gerente1.dirigir());
    }
}

class Animal{ //Inicializamos la clase principal
    public String Nombre;

    public Animal (String Nombre){ //Este es el constructor de la clase principal
        this.Nombre=Nombre;
    }
}

class Perro extends Animal{ //Así se heredan las clases

    private String sonido;
    public Perro(String Nombre,String sonido) { //Constructor de la subclase
        super(Nombre);
        this.sonido=sonido;
    }
    public String ladrar(){ //Método de l clase
        return ("El perro con nombre "+ this.Nombre+" está "+ this.sonido);
    }
}

class Gato extends Animal{
    private String sonido;
    public Gato(String Nombre,String sonido){
        super(Nombre);
        this.sonido=sonido;
    }
    public String maullar(){
        return("El Gato con nombre "+ this.Nombre+" está "+ this.sonido);
    }
}

//Dificultad EXTRA

class Empleado{
    public int id;
    public String Nombre;
    public Stack<String> personas;


    public Empleado(int id,String Nombre,Stack<String> personas){
        this.id= id;
        this.Nombre=Nombre;
        this.personas=(personas !=null)? personas : new Stack<>();

    }
}

class Programador extends Empleado{
    public Programador(int id,String Nombre,Stack<String> personas){
        super(id,Nombre,personas);
    }
    public String desarrollar(){
        return ("La persona "+this.Nombre+" con ID "+this.id+" está desarrollando una aplicación y lleva a cargo a "
        + this.personas.size()+ " personas");
    }
}

class Gerente_Proyecto extends Empleado{
    public Gerente_Proyecto(int id,String Nombre,Stack<String> personas){
        super(id,Nombre,personas);
    }
    public String supervisar(){
        return ("La persona "+this.Nombre+" con ID "+this.id+" está comprobando que no hay bugs y lleva a cargo a "
                + this.personas.size()+ " personas");
    }
}

class Gerente extends Empleado{
    public Gerente(int id,String Nombre,Stack<String> personas){
        super(id,Nombre,personas);
    }
    public String dirigir(){
        return ("La persona "+this.Nombre+" con ID "+this.id+" está decidiendo  que nueva característica " +
                "añadir y lleva a cargo a " + this.personas.size()+ " personas");
    }
}


