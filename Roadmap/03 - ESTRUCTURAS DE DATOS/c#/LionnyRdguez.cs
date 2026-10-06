using System;
using System.Collections.Generic;
using System.Linq;

namespace Ejercicio_03
{
    class Program
    {
        static void Main(string[] args)
        {
            EjemploArray();
            EjemploList();
            EjemploDictionary();
            EjemploHashSet();
            EjemploQueue();
            EjemploStack();
            EjemploLinkedList();
            EjemploSortedDictionary();
        }

        // 1. ARRAY de tamaño fijo
        static void EjemploArray()
        {
            int[] numeros = new int[5] { 3, 1, 4, 1, 5 };
            Console.WriteLine("Original: " + string.Join(", ", numeros));

            // No se puede insertar, pero podemos asignar en una posición
            numeros[2] = 99; // actualizacion
            Console.WriteLine("Después de actualizar índice 2 a 99: " + string.Join(", ", numeros));

            // No se puede borrar un elemento, pero podemos asignar un valor por defecto o crear uno nuevo
            // Borrado poniendo 0 en la posición 3
            numeros[3] = 0;
            Console.WriteLine("Después de borrar índice 3 (poner 0): " + string.Join(", ", numeros));

            // Ordenación
            Array.Sort(numeros);
            Console.WriteLine("Ordenado ascendente: " + string.Join(", ", numeros));

            // Inversión (otra forma de ordenar)
            Array.Reverse(numeros);
            Console.WriteLine("Invertido descendente: " + string.Join(", ", numeros));
            Console.WriteLine();
        }

        // 2. LIST<T>
        static void EjemploList()
        {
            List<string> frutas = new List<string> { "manzana", "platano", "cereza" };
            Console.WriteLine("Original: " + string.Join(", ", frutas));

            // Inserción
            frutas.Add("durazno"); // al final
            frutas.Insert(1, "pera"); // en posición 1
            Console.WriteLine("Después de Add e Insert: " + string.Join(", ", frutas));

            // Actualización
            frutas[2] = "mango";
            Console.WriteLine("Actualizado índice 2 a 'mango': " + string.Join(", ", frutas));

            // Borrado
            frutas.Remove("platano"); // por valor
            frutas.RemoveAt(0); // por índice
            Console.WriteLine("Después de Remove('platano') y RemoveAt(0): " + string.Join(", ", frutas));

            // Ordenación
            frutas.Sort();
            Console.WriteLine("Ordenado: " + string.Join(", ", frutas));

            // Orden descendente con LINQ, no modifica la lista original
            var descendente = frutas.OrderByDescending(f => f).ToList();
            Console.WriteLine("Orden descendente (con LINQ): " + string.Join(", ", descendente));
            Console.WriteLine();
        }

        // 3. DICTIONARY<TKey, TValue>
        static void EjemploDictionary()
        {
            Dictionary<string, int> edades = new Dictionary<string, int>
            {
                { "Ana", 25 },
                { "Luis", 30 },
                { "Carlos", 22 }
            };
            Console.WriteLine("Original:");
            foreach (var kv in edades)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");

            // Inserción
            edades.Add("Marta", 28);
            // O con índice: edades["Marta"] = 28;
            Console.WriteLine("Después de Add Marta: ");
            foreach (var kv in edades)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");

            // Actualización
            edades["Luis"] = 31;
            Console.WriteLine("Después de actualizar Luis a 31: ");
            foreach (var kv in edades)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");

            // Borrado
            edades.Remove("Carlos");
            Console.WriteLine("Después de Remove Carlos: ");
            foreach (var kv in edades)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");

            // No hay Sort en Dictionary, uso LINQ para mostrar ordenado
            var ordenadoPorClave = edades.OrderBy(kv => kv.Key);
            Console.WriteLine("Ordenado por clave (LINQ):");
            foreach (var kv in ordenadoPorClave)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");

            var ordenadoPorValor = edades.OrderBy(kv => kv.Value);
            Console.WriteLine("Ordenado por valor (LINQ):");
            foreach (var kv in ordenadoPorValor)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");
            Console.WriteLine();
        }

