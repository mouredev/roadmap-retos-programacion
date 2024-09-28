namespace exs29;
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
-----------------------------------------------------
* SOLID: PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP)
-----------------------------------------------------
- Una clase no debería estar obligada a implementar interfaces que no utiliza.
  Evitando crear grandes clases monolíticas.
*/

// NOTA: Este ejemplo muestra el uso CORRECTO. Para suponer un ejemplo que viole el principio, sería. 
//       Imaginar todos los métodos siguientes, en una sola interfaz, entonces algunos animales
//       implementarían una interfaz que no utilizarían.

public interface IFlyable
{
    void Fly();
}

public interface ISwimmable
{
    void Swim();
}

// ____________________________
// Implementar
public class Fish : ISwimmable
{
    public void Swim()
    {
        Console.WriteLine("El pez está nadando.");
    }
}

public class Duck : IFlyable, ISwimmable
{
    public void Fly()
    {
        Console.WriteLine("El pato está volando.");
    }

    public void Swim()
    {
        Console.WriteLine("El pato está nadando.");
    }
}

/*
_______________
 * EJERCICIO:
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
*/

public interface IPrinter
{
    void PrintFile(string file);
}

public interface IScanner
{
    void ToScan(string pathSave);
}

public interface IFax
{
    void SendFile(string file, int phoneNumber);
}

// ____________________________
// Implementar
public class MonoPrinter : IPrinter
{
    public void PrintFile(string file)
    {
        Console.WriteLine("\nImpresora blanco y negro:");
        Console.WriteLine(file + " se imprimió.");
    }
}

public class ColorPrinter : IPrinter
{
    public void PrintFile(string file)
    {
        Console.WriteLine("\nImpresora a color:");
        Console.WriteLine(file + " se imprimió.");
    }
}

public class Scanner : IScanner
{
    public void ToScan(string pathSave)
    {
        Console.WriteLine("\nEscaneo realizado, Guardado en: " + pathSave);
    }
}

public class Fax : IFax
{
    public void SendFile(string file, int phoneNumber)
    {
        Console.WriteLine("\n-" + file + " Fue enviado a: " + phoneNumber);
    }
}

public class MultiFunctionPrinter
{
    public IPrinter monoPrinter = new MonoPrinter();
    public IPrinter colorPrinter = new ColorPrinter();
    public IScanner theScanner = new Scanner();
    public IFax fax = new Fax();
}

//__________________
public class Program
{
    static void Main()
    {
        Fish theFish = new();
        Duck theDuck = new();
        theFish.Swim();
        theDuck.Swim();
        theDuck.Fly();
        
        //___________________________
        // exs 2
        MonoPrinter monoPrinter = new();
        monoPrinter.PrintFile("filex.pdf");

        ColorPrinter colorPrinter = new();
        colorPrinter.PrintFile("filex.pdf");

        Scanner theScanner = new ();
        theScanner.ToScan("c:\\docs");

        Fax fax = new();
        fax.SendFile("filex.pdf", 12345678);

        Console.WriteLine("\n___________\nMultifunción:");

        MultiFunctionPrinter multiFunctionPrinter = new();
        multiFunctionPrinter.monoPrinter.PrintFile("filex.pdf");
        multiFunctionPrinter.colorPrinter.PrintFile("filex.pdf");
        multiFunctionPrinter.theScanner.ToScan("c:\\docs");
        multiFunctionPrinter.fax.SendFile("filex.pdf", 12345678);

    }
}
