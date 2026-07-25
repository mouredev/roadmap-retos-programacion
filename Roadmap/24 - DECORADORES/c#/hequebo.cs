class Program
{
    static void Main(string[] args)
    {
        // Componente original
        Console.WriteLine("---Componente original---");
        IComponent component = new ConcreteComponent();
        component.Operation();
        // Decorator
        Console.WriteLine("---Decorator---");
        Decorator decorator = new ConcreteDecorator();
        decorator.SetComponent(component);
        decorator.Operation();

        // Ejercicio extra
        Console.WriteLine("---Ejercicio extra---");
        CountDecorator countDecorator = new ConcreteCountDecorator();
        countDecorator.SetComponent(component);
        countDecorator.Operation();
        countDecorator.Operation();
        countDecorator.Operation();
        countDecorator.Operation();
        countDecorator.Operation();

    }
}
/*
 * El patrón Decorator es un patrón de 
 * diseño que nos permite agregar 
 * comportamiento a un objeto sin afectar
 * el comportamiento de otros objetos de 
 * la misma clase.
 */

/*
 * Definimos la interface base que define
 * la funcionalidad del objeto
 */
interface IComponent
{
    public void Operation();
}
/* 
 * Se crea el componente concreto, una 
 * clase que implementa el metodo de
 * la interface
 */
class ConcreteComponent : IComponent
{
    public void Operation() => Console.WriteLine("Ejecutando operación...");
}
/* 
 * Se crea el decorador base, una clase
 * abstracta que implementa la interface
 * y permite agregar funcionalidad, no
 * es obligatorio crear el decorador base
 */
abstract class Decorator : IComponent
{
    protected IComponent _component;

    public void SetComponent(IComponent component) => _component = component;
    public virtual void Operation()
    {
        if (_component != null) 
            _component.Operation();
    }
}
/*
 * Se crea el decorador concreto, hereda de
 * la clase abstracta Decorator y agrega la 
 * funcionalidad extra al objeto
 */
class ConcreteDecorator : Decorator
{
    public override void Operation()
    {
        base.Operation();
        Console.WriteLine("Se expande funcionalidad con Decorator...");
    }
}
abstract class CountDecorator : IComponent
{
    protected IComponent _component;
    protected int count;
    public void SetComponent(IComponent component) 
    {
        _component = component;
        count = 0;
    }
    public virtual void Operation()
    {
        if (_component != null) 
            _component.Operation();
    }
}
class ConcreteCountDecorator : CountDecorator
{
    public override void Operation()
    {
        base.Operation();
        count++;
        Console.WriteLine($"Se ha llamado a la función {count} veces");
    }
}
    
