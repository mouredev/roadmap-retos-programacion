/*
--------------------------------------------------------------------------------------------------------
Instrucciones:

    1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
       Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
       (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
    2. Utilizando las operaciones con operadores que tú quieras, crea ejemplos
       que representen todos los tipos de estructuras de control que existan
       en tu lenguaje:
       Condicionales, iterativas, excepciones...
    3. Debes hacer print por consola del resultado de todos los ejemplos.

Dificultad extra:
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
--------------------------------------------------------------------------------------------------------
*/

#region Definicion de variables

int a = 1;
int b = 2;
bool c = true;
bool d = false;
object e = "e";
string[] f = { "1", "2", "3", "4", "5" };

#endregion

#region 1.

Console.WriteLine("Operadores:\n");

#region Aritmeticos

Console.WriteLine("Aritmeticos:");

Console.WriteLine($"    Suma: {a + b}");
Console.WriteLine($"    Resta: {a - b}");
Console.WriteLine($"    Multiplicacion: {a * b}");
Console.WriteLine($"    Divicion: {a / b}");
Console.WriteLine($"    Modulo: {a % b}");
Console.WriteLine($"    Potenciacion: {Math.Pow(a, b)}"); //No existe el operador así que se usa Math.Pow()
Console.WriteLine($"    Radicacion: {Math.Pow(a, 1.0 / b)}"); // No existe operado así que se usa Math.Sqrt() 
                                                        // para raiz cuadrada o elevando a la potencia de 1/n
Console.WriteLine($"    Logaritmacion: {Math.Log(a, b)}"); //No existe el operador así que se usa Math.Log()

#endregion

#region Logicos

Console.WriteLine("Logicos:");

Console.WriteLine($"    AND: {c && d}");
Console.WriteLine($"    OR: {c || d}");
Console.WriteLine($"    NOT: {!c}");

#endregion

#region Comparacion

Console.WriteLine("Comparacion:");

Console.WriteLine($"    Igualdad: {a == b}");
Console.WriteLine($"    Diferente: {a != b}");
Console.WriteLine($"    Mayor que: {a > b}");
Console.WriteLine($"    Mayor o igual que: {a >= b}");
Console.WriteLine($"    Menor que: {a < b}");
Console.WriteLine($"    Menor o igual que: {a <= b}");

#endregion

#region Asignacion

Console.WriteLine("Asignacion:");

Console.WriteLine($"    Simple: {a = 3}");
Console.WriteLine($"    Suma y asignacion: {a += 2}");
Console.WriteLine($"    Suma 1 y asignacion: {a++}");
Console.WriteLine($"    Resta y asignacion: {a -= 2}");
Console.WriteLine($"    Resta 1 y asignacion: {a--}");
Console.WriteLine($"    Multiplicacion y asignacion: {a *= 2}");
Console.WriteLine($"    Divicion y asignacion: {a /= 2}");
Console.WriteLine($"    Modulo y asignacion: {a %= 2}");

#endregion

#region Pertenencia

Console.WriteLine("Pertenencia:");

Console.WriteLine($"    Es: {e is string}");
Console.WriteLine($"    Como: {e as string}");

#endregion

#region Bits

Console.WriteLine("Bits:");

Console.WriteLine($"    AND: {c & d}");
Console.WriteLine($"    OR: {c | d}");
Console.WriteLine($"    XOR: {c ^ d}");
Console.WriteLine($"    NOT: {~a}");
Console.WriteLine($"    Desplazamiento a la izquierda: {a << 2}");
Console.WriteLine($"    Desplazamiento a la derecha: {a >> 2}");

#endregion

#endregion

#region 2.

AñadirDivision();
Console.WriteLine("Estructuras de control:\n");

#region Condicionales

Console.WriteLine("Condicionales:");

if (a == b)
{
    Console.WriteLine("    Si");
}
else if (a > b)
{
    Console.WriteLine("    Si no, si");
}
else
{
    Console.WriteLine("    Si no");
}

Console.WriteLine("    Switch");
switch (a)
{
    case 1:
        Console.WriteLine("        a = 1");
        break;
    case 7:
        Console.WriteLine("        a = 7");
        break;
    default:
        Console.WriteLine("        Default (No esta en ninguno de los casos)");
        break;
}

#endregion

#region Iterativas y control de flujo

Console.WriteLine("Iterativas:");

Console.WriteLine("    For:");
for (int i = 0; i < f.Length; i++)
{
    if (i == 1)
    {
        Console.WriteLine("«Continue»");
        continue;
    }
    Console.WriteLine($"        i = {i}; f[i] = {f[i]}");    
}

Console.WriteLine("    Foreach:");
foreach (string item in f)
{
    if (item == "3")
    {
        Console.WriteLine("«Break»");
        break;
    }
    Console.WriteLine($"        Item: {item}");    
}

Console.WriteLine("    While:");
while (a < 8)
{
    a++;
    Console.WriteLine($"        Aun se cumple la condicion. a = {a}");
}

Console.WriteLine("    Do-While:");
do
{
    Console.WriteLine($"        Primero realiza la accion y luego si revisa si lo vuelve a hacer.");
} while (false);

#endregion

#region Excepciones

Console.WriteLine("Excepciones:");

try
{
    Console.WriteLine("    Try");
    throw new Exception();
}
catch
{
    Console.WriteLine("    Catch");
}
finally
{
    Console.WriteLine("    Finally");
}

#endregion

#endregion

#region Extra

AñadirDivision();
Console.WriteLine("Extra:\n");

Extra();

#endregion

#region Funciones

void AñadirDivision() => Console.WriteLine("\n" + new string('-', 75) + "\n");

void Extra()
{
    /*Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/

    Enumerable.Range(10, 46)
        .Where(i => !((i % 2) != 0 || i == 16 || (i % 3) == 0))
        .ToList()
        .ForEach(i => Console.WriteLine($"    {i}"));

}

#endregion