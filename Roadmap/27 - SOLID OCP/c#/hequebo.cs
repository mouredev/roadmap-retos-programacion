/*
 * El Principio Abierto Cerrado (SRP)
 * nos dice que una clase tiene que estar
 * abierta para su extensión pero cerrada
 * para su modificación
 */
class Program
{
    static void Main(string[] args)
    {
        // Incorrecto 
        Shape square = new Shape();
        square.Width = 3; 
        square.Height = 3;
        AreaCalculator areaCalculator = new AreaCalculator();
        double area = areaCalculator.CalculateArea(square);
        Console.WriteLine($"El área es de {area}m2");

        // Correcto
        Rectangle rectangle = new Rectangle();
        rectangle.Width = 3;
        rectangle.Height = 5;
        AreaCalculatorOCP areaCalculatorOCP = new AreaCalculatorOCP();
        area = areaCalculatorOCP.CalculateArea(rectangle);
        Console.WriteLine($"El área es de {area}m2");

        Circle circle = new Circle();
        circle.Radius = 5.2;
        area = areaCalculatorOCP.CalculateArea(circle);
        Console.WriteLine($"El área es de {area}m2");

        // Ejercicio Extra
        Console.WriteLine("---Ejercicio Extra---");
        Calculator calculator = new Calculator();
        calculator.AddOperation("Suma", new Addition());
        calculator.AddOperation("Resta", new Substraction());
        calculator.AddOperation("Multiplicación", new Multiplication());
        calculator.AddOperation("División", new Division());
        calculator.AddOperation("Potencia", new Pow());

        Console.WriteLine($"2 + 3 = {calculator.ExecuteOperation("Suma", 2, 3)}");
        Console.WriteLine($"2 - 3 = {calculator.ExecuteOperation("Resta", 2, 3)}");
        Console.WriteLine($"2 * 3 = {calculator.ExecuteOperation("Multiplicación", 2, 3)}");
        Console.WriteLine($"2 / 3 = {calculator.ExecuteOperation("División", 2, 3)}");
        Console.WriteLine($"2^3 = {calculator.ExecuteOperation("Potencia", 2, 3)}");

    }
}

// Incorrecto 
class Shape
{
    public double Width {  get; set; }
    public double Height { get; set; }

}
class AreaCalculator
{
    /*
     * La función CalculateArea solo funciona
     * para rectangulos. Si quisieramos calcular
     * el área de otras formas la función tendría
     * que ser modificada, lo cual rompe el principio
     * de Abierto Cerrado
     */
    public double CalculateArea(Shape shape) => shape.Width * shape.Height;
}

// Correcto
/*
 * Para cumplir con el principio Abierto Cerrado
 * podemos utilizar abstracción y herencia para
 * crear clases separadas para cada tipo de forma
 * y proveer un metodo consistente para el cálculo
 * de su area
 */
interface IShape
{
    public double CalculateArea();
}
class Rectangle : IShape
{
    public double Height { get; set; }
    public double Width { get; set; }

    public double CalculateArea() => Height * Width;
}
class Circle : IShape
{
    public double Radius { get; set; }

    public double CalculateArea() => Math.PI * Math.Pow(Radius, 2);
}
class AreaCalculatorOCP
{
    public double CalculateArea(IShape shape) => shape.CalculateArea();
}

// Ejercicio Extra
interface IOperation
{
    public double Execute(double a, double b);
}
class Addition : IOperation
{

    public double Execute(double a, double b) => a + b; 
}
class Substraction : IOperation
{
    public double Execute(double a, double b) => a - b;
}
class Multiplication : IOperation
{
    public double Execute(double a, double b) => a * b;
}
class Division : IOperation
{
    public double Execute(double a, double b) => a / b;
}
class Pow : IOperation
{
    public double Execute(double a, double b) => Math.Pow(a, b);
}
class Calculator
{
    private Dictionary<string, IOperation> _operations;

    public Calculator()
    {
        _operations = new Dictionary<string, IOperation>();
    }

    public void AddOperation(string name, IOperation operation) => _operations.Add(name, operation);
    public double ExecuteOperation(string name, double a, double b)
    {
        if (!_operations.ContainsKey(name))
        {
            Console.WriteLine("La operación no existe");
            return 0; 
        }
        return _operations[name].Execute(a, b);
    }
}