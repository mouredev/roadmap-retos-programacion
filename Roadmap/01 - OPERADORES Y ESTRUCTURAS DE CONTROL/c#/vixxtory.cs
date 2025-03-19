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

        // Operadores de Asignación (unarios)
        Console.WriteLine($"x = 15 => +x = {+x}");
        Console.WriteLine($"x = 15 => -x = {-x}");
        Console.WriteLine($"y = false => !y = {!y}");
        Console.WriteLine($"x = 15 => ++x = {++x}");

        // Operadores Aritméticos
        Console.WriteLine($"x = 15 y z = 3 => x * z = {x * z}");
        Console.WriteLine($"x = 15 y z = 3 => x / z = {x / z}");
        Console.WriteLine($"x = 15 y z = 3 => x % z = {x % z}");
        Console.WriteLine($"x = 15 y z = 3 => x + z = {x + z}");
        Console.WriteLine($"x = 15 y z = 3 => x - z = {x - z}");

        // Operadores Lógicos
        Console.WriteLine($"t = true y y = false => t && y = {y && t}");
        Console.WriteLine($"t = true y y = false => t || y = {y || t}");
        Console.WriteLine($"t = true => !t = {!t}");

        // Operadores de Comparación o Relacionales
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

        Console.WriteLine("x ? y : z" + (y ? x : t)); //Evalúa / devuelve x si y es verdadero; De lo contrario, evalúa t

        //Operador de fusión nula

        Console.WriteLine(x ?? y); //Devuelve x si no es nulo, De lo contrario, devuelve y .

        /**ESTRUCTURAS DE CONTROL**/

        //if - else:  Permite ejecutar un bloque de código si se cumple una condición, y otro bloque de código si la condición no se cumple.
        if (x > 5)
        {
            Console.WriteLine("x es mayor que 5");
        }
        else
        {
            Console.WriteLine("x no es mayor que 5");
        }

        //switch-case: Permite seleccionar uno de varios bloques de código para ejecutar, dependiendo del valor de una expresión.
        int opcion = 2;
        switch (opcion)
        {
            case 1:
                Console.WriteLine("Opción 1 seleccionada");
                break;
            case 2:
                Console.WriteLine("Opción 2 seleccionada");
                break;
            default:
                Console.WriteLine("Opción no válida");
                break;
        }

        //for: Permite ejecutar un bloque de código un número específico de veces, controlando el ciclo mediante una variable de iteración.
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine("El valor de i es: " + i);
        }

        //while: Ejecuta un bloque de código mientras se cumple una condición especificada.
        int j = 0;
        while (j < 5)
        {
            Console.WriteLine("El valor de j es: " + j);
            j++;
        }

        //do-while: Similar al bucle while, pero garantiza que el bloque de código se ejecute al menos una vez antes de verificar la condición.
        int num;
        do
        {
            Console.Write("Introduce un número positivo: ");
            num = int.Parse(Console.ReadLine());
        } while (num <= 0);
        Console.WriteLine("Has introducido: " + num);

        //foreach: Se utiliza para iterar sobre los elementos de una colección o arreglo.
        int[] numeros = { 1, 2, 3, 4, 5 };

        foreach (int numero in numeros)
        {
            Console.WriteLine(numero);
        }

        //break: Se utiliza para salir de un bucle o de un bloque switch antes de que se complete su ejecución.
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine("Número: " + i);

            if (i == 5)
            {
                Console.WriteLine("¡Se ha encontrado el número 5! Saliendo del bucle.");
                break;
            }
        }

        //continue: Se utiliza para omitir el resto del código en un bucle y pasar a la siguiente iteración.
        for (int i = 1; i <= 5; i++)
        {
            if (i == 3)
            {
                Console.WriteLine("Saltando la iteración para el número 3.");
                continue;
            }

            Console.WriteLine("Número: " + i);
        }

        //return: Se utiliza para devolver un valor de una función y salir de ella.
        static int Sumar(int a, int b)
        {
            int suma = a + b;

            return suma;
        }

    }
}