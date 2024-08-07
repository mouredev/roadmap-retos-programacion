// ╔══════════════════════════════════════╗
// ║ Autor: Kenys Alvarado                ║
// ║ GitHub: https://github.com/Kenysdev  ║
// ║ 2024 - C#                            ║
// ╚══════════════════════════════════════╝

/*
1. Funciones:
*************
Sintaxis:
║ [modificadorAcceso] ║ [modificador]     ║ TipoRetorno     ║ NombreFuncion║ ([parametros])║
║ public, private, .. ║ static, async, .. ║ int, string, .. ║       --     ║      --       ║
Las funciones básicas pueden ser **públicas o privadas**.
Las privadas solo son accesibles en la misma clase.
Si no se especifica el tipo de acceso, entonces serán privadas por default.
----------------------------
Funcion estática sin retorno
----------------------------
Pueden ser llamadas sin crear una instancia de la clase.
*/
using System;

static void print(object msg)
{
    Console.WriteLine(msg);
}

print("Estática");

// -----------------------------
// Funcion estática con retorno:
// -----------------------------
// Se debe especificar el tipo de dato a retornar.(int, string, etc.)
static int Suma(int a, int b)
{
    return a + b;
}

print(Suma(2, 2));

// ---------------------
// Funcion de Instancia:
// ---------------------
// Requieren crear una instancia de la clase para ser llamadas.
// Pueden ser sin retorno, usando (void) o con retorno(int, string,..).
int Resta(int a, int b)
{
    return a - b;
}

print(Resta(4, 2));

// -----------------------
// Con Parámetro Opcional:
// -----------------------
void Divide(int a, int b = 2)
{
    print(a / b);
}
Divide(10);

// -------------------------
// Con Parámetros de Salida:
// -------------------------
// Permiten devolver más de un valor utilizando la palabra clave out.

void Dividir(int dividendo, int divisor, out int cociente, out int residuo)
{
    cociente = dividendo / divisor;
    residuo = dividendo % divisor; 
}
int rCociente;
int rResiduo;
Dividir(10, 5, out rCociente, out rResiduo);
print($"Cociente: {rCociente}, Residuo: {rResiduo}");

// -------------------------
// Funciones Recursivas::
// -------------------------
int Factorial(int n)
{
    return (n == 0) ? 1 : n * Factorial(n - 1);
}
print(Factorial(6));

//2. Función anidada:
// ******************
int multi(int a, int b)
{
    int interna()
    {
        return a * b;
    }

    return interna();
}
print(multi(2, 2));

// 3. Ejemplo de funciones incorporadas:
// *************************************
// Conversión de Tipos:
bool un_bool = true;
string a_str = Convert.ToString(un_bool);
print(a_str);

//  Fecha y Hora
print(DateTime.Now);

// longitud de la cadena
print(("abc".Length));

/*
# 5. Ejercicio:
# *************
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.""")
*/

 static int Ejercicio(string str1, string str2)
{
    int nVeces = 0; 
    for (int num = 1; num <= 100; num++)
    {
        if (num % 3 == 0 && num % 5 == 0)
        {print(str1 + str2);}
        else if (num % 3 == 0)
        {print(str1);}
        else if (num % 5 == 0)
        {print(str2);}
        else
        {nVeces++;print(num);}
    }

    return nVeces;
}

print(Ejercicio("múltiplo de 3", "múltiplo de 5"));
