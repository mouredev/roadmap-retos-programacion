// Ejemplos de funcinalidades con String

string frase = "El Perro de San Roque no tiene rabo";
string frase2 = ", porqué Ramón Ramirez se lo ha cortado.";
Console.WriteLine($"Nuestra frase es: {frase}");
// Recorrer cada letra del string
Console.WriteLine("Recorrer con un foreach cada letra");
foreach (var letra  in frase)
{
    Console.Write($"{letra} ");
}
Console.WriteLine();

// Longitud
Console.WriteLine($"La longitud de toda la cadena es: {frase.Length}");
Console.WriteLine($"La longitud de la cadena sin espacioes es: {frase.Trim().Length}");

// Separar en palabras
string[] fraseCortada = frase.Split(" ");
Console.WriteLine("Separar en palabras con Split(\" \")");
foreach (var item in fraseCortada)
{
    Console.WriteLine(item);
}

// Todo a mayusculas y todo a minusculas
Console.WriteLine("Frase en mayusculas y minusculas");
Console.WriteLine($"{frase.ToUpper()}");
Console.WriteLine($"{frase.ToLower()}");

// Acceso a la primera letra y a la ultima

Console.WriteLine($"La primera letra es {frase[0]}");

// Quitar uno ya que el array empieza por el indice 0 o bien usar [^1]
Console.WriteLine($"La útlima letra es {frase[frase.Length - 1]}");

// Concatenacion
Console.WriteLine("Concatenacion de frases");
Console.WriteLine($"{string.Concat(frase, frase2)}");

// Reemplazar

string fraseConI = frase.Replace("o", "i");
Console.WriteLine($"Reemplazamos las o por i. {fraseConI}");

string cadenaCortada = frase.Substring(0, 7);
Console.WriteLine($"Cortamos desde la posicion 0 hasta 7 de largo: {cadenaCortada}");

// Busqueda, esto es Case Sensitive si no le añadimos el parametro de StringComparison
bool respuesta = frase.Contains("Perro", StringComparison.OrdinalIgnoreCase);
if (respuesta)
{

    Console.WriteLine("La frase tiene Perro");
}
else
{
    Console.WriteLine("La frase no tiene Perro");
}

// DIFICULTAD EXTRA: obs. No está chequeado los posibles nulos en el ReadLine

Console.WriteLine("Ingresa la primera palabra");

string palabra1 = Console.ReadLine()!;
Console.WriteLine("Ingresa la Segunda palabra");
string palabra2 = Console.ReadLine()!;

ComparadorPalabras(palabra1, palabra2);


void ComparadorPalabras(string a, string b)
{
    // Palindromos
    // Descomponer en chars
    char[] reverse = a.ToCharArray();
    Array.Reverse(reverse);
    string aReverse = new string(reverse);
    
    // Comparacion
    if (aReverse.Equals(b))
    {
        Console.WriteLine("Son palindromos");
    }
    
    // Anagramas
    char[] aOrder = a.ToCharArray();
    Array.Sort(aOrder);
    string aOrdenada = new string(aOrder);
    char[] bOrder = b.ToCharArray();
    Array.Sort(bOrder);
    string bOrdenada = new string(bOrder);
    if (aOrdenada.Equals(bOrdenada))
    {
        Console.WriteLine("Las palabras son Anagramas");
    }

    // Isogramas
    char[] aIsogramaChar = a.ToCharArray();
    Array.Sort(aIsogramaChar);
    char[] bIsogramaChar = b.ToCharArray();
    Array.Sort(bIsogramaChar);
    bool flagA = true;
    bool flagB = true;
    for (int i = 1; i <aIsogramaChar.Length; i++)
    {
        if (aIsogramaChar[i] == aIsogramaChar[i -1])
        {
            flagA = false;
        }
    }
    for (int i = 1; i < bIsogramaChar.Length; i++)
    {
        if (bIsogramaChar[i] == bIsogramaChar[i -1])
        {
            flagB = false;
        }
    }

    if (flagA)
    {
        Console.WriteLine($"La palabra {a} es un isograma");
    }
    if (flagB)
    {
        Console.WriteLine($"La palabra {b} es un isograma");
    }

    if (!flagB && !flagA)
    {
        Console.WriteLine("Ningun Isograma");
    }
}




















