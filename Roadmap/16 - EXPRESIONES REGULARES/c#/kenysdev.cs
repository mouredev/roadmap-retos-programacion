/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
* EXPRESIONES REGULARES
------------------------------------------
https://learn.microsoft.com/es-es/dotnet/standard/base-types/regular-expressions

* EJERCICIO #1:
* Utilizando tu lenguaje, explora el concepto de expresiones regulares,
* creando una que sea capaz de encontrar y extraer todos los números
* de un texto.
*/

using System.Text.RegularExpressions;

static void GetNumbers(string text) {
    string Pattern = @"\d+";
    MatchCollection numbers = Regex.Matches(text, Pattern);
        
    foreach (object n in numbers) {
        Console.WriteLine(n);
    }
}

GetNumbers("abcdsfs1s(*&#}2. a3// 45sdf67");
GetNumbers("45sdf67");

/*
* EJERCICIO #2:
* Crea 3 expresiones regulares (a tu criterio) capaces de:
* - Validar un email.
* - Validar un número de teléfono.
* - Validar una url.
*/

static bool IsEmail(string text) {
    string patron = @"^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$";
    return Regex.IsMatch(text, patron);
}

static bool IsPhoneNumber(string text) {
    string patron = @"^(\d{3}-\d{3}-\d{4}|\d{10})$";
    return Regex.IsMatch(text, patron);
}

static bool IsURL(string text) {
    string patron = @"^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/\S*)?$";
    return Regex.IsMatch(text, patron);
}

static void Print(Object text) {
    Console.WriteLine(text);
}

Print("\nIsEmail");
Print(IsEmail("ejm@dmn.com"));         // True
Print(IsEmail("e_jm-2+b@dmn.co.hn"));  // True
Print(IsEmail("ejm@dmn.com_"));        // False
Print(IsEmail("ejm@dmn"));             // False

Print("\nIsPhoneNumber");
Print(IsPhoneNumber("123-456-7890"));  // True
Print(IsPhoneNumber("1234567890"));    // True
Print(IsPhoneNumber("123456-7890"));   // False
Print(IsPhoneNumber("uno234567890"));  // False

Print("\nIsURL");
Print(IsURL("http://www.ejm.com"));    // True
Print(IsURL("google.com"));            // True
Print(IsURL("ejm.com/a/b/c"));         // True
Print(IsURL("https://.ejm.com"));      // False
Print(IsURL("https://.ejm.com/a b"));  // False 

