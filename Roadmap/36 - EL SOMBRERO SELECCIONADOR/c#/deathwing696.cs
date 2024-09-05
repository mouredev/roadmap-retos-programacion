using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.Remoting.Messaging;
using System.Text;
using System.Threading;

/*
 * EJERCICIO:
 * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
 * de programación de Hogwarts para magos y brujas del código.
 * En ella, su famoso sombrero seleccionador ayuda a los programadores
 * a encontrar su camino...
 * Desarrolla un programa que simule el comportamiento del sombrero.
 * Requisitos:
 * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
 * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
 *    (Puedes elegir las que quieras)
 * Acciones:
 * 1. Crea un programa que solicite el nombre del alumno y realice 10
 *    preguntas, con cuatro posibles respuestas cada una.
 * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 * 3. Una vez finalizado, el sombrero indica el nombre del alumno 
 *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
 *    pero indicándole al alumno que la decisión ha sido complicada).
 */

namespace Reto_36
{
    public class sortingHat
    {
        private int frontendPoints, backendPoints, mobilePoints, dataPoints;

        public int FrontendPoints { get { return frontendPoints; } }
        public int BackendPoints { get { return backendPoints; } }
        public int MobilePoints { get { return mobilePoints; } }
        public int DataPoints { get { return dataPoints; } }

        public string Name { get; set; }

        public sortingHat()
        {
            frontendPoints = 0;
            backendPoints = 0;
            mobilePoints = 0;
            dataPoints = 0;
        }

        public void AskQuestion(int number)
        {
            switch (number)
            {
                case 1:
                    AskQuestion1();
                    break;
                case 2:
                    AskQuestion2();
                    break;
                case 3:
                    AskQuestion3();
                    break;
                case 4:
                    AskQuestion4();
                    break;
                case 5:
                    AskQuestion5();
                    break;
                case 6:
                    AskQuestion6();
                    break;
                case 7:
                    AskQuestion7();
                    break;
                case 8:
                    AskQuestion8();
                    break;
                case 9:
                    AskQuestion9();
                    break;
                case 10:
                    AskQuestion10();
                    break;
                default:
                    break;
            }
        }

        private void AskQuestion1()
        {
            int response;
            Console.WriteLine("Pregunta 1: ¿Qué tecnología elegirías para desarrollar una interfaz de usuario interactiva?\r\n\r    1.React\r\n    2.Vue\r\n    3.Angular.js\r\n    4.Ni pajolera idea de lo que me hablas");
            Console.Write("Respuesta: ");
            try
            {
                response = Int16.Parse(Console.ReadLine());
            }
            catch
            {
                response = 0;
            }

            switch (response)
            {
                case 1:
                    frontendPoints += 5;
                    backendPoints += 1;
                    mobilePoints += 2;
                    dataPoints += 1;
                    break;
                case 2:
                    frontendPoints += 5;
                    backendPoints += 1;
                    mobilePoints += 1;
                    dataPoints += 2;
                    break;
                case 3:
                    frontendPoints += 4;
                    backendPoints += 2;
                    mobilePoints += 1;
                    dataPoints += 2;
                    break;
                case 4:
                    Console.WriteLine("No te preocupes, pasamos a la siguiente pregunta, verás como se te da mejor");
                    break;
                default:
                    Console.WriteLine("Respuesta incorrecta, pasamos a la siguiente pregunta");
                    break;
            }
        }

        private void AskQuestion2()
        {
            int response;
            Console.WriteLine("Pregunta 2: ¿Qué base de datos usarías para una aplicación con alta disponibilidad y escalabilidad?\r\n\r    1.MongoDB\r\n    2.PostgreSQL\r\n    3.Firebase Realtime Database\r\n    4.Ni pajolera idea de lo que me hablas");
            Console.Write("Respuesta: ");
            try
            {
                response = Int16.Parse(Console.ReadLine());
            }
            catch
            {
                response = 0;
            }


            switch (response)
            {
                case 1:
                    frontendPoints += 1;
                    backendPoints += 4;
                    mobilePoints += 2;
                    dataPoints += 3;
                    break;
                case 2:
                    frontendPoints += 1;
                    backendPoints += 4;
                    mobilePoints += 1;
                    dataPoints += 4;
                    break;
                case 3:
                    frontendPoints += 2;
                    backendPoints += 3;
                    mobilePoints += 3;
                    dataPoints += 2;
                    break;
                case 4:
                    Console.WriteLine("No te preocupes, pasamos a la siguiente pregunta, verás como se te da mejor");
                    break;
                default:
                    Console.WriteLine("Respuesta incorrecta, pasamos a la siguiente pregunta");
                    break;
            }
        }

