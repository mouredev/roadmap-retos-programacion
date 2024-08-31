namespace exs28;
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
-------------------------------------------------
* SOLID: PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)
-------------------------------------------------
*/

// clase base
public abstract class Animal(string name)
{
    protected string name = name;

    public abstract string MakeSound();
}

// Clases derivadas
public class Dog(string name) : Animal(name)
{
    public override string MakeSound()
    {
        return $"{name} hace Woof";
    }
}

public class Cat(string name) : Animal(name)
{
    public override string MakeSound()
    {
        return $"{name} hace Meow";
    }
}

/*
_______________
* EJERCICIO:
* Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
* cumplir el LSP.
* Instrucciones:
* 1. Crea la clase Vehículo.
* 2. Añade tres subclases de Vehículo.
* 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
* 4. Desarrolla un código que compruebe que se cumple el LSP.
*/

// Clase base abstracta
public abstract class Vehicle(string brand, string model)
{
    // Propiedades
    public string Brand { get; } = brand;
    public string Model { get; } = model;

    // Métodos abstractos
    public abstract string Accelerate();
    public abstract string Brake();
}

// Clases derivadas
public class Car(string brand, string model) : Vehicle(brand, model)
{
    public override string Accelerate()
    {
        string properties = $"{Brand} - {Model}";
        return $"Acelerando auto: {properties}";
    }

    public override string Brake()
    {
        string properties = $"{Brand} - {Model}";
        return $"Frenando auto: {properties}";
    }
}

public class Motorcycle(string brand, string model) : Vehicle(brand, model)
{
    public override string Accelerate()
    {
        string properties = $"{Brand} - {Model}";
        return $"Acelerando Motocicleta: {properties}";
    }

    public override string Brake()
    {
        string properties = $"{Brand} - {Model}";
        return $"Frenando Motocicleta: {properties}";
    }
}

public class Truck(string brand, string model) : Vehicle(brand, model)
{
    public override string Accelerate()
    {
        string properties = $"{Brand} - {Model}";
        return $"Acelerando Camión: {properties}";
    }

    public override string Brake()
    {
        string properties = $"{Brand} - {Model}";
        return $"Frenando Camión: {properties}";
    }
}

//__________________
public class Program
{
    static void Main()
    {
        Dog perro = new("Max");
        Cat gato = new("Milo");
        Animal Ncat = new Cat("Dex");

        Console.WriteLine(perro.MakeSound());
        Console.WriteLine(gato.MakeSound());
        Console.WriteLine(Ncat.MakeSound());
        
        //___________________________
        // exs 2
        
        Car car = new("Honda", "Civic");
        TestSubClass(car);

        Vehicle motorcycle = new Motorcycle("Kawasaki", "Ninja");
        TestSubClass(motorcycle);

        Vehicle truck = new Truck("Ford", "Raptor");
        TestSubClass(truck);

    }

    static void TestSubClass(Vehicle subClass)
    {
        Console.WriteLine("\nPropiedades:");
        Console.WriteLine($"{subClass.Brand} - {subClass.Model}");

        Console.WriteLine("\nMétodos:");
        Console.WriteLine(subClass.Accelerate());
        Console.WriteLine(subClass.Brake());
    }
}
