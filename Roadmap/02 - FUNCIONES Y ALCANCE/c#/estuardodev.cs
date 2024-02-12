/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
using System;
using System.Runtime.CompilerServices;

class Program
{
    // Esta variable es accesible por todo el programa
    public string variableGlobal = "Prueba";

    public static void Main(string[] args)
    {
        Program program = new Program();

        // Funciones sin retorno y sin parámetros
        FuncionSinRetornoPublica();
        FuncionSinRetornoPrivada();
        FuncionSinRetornoProtegida();

        // No puedes llamar a FuncionSinRetornoNoEstatica directamente desde un método estático como Main
        // Deberías crear una instancia de la clase Program y luego llamar a ese método
        program.FuncionSinRetornoNoEstatica();

        // De esta forma ejecutas un método asíncrono en un método no asíncrono
        Task.Run(async () => await program.FuncionAsincronaSinRetornoPrivada());

        // Funciones con parámetros y retornos
        Console.WriteLine(Suma(5, 6));
        Console.WriteLine(Minusculas("Hola"));
        Console.WriteLine(EsPalindromo("Ana"));

        // Prueba de método dentro de métodos
        PruebaDeMetodos();


        // Dificultad extra
        Console.WriteLine(DificultadExtra("Uno", "Dos"));
    }

    // Funciones sin retorno y sin parámetros
    public static void FuncionSinRetornoPublica() { Console.WriteLine("No retorna nada pública"); }
    private static void FuncionSinRetornoPrivada() { Console.WriteLine("No retorna nada privada"); }
    protected static void FuncionSinRetornoProtegida() { Console.WriteLine("No retorna nada protegida"); }
    public void FuncionSinRetornoNoEstatica() {
        // Esta variable solo es accesible dentro de este método
        string variableLocal = "Variable Local";
        Console.WriteLine("No retorna nada no estatica"); 
    }
    private async Task FuncionAsincronaSinRetornoPrivada() { await Task.Run(() => Console.WriteLine("No retorna nada, privada")); }

    // Funciones con parámetros y retornos
    public static int Suma(int num1, int num2){ return num1 + num2; }
    public static string Minusculas(string frase) { return frase.ToLower(); }
    private static bool EsPalindromo(string texto1)
    {
        texto1 = texto1.ToLower();
        if (texto1.Equals(texto1.Reverse())){
            return true;
        } else 
        { 
            return false; 
        }
    }

    // Prueba de método dentro de métodos
    private static void PruebaDeMetodos()
    { 
        // Si se puede crear métodos dentro de otros métodos, pero estos funcionan de forma local.
        static bool MetodoDentro(int numero)
        {
            return numero == 5;
        }

        Console.WriteLine(MetodoDentro(5));
    }

    // Dificultad extra
    private static int DificultadExtra(string valor1, string valor2)
    {
        int contador = 1;
        int numerosImpresos = 0;
        while (contador < 101)
        {
            if (contador % 3 == 0 && contador % 5 == 0)
            {
                Console.WriteLine(valor1 + " " + valor2);
            } else if (contador % 5 == 0)
            {
                Console.WriteLine(valor2);
            } else if (contador % 3 == 0)
            {
                Console.WriteLine(valor1);
            }
            else
            {
                Console.WriteLine(contador);
                numerosImpresos++;
            }
            contador++;   
        }
        return numerosImpresos;
    }

}
