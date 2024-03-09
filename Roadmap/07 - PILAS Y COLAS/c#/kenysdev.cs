/* ╔══════════════════════════════════════╗
   ║ Autor:  Kenys Alvarado               ║
   ║ GitHub: https://github.com/Kenysdev  ║
   ║ 2024 -  C#                           ║
   ╚══════════════════════════════════════╝
   ------------------------------------------
   # PILAS Y COLAS
   ------------------------------------------
// Pilas(stack - LIFO):
 - Sigue el principio LIFO (last in, first out), significa que
   el último elemento añadido, es el primero en ser retirado. */

var myStack = new Stack<int>();
myStack.Push(1); // Agregar elemento.
myStack.Push(2); 
myStack.Push(3);

Console.WriteLine(@$"
- Eliminar y obtener:   {myStack.Pop()}
- Obtener sin eliminar: {myStack.Peek()}
- Total de elementos:   {myStack.Count}
- Verificar si existe:  {myStack.Contains(5)}
- Obtener elementos:    {string.Join(", ", myStack.ToArray())}");

/* ___________________________________________
// Colas (Queue - FIFO):
   - Estructura de datos que sigue el principio FIFO(First In, First Out)
   - El primer elemento que se inserta es el primero en ser retirado. */
var myQueue = new Queue<int>();
myQueue.Enqueue(1); // Agregar elemento.
myQueue.Enqueue(2);
myQueue.Enqueue(3);

Console.WriteLine(@$"
- Eliminar y obtener:   {myQueue.Dequeue()}
- Obtener sin eliminar: {myQueue.Peek()}
- Total de elementos:   {myQueue.Count}
- Verificar si existe:  {myQueue.Contains(5)}
- Obtener elementos:    {string.Join(", ", myQueue.ToArray())}");

/* ____________________________________________
// Ejercicio usando la implementación de pilas:
Simula el mecanismo adelante/atrás de un navegador web.
- Crea un programa en el que puedas navegar a una página o indicarle que te quieres 
  desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
- Las palabras "adelante", "atrás" desencadenan esta acción, el resto 
  se interpreta como el nombre de una nueva web. */

string msgNav = @"
Historial de navegación:
-------------------------------------------------
Usar: '<' para página anterior.
      '>' para página adelante.
      'h' Ver historial completo.
      'x' para salir. 
Escribir web para agregar:
-------------------------------------------------";
void NavHistory(){
   var history = new Stack<string>();
   history.Push("Inicio");
   var backHistory = new Stack<string>();
   var forwardHistory = new Stack<string>();

   Console.WriteLine(msgNav);
   Web(history.Peek());
   Select();

   void Select(){
      Console.Write("____________\r\n Acción: ");
      string action = Console.ReadLine()!;
      if (action.Length > 0){
         switch(action){
            case "<": Back(); break;
            case ">": Forward(); break;
            case "x": Home(); break;
            case "h": TheHistory(); break;
            default:  NewWeb(action); break;
         }
      }
      else {Console.WriteLine("Eres muy gracioso xD."); Select();}  
   }

   void Web(string url){
      Console.WriteLine($"{backHistory.Count} <-[Actual: {url}]-> {forwardHistory.Count}");
   }

   void Back(){
      if (backHistory.Count > 0){
         forwardHistory.Push(history.Peek());
         history.Push(backHistory.Pop());
         Web(history.Peek());
      }
      else {Console.WriteLine("No hay página previa.");}
      Select();
   }

   void Forward(){
      if (forwardHistory.Count > 0){
         backHistory.Push(history.Peek());
         history.Push(forwardHistory.Pop());
         Web(history.Peek());
      }
      else {Console.WriteLine("No hay página siguiente.");}
      Select();
   }

   void NewWeb(string url){
      backHistory.Push(history.Peek());
      forwardHistory.Clear();
      history.Push(url);
      Web(url);
      Select();
   }

   void TheHistory(){
      if (forwardHistory.Count > 0){
         foreach (string item in history){
            Console.WriteLine(item);
         }
      }
      else {Console.WriteLine("Historial vacío.");}
      Select();
   }
} 

/* ____________________________________________
// Ejercicio usando la implementación de Colas:
Simula el mecanismo de una impresora compartida.
- recibe documentos y los imprime cuando así se le indica.
- La palabra "imprimir" imprime un elemento de la cola.
- El resto de palabras se interpretan como nombres de documentos. */

string msgPrinter = @"
------------------------------------------------
Usar: 'p' Imprimir.
      'l' Ver documentos pendientes.
      'x' para salir.
Escribir nombre de documento para enviar a cola: 
------------------------------------------------";

void QueuePrinter(){
   var docQueue = new Queue<string>();
   Console.WriteLine(msgPrinter);
   Select();

   void Select(){
      Console.Write("____________\r\n Acción: ");
      string action = Console.ReadLine()!;
      if (action.Length > 0){
         switch(action){
            case "p": PrintDoc(); break;
            case "l": QueuePending(); break;
            case "x": Home(); break;
            default:  SendDoc(action); break;
         }
      }
      else {Console.WriteLine("Eres muy gracioso xD."); Select();}  
   }

   void PrintDoc(){
      if (docQueue.Count > 0){
         Console.WriteLine(@$"
         {docQueue.Dequeue()} -> ha sido impreso.
         {docQueue.Count} -> archivos faltantes.");
      }
      else{Console.WriteLine("No hay archivos.");}
      Select();
   }

   void QueuePending(){
      if (docQueue.Count > 0){
         foreach (string doc in docQueue){
            Console.WriteLine(doc);
         }
      }
      else {Console.WriteLine("No hay archivos.");}
      Select();
   }

   void SendDoc(String doc){
      docQueue.Enqueue(doc);
      Console.WriteLine("Archivo agregado a cola de impresión.");
      Select();
   }
}

// ____________________________________________
string msgHome = @"
----------------------------------
Usar: '1' para simulador_navegador.
      '2' para simulador_impresora.
      'Otra tecla' para salir.
----------------------------------";

void Home(){
   Console.WriteLine(msgHome);
   Console.Write("____________\r\n Acción: ");
   string action = Console.ReadLine()!;
   switch(action){
      case "1": NavHistory();; break;
      case "2": QueuePrinter(); break;
      default:  Console.WriteLine("Bye"); break;
   }
}

Home();
