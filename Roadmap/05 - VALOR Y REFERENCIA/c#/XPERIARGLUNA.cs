using System;
using System.Collections.Generic;

class Persona
{
    public string Nombre;
}

class Program
{
    // -------- FUNCIONES PARA COMPROBAR PASO POR VALOR Y REFERENCIA --------

    static void CambiarValor(int x)
    {
        x = 999;
        Console.WriteLine($"Dentro de CambiarValor: x = {x}");
    }

    static void CambiarPorReferencia(ref int x)
    {
        x = 888;
        Console.WriteLine($"Dentro de CambiarPorReferencia: x = {x}");
    }

    static void CambiarNombrePersona(Persona p)
    {
        p.Nombre = "Juan";
        Console.WriteLine($"Dentro de CambiarNombrePersona: p.Nombre = {p.Nombre}");
    }

    // -------- FUNCIONES PARA INTERCAMBIAR VALORES --------

    static (int, int) IntercambiarPorValor(int a, int b)
    {
        int temp = a;
        a = b;
        b = temp;
        return (a, b);
    }

    static void IntercambiarPorReferencia(ref int a, ref int b)
    {
        int temp = a;
        a = b;
        b = temp;
    }

    // -------- MAIN --------

    static void Main(string[] args)
    {
        // -------- ASIGNACIÓN POR VALOR --------
        int a = 10;
        int b = a;
        b = 20;
        Console.WriteLine("== Asignación por VALOR ==");
        Console.WriteLine($"a = {a}, b = {b}\n");

        // -------- ASIGNACIÓN POR REFERENCIA --------
        int[] array1 = { 1, 2, 3 };
        int[] array2 = array1;
        array2[0] = 99;
        Console.WriteLine("== Asignación por REFERENCIA ==");
        Console.WriteLine($"array1[0] = {array1[0]}, array2[0] = {array2[0]}\n");

        // -------- FUNCIONES: PASO POR VALOR --------
        int valor = 100;
        CambiarValor(valor);
        Console.WriteLine($"Después de CambiarValor: valor = {valor}\n");

        // -------- FUNCIONES: PASO POR REFERENCIA --------
        int refValor = 100;
        CambiarPorReferencia(ref refValor);
        Console.WriteLine($"Después de CambiarPorReferencia: refValor = {refValor}\n");

        // -------- FUNCIONES: OBJETOS PASADOS POR VALOR (REFERENCIA INTERNA) --------
        Persona persona = new Persona();
        persona.Nombre = "Ana";
        CambiarNombrePersona(persona);
        Console.WriteLine($"Después de CambiarNombrePersona: persona.Nombre = {persona.Nombre}\n");

        // -------- INTERCAMBIO POR VALOR --------
        int a1 = 5;
        int b1 = 10;
        var (nuevoA1, nuevoB1) = IntercambiarPorValor(a1, b1);

        Console.WriteLine("== Intercambio por VALOR ==");
        Console.WriteLine($"Originales: a1 = {a1}, b1 = {b1}");
        Console.WriteLine($"Nuevas: nuevoA1 = {nuevoA1}, nuevoB1 = {nuevoB1}\n");

        // -------- INTERCAMBIO POR REFERENCIA --------
        int a2 = 15;
        int b2 = 30;
        int copiaA2 = a2;
        int copiaB2 = b2;

        IntercambiarPorReferencia(ref a2, ref b2);
        int nuevoA2 = a2;
        int nuevoB2 = b2;

        Console.WriteLine("== Intercambio por REFERENCIA ==");
        Console.WriteLine($"Originales antes: copiaA2 = {copiaA2}, copiaB2 = {copiaB2}");
        Console.WriteLine($"Nuevas (modificadas): nuevoA2 = {nuevoA2}, nuevoB2 = {nuevoB2}");
    }
}
