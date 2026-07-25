import java.util.ArrayList;
import java.util.List;

public class Josegs95 {
    public static void main(String[] args) {
        //Herencia
        Animal animal = new Animal(null);
        Perro dog = new Perro();
        Gato cat = new Gato();

        animal.makeSound(); //Out: null
        dog.makeSound(); //Out: Guau
        cat.makeSound(); //Out: Miau

        //Reto
        System.out.println("\n");
        retoFinal();
    }

    public static class Animal{

        private String sound;

        public Animal(String sound){
            this.sound = sound;
        }

        public void makeSound(){
            System.out.println(sound);
        }

    }

    public static class Perro extends Animal{

        public Perro(){
            super("Guau");
        }
    }

    public static class Gato extends Animal{

        public Gato(){
            super("Miau");
        }
    }

    public static void retoFinal(){
        Manager manager = new Manager("1154257", "Jose");
        ProyectManager pm1 = new ProyectManager("9822361", "Rocío");
        ProyectManager pm2 = new ProyectManager("5418742", "Guillermo");
        Programmer p1 = new Programmer("7739682", "Lucía", "Java");
        Programmer p2 = new Programmer("3125055", "Nuria", "Python");
        Programmer p3 = new Programmer("4060533", "Isidoro", "C#");

        manager.addEmployee(pm1);
        manager.addEmployee(pm2);
        pm1.addEmployee(p1);
        pm1.addEmployee(p2);
        pm2.addEmployee(p3);

        p1.addEmployee(manager);
        p1.programme();

        pm2.addEmployee(manager);
        pm2.manageProyect();

        manager.manageCompany();

        System.out.print("Empleados a cargo de " + manager.getName() + ": ");
        manager.printEmployeeList();
        System.out.println();

        System.out.print("Empleados a cargo de " + pm1.getName() + ": ");
        pm1.printEmployeeList();
        System.out.println();

        System.out.print("Empleados a cargo de " + pm2.getName() + ": ");
        pm2.printEmployeeList();
        System.out.println();
    }

    public static class Employee {
        private final String ID;
        private String name;
        private List<Employee> employeeList;

        public Employee(String id, String name){
            this.ID = id;
            this.name = name;
            employeeList = new ArrayList<>();
        }

        public void addEmployee(Employee e){
            employeeList.add(e);
        }

        public void printEmployeeList(){
            for (Employee e : employeeList){
                e.printEmployeeList();
                System.out.print(e + " ");
            }
        }

        public String getID() {
            return ID;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        @Override
        public String toString() {
            return "[" + name + ":" + ID + "]";
        }
    }

    public static class Manager extends Employee{

        public Manager(String id, String name){
            super(id, name);
        }

        public void manageCompany(){
            System.out.println(getName() + " is managing the company...");
        }
    }

    public static class ProyectManager extends Employee{

        public ProyectManager(String id, String name){
            super(id, name);
        }

        public void manageProyect(){
            System.out.println(getName() + " is managing their project...");
        }

        @Override
        public void addEmployee(Employee e){
            if (e instanceof Manager){
                System.out.println("The project manager can not have a manager in their charge");
                return;
            }

            super.addEmployee(e);
        }
    }

    public static class Programmer extends Employee{

        private String language;

        public Programmer(String id, String name, String language){
            super(id, name);
            this.language = language;
        }

        public void programme(){
            System.out.println(getName() + " is programming with " + language);
        }

        @Override
        public void addEmployee(Employee e) {
            System.out.println("The programmer can not have employees in their charge");
        }
    }
}
