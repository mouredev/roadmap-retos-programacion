namespace exs34;
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
-----------------------------------------------------
 #34 ÁRBOL GENEALÓGICO DE LA CASA DEL DRAGÓN
-----------------------------------------------------
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026! 
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijos
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
*/

// NOTE: Here is the 'people.json' file with the data if you want to test it:
//       https://pastebin.com/29kWWgPU
//       Just paste it into the base folder.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;

//______________________________

public class Person(int id, string name)
{
    public int Id { get; set; } = id;
    public string Name { get; set; } = name;
    public List<int> Parents { get; set; } = [];
    public List<int> Partners { get; set; } = [];
    public Dictionary<int, List<int>> Children { get; set; } = [];
    public bool Deleted { get; set; }

    public Dictionary<string, object> ToDict()
    {
        return new Dictionary<string, object>
        {
            ["id"] = Id,
            ["name"] = Name,
            ["parents"] = Parents,
            ["partners"] = Partners,
            ["children"] = Children,
            ["deleted"] = Deleted
        };
    }

    public static Person FromDict(Dictionary<string, object> data)
    {
        var person = new Person((int)data["id"], (string)data["name"]);
        
        if (data.TryGetValue("parents", out var parents))
            person.Parents = (List<int>)parents;
        
        if (data.TryGetValue("partners", out var partners))
            person.Partners = (List<int>)partners;
        
        if (data.TryGetValue("children", out var children))
            person.Children = ((JsonElement)children).Deserialize<Dictionary<int, List<int>>>()!;
        
        if (data.TryGetValue("deleted", out var deleted))
            person.Deleted = (bool)deleted;
        
        return person;
    }

    public override string ToString() => $"Person(id={Id}, name='{Name}')";
}

//______________________________
public static class Input
{
    public static string GetStr(string msg)
    {
        while (true)
        {
            Console.Write(msg);
            string txt = Console.ReadLine()!;
            if (!string.IsNullOrEmpty(txt))
            {
                return txt;
            }

            Console.WriteLine("\n❌ This field cannot be empty.");
        }
    }

    public static int GetInt(string msg)
    {
        while (true)
        {
            string txt = GetStr(msg);
            if (int.TryParse(txt, out int result))
            {
                return result;
            }

            Console.WriteLine("\n❌ Enter an integer.");
        }
    }
}

//______________________________
public class People
{
    private List<Person> _people = [];
    private readonly string _filename;
    private static readonly JsonSerializerOptions _jsonOptions = new(JsonSerializerDefaults.Web) { WriteIndented = true };

    public People(string filename = "people.json")
    {
        _filename = filename;
        LoadFromJson();
    }

    public IReadOnlyList<Person> GetPeople() => _people.AsReadOnly();

    public void LoadFromJson()
    {
        try
        {
             string jsonString = File.ReadAllText(_filename);
            _people = JsonSerializer.Deserialize<List<Person>>(jsonString, _jsonOptions) ?? [];
            Console.WriteLine($"✅ The file '{_filename}' has been successfully loaded.");
        }
        catch (Exception)
        {
            Console.WriteLine($"⚠️ The file '{_filename}' not found. Starting with an empty list.");
            _people = [new(0, "unknown")];
        }
    }

    public void SaveToJson()
    {
        try
        {
            string jsonString = JsonSerializer.Serialize(_people, _jsonOptions);
            File.WriteAllText(_filename, jsonString);
            Console.WriteLine($"✅ Data saved successfully to {_filename}");
        }
        catch (Exception e)
        {
            Console.WriteLine($"❌ An error occurred while saving to '{_filename}': {e.Message}. Data may not have been saved.");
        }
    }

    public void PrintPeople()
    {
        Console.WriteLine(new string('_', 32));
        Console.WriteLine($"|{"id",4}|{"Name",-25}|");
        Console.WriteLine(new string('_', 32));
        foreach (var person in _people.Where(p => !p.Deleted))
        {
            Console.WriteLine($"|{person.Id,4}|{person.Name,-25}|");
        }
        Console.WriteLine(new string('_', 32));
    }

    public Person? GetPersonById(int id)
    {
        var person = _people.FirstOrDefault(p => p.Id == id);
        if (person == null)
        {
            Console.WriteLine("❌ id not found.");
        }
        return person;
    }

    public void AddPerson()
    {
        Console.WriteLine("Add Person or 'x' to Exit");
        string name = Input.GetStr("Name: ");
        if (name.Equals("x", StringComparison.CurrentCultureIgnoreCase))
        {
            Console.WriteLine("Exit");
            return;
        }

        int newId = _people.Count > 0 ? _people.Max(p => p.Id) + 1 : 0;
        var newPerson = new Person(newId, name);
        _people.Add(newPerson);
        Console.WriteLine($"✅ Added: {newPerson}");
        SaveToJson();
    }

