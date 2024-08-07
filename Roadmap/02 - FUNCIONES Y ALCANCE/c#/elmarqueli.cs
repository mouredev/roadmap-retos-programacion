/*
	=== Para realizar el ejercicio me vase en los delegados Func y action ===
*/

namespace elmarqueli
{
  class Program
  {
    // Solo imprime por consola
    static Action PrintHolaMundo = () => Console.WriteLine("Hola Mundo\n");
  
    // Recibe dos parametros de de tipo string e imprime por consola
    static Action<string, string> PrintString = (str1, str2) => {Console.WriteLine($"String1: {str1}\nString2: {str2}\n"); };
  
    // Recibe dos parametors de tipo strigs y retorna la concatenacion de estos dos.
    static Func<string, string, string> FuncConcatReturn = (str1, str2) => $"{str1} {str2}";
  
    // Recibe un entero retorna un string y dentro se resuelve otra funcion.
    static Func<int, string> FuncCreatToFunc = (num) => {
    
      // Funcion interna act, recibe un entero y retorna el doble.
      var act = (int x) => {
        return x * 2;
      };
  
      // Se ejecuta act con el parametro num y retora el valor en formato string.
      return act.Invoke(num).ToString();
    };
  
    // Dificultad extra
    static Func<string, string, int> FuncMultiplos_3_5 = (str1,str2) => {
  
        // Delcaramos la variable en la cual se asiganra la función.
        Func<int, int>? CountPrint = null;
        var count = 0;
  
        // Se asigna la función anonima a la variable.
        CountPrint = (x) => {
          if (x < 100)
          {
            if (x % 3 == 0 && x % 5 == 0)
              Console.WriteLine($"{str1} {str2}");
            else if(x % 3 == 0)
              Console.WriteLine($"{str1}");
            else if (x % 5 == 0)
              Console.WriteLine($"{str2}");
            else
            {
              Console.WriteLine(x);
              count +=1;
            }
    
            return CountPrint!(x+1);
          }
          else
            Console.WriteLine(x);
          return x;
        };
  
    CountPrint(1);

    return count;
    };
  
    // Global variable
    static int Number = 12;
  
    static void Main(string[] args)
    {
      // Local variable
      var text = "Función nativa";
  
      PrintHolaMundo();
  
      PrintString("Primer texto de prueva", "Segundo texto de prueva");
  
      Console.WriteLine(FuncConcatReturn("Codeando en", "GitHub")+"\n");
  
      Console.WriteLine(FuncCreatToFunc(15) + "\n");
  
      // WriteLiane como funcion del lenguaje
      Console.WriteLine(text);
  
      Console.WriteLine($"Total de numeros impreso: {FuncMultiplos_3_5("Fizz", "Buzz")}");
    }
  }
}