        private void AskQuestion3()
        {
            int response;
            Console.WriteLine("Pregunta 3: ¿Qué herramienta utilizarías para control de versiones en un proyecto de desarrollo?\r\n\r    1.Git\r\n    2.Mercurial\r\n    3.Subversion\r\n    4.Ni pajolera idea de lo que me hablas");
            Console.Write("Respuesta: ");
            try
            {
                response = Int16.Parse(Console.ReadLine());
            }
            catch
            {
                response = 0;
            }

            switch (response)
            {
                case 1:
                    frontendPoints += 3;
                    backendPoints += 3;
                    mobilePoints += 2;
                    dataPoints += 2;
                    break;
                case 2:
                    frontendPoints += 2;
                    backendPoints += 2;
                    mobilePoints += 2;
                    dataPoints += 2;
                    break;
                case 3:
                    frontendPoints += 2;
                    backendPoints += 2;
                    mobilePoints += 2;
                    dataPoints += 2;
                    break;
                case 4:
                    Console.WriteLine("No te preocupes, pasamos a la siguiente pregunta, verás como se te da mejor");
                    break;
                default:
                    Console.WriteLine("Respuesta incorrecta, pasamos a la siguiente pregunta");
                    break;
            }
        }

        private void AskQuestion4()
        {
            int response;
            Console.WriteLine("Pregunta 4: ¿Cuál es tu framework preferido para desarrollo backend?\r\n\r    1.Express.js\r\n    2.Django\r\n    3.Spring Boot\r\n    4.Ni pajolera idea de lo que me hablas");
            Console.Write("Respuesta: ");
            try
            {
                response = Int16.Parse(Console.ReadLine());
            }
            catch
            {
                response = 0;
            }

            switch (response)
            {
                case 1:
                    frontendPoints += 2;
                    backendPoints += 5;
                    mobilePoints += 2;
                    dataPoints += 1;
                    break;
                case 2:
                    frontendPoints += 2;
                    backendPoints += 5;
                    mobilePoints += 1;
                    dataPoints += 2;
                    break;
                case 3:
                    frontendPoints += 1;
                    backendPoints += 5;
                    mobilePoints += 2;
                    dataPoints += 2;
                    break;
                case 4:
                    Console.WriteLine("No te preocupes, pasamos a la siguiente pregunta, verás como se te da mejor");
                    break;
                default:
                    Console.WriteLine("Respuesta incorrecta, pasamos a la siguiente pregunta");
                    break;
            }
        }

        private void AskQuestion5()
        {
            int response;
            Console.WriteLine("Pregunta 5: ¿Qué lenguaje de programación prefieres para desarrollar aplicaciones móviles?\r\n\r    1.Swift\r\n    2.Kotlin\r\n    3.JavaScript\r\n    4.Ni pajolera idea de lo que me hablas");
            Console.Write("Respuesta: ");
            try
            {
                response = Int16.Parse(Console.ReadLine());
            }
            catch
            {
                response = 0;
            }

            switch (response)
            {
                case 1:
                    frontendPoints += 2;
                    backendPoints += 1;
                    mobilePoints += 5;
                    dataPoints += 1;
                    break;
                case 2:
                    frontendPoints += 2;
                    backendPoints += 2;
                    mobilePoints += 5;
                    dataPoints += 1;
                    break;
                case 3:
                    frontendPoints += 3;
                    backendPoints += 2;
                    mobilePoints += 4;
                    dataPoints += 1;
                    break;
                case 4:
                    Console.WriteLine("No te preocupes, pasamos a la siguiente pregunta, verás como se te da mejor");
                    break;
                default:
                    Console.WriteLine("Respuesta incorrecta, pasamos a la siguiente pregunta");
                    break;
            }
        }

