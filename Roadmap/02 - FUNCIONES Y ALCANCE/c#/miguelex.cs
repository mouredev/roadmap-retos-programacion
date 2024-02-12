class miguelex
{
    static void holaMundo(){
        Console.WriteLine("Hola Mundo");
    }

    static void saludo (string nombre){
        Console.WriteLine("Hola " + nombre);
    }

    static int suma (int a, int b){
        return a + b;
    }

    // Funcion declarada dentro de otra funcion

    static void funcionExterna(){
        Console.WriteLine("Funcion externa");
        void funcionInterna(){
            Console.WriteLine("Funcion interna");
        }
        funcionInterna();
    }

    // Funcion con parametros por defecto

    static void porDefecto(int a = 0, int b = 0){
        Console.WriteLine("El valor de a es : " + a);
        Console.WriteLine("El valor de b es : " + b);
    }

    static int Extra(string param1, string param2 ){
        int contador = 0;
        for (int i = 0; i < 100; i++){
            if (i % 15 == 0){
                Console.WriteLine(param1+param2);
            }
            else if (i % 3 == 0){
                Console.WriteLine(param1);
            }
            else if (i % 5 == 0){
                Console.WriteLine(param2);
            }
            else{
                Console.WriteLine(i);
                contador++;
            }
        }
        return contador;
    }

    static void Main(string[] args)
    {
        holaMundo();
        saludo("Miguel");
        Console.WriteLine("Resultado de la suma de 5 y 5 : " + suma(5, 3));
        funcionExterna();
        Console.WriteLine("Ejemplo de funcion del sistema Math.Pow(2,3) : " + Math.Pow(2,3));
        Console.Write("Funcion por defecto sin ningun parametro ");
        porDefecto();
        Console.WriteLine("Funcion por defecto con un parametro ");
        porDefecto(5);
        Console.WriteLine("Funcion por defecto con dos parametros "); 
        porDefecto(5, 10);
        Console.WriteLine("Se han imprimido " + Extra("Fizz", "Buzz") + " numeros");
    }
        
}
