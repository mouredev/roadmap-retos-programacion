' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* CONJUNTOS
'-----------------------------------------------

Module Program

    Sub Main()
        ' CONJUNTOS: Son una colección desordenada de elementos únicos.
        Dim mySet As New HashSet(Of Integer) From {1, 2, 3, 0}

        ' EJERCICIO #1:
        ' Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
        ' operaciones (debes utilizar una estructura que las soporte):

        ' NOTA: - Algunas operaciones del ejercicio no pueden realizarse utilizando 'HashSet'.

        Dim myList As New List(Of String) From {"a", "b", "c"}

        ' Añade un elemento al final.
        myList.Add("d")

        ' Añadir un elemento al principio
        myList.Insert(0, "-")

        ' Añadir varios elementos en bloque al final
        myList.AddRange({"e", "f"})

        ' Añadir varios elementos en bloque en una posición concreta
        myList.InsertRange(4, {"-", ">"})

        ' Eliminar un elemento en una posición concreta
        myList.RemoveAt(5)

        ' Actualizar el valor de un elemento en una posición concreta
        myList(2) = "-b"

        ' Mostrar la lista
        Console.WriteLine("Elementos de la lista:")
        Console.WriteLine(String.Join(", ", myList) + vbCrLf)

        ' Comprueba si un elemento está en un conjunto
        Console.WriteLine($"'4' en conjunto: {mySet.Contains(4)}" + vbCrLf)
        Console.WriteLine($"'c' en lista: {myList.Contains("c")}" + vbCrLf)

        ' Elimina todo el contenido del conjunto y la lista.
        mySet.Clear()
        myList.Clear()

        ' EJERCICIO #2:
        ' Muestra ejemplos de las siguientes operaciones con conjuntos:
        ' - Unión.
        ' - Intersección.
        ' - Diferencia.
        ' - Diferencia simétrica.

        Dim set1 As New HashSet(Of Integer) From {1, 2, 3, 4}
        Dim set2 As New HashSet(Of Integer) From {3, 4, 5, 6}

        Console.WriteLine(
            $"* set_1: {{{String.Join(", ", set1)}}} - set_2: {{{String.Join(", ", set2)}}}" + vbCrLf)

        ' Unión
        ' Elementos que están en al menos uno de los conjuntos.
        Dim union As New HashSet(Of Integer)(set1)
        union.UnionWith(set2)
        Console.WriteLine($"- Unión: {{{String.Join(", ", union)}}}" + vbCrLf)

        ' Intersección
        ' Elementos que están en ambos conjuntos.
        Dim intersection As New HashSet(Of Integer)(set1)
        intersection.IntersectWith(set2)
        Console.WriteLine($"- Intersección: {{{String.Join(", ", intersection)}}}" + vbCrLf)

        ' Diferencia
        ' Elementos que están en set_1 pero no en set_2
        Dim difference As New HashSet(Of Integer)(set1)
        difference.ExceptWith(set2)
        Console.WriteLine($"- Diferencia: {{{String.Join(", ", difference)}}}" + vbCrLf)

        ' Diferencia simétrica
        ' Elementos que están en uno de los conjuntos pero no en ambos.
        Dim symmetricDiff As New HashSet(Of Integer)(set1)
        symmetricDiff.SymmetricExceptWith(set2)
        Console.WriteLine($"- Diferencia simétrica: {{{String.Join(", ", symmetricDiff)}}}")
    End Sub
End Module
