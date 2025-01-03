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
 * 
 * @version v1.0
 * 
 * @since 09/09/2024
 * 
 * @author GlossyPath
 */

 import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class GlossyPath {
    public static void main(String[] args) throws Exception {

        Gato cat = new Gato();
        Perro dog = new Perro();

        cat.sonidoAnimal();
        dog.sonidoAnimal();
        
        System.out.println();

        Gerentes gerentePaco = new Gerentes("Paco", "Gerente");

        GerentesProyecto gerenteProyectoAna = new GerentesProyecto("Ana", "Gerente de proyecto");

        gerenteProyectoAna.setProyecto("Valerian");

        GerentesProyecto.Programador claraProgramadora = gerenteProyectoAna.new Programador("Clara", "Programador", gerenteProyectoAna);

        gerentePaco.añadirGerentesProyecto(gerenteProyectoAna);
        
        gerenteProyectoAna.añadirProgramador(claraProgramadora);
        System.out.println();

        System.out.println(gerentePaco);
        System.out.println();

        System.out.println(gerenteProyectoAna);
        System.out.println();

        System.out.println(claraProgramadora);

    }
}

 abstract class Animal {

    public abstract void sonidoAnimal();
}


class Perro extends  Animal {

    @Override
    public void sonidoAnimal() {
        System.out.println("El perro hace GUAU");
    }
}


class Gato extends Animal {

    @Override
    public void sonidoAnimal() {
        System.out.println("El gato hace MIAUUU");
    }  
}


abstract class Empleados {

    private String identificador;
    private String nombre;
    private String puesto;

    public Empleados (String nombre, String categoria){
        this.nombre = nombre;
        this.puesto = categoriaTrabajador(categoria);
        this.identificador = indentificadorAleatorio();
    }

    private String categoriaTrabajador(String categoria) throws IllegalArgumentException {

        String[] categorias = {"gerente", "gerente de proyecto", "programador"};

        boolean correcto = Arrays.stream(categorias).anyMatch(c -> c.equalsIgnoreCase(categoria));

        if(correcto) {
            return categoria;

        } else {
            throw new IllegalArgumentException ("Categoria no valida");
        }
    }


    private String indentificadorAleatorio () {

        StringBuilder id = new StringBuilder();
        char[] letras = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'};

        for(int i=0; i<5; i++){
            String numsAle = String.valueOf((int) (Math.random()*10));
            id.append(numsAle);
        }

        for(int i=0; i<5; i++){
            int indice  = (int) (Math.random()*letras.length);
            id.append(letras[indice]);
        }

        return id.toString();
    }

    public String getPuesto(){
        return this.puesto;
    }

    public String getIdentificador() {
        return identificador;
    }

    public void setIdentificador(String identificador) {
        this.identificador = identificador;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {

        return "Empleado: " + getNombre() + "\n" +
        "Puesto de trabajo: " + getPuesto() + "\n" +
        "Identificador: " + getIdentificador();
    }
}



class Gerentes extends Empleados {

    private List<GerentesProyecto> gerentesProyecto;

    private final Scanner SC = new Scanner("System.in");

    public Gerentes(String nombre, String categoria) {
        super(nombre, categoria);

        this.gerentesProyecto = new ArrayList<>();
    }

    public void añadirGerentesProyecto(GerentesProyecto gerenteAñadir) {

      boolean existe = gerentesProyecto.stream().anyMatch(gp -> gp.getNombre().equals(gerenteAñadir.getNombre()));
       
      if(!existe){
        gerentesProyecto.add(gerenteAñadir);
        System.out.println("El gerente de proyecto " + gerenteAñadir.getNombre() + " ha sido añadido correctamente.");

      } else {
        System.out.println("El gerente de proyectos ya esta en la lista");
        }
    }

    public void despedirGerenteProyecto() {

        gerentesProyecto.stream().forEach(System.out::println);

        System.out.println("Introduce el nombre del gerente de proyecto que quieres despedir");
        String nombre = SC.nextLine();

        boolean existe = gerentesProyecto.stream().anyMatch(p -> p.getNombre().equals(nombre));

        if(existe) { 
            gerentesProyecto.removeIf(p -> p.getNombre().equals(nombre));
            System.out.println("El programador " + nombre + " ha sido despedido.");

        } else {
            System.out.println("Ese programador no existe");
        }
    }


    public List<GerentesProyecto> getGerentesProyecto() {
        return gerentesProyecto;
    }

    public void setGerentesProyecto(List<GerentesProyecto> gerentesProyecto) {
        this.gerentesProyecto = gerentesProyecto;
    }

    @Override
    public String toString(){
        return super.toString() +
        "\nGerentes de proyecto que gestiona: " + gerentesProyecto.size();
    }
}



class GerentesProyecto extends Empleados {

    private final Scanner SC = new Scanner(System.in);
    String proyecto;
    private List<Programador> programadores;

    public GerentesProyecto(String nombre, String categoria) {
        super(nombre, categoria);

        this.programadores = new ArrayList<>();
    }


    public void añadirProgramador(Programador programador){

        boolean existe = programadores.stream().anyMatch(p -> p.getNombre().equals(programador.getNombre()));

        if(!existe) {
            this.programadores.add(programador);

        } else {
            System.out.println("El nombre del programador ya existe");
        }
    }

    public void despedirProgramador() {

        programadores.stream().forEach(System.out::println);

        System.out.println("Introduce el nombre del programador que quieres despedir");
        String nombre = SC.nextLine();

        boolean existe = programadores.stream().anyMatch(p -> p.getNombre().equals(nombre));

        if(existe) { 
            programadores.removeIf(p -> p.getNombre().equals(nombre));
            System.out.println("El programador " + nombre + " ha sido despedido.");


        } else {
            System.out.println("Ese programador no existe");
        }
    }


    public List<Programador> getProgramadores() {
        return programadores;
    }


    public void setProgramadores(List<Programador> programadores) {
        this.programadores = programadores;
    }


    public String getProyecto() {
        return proyecto;
    }


    public void setProyecto(String proyecto) {
        this.proyecto = proyecto;
    }

    @Override
    public String toString(){
        return super.toString() +
        "\nProgramadores que gestiona: " + programadores.size() +
        "\nProyecto en el que esta involucrado: " + proyecto;
    }

    class Programador extends Empleados {

        GerentesProyecto gerenteJefe;

        public Programador(String nombre, String puesto, GerentesProyecto gerenteProyecto) {
            super(nombre, puesto);

            this.gerenteJefe = gerenteProyecto;

        }

        @Override
        public String toString() {
            return super.toString() +
            "\nSu jefe es: " + gerenteJefe.getNombre();
        }
    
    }

}



