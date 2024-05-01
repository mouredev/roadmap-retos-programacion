using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Conjuntos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * EJERCICIO:
             * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
             * operaciones (debes utilizar una estructura que las soporte):*/
            List<string> conjuntos = new List<string>();
            conjuntos.Add("casa");
            conjuntos.Add("coche");
            conjuntos.Add("llaves");

            List<string> conjuntos2 = new List<string>();
            conjuntos2.Add("casa2");
            conjuntos2.Add("coche");
            conjuntos2.Add("llaves2");

            List<string> conjuntos3 = new List<string>();
            conjuntos3.Add("casa3");
            conjuntos3.Add("coche3");
            conjuntos3.Add("llaves3");

            List<string> conjuntos4 = new List<string>();
            conjuntos4.Add("casa4");
            conjuntos4.Add("coche4");
            conjuntos4.Add("llaves4");

            /* - Añade un elemento al final.*/
            conjuntos.Add("final");            

            /* - Añade un elemento al principio.*/
            conjuntos.Insert(0, "principio");
            
            /* - Añade varios elementos en bloque al final.*/
            conjuntos.AddRange(conjuntos2);

            /* - Añade varios elementos en bloque en una posición concreta.*/
            conjuntos.InsertRange(3, conjuntos3);//pendiente de que lo inserte en una posición concreta
            
            /* - Elimina un elemento en una posición concreta.*/            
            conjuntos.RemoveRange(1, 1);//borra 1 elemento (casa) que esta en la posición 1

            /* - Actualiza el valor de un elemento en una posición concreta.*/
            conjuntos[5] = "Posicion actualizada 5";
            /* - Comprueba si un elemento está en un conjunto.*/
            if (conjuntos.IndexOf("casa2") != -1)
            {
                Console.WriteLine("El elemento está en la posición " + (conjuntos.IndexOf("casa2") + 1));
            }
            else 
            {
                Console.WriteLine("El elemento no está en la lista");
            }

            /* - Elimina todo el contenido del conjunto.*/
            conjuntos4.RemoveRange(0, (conjuntos4.Count() - 1));            

            /*
            /* DIFICULTAD EXTRA (opcional):
            /* Muestra ejemplos de las siguientes operaciones con conjuntos:
            /* - Unión.*/
            conjuntos2 = conjuntos2.Concat(conjuntos4).ToList();

            /* - Intersección.*/
            IEnumerable<string> both = conjuntos.Intersect(conjuntos2);            

            /* - Diferencia.*/
            var diferencias = conjuntos.Except(conjuntos2);
            var diferencias2 = conjuntos2.Except(conjuntos);

            /* - Diferencia simétrica.*/
            var primer_conjunto = conjuntos.ToHashSet();
            primer_conjunto.SymmetricExceptWith(conjuntos2);
            var dif_simetrica = primer_conjunto.ToList();

        }
    }
}