    public void RemovePerson()
    {
        PrintPeople();
        Console.WriteLine("\nPerson ID to mark as deleted or a letter to exit.");
        string idStr = Input.GetStr("ID: ");
        if (!int.TryParse(idStr, out int id))
        {
            Console.WriteLine("Exit");
            return;
        }

        var person = GetPersonById(id);
        if (person == null) return;

        if (person.Partners.Count != 0 || person.Parents.Count != 0)
        {
            Console.WriteLine("❌ You cannot delete a person who is linked to parents or partners.");
            return;
        }

        person.Deleted = true;
        Console.WriteLine($"✅ '{person.Name}' is marked as deleted.");
        SaveToJson();
    }

    public int Count => _people.Count;

}

//______________________________
public class Partners : People
{
    private void Add(List<int> partners, int idPerson)
    {
        Console.WriteLine("Select Partner ID");
        int idPartner = Input.GetInt("ID: ");
        var partner = GetPersonById(idPartner);
        if (partner == null || partner.Deleted)
        {
            Console.WriteLine("❌ ID not found or the person is deleted.");
            return;
        }

        if (partners.Contains(idPartner))
        {
            Console.WriteLine("❌ This partner is already added.");
            return;
        }

        partners.Add(idPartner);
        partner.Partners.Add(idPerson);

        Console.WriteLine("✅ Partner successfully added.");
        SaveToJson();
    }

    private void Remove(List<int> partners, int idPerson)
    {
        Console.WriteLine("Select Partner ID to Delete");
        int id = Input.GetInt("ID: ");
        if (!partners.Contains(id))
        {
            Console.WriteLine("❌ ID not found.");
            return;
        }

        var partner = GetPersonById(id);
        if (partner == null)
        {
            Console.WriteLine("❌ Partner not found.");
            return;
        }

        if (partner.Children.Count != 0)
        {
            Console.WriteLine("❌ Cannot delete a partner who has children.");
            return;
        }

        partners.Remove(id);
        partner.Partners.Remove(idPerson);

        Console.WriteLine("✅ Partner deleted");
        SaveToJson();
    }

    private void Options(List<int> partners, int idPerson)
    {
        Console.WriteLine("\n1. Add partner | 2. Remove partner | 3. Exit");
        int option = Input.GetInt("\nOption: ");

        switch (option)
        {
            case 1:
                Add(partners, idPerson);
                break;
            case 2:
                Remove(partners, idPerson);
                break;
            case 3:
                return;
            default:
                Console.WriteLine("❌ Invalid option.");
                break;
        }
    }

    public void EditPartners()
    {
        PrintPeople();
        Console.WriteLine("\nPerson ID to edit partners or a letter to exit.");
        string idStr = Input.GetStr("ID: ");
        if (!int.TryParse(idStr, out int id))
        {
            Console.WriteLine("Exit");
            return;
        }

        var person = GetPersonById(id);
        if (person == null || person.Deleted)
        {
            Console.WriteLine("❌ ID not found or the person is deleted.");
            return;
        }

        Console.WriteLine($"You selected '{person.Name}'");
        var partners = person.Partners;

        if (partners.Count != 0)
        {
            Console.WriteLine("Partners:");
            foreach (var idP in partners)
            {
                var partner = GetPersonById(idP);
                if (partner != null)
                {
                    Console.WriteLine($"ID: {partner.Id} -> {partner.Name}");
                }
            }
        }
        else
        {
            Console.WriteLine("🚫 This person has no partners.");
        }

        Options(partners, id);
    }
}

//______________________________
public class Children : Partners
{
    private int _idParent;
    private Dictionary<int, List<int>>? _children;
    private int _idChild;
    private int _idPartner;

    private int? SelectPartner(List<int> partners)
    {
        Console.WriteLine("Partners:");
        foreach (var idP in partners)
        {
            var partnerPerson = GetPersonById(idP);
            if (partnerPerson != null)
            {
                Console.WriteLine($"ID: {partnerPerson.Id} -> {partnerPerson.Name}");
            }
        }

        Console.WriteLine("Select the ID of the partner with whom you have the child.");
        int idPartner = Input.GetInt("ID: ");
        var partner = GetPersonById(idPartner);
        if (!partners.Contains(idPartner) || partner == null || partner.Deleted)
        {
            Console.WriteLine("❌ ID not found or the person is deleted.");
            return null;
        }

        return idPartner;
    }

