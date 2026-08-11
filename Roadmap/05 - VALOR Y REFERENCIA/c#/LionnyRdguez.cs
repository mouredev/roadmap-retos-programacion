using System;

namespace Ejercicio_05
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Intercambio de valores por valor:");
            DificultadExtra dificultadExtra = new DificultadExtra();

            int a = 5, b = 10;
            Console.WriteLine($"Antes del intercambio: a = {a}, b = {b}");

            int[] intercambioValor = dificultadExtra.IntercambiarValoresPorValor(a, b);
            int aNuevo = intercambioValor[0];
            int bNuevo = intercambioValor[1];

            Console.WriteLine($"Nuevo valor de las variables: a = {aNuevo}, b = {bNuevo}");
            Console.WriteLine($"Valores originales después del intercambio: a = {a}, b = {b}");

            Console.WriteLine("\nIntercambio de referencias por referencia:");
            List<int> lista1 = new List<int> { 5 };
            List<int> lista2 = new List<int> { 10 };
            Console.WriteLine($"Antes del intercambio: lista1 = [{string.Join(", ", lista1)}], lista2 = [{string.Join(", ", lista2)}]");

            List<int>[] intercambioReferencias = dificultadExtra.IntercambiarValoresPorReferencia(ref lista1, ref lista2);
            List<int> lista1Nueva = intercambioReferencias[0];
            List<int> lista2Nueva = intercambioReferencias[1];

            Console.WriteLine($"Nuevas referencias devueltas: lista1Nueva = [{string.Join(", ", lista1Nueva)}], lista2Nueva = [{string.Join(", ", lista2Nueva)}]");
            Console.WriteLine($"Referencias originales después del intercambio: lista1 = [{string.Join(", ", lista1)}], lista2 = [{string.Join(", ", lista2)}]");

            Console.WriteLine("Comprobación de identidad de las referencias:");
            Console.WriteLine($"lista1Nueva apunta a la referencia original de lista2: {ReferenceEquals(lista1Nueva, lista2)}");
            Console.WriteLine($"lista2Nueva apunta a la referencia original de lista1: {ReferenceEquals(lista2Nueva, lista1)}");
            Console.WriteLine($"lista1 conserva su valor original: {lista1[0] == 10}");
            Console.WriteLine($"lista2 conserva su valor original: {lista2[0] == 5}");
        }

        public static void PrimerInciso()
        {
            //Asignacion de variables por valor
            int a = 10;
            int b = a;
            b = 20;
            Console.WriteLine("Valor de a: " + a); // Imprime 10. a no se ve afectado por el cambio en b

            //Asignacion de variables por referencia
            int[] arrayA = { 1, 2, 3 };
            int[] arrayB = arrayA;
            arrayB[0] = 10;
            Console.WriteLine("Valor de arrayA[0]: " + arrayA[0]); // Imprime 10. arrayA se ve afectado por el cambio en arrayB

            // Hay una diferencia en el caso de strings, ya que son inmutables, 
            // por lo que no se puede cambiar su valor directamente. Aunque sean un tipo de referencia 

            string strA = "Hola";
            string strB = strA;
            strB = "Mundo";
            Console.WriteLine("Valor de strA: " + strA); // Imprime "Hola". strA no se ve afectado por el cambio en strB

        }

        public static void SegundoInciso()
        {
           //Ejemplo de funcion que recibe un parametro por valor
            void IncrementarPorValor(int numero)
            {
                numero++;
            }

            int valor = 5;
            IncrementarPorValor(valor);
            Console.WriteLine("Valor después de IncrementarPorValor: " + valor); // Imprime 5. El valor 
            // original no se ve afectado

            //Ejemplo de funcion que recibe un parametro por referencia
            void IncrementarPorReferencia(ref int numero)
            {
                numero++;
            }
            //En C# al usar ref , se pasa la referencia de la variable, por lo que cualquier cambio en el 
            // parámetro afectará a la variable original. También se puede usar out, que es similar a ref, 
            // pero requiere que la variable sea inicializada antes de ser pasada a la función. Esto sirve para 
            // indicar que la función va a devolver un valor a través de ese parámetro.

            int valorRef = 5;
            IncrementarPorReferencia(ref valorRef);
            Console.WriteLine("Valor después de IncrementarPorReferencia: " + valorRef); // Imprime 6. El valor 
            // original se ve afectado

            //Ejemplo con lista 

            List<int> numeros = new List<int> { 1, 2, 3 };
            AgregarElemento(numeros);
            void AgregarElemento(List<int> lista)
            {
                lista.Add(4);
            }
            // La lista original se ve afectada, ya que se pasa por referencia
            Console.WriteLine("Lista después de AgregarElemento: " + string.Join(", ", numeros)); // Imprime 1, 2, 
            // 3, 4.

            //Ejemplo de reasignacion de referencia
            List<int> numeros2 = new List<int> { 1, 2, 3 };
            ReasignarReferencia(numeros2);
            void ReasignarReferencia(List<int> lista)
            {
                lista = new List<int> { 4, 5, 6 }; // Se crea una nueva lista y se asigna a la variable local
            }
            // La lista original no se ve afectada, ya que la referencia se reasignó a una nueva lista
            Console.WriteLine("Lista después de ReasignarReferencia: " + string.Join(", ", numeros2)); // Imprime
            //  1, 2, 3.
            //En resumen, cuando se pasa un parámetro por valor, se crea una copia del valor original y cualquier 
            // cambio en el parámetro no afectará al valor original.
            //Cuando se pasa un parámetro por referencia, se pasa la referencia del valor original y 
            // cualquier cambio en el parámetro afectará al valor original. Sin embargo, si se reasigna la 
            // referencia a una nueva variable dentro de la función, la variable original no se verá afectada.
            //Si se desea que la variable original se vea afectada incluso si se reasigna la referencia, 
            // se puede usar el modificador ref en la declaración del parámetro de la función. Esto indica que
            // se está pasando la referencia de la variable original y cualquier cambio en el parámetro afectará
            // a la variable original, incluso si se reasigna la referencia a una nueva variable dentro
            // de la función.
            //Con parametros por valor si se usa ref, se pasa la referencia de la variable original y cualquier 
            // cambio en el parámetro afectará a la variable original.
        
        }

    
    }

    public partial class DificultadExtra
    {
        public int[] IntercambiarValoresPorValor(int a, int b)
        {
            int temp = a;
            a = b;
            b = temp;
            return new int[] { a, b };
        }
    }

    public partial class DificultadExtra
    {
        public List<int>[] IntercambiarValoresPorReferencia(ref List<int> lista1, ref List<int> lista2)
        {
            List<int> temp = lista1;
            lista1 = lista2;
            lista2 = temp;

            return new List<int>[] { lista1, lista2 };
        }
    }
}