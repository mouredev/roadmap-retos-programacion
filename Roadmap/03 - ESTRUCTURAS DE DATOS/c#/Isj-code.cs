
// ## Ejercicio, se hace con las colecciones mas usadas, Hash está en desuso dicho por la documentacion oficial.
// Basadas en IList
// Array

int[] array = { 1, 2, 3, 4, 5 };
Console.WriteLine("----- Array -----");
Console.WriteLine("Array base a trabajar");
foreach (var item in array)
{
    Console.Write($"{item} ");
}

// Operaciones con array
Console.WriteLine($"la longitud del array es {array.Length}");
// Cambio de dato explicito
array[0] = 0;
Console.WriteLine("Cambio del primer valor");
foreach (var item in array)
{
    Console.Write($"{item} ");
}

Console.WriteLine("");
// Primer valor
Console.WriteLine($"El primer valor es {array.First()}");
// Añadimos al final
Console.WriteLine("Métodos sin modificar el array original");
var arrayMas = array.Append(5);
Console.WriteLine("Añadimos otro 5 al final");
foreach (var item in arrayMas)
{
    Console.Write($"{item} ");
}

Console.WriteLine(" ");
// Hacer el reverso
Console.WriteLine("Reverse");
var arrayRev = array.Reverse();
foreach (var item in arrayRev)
{
    Console.Write($"{item} ");
}

Console.WriteLine(" ");
// Pasamos el array a uno nuevo que sea un lista para hacer otro tipo de operaciones
Console.WriteLine("Pasamos el array a lista");
List<int> listaNumeros = array.ToList();
Console.WriteLine("----- Lista -----");
foreach (var item in listaNumeros)
{
    Console.Write($"{item} ");
}
// Borrado de una posicion en concreto
Console.WriteLine("Borramos el indice 0");
listaNumeros.RemoveAt(0);
foreach (var item in listaNumeros)
{
    Console.Write($"{item} ");
}

Console.WriteLine("");
Console.WriteLine("Recorte de 2 posiciones, desde cero 2 posiciones");
var listaRecorte = listaNumeros.Slice(0, 2);
foreach (var item in listaRecorte)
{
    Console.Write($"{item} ");
    
}

Console.WriteLine("");
// Añadimos un rango de varios números de una lista
Console.WriteLine("Añadimos un rango de nuemeros");
listaNumeros.AddRange([4,2,1,2,3]);
foreach (var item in listaNumeros)
{
    Console.Write($"{item} ");
}

Console.WriteLine("");
// Sort() para ordenar
Console.WriteLine("Ordenamos son Sort");
listaNumeros.Sort();
foreach (var item in listaNumeros)
{
    Console.Write($"{item} ");
}
Console.WriteLine("");
// Busqueda dentro de la lista
Console.WriteLine("Busqueda del primer numero 1, en una lista de valores primitivos no es muy útil pero en lista de objetos es muy útil");
var resp = listaNumeros.FirstOrDefault((i) => i == 1);
Console.WriteLine(resp);

// Limpieza de la lista
Console.WriteLine("Vaciamos la lista");
listaNumeros.Clear();

// Dictionary con key int y valor string

// Declaracion
Console.WriteLine("----- Diccionario -----");
Dictionary<int, string> dictionary = new Dictionary<int, string>();

// Añadir al dicionario
dictionary.Add(1,"Jose");
dictionary.Add(3,"Pepito");
dictionary.Add(4,"Luisita");
dictionary.Add(5,"Maribel");

foreach (var item in dictionary)
{
    Console.WriteLine($"Key: {item.Key} tiene de valor: {item.Value}");
}

var respDic = dictionary.FirstOrDefault((t) => t.Key == 1);
Console.WriteLine($"La busqueda con clave 1 es: {respDic.Value}");

// Borrado
dictionary.Remove(3);
Console.WriteLine("Borrado del key 3");
foreach (var item in dictionary)
{
    Console.WriteLine($"Key: {item.Key} tiene de valor: {item.Value}");
}

