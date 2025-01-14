  // See https://aka.ms/new-console-template for more information

  /*
  * EJERCICIO:
  * - Crea un comentario en el código y coloca la URL del sitio web oficial del
  *   lenguaje de programación que has seleccionado.
  * - Representa las diferentes sintaxis que existen de crear comentarios
  *   en el lenguaje (en una línea, varias...).
  * - Crea una variable (y una constante si el lenguaje lo soporta).
  * - Crea variables representando todos los tipos de datos primitivos
  *   del lenguaje (cadenas de texto, enteros, booleanos...).
  * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
  */

  // tipos de comentarios

  // este es un comentario de una linea url del sitio es https://dotnet.microsoft.com/es-es/languages/csharp
  /* este es un comentario
  de varias lineas */

  // variables

  public string variable = "hola";
  public const string constante = "hola";
  public char caracter = 'a';
  public var variable = "hola";
  public string[] arreglo = {"hola", "mundo"};
  public List<string> lista = new List<string> {"hola", "mundo"};
  public Dictionary<string, string> diccionario = new Dictionary<string, string> {{"hola", "mundo"}};


  // tipos de datos primitivos

  public byte b = 1;
  public short corto = 1;
  public int entero = 1;
  public float flotante = 1.1f;
  public double doble = 1.1;
  public bool booleano = true;




  // impresion por terminal
  public string lenguaje = "C#";

  Console.WriteLine($"Hello, {lenguaje}");