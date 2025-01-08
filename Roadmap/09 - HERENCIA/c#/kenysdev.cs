/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
# Herencia
------------------------------------------
- Permite definir una clase que hereda atributos y métodos de una 
  clase existente, para reutilización y organización.
- La clase que hereda se conoce como “subclase” o “clase hija”.
- La clase de la que hereda se conoce como “superclase” o “clase padre”.

# Polimorfismo:
# ----------------------------------------
# - Los objetos de diferentes clases pueden ser accedidos utilizando el 
#   mismo interfaz, mostrando un comportamiento distinto 
#   (tomando diferentes formas) según cómo sean accedidos. */

class Program{

    // Superclase
    public class Animal(string name, string sound)
    {
        public string Name { get; set; } = name;
        public string Sound { get; set; } = sound;

        public void MakeSound(){
            Console.WriteLine($"{Name} hace: {Sound}");
        }
    }

    // Subclases
    class Dog(string name) : Animal(name, "Woof"){

    }

    class Cat(string name) : Animal(name, "Meow"){

    }

/*____________________________________________________
* Ejercicio usando herencia y Polimorfismo.
- Implementa la jerarquía de una empresa de desarrollo formada por 
  empleados que pueden ser Gerentes, Gerentes de Proyectos o Programadores.
- Cada empleado tiene un identificador y un nombre.
- Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
  actividad, y almacenan los empleados a su cargo. */

    class Employees{
        public static List<string[]> employees = [];
        public string identifier = "";
        public HashSet<string> tasks = [];
        public HashSet<string> staff = [];

        public void Add(params string[] names){
            foreach (var name in names){
                employees.Add([identifier, name]);
            }
        }

        public void Print(){
            foreach (var employee in employees){
                if (employee[0] == identifier){
                    Console.WriteLine($"{employee[1]} -> {identifier}");
                }
            }
        }

        public void Functions(){
            Console.WriteLine($"\nFunciones de {identifier}");
            foreach (var task in tasks){
                Console.WriteLine(task);
            }
            Console.WriteLine("--------------------");
        }

        public void Subordinates(){
            Console.WriteLine($"\nSubordinados de un {identifier}");
            foreach (var employee in employees){
                 if (staff.Contains(employee[0])){
                    Console.WriteLine($"{employee[1]} -> {employee[0]}");
                 }
            }
            Console.WriteLine("--------------------");
        }
    }

    // Subclases
    class Manager : Employees{
        public Manager(){
            identifier = "Gerente";
            tasks = ["- Supervisión", "- Toma de decisiones"];
            staff = ["Gerente de Proyecto", "Programador"];
        }
    }

    class ProjectManager : Employees{
        public ProjectManager(){
            identifier = "Gerente de Proyecto";
            tasks = ["- Planificación", "- Coordinación de proyectos"];
            staff = ["Programador"];
        }
    }

    class Programmer : Employees{
        public Programmer(){
            identifier = "Programador";
            tasks = ["- Desarrollo", "- Mantenimiento de código"];
            staff = ["No tiene subordinados"];
        }
    }

//____________________________________________________
    static void Main(){
        Dog dog = new("Max");
        Cat cat = new("Milo");
        dog.MakeSound();
        cat.MakeSound();

        //--------------
        Manager manager = new();
        ProjectManager projectManager = new();
        Programmer programmer = new();

        manager.Add("Ben", "Dan");
        projectManager.Add("Ray", "Joe");
        programmer.Add("Leo", "Sam", "Zoe", "Ana");

        manager.Functions();
        projectManager.Functions();
        programmer.Functions();

        manager.Subordinates();
        projectManager.Subordinates();

        Console.WriteLine("Total:");
        manager.Print();
        projectManager.Print();
        programmer.Print();
    }
}
