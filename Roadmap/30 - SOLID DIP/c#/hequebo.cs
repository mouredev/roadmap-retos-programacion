/*
 * El Principio de Inversión de Dependencia (DIP) nos dice
 * que la lógica debe de ser separada en módulos o servicios
 * que puedan ser reutilizados y si se deben de modificar
 * solo estos servicios se verán afectados. Los módulos de
 * alto nivel no deben depender de modulos de bajo nivel
 * si no de abstracciones
 */
// Incorrecto 
/*
 * Creamos un servicio o módulo encargado de trar información
 * de un archivo en una ruta específica. Este servicio lo 
 * usaremos dentro de otra clase
 */
class InfoFile
{
    private string _path;

    public InfoFile(string path)
    {
        _path = path;
    }
    public void GetInfo() => Console.WriteLine($"Se lee información de archivo en: {_path}...");
}
/*
 * La clase Monitor Depende del servicio FileInfo 
 * ya que utiliza la función GetInfo(), el principio
 * de Inversión de Dependencia se rompe ya que dentro
 * del módulo de nivel superior estamos creando una 
 * instancia del módulo de nivel inferior, si este
 * módulo fuera a ser remplazado y ahora se leyera
 * la información de otra fuente se tendría que 
 * buscar todas las partes del sistema donde se
 * tenga esta dependencia y modificarla
 */
class Monitor
{
    string _path;
    public Monitor(string path) 
    {
        _path = path;
    }
    public void GetInfo()
    {
        InfoFile infoFile = new InfoFile(_path);
        infoFile.GetInfo();
    }

}
// Correcto 
/*
 * Se crea una interfaz con el método que debe de ser
 * implementado por las clases
 */
interface IInfo
{
    public void GetInfo();
}
/*
 * Las siguientes clases implementan la interfaz
 * IInfo, una simula conectarse a una base de
 * datos mientras que la otra a un API
 */
class InfoDB : IInfo
{
    private string _connectionString;
    public InfoDB(string connectionString)
    {
        _connectionString = connectionString;
    }
    public void GetInfo() => Console.WriteLine("Se realiza conexión a base de datos...");
}
class InfoHttp : IInfo
{
    private string _url;
    public InfoHttp(string url)
    {
        _url = url;
    }
    public void GetInfo() => Console.WriteLine("Se realiza conexión a endpoint...");
}
class MonitorDIP
{
    private IInfo _info;

    /*
     * El servicio se obtiene ahora en el constructor ya creado
     * en lugar de ser creado en la clase, El constructor espera
     * recibir cualquier clase que implemente la interfaz IInfo
     */
    public MonitorDIP(IInfo info)
    {
        _info = info;
    }
    public void GetInfo() => _info.GetInfo();
}

// Ejercicio Extra

interface INotification
{
    public void Send();
}
class EmailNotification : INotification
{
    private string _content;

    public EmailNotification(string content)
    {
        _content = content;
    }

    public void Send() => Console.WriteLine("Se envía notificación a correo electrónico...");
}
class PushNotification : INotification
{
    private string _content;

    public PushNotification(string content)
    {
        _content = content;
    }

    public void Send() => Console.WriteLine("Se envía notificación push...");
}

class SMSNotification : INotification
{
    private string _content;

    public SMSNotification(string content)
    {
        _content = content;
    }
    public void Send() => Console.WriteLine("Se envía notificación por SMS...");
}

class NotificationSystem
{
    private INotification _notification;

    public NotificationSystem(INotification notification)
    {
        _notification = notification;
    }

    public void Send() => _notification.Send();
}
class Program
{
    static void Main(string[] args)
    {
        // Incorrecto
        string path = "info.txt";
        Monitor monitor = new Monitor(path);
        monitor.GetInfo();

        // Correcto
        string connectionString = "Data source=server; Initial Catalog=database;User=user; Password=password";
        InfoDB infoDB = new InfoDB(connectionString);
        MonitorDIP monitorDB = new MonitorDIP(infoDB);
        monitorDB.GetInfo();

        string url = "https://jsonplaceholder.typicode.com/posts";
        InfoHttp infoHttp = new InfoHttp(url);
        MonitorDIP monitorHttp = new MonitorDIP(infoHttp);
        monitorHttp.GetInfo();

        // Ejercicio Extra
        string content = "Contenido de la notificación";
        EmailNotification emailNotification = new EmailNotification(content);
        NotificationSystem notificationSystem = new NotificationSystem(emailNotification);
        notificationSystem.Send();

        PushNotification pushNotification = new PushNotification(content);
        notificationSystem = new NotificationSystem(pushNotification);
        notificationSystem.Send();

        SMSNotification smsNotification = new SMSNotification(content);
        notificationSystem = new NotificationSystem(smsNotification);
        notificationSystem.Send();

    }
}