Console.WriteLine("AHora vamos a buscar todos los valores que tengan una i");
var respWhere = dictionary.Where(t => t.Value.Contains("i"));
foreach (var item in respWhere)
{
    Console.WriteLine($"Key: {item.Key} tiene de valor: {item.Value}");
}

Console.WriteLine("Se ve que Jose no está en la lista");

// ## Dificultad Extra (opcional)
Console.WriteLine("-----------------------");
Console.WriteLine("--- Ejercicio opcional ---");
Console.WriteLine("-----------------------");

Dictionary<string, int> agenda = new Dictionary<string, int>();
var entrada = "";

do
{
    Console.WriteLine("Elige una opción");
    Console.WriteLine("c-Crear");
    Console.WriteLine("a-Actualizar");
    Console.WriteLine("d-Borrar");
    Console.WriteLine("f-Buscar");
    Console.WriteLine("x-Salir");
    entrada = Console.ReadLine().ToUpper();
    if (entrada != "C" && entrada != "A" && entrada != "D" & entrada != "F" && entrada != "X")
    {
        Console.WriteLine("Eleccion Incorrecta, vuelva a elegir");
    }
    else
    {
        var name = "";
        int tlf;
        switch (entrada)
        {
            case "C":
                Console.WriteLine("Añada el nombre:");
                name = Console.ReadLine().ToUpper().TrimEnd().TrimStart();
                Console.WriteLine("Añada el número, solo 9 digitos ");
                string? numeroTlf = Console.ReadLine();
                if (numeroTlf != null && name.Length > 0)
                {
                    var sol = int.TryParse(numeroTlf, out tlf);
                    if (sol == true && numeroTlf.Length < 9)
                    {
                        agenda.Add(name, tlf);
                    }
                    else
                    {
                        Console.WriteLine("Ingresa los datos correctos, vuelva a empezar.");
                    }
                }
                break;
            case "F":
                Console.WriteLine("Ingrese el contacto a buscar: ");
                string nombreBusqueda = Console.ReadLine().TrimStart().ToUpper().TrimEnd();
                if (nombreBusqueda != null)
                {
                    var respBusqueda = agenda.FirstOrDefault(t => t.Key == nombreBusqueda);
                    if (respBusqueda.Key != null)
                    {
                        Console.WriteLine($"El nombre {respBusqueda.Key} tiene el telefono {respBusqueda.Value}");
                    }
                    else
                    {
                        Console.WriteLine("Nombre erroneo o inexistente, intentelo de nuevo");
                    }
                }
                else
                {
                    Console.WriteLine("Nombre erroneo o inexistente, intentelo de nuevo");
                }

                break;
            case "D":
                Console.WriteLine("Ingrese el contacto a Borrar");
                var contactoBorrar = Console.ReadLine().ToUpper().TrimStart().TrimEnd();
                if (contactoBorrar != null)
                {
                    var respDelete = agenda.Remove(contactoBorrar);
                    if (!respDelete)
                    {
                        Console.WriteLine("Contacto no econtrado");
                    }
                    else
                    {
                        Console.WriteLine("Contacto Borrado");
                    }
                }
                break;
            case "A":
                Console.WriteLine("Ingrese el contacto a Modificar");
                var respMod = Console.ReadLine().ToUpper().TrimEnd().TrimStart();
                if (respMod != null)
                {
                    var findMod = agenda.FirstOrDefault((t) => t.Key == respMod);
                    if (findMod.Key != null)
                    {
                        Console.WriteLine("Indique su nuevo numero");
                        string stringTlf = Console.ReadLine().Trim();
                        int nuevoTlf;
                        bool respConvert = int.TryParse(stringTlf, out nuevoTlf);
                        if (respConvert)
                        {
                            agenda[findMod.Key] = nuevoTlf; 
                        }

                        Console.WriteLine("Numero erroneo, pruebe otra vez");
                    }
                    else
                    {
                        Console.WriteLine("Nombre no encontrado");
                    }
                }
                break;
        }
    }
} while (!entrada.Equals("X"));


