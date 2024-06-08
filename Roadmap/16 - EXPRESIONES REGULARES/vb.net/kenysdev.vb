' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* EXPRESIONES REGULARES
'-----------------------------------------------
Imports System.Text.RegularExpressions

Module Program
    '* EJERCICIO #1:
    '* Utilizando tu lenguaje, explora el concepto de expresiones regulares,
    '* creando una que sea capaz de encontrar y extraer todos los números
    '* de un texto.

    Sub GetNumbers(text As String)
        Dim pattern = "\d+"
        Dim numbers = Regex.Matches(text, pattern)

        For Each n As Match In numbers
            Console.WriteLine(n)
        Next
    End Sub

    '* EJERCICIO #2
    '* Crea 3 expresiones regulares (a tu criterio) capaces de
    '* - Validar un email.
    '* - Validar un número de teléfono.
    '* - Validar una url.

    Function IsEmail(text As String) As Boolean
        Dim pattern = "^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$"
        Return Regex.IsMatch(text, pattern)
    End Function

    Function IsPhoneNumber(text As String) As Boolean
        Dim pattern = "^(\d{3}-\d{3}-\d{4}|\d{10})$"
        Return Regex.IsMatch(text, pattern)
    End Function

    Function IsURL(text As String) As Boolean
        Dim pattern = "^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/\S*)?$"
        Return Regex.IsMatch(text, pattern)
    End Function

    Sub Print(text As Object)
        Console.WriteLine(text)
    End Sub

    Sub Main()
        Print("GetNumbers")
        GetNumbers("abcdsfs1s(*&#}2. a3// 45sdf67")
        GetNumbers("45sdf67")

        Print(vbCrLf + "IsEmail")
        Print(IsEmail("ejm@dmn.com"))         ' True
        Print(IsEmail("e_jm-2+b@dmn.co.hn"))  ' True
        Print(IsEmail("ejm@dmn.com_"))        ' False
        Print(IsEmail("ejm@dmn"))             ' False

        Print(vbCrLf + "IsPhoneNumber")
        Print(IsPhoneNumber("123-456-7890"))  ' True
        Print(IsPhoneNumber("1234567890"))    ' True
        Print(IsPhoneNumber("123456-7890"))   ' False
        Print(IsPhoneNumber("uno234567890"))  ' False

        Print(vbCrLf + "IsURL")
        Print(IsURL("http://www.ejm.com"))    ' True
        Print(IsURL("google.com"))            ' True
        Print(IsURL("ejm.com/a/b/c"))         ' True
        Print(IsURL("https://.ejm.com"))      ' False
        Print(IsURL("https://.ejm.com/a b"))  ' False 
    End Sub
End Module
