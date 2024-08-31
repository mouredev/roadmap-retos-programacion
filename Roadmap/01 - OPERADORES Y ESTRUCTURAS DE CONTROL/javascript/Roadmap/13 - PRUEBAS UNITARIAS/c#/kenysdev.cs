/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  C#                            ║
╚═══════════════════════════════════════╝
-----------------------------------------------
* PRUEBAS UNITARIAS
-----------------------------------------------
# - Verifican que las unidades individuales de código (como 
#   funciones, métodos o clases) funcionen como se espera.
# - Mas info: https://www.netmentor.es/entrada/unit-testing
*/
#pragma warning disable CA1050
using Microsoft.VisualStudio.TestTools.UnitTesting;

/* ____________________________________
 * EJERCICIO #1
 * Crea una función que se encargue de sumar dos números y retornar
   su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
   capaz de determinar si esa función se ejecuta correctamente.
*/
public class FunSum {
    public static double Sum(double a, double b) {
        return a + b;
    } 
}

[TestClass]
public class TestSum {
    [TestMethod]
    public void TestSumCorrect() {
        Assert.AreEqual(FunSum.Sum(5, 2), 7);
        Assert.AreEqual(FunSum.Sum(2.50, 1.25), 3.75);
        Assert.AreEqual(FunSum.Sum(-2, 1), -1);
    }

    [TestMethod]
    public void TestSumIncorrect() {
        Assert.AreNotEqual(FunSum.Sum(1, 3), 5);
    }
}

/* ____________________________________
 * EJERCICIO #2
 * Crea un diccionario con las siguientes claves y valores:
   - "name": "Tu nombre"
   - "age": "Tu edad"
   - "birth_date": "Tu fecha de nacimiento"
   - "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
   - Un primero que determine que existen todos los campos.
   - Un segundo que determine que los datos introducidos son correctos.
*/

[TestClass]
public class TestDict {
    readonly Dictionary<string, object> dictUser = new() {
        { "name", "Ken" },
        { "age", 121 },
        { "birth_date", "1903-03-19" },
        { "prog_langs", new List<string> { "cs", "py", "vb", "rs", "js" } }
    };

    [TestMethod]
    public void TestDicKeyExistence() {
        Assert.IsTrue(dictUser.ContainsKey("name"));
        Assert.IsTrue(dictUser.ContainsKey("age"));
        Assert.IsTrue(dictUser.ContainsKey("birth_date"));
        Assert.IsTrue(dictUser.ContainsKey("prog_langs"));
    }

    [TestMethod]
    public void TestDicValueTypes() {
        Assert.IsInstanceOfType(dictUser["name"], typeof(string));
        Assert.IsInstanceOfType(dictUser["age"], typeof(int));
        Assert.IsInstanceOfType(dictUser["birth_date"], typeof(string));
        Assert.IsInstanceOfType(dictUser["prog_langs"], typeof(List<string>));
    }

    [TestMethod]
    public void TestDicValueContent() {
        Assert.AreEqual(dictUser["name"], "Ken");
        Assert.AreEqual(dictUser["age"], 121);
        Assert.AreEqual(dictUser["birth_date"], "1903-03-19");
        CollectionAssert.AreEqual(
            (List<string>)dictUser["prog_langs"],
            new List<string> { "cs", "py", "vb", "rs", "js" }
        );
    }
}
