// ESTA ES UNA LINEA DE COMENTARIO. PUEDE ESTAR UBICADA AL PRINCIPIO O EN ALGUN OTRO
// LUGAR DEL CODIGO, TODO LO QUE SE ENCUENTRE A SU DERECHA SERA OMITIDO POR EL COMPILADOR

/*
    ESTO
    ES
    UN COMENTARIO 
    EN  VARIAS 
    LINEAS, TODO LO QUE SE 
    ENCUENTRE EN ESTE BLOQUE DELIMITADO POR ESTOS CARACTERES INICIALES Y FINALES
    SERA OMITIDO POR EL COMPILADOR
*/

// SITIO OFICIAL DE CSHARP: https://learn.microsoft.com/en-us/dotnet/csharp/

using System;

namespace CSharpHelloWorld
{
    class HelloWorld
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hola CSharp!");
            // VARIABLES. DEBEN SER DECLARADAS ANTES DE SER UTILIZADAS
            // * BASICAS O PRIMITIVAS: PUEDE DEFINIRSE CON EL TIPO DE DATO AL PRINCIPIO
            //   O POR INFERENCIA DEL DATOS ASIGNADO A LA VARIABLE CREADA UTILIZANDO LA
            //   PALABRA RESERVADA 'VAR'

            string miTexto1   = "esta es una variable tipo string en Csharp";
            char caracter = 'A';
            int miEntero1     = 10;
            long numeroLargo = 1234567890123456L;
            short numeroCorto = 12323;
            byte numeroByte = 211;
            float miFlotante1 = 10.5f;
            double miDoble1   = 10.99999;
            decimal numeroDecimal = 123.456m;
            bool miBooleano1  = true; 
            Console.WriteLine("TIPOS DE VARIABLE BASICAS O PRIMITIVAS:");
            Console.WriteLine("string,int, long, byte, float,double,bool");

            Console.WriteLine("* declaracion con tipo variable / impresion sin formato");
            Console.WriteLine("string: " + miTexto1);
            Console.WriteLine("entero: " + miEntero1);
            Console.WriteLine("flotante: " + miFlotante1);
            Console.WriteLine("doble: " + miDoble1);
            Console.WriteLine("booleano: " + miBooleano1);

            var miTexto2 = "esta es una variable tipo string en Csharp";
            var miEntero2 = 10;
            var miFlotante2 = 10.5f;
            var miDoble2 = 10.99999;
            var miBooleano2 = true; 

            Console.WriteLine("* declarando con var / impresion con formato incluido");
            Console.WriteLine($"string:\t\t{miTexto2}");
            Console.WriteLine($"entero:\t\t{miEntero2}");
            Console.WriteLine($"flotante:\t{miFlotante2}");
            Console.WriteLine($"doble:\t\t{miDoble2}");
            Console.WriteLine($"booleano:\t{miBooleano2}");

            Console.WriteLine("Las constantes se declaran con la palabra reservada const");
            Console.WriteLine("seguido del tipo de dato");
            const int miConstanteNum = 10;
            const string miConstanteTexto = "CONSTANTE ALFANUMERICA";

            Console.WriteLine($"CONSTANTE NUMERICA:{miConstanteNum}");
            Console.WriteLine($"CONSTANTE ALFANUMERICA:\t{miConstanteTexto}");

            Console.WriteLine("* ESTRUCTURAS DE DATOS: array, dictionary,set,tupla");

            var miArray = new string[] {"rojo","blanco","verde"};
            Console.WriteLine($"la posicion 2 de mi array es: {miArray[2]}");

            var miDict = new Dictionary <string, int>
            {
                {"rojo",36},
                {"verde",15},
                {"azul",23}
            };

            Console.WriteLine($"la posicion 0 de mi diccionario es: {miDict["rojo"]}");

            var miSet = new HashSet <string> {"rojo","verde","azul","verde","azul"};
            Console.WriteLine(miSet); // los set no estan indexados, tampoco se admiten repetidos

            var miTuple = ("rojo","verde","azul");
            Console.WriteLine(miTuple); // no indexados, permiten visualizar todo el contenido
        }
    }
}