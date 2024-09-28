#pragma warning disable CA1050
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
* DECORADORES
------------------------------------------
Mas info: https://bytehide.com/blog/decorator-pattern-csharp

* EJERCICIO #1:
* Explora el concepto de "decorador" y muestra cómo crearlo
* con un ejemplo genérico.
*/

// Interfaz
public interface ISayHello {
    void SayHello(string first_name, string last_name);
}

// Componente Concreto
public class HelloSpeaker : ISayHello {
    public void SayHello(string first_name, string last_name) {
        Console.WriteLine($"Hola, {first_name} {last_name}!");
    }
}

// Decorador Base
public abstract class DecoratorBase : ISayHello {
    protected ISayHello _helloSpeaker;

    public DecoratorBase(ISayHello helloSpeaker) {
        _helloSpeaker = helloSpeaker;
    }

    public virtual void SayHello(string first_name, string last_name) {
        _helloSpeaker.SayHello(first_name, last_name);
    }
}

// Decorador Concreto
public class MyDecorator : DecoratorBase {
    public MyDecorator(ISayHello helloSpeaker) : base(helloSpeaker) { }

    public override void SayHello(string first_name, string last_name) {
        Console.WriteLine("\nAntes de llamar a la función.");
        base.SayHello(first_name, last_name);
        Console.WriteLine("Después de llamarla");
    }
}

/*
__________________________________
* EJERCICIO #2:
* Crea un decorador que sea capaz de contabilizar cuántas veces
* se ha llamado a una función y aplícalo a una función de tu elección.
*/
public interface IFunction{
    void Execute(params object[] args);
}

public class Function : IFunction{
    private readonly string _name;

    public Function(string name) {
        _name = name;
    }

    public void Execute(params object[] args) {
        Console.WriteLine($"\nLa función '{_name}':");
    }
}

public abstract class CallCountDecorator : IFunction {
    protected IFunction _function;
    protected int _calls;

    public CallCountDecorator(IFunction function) {
        _function = function;
        _calls = 0;
    }

    public void Execute(params object[] args) {
        _calls++;
        _function.Execute(args);
        Console.WriteLine($"Ha sido llamada {_calls} veces");
    }
}

public class CountCallsDecorator : CallCountDecorator {
    public CountCallsDecorator(IFunction function) : base(function) { }
}

// __________________________________
class Program {    
    static void Main() {
        Console.WriteLine("EJERCICIO #1");

        ISayHello helloSpeaker = new HelloSpeaker();
        ISayHello decoratedHelloSpeaker = new MyDecorator(helloSpeaker);
        decoratedHelloSpeaker.SayHello("Zoe", "Roy");

        // __________________________________
        Console.WriteLine("\nEJERCICIO #2");

        IFunction functionA = new CountCallsDecorator(new Function("A"));
        IFunction functionB = new CountCallsDecorator(new Function("B"));

        functionA.Execute();
        functionA.Execute();
        functionA.Execute();

        functionB.Execute();
        functionB.Execute();

    }
}
