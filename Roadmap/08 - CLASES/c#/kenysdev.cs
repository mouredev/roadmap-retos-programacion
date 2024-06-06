/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
# CLASES
------------------------------------------
- Las clases proporcionan una forma de organizar y estructurar
  el código de manera más modular y reutilizable. */

class Program{
   public class Person{
      // Propiedades
      public string Name { get; set; }
      public int Age { get; set; }

      //Constructor
      public Person(string name, int age){
         this.Name = name;
         this.Age = age;
      }

      // Metodo
      public void Print(){
         Console.WriteLine($"Nombre: {Name} - Edad: {Age}");
      }
   }

   /*----------------------------------------
     Ejercicio:
     ----------------------------------------
   - Implementa dos clases que representen las estructuras de Pila y Cola 
     (estudiadas en el ejercicio número 7 de la ruta de estudio)
   - Deben poder inicializarse y disponer de operaciones para añadir, 
     eliminar, retornar el número de elementos e imprimir todo su contenido.
     _________________________________________
     Pilas(stack - LIFO): */
   public class MyStack{
      private Stack<object> _stack = new();

      public void Push(object item){
         _stack.Push(item);
      }

      public object? Pop(){
         if (_stack.Count > 0){
            return _stack.Pop();
         }
         else {
            return null;
         }
      }

      public int Count(){
         return _stack.Count;
      }

      public void Print(){
         if (_stack.Count > 0){
            foreach (object item in _stack){
               Console.WriteLine(item);
            }
         }
      }
   }

// _________________________________________
// Colas (Queue - FIFO):
   public class MyQueue{
      private Queue<object> _queue = new();

      public void Enqueue(object item){
         _queue.Enqueue(item);
      }

      public object? Dequeue(){
         if (_queue.Count > 0){
            return _queue.Dequeue();
         }
         else {
            return null;
         }
      }

      public int Count(){
         return _queue.Count;
      }

      public void Print(){
         if (_queue.Count > 0){
            foreach (object item in _queue){
               Console.WriteLine(item);
            }
         }
      }
   }

// _________________________________________
   static void Main(){
      // Crear objeto
      var person = new Person("Ben", 21);
      person.Print();
      person.Age = 19;
      person.Print();
      
      // --------------
      Console.WriteLine("Uso de pila:");
      var Stack = new MyStack();
      Stack.Push("uno");
      Stack.Push(22222);
      Stack.Push(false);
      Stack.Pop();
      Stack.Print();

      // --------------
      Console.WriteLine("Uso de cola:");
      var Queue = new MyQueue();
      Queue.Enqueue("uno");
      Queue.Enqueue(22222);
      Queue.Enqueue(33.33);
      Queue.Dequeue();
      Queue.Print();
   }
}