        // 4. HASHSET<T>
        static void EjemploHashSet()
        {
            HashSet<int> conjunto = new HashSet<int> { 1, 2, 3, 4, 5 };
            Console.WriteLine("Original: " + string.Join(", ", conjunto));

            // Inserción
            conjunto.Add(6);
            conjunto.Add(3); // duplicado, no se añade
            Console.WriteLine("Después de Add(6) y Add(3): " + string.Join(", ", conjunto));

            // Borrado
            conjunto.Remove(4);
            Console.WriteLine("Después de Remove(4): " + string.Join(", ", conjunto));

            // No existe actualización directa, hay que borrar y añadir
            conjunto.Remove(2);
            conjunto.Add(20);
            Console.WriteLine("Para 'actualizar' 2→20: Remove(2) y Add(20): " + string.Join(", ", conjunto));

            // No tiene orden; para mostrarlo ordenado usamos LINQ
            var ordenado = conjunto.OrderBy(x => x);
            Console.WriteLine("Mostrar ordenado con LINQ: " + string.Join(", ", ordenado));
            Console.WriteLine();
        }

        // 5. QUEUE<T>
        static void EjemploQueue()
        {
            Queue<string> cola = new Queue<string>();
            cola.Enqueue("primero");
            cola.Enqueue("segundo");
            cola.Enqueue("tercero");
            Console.WriteLine("Original: " + string.Join(", ", cola));

            // Inserción (Enqueue)
            cola.Enqueue("cuarto");
            Console.WriteLine("Después de Enqueue('cuarto'): " + string.Join(", ", cola));

            // Borrado (Dequeue)
            string eliminado = cola.Dequeue();
            Console.WriteLine($"Dequeue saca: '{eliminado}'. Resto: " + string.Join(", ", cola));

            // No se puede actualizar directamente, habría que Dequeue, modificar y Enqueue
            // Ejemplo: sacar "segundo" y reinsertar "SEGUNDO"
            Console.WriteLine("Queue no admite actualización directa ni ordenación.");

            // Ordenación no tiene sentido en Queue, voy a convertir a List y ordenar
            var listaOrdenada = cola.OrderBy(x => x).ToList();
            Console.WriteLine("Ordenado (convirtiendo a List): " + string.Join(", ", listaOrdenada));
            Console.WriteLine();
        }

        // 6. STACK<T>
        static void EjemploStack()
        {
            Stack<int> pila = new Stack<int>();
            pila.Push(10);
            pila.Push(20);
            pila.Push(30);
            Console.WriteLine("Original: " + string.Join(", ", pila));

            // Inserción (Push)
            pila.Push(40);
            Console.WriteLine("Después de Push(40): " + string.Join(", ", pila));

            // Borrado (Pop)
            int sacado = pila.Pop();
            Console.WriteLine($"Pop saca: {sacado}. Resto: " + string.Join(", ", pila));

            // Actualización no directa igual que Queue no tiene acceso por índice
            Console.WriteLine("Stack no admite actualización directa ni ordenación.");

            // Ordenación, hay que convertir a List
            var ordenado = pila.OrderBy(x => x).ToList();
            Console.WriteLine("Ordenado (convirtiendo a List): " + string.Join(", ", ordenado));
            Console.WriteLine();
        }

        // 7. LINKEDLIST<T>
        static void EjemploLinkedList()
        {
            LinkedList<string> listaEnlazada = new LinkedList<string>();
            listaEnlazada.AddLast("nodo1");
            listaEnlazada.AddLast("nodo2");
            listaEnlazada.AddLast("nodo3");
            Console.WriteLine("Original: " + string.Join(", ", listaEnlazada));

            // Inserción
            listaEnlazada.AddFirst("nodo0");
            listaEnlazada.AddBefore(listaEnlazada.Find("nodo3"), "nodo2.5");
            Console.WriteLine("Después de AddFirst y AddBefore: " + string.Join(", ", listaEnlazada));

            // Actualización
            var nodo = listaEnlazada.Find("nodo2");
            if (nodo != null)
                listaEnlazada.AddBefore(nodo, "nodo1.5"); // no se puede reemplazar el valor directamente, hay que eliminar y agregar
            // El valor se puede cambiar mediante la propiedad Value
            var nodo2 = listaEnlazada.Find("nodo2");
            if (nodo2 != null)
                nodo2.Value = "nodo2_modificado";
            Console.WriteLine("Después de modificar 'nodo2' a 'nodo2_modificado': " + string.Join(", ", listaEnlazada));

            // Borrado
            listaEnlazada.Remove("nodo1.5");
            Console.WriteLine("Después de Remove('nodo1.5'): " + string.Join(", ", listaEnlazada));

            // LinkedList no tiene Sort, convierto a List
            var ordenado = listaEnlazada.OrderBy(x => x).ToList();
            Console.WriteLine("Ordenado (LINQ): " + string.Join(", ", ordenado));
            Console.WriteLine();
        }

