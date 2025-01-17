/*
 * El principio de sustitución de Liskov (LSP)
 * establece que los objetos de una clase padre
 * deben poder ser reemplazados por objetos de 
 * clases hijas sin alterar la integridad del 
 * programa
 */
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("---Principio de Sustitución de Liskov---");
        // Incorrecto
        AbstractSale sale = new Sale(500);
        sale.Generate();
        Console.WriteLine($"El impuesto es de ${sale.CalculateTax()}");
        Console.WriteLine($"El total es de ${sale.GetTotal()}");
        Console.WriteLine();

        AbstractSale saleWithoutTax = new SaleWithoutTax(500);
        saleWithoutTax.Generate();
        /*
         * Si se intenta ejecutar estos métodos el sistema se
         * rompe por lo que se rompería el principio de sustutución de Liskov
         */
        // Console.WriteLine($"El impuesto es de ${saleWithoutTax.CalculateTax()}");
        // Console.WriteLine($"El total es de ${saleWithoutTax.GetTotal()}");
        Console.WriteLine();
        // Correcto

        SaleWithTaxes localSale = new LocalSale(500);
        localSale.Generate();
        Console.WriteLine($"El impuesto es de ${localSale.CalculateTax()}");
        Console.WriteLine($"El total es de ${localSale.GetTotal()}");
        Console.WriteLine();

        AbstractSaleLSP saleLSP = new SaleWithoutTaxes(500);
        saleLSP.Generate();
        Console.WriteLine();

        // Ejercicio extra
        Console.WriteLine("---Ejercicio Extra---");
        Vehicle car = new Car(50);
        car.Accelerate(15);
        car.Brake(5); 
        Console.WriteLine();

        Vehicle moto = new Motorcycle(40);
        moto.Accelerate(20);
        moto.Brake(30);
        Console.WriteLine();

        Vehicle truck = new Truck(80);
        truck.Accelerate(30);
        truck.Brake(110);

        Console.ReadLine();
    }
}
// Incorecto
/*
 * Creamos una clase padre para ventas
 * con tres campos para el importe, el
 * impuesto y el total y tres métodos
 * para generar la venta, calcular el 
 * impuesto y obtener el total 
 */
abstract class AbstractSale
{
    protected decimal _amount;
    protected decimal _tax;
    protected decimal _total;

    public abstract void Generate();
    public abstract decimal CalculateTax();
    public abstract decimal GetTotal();
}

/*
 * Se crea una clase hija la cual
 * implementa los metodos de la clase
 * padre
 */
class Sale : AbstractSale
{
    public Sale(decimal amount)
    {
        _amount = amount;
    }
    public override void Generate()
    {
        Console.WriteLine("Se genera venta");
    }
    public override decimal CalculateTax()
    {
        _tax = _amount * 0.16m;
        return _tax;
    }
    public override decimal GetTotal()
    {
        _total = _amount + _tax;
        return _total;
    }
}
/*
 * Se crea una segunda clase la cual
 * está pensada para no calcular 
 * impuestos, por lo que al no tener
 * una implementación de estos métodos
 * se arrojará una excepción
 */
class SaleWithoutTax: AbstractSale
{
    public SaleWithoutTax(decimal amount)
    {
        _amount = amount;
    }

    public override void Generate()
    {
        Console.WriteLine("Se genera venta sin Impuestos");
    }
    public override decimal CalculateTax()
    {
        throw new NotImplementedException();
    }
    public override decimal GetTotal()
    {
        throw new NotImplementedException();
    }
}

// Correcto 
/*
 * Se crea la clase padre con lo mínimo que 
 * necesita una venta, en este ejemplo el monto
 * y el método generar
 */
abstract class AbstractSaleLSP
{
    protected decimal _amount;
    public abstract void Generate();
}
/*
 * Podemos crear una segunada clase abstracta
 * que incluya el impuesto y un metodo que lo
 * genere, esta a su vez hereda de la clase
 * AbstractSaleLSP
 */
abstract class SaleWithTaxes : AbstractSaleLSP
{
    protected decimal _tax;
    protected decimal _total;

    public abstract decimal CalculateTax();
    public abstract decimal GetTotal();
}
/*
 * La clase LocalSale hereda de la clase SaleWithTaxes
 * y a su ves de AbstractSaleLSP por lo que implementa
 * todos los métodos que tiene estas clases padre
 */
class LocalSale: SaleWithTaxes
{
    public LocalSale(decimal amount)
    {
        _amount = amount;
    }
    public override void Generate()
    {
        Console.WriteLine("Se genera la venta con impuestos");
    }
    public override decimal CalculateTax()
    {
        _tax = _amount * 0.16m;
        return _tax;
    }
    public override decimal GetTotal()
    {
        _total = _amount + _tax;
        return _total;
    }
}
/*
 * Ahora podemos crear una clase que solo herede de
 * AbstractSaleLSP por lo que solo debe de implementar
 * el método Generate()
 */
class SaleWithoutTaxes : AbstractSaleLSP
{
    public SaleWithoutTaxes(decimal amount)
    {
        _amount = amount;
    }
    public override void Generate() => Console.WriteLine("Se genera venta sin impuestos");
}

// Ejercicio Extra
class Vehicle
{
    public int Speed;
    public Vehicle(int speed)
    {
        Speed = speed;
    }

    public virtual void Accelerate(int speed) => Speed += speed;
    public virtual void Brake(int speed)
    {
        Speed += speed;
        if (Speed > 0)
            Speed = 0;
    }
}
class Car : Vehicle
{
    public Car(int speed) : base(speed) { }
    public override void Accelerate(int speed)
    {
        Console.WriteLine("El auto acelera");
        base.Accelerate(speed);
        Console.WriteLine($"La velocidad del auto es de {Speed}km/h");
    }
    public override void Brake(int speed)
    {
        Console.WriteLine("El auto frena");
        base.Brake(speed);
        if (Speed == 0)
            Console.WriteLine("El auto se ha detenido por completo");
    }
}

class Motorcycle : Vehicle
{
    public Motorcycle(int speed) : base(speed) { }
    public override void Accelerate(int speed)
    {
        Console.WriteLine("La moto acelera");
        base.Accelerate(speed);
        Console.WriteLine($"La velocidad de la moto es de {Speed}km/h");
    }
    public override void Brake(int speed)
    {
        Console.WriteLine("La moto frena");
        base.Brake(speed);
        if (Speed == 0)
            Console.WriteLine("La moto se ha detenido por completo");
    }
}

class Truck : Vehicle
{
    public Truck(int speed) : base(speed) { }
    public override void Accelerate(int speed)
    {
        Console.WriteLine("El camión acelera");
        base.Accelerate(speed);
        Console.WriteLine($"La velocidad del camión es de {Speed}km/h");
    }
    public override void Brake(int speed)
    {
        Console.WriteLine("El camión frena");
        base.Brake(speed);
        if (Speed == 0)
            Console.WriteLine("El camión se ha detenido por completo");
    }
}