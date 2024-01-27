// ╔══════════════════════════════════════╗
// ║ Autor: Kenys Alvarado                ║
// ║ GitHub: https://github.com/Kenysdev  ║
// ║ 2024 - C#                            ║
// ╚══════════════════════════════════════╝

int n;
Console.WriteLine(@"
1. Imprimir ejemplos utilizando todos los tipos 
de operadores de tu lenguaje:
-----------------------------------------------
Operadores aritmeticos:
***********************
- Suma:              10 + 5         = " + (10 + 5) + @"
- Resta:             10 - 5         = " + (10 - 5) + @"
- Multiplicacion:    10 * 5         = " + (10 * 5) + @"
- Division: 
  double, float o    5.0 / 2.0      = " + (5.0 / 2.0) + @"
- Division Entera: int o 17 / 4     = " + (17 / 4) + @"
- Residuo:           20 % 7         = " + (20 % 7) + @"
- Potenciacion:      Math.Pow(2, 3) = " + Math.Pow(2, 3) + @"
- Combined:         (4 + 2) * 3 / 2 = " + ((4 + 2) * 3 / 2) + @"

Operadores de Comparación:
**************************
- igual a       5 == 5 -> " + (5 == 5) + @"
- Diferente de  5 != 5 -> " + (5 != 5) + @"
- Menor que     4 < 5  -> " + (4 < 5) + @"
- Mayor que     4 > 5  -> " + (4 > 5) + @"
- Menor o igual 4 <= 5 -> " + (4 <= 5) + @"
- Mayor o igual 4 >= 5 -> " + (4 >= 5) + @"

Operadores de Asignación:
*************************
- asigna:          n = 10  = " + (n = 10) + @"
- suma:            n += 2  = " + (n += 2) + @"
- resta:           n -= 2  = " + (n -= 2) + @"
- multiplica:      n *= 2  = " + (n *= 2) + @"
- división:        n /= 2  = " + (n /= 2) + @"
- modulo:          n %= 2  = " + (n %= 2) + @"
- pow:      Math.Pow(n, 2) = " + Math.Pow(n, 2) + @"

Operadores Lógicos:
*******************
and: 5 == 5 && 6 != 5  -> " + (5 == 5 && 6 != 5) + @"
or:  5 == 5 || 6 != 5  -> " + (5 == 5 || 6 != 5) + @"
not: !(5 == 6)         -> " + !(5 == 6) + @"

Operador de Pertenencia:
************************
in: ""abcde"".Contains(""c"") -> " + "abcde".Contains("cd") + @"

Operadores Bit a Bit:
**********************
and:       Convert.ToString(10 & 5)  -> " + Convert.ToString(10 & 5, 2) + @"
or:        Convert.ToString(10 | 5)  -> " + Convert.ToString(10 | 5, 2) + @"
xor:       Convert.ToString(10 ^ 5)  -> " + Convert.ToString(10 ^ 5, 2) + @"
not_a:     Convert.ToString(~10)     -> " + Convert.ToString(~10, 2) + @"
izquierda: Convert.ToString(10 << 2) -> " + Convert.ToString(10 << 2, 2) + @"
derecha:   Convert.ToString(10 >> 1) -> " + Convert.ToString(10 >> 1, 2) + @"

2. Estructuras de control:
--------------------------
# condicinal:
*************");
int x = 2;
if (x == 5)
{
    Console.WriteLine("Si 5 == 5");
}
// si de lo contrario
else if (x == 2)
{
    Console.WriteLine("Si 2 == 2");
}
else
{
    Console.WriteLine("Ninguna");
}

//---------------------------------
Console.WriteLine(@"
Operador ternario:");
Console.WriteLine((15 == 15) ? "si es igual" : "no es igual");

//---------------------------------
Console.WriteLine(@"
switch:");
int num = 2;
switch (num)
{
    case 1:
        Console.WriteLine("Es 1");
        break;
    case 2:
        Console.WriteLine("Es 2");
        break;
    default:
        Console.WriteLine("null");
        break;
}

//---------------------------------
Console.WriteLine(@"
Bucles:
*******
Bucle for:");
for (int i = 0; i < 3; i++)
{
    Console.WriteLine($"Iteración {i + 1}");
}

//---------------------------------
Console.WriteLine(@"
Bucle while:");
int j = 0;
while (j < 3)
{
    Console.WriteLine($"Iteración {j + 1}");
    j++;
}

//---------------------------------
Console.WriteLine(@"
Bucle do-while:");
int k = 0;
do
{
    Console.WriteLine($"Iteración {k + 1}");
    k++;
} while (k < 3);

//---------------------------------
Console.WriteLine(@"
Bucle foreach (para iterar sobre colecciones):");
int[] z = { 1, 2, 3 };
foreach (int num2 in z)
{
    Console.WriteLine($"Número: {num2}");
}

//---------------------------------
Console.WriteLine(@"
break & continue:");
for (int i = 1; i <= 3; i++)
{
    if (i == 4)
    {
        Console.WriteLine($"Valor 4 encontrado. Break.");
        break;
    }
    if (i % 2 == 0)
    {
        Console.WriteLine($"Iteración {i} es par. Continue.");
        continue;
    }
    Console.WriteLine($"Iteración {i}");
}
Console.WriteLine($"Finalizando");

//---------------------------------
Console.WriteLine(@"
Control de Excepciones:");
try
{
    int nu = 10;
    Console.WriteLine($"Resultado: {nu / 0}");
}
catch (DivideByZeroException e)
{
    Console.WriteLine($"Error división: {e.Message}");
}
finally
{
    Console.WriteLine("finally");
}

//---------------------------------
Console.WriteLine(@"
3. Ejercicio:
-------------
Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.");
for (int numero = 10; numero <= 55; numero++)
{
    if (numero % 2 == 0 && numero != 16 && numero % 3 != 0)
    {
        Console.WriteLine(numero);
    }
}
