import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Worlion {

    /*
    * EJERCICIO: Herencia
    */
    abstract class Animal {
        String name;
        String family;
        String sound;
        String icon;

        abstract String doSound();
    }

    class Dog extends Animal {
        String family = "Canidae";
        String sound = "guau";
        String icon = "🐶";

        public Dog(String name){
            this.name = name;
        }
        
        public String doSound() {
            StringBuilder s = new StringBuilder("Los perros ladran asi: ");
            s.append(this.sound);
            s.append(this.icon);
            s.append(", y este se llama "+this.name);

            return s.toString();
        }
    }

    class Cat extends Animal {
        String family = "Felidae";
        String sound = "miau";
        String icon = "🐱";

        public Cat(String name){
            this.name = name;
        }
        
        public String doSound() {
            StringBuilder s = new StringBuilder("Los gatos maullan asi: ");
            s.append(this.sound);
            s.append(this.icon);
            s.append(", y este se llama "+this.name);

            return s.toString();
        }
    }
    

    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run(){
        Animal perro = new Dog("Juanito");
        System.out.println(perro.doSound());

        Animal cat = new Cat("Botitas");
        System.out.println(cat.doSound());

        testEmployeesClasses();
    }

    /*
    * DIFICULTAD EXTRA (opcional): Employees
    */

    abstract class Employee {
        String id;
        String name;
        List<Employee> minionList = new ArrayList<>();
        public abstract String toString();
        private void addMinionEmployee(Employee e){
            this.minionList.add(e);
        }
        private List<Employee> getMinionEmployees(){
            return this.minionList;
        }
        protected String getId(String typeId, int counter){
            return typeId+ String.format("%03d", counter);
        }
    }

    class Manager extends Employee{
        static int idCount=0;
        
        public Manager(String name){
            this.id = getId("MNG_",++idCount);
            this.name = name;
        }

        public void addMinionEmployee(Employee employee) {
            this.minionList.add(employee);
        }


        public String toString(){
            StringBuilder sb = new StringBuilder("\nMANAGER: {");
            sb.append("\n\tId: "+this.id);
            sb.append("\n\tName: "+this.name);
            sb.append("\n\tEmployees in charge: "+this.minionList);

            sb.append("}");
            return sb.toString();
        }
    }
    class ProjectManager extends Employee{
        static int idCount=0;

        List<String> projects = new ArrayList<>();

        public ProjectManager(String name){
            this.id = getId("PM_",++idCount);
            this.name = name;
        }

        public void addProject(String project) {
            this.projects.add(project);
        }

        public void addMinionEmployee(Developer developer) {
            this.minionList.add(developer);
        }

        public String toString(){
            StringBuilder sb = new StringBuilder("\nPROJECT MANAGER: {");
            sb.append("\n\tId: "+this.id);
            sb.append("\n\tName: "+this.name);
            sb.append("\n\tProjects: "+this.projects);
            sb.append("\n\tIn charge developers: "+this.minionList);

            sb.append("}");
            return sb.toString();
        }
    }
    class Developer extends Employee{
        private static int idCount=0;
        private List<String> languages = new ArrayList<>();

        public Developer(String name){
            this.id = getId("DEV_",++idCount);
            this.name = name;
        }

        public Developer(String name, List<String> languages){
            this(name);
            this.languages = languages;
        }

        public void addLanguage(String language) {
            this.languages.add(language);
        }

        public String toString(){
            StringBuilder sb = new StringBuilder("\nDEVELOPER: {");
            sb.append("\n\tId: "+this.id);
            sb.append("\n\tName: "+this.name);
            sb.append("\n\tLanguages: "+this.languages);

            sb.append("}");
            return sb.toString();
        }
    }

    public void testEmployeesClasses() {
    
        System.out.println(" \n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");

        Developer kevin = new Developer("Kevin");
        kevin.addLanguage("Java");
        Developer stuart = new Developer("Stuart", Arrays.asList(new String[]{"PHP", "Lisp"}));
        Developer Jerry = new Developer("Jerry", Arrays.asList(new String[]{"Haskel", "Rust", "C#"}));

        ProjectManager oneil = new ProjectManager("O'Neil");
        oneil.addProject("proyecto caca");
        oneil.addProject("otro");
        
        oneil.addMinionEmployee(kevin);
        oneil.addMinionEmployee(stuart);

        ProjectManager ripley = new ProjectManager("Ripley");
        ripley.addProject("TOP SECRET");
        ripley.addMinionEmployee(Jerry);


        Manager theKing = new Manager("Jaffe Joffer");
        theKing.addMinionEmployee(oneil);
        theKing.addMinionEmployee(ripley);

        System.out.println(theKing.toString());

        //System.out.println(kevin);
        //System.out.println(stuart);
        //System.out.println(Jerry);

    }
}

