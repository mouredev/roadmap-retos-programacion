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

        Employee emp1 = new Employee(1002, "Simon");
        Employee emp2 = new Employee(1003, "John");
        Employee emp3 = new Employee(1004, "Jane");

        // Agregar empleados a la lista
        emp1.agregarEmpleado(emp2);
        emp1.agregarEmpleado(emp3);

        // Listar los empleados
        emp1.listarEmpleados();

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
        private int id;
        private String name;
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

    static class Manager{

    }

    static class ProjectManager{

    }

    static class programmer{

    }

}

