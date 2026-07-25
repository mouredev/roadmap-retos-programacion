class Program
{
    static void Main(string[] args)
    {
        Perro perro = new Perro();
        Gato gato = new Gato();

        EmitirSonido(perro);
        EmitirSonido(gato);
        Console.ReadLine();

        Manager manager = new Manager(1, "Joaquín");
        ProjectManager projectManager1 = new ProjectManager(2, "Ramiro", "App móvil");
        ProjectManager projectManager2 = new ProjectManager(3, "Alberto", "Página Web");
        Programmer programmer1 = new Programmer(4, "Emilio", "C#");
        Programmer programmer2 = new Programmer(5, "Luis", "Python");
        Programmer programmer3 = new Programmer(6, "Aldo", "Java");
        Programmer programmer4 = new Programmer(7, "Ale", "PHP");
        Programmer programmer5 = new Programmer(8, "Samantha", "SQL");
        Programmer programmer6 = new Programmer(9, "Mario", "VB");

        manager.AgregarEmpleado(projectManager1.Nombre);
        manager.AgregarEmpleado(projectManager2.Nombre);
        manager.ImprimirEmpleados();
        manager.CoordinarProyectos();
        Console.WriteLine();

        projectManager1.AgregarEmpleado(programmer1.Nombre);
        projectManager1.AgregarEmpleado(programmer3.Nombre);
        projectManager1.AgregarEmpleado(programmer5.Nombre);

        projectManager1.ImprimirEmpleados();
        projectManager1.ConsultarProyecto();
        Console.WriteLine();

        projectManager2.AgregarEmpleado(programmer2.Nombre);
        projectManager2.AgregarEmpleado(programmer4.Nombre);
        projectManager2.AgregarEmpleado(programmer6.Nombre);

        projectManager2.ImprimirEmpleados();
        projectManager2.ConsultarProyecto();
        Console.WriteLine();

        programmer1.AgregarEmpleado("Ziggy");
        programmer1.ImprimirEmpleados();
        programmer1.Consultar();

    }
    static void EmitirSonido(Animal animal)
    {
        animal.EmitirSonido();
    }
}
class Animal
{
    public virtual void EmitirSonido()
    {

    }
}

class Perro : Animal
{
    public override void EmitirSonido() 
    {
        Console.WriteLine("Guau!");
    }
}
class Gato : Animal
{
    public override void EmitirSonido()
    {
        Console.WriteLine("Miau!");
    }
}

class Empleado
{
    protected int _id;
    protected string _nombre;
    protected List<string> _empleados;

    public string Nombre { get { return _nombre; } }

    public Empleado(int id, string nombre)
    {
        _id = id;
        _nombre = nombre;
        _empleados = new List<string>();
    }
    public virtual void AgregarEmpleado(string empleado)
    {
        _empleados.Add(empleado);
    }
    public virtual void ImprimirEmpleados()
    {
        if (_empleados.Count == 0)
        {
            Console.WriteLine($"No hay empleados al cargo de {_nombre}");
            return;
        }
        Console.WriteLine($"Los empleados a cargo de {_nombre} son:");
        foreach(string empleado in _empleados)
            Console.WriteLine($"{empleado}");
    }
}
class Manager : Empleado
{
    public Manager(int id, string nombre) : base(id, nombre) { }
    public void CoordinarProyectos()
    {
        Console.WriteLine($"{_nombre} esta coordinando todos los proyectos");
    }
}
class ProjectManager : Empleado
{
    private string _proyecto;
    public ProjectManager(int id, string nombre, string proyecto) : base(id, nombre) 
    {
        _proyecto = proyecto;
    }
    public void ConsultarProyecto()
    {
        Console.WriteLine($"{_nombre} coordina el proyecto {_proyecto}");
    }
}
class Programmer : Empleado
{
    private string _lenguaje;
    public Programmer(int id, string nombre, string lenguaje): base(id, nombre)
    {
        _lenguaje = lenguaje;
    }
    public override void AgregarEmpleado(string empleado)
    {
        Console.WriteLine($"{_nombre} no puede agregar empleados");
    }
    public void Consultar()
    {
        Console.WriteLine($"{_nombre} programa en {_lenguaje}");
    }
}