/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */

using System;

namespace Roadmap22
{
    class SuperFunctions
    {
        public static double Average(double[] numbers)
        {
            double sum = 0;
            foreach (double number in numbers)
            {
                sum += number;
            }
            return sum / numbers.Length;
        }

        public static double Max(double[] numbers)
        {
            double max = numbers[0];
            foreach (double number in numbers)
            {
                if (number > max)
                {
                    max = number;
                }
            }
            return max;
        }

        public static double Min(double[] numbers)
        {
            double min = numbers[0];
            foreach (double number in numbers)
            {
                if (number < min)
                {
                    min = number;
                }
            }
            return min;
        }

        public static double[] Filter(double[] numbers, Func<double, bool> condition)
        {
            int count = 0;
            foreach (double number in numbers)
            {
                if (condition(number))
                {
                    count++;
                }
            }

            double[] result = new double[count];
            int index = 0;
            foreach (double number in numbers)
            {
                if (condition(number))
                {
                    result[index] = number;
                    index++;
                }
            }

            return result;
        }

        public static double[] Map(double[] numbers, Func<double, double> operation)
        {
            double[] result = new double[numbers.Length];
            for (int i = 0; i < numbers.Length; i++)
            {
                result[i] = operation(numbers[i]);
            }
            return result;
        }

        public static double[] Reduce(double[] numbers, Func<double, double, double> operation)
        {
            double result = numbers[0];
            for (int i = 1; i < numbers.Length; i++)
            {
                result = operation(result, numbers[i]);
            }
            return new double[] { result };
        }

        public static void Main(string[] args)
        {
            double[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

            Console.WriteLine("Average: " + Average(numbers));
            Console.WriteLine("Max: " + Max(numbers));
            Console.WriteLine("Min: " + Min(numbers));

            double[] evenNumbers = Filter(numbers, number => number % 2 == 0);
            Console.WriteLine("Even numbers: " + string.Join(", ", evenNumbers));

            double[] squaredNumbers = Map(numbers, number => number * number);
            Console.WriteLine("Squared numbers: " + string.Join(", ", squaredNumbers));

            double[] sum = Reduce(numbers, (a, b) => a + b);
            Console.WriteLine("Sum: " + sum[0]);
        }
    }
}
