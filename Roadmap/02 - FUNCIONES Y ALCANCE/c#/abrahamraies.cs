// Author: Abraham Raies https://github.com/abrahamraies

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

class Program
{
    static string variableGlobal = "variable global";

    static void Main(string[] args)
    {
        //Funciones:
        Console.WriteLine("Funciones");
        Saludar(); //Sin parametros
        SaludarA("Julio"); //Con parametro
        DespedirA("Julio",25); //Con parametros y retorno

        Console.WriteLine(Calcular(4,5)); //Funcion que llama a otra funcion

        //Random -- funcion creada por el lenguaje
        Random random = new Random();
        Console.WriteLine(random.Next());

        // variables globales y locales
        Console.WriteLine("Variables globales y locales");
        Scopes();

        // Ejercicio extra
        Console.WriteLine("Ejercicio Extra");
        EjercicioExtra("Agua","Fuego");

    }

    // Funcion sin parametros:
    static void Saludar()
    {
        Console.WriteLine("Hola, ¿como va?");
    }
    // Funcion con parametro:
    static void SaludarA(string name){
        Console.WriteLine($"Hola {name}, ¿como va?");
    }
    // Funcion con parametros y retorno:
    static string DespedirA(string name,int edad){
        return $"Hola {name}, ¿tenes {edad} años?";
    }

    // Funcion que llama a otra funcion
    static int Calcular(int num1,int num2){

        int Suma(int num1,int num2) => num1 + num2;

        return Suma(num1,num2);
    }

    // Scopes de funciones (alcance)
    static string Scopes(){
        string variableLocal = "variable local";
        Console.WriteLine(variableGlobal);
        Console.WriteLine(variableLocal); //Fuera de esta funcion no existe la variable "variableLocal"
    }

    // Ejercicio extra
    static int EjercicioExtra(string palabra1,palabra2){
        int contador = 0;
        for(int i = 1; i <= 100; i++){
            if(i % 3 == 0 && i % 5 == 0){
                Console.WriteLine(palabra1+palabra2);
            }else if(i % 5 == 0){
                Console.WriteLine(palabra2);
            }else if(i % 3 == 0){
                Console.WriteLine(palabra1);
            }else{
                Console.WriteLine(i);
                contador++;
            }
        }
        return contador;
    }
}