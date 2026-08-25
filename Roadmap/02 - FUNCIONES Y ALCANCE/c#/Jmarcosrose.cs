using System;
using Microsoft.VisualBasic;

namespace Jmarcosrose {
    class Program {
        static int MyGlobalVar = 20;
        public static void Main(string[] args) {
            double num = -5.25;
            string text = "Hello World";
            string numberText = "1520";
            DateTime Today = DateTime.Now;
            int MyLocalVar = 2;
            

            Greet();
            Console.WriteLine("Function with return. " + ReturnGreet(20, 15));
            ArgGreet("James");
            DataGreet("James", 50);
            PredArgGreet(); //Muestra mensaje predeterminado.
            PredArgGreet("James");//Muestra el mensaje con el objeto del parentesis.
            DataPerson("James", 55);
            Console.WriteLine("Summ of squares is: " + Squares(3,4));
            
            //Ejemplo de variable local
            MyLocalVar++;
            Console.WriteLine("Value of my variable is: " + MyLocalVar);     
            LocalVariable();  //La varible local en la funcion no cambia a pesar del incremento
            Console.WriteLine("Now value of my variable is: " + MyLocalVar);

            //Ejemplo de variable global
            Console.WriteLine("Initial value: " + MyGlobalVar);
            MyGlobalVar++;
            GlobalVar();
            Console.WriteLine("New value: " + MyGlobalVar);

            
            //Funciones del lenguaje
            //Funciones matemáticas (System.Math)
            Console.WriteLine(Math.Abs(num));         //Devuelve 5.25
            Console.WriteLine(Math.Round(2.718281));  // Redondeo 2
            Console.WriteLine(Math.Sqrt(25));         // Raíz cuadrada 5
            Console.WriteLine(Math.Pow(5, 3));        // Potencia 125

            //Funciones String (System.String)
            Console.WriteLine(text.Contains("Hello")); // true
            Console.WriteLine(text.Substring(2, 4)); // "Hello"
            Console.WriteLine(text.Replace("Mundo", "C#")); // "  Hola C#  "

            //Funciones de conversion
            int numero = Convert.ToInt32(numberText); //Convierte el texto a numero entero
            Console.WriteLine(numero + 480);          //Convierte a numero entero + 480 = 2000

            //Funciones de fecha y hora (System.DateTime)
            Console.WriteLine(Today.ToString());      //Muestra la fecha y hora actual
            Console.WriteLine(Today.DayOfWeek);       //Muestra el día actual con letra
            Console.WriteLine(Today.AddDays(3));      //Muestra la fecha adelantada en tres días
            
            //Dificultad extra
            PrintNumber("Fizz", "Buzz");
            

        }

        //Funcion simple
        static void Greet()
        {
            Console.WriteLine("Hello, C#!!!");
        }

        //Funcion con retorno
        static int ReturnGreet(int a, int b)
        {
            return a + b;
        }

        //Funcion con un argumento
        static void ArgGreet(string name)
        {
            Console.WriteLine($"Hello, {name}");
        }

        //funcion con dos argumentos
        static void DataGreet(string name, int age)
        {
            Console.WriteLine($"Hello {name}, your age is {age}");
        }
        
        //Funcion con argumento predeterminado
        static void PredArgGreet(string name = "C#")
        {
            Console.WriteLine($"Hello, {name}");
        }

        //Funcion con un numero variable de argumentos y palabraclave
        static void DataPerson(string name, int age, string job = "Employee")
        {
            Console.WriteLine($"My name is {name}, my age is {age}, {job}");
        }

        //Funciones dentro de funciones
        static int Square(int n)
        {
            return n * n;
        }

        static int Squares(int a, int b)
        {
            return Square(a) + Square(b);
        }

        //Variable local y global
        static void LocalVariable()
        {
            int MyLocalVar = 10;
            Console.WriteLine("My local variable is: " + MyLocalVar);
        }

        static void GlobalVar()
        {
            MyGlobalVar++;
            Console.WriteLine("My value is: " + MyGlobalVar);
        }
        
        //Dificultad extra
        static int PrintNumber(string mult3, string mult5)
        {
            int cont = 0;
            
            for(int i = 1; i <= 100; i++)
            {
                if(i % 3 == 0 && i % 5 == 0)
                {
                    Console.WriteLine(mult3 + mult5);
                }
                else if(i % 3 == 0)
                {
                    Console.WriteLine(mult3);
                }
                else if(i % 5 == 0)
                {
                    Console.WriteLine(mult5);
                }
                else
                {
                    Console.WriteLine(i);
                    cont++;
                }
            }
            
            return cont;
        }
        

 
        

        
    }
}