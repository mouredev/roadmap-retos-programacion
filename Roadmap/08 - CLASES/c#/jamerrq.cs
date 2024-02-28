using System;

namespace Roadmap08
{
    class Example
    {
        // Atributos
        private string message;
        // Propiedades
        public string Message
        {
            get { return message; }
            set { message = value; }
        }
        // Constructor
        public Example(string message)
        {
            this.message = message;
        }
        // Funciones
        public void PrintMessage()
        {
            Console.WriteLine(message);
        }
        // Main
        static void Main(string[] args)
        {
            Example example = new Example("Hello, C#!");
            example.PrintMessage();
            example.Message = "Goodbye, Julia!";
            example.PrintMessage();
        }
    }
}
