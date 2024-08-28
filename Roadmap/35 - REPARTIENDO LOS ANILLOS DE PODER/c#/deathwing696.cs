using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse! 
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
 */

namespace Reto_35
{
    internal class deathwing696
    {
        public class ManageRings
        {
            public ManageRings()
            {
            }

            public List<int> RingSharing(int totalRings)
            {
                for (int elves = 1;  elves < totalRings; elves += 2) //Sólo números impares
                {
                    for (int dwarfs = 2; dwarfs < totalRings; dwarfs++) //Los primos empiezan a partir de 2
                    {
                        for (int humans = 2; humans < totalRings; humans += 2) // Sólo números pares
                        {
                            int sauron = 1;
                            int sum = elves + dwarfs + humans + sauron;

                            if (sum == totalRings)
                            {
                                Console.WriteLine("Reparto encontrado:");
                                Console.WriteLine($"Elfos: {elves}");
                                Console.WriteLine($"Enanos: {dwarfs}");
                                Console.WriteLine($"Hombres: {humans}");
                                Console.WriteLine($"Sauron: {sauron}");

                                var solution = new List<int>();
                                solution.Add(elves);
                                solution.Add(dwarfs);
                                solution.Add(humans);
                                solution.Add(sauron);

                                return solution;
                            }
                        }
                    }
                }

                Console.WriteLine("No se encontró un reparto válido para el número total de anillos proporcionado.");

                return null;
            }

            public bool IsPrime(int number)
            {
                if (number < 2)
                    return false;

                for (int i = 2; i < Math.Sqrt(number); i++)
                {
                    if (number % i == 0)
                        return false;
                }

                return true;
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Bienvenido al programa de gestión para el reparto de los anillos de poder.");
            Console.WriteLine("El reparto se hará según los siguientes criterios.");
            Console.WriteLine("1. Los Elfos recibirán un número impar.");
            Console.WriteLine("2. Los Enanos un número primo.");
            Console.WriteLine("3. Los Hombres un número par.");
            Console.WriteLine("4. Sauron siempre uno.");
            Console.Write("Introduce el númeor de anillos que desea repartir: ");
            var totalRings = Int16.Parse(Console.ReadLine());

            ManageRings rings = new ManageRings();
            rings.RingSharing(totalRings);
            Console.WriteLine("Adiós!");

            Console.ReadKey();
        }
    }
}
