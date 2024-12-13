using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace reto_34
{
    public class Deathwing696
    {
        public class Arbol
        {
            private List<Personaje> personajes;

            public List<Personaje> Personajes { get { return personajes; } }

            public Arbol()
            {
                personajes = new List<Personaje>();
            }

            public bool AddPersonaje(Personaje personaje)
            {
                if (!personajes.Contains(personaje))
                {
                    personajes.Add(personaje);
                    Console.WriteLine("Personaje introducido correctamente\n");
                    return true;
                }

                Console.WriteLine("El personaje introducido ya existe");
                return false;
            }

            public bool DeletePersonaje(int pos)
            {
                if (personajes.Count > 0 && pos >= 0 && pos < personajes.Count)
                {
                    personajes.RemoveAt(pos);
                    Console.WriteLine("Personaje borrado correctamente\n");
                    return true;
                }

                Console.WriteLine("No se ha encontrado al personaje");
                return false;
            }

            internal void ShowSelect()
            {
                Console.WriteLine("Selecciones un personaje:");
                var i = 1;

                foreach (var personaje in personajes)
                    Console.WriteLine($"{i++}. {personaje.Name}"); 
            }

            internal bool ModificaPareja(int index, int id, string name)
            {
                if (personajes.Count == 0 || index < 0 || index >= personajes.Count)
                {
                    Console.WriteLine("Selección de personaje inválida\n");
                    return false;
                }

                Personaje parejaExistente = personajes.Where(p => p.ID == id).FirstOrDefault();

                if (parejaExistente != null)
                {
                    Console.WriteLine("El personaje pareja ya existe y no se podrá crear para crear la relación\n");
                    return false;
                }

                Personaje personajeSelected = personajes[index];
                Personaje pareja = new Personaje(id, name);

                if (!personajeSelected.AddPareja(pareja))
                    return false;                    

                Console.WriteLine("Pareja asignada correctamente");
                return true;
            }

            internal bool ModificarHijo(int index, int id, string name)
            {
                if (personajes.Count == 0 || index < 0 || index >= personajes.Count)
                {
                    Console.WriteLine("Selección de personaje inválida\n");
                    return false;
                }

                Personaje hijoExistente = personajes.Where(p => p.ID == id).FirstOrDefault();

                if (hijoExistente != null)
                {
                    Console.WriteLine("El personaje pareja ya existe y no se podrá crear para crear la relación\n");
                    return false;
                }

                Personaje personajeSelected = personajes[index];
                Personaje hijo = new Personaje(id, name);

                if (!personajeSelected.AddHijo(hijo))
                    return false;

                Console.WriteLine("Hijo asignado correctamente");
                return true;
            }

            internal void Show()
            {
                foreach (Personaje personaje in personajes)
                {
                    var pareja = personaje.Pareja?.Name;
                    Console.WriteLine($"- {personaje.Name}\t - \t {pareja}");
                    ShowSons(personaje.Hijos);
                }
            }

            private void ShowSons(List<Personaje> hijos)
            {
                foreach (Personaje hijo in hijos)
                {
                    Console.WriteLine($"\t\t - {hijo.Name}");
                }
            }
        }
        public class Personaje
        {
            private int id;
            private string name;
            private Personaje pareja = null;
            private List<Personaje> hijos;
            private int? parentId = null;

            public int ID { get { return id; } }
            public string Name { get { return name; } }

            public Personaje Pareja { get { return pareja; } }

            public List<Personaje> Hijos { get { return hijos; } }

            public int? ParentId { get { return parentId; } }

            public override bool Equals(object obj)
            {
                Personaje personaje2 = obj as Personaje;

                return this.id == personaje2.id;
            }

            public override int GetHashCode()
            {
                int hashCode = -48284730;
                hashCode = hashCode * -1521134295 + id.GetHashCode();
                hashCode = hashCode * -1521134295 + EqualityComparer<string>.Default.GetHashCode(name);
                return hashCode;
            }

            public Personaje(int id, string name)
            {
                this.id = id;
                this.name = name;
                hijos = new List<Personaje>();
            }

            public bool AddPareja(Personaje pareja)
            {
                if (this.pareja != null)
                {
                    Console.WriteLine("El personaje ya tiene una pareja\n");
                    return false;
                }

                if (pareja.pareja != null)
                {
                    Console.WriteLine("Esta pareja ya está casada con otro personaje\n");
                    return false;
                }

                this.pareja = pareja;
                pareja.pareja = this;
                return true;
            }

            public bool AddHijo(Personaje hijo)
            {
                if (hijo.parentId != null)
                {
                    Console.WriteLine("Un hijo no puede tener más de un padre\n");
                    return false;
                }

                this.Hijos.Add(hijo);
                hijo.parentId = this.id;
                return true;
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Bienvenido a la simulación del árbol genealógico de la casa de dragones");

            Arbol arbol = new Arbol();

            while (true)
            {
                Console.WriteLine("¿Qué desea hacer?");
                Console.WriteLine("1. Añadir personaje");
                Console.WriteLine("2. Eliminar personaje");
                Console.WriteLine("3. Modificar pareja");
                Console.WriteLine("4. Modificar hijos");
                Console.WriteLine("5. Mostrar árbol");
                Console.WriteLine("0. Salir");
                Console.Write("Introduce la opción: ");
                var opcion = Int16.Parse(Console.ReadLine());

                switch (opcion)
                {
                    case 1:
                        Console.Write("Introduce el id del personaje:");
                        var id = Int16.Parse(Console.ReadLine());
                        Console.Write("Introduce el nombre del personaje:");
                        var name = Console.ReadLine();
                        Personaje personaje = new Personaje(id, name);

                        arbol.AddPersonaje(personaje);
                        break;
                    case 2:
                        arbol.ShowSelect();
                        Console.Write("Seleccione una opción: ");
                        var sel = Int16.Parse(Console.ReadLine());
                        arbol.DeletePersonaje(sel - 1);
                        break;
                    case 3:
                        arbol.ShowSelect();
                        Console.Write("Seleccione una opción: ");
                        sel = Int16.Parse(Console.ReadLine());
                        Console.Write("Introduce el id de la pareja: ");
                        id = Int16.Parse(Console.ReadLine());
                        Console.Write("Introduce el nombre de la pareja: ");
                        name = Console.ReadLine();
                        arbol.ModificaPareja(sel - 1, id, name);
                        break;
                    case 4:
                        arbol.ShowSelect();
                        Console.Write("Seleccione una opción: ");
                        sel = Int16.Parse(Console.ReadLine());
                        Console.Write("Introduce el id del hijo: ");
                        id = Int16.Parse(Console.ReadLine());
                        Console.Write("Introduce el nombre del hijo: ");
                        name = Console.ReadLine();
                        arbol.ModificarHijo(sel - 1, id, name);
                        break;
                    case 5:
                        arbol.Show();
                        break;
                    case 0:
                        Console.WriteLine("Adios!");
                        Console.ReadKey();
                        return;
                    default:
                        Console.WriteLine("Opción incorrecta\n");
                        break;
                }
            }
        }
    }
}
