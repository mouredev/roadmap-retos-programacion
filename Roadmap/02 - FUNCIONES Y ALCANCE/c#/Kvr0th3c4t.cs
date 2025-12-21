//Funciones definidas por el ususario

//Simple

using System.Net.Mime;

int Sumar(int a, int b)
{
    return a + b;
}

//Sin que devuelva nada

void Saludar()
{
    Console.WriteLine("Hola");
}

//Métodos static

static string Saludo()
{
    return "Hola que tal";
}

Console.WriteLine(Saludo());

//Expresiones lambda

int Saludar(int x, int y) => x + y;

//Funciones locales

void Ejemplo()
{
    void EnElEjemplo()
    {
    }
}

//Métodos preddefinidos (built-in)

//Para strings

string ejemplo = "";

ejemplo.ToUpper();      //Mayúsculas
ejemplo.ToLower();      //Minúsculas
ejemplo.Length;         //Longitud
ejemplo.Contains();     //Contiene el parámetro
ejemplo.Replace();      //Reemplaza contenido

//Consola

Console.WriteLine();    //Print
Console.ReadLine();     //Leer input

//Matemáticas

Math.Max();     //Máximo 
Math.Min();     //Mínimo    
Math.Sqrt();    //Raíz cuadrada
Math.Pow();     //Potencia
Math.Abs();     //Valor absoluto

//Arrays/Listas

Array.Sort();   //Ordenar un array
List.Add();     //Añadir a una lista
List.Count();   //contar elementos de una lista

//conversiones

int.Parse();        //Convertir en int
Convert.ToInt32();  //Convertir a int

/*
    DIFICULTAD EXTRA:

    Crea una función que reciba dos parámtros de tipo caena de texto y retorne un número.

    * La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
        * Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
        * Si el número es múltiplo de 5, muestra la cadena e texto del segundo parámetro.
        * Si el número es múltiplo dde 3 y dde 5, muestra las dos cadenas de texto concatenadas.
    * La función retorna el número de veces uq ese ha impreso el número en lugar de los textos. 
*/

static int FizzBuzz(string Fizz, string Buzz)
{
    int contadorNum = 0;
    for (int i = 1; i < 101; i++)
    {
        if (i % 15 == 0)
        {
            Console.WriteLine(Fizz + Buzz);
        }
        else if (i % 3 == 0)
        {
            Console.WriteLine(Fizz);
        }
        else if (i % 5 == 0)
        {
            Console.WriteLine(Buzz);
        }
        else
        {
            Console.WriteLine(i);
            contadorNum++;
        }
    }
    return contadorNum;
}