        private void AskQuestion6()
        {
            int response;
            Console.WriteLine("Pregunta 6: ¿Qué metodología ágil prefieres para gestionar tus proyectos de desarrollo?\r\n\r    1.Scrum\r\n    2.Kanban\r\n    3.XP (Extreme Programming)\r\n    4.Ni pajolera idea de lo que me hablas");
            Console.Write("Respuesta: ");
            try
            {
                response = Int16.Parse(Console.ReadLine());
            }
            catch
            {
                response = 0;
            }

            switch (response)
            {
                case 1:
                    frontendPoints += 3;
                    backendPoints += 3;
                    mobilePoints += 3;
                    dataPoints += 3;
                    break;
                case 2:
                    frontendPoints += 3;
                    backendPoints += 3;
                    mobilePoints += 3;
                    dataPoints += 3;
                    break;
                case 3:
                    frontendPoints += 3;
                    backendPoints += 3;
                    mobilePoints += 3;
                    dataPoints += 1;
                    break;
                case 4:
                    Console.WriteLine("No te preocupes, pasamos a la siguiente pregunta, verás como se te da mejor");
                    break;
                default:
                    Console.WriteLine("Respuesta incorrecta, pasamos a la siguiente pregunta");
                    break;
            }
        }

        private void AskQuestion7()
        {
            int response;
            Console.WriteLine("Pregunta 7: ¿Qué herramienta prefieres para pruebas automáticas en frontend?\r\n\r    1.Jest\r\n    2.Cypress\r\n    3.Mocha\r\n    4.Ni pajolera idea de lo que me hablas");
            Console.Write("Respuesta: ");
            try
            {
                response = Int16.Parse(Console.ReadLine());
            }
            catch
            {
                response = 0;
            }

            switch (response)
            {
                case 1:
                    frontendPoints += 4;
                    backendPoints += 2;
                    mobilePoints += 2;
                    dataPoints += 2;
                    break;
                case 2:
                    frontendPoints += 4;
                    backendPoints += 2;
                    mobilePoints += 2;
                    dataPoints += 2;
                    break;
                case 3:
                    frontendPoints += 4;
                    backendPoints += 2;
                    mobilePoints += 2;
                    dataPoints += 2;
                    break;
                case 4:
                    Console.WriteLine("No te preocupes, pasamos a la siguiente pregunta, verás como se te da mejor");
                    break;
                default:
                    Console.WriteLine("Respuesta incorrecta, pasamos a la siguiente pregunta");
                    break;
            }
        }

        private void AskQuestion8()
        {
            int response;
            Console.WriteLine("Pregunta 8: ¿Cuál es tu enfoque preferido para manejar la autenticación en una aplicación web?\r\n\r    1.OAuth\r\n    2.JWT (JSON Web Token)\r\n    3.Session-based\r\n    4.Ni pajolera idea de lo que me hablas");
            Console.Write("Respuesta: ");
            try
            {
                response = Int16.Parse(Console.ReadLine());
            }
            catch
            {
                response = 0;
            }

            switch (response)
            {
                case 1:
                    frontendPoints += 2;
                    backendPoints += 4;
                    mobilePoints += 2;
                    dataPoints += 2;
                    break;
                case 2:
                    frontendPoints += 2;
                    backendPoints += 4;
                    mobilePoints += 3;
                    dataPoints += 1;
                    break;
                case 3:
                    frontendPoints += 2;
                    backendPoints += 4;
                    mobilePoints += 2;
                    dataPoints += 2;
                    break;
                case 4:
                    Console.WriteLine("No te preocupes, pasamos a la siguiente pregunta, verás como se te da mejor");
                    break;
                default:
                    Console.WriteLine("Respuesta incorrecta, pasamos a la siguiente pregunta");
                    break;
            }
        }