        // 8. SORTEDDICTIONARY<TKey, TValue> 
        static void EjemploSortedDictionary()
        {
            SortedDictionary<string, int> sorted = new SortedDictionary<string, int>
            {
                { "zebra", 10 },
                { "alfa", 20 },
                { "beta", 15 }
            };
            Console.WriteLine("Original ya ordenado por clave:");
            foreach (var kv in sorted)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");

            // Inserción
            sorted.Add("gamma", 25);
            Console.WriteLine("Después de Add gamma:");
            foreach (var kv in sorted)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");

            // Actualización
            sorted["beta"] = 99;
            Console.WriteLine("Después de actualizar beta a 99:");
            foreach (var kv in sorted)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");

            // Borrado
            sorted.Remove("alfa");
            Console.WriteLine("Después de Remove alfa:");
            foreach (var kv in sorted)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");

            // Ya esta ordenado por clave, por valor usamos LINQ
            var porValor = sorted.OrderBy(kv => kv.Value);
            Console.WriteLine("Ordenado por valor (LINQ):");
            foreach (var kv in porValor)
                Console.WriteLine($"  {kv.Key}: {kv.Value}");
            Console.WriteLine();
        }
    }

    public class DificultadExtra
    {
        Dictionary<string,string> MiListaDeContactos = new Dictionary<string,string>();


        public void ProgramaListaDeContactos(){
        char key;
        sbyte option;
        bool result;

        Console.WriteLine("---Lista de contactos---");
        do{
            Console.WriteLine("Que operacion desea hacer:\n" +
            "Agregar(1)\n"+
            "Buscar(2)\n"+
            "Actualizar(3)\n"+
            "Eliminar(4)\n"+
            "No hacer nada(0)\n"+
            "Opcion: ");
            string optionInput = Console.ReadLine();
            if (!sbyte.TryParse(optionInput, out option))
            {
                option = -1;
            }

                switch (option)
                {
                    case 1: 
                    result = Agregar(); 
                     if (result)
                {
                    Console.WriteLine("Tarea completada");
                }else
                {
                    Console.WriteLine("Ha ocurrido un error o usted ha decidido salir.");
                } 
                break;
                    
                    case 2: 
                    result = Buscar(); 
                     if (result)
                {
                    Console.WriteLine("Tarea completada");
                }
                break;
                    case 3: 
                    result = Actualizar(); 
                     if (result)
                {
                    Console.WriteLine("Tarea completada");
                }
                break;
                    case 4: 
                    result = Eliminar(); 
                     if (result)
                {
                    Console.WriteLine("Tarea completada");
                }else
                {
                    Console.WriteLine("Ha ocurrido un error o usted ha decidido salir.");
                } 
                break;
                    case 0: 
                    Console.WriteLine("Ha decidido salir del programa");
                    key = 'n';
                    break;
                    default:
                    Console.WriteLine("Opcion no valida");
                    break;
                }

               
        if (option != 0)
        {
            Console.WriteLine("Desea realizar alguna otra operacion (S/N):");
            var response = Console.ReadLine();
            key = !string.IsNullOrEmpty(response) ? response[0] : 'n';
        }
        }while (key == 's' || key == 'S');


        }

