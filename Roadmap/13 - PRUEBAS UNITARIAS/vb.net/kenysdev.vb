' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* PRUEBAS UNITARIAS
'-----------------------------------------------
' - Verifican que las unidades individuales de código (como 
'   funciones, métodos o clases) funcionen como se espera.
' - Mas info: https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-visual-basic-with-mstest

Imports Microsoft.VisualStudio.TestTools.UnitTesting

' _________________________________________________________________________
'* EJERCICIO #1
'* Crea una función que se encargue de sumar dos números y retornar
'  su resultado.
'* Crea un test, utilizando las herramientas de tu lenguaje, que sea
'  capaz de determinar si esa función se ejecuta correctamente.

Public Class FunSum
    Public Shared Function Sum(a As Double, b As Double) As Double
        Return a + b
    End Function
End Class

<TestClass>
Public Class TestSum
    <TestMethod>
    Public Sub TestSumCorrect()
        Assert.AreEqual(FunSum.Sum(5, 2), 7)
        Assert.AreEqual(FunSum.Sum(2.5, 1.25), 3.75)
        Assert.AreEqual(FunSum.Sum(-2, 1), -1)
    End Sub

    <TestMethod>
    Public Sub TestSumIncorrect()
        Assert.AreNotEqual(FunSum.Sum(1, 3), 5)
    End Sub
End Class

' _________________________________________________________________________
'* EJERCICIO #2
'* Crea un diccionario con las siguientes claves y valores:
'  - "name" "Tu nombre"
'  - "age": "Tu edad"
'  - "birth_date": "Tu fecha de nacimiento"
'  - "programming_languages": ["Listado de lenguajes de programación"]
'* Crea dos test:
'  - Un primero que determine que existen todos los campos.
'  - Un segundo que determine que los datos introducidos son correctos.

<TestClass>
Public Class TestDict
    ReadOnly dictUser As New Dictionary(Of String, Object) From {
        {"name", "Ken"},
        {"age", 121},
        {"birth_date", "1903-03-19"},
        {"prog_langs", New List(Of String) From {"cs", "py", "vb", "rs", "js"}}
    }

    <TestMethod>
    Public Sub TestDicKeyExistence()
        Assert.IsTrue(dictUser.ContainsKey("name"))
        Assert.IsTrue(dictUser.ContainsKey("age"))
        Assert.IsTrue(dictUser.ContainsKey("birth_date"))
        Assert.IsTrue(dictUser.ContainsKey("prog_langs"))
    End Sub

    <TestMethod>
    Public Sub TestDicValueTypes()
        Assert.IsInstanceOfType(dictUser("name"), GetType(String))
        Assert.IsInstanceOfType(dictUser("age"), GetType(Integer))
        Assert.IsInstanceOfType(dictUser("birth_date"), GetType(String))
        Assert.IsInstanceOfType(dictUser("prog_langs"), GetType(List(Of String)))
    End Sub

    <TestMethod>
    Public Sub TestDicValueContent()
        Assert.AreEqual(dictUser("name"), "Ken")
        Assert.AreEqual(dictUser("age"), 121)
        Assert.AreEqual(dictUser("birth_date"), "1903-03-19")
        CollectionAssert.AreEqual(
            DirectCast(dictUser("prog_langs"), List(Of String)),
            New List(Of String) From {"cs", "py", "vb", "rs", "js"}
        )
    End Sub
End Class
