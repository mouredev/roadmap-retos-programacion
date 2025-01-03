' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 35 REPARTIENDO LOS ANILLOS DE PODER
' ------------------------------------
' ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
' ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
' entre las razas de la Tierra Media?
' Desarrolla un programa que se encargue de distribuirlos.
' Requisitos:
' 1. Los Elfos recibirán un número impar.
' 2. Los Enanos un número primo.
' 3. Los Hombres un número par.
' 4. Sauron siempre uno.
' Acciones:
' 1. Crea un programa que reciba el número total de anillos
'   y busque una posible combinación para repartirlos.
' 2. Muestra el reparto final o el error al realizarlo.

Module Program
    Function GetTotalRings() As Integer
        Do
            Console.Write("Cantidad de anillos: ")
            Dim input = Console.ReadLine()
            Dim result As Integer
            If Integer.TryParse(input, result) AndAlso result >= 1 Then
                Return result
            End If
            Console.WriteLine("Debe ser un valor entero '>= 1'.")
        Loop
    End Function

    Function IsPrime(n As Integer) As Boolean
        If n < 2 Then Return False
        For i As Integer = 2 To Math.Sqrt(n)
            If n Mod i = 0 Then Return False
        Next
        Return True
    End Function

    Function Distribute(total As Integer) As List(Of (Integer, Integer, Integer))
        Dim combinations As New List(Of (Integer, Integer, Integer))
        Dim range As Integer
        Dim start As Integer
        Dim [end] As Integer

        If total > 1000 Then
            ' For large numbers.
            range = Math.Min(1000, total \ 3)
            start = (total - range) \ 2
            [end] = start + range
        Else
            ' For smaller numbers.
            start = 1
            [end] = total - 1
        End If

        For elves As Integer = start To [end] Step 2
            For men As Integer = start + 1 To [end] Step 2
                Dim dwarves As Integer = total - (men + elves)
                If dwarves > 0 AndAlso IsPrime(dwarves) Then
                    combinations.Add((elves, men, dwarves))
                End If
            Next
        Next

        Return combinations
    End Function

    Function StandardDeviation(tup As (Integer, Integer, Integer)) As Double
        Dim values() As Double = {tup.Item1, tup.Item2, tup.Item3}
        Dim avg As Double = values.Average()
        Dim sum As Double = values.Sum(Function(d) Math.Pow(d - avg, 2))
        Return Math.Sqrt(sum / (values.Length - 1))
    End Function

    Function TheMostBalanced(combinations As List(Of (Integer, Integer, Integer))) As (Integer, Integer, Integer)
        Return combinations.OrderBy(Function(c) StandardDeviation(c)).First()
    End Function

    Sub PrintResult(distribution As (Integer, Integer, Integer), sauron As Integer)
        If distribution.Equals(Nothing) Then
            Console.WriteLine("Error en la selección equitativa.")
            Return
        End If

        Console.WriteLine("_________________________")
        Console.WriteLine($"Elfos   -> {distribution.Item1} : # Impar")
        Console.WriteLine($"Enanos  -> {distribution.Item3} : # Primo")
        Console.WriteLine($"Hombres -> {distribution.Item2} : # Par")
        Console.WriteLine($"Sauron  -> {sauron} : # Fijo")
        Console.WriteLine("-------------------------")
    End Sub

    Sub Main()
        Console.WriteLine("REPARTIENDO LOS ANILLOS DE PODER")
        Dim total As Integer = GetTotalRings()
        Dim sauron As Integer = 1
        total -= sauron

        Dim combinations = Distribute(total)
        If combinations.Count = 0 Then
            Console.WriteLine("No existe una combinación posible.")
            Return
        End If

        Dim distribution = TheMostBalanced(combinations)
        PrintResult(distribution, sauron)
    End Sub
End Module