        private bool Agregar()
        {
            char key;
            sbyte option;
            string nombre;
            string numero;

            do{
            Console.WriteLine("Diga el nombre del contacto: ");
            nombre = Console.ReadLine();
            Console.WriteLine("Diga el numero de telefono: ");
            numero = Console.ReadLine();
            if (string.IsNullOrWhiteSpace(nombre))
                {
                    Console.WriteLine("El nombre del contacto no puede estar vacio");
                    Console.WriteLine("Volver a intentar(1)\n"+
                    "Salir(0)\n"+
                    "Que desea hacer: ");
                    string optionInput = Console.ReadLine();
                    if (!sbyte.TryParse(optionInput, out option))
                    {
                        option = 1;
                    }
                    if(option == 0)
                    {
                        return false;
                    }else
                    {
                        key = 's';
                    }
                }
                else if (string.IsNullOrWhiteSpace(numero))
                {
                    Console.WriteLine("El numero de telefono no puede estar vacio");
                    Console.WriteLine("Volver a intentar(1)\n"+
                    "Salir(0)\n"+
                    "Que desea hacer: ");
                    string optionInput = Console.ReadLine();
                    if (!sbyte.TryParse(optionInput, out option))
                    {
                        option = 1;
                    }
                    if(option == 0)
                    {
                        return false;
                    }else
                    {
                        key = 's';
                    }
                }
                else if (numero.Length > 11)
                {
                    Console.WriteLine("El numero de telefono no puede tener mas de 11 digitos");
                    Console.WriteLine("Volver a intentar(1)\n"+
                    "Salir(0)\n"+
                    "Que desea hacer: ");
                    string optionInput = Console.ReadLine();
                    if (!sbyte.TryParse(optionInput, out option))
                    {
                        option = 1;
                    }
                    if(option == 0)
                    {
                        return false;
                    }else
                    {
                        key = 's';
                    }
                }
                else if (MiListaDeContactos.ContainsKey(nombre))
                {
                    Console.WriteLine("Ya existe este contacto");
                    Console.WriteLine("Volver a intentar(1)\n"+
                    "Salir(0)\n"+
                    "Que desea hacer: ");
                    string optionInput = Console.ReadLine();
                    if (!sbyte.TryParse(optionInput, out option))
                    {
                        option = 1;
                    }
                    if(option == 0)
                    {
                        return false;
                    }else
                    {
                        key = 's';
                    }
                }
                else if (!numero.All(char.IsDigit))
                        {
                            Console.WriteLine("El numero de telefono solo puede contener digitos numericos");
                            Console.WriteLine("Volver a intentar(1)\n"+
                            "Salir(0)\n"+
                            "Que desea hacer: ");
                            string optionInput = Console.ReadLine();
                            if (!sbyte.TryParse(optionInput, out option))
                            {
                                option = 1;
                            }
                            if(option == 0)
                            {
                                return false;
                            }else
                            {
                                key = 's';
                            }
                        }else
                {
                    MiListaDeContactos.Add(nombre,numero);
                    return true;
                }

        }while(key == 's');

        }

        private bool Buscar()
        {
            string nombre;
            Console.WriteLine("Diga el nombre del contacto a buscar: ");
            nombre = Console.ReadLine();

            if (MiListaDeContactos.ContainsKey(nombre))
            {
                Console.WriteLine($"El numero de {nombre} es: {MiListaDeContactos[nombre]}");
                return true;
            }else
            {
                Console.WriteLine("No se ha encontrado el contacto");
                return false;
            }
        }

        private bool Actualizar()
        {
            string nombre;
            string numero;
            sbyte option;
            Console.WriteLine("Diga el nombre del contacto a actualizar: ");
            nombre = Console.ReadLine();

            if (MiListaDeContactos.ContainsKey(nombre))
            {
                do
                {
                    Console.WriteLine("Diga el nuevo numero de telefono: ");
                    numero = Console.ReadLine();

                    if (string.IsNullOrWhiteSpace(numero))
                    {
                        Console.WriteLine("El numero de telefono no puede estar vacio");
                    }
                    else if (numero.Length > 11)
                    {
                        Console.WriteLine("El numero de telefono no puede tener mas de 11 digitos");
                    }
                    else if (!numero.All(char.IsDigit))
                    {
                        Console.WriteLine("El numero de telefono no puede contener caracteres no validos");
                    }
                    else
                    {
                        MiListaDeContactos[nombre] = numero;
                        return true;
                    }

                    Console.WriteLine("Volver a intentar(1)\n" +
                        "Salir(0)\n" +
                        "Que desea hacer: ");
                    string optionInput = Console.ReadLine();
                    if (!sbyte.TryParse(optionInput, out option))
                    {
                        option = 1;
                    }
                    if (option == 0)
                    {
                        return false;
                    }
                } while (true);
            }
            else
            {
                Console.WriteLine("No se ha encontrado el contacto");
                return false;
            }
        }

        private bool Eliminar()
        {
            string nombre;
            Console.WriteLine("Diga el nombre del contacto a eliminar: ");
            nombre = Console.ReadLine();

            if (MiListaDeContactos.ContainsKey(nombre))
            {
                MiListaDeContactos.Remove(nombre);
                return true;
            }else
            {
                Console.WriteLine("No se ha encontrado el contacto");
                return false;
            }
        }


    }
}