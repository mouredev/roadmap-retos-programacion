using System;
using System.Diagnostics.Metrics;
using System.Reflection;
using System.Runtime.InteropServices.Marshalling;

class Hello
{

    static void Main()
    {
        //Operadores

        byte x = 15;
        bool y = false;
        byte z = 3;
        bool t = true;

        // Operadores de Asignaci�n (unarios)
        Console.WriteLine($"x = 15 => +x = {+x}");
        Console.WriteLine($"x = 15 => -x = {-x}");
        Console.WriteLine($"y = false => !y = {!y}");
        Console.WriteLine($"x = 15 => ++x = {++x}");

        // Operadores Aritm�ticos
        Console.WriteLine($"x = 15 y z = 3 => x * z = {x * z}");
        Console.WriteLine($"x = 15 y z = 3 => x / z = {x / z}");
        Console.WriteLine($"x = 15 y z = 3 => x % z = {x % z}");
        Console.WriteLine($"x = 15 y z = 3 => x + z = {x + z}");
        Console.WriteLine($"x = 15 y z = 3 => x - z = {x - z}");

        // Operadores L�gicos
        Console.WriteLine($"t = true y y = false => t && y = {y && t}");
        Console.WriteLine($"t = true y y = false => t || y = {y || t}");
        Console.WriteLine($"t = true => !t = {!t}");

        // Operadores de Comparaci�n o Relacionales
        Console.WriteLine($"x = 15 y z = 3 => x == z = {x == z}");
        Console.WriteLine($"x = 15 y z = 3 => x != z = {x != z}");
        Console.WriteLine($"x = 15 y z = 3 => x << z = {x << z}"); //Desplazar bits a la izquierda.
        Console.WriteLine($"x = 15 y z = 3 => x >> z = {x >> z}"); //Desplazar bits a la derecha.7
        Console.WriteLine($"x = 15 y z = 3 => x < z = {x < z}");
        Console.WriteLine($"x = 15 y z = 3 => x > z = {x > z}");
        Console.WriteLine($"x = 15 y z = 3 => x >= z = {x >= z}");
        Console.WriteLine($"x = 15 y z = 3 => x <= z = {x <= z}");

        // Operadores de incremento y decremento

        Console.WriteLine("x++ =  " + (x++)); //Devuelve el valor de x y luego incrementa
        Console.WriteLine("++x =  " + (++x)); //Incrementa el valor de x y luego devuelve x
        Console.WriteLine("x-- =  " + (x--));
        Console.WriteLine("--x =  " + (--x));

        //Operador condicional

        Console.WriteLine("x ? y : z" + (y ? x : t)); //Eval�a / devuelve x si y es verdadero; De lo contrario, eval�a t

        //Operador de fusi�n nula

        Console.WriteLine(x ?? y); //Devuelve x si no es nulo, De lo contrario, devuelve y .

        /**ESTRUCTURAS DE CONTROL**/

        //if - else:  Permite ejecutar un bloque de c�digo si se cumple una condici�n, y otro bloque de c�digo si la condici�n no se cumple.
        if (x > 5)
        {
            Console.WriteLine("x es mayor que 5");
        }
        else
        {
            Console.WriteLine("x no es mayor que 5");
        }

        //switch-case: Permite seleccionar uno de varios bloques de c�digo para ejecutar, dependiendo del valor de una expresi�n.
        int opcion = 2;
        switch (opcion)
        {
            case 1:
                Console.WriteLine("Opci�n 1 seleccionada");
                break;
            case 2:
                Console.WriteLine("Opci�n 2 seleccionada");
                break;
            default:
                Console.WriteLine("Opci�n no v�lida");
                break;
        }

        //for: Permite ejecutar un bloque de c�digo un n�mero espec�fico de veces, controlando el ciclo mediante una variable de iteraci�n.
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine("El valor de i es: " + i);
        }

        //while: Ejecuta un bloque de c�digo mientras se cumple una condici�n especificada.
        int j = 0;
        while (j < 5)
        {
            Console.WriteLine("El valor de j es: " + j);
            j++;
        }

        //do-while: Similar al bucle while, pero garantiza que el bloque de c�digo se ejecute al menos una vez antes de verificar la condici�n.
        int num;
        do
        {
            Console.Write("Introduce un n�mero positivo: ");
            num = int.Parse(Console.ReadLine());
        } while (num <= 0);
        Console.WriteLine("Has introducido: " + num);

        //foreach: Se utiliza para iterar sobre los elementos de una colecci�n o arreglo.
        int[] numeros = { 1, 2, 3, 4, 5 };

        foreach (int numero in numeros)
        {
            Console.WriteLine(numero);
        }

        //break: Se utiliza para salir de un bucle o de un bloque switch antes de que se complete su ejecuci�n.
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine("N�mero: " + i);

            if (i == 5)
            {
                Console.WriteLine("�Se ha encontrado el n�mero 5! Saliendo del bucle.");
                break;
            }
        }

        //continue: Se utiliza para omitir el resto del c�digo en un bucle y pasar a la siguiente iteraci�n.
        for (int i = 1; i <= 5; i++)
        {
            if (i == 3)
            {
                Console.WriteLine("Saltando la iteraci�n para el n�mero 3.");
                continue;
            }

            Console.WriteLine("N�mero: " + i);
        }

        //return: Se utiliza para devolver un valor de una funci�n y salir de ella.
        static int Sumar(int a, int b)
        {
            int suma = a + b;

            return suma;
        }

    }
}