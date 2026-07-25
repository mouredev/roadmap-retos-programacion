using System;
using System.IO.Compression;
using System.Runtime.Serialization.Formatters;

namespace Ejercicio_02
{
    class Program
    {
        static void Main(string[] args)
        {
            
        }
    }

    class PrimerInciso
    {
        //Crear funciones con las diferentes formas de declarar funciones en C#
        public void FuncionSinRetorno(){
            Console.WriteLine("Esta es una función sin retorno");
        }

        public int FuncionConRetorno(){
            return 5;
        }

        public void FuncionConParametros(int a, int b){
            Console.WriteLine("La suma de los parámetros es: " + (a + b));
        }

        public double FuncionConParametrosYRetorno(int a, int b){
            if(b == 0){
                throw new Exception("El segundo parámetro no puede ser cero");
            }
            return (double)a / b; //si el metodo retorna un double, se debe convertir la division 
                                  //en double usando el casting que es poner el tipo de dato entre
                                  //parentesis antes de la variable que se quiere convertir
        }
    }

    class SegundoInciso
    {
        /*Me preguntan si en mi lenguaje se pueden crear funciones dentro de otras funciones
        He de confesar que yo esto no lo sabia pero ahora lo acabo de investigar y si se puede hacer
        Voy a tratar de explicarlo con mis palabras:
        Una función local es basicamente una función que está declarada dentro del cuerpo de un método
        Esta solo es accesible desde dentro del método que la creó
        Se usa cuando quieres hacer una funcionalidad que no tiene sentido en más ningún otro
        lugar que no sea el propio método. También hay que tener en cuenta que esta solo puede usar 
        las variables locales del método o las que este reciba por parámetros. No será necesario 
        poner public, private... etc, pues está solo es accesible desde el método en el que recide
        Un ejemplo que se me ocurre es si yo quisiera recibir en un método el número de carnet de 
        identidad de una persona y quiero mediante ese número obtener la edad de la persona, yo 
        puedo para esto usar una función local
        */

        public void EjemploFuncionLocal(long carnetIdentidad)
        {
            int? edadPersona = null;

            int CalcularEdad() //Función local
            {
                long nacimiento = carnetIdentidad / 1000000000;  // Obteniendo las primeras dos cifras del carnet
                nacimiento = nacimiento > 50 ?
                1900 + nacimiento :
                2000 + nacimiento; // Convirtiendo esas dos cifras al año de nacimiento
                return (int)DateTime.Now.Year - nacimiento; // Calculando edad
            }

            Console.WriteLine("La edad de la " +
          "persona es " + edadPersona = CalcularEdad(carnetIdentidad));
        }
    }

    public class TercerInciso
    {
        public static void Ejemplo()
        {
            Console.WriteLine("Esta es una funcion ya creada en el lenguaje");
            /*
            WriteLine es un metodo (funcion) static de la clase Console. Por eso no hace falta crear 
            un objeto para poder usar dicho metodo
            */
        }
    }

    
    public class CuartoInciso
    {
        //Hay que mencionar que en C# no existen las variables globales como en C
        //Por ende solo hay variables locales o de clase
        // Lo mas parecido a una variable global segun me dijo la IA es la variable de clase
        private string Name { get; private set;} => String.Empty; //Variable de clase
        //Una variable de clase solo es accesible desde la clase donde fue declarada por metodos de dicha clase

        public CuartoInciso(string Name)
        {
            this.Name = Name; //Me sorprende la cantidad de conceptos que recuerdo de C# a pesar de que llevo 
            // meses sin programar
        }

        public void Saludo()
        {
            Console.WriteLine($"Hola! Mi nombre es {Name}"); //Puedo acceder a Name porque este es un metodo de la clase 
            double pi = Math.PI; // Esta es una variable local. Solo es accesible desde este metodo                                                 
        }
    }

    public class DificultadExtra
    {
        public static int MiFuncion(string cad1, string cad2)
        {
            int cont = 0;
            for(int i = 0; i < 100; i++)
            {
                if(i % 3 == 0 && i % 5 == 0)
                {
                    Console.WriteLine(String.Concat(cad1,cad2));
                } else if(i % 3 == 0)
                {
                    Console.WriteLine(cad1);

                } else if(i % 5 == 0)
                {
                    Console.WriteLine(cad2);
                }else
                {
                    Console.WriteLine(i);
                    
                    cont++;
                }
            }

            return cont;
        }
    }
}