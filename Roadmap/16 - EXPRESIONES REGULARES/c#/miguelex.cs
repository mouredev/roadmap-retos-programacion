using System;
using System.Text.RegularExpressions;

class miguelex
{
    static void RegExpr(string cadena)
    {
        string patron = @"-?\d+(\.\d+)?";
        MatchCollection numeros = Regex.Matches(cadena, patron);

        Console.WriteLine("Números encontrados:");
        foreach (Match numero in numeros)
        {
            Console.WriteLine(numero.Value);
        }
        Console.WriteLine();
    }

    static void Main(string[] args)
    {
        string texto = "Este es un texto con números como 123, 45.6, -7 y 1000.";
        Console.WriteLine("Vamos a analizar el siguiente texto:");
        Console.WriteLine("'" + texto + "'\n");
        RegExpr(texto);

        texto = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456";
        Console.WriteLine("Vamos a analizar el siguiente texto:");
        Console.WriteLine("'" + texto + "'\n");
        RegExpr(texto);

        EmailValidation("correo@correo.com");
        EmailValidation("correo@correo");

        PhoneValidation("+34 123456789");
        PhoneValidation("123456789");

        UrlValidation("http://www.google.com");
        UrlValidation("www.google.com");
    }

    static void EmailValidation(string email)
    {
        string patron = @"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$";
        if (Regex.IsMatch(email, patron))
        {
            Console.WriteLine($"El email {email} es válido.");
        }
        else
        {
            Console.WriteLine($"El email {email} no es válido.");
        }
    }

    static void PhoneValidation(string phone)
    {
        string patron = @"^\+?(\d{2,3})?[-. ]?\d{9}$";
        if (Regex.IsMatch(phone, patron))
        {
            Console.WriteLine($"El teléfono {phone} es válido.");
        }
        else
        {
            Console.WriteLine($"El teléfono {phone} no es válido.");
        }
    }

    static void UrlValidation(string url)
    {
        string patron = @"^(http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}";
        if (Regex.IsMatch(url, patron))
        {
            Console.WriteLine($"La URL {url} es válida.");
        }
        else
        {
            Console.WriteLine($"La URL {url} no es válida.");
        }
    }
        
}