        private void AskQuestion9()
        {
            int response;
            Console.WriteLine("Pregunta 9: ¿Qué estrategia de despliegue prefieres para tus aplicaciones?\r\n\r    1.CI/CD con Jenkins\r\n    2.GitHub Actions\r\n    3.CircleCI\r\n    4.Ni pajolera idea de lo que me hablas");
            Console.Write("Respuesta: ");
            try
            {
                response = Int16.Parse(Console.ReadLine());
            }
            catch
            {
                response = 0;
            }

            switch (response)
            {
                case 1:
                    frontendPoints += 2;
                    backendPoints += 5;
                    mobilePoints += 3;
                    dataPoints += 2;
                    break;
                case 2:
                    frontendPoints += 3;
                    backendPoints += 4;
                    mobilePoints += 3;
                    dataPoints += 2;
                    break;
                case 3:
                    frontendPoints += 3;
                    backendPoints += 4;
                    mobilePoints += 3;
                    dataPoints += 2;
                    break;
                case 4:
                    Console.WriteLine("No te preocupes, pasamos a la siguiente pregunta, verás como se te da mejor");
                    break;
                default:
                    Console.WriteLine("Respuesta incorrecta, pasamos a la siguiente pregunta");
                    break;
            }
        }

        private void AskQuestion10()
        {
            int response;
            Console.WriteLine("Pregunta 10: ¿Qué enfoque prefieres para el análisis de datos en tus aplicaciones?\r\n\r    1.Python con Pandas\r\n    2.R\r\n    3.SQL\r\n    4.Ni pajolera idea de lo que me hablas");
            Console.Write("Respuesta: ");
            try
            {
                response = Int16.Parse(Console.ReadLine());
            }
            catch
            {
                response = 0;
            }

            switch (response)
            {
                case 1:
                    frontendPoints += 1;
                    backendPoints += 2;
                    mobilePoints += 1;
                    dataPoints += 5;
                    break;
                case 2:
                    frontendPoints += 1;
                    backendPoints += 2;
                    mobilePoints += 1;
                    dataPoints += 5;
                    break;
                case 3:
                    frontendPoints += 1;
                    backendPoints += 3;
                    mobilePoints += 1;
                    dataPoints += 4;
                    break;
                case 4:
                    Console.WriteLine("No te preocupes, pasamos a la siguiente pregunta, verás como se te da mejor");
                    break;
                default:
                    Console.WriteLine("Respuesta incorrecta, pasamos a la siguiente pregunta");
                    break;
            }
        }

        internal void AsignHouse()
        {
            List<Tuple<string, int>> puntuation = new List<Tuple<string, int>>();
            puntuation.Add(new Tuple<string, int>("frontend", frontendPoints));
            puntuation.Add(new Tuple<string, int>("backend", backendPoints));
            puntuation.Add(new Tuple<string, int>("mobile", mobilePoints));
            puntuation.Add(new Tuple<string, int>("data", dataPoints));

            puntuation.Sort((x,y) =>
            {
                var result = y.Item2.CompareTo(x.Item2);

                if (result == 0)
                    result = x.Item1.CompareTo(y.Item1);

                return result;
            });

            if (puntuation.First().Item2 == puntuation.ElementAt(1).Item2)
            {
                Console.WriteLine("Ha sido una difícil elección...mmmmmm....pero creo que lo tengo...");
                Thread.Sleep(2000);
            }

            string houseName = puntuation.First().Item1;

            switch (houseName)
            {
                case "frontend":
                    Console.WriteLine($"¡Enhorabuena {Name}! Has sido asignado a la casa Frontend");
                    break;
                case "backend":
                    Console.WriteLine($"¡Enhorabuena {Name}! Has sido asignado a la casa Backend");
                    break;
                case "mobile":
                    Console.WriteLine($"¡Enhorabuena {Name}! Has sido asignado a la casa Mobile");
                    break;
                case "data":
                    Console.WriteLine($"¡Enhorabuena {Name}! Has sido asignado a la casa Data");
                    break;
            }
        }
    }
    internal class deathwing696
    {        
        static void Main(string[] args)
        {            
            sortingHat sortingHat = new sortingHat();

            Console.WriteLine("Bienvenido a Hogwarts, soy el sombrero seleccionador y voy a intentar asignarte una de las cuatro casas posibles: Frontend, Backend, Mobile o Data");
            Console.WriteLine("Te haré diez preguntas, según tus respuestas te asignaré a una de las casas anteriores, ¿Estás preparado?");
            Console.Write("Primero de nada, dime cómo te llamas:");
            sortingHat.Name = Console.ReadLine();
            Console.WriteLine($"Perfecto {sortingHat.Name}, ¡Comenzamos!");

            for (int i = 1; i < 11; i++)
            {
                sortingHat.AskQuestion(i);
            }

            sortingHat.AsignHouse();

            Console.ReadKey();
        }
    }
}
