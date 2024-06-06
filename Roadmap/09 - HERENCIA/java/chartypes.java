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

public class chartypes {

  public static void main(String[] args) {
    // Exercise
    Dog dog1 = new Dog("My dog1");
    dog1.sound();
    Cat cat1 = new Cat("my cat1");
    cat1.sound();
    Animal cat2 = new Cat("my cat2");
    cat2.sound();
    System.out.println(cat1);

    // Extra
    System.out.println("/////////////////// Extra ////////////////////");
    Manager myManager1 = new Manager("robert", "12");
    ProjectManager myProjManager1 = new ProjectManager("Gonzalo", "234");
    Programmer myProgrammer1 = new Programmer("Coby", "12312234");
    myManager1.checkEmployee("Coby");
    myProjManager1.checkProject();
    myProgrammer1.createProgram();

  }

}

// Exercise
class Animal {
  private String name;

  public Animal(String name) {
    this.name = name;
  }

  public void sound() {
    System.out.println("");
  }
  @Override
  public String toString() {
    return this.name;
  }
}

class Dog extends Animal {
  public Dog(String name){
    super(name);
  }
  
  @Override
  public void sound() {
    System.out.println("Guauuuuuu");
  }
}

class Cat extends Animal {
  public Cat(String name){
    super(name);
  }
  @Override
  public void sound() {
    System.out.println("Miauuu");
  }
}
/////////////////////////////////////////
//
//Extra

class Employee{
  String name;
  String id;

  public Employee(String name, String id){
    this.name = name;
    this.id = id;
  }

  @Override
  public String toString() {
    return this.name;
  }

}

class Manager extends Employee{

  public Manager(String name, String id){
    super(name,id);
  }

  public void checkEmployee(String name){
    System.out.println(this.name + " is checking everything is alright with " + name);
  }

}


class ProjectManager extends Employee{

  public ProjectManager(String name, String id){
    super(name,id);
  }

  public void checkProject(){
    System.out.println(this.name + " is checking a project right now...");
  }

}


class Programmer extends Employee{

  public Programmer(String name, String id){
    super(name,id);
  }

  public void createProgram(){
    System.out.println(this.name + " is coding to create a program... ");
  }

}


