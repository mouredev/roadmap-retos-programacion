using System;

class Person
{
    private int _id;
    private string _name;
    private Person? _partner = null;
    private List<Person>? _children;
    private bool _hasParents;

    public int Id { get { return _id; } }
    public string Name { get { return _name; } }
    public Person Partner { get { return _partner; } }
    public List<Person> Children { get { return _children; } }
    public bool HasParents { get { return _hasParents; } set { _hasParents = value; } }

    public Person(int id, string name)
    {
        _id = id;
        _name = name;
        _hasParents = false;
        _children = new List<Person>();
    }

    public void AddPartner(Person partner) 
    {
        if (_partner != null)
        {
            Console.WriteLine($"{_name} ya tiene una pareja ({_partner._name})");
            return;
        }
        if (partner.Partner != null)
        {
            Console.WriteLine($"{partner.Name} ya tiene una pareja ({partner.Partner.Name})");
            return;
        }
        if (partner == this)
        {
            Console.WriteLine($"{_name} no puede estar emparejado consigo mismo...");
            return;
        }
        _partner = partner;
        _partner._partner = this;
        Console.Clear();
        Console.WriteLine($"{_partner._name} ahora es pareja de {_name}");
    }

    public void AddChild(Person child)
    {
        if (_children.Where(c => c._id == child._id).Count() > 0)
        {
            Console.WriteLine($"{child._name} ya es hijo de {_name}");
            return;
        }
        if (child == this)
        {
            Console.WriteLine($"{_name} no puede ser su mismo hijo");
        }
        _children.Add(child);
        Console.Clear();
    }
}

class FamiliyTree
{
    private List<Person> _people;
    public int Id = 1;
    public FamiliyTree()
    {
        _people = new List<Person>();
    }

    public void AddPerson(Person person)
    {
        if (_people.Exists(p => p.Id == person.Id))
        {
            Console.WriteLine($"Una persona con el Id {person.Id} ya ha sido registrada...");
            return;
        }
        _people.Add(person);
        Console.WriteLine($"{person.Name} ha sido agregado a la lista correctamente...");
        Id++;
    }
    public void RemovePerson(int id)
    {
        var person = _people.Where(p => p.Id == id).FirstOrDefault();
        if (person == null)
        {
            Console.WriteLine($"La persona con el id {id} no existe...");
            return;
        }
        _people.Remove(person);
        Console.Clear();
        Console.WriteLine($"{person.Name} ha sido eliminado...");
    }

