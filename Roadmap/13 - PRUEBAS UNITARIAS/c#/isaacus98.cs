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

using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Roadmap
{
    public class Reto13
    {
        public Dictionary<string, string> Programmer = new Dictionary<string, string>()
        {
            {"name", "Isaac" },
            {"age", "26" },
            {"birth_date", "13-02-1998" },
            {"programming_languages", "C#, VB.Net, Kotlin"}
        };

        public int Suma(int num1, int num2)
        {
            return num1 + num2;
        }
    }

    [TestClass]
    public class Reto13Test
    {
        [TestMethod]
        public void SumaTest()
        {
            Reto13 reto = new();
            int result = reto.Suma(1, 2);
            Assert.AreEqual(3, result);
        }

        [TestMethod]
        public void DictionaryTest()
        {
            Reto13 reto = new();
            Assert.IsTrue(reto.Programmer.ContainsKey("name"));
            Assert.IsTrue(reto.Programmer.ContainsKey("age"));
            Assert.IsTrue(reto.Programmer.ContainsKey("birth_date"));
            Assert.IsTrue(reto.Programmer.ContainsKey("programming_languages"));
        }

        [TestMethod]
        public void DictionaryValuesTest()
        {
            Reto13 reto = new();
            Assert.AreEqual("Isaac", reto.Programmer["name"]);
            Assert.AreEqual("26", reto.Programmer["age"]);
            Assert.AreEqual("13-02-1998", reto.Programmer["birth_date"]);
            Assert.AreEqual("C#, VB.Net, Kotlin", reto.Programmer["programming_languages"]);
        }
    }
}
