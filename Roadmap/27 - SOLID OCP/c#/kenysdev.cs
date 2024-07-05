namespace exs27;
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
-------------------------------------------------
* SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
-------------------------------------------------
- Una entidad de software que está abierta a extensión, pero cerrada a modificación, 
  esto significa que debemos poder extender el comportamiento de una clase sin 
  necesidad de modificar su código fuente original.

_______________
* EJERCICIO #1:
* Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
* y crea un ejemplo simple donde se muestre su funcionamiento
* de forma correcta e incorrecta.
*/

// Abstract base class Product
public abstract class Product(string name, decimal price)
{
    public string Name { get; set; } = name;
    public decimal Price { get; set; } = price;

    // Abstract method
    public abstract decimal ApplyDiscount();

    // Concrete metho
    public decimal FinalPrice()
    {
        return Price - ApplyDiscount();
    }
}

// Concrete class
public class ElectronicsProduct(string name, decimal price) : Product(name, price)
{
    public override decimal ApplyDiscount()
    {
        return Price * 0.05m; // Discount of 5%
    }
}


// Concrete class
public class ClothingProduct(string name, decimal price) : Product(name, price)
{
    public override decimal ApplyDiscount()
    {
        if (Price > 50)
            return 10; // Discount of $10 if price is over $50
        else
            return 0; // No discount otherwise
    }
}

/*
_______________
* EJERCICIO #2:
* Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
* Requisitos:
* - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
* Instrucciones:
* 1. Implementa las operaciones de suma, resta, multiplicación y división.
* 2. Comprueba que el sistema funciona.
* 3. Agrega una quinta operación para calcular potencias.
* 4. Comprueba que se cumple el OCP.
*/

// Abstract base
public abstract class Calculator(double a, double b)
{
    protected double a = a;
    protected double b = b;

    // Abstract method
    public abstract double MathOperation();

    // Concrete method
    public void PrintResult()
    {
        Console.WriteLine($"Es: {MathOperation()}");
    }
}

public class Sum(double a, double b) : Calculator(a, b)
{
    public override double MathOperation()
    {
        Console.WriteLine($"\nSuma de {a} + {b}:");
        return a + b;
    }
}

public class Subtraction(double a, double b) : Calculator(a, b)
{
    public override double MathOperation()
    {
        Console.WriteLine($"\nResta de {a} - {b}:");
        return a - b;
    }
}

public class Multiplication(double a, double b) : Calculator(a, b)
{
    public override double MathOperation()
    {
        Console.WriteLine($"\nMultiplicación de {a} * {b}:");
        return a * b;
    }
}

public class Division(double a, double b) : Calculator(a, b)
{
    public override double MathOperation()
    {
        Console.WriteLine($"\nDivisión de {a} / {b}:");
        if (b != 0)
            return a / b;
        else
            throw new ArgumentException("DivisionErrorbyZero.");
    }
}

public class Pow(double a, double b) : Calculator(a, b)
{
    public override double MathOperation()
    {
        Console.WriteLine($"\nPotencia de {a} ^ {b}:");
        return Math.Pow(a, b);
    }
}

//__________________
public class Program
{
    public static void ProcessProduct(Product product)
    {
        Console.WriteLine($"Producto: {product.Name}, Precio final: {product.FinalPrice()}");
    }

    static void Main()
    {
        ElectronicsProduct laptop = new("Laptop", 700 );
        ClothingProduct pants = new("Pants", 55);

        ProcessProduct(laptop);
        ProcessProduct(pants);

        //___________________________
        // exs 2

        Sum sum = new(2, 2);
        sum.PrintResult();

        Subtraction subtraction = new(2, 2);
        subtraction.PrintResult();

        Multiplication multiplication = new(2, 2);
        multiplication.PrintResult();

        Division division = new(2, 2);
        division.PrintResult();

        Pow pow = new(2, 2);
        pow.PrintResult();

    }
}
