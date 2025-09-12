/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */

namespace Roadmap
{
    internal class Reto18
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1, 2, 3, 4 };
            
            // Elemento al final de la lista
            numbers.Add(5);
            Console.WriteLine(String.Join(", ", numbers));
            
            Console.WriteLine();

            // Elemento al principio
            numbers.Insert(0, 1);
            Console.WriteLine(String.Join(", ", numbers));

            Console.WriteLine();

            // Varios elementos al final
            int[] numbers2 = [6, 7, 8, 9, 10];
            numbers.AddRange(numbers2);
            Console.WriteLine(String.Join(", ", numbers));

            Console.WriteLine();

            // Varios elementos en una posicion concreta
            int[] numbers3 = [15, 16, 17, 18];
            numbers.InsertRange(4, numbers3);
            Console.WriteLine(String.Join(", ", numbers));

            Console.WriteLine();
            
            // Eliminar elemento de una posición en concreto
            numbers.RemoveAt(3);
            Console.WriteLine(String.Join(", ", numbers));

            Console.WriteLine();
            
            // Actualizar valor en una posición concreta
            numbers[4] = 20;
            Console.WriteLine(String.Join(", ", numbers));

            Console.WriteLine();

            //Comprobar que elemento existe
            Console.WriteLine(numbers.Contains(5));

            Console.WriteLine();

            // Eliminar todos los valores de la lista
            numbers.Clear();

            // Reto extra
            HashSet<int> hashset1 = new HashSet<int>() { 1, 2, 3, 4 };
            HashSet<int> hashset2 = new HashSet<int>() { 1, 5, 3, 6, 8 };

            //Unión
            var union = hashset1.Union(hashset2);
            Console.WriteLine(string.Join(",", union));

            Console.WriteLine();

            // Intersección
            var interseccion = hashset1.Intersect(hashset2);
            Console.WriteLine(string.Join(",", interseccion));

            Console.WriteLine();

            // Diferencia
            var diferencia = hashset1.Except(hashset2);
            Console.WriteLine(string.Join(",", diferencia));
            diferencia = hashset2.Except(hashset1);
            Console.WriteLine(string.Join(",", diferencia));

            Console.WriteLine();

            // Diferencia simetrica
            hashset1.SymmetricExceptWith(hashset2);
            Console.WriteLine(string.Join(",", hashset1));

        }
    }
}
