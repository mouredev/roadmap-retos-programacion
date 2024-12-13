using Microsoft.VisualStudio.TestTools.UnitTesting;

class Program
{
    static void Main(string[] args)
    {
        // Pruebas unitarias Suma
        Console.WriteLine("---Pruebas Unitarias Sumas---");
        var opTest = new OperacionesTest();
        try
        {
            opTest.PruebaSumas();
            Console.WriteLine("Las pruebas se completaron correctamente");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Las pruebas fallaron...");
            Console.WriteLine(ex.Message);
        }
        finally
        {
            Console.WriteLine("Aquí terminan las pruebas unitarios de Sumas");
        }
        Console.ReadLine();
        Console.Clear();
        // Ejercicio Extra
        Console.WriteLine("---Pruebas unitarias Diccionario");
        var personaTest = new PersonaTest();
        try
        {
            personaTest.PruebaExistenValores();
            personaTest.PruebaValoresCorrectos();
            Console.WriteLine("Las pruebas se completaron correctamente");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Las pruebas fallaron...");
            Console.WriteLine(ex.Message);
        }
        finally
        {
            Console.WriteLine("Aquí terminan las pruebas unitarios de Diccionarios");
        }
    }
}
class Operaciones
{
    public int Suma(int a, int b)
    {
        return a + b;
    }
}

[TestClass]
class OperacionesTest
{
    
    [TestMethod]
    public void PruebaSumas()
    {
        var operaciones = new Operaciones();
        Assert.AreEqual(7, operaciones.Suma(5, 2));
        Assert.AreEqual(0, operaciones.Suma(5, -5));
        Assert.AreEqual(-7, operaciones.Suma(-5, -2));
        Assert.AreEqual(-3, operaciones.Suma(-5, 2));
    }
}
class Persona
{
    public Dictionary<string, object> persona = new Dictionary<string, object>
    {
        {"name", "Emilio Quezada" },
        {"age", "27"},
        {"birth_date", new DateTime(1997, 07, 28)},
        {"programming_languages", new List<string>{"C#", "Typescript", "VB"} }
    };
}
[TestClass]
class PersonaTest
{
    [TestMethod]
    public void PruebaExistenValores()
    {
        var personaPrueba = new Persona();
        Assert.IsTrue(personaPrueba.persona.ContainsKey("name"));
        Assert.IsTrue(personaPrueba.persona.ContainsKey("age"));
        Assert.IsTrue(personaPrueba.persona.ContainsKey("birth_date"));
        Assert.IsTrue(personaPrueba.persona.ContainsKey("programming_languages"));
    }
    [TestMethod]
    public void PruebaValoresCorrectos()
    {
        var personaPrueba = new Persona();
        Assert.IsInstanceOfType(personaPrueba.persona["name"], typeof(String));
        Assert.IsInstanceOfType(personaPrueba.persona["age"], typeof(Int32));
        Assert.IsInstanceOfType(personaPrueba.persona["birth_date"], typeof(DateTime));
        Assert.IsInstanceOfType(personaPrueba.persona["programming_languages"], typeof(List<string>));
    }
}
