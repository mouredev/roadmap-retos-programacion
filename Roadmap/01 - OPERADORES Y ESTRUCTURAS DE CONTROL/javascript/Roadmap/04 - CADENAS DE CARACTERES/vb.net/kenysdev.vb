' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝

' Cadenas de Caracteres
' ---------------------
Imports System.Text

Module Program

    Sub Main(args As String())
        ' ________________________________________
        ' Declaración e inicialización
        Dim msg As String
        Dim msg1 As String = ""
        ' Tabulación horizontal.
        Dim columns As String = "Column 1" & vbTab & "Column 2"
        ' Salto de línea.
        Dim rows As String = "Row 1" & vbCrLf & "Row 2"
        Console.WriteLine(columns)
        Console.WriteLine(rows)

        ' ________________________________________
        ' Longitud
        Dim str1 As String = "abcd"
        Dim length As Integer = str1.Length
        Console.WriteLine("longitud: " & length)

        ' ________________________________________
        ' Método Trim 
        Dim str2 As String = "   str   "
        ' Eliminar los caracteres en blanco al inicio y al final.
        Dim trim_str As String = str2.Trim()
        Console.WriteLine(trim_str)
        ' Eliminar al inicio.
        Dim trim_start As String = str2.TrimStart()
        Console.WriteLine(trim_start)
        ' Eliminar al final.
        Dim trim_end As String = str2.TrimEnd()
        Console.WriteLine(trim_end)

        ' ________________________________________
        ' Extraer una parte de la cadena.
        Dim str3 As String = "Hello, world!"
        Dim newStr3 As String = str3.Substring(7, 5)
        Console.WriteLine(newStr3) ' World

        ' Eliminar una parte de la cadena.
        Dim sb As New Text.StringBuilder(str3)
        sb.Remove(7, 5)
        Console.WriteLine(sb.ToString()) ' Hello, !

        ' ________________________________________
        ' Reemplazar un carácter por otro
        Dim str4 As String = "abc def"
        Dim newStr4 As String = str4.Replace("c", "C")
        Console.WriteLine(newStr4) ' abC def
        newStr4 = str4.Replace("def", "DEF")
        Console.WriteLine(newStr4) ' abc DEF

        ' ________________________________________
        ' Mayúsculas
        Dim str5 As String = "abc"
        Dim newStr5 As String = str5.ToUpper()
        Console.WriteLine(newStr5) ' ABC

        ' ________________________________________
        ' Minúsculas
        Dim str6 As String = "ABC"
        Dim newStr6 As String = str6.ToLower()
        Console.WriteLine(newStr6) ' abc

        ' ________________________________________
        ' Concatenación
        Dim str_a As String = "a"
        Dim str_b As String = "b"
        Dim int_r As Integer = 7
        Dim combined_str As String
        combined_str = str_a & "-" & str_b & "=" & int_r.ToString()
        Console.WriteLine(combined_str) ' a-b=7

        ' ________________________________________
        ' Interpolación
        Dim name As String = "Ben"
        Dim age As Integer = 21
        Console.WriteLine($"Soy {name} y tengo {age} años.")

        ' ________________________________________
        ' Acceso
        Dim str7 As String = "abcd"
        Dim endChar As Char = str7(3)
        Console.WriteLine(endChar) ' d

        ' verificación
        Console.WriteLine(str7.Contains("bc")) ' True

        ' ________________________________________
        ' Iterar
        For Each c As Char In str7
            Console.WriteLine(c)
        Next

        ' ________________________________________
        ' Ejercicio:
        ' Crea un programa que analice dos palabras diferentes y realice comprobaciones
        ' para descubrir si son:
        ' - Palíndromos (Igual ambas direcciones)
        ' - Anagramas   (Reordenamiento de las letras de otra palabra)
        ' - Isogramas   (No hay letras repetidas)

        exs("reconocer", "vida")
        exs("notas", "santo")
        exs("héroe", "radar")
    End Sub

    Sub exs(str1 As String, str2 As String)
        Dim isAnagram As Boolean
        isAnagram = str1.OrderBy(Function(c) c).SequenceEqual(str2.OrderBy(Function(c) c))

        Console.WriteLine($"
    ________________________________________
    ""{str1}"" es un palíndromo?: {str1 = New String(str1.Reverse().ToArray())}
    ""{str2}"" es un palíndromo?: {str2 = New String(str2.Reverse().ToArray())}

    ""{str1}"" es un anagrama de ""{str2}""?: {isAnagram}

    ""{str1}"" es un isograma?: {str1.Length = str1.Distinct().Count()}
    ""{str2}"" es un isograma?: {str2.Length = str2.Distinct().Count()}
    ")
    End Sub
End Module
