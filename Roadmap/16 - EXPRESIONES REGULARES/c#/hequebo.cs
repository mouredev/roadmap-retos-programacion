using System.Text.RegularExpressions;

class Program
{
    static void Main(string[] args)
    {
        #region RegEx
        // Expresiones Regulares
        string texto = "1Est3e T8ext0o tie5n4e n0um98er5467os q78u11e de7851b44e651n313 s51e35r 00ob5t3en5i1d6o0s5";
        // El siguiente patrón busca números del 0 al 9
        string pattern = "[0-9]";
        /*
         * Se inicializa un objeto de tipo Regex y se envía
         * el patrón anterior en su constructor
         */
        var regex = new Regex(pattern);
        /*
         * El método Matches() devuelve una colección con 
         * todas las coincidencias encontradas en el texto
         * especificado
         */
        var numeros = regex.Matches(texto);
        Console.WriteLine($"Numeros Encontrados en texto: {texto}");
        /*
         * Recorremos la colección e imprimimos todos las
         * coincidencias
         */
        foreach (var numero in numeros)
            Console.Write($"{numero}, ");
        Console.WriteLine();
        /*
         * La clase Regex contiene el método estático Replace()
         * el cual reemplaza dentro de la cadena envíada el patrón
         * que se indique por otro carácter
         */
        texto = Regex.Replace(texto, pattern, "");
        Console.WriteLine($"Texto con números eliminados: {texto}");
        #endregion
        // Ejercicio extra
        Console.ReadLine();
        Console.Clear();
        bool salir = false;
        do
        {
            Menu();
            string option = Console.ReadLine();
            switch (option.ToLower())
            {
                case "a":
                    var responseEmail = ValidarEmail();
                    if (responseEmail.Item2)
                        Console.WriteLine($"El email {responseEmail.Item1} es válido...");
                    else
                        Console.WriteLine($"El email {responseEmail.Item1} no es válido...");
                    break;
                case "b":
                    var responseTelefono = ValidarNumero();
                    if (responseTelefono.Item2)
                        Console.WriteLine($"El número {responseTelefono.Item1} es válido...");
                    else
                        Console.WriteLine($"El número {responseTelefono.Item1} no es válido...");
                    break;
                case "c":
                    var responseURL = ValidarURL();
                    if (responseURL.Item2)
                        Console.WriteLine($"La URL {responseURL.Item1} es válida...");
                    else
                        Console.WriteLine($"La URL {responseURL.Item1} no es válida...");
                    break;
                case "d":
                    Console.Clear();
                    Console.WriteLine("Hasta la próxima...");
                    salir = true;
                    Thread.Sleep(1000);
                    break;
                default:
                    Console.Clear();
                    Console.WriteLine("Opción no válida...");
                    break;
            }
        }
        while (!salir);
        
    }
    static void Menu()
    {
        Console.WriteLine("---Sistema RegEx---");
        Console.WriteLine("a.- Validar email");
        Console.WriteLine("b.- Validar número telefónico");
        Console.WriteLine("c.- Validar URL");
        Console.WriteLine("d.- Salir");
        Console.WriteLine("Selecciones la opción deseada...");
    }
    static (string, bool) ValidarEmail()
    {
        Console.Clear();
        Console.WriteLine("Ingresa email a validar");
        string email = Console.ReadLine();

        if(string.IsNullOrEmpty(email)) 
            return (email, false);

        string pattern = @"^[^@\s]+@[^@\s]+\.[^@\s]+$";
        /*
         * ^ -> Comenzar la búsqueda al inicio de la cadena
         * [^@\s]+ -> Busca uno o más carácterers diferentes de @ o espacio en blanco
         * @ -> Busca el carácter @
         * \. -> Busca un único carácter de punto
         * $ -> Finalizar la busqueda al final de la cadena
         */
        return Regex.IsMatch(email, pattern) ? (email, true) : (email, false);
    }
    static (string, bool) ValidarNumero()
    {
        Console.Clear();
        Console.WriteLine("Ingresa número teléfonico a validar");
        string numero = Console.ReadLine();
        if (string.IsNullOrEmpty(numero))
            return (numero, false);
        string pattern = @"^(\+?\s?\d{3}[\s.-]?\d{3}[\s.-]?\d{4}|\d{10})$";
        /*
         * ^ -> Comenzar la búsqueda al inicio de la cadena
         * \+? -> Puede comenzar con un +
         * \s -> Puede incluir un espacio en blanco
         * \d{3} Debe incluir tres dígitos
         * [\s.-]? -> Puede contener un espacio en blanco, un punto o un guión
         * \d{4} -> Debe incluir cuatro dígitos
         * |\d{10} O incluye dies dígitos
         * $ -> Finalizar la busqueda al final de la cadena
         */
        return Regex.IsMatch(numero, pattern) ? (numero, true) : (numero, false);
    }
    static (string, bool) ValidarURL()
    {
        Console.Clear();
        Console.WriteLine("Ingresa URL a validar");
        string url = Console.ReadLine();
        if (string.IsNullOrEmpty(url))
            return (url, false);
        string pattern = @"^(http+s?\:\/\/)?(www\.)?\w+\.\w+$";
        /*
         * ^ -> Comenzar la búsqueda al inicio de la cadena
         * (http+s?\:\/\/)? -> Puede incluir http:// o https://
         * (www\.)? -> Puede incluir www.
         * \w+ -> Incluye uno o varios carácteres alfanuméricos
         * \. Incluye un punto
         * $ -> Finalizar la busqueda al final de la cadena
         */

        return Regex.IsMatch(url, pattern) ? (url, true) : (url, false);
    }
}