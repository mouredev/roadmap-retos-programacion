/* Clase principal */
public class Inheritance {

    public static void main(String[] args) {
        Animal dog = new Dog(1, "Lalo");
        dog.sound();
        Animal cat = new Cat(1, "Lalo");
        cat.sound();

        Programmer programmer1 = new Programmer(1, "Amador");
        programmer1.addLanguage("Java");
        programmer1.addLanguage("Go");
        programmer1.addLanguage("Python");

        Programmer programmer2 = new Programmer(2, "Rosa");
        programmer2.addLanguage("PHP");
        programmer2.addLanguage("C#");

        Programmer programmer3 = new Programmer(3, "Mario");
        programmer3.addLanguage("JavaScript");
        programmer3.addLanguage("HTML");
        programmer3.addLanguage("CSS");

        Project project1 = new Project("P001", "Desarrollo E-Commerce");
        project1.addToTeam(programmer1);
        project1.addToTeam(programmer3);

        ProjectManager projectManager1 = new ProjectManager(4, "Pedro");
        projectManager1.addProject(project1);
        projectManager1.listProjects();

        Manager manager = new Manager(5, "Maure Dev");
        manager.addProgramer(programmer1);
        manager.addProgramer(programmer2);
        manager.addProgramer(programmer3);

        manager.addProjectManager(projectManager1);

    }
}



/*==================CLASE ANIMAL======================*/
public class Animal {
    private int code;
    private String name;

    public Animal() {
    }

    public Animal(int code, String name) {
        this.code = code;
        this.name = name;
    }

    public void sound() {
        System.err.println("hace sonido");
    }

    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

}


/*==================CLASE CAT======================*/
public class Cat extends Animal {
    public Cat() {
    }

    public Cat(int code, String name) {
        super(code, name);
    }

    @Override
    public void sound() {
        System.err.println("El gato Hace Miau Miau");
    }
}



/*==================CLASE DOG======================*/
public class Dog extends Animal {
    public Dog() {
    }

    public Dog(int code, String name) {
        super(code, name);
    }

    @Override
    public void sound() {
        System.err.println("El perro Hace Wau Wau");
    }
}



/*==================CLASE EMPLOYEE======================*/
public class Employee {
    private Integer code;
    private String name;

    public Employee() {
    }

    public Employee(Integer code, String name) {
        this.code = code;
        this.name = name;
    }

    public Integer getCode() {
        return code;
    }

    public void setCode(Integer code) {
        this.code = code;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Employee) {
            Employee e = (Employee) obj;
            if (this.code.equals(e.code))
                return true;
        }
        return false;
    }

}




/*==================CLASE PROJECT======================*/
public class Project {
    private String code;
    private String name;
    private Set<Programmer> team;

    public Project() {
    }

    public Project(String code, String name) {
        this.code = code;
        this.name = name;
    }

    public void addToTeam(Programmer programmer) {
        if (team == null) {
            this.team = new HashSet<>();
        }
        this.team.add(programmer);
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Set<Programmer> getTeam() {
        return team;
    }

}




/*==================CLASE MANAGER======================*/
public class Manager extends Employee {
    private Set<ProjectManager> projectManagers;
    private Set<Programmer> programmers;

    public Manager() {
    }

    public Manager(Integer code, String name) {
        super(code, name);
    }

    public void addProjectManager(ProjectManager projectManager) {
        if (projectManagers == null) {
            this.projectManagers = new HashSet<>();
        }
        this.projectManagers.add(projectManager);
    }

    public void addProgramer(Programmer programmer) {
        if (programmers == null) {
            this.programmers = new HashSet<>();
        }
        this.programmers.add(programmer);
    }

    public Set<ProjectManager> getProjectManagers() {
        return projectManagers;
    }

    public Set<Programmer> getProgrammers() {
        return programmers;
    }

}





/*==================CLASE PROJECT MANAGER======================*/
public class ProjectManager extends Employee {
    private List<Project> projects;

    public ProjectManager() {
    }

    public ProjectManager(Integer code, String name) {
        super(code, name);
    }

    public void addProject(Project project) {
        if (projects == null) {
            this.projects = new ArrayList<>();
        }
        this.projects.add(project);
    }

    public List<Project> getProjects() {
        return projects;
    }

    public void listProjects() {
        this.projects.forEach(p -> {
            System.out.println("#".repeat(20));
            System.out.println(String.format("Proyecto %s - %s", p.getCode(), p.getName()));
            System.out.println(String.format("Gerentes de Proyecto : %s - %s", getCode(), getName()));
            System.out.println("Equipo conformado por :");
            p.getTeam().forEach(t -> System.out.println(t.toString()));
        });
    }

}



/*==================CLASE PROGRAMMER======================*/
public class Programmer extends Employee {
    private Set<String> languages;

    public Programmer() {
    }

    public Programmer(Integer code, String name) {
        super(code, name);
        this.languages = new HashSet<>();
    }

    public Set<String> getLanguages() {
        return languages;
    }

    public void setLanguages(Set<String> languages) {
        this.languages = languages;
    }

    public void addLanguage(String language) {
        this.languages.add(language);
    }

    @Override
    public String toString() {
        return String.format("Código : %s, Nombre : %s, Lenguajes : %s", getCode(), getName(), getLanguages());
    }

}