/*
 * El principio de Segregación de Interfaces dice que
 * "Los clientes no deben de ser forzados a depender
 * de métodos que no utilizan". Esto evita crear interfaces
 * con demasiados métodos que no todas las clases que implementen
 * la interfas van a utilizar, por lo que estos métodos no tendrán
 * implementación. Es un principio parecido al de Sustitución de 
 * Liskov pero enfocado a las interfaces.
 */

// Incorrecto
/*
 * Creamos una interfaz que contiene varios métodos
 * para realizar un CRUD para diferentes tipos de 
 * entidades
 */
interface ICrud<T>
{
    public List<T> GetList();
    public T Get(int id);
    public void Add(T entity);
    public void Update(T entity);
    public void Delete(T entity);

}
/*
 * Este primer servicio encargado de la clase User
 * implementa todas las operaciones de la interfaz
 * ICrud
 */
class UserService : ICrud<User>
{
    public List<User> GetList()
    {
        Console.WriteLine("Se obtiene lista de usuarios");
        return new List<User>();
    }
    public User Get(int id)
    {
        Console.WriteLine("Se obtiene usuario");
        return new User();
    }
    public void Add(User user) => Console.WriteLine($"Se agrega nuevo usuario {user.Name}.- {user.Name}");
    public void Update(User user) => Console.WriteLine($"Se actualiza usuario {user.Id}.- {user.Name}");
    public void Delete(User user) => Console.WriteLine($"Se elimina usuario {user.Id}.- {user.Name}");
}
/*
 * El siguiente servicio encargado de las transacción
 * realmente solo implementa los métodos de obtener y
 * agregar nuevas transacciones que por lógica de 
 * negocio no es posible modificarlas o eliminarlas
 */
class TransactionsService : ICrud<Transaction>
{
    public List<Transaction> GetList()
    {
        Console.WriteLine("Se obtiene lista de transacciones");
        return new List<Transaction>();
    }
    public Transaction Get(int id)
    {
        Console.WriteLine("Se obtiene transacción");
        return new Transaction();
    }
    public void Add(Transaction transaction)
    {
        Console.WriteLine("Se guardó transacción");
    }

    /*
     * Los métodos Delete() y Update() arrojarán una excepción ya 
     * que no se tiene una implementación debido a reglas de negocio
     */
    public void Delete(Transaction transaction)
    {
        throw new NotImplementedException();
    }
    public void Update(Transaction transaction)
    {
        throw new NotImplementedException();
    }
}
// Correcto
/*
 * Separamos la interfaz anterior en dos, una que
 * contenga los método que ambos servicio implementan
 * y otra que contenga los métodos de actualizar y
 * eliminar
 */
interface IBasicCrud<T>
{
    public List<T> GetList();
    public T Get(int id);
    public void Add(T entity);
}
interface IEditableCrud<T>
{
    public void Update(T entity);
    public void Delete(T entity);
}
/*
 * Ahora los nuevos servicios pueden implementar la intrefaz
 * que contenga solo los métodos requeridos
 */
class UserServiceISP : IBasicCrud<User>, IEditableCrud<User>
{
    public List<User> GetList()
    {
        Console.WriteLine("Se obtiene lista de usuarios");
        return new List<User>();
    }
    public User Get(int id)
    {
        Console.WriteLine("Se obtiene usuario");
        return new User();
    }
    public void Add(User user) => Console.WriteLine($"Se agrega nuevo usuario {user.Name}.- {user.Name}");
    public void Update(User user) => Console.WriteLine($"Se actualiza usuario {user.Id}.- {user.Name}");
    public void Delete(User user) => Console.WriteLine($"Se elimina usuario {user.Id}.- {user.Name}");
}
class TransactionServiceISP : IBasicCrud<Transaction>
{
    public List<Transaction> GetList()
    {
        Console.WriteLine("Se obtiene lista de transacciones");
        return new List<Transaction>();
    }
    public Transaction Get(int id)
    {
        Console.WriteLine("Se obtiene transacción");
        return new Transaction();
    }
    public void Add(Transaction transaction)
    {
        Console.WriteLine("Se guardó transacción");
    }
}

/*
 * Las siguientes clases representan modelos en la base de 
 * datos, uno para una tabla de usuarios y otra para 
 * transacciones realizadas en el sistema.
 */
class User
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
}
class Transaction
{
    public int Id { get; set; }
    public int UserId { get; set; }
    public DateTime Date { get; set; }
}
// Ejercicio Extra
interface IPrinter
{
    public void Print(string doc);
}
interface IColorPrinter
{
    public void PrintColor(string doc);
}
interface IScanner
{
    public void Scan(string doc);
}
interface IFax
{
    public void SendFax(string doc);
}

class Printer : IPrinter
{
    public void Print(string doc) => Console.WriteLine($"Imprimiendo documento {doc} en blanco y negro...");
}
class ColorPrinter : IColorPrinter
{
    public void PrintColor(string doc) => Console.WriteLine($"Imprimiendo documento {doc} a color...");
}
class MultiFunctionPrinter : IPrinter, IColorPrinter, IScanner, IFax
{
    public void Print(string doc) => Console.WriteLine($"Imprimiendo documento {doc} en blanco y negro...");
    public void PrintColor(string doc) => Console.WriteLine($"Imprimiendo documento {doc} a color...");
    public void Scan(string doc) => Console.WriteLine($"Esanenado documento {doc}...");
    public void SendFax(string doc) => Console.WriteLine($"Envíando documento {doc} por fax...");

}
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("----Principio de Segregación de Interfaces----");
        Console.WriteLine("---Incorrecto---");
        // Incorrecto
        UserService userService = new UserService();
        var userList = userService.GetList();
        var user = userService.Get(1);
        userService.Add(new User());
        userService.Update(user);
        userService.Delete(user);

        TransactionsService transactionsService = new TransactionsService();
        var transactionList = transactionsService.GetList();
        var transaction = transactionsService.Get(1);
        transactionsService.Add(new Transaction());
        try
        {
            transactionsService.Update(transaction);
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
        try
        {
            transactionsService.Delete(transaction);
        } 
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }

        Console.WriteLine("---Correcto---");
        UserServiceISP userServiceISP = new UserServiceISP();
        userList = userServiceISP.GetList();
        user = userServiceISP.Get(1);
        userServiceISP.Add(new User());
        userServiceISP.Update(user);
        userServiceISP.Delete(user);

        TransactionServiceISP transactionServiceISP = new TransactionServiceISP();
        transactionList = transactionServiceISP.GetList();
        transaction = transactionServiceISP.Get(1);
        transactionServiceISP.Add(new Transaction());

        // Ejercicio Extra
        Console.WriteLine("---Ejercicio Extra---");
        Printer printer = new Printer();
        printer.Print("holamundo.pdf");
        
        ColorPrinter colorPrinter = new ColorPrinter();
        colorPrinter.PrintColor("holamundo.pdf");

        MultiFunctionPrinter multiFunctionPrinter = new MultiFunctionPrinter();
        multiFunctionPrinter.Print("holamundo.pdf");
        multiFunctionPrinter.PrintColor("holamundo.pdf");
        multiFunctionPrinter.Scan("holamundo.pdf");
        multiFunctionPrinter.SendFax("holamundo.txt");
        Console.ReadLine();
    }
}