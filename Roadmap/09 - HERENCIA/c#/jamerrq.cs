using System;

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

namespace Roadmap09
{
    class Animal
    {
        public string Sound { get; set; }
        public Animal(string sound)
        {
            Sound = sound;
        }
        public void MakeSound()
        {
            Console.WriteLine(Sound);
        }
    }

    class Dog : Animal
    {
        public Dog() : base("Woof!") { }
    }

    class Cat : Animal
    {
        public Cat() : base("Meow!") { }
    }

    // Extra ejercicio: Empresa de desarrollo

    class Employee
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public Employee(int id, string name)
        {
            Id = id;
            Name = name;
        }
    }

    class Manager : Employee
    {
        public Manager(int id, string name) : base(id, name) { }
    }

    class ProjectManager : Employee
    {
        public ProjectManager(int id, string name) : base(id, name) { }
    }

    class Programmer : Employee
    {
        public Programmer(int id, string name) : base(id, name) { }
    }

    class Company
    {
        public Employee[] Employees { get; set; }
        public Company(Employee[] employees)
        {
            Employees = employees;
        }
    }

    class Tasks
    {
        public void AssignTask(Employee employee, string description)
        {
            Console.WriteLine($"Assigning task to {employee.Name}: {description}");
            switch (employee)
            {
                case Manager manager:
                    Console.WriteLine($"Assigning task to manager {manager.Name}");
                    break;
                case ProjectManager projectManager:
                    Console.WriteLine($"Assigning task to project manager {projectManager.Name}");
                    break;
                case Programmer programmer:
                    Console.WriteLine($"Assigning task to programmer {programmer.Name}");
                    break;
                default:
                    Console.WriteLine("Employee not found");
                    break;
            }
        }
    }

    class CompanyProgram
    {
        public static void CompanyMain(string[] args)
        {
            Employee[] employees = new Employee[3];
            employees[0] = new Manager(1, "John Doe");
            employees[1] = new ProjectManager(2, "Jane Doe");
            employees[2] = new Programmer(3, "Julia Doe");
            Company company = new Company(employees);
            Tasks tasks = new Tasks();
            tasks.AssignTask(employees[0], "Create a new project");
            tasks.AssignTask(employees[1], "Assign tasks to programmers");
            tasks.AssignTask(employees[2], "Create a new feature");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Animal dog = new Dog();
            Animal cat = new Cat();
            dog.MakeSound();
            cat.MakeSound();
            Console.WriteLine("========================================");
            Console.WriteLine("============ EJERCICIO EXTRA ===========");
            Console.WriteLine("========================================\n");
            CompanyProgram.CompanyMain(args);
        }
    }
}