    private int? UpdateChildParent()
    {
        int idPartner = _idPartner;
        Console.WriteLine("Select Child ID");
        int idChild = Input.GetInt("ID: ");
        var child = GetPersonById(idChild);
        if (child == null)
        {
            Console.WriteLine("❌ ID not found.");
            return null;
        }

        if (child.Parents.Count != 0)
        {
            Console.WriteLine("❌ This person already has parents.");
            return null;
        }

        _children ??= [];

        if (_children.TryGetValue(idPartner, out var childrenList))
        {
            if (!childrenList.Contains(idChild))
            {
                childrenList.Add(idChild);
            }
        }
        else
        {
            _children[idPartner] = [idChild];
        }

        var parent = GetPersonById(_idParent);
        if (parent != null)
        {
            parent.Children = _children;
        }

        child.Parents = [_idParent, idPartner];

        return idChild;
    }

    private void UpdateChildPartner(Person partner)
    {
        if (partner.Children.TryGetValue(_idParent, out var childrenList))
        {
            if (!childrenList.Contains(_idChild))
            {
                childrenList.Add(_idChild);
            }
        }
        else
        {
            partner.Children[_idParent] = [_idChild];
        }
    }

    private void Add()
    {
        var parent = GetPersonById(_idParent);
        if (parent == null)
        {
            Console.WriteLine("❌ Parent not found.");
            return;
        }

        var partners = parent.Partners;
        if (partners.Count == 0)
        {
            Console.WriteLine("❌ This person does not have a partner with whom to have children.");
            return;
        }

        var idPartner = SelectPartner(partners);
        if (!idPartner.HasValue)
        {
            return;
        }

        var partner = GetPersonById(idPartner.Value);
        if (partner == null)
        {
            Console.WriteLine("❌ Partner not found.");
            return;
        }

        _idPartner = idPartner.Value;
        var idChild = UpdateChildParent();
        if (!idChild.HasValue)
        {
            return;
        }

        _idChild = idChild.Value;
        UpdateChildPartner(partner);

        Console.WriteLine("✅ Child successfully added.");
        SaveToJson();
    }

    private void RemoveAndUpdate(int idParent, int idPartner)
    {
        var parent = GetPersonById(idParent);
        if (parent == null)
        {
            Console.WriteLine("❌ Parent not found.");
            return;
        }

        if (parent.Children.TryGetValue(idPartner, out var childrenWithPartner))
        {
            childrenWithPartner.Remove(_idChild);
            if (childrenWithPartner.Count == 0)
            {
                parent.Children.Remove(idPartner);
            }
            else
            {
                parent.Children[idPartner] = childrenWithPartner;
            }
        }

        var child = GetPersonById(_idChild);
        child?.Parents.Remove(idParent);

        Console.WriteLine($"✅ Child deleted in parent: (ID: {idParent})");
        SaveToJson();
    }

    private void Remove()
    {
        Console.WriteLine("Select Child ID to Delete");
        _idChild = Input.GetInt("ID: ");
        var child = GetPersonById(_idChild);
        if (child == null)
        {
            Console.WriteLine("❌ Child not found.");
            return;
        }

        var parents = child.Parents;
        if (parents.Count != 2)
        {
            Console.WriteLine("❌ Child does not have two parents.");
            return;
        }

        int idP1 = parents[0], idP2 = parents[1];
        RemoveAndUpdate(idP1, idP2);
        RemoveAndUpdate(idP2, idP1);
    }

    private void Options()
    {
        Console.WriteLine("\n1. Add child | 2. Remove child | 3. Exit");
        int option = Input.GetInt("\nOption: ");

        switch (option)
        {
            case 1:
                Add();
                break;
            case 2:
                Remove();
                break;
            case 3:
                return;
            default:
                Console.WriteLine("❌ Invalid option.");
                break;
        }
    }

    public void EditChildren()
    {
        PrintPeople();
        Console.WriteLine("\nPerson ID to edit Children or a letter to exit.");
        string idStr = Input.GetStr("ID: ");
        if (!int.TryParse(idStr, out int id))
        {
            Console.WriteLine("Exit");
            return;
        }

        var parent = GetPersonById(id);
        if (parent == null || parent.Deleted)
        {
            Console.WriteLine("❌ ID not found or the person is deleted.");
            return;
        }

        Console.WriteLine($"You selected '{parent.Name}'");
        var children = parent.Children;
        if (children.Count != 0)
        {
            Console.WriteLine("Children:");
            foreach (var (partnerId, childIds) in children)
            {
                var partner = GetPersonById(partnerId);
                string partnerName = partner?.Name ?? "Unknown";
                Console.WriteLine($"With ID: {partnerId} -> '{partnerName}':");
                foreach (var childId in childIds)
                {
                    var child = GetPersonById(childId);
                    string childName = child?.Name ?? "Unknown";
                    Console.WriteLine($"    ID: {childId} -> '{childName}'");
                }
            }
        }
        else
        {
            Console.WriteLine("🚫 This person has no children.");
        }

        _idParent = id;
        _children = children;
        Options();
    }
}

