public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog("Tobby");
        System.out.println(dog);
        dog.speak();

        Cat cat = new Cat("Dora");
        System.out.println(cat);
        cat.speak();

        System.out.println("\n------ DIFICULTAD EXTRA ---------\n");

        Manager manager = new Manager(0,"Moure");
        ProjectManager projectManager1 = new ProjectManager(1, "Luis", "09");
        ProjectManager projectManager2 = new ProjectManager(2, "Carlos", "08");
        Programmer programmer1 = new Programmer(3,"Abel","Java");
        Programmer programmer2 = new Programmer(4,"María","PHP");
        Programmer programmer3 = new Programmer(5,"Cecília","JavaScript");
        Programmer programmer4 = new Programmer(6,"Julián","Kotlin");

        manager.addEmployee(projectManager1);
        manager.addEmployee(projectManager2);
        manager.printEmployees();

        projectManager1.addEmployee(programmer1);
        projectManager1.addEmployee(programmer2);
        projectManager1.printEmployees();

        projectManager2.addEmployee(programmer3);
        projectManager2.addEmployee(programmer4);
        projectManager2.printEmployees();

        programmer1.addEmployee(programmer2);
        programmer1.printEmployees();

        programmer2.code();
    }
}

class Animal{
    //Atributos
    String name;
    String sound;

    //Geters y Seters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSound() {
        return sound;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }

    //Constructor
    public Animal(String name) {
        this.name = name;
    }

    //Método para hablar
    public void speak(){
        System.out.println(sound);
    }

    @Override
    public String toString() {
        return getClass().getName() + ": " + name;
    }
}

class Dog extends Animal{
    public Dog(String name) {
        super(name);
        this.sound = "Guau!";
    }
}

class Cat extends Animal{
    public Cat(String name) {
        super(name);
        this.sound = "Miau!";
    }
}

class Employee{
    int id;
    String name;
    ArrayList<Employee> employees;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<Employee> getEmployees() {
        return employees;
    }

    public void setEmployees(ArrayList<Employee> employees) {
        this.employees = employees;
    }

    public Employee(int id, String name) {
        this.id = id;
        this.name = name;
        this.employees = new ArrayList<>();
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }

    public void printEmployees() {
        System.out.print("Trabajadores a cargo de " + name + ":");
        for (Employee employee : employees) {
            System.out.print(" - " + employee.getName());
        }
        System.out.println();
    }
}

class Manager extends Employee{
    public Manager(int id, String name) {
        super(id, name);
    }

    public void coordinate(){
        System.out.println(name + " está coordinando los proyectos.");
    }
}

class ProjectManager extends Employee{
    String project;

    public ProjectManager(int id, String name, String project) {
        super(id, name);
        this.project = project;
    }

    public void coordinate(){
        System.out.println(name + " está coordinando el proyecto " + project);
    }
}

class Programmer extends Employee{
    String language;

    public Programmer(int id, String name, String language) {
        super(id, name);
        this.language = language;
    }

    public void code(){
        System.out.println(name + " está programando un proyecto en " + language);
    }

    @Override
    public void addEmployee(Employee employee) {
        System.out.println("No puede tener empleados a su cargo.");
    }
}
