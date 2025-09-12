/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */

using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

class Testing
{
    public int Suma(int num1, int num2)
    {
        return num1 + num2;
    }

    public Dictionary<string, string> Programmer = new Dictionary<string, string>()
    {
        {"name", "Jamer" },
        {"age", "24" },
        {"birth_date", "21-02-2000" },
        {"programming_languages", ["C#", "TypeScript", "Bash", "Python"] }
    };

    [TestClass]
    public class TestingTest
    {
        [TestMethod]
        public void SumaTest()
        {
            Testing test = new();
            int result = test.Suma(1, 2);
            Assert.AreEqual(3, result);
        }

        [TestMethod]
        public void DictionaryTest()
        {
            Testing test = new();
            Assert.IsTrue(test.Programmer.ContainsKey("name"));
            Assert.IsTrue(test.Programmer.ContainsKey("age"));
            Assert.IsTrue(test.Programmer.ContainsKey("birth_date"));
            Assert.IsTrue(test.Programmer.ContainsKey("programming_languages"));
        }
    }

    static void Main()
    {
        Testing test = new();
        int result = test.Suma(1, 2);
        Console.WriteLine(result);

        Console.WriteLine(test.Programmer["name"]);
        Console.WriteLine(test.Programmer["age"]);
        Console.WriteLine(test.Programmer["birth_date"]);
        foreach (string language in test.Programmer["programming_languages"])
        {
            Console.WriteLine(language);
        }
    }
}
