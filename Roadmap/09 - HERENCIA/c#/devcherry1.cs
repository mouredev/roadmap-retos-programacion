using System;
class Program
{
    static void Main()
    {
        Perro miPerro = new Perro();
        miPerro.Nombre = "Firulais";
        miPerro.Comer();  // Método heredado de la clase Animal
        miPerro.Ladrar();
        Gato miGato = new Gato();
        miGato.Nombre = "Michin";
        miGato.Comer();
        miGato.Maullar();

        Developer dev1 = new Developer { Nombre = "Luis", ID = 7 };
        Developer dev2 = new Developer { Nombre = "Camila", ID = 2 };
        Developer dev3 = new Developer { Nombre = "Alexandra", ID = 3 };
        Developer dev4 = new Developer { Nombre = "Carlos", ID = 4 };
        Developer dev5 = new Developer { Nombre = "Sofia", ID = 8 };

        ProjectManager pm1 = new ProjectManager { Nombre = "Gerald", ID = 5 };
        ProjectManager pm2 = new ProjectManager { Nombre = "Edgar", ID = 6 };

        Manager boss = new Manager { Nombre = "Ernesto", ID = 1 };

        dev1.Funcion();
        pm1.Funcion();
        boss.Funcion();

        // Asignar Developers a cada ProjectManager
        pm1.AsignarDeveloper(dev1);
        pm1.AsignarDeveloper(dev2);

        pm2.AsignarDeveloper(dev3);
        pm2.AsignarDeveloper(dev4);
        pm2.AsignarDeveloper(dev5);

        // Asignar ProjectManagers al Manager
        boss.AsignarProjectManager(pm1);
        boss.AsignarProjectManager(pm2);

        // Mostrar la jerarquía
        Console.WriteLine($"\n**Jerarquía del Manager:**");
        boss.MostrarJerarquia();
    }
}
public class Animal
{
    public string Nombre { get; set; }

    public void Comer()
    {
        Console.WriteLine($"{Nombre} está comiendo.");
    }
}
public class Perro : Animal
{
    public void Ladrar()
    {
        Console.WriteLine($"{Nombre} está ladrando.");
    }
}
public class Gato : Animal
{
    public void Maullar()
    {
        Console.WriteLine($"{Nombre} está maullando.");
    }
}
public class Empleado
{
    public string Nombre { get; set; }
    public int ID { get; set; }
}
public class Developer : Empleado
{
    public void Funcion()
    {
        Console.WriteLine($"{Nombre} convierte el cafe en codigo.");
    }
}
public class ProjectManager : Empleado
{
    public List<Developer> Developers { get; private set; } = new List<Developer>();
    public void Funcion()
    {
        Console.WriteLine($"{Nombre} se encarga de que todos planifica y coordina.");
    }
    public void AsignarDeveloper(Developer developer)
    {
        Developers.Add(developer);
    }

    public void MostrarDevelopers()
    {
        Console.WriteLine($"  {Nombre} tiene asignados los siguientes Developers: ({Developers.Count})");
        foreach (var dev in Developers)
        {
            Console.WriteLine($"    - {dev.Nombre} (ID: {dev.ID})");
        }
    }
}
public class Manager : Empleado
{
    public List<ProjectManager> ProjectManagers { get; private set; } = new List<ProjectManager>();

    public void Funcion()
    {
        Console.WriteLine($"{Nombre} asigna responsabilidades y supervisa operaciones.");
    }
    public void AsignarProjectManager(ProjectManager projectManager)
    {
        ProjectManagers.Add(projectManager);
    }
    public void MostrarJerarquia()
    {
        Console.WriteLine($"\n{Nombre} supervisa a los siguientes ProjectManagers: ({ProjectManagers.Count})");
        foreach (var pm in ProjectManagers)
        {
            Console.WriteLine($"- {pm.Nombre} (ID: {pm.ID})");
            pm.MostrarDevelopers();
        }
    }
}
