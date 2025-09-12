' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝

' # VALOR Y REFERENCIA
' --------------------
Module Program
    Sub Main(args As String())
        ' Asignación de variables "por valor"
        ' - se asigna el valor real de la variable a otra variable.
        ' - los cambios en una variable no afectarán a la otra.

        Console.WriteLine("Por valor")
        Dim int1 As Integer = 111
        Dim bool1 As Boolean = False
        Dim str1 As String = "Ben"

        ' Asignación
        Dim int2 As Integer = int1
        Dim bool2 As Boolean = bool1
        Dim str2 As String = str1

        ' Cambio
        int1 = 777
        bool1 = True
        str1 = "zoe"

        ' Las variables no fueron afectadas.
        Console.WriteLine($"{int2} - {bool2} - {str2}")

        ' Ejemplo con una función:
        Sub_value(int1, bool1, str1)

        ' No afectadas por los cambios en la función.
        Console.WriteLine($"{int2} - {bool2} - {str2}")

        '___________________________________________________________________
        ' Asignación de variables "por referencia"
        ' - se asigna la referencia o dirección de memoria
        ' - de la variable a otra variable.
        ' - Los cambios en una variable pueden afectar a la otra.

        Console.WriteLine("Por referencia")
        Dim list1 As New List(Of String) From {"Bob", "Zoe", "Dan"}
        Dim dic1 As New Dictionary(Of String, String) From {{"name", "Dan"}}

        ' Asignación
        Dim list2 As List(Of String) = list1
        Dim dic2 As Dictionary(Of String, String) = dic1

        ' Cambio
        list1(0) = "Tom"
        dic1("name") = "Zoe"

        ' Las variables fueron afectadas por el cambio.
        Dim rList As String = String.Join(", ", list2)
        Console.WriteLine($"{rList}) - {dic2("name")}")

        ' Ejemplo en una función
        Sub_reference(list2, dic2)

        ' Fueron afectadas por los cambios en la función.
        Dim rList2 As String = String.Join(", ", list2)
        Console.WriteLine($"{rList2}) - {dic2("name")}")

        '___________________________________________________________________
        ' Ejercicio:
        ' Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
        ' - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
        '   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
        '   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
        '   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
        '   Comprueba también que se ha conservado el valor original en las primeras.
        Console.WriteLine("Ejercicio:")
        Dim s1 As String = "Ben"
        Dim s2 As String = "Zoe"
        Dim l1 As New List(Of Object) From {12, 21}
        Dim l2 As New List(Of Object) From {"Ben", "Zoe"}

        Dim rL1 As String = String.Join(", ", l1)
        Dim rL2 As String = String.Join(", ", l2)
        Console.WriteLine($"Pre-Intercambio:{vbCrLf}{s1} - {s2}{vbCrLf}{rL1} - {rL2}")

        Dim new_str = ByValue(s1, s2)
        Dim new_list = ByReference(l1, l2)

        rL1 = String.Join(", ", l1)
        rL2 = String.Join(", ", l2)
        Console.WriteLine($"Originales:{vbCrLf}{s1} - {s2}{vbCrLf}{rL1} - {rL2}")

        rL1 = String.Join(", ", new_list.Item1)
        rL2 = String.Join(", ", new_list.Item2)
        Console.WriteLine($"Nuevas:{vbCrLf}{new_str.Item1} - {new_str.Item2}{vbCrLf}{rL1} - {rL2}")
    End Sub

    Sub Sub_value(ByVal int3 As Integer, ByVal bool3 As Boolean, ByVal str3 As String)
        int3 = 333
        bool3 = False
        str3 = "Zoe"
    End Sub

    Sub Sub_reference(ByRef list As List(Of String), ByRef dic As Dictionary(Of String, String))
        list(0) = "Bob"
        dic("name") = "Dan"
    End Sub

    Function ByValue(str1 As String, str2 As String) As (String, String)
        Dim temp As String = str1
        str1 = str2
        str2 = temp
        Return (str1, str2)
    End Function

    Function ByReference(list1 As List(Of Object), list2 As List(Of Object)) As (List(Of Object), List(Of Object))
        Dim temp As List(Of Object) = list1
        list1 = list2
        list2 = temp
        Return (list1, list2)
    End Function
End Module