//______________________________
public class Tree : Children
{
    private (List<Person> Grandparents, List<Person> NoPartner) FilteredGrandparents()
    {
        var grandparents = new List<Person>();
        var noPartner = new List<Person>();

        foreach (var person in GetPeople())
        {
            if (person.Parents.Count == 0 && !person.Deleted && person.Name != "unknown")
            {
                if (person.Partners.Count == 0)
                {
                    noPartner.Add(person);
                    continue;
                }

                bool hasGrandparentPartner = person.Partners.Any(partnerId =>
                {
                    var partner = GetPersonById(partnerId);
                    return partner != null && grandparents.Contains(partner);
                });

                if (!hasGrandparentPartner)
                {
                    grandparents.Add(person);
                }
            }
        }

        return (grandparents, noPartner);
    }

    private void PrintChild(List<int> children, string prefix, bool isLast, bool isRoot)
    {
        for (int j = 0; j < children.Count; j++)
        {
            bool isLastChild = j == children.Count - 1;
            string newPrefix = prefix;
            if (!isRoot)
            {
                newPrefix = prefix[..^4] + (isLast ? "    " : "│   ");
            }

            PrintFamily(
                children[j],
                newPrefix + (isLastChild ? "└── " : "├── "),
                isLastChild,
                false
            );
        }
    }

    private void PrintParents(int id, List<int> partners, string prefix, bool isLast, bool isRoot)
    {
        foreach (var partnerId in partners)
        {
            var partner = GetPersonById(partnerId);
            if (partner != null)
            {
                Console.WriteLine($"{prefix}💑 With: {partner.Name} (ID: {partner.Id})");
                if (partner.Children.TryGetValue(id, out var children) && children.Count > 0)
                {
                    PrintChild(children, prefix, isLast, isRoot);
                }
                else
                {
                    Console.WriteLine($"{prefix}└── 🚫 Without children");
                }
            }
        }
    }

    private void PrintFamily(int id, string prefix = "", bool isLast = false, bool isRoot = true)
    {
        var person = GetPersonById(id);
        if (person == null) return;

        Console.WriteLine($"{prefix}🙂 {person.Name} (ID: {person.Id})");

        if (person.Partners.Count > 0)
        {
            if (!isRoot)
            {
                prefix = prefix[..^4] + (isLast ? "    " : "│   ");
            }

            PrintParents(id, person.Partners, prefix, isLast, isRoot);
            if (!isLast)
            {
                Console.WriteLine(prefix);
            }
        }
    }

    public void PrintTree()
    {
        var (grandparents, noPartner) = FilteredGrandparents();

        if (grandparents.Count == 0 && noPartner.Count == 0)
        {
            Console.WriteLine("⚠️ No users are registered.");
            return;
        }

        if (noPartner.Count > 0)
        {
            Console.WriteLine("__________\nParents unknown, without descendants and without a partner:");
            foreach (var p in noPartner)
            {
                Console.WriteLine($"😐 {p.Name} (ID: {p.Id})");
            }
        }

        Console.WriteLine();
        for (int i = 0; i < grandparents.Count; i++)
        {
            Console.WriteLine($"__________\nFamily #{i + 1}");
            PrintFamily(grandparents[i].Id);
        }
    }
}

//______________________________
public class Program: Tree
{
    private const string MENU = @"
---------------------------------------------
| 1. Add person     | 4. Edit children      |  
| 2. Remove person  | 5. Print tree         |
| 3. Edit partners  | 6. Exit               |
---------------------------------------------";

    public void Run()
    {
        while (true)
        {
            Console.WriteLine(MENU);
            int option = Input.GetInt("\nOption: ");
            switch (option)
            {
                case 1:
                    AddPerson();
                    break;
                case 2:
                    RemovePerson();
                    break;
                case 3:
                    EditPartners();
                    break;
                case 4:
                    EditChildren();
                    break;
                case 5:
                    PrintTree();
                    break;
                case 6:
                    Console.WriteLine("Bye");
                    return;
                default:
                    Console.WriteLine("❌ Invalid option.");
                    break;
            }
        }
    }

    public static void Main()
    {
        Program program = new();
        program.Run();
    }
}
