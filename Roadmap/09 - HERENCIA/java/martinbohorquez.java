/**
 * #09 HERENCIA Y POLIMORFISMO
 *
 * @author martinbohorquez
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class martinbohorquez {

    public static void main(String[] args) {
        Animal perro = new Perro("Punky");
        printSound(perro);
        Animal gato = new Gato("Smoking");
        printSound(gato);
        /*
         *  DIFICULTAD EXTRA
         */
        Manager manager = new Manager(1, "MartinDev");
        ProjectManager projectManager1 = new ProjectManager(2, "Robert",
                Arrays.asList("Project 1", "Project 2", "Project 3"));
        ProjectManager projectManager2 = new ProjectManager(3, "Kathie",
                Arrays.asList("Project 11", "Project 12"));
        Programmer programmer1 = new Programmer(4, "Mark",
                Arrays.asList("Java", "Typescript"));
        Programmer programmer2 = new Programmer(5, "Tim",
                Arrays.asList("Python", "JavaScript"));
        Programmer programmer3 = new Programmer(6, "Linus",
                Arrays.asList("Java", "Python", "JavaScript"));
        Programmer programmer4 = new Programmer(7, "Moure",
                Arrays.asList("Python", "Typescript"));

        manager.coordinateProjects();
        manager.addEmployee(projectManager1);
        manager.addEmployee(projectManager2);
        manager.printEmployees();
        projectManager1.coordinateProject();
        projectManager1.addEmployee(programmer1);
        projectManager1.addEmployee(programmer3);
        projectManager1.printEmployees();
        programmer2.code();
        programmer3.addEmployee(programmer4);
        programmer2.printEmployees();
    }

    private static void printSound(Animal animal) {
        animal.sonido();
    }

    private static class Animal {
        protected String name;

        public Animal(String name) {
            this.name = name;
        }

        protected void sonido() {
            System.out.println("El animal emite un sonido!");
        }
    }

    private static class Perro extends Animal {

        public Perro(String name) {
            super(name);
        }

        @Override
        protected void sonido() {
            System.out.printf("El perro %s dice guau!%n", name);
        }
    }

    private static class Gato extends Animal {

        public Gato(String name) {
            super(name);
        }

        @Override
        protected void sonido() {
            System.out.printf("El gato %s dice miau!%n", name);
        }
    }

    private static class Employee {
        protected int id;
        protected String name;
        protected List<Employee> employees = new ArrayList<>();

        public Employee(int id, String name) {
            this.id = id;
            this.name = name;
        }

        protected void addEmployee(Employee employee) {
            employees.add(employee);
            System.out.printf("Se asigna empleado %s a cargo de %s%n", employee.name, name);
        }

        protected void printEmployees() {
            System.out.printf("Los empleados a cargo de %s:%n", name);
            employees.forEach(e -> System.out.println(e.name));
        }
    }

    private static class Manager extends Employee {

        public Manager(int id, String name) {
            super(id, name);
        }

        private void coordinateProjects() {
            System.out.printf("%s está coordinando todos los proyectos de la empresa%n", name);
        }
    }

    private static class ProjectManager extends Employee {
        private List<String> projects = new ArrayList<>();

        public ProjectManager(int id, String name, List<String> projects) {
            super(id, name);
            this.projects = new ArrayList<>(projects);
        }

        private void coordinateProject() {
            System.out.printf("%s está coordinando sus proyectos %s%n", name, projects.toString());
        }
    }

    private static class Programmer extends Employee {
        private List<String> languages = new ArrayList<>();

        public Programmer(int id, String name, List<String> languages) {
            super(id, name);
            this.languages = new ArrayList<>(languages);
        }

        @Override
        protected void addEmployee(Employee employee) {
            System.out.printf("Un programador no tiene empleados a su cargo. %s no se añadirá!%n", employee.name);
        }

        private void code() {
            System.out.printf("%s está programando en %s%n", name, languages.toString());
        }
    }
}
