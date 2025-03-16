using System.ComponentModel;
using System.Reflection;

/**
 * Clase base Animal
 */
public abstract class Animal
{
    public string? Name { get; }
    public string? Color { get; }
    public int? Age { get; }

    protected Animal(string name, string color, int age) 
    { 
        this.Name = name;
        this.Color = color;
        this.Age = age;
    }

    public abstract string Sonido();
}

/**
 * Subclase Perro que hereda de Animal
 */
public class Dog : Animal
{
    public Dog(string name, string color, int age) : base(name, color, age) { }

    public override string Sonido()
    {
        return "Guau!";
    }
}

/**
 * Subclase Gato que hereda de Animal
 */
public class Cat : Animal
{
    public Cat(string name, string color, int age) : base(name, color, age) { }

    public override string Sonido()
    {
        return "Miau!";
    }
}

/**
 * Enumeración para los roles de los empleados
 */
public enum EmployeeRole
{
    [Description("Gerente")]
    Managers,
    [Description("Gerente de proyecto")]
    ProjectManagers,
    [Description("Programador")]
    Programmers,
    [Description("Programador Senior")]
    Senior,
    [Description("Programador Midle")]
    Midle,
    [Description("Programador Junior")]
    Junior
}

/**
 * Clase base Empleado
 */
public abstract class Employee
{
    public int Identifier { get; }
    public string Name { get; }
    public EmployeeRole Rol { get; }

    protected Employee(int identifier, string name, EmployeeRole rol)
    {
        Identifier = identifier;
        Name = name;
        Rol = rol;
    }

    /**
     * Obtener el Description attribute del enum
     */
    public string GetNameRol()
    {
        MemberInfo? field = Rol.GetType().GetField(Rol.ToString());
        DescriptionAttribute? attribute = Attribute.GetCustomAttribute(element: field, attributeType: typeof(DescriptionAttribute)) as DescriptionAttribute;
        return attribute.Description;
    }

    public virtual string GetEmployeeInformation()
    {
        return $"=> ID: {Identifier}, Nombre: {Name}, Rol: {GetNameRol()}";
    }

    public abstract void Work();
}

/**
 * Subclase Gerente que hereda de Empleado
 */
public class Managers : Employee
{
    public decimal Salary { get; }
    public string Department { get; }
    public int Experience { get; }
    public DateTime HiringDate { get; }
    public List<Employee> EmployeesInCharge { get; }

    public Managers(int identifier, string name, EmployeeRole rol, decimal salary, string department, int experience, DateTime hiringDate) : base(identifier, name, rol) 
    { 
        Salary = salary;
        Department = department;
        Experience = experience;
        HiringDate = hiringDate;
        EmployeesInCharge = new List<Employee>();
    }

    public void AddEmployee(Employee employee)
    {
        EmployeesInCharge.Add(employee);
    }

    public override void Work()
    {
        Console.WriteLine($"{base.GetEmployeeInformation()}");
        Console.WriteLine($"Salario: {Salary}, Departamento: {Department}, Experiencia: {Experience} años, Fecha de Contratación: {HiringDate.ToString("dd/MM/yyyy")}");
        Console.WriteLine($"Empleados a cargo: {EmployeesInCharge.Count}");
        Console.WriteLine("Supervisando equipos y proyectos");
    }
}

/**
 * Subclase GerenteProyecto que hereda de Gerente
 */
public class ProjectManagers : Managers
{
    public List<string> Project { get; }

    public ProjectManagers(int identifier, string name, EmployeeRole rol, decimal salary, string department, int experience, DateTime hiringDate) : base(identifier, name, rol, salary, department, experience, hiringDate)
    {
        Project = new List<string>();
    }

    public void AddProject(string proyecto)
    {
        Project.Add(proyecto);
    }

    public override void Work()
    {
        Console.WriteLine($"{base.GetEmployeeInformation()}");
        Console.WriteLine($"Salario: {Salary}, Departamento: {Department}, Experiencia: {Experience} años, Fecha de Contratación: {HiringDate.ToString("dd/MM/yyyy")}");
        Console.WriteLine($"Número de empleados a cargo: {EmployeesInCharge.Count}");
        Console.WriteLine($"Número de proyectos asignados: {Project.Count}");
        Console.WriteLine("Gestionando proyectos y recursos");
    }
}

/**
 * Subclase Programador que hereda de Empleado
 */
public class Programmers : Employee
{
    protected string[] Technologies { get; }
    protected string Level { get; }

    public Programmers(int id, string nombre, string[] technologies, string level) : base(id, nombre, GetRolByNivel(level))
    {
        Technologies = technologies;
        Level = level;
    }

    /**
     * Método para obtener el RolEmpleado según el nivel del programador
     */
    private static EmployeeRole GetRolByNivel(string level)
    {
        switch (level.ToLower())
        {
            case "junior":
                return EmployeeRole.Junior;
            case "midle":
                return EmployeeRole.Midle;
            case "senior":
                return EmployeeRole.Senior;
            default:
                return EmployeeRole.Programmers;
        }
    }

    public override void Work()
    {
        Console.WriteLine($"{base.GetEmployeeInformation()}");
        Console.WriteLine($"Tecnologias: {string.Join(", ", Technologies)}");
        Console.WriteLine($"Nivel: {Level}");
        Console.WriteLine("Desarrollando código");
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Ejemplo de animales
        Animal perro = new Dog("Tom", "Negro", 5);
        Animal gato = new Cat("Jerry", "Blanco", 5);

        Console.WriteLine("Sonido del perro: " + perro.Sonido());
        Console.WriteLine("Sonido del gato: " + gato.Sonido());

        // Ejemplo de empleados Gerente/Gerente proyecto/Programador
        Employee gerente = new Managers(1, "Juan", EmployeeRole.Managers, 50000, "Recursos Humanos", 10, DateTime.Now.AddYears(-5));
        Employee gerenteProyecto = new ProjectManagers(2, "María", EmployeeRole.ProjectManagers, 60000, "Arquitecto", 8, DateTime.Now.AddYears(-3));
        Employee programadorSenior = new Programmers(3, "Pedro", new string[] { "C#", "JavaScript", "SQL", "Angular", "Nodejs" }, "senior");
        Employee programadorJunior = new Programmers(4, "Carlos", new string[] { "C#", "JavaScript", "SQL" }, "junior");
        
        ((Managers)gerente).AddEmployee(gerenteProyecto);
        ((Managers)gerente).AddEmployee(programadorSenior);
        ((Managers)gerente).AddEmployee(programadorJunior);

        ((ProjectManagers)gerenteProyecto).AddEmployee(programadorSenior);
        ((ProjectManagers)gerenteProyecto).AddEmployee(programadorJunior);

        ((ProjectManagers)gerenteProyecto).AddProject("Proyecto A");
        ((ProjectManagers)gerenteProyecto).AddProject("Proyecto B");

        gerente.Work();
        gerenteProyecto.Work();
        programadorSenior.Work();
        programadorJunior.Work();
    }
}