    public bool PrintList()
    {
        if (_people.Count == 0)
        {
            Console.WriteLine("No hay personas registradas...");
            return false;
        }
        foreach (Person person in _people)
            Console.WriteLine($"{person.Id}.- {person.Name}");
        return true;
    }
    public Person? Get(int id)
    {
        var person = _people.FirstOrDefault(p => p.Id == id);

        return person;
    }
    public void SetPartner(int id, int idPartner)
    {
        var person = Get(id);
        var partner = Get(idPartner);

        if (person == null || partner == null)
        {
            Console.WriteLine("Un Id o más no pudieron ser encontrados");
            return;
        }
        person.AddPartner(partner);
    }
    public void SetChild(int idParent, int idChild)
    {
        var parent = Get(idParent);
        var child = Get(idChild);

        if (parent == null || child == null)
        {
            Console.WriteLine("Un Id o más no pudieron ser encontrados");
            return;
        }
        if (parent.Partner == null)
        {
            Console.WriteLine($"{parent.Name} no tiene una pareja con la que tener hijos...");
            return;
        }
        if (child.HasParents)
        {
            Console.WriteLine($"{child.Name} ya cuenta con padres...");
            var parents = GetParents(idChild);
            foreach (var person in GetParents(idChild))
                Console.WriteLine($"{person.Id}.- {person.Name}");
            return;
        }
        parent.AddChild(child);
        parent.Partner.AddChild(child);
        child.HasParents = true;
        Console.WriteLine($"{child.Name} es hijo de {parent.Name} y {parent.Partner.Name}");
    }
    public List<Person> GetParents(int idChild)
    {
        var parents = new List<Person>();
        foreach (Person person in _people)
        {
            if (person.Children.Exists(p => p.Id == idChild))
                parents.Add(person);
        }
        return parents;
    }
    public void PrintTree()
    {
        if (_people.Count == 0)
        {
            Console.WriteLine("No hay personas registradas...");
            return;
        }
        List<Person> visited = new List<Person>();
        void PrintPerson(Person person)
        {
            if (visited.Contains(person))
                return;
            visited.Add(person);

            Console.Write($"{person.Id}.- {person.Name}");

            if (person.Partner != null)
            {
                visited.Add(person.Partner);
                Console.Write($"\tPareja: {person.Partner.Id}.- {person.Partner.Name}");
            }
            Console.WriteLine();
            if (person.Children.Count > 0)
            {
                Console.WriteLine("Hijos");
                foreach (Person child in person.Children)
                    PrintPerson(child);
                Console.WriteLine();
            }
        }
        
        foreach(Person person in _people) 
            PrintPerson(person);
    }
    
}
class Program
{
    static void Main(string[] args)
    {
        var tree = new FamiliyTree();
        bool exit = false;

        do
        {
            Menu();
            int option = 0;
            int.TryParse(Console.ReadLine(), out option);

            switch (option)
            {
                case 1:
                    AddPerson(ref tree);
                    break;
                case 2:
                    RemovePerson(ref tree);
                    break;
                case 3:
                    SetPartner(ref tree);
                    break;
                case 4:
                    SetChild(ref tree);
                    break;
                case 5:
                    PrintTree(ref tree);
                    break;
                case 6:
                    exit = true;
                    Console.Clear();
                    Console.WriteLine("Hasta la próxima...");
                    Thread.Sleep(1000);
                    break;
                default:
                    Console.Clear();
                    Console.WriteLine("Opción no válida...");
                    break;
            }
        } while (!exit);


    }

    static void Menu()
    {
        Console.WriteLine("---ÁRBOL GENEALÓGICO---");
        Console.WriteLine("1.- Agregar una persona.");
        Console.WriteLine("2.- Eliminar a una persona.");
        Console.WriteLine("3.- Agregar una pareja.");
        Console.WriteLine("4.- Agregar un hijo.");
        Console.WriteLine("5.- Imprimir árbol.");
        Console.WriteLine("6.- Salir.");
        Console.WriteLine("Selecciona una opción...");
    }
    static void AddPerson(ref FamiliyTree tree)
    {
        Console.Clear();
        Console.WriteLine("Ingresa el nombre de la persona");
        string? name = Console.ReadLine();
        if (string.IsNullOrEmpty(name))
        {
            Console.WriteLine("El nombre no es válido...");
            return;
        }
        var person = new Person(tree.Id, name);
        tree.AddPerson(person);
    }
    static void RemovePerson(ref  FamiliyTree tree)
    {
        Console.Clear();
        if (!tree.PrintList())
            return;
        Console.WriteLine("Ingresa el Id de la persona a eliminar");
        int id = 0;
        int.TryParse(Console.ReadLine(), out id);
        tree.RemovePerson(id);
    }
    static void SetPartner(ref FamiliyTree tree)
    {
        Console.Clear();
        if (!tree.PrintList())
            return;
        Console.WriteLine("Ingresa el Id de la primera persona");
        int id = 0;
        int.TryParse(Console.ReadLine(), out id);
        Console.WriteLine("Ingresa el Id de su pareja");
        int idPartner = 0;
        int.TryParse(Console.ReadLine(), out idPartner);
        tree.SetPartner(id, idPartner);
    }
    static void SetChild(ref  FamiliyTree tree)
    {
        Console.Clear();
        if (!tree.PrintList()) 
            return;
        Console.WriteLine("Ingresa el Id del padre");
        int idParent = 0;
        int.TryParse(Console.ReadLine(), out idParent);
        Console.WriteLine("Ingresa el Id del hijo");
        int idChild = 0;
        int.TryParse(Console.ReadLine(), out idChild);
        tree.SetChild(idParent, idChild);
    }
    static void PrintTree(ref FamiliyTree tree)
    {
        Console.Clear();
        tree.PrintTree();
        Console.ReadLine();
    }
}