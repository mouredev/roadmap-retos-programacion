namespace exs30;
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
-----------------------------------------------------
* SOLID: PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP)
-----------------------------------------------------
- Los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de abstracciones. A su vez, las 
  abstracciones no deben depender de detalles concretos; los detalles deben depender de las abstracciones.

___________________________________________________
* EJERCICIO #1:
* Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
* Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
* de forma correcta e incorrecta.
*/

// ________________________________________________
// De manera INCORRECTA:

public class Printer_
{
    public static void Print(string content)
    {
        Console.WriteLine("Impresión: " + content);
    }
}

public class Report_
{
    public static void GenerateReport(string content)
    {
        Console.WriteLine("Generando informe, contenido: " + content);

        // Dependencia directa
        Printer_.Print(content);
    }
}

// ________________________________________________
// De manera CORRECTA:

public interface IPrinter
{
     void Print(string content);
}

public class Printer : IPrinter
{
    public void Print(string content)
    {
        Console.WriteLine("Impresión: " + content);
    }
}

public class Report(IPrinter printer)
{
    // Ya no esta dependiendo de un modulo de bajo nivel.
    private readonly IPrinter _printer = printer;

    public void GenerateReport(string content)
    {
        Console.WriteLine("Generando informe, contenido: " + content);
        _printer.Print(content);
    }
}

/*
___________________________________________________
* EJERCICIO #2:
* Crea un sistema de notificaciones.
* Requisitos:
* 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
* 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
* Instrucciones:
* 1. Crea la interfaz o clase abstracta.
* 2. Desarrolla las implementaciones específicas.
* 3. Crea el sistema de notificaciones usando el DIP.
* 4. Desarrolla un código que compruebe que se cumple el principio.
*/

public interface INotificationService
{
    void Send(object To, string Msg);
}

// Implementación
public class EmailService : INotificationService
{
    public void Send(object To, string Msg)
    {
        Console.WriteLine($"Correo enviado a: {To}");
        Console.WriteLine($"Mensaje: {Msg}");
    }
}

// Implementación
public class PUSHService : INotificationService
{
    public void Send(object To, string Msg)
    {
        Console.WriteLine($"Notificación PUSH enviada a: {To}");
        Console.WriteLine($"Mensaje: {Msg}");
    }
}

// Implementación
public class SMSService : INotificationService
{
    public void Send(object To, string Msg)
    {
        Console.WriteLine($"Mensaje SMS enviado a: {To}");
        Console.WriteLine($"Mensaje: {Msg}");
    }
}

// Clase de alto nivel
public class NotificationSystem(INotificationService Service)
{
    // Depende de la interfaz y no de implementaciones concretas.
    private readonly INotificationService _Service = Service;

    public void Notify(object To, string Msg)
    {
        _Service.Send(To, Msg);
    }

}

// ________________________________________________
public class Program
{
    // Comprobación
    public static void TestNotificationSystem(object To, string Msg, INotificationService Service)
    {
        // Inyeccion
        NotificationSystem ServiceNotifer = new(Service);
        ServiceNotifer.Notify(To, Msg);
    }

    public static void Main()
    {
        //________________________________
        Console.WriteLine("EJERCICIO #1");

        // Imlementacion incorrecta
        Report_.GenerateReport("Contenido x");

        // Imlementacion correcta
        IPrinter printer = new Printer(); // Crear intancia
        Report report = new(printer); // inyectar

        report.GenerateReport("Contenido x");

        //________________________________
        Console.WriteLine("\nEJERCICIO #2");

        // Intancias de las implementaciones:
        INotificationService emailService = new EmailService();
        INotificationService pushService = new PUSHService();
        INotificationService smsService = new SMSService();

        // Pruebas
        TestNotificationSystem("ejm@gg.com", "abcdsf", emailService);
        TestNotificationSystem("user01", "123456", pushService);
        TestNotificationSystem(123456789, "aeiou", smsService);
    }
}
