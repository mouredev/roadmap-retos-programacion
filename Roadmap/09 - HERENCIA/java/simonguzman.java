import java.util.List;
import java.util.ArrayList;
public class simonguzman {
    public static void main(String[] args) {
        Dog dog1 = new Dog("Ares", "Lobo siberiano");
        Cat cat1 = new Cat("Katy", "Carey");

        
        System.out.println("Nombre: "+ dog1.getName() + " Raza: "+dog1.getRaza());
        dog1.hacerSonido();
        System.out.println("Nombre: "+ cat1.getName() + " Raza: "+cat1.getRaza());
        cat1.hacerSonido();

        // Crear instancias de Manager, ProjectManager y Programmer
        Manager manager1 = new Manager(1001, "Alice", "TechCorp");
        ProjectManager pm1 = new ProjectManager(1002, "Bob", "Project X");
        Programmer programmer1 = new Programmer(1003, "Charlie", "Java");
        Programmer programmer2 = new Programmer(1004, "Diana", "Python");

        // Agregar empleados al manager
        manager1.agregarEmpleado(pm1);
        manager1.agregarEmpleado(programmer1);
        manager1.agregarEmpleado(programmer2);

        // Listar empleados bajo el manager
        System.out.println("Empleados a cargo de " + manager1.name + ":");
        manager1.listarEmpleados();

        // Probar métodos específicos de cada clase
        manager1.coordManager();
        pm1.coordProjManager();
        programmer1.programmerProyect();
        programmer2.programmerProyect();
    }

    static class Animal{
        private String name;
        private String raza;
    
        public Animal(){
    
        }
    
        public Animal(String name, String raza){
            this.name = name;
            this.raza = raza;  
        }
    
        public void hacerSonido(){
            
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getRaza() {
            return raza;
        }

        public void setRaza(String raza) {
            this.raza = raza;
        }
    }
    
     static class Dog extends Animal{
    
        public Dog(){
    
        }
    
        public Dog(String name, String raza){
            super(name, raza);
        }
    
        @Override
        public void hacerSonido() {
            System.out.println("Guau");
        }
        
    }
    
    static class Cat extends Animal{
    
        public Cat(){
    
        }
    
        public Cat(String name, String raza){
            super(name, raza);
        }
    
        @Override
        public void hacerSonido() {
            System.out.println("Miau");
        } 
    }

    static class Employee{
        protected int id;
        protected String name;
        List<Employee> employees; 

        public Employee(){

        }

        public Employee(int id, String name){
            this.id = id;
            this.name = name;
            this.employees = new ArrayList<>();
        }

        public void agregarEmpleado(Employee employee){
            this.employees.add(employee);
        }

        public void listarEmpleados() {
            if (!this.employees.isEmpty()) {
                for (Employee emp : employees) {
                    System.out.println("ID: "+emp.id+" Nombre: "+emp.name);
                }
            } else {
                System.out.println("No hay empleados");
            }
        }
    }

    static class Manager extends Employee{

        private String nameEnterprise;

        public Manager(){

        }        

        public Manager(int id, String name, String nameEnterprise){
            super(id, name);
            this.nameEnterprise = nameEnterprise;
        }

        public void coordManager(){
            System.out.println("El gerente " +this.name + " esta a cargo de los proyectos de la empresa "+this.nameEnterprise);
        }

    }

    static class ProjectManager extends Employee{

        private String proyName;

        public ProjectManager(){

        }

        public ProjectManager(int id, String name, String proyName){
            super(id, name);
            this.proyName = proyName;
        }

        public void coordProjManager(){
            System.out.println("El gerente de proyecto "+this.name+" dirije al proyecto "+this.proyName);
        }
    }

    static class Programmer extends Employee{

        private String languaje;

        public Programmer(){

        }

        public Programmer(int id, String name, String languaje){
            super(id, name);
            this.languaje = languaje;
        }

        public void programmerProyect(){
            System.out.println("El programador de proyecto "+this.name+ " programa en lenguaje "+this.languaje);
        }

    }

}

