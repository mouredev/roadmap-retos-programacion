import java.util.ArrayList;
import java.util.List;

public class danhingar {

    public static void main(String[] args) {
        Animal dog = new Dog("Pastor Alemán");
        Animal cat = new Cat("Gato persa");
        Cat cat1 = new Cat("Gato siamés");
        Dog dog1 = new Dog("Bulldog");
        Animal animal = new Animal("Pez");
        sound(dog);
        sound(cat);
        sound(dog1);
        sound(cat1);
        sound(animal);

        Manager myManager = new Manager(1, "Daniel");
        ProjectManager myProjectManager = new ProjectManager(2, "Juan", "Proyecto 1");
        ProjectManager myProjectManager2 = new ProjectManager(3, "Pepe", "Proyecto 2");
        Programmer myProgrammer = new Programmer(4, "Luis", "Java");
        Programmer myProgrammer2 = new Programmer(5, "Marcos", "Python");
        Programmer myProgrammer3 = new Programmer(6, "Pablo", "Dart");
        Programmer myProgrammer4 = new Programmer(7, "Rubén", "Typescript");

        myManager.add(myManager, List.of(myProjectManager,myProjectManager2));
        myProjectManager.add(myProjectManager, List.of(myProgrammer,myProgrammer2));
        myProjectManager2.add(myProjectManager2, List.of(myProgrammer3,myProgrammer4));

        myProgrammer.add(myProgrammer, myProgrammer2);
        myProgrammer3.code();

        myProjectManager.coordinateProject();

        myManager.coordinateProject();
        myManager.printEmployees();

        myProjectManager.printEmployees();
        myProjectManager2.printEmployees();

    }

    public static class Animal {
        private String name;

        public Animal(String name) {
            this.name = name;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public void sound() {
            System.out.println("Sonido genérico");
        }
    }

    public static class Dog extends Animal {

        public Dog(String name) {
            super(name);
        }

        public void sound() {
            System.out.println("Guau!");
        }

    }

    public static class Cat extends Animal {

        public Cat(String name) {
            super(name);
        }

        public void sound() {
            System.out.println("Miau!");
        }

    }

    public static void sound(Animal animal) {
        animal.sound();
    }

    // EXTRA
    public static class Employee {
        private Integer id;
        private String name;
        private List<Employee> employees = new ArrayList<>();

        public Employee(Integer id, String name) {
            this.id = id;
            this.name = name;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public Integer getId() {
            return id;
        }

        public void setId(Integer id) {
            this.id = id;
        }

        public List<Employee> getEmployees() {
            return employees;
        }

        public void setEmployees(List<Employee> employees) {
            this.employees = employees;
        }

        public void add(Employee employee, List<Employee> employees) {
            employee.employees.addAll(employees);
        }

        public void printEmployees(){
            for (Employee employee : employees) {
                System.out.println(employee.name);
            }
        }

    }

    public static class Programmer extends Employee {

        private String language;

        public Programmer(Integer id, String name,String language) {
            super(id, name);
            this.language = language;
        }

        public String getLanguage() {
            return language;
        }

        public void setLanguage(String language) {
            this.language = language;
        }

        public void add(Employee e,Employee e2){
            System.out.println("Un programador no tiene empleados a su cargo. "+e2.getName()+" no se añadirá.");
        }

        public void code(){
            System.out.println(this.getName()+" está programando en "+this.getLanguage());
        }

    }

    public static class Manager extends Employee {

        public Manager(Integer id, String name) {
            super(id, name);
        }

        public void coordinateProject(){
            System.out.println(this.getName()+" coordina todos los proyectos.");
        }

    }

    public static class ProjectManager extends Employee {

        private String project;

        public ProjectManager(Integer id, String name,String project) {
            super(id, name);
            this.project = project;
        }

        public void coordinateProject(){
            System.out.println(this.getName()+" está coordinando su proyecto "+this.project+".");
        }

        public String getProject() {
            return project;
        }

        public void setProject(String project) {
            this.project = project;
        }

        

    }
}
