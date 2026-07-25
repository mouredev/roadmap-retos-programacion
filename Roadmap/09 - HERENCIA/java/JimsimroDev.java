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

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class JimsimroDev {

  public static void main(String[] args) {
    var perro = new Perro("max");
    perro.sonido();

    var gato = new Gato("garfield");
    System.out.println(gato.getNombre());
    gato.sonido();

    // Puedo crear un arreglo pero como el arreglo solo acepta datos del mismo tipo
    // uso la clase Padre JimsimroDev
    Animal animales[] = new Animal[4]; // Aquie le digo que puedo guardar 4 animales
    // Ahora asigno valor a cada posicoin del arreglo
    animales[0] = perro;
    animales[1] = gato;
    animales[2] = new Perro("Dante");
    animales[3] = new Perro("Gilver");
    System.out.println(animales[2].toString());
    // Lo puedo recorre con un for o usando Arrays.toString() para mostrarlos
    for (int a = 0; a < animales.length; a++) {
      System.out.println(animales[a].toString());
    }
    System.out.println(Arrays.toString(animales));

    System.out.println("::::::::::EXTRA::::::::::::::");
    // EXTRA
    var gerente = new Gerente(1L, "Jhoan");

    var gerenteDeProyectos = new GerenteProyecto(2L, "Isabel", "Proyecto 1");
    var gerenteDeProyectos1 = new GerenteProyecto(3L, "Keren", "Proyecto 2");

    var desarrollador = new Programador(4L, "Jesus", "PHP");
    var desarrollador1 = new Programador(5L, "Jarvis", "Ruby");
    var desarrollador2 = new Programador(6L, "Carmen", "perl");
    var desarrollador3 = new Programador(7L, "Jimmis", "Java");

    System.out.println("::::::::::EXTRA::::::::::::::");
    System.out.println("::::::::::GERENTE::::::::::::");
    gerente.agregarEmpleado(gerenteDeProyectos);
    gerente.agregarEmpleado(gerenteDeProyectos1);
    gerente.coordinarImplementacion();
    gerente.mostrarNombreYPuesto();
    gerente.print();

    System.out.println("::::::::::GERENTE DE PROYECTOS::::::::::::::");
    gerenteDeProyectos.agregarEmpleado(desarrollador);
    gerenteDeProyectos.agregarEmpleado(desarrollador1);
    gerenteDeProyectos.agregarEmpleado(desarrollador2);
    gerenteDeProyectos.agregarEmpleado(desarrollador3);
    gerenteDeProyectos.mostrarNombreYPuesto();
    gerenteDeProyectos.coordinarImplementacion();
    gerenteDeProyectos.print();

    System.out.println("::::::::::DESARROLLADOR::::::::::::::");
    desarrollador.mostrarNombreYPuesto();
    desarrollador.agregarEmpleado(desarrollador3);
    desarrollador.print();
  }
}

class Animal {
  private String nombre;

  public String getNombre() {
    return this.nombre;

  }

  public Animal(String nombre) {
    this.nombre = nombre;
  }

  public Animal() {
  }

  public void sonido() {
    System.out.println("Soindio generico");
  }

}

class Perro extends Animal {

  public Perro(String nombre) {
    super(nombre);
  }

  // Para sobrescribir el metodo en tiempo de ejecucion en java se usa la
  // anotacion @Overrideo
  @Override
  public void sonido() {
    System.out.println("El perro ladra: ┬íGuau!");
  }

  @Override
  public String toString() {
    return "Nombre: " + getNombre();
  }

}

class Gato extends Animal {

  public Gato(String nombre) {
    super(nombre);
  }

  @Override
  public void sonido() {
    System.out.println("El gato maulla: Miau!");
  }

  @Override
  public String toString() {
    return "Nombre: " + getNombre();
  }
}

// Extra
class Empleado {
  private Long id;
  private String puesto;
  private String nombre;
  private List<Empleado> empleadosACargo;

  public Empleado() {

  }

  public Empleado(Long id, String puesto, String nombre) {
    this.id = id;
    this.puesto = puesto;
    this.nombre = nombre;
    this.empleadosACargo = new ArrayList<>();
  }

  public void agregarEmpleado(Empleado empleado) {
    if (this instanceof Gerente || this instanceof GerenteProyecto) {
      empleadosACargo.add(empleado);
    } else {
      System.out.println("Solo gerente y gerente de Proyectos pueden tener empleados a cargo");
    }
  }

  public void print() {
    System.out.println("Empleados a cargo");
    for (Empleado empleado : empleadosACargo) {
      System.out.print(empleado.getNombre());
      System.out.print(",");
    }
    System.out.println();
  }

  public void mostrarNombreYPuesto() {
    System.out.println(getPuesto() + getNombre());
  }

  public Long getId() {
    return this.id;
  }

  public String getNombre() {
    return this.nombre;
  }

  public void setNombre(String nombre) {
    this.nombre = nombre;
  }

  public List<Empleado> getEmpleadosACargo() {
    return this.empleadosACargo;
  }

  public String getPuesto() {
    return puesto;
  }
}

class Gerente extends Empleado {

  public Gerente() {

  }

  public Gerente(Long id, String nombre) {
    super(id, " Gerente ", nombre);
  }

  public void coordinarImplementacion() {
    System.out.printf("%s Coordinando la Implementación de los proyecto informatico\n", getNombre());
  }
}

class Programador extends Empleado {
  private String lenguaje;

  public Programador(Long id, String nombre, String lenguaje) {
    super(id, " Programador ", nombre);
    this.lenguaje = lenguaje;
  }

  public void codeando() {
    System.out.printf("%s Esta Desrrollando en el %s\n ", getNombre(), lenguaje);
  }

  public String getlenguaje() {
    return lenguaje;
  }

  public void setlenguaje(String lenguaje) {
    this.lenguaje = lenguaje;
  }
}

class GerenteProyecto extends Empleado {
  private String proyecto;

  public GerenteProyecto(Long id, String nombre, String proyecto) {
    super(id, " Gerente de Proyectos ", nombre);
    this.proyecto = proyecto;
  }

  public void coordinarImplementacion() {
    System.out.printf("%s Coordinando la Implementación su proyecto informatico\n", getNombre());
  }

  public String getProyecto() {
    return this.proyecto;
  }

  public void setProyecto(String proyecto) {
    this.proyecto = proyecto;
  }
}
