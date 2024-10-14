using System

class Program
{
    //Variable global
    static string globalVar =" Yo soy la variable global"

    static void Main(string[] args)
    {
        //Llamadas a las funciones y demostracion de conceptos
        Greet();
        GreetName("Alicia");
        GreetFullName("Alicia, Luis");


        console.WriteLine(GetGreeting());
        console.WriteLine(GetGreetingName("Andrea"));
        console.WriteLine(GetGreetingFullName("Andrea, Fran"));

        OuterFuncion();

        ScopeExample();
        console.WriteLine(globalVar); // Accede a la variable global
        changeGlobalVar();
        console.WriteLine(globalVar); // Muestra el cambio global

        changeLocalVar();
        console.WriteLine(globalVar); // La variable global no cambia por changeLocalVar

        // Funciones de ejemplo ya creadas en el leguaje (Math)
        console.WriteLine(Math.Max(1, 2, 3)); // Funcion incorporada Math.Max
        console.WriteLine(Math.Min(1, 2, 3)); // Funcion incorporada Math.Min
        console.WriteLine(Math.Sqrt(16));     // Funcion incorporada Math.Sqrt
        console.WriteLine(Math.Pow(2 ,3));    // Funcion incorporada Math.Pow
    }


    // Funcion sin parametros ni retorno
    static void Greet
    {
        console.WriteLine("Hola, mundo!");
    }

    // Funcion con retorno y un parametros
    static void GreetName (string name)
    {
        console.WriteLine("Hola, "+ name +"!");
    }

    // Funcion con retorno y varios parametro
    static string GetGreetingFullName(string firstName, string lastName)
    {
        return "Hola "+ firstName + " " + lastName + "!";
    }

    // Funcion anidada (funcion dentro de una funcion)
    static void OuterFuncion()
    {
        console.WriteLine("Otra funcion");

        void InnerFuncion()
        {
            console.WriteLine("Funcion interna");
        }

        InnerFuncion();
    }

    // Ejemplo de variables globales y locales
    static void ScopeExample()
    {
        string localVar = "Soy una variable local";
        console.WriteLine(globalVar); // Accede a la variable global
        console.WriteLine(localVar);  // Accede a la variable local
    }

    static void changeGlobalVar()
    {
        globalVar = "Soy la variable global";
    }

    static void changeLocalVar()
    {
        globalVar = "Me he cambiando a global";
    }

    static void changeLocalVar()
    {
        string localVar = "Soy la variable local";
        localVar = "Me he cambiado a local";
        console.WriteLine(localVar); // Muestra el cambio local
    }
}


/*
Explicación:

Funciones sin parámetros ni retorno:
Greet: Imprime un saludo simple.

Funciones con un parámetro y sin retorno:
GreetName: Imprime un saludo con un nombre proporcionado.

Funciones con varios parámetros y sin retorno:
GreetFullName: Imprime un saludo con nombre y apellido.

Funciones con retorno y sin parámetros:
GetGreeting: Retorna un saludo simple.

Funciones con retorno y un parámetro:
GetGreetingName: Retorna un saludo con un nombre proporcionado.

Funciones con retorno y varios parámetros:
GetGreetingFullName: Retorna un saludo con nombre y apellido.

Funciones anidadas:
OuterFunction: Contiene una función InnerFunction dentro de ella.

Variables globales y locales:
globalVar: Variable global.
ScopeExample: Demuestra el acceso a variables globales y locales.
ChangeGlobalVar: Modifica la variable global.
ChangeLocalVar: Modifica una variable local.
Funciones de ejemplo ya creadas en el lenguaje:

Uso de funciones incorporadas como Math.Max, Math.Min, Math.Sqrt, y Math.Pow.

*/
