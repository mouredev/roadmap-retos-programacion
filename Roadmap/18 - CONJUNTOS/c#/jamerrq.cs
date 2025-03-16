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

using System;

namespace Roadmap18
{
    class Sets
    {
        static void Main(string[] args)
        {
            // Creamos un conjunto de datos
            int[] set = [];

            // Añadimos un elemento al final
            Array.Resize(ref set, set.Length + 1);
            set[^1] = 1;

            // Añadimos un elemento al principio
            Array.Resize(ref set, set.Length + 1);
            Array.Copy(set, 0, set, 1, set.Length - 1);
            set[0] = 2;

            // Añadimos varios elementos al final
            int[] newElements = [3, 4, 5];
            Array.Resize(ref set, set.Length + newElements.Length);
            Array.Copy(newElements, 0, set, set.Length - newElements.Length, newElements.Length);

            // Añadimos varios elementos en una posición concreta
            int[] newElements2 = [6, 7, 8];
            int position = 2;
            Array.Resize(ref set, set.Length + newElements2.Length);
            Array.Copy(set, position, set, position + newElements2.Length, set.Length - position - newElements2.Length);
            Array.Copy(newElements2, 0, set, position, newElements2.Length);

            // Eliminamos un elemento en una posición concreta
            position = 3;
            Array.Copy(set, position + 1, set, position, set.Length - position - 1);
            Array.Resize(ref set, set.Length - 1);

            // Actualizamos el valor de un elemento en una posición concreta
            position = 2;
            set[position] = 9;

            // Comprobamos si un elemento está en un conjunto
            int element = 5;
            bool contains = Array.Exists(set, e => e == element);
            Console.WriteLine("El conjunto contiene el elemento " + element + ": " + contains);

            // Eliminamos todo el contenido del conjunto
            Array.Resize(ref set, 0);

            // Mostramos el contenido del conjunto
            Console.WriteLine("Contenido del conjunto:");
            foreach (int e in set)
            {
                Console.WriteLine(e);
            }
        }
    }
}
