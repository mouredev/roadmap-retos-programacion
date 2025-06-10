/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
* CONJUNTOS
------------------------------------------
Son una colección desordenada de elementos únicos.
*/
var mySet = new HashSet<int> { 1, 2, 3, 0 };

/*
* EJERCICIO #1:
* Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
* operaciones (debes utilizar una estructura que las soporte):

NOTA: - Algunas operaciones del ejercicio no pueden realizarse utilizando 'HashSet'.
*/

var myList = new List<string> { "a", "b", "c" };

// Añade un elemento al final.
myList.Add("d");

// Añadir un elemento al principio
myList.Insert(0, "-");

// Añadir varios elementos en bloque al final
myList.AddRange(new string[] { "e", "f" });

// Añadir varios elementos en bloque en una posición concreta
myList.InsertRange(4, new string[] { "-", ">" });

// Eliminar un elemento en una posición concreta
myList.RemoveAt(5);

// Actualizar el valor de un elemento en una posición concreta
myList[2] = "-b";

// Mostrar la lista
Console.WriteLine("Elementos de la lista:");
Console.WriteLine(string.Join(", ", myList));

// Comprueba si un elemento está en un conjunto
Console.WriteLine($"4 en conjunto: {mySet.Contains(4)}");

Console.WriteLine($"'c' en lista: {myList.Contains("c")}");

// Elimina todo el contenido del conjunto y la lista.
mySet.Clear();
myList.Clear();

/*
* EJERCICIO #2:
* Muestra ejemplos de las siguientes operaciones con conjuntos:
* - Unión.
* - Intersección.
* - Diferencia.
* - Diferencia simétrica.
*/

var set1 = new HashSet<int>() { 1, 2, 3, 4 };
var set2 = new HashSet<int>() { 3, 4, 5, 6 };

Console.WriteLine(
    $"\n* set_1: {{{string.Join(", ", set1)}}} - set_2: {{{string.Join(", ", set2)}}}");

// Unión
// Elementos que están en al menos uno de los conjuntos.
var union = new HashSet<int>(set1);
union.UnionWith(set2);
Console.WriteLine($"\n- Union: {{{string.Join(", ", union)}}}");

// Intersección
// Elementos que están en ambos conjuntos.
var intersection = new HashSet<int>(set1);
intersection.IntersectWith(set2);
Console.WriteLine($"\n- Intersection: {{{string.Join(", ", intersection)}}}");

// Diferencia
// Elementos que están en set_1 pero no en set_2
var difference = new HashSet<int>(set1);
difference.ExceptWith(set2);
Console.WriteLine($"\n- Difference: {{{string.Join(", ", difference)}}}");

// Diferencia simétrica
// Elementos que están en uno de los conjuntos pero no en ambos.
var symmetricDiff = new HashSet<int>(set1);
symmetricDiff.SymmetricExceptWith(set2);
Console.WriteLine($"\n- Symmetric Difference: {{{string.Join(", ", symmetricDiff)}}}");

