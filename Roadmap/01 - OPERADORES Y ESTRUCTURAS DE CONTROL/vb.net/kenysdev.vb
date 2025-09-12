' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
Imports System

Module Program
    Sub Main(args As String())

        ' 1. Imprimir ejemplos utilizando todos los tipos 
        '    de operadores de tu lenguaje: 
        ' ***********************************************
        Console.WriteLine("
        Operadores aritmeticos:
        -----------------------
        - Suma:              10 + 5         = " & (10 + 5) & "
        - Resta:             10 - 5         = " & (10 - 5) & "
        - Multiplicacion:    10 * 5         = " & (10 * 5) & "
        - Division: 
          double, float o    5.0 / 2.0      = " & (5.0 / 2.0) & "
        - Division Entera: int o 17 \ 4     = " & (17 \ 4) & "
        - Residuo:           20 % 7         = " & (20 Mod 7) & "
        - Potenciacion:      Math.Pow(2, 3) = " & Math.Pow(2, 3) & "
        - Combined:         (4 + 2) * 3 / 2 = " & ((4 + 2) * 3 / 2) & "

        Operadores de Comparacion:
        --------------------------
        - igual a       5 == 5 -> " & (5 = 5) & "
        - Diferente de  5 != 5 -> " & (5 <> 5) & "
        - Menor que     4 < 5  -> " & (4 < 5) & "
        - Mayor que     4 > 5  -> " & (4 > 5) & "
        - Menor o igual 4 <= 5 -> " & (4 <= 5) & "
        - Mayor o igual 4 >= 5 -> " & (4 >= 5) & "
        ")
        ' -------------------------
        ' Operadores de Asignación:
        ' -------------------------
        Console.WriteLine(Environment.NewLine & "Operadores de Asignación:")
        Dim n As Double = 10
        n += 2
        n -= 2
        n *= 2
        n /= 2
        n = n Mod 2 'modulo
        Math.Pow(n, 2) 'pow
        Console.WriteLine(n) ' 0

        ' -------------------
        ' Operadores Lógicos:
        ' -------------------
        Console.WriteLine(Environment.NewLine & "Operadores Lógicos:")
        ' Operador AndAlso (and)
        Dim resultadoAnd As Boolean = (5 = 5 AndAlso 6 <> 5)
        Console.WriteLine("Operador AndAlso (and): " & resultadoAnd)

        ' Operador OrElse (or)
        Dim resultadoOr As Boolean = (5 = 5 OrElse 6 <> 5)
        Console.WriteLine("Operador OrElse (or): " & resultadoOr)

        ' Operador Not (not)
        Dim resultadoNot As Boolean = Not (5 = 6)
        Console.WriteLine("Operador Not (not): " & resultadoNot)

        ' ------------------------
        ' Operador de Pertenencia:
        ' ------------------------
        Console.WriteLine(Environment.NewLine & "Operador de Pertenencia:")
        Dim resultado As Boolean = "abcde".Contains("c")
        Console.WriteLine("Resultado de ""abcde"".Contains(""c""): " & resultado)

        ' ---------------------
        ' Operadores Bit a Bit:
        ' ---------------------
        Console.WriteLine(Environment.NewLine & "Operadores Bit a Bit:")
        ' Operador AND
        Dim resultado_And As String = Convert.ToString(10 And 5, 2)
        Console.WriteLine("and:       " & resultado_And)

        ' Operador OR
        Dim resultado_Or As String = Convert.ToString(10 Or 5, 2)
        Console.WriteLine("or:        " & resultado_Or)

        ' Operador XOR
        Dim resultadoXor As String = Convert.ToString(10 Xor 5, 2)
        Console.WriteLine("xor:       " & resultadoXor)

        ' Operador NOT
        Dim resultado_Not As String = Convert.ToString(Not 10, 2)
        Console.WriteLine("not_a:     " & resultado_Not)

        ' Desplazamiento a la izquierda
        Dim resultado_Izquierda As String = Convert.ToString(10 << 2, 2)
        Console.WriteLine("izquierda: " & resultado_Izquierda)

        ' Desplazamiento a la derecha
        Dim resultado_Derecha As String = Convert.ToString(10 >> 1, 2)
        Console.WriteLine("derecha:   " & resultado_Derecha)

        ' **************************
        ' 2. Estructuras de control:
        ' **************************
        ' __________________________
        ' Condicinal
        Console.WriteLine(Environment.NewLine & "Condicinal:")
        Dim x As Integer = 2
        If x = 5 Then
            Console.WriteLine("Si 5 == 5")
        ElseIf x = 2 Then
            Console.WriteLine("Si 2 == 2")
        Else
            Console.WriteLine("Ninguna")
        End If

        ' __________________________
        ' Operador ternario
        Console.WriteLine(Environment.NewLine & "Operador ternario:")
        Console.WriteLine(If(15 = 15, "si es igual", "no es igual"))

        ' __________________________
        ' Switch
        Console.WriteLine(Environment.NewLine & "switch:")
        Dim num As Integer = 2
        Select Case num
            Case 1
                Console.WriteLine("Es 1")
            Case 2
                Console.WriteLine("Es 2")
            Case Else
                Console.WriteLine("null")
        End Select

        ' __________________________
        ' Bucle for
        Console.WriteLine("Bucle for:")
        For i As Integer = 0 To 2
            Console.WriteLine($"Iteración {i + 1}")
        Next

        ' __________________________
        ' Bucle while
        Console.WriteLine(Environment.NewLine & "Bucle while:")
        Dim j As Integer = 0
        While j < 3
            Console.WriteLine($"Iteración {j + 1}")
            j += 1
        End While

        ' __________________________
        ' Bucle do - Loop While
        Console.WriteLine(Environment.NewLine & "Bucle do-while:")
        Dim k As Integer = 0
        Do
            Console.WriteLine($"Iteración {k + 1}")
            k += 1
        Loop While k < 3

        ' __________________________
        ' Bucle For Each
        Console.WriteLine(Environment.NewLine & "Bucle foreach (para iterar sobre colecciones):")
        Dim z() As Integer = {1, 2, 3}
        For Each num2 In z
            Console.WriteLine($"Número: {num2}")
        Next

        ' __________________________
        ' Exit For & Continue
        Console.WriteLine(Environment.NewLine & "break & continue:")
        For i As Integer = 1 To 3
            If i = 4 Then
                Console.WriteLine($"Valor 4 encontrado. Break.")
                Exit For
            End If
            If i Mod 2 = 0 Then
                Console.WriteLine($"Iteración {i} es par. Continue.")
                Continue For
            End If
            Console.WriteLine($"Iteración {i}")
        Next
        Console.WriteLine($"Finalizando")

        ' __________________________
        ' Control de Excepciones
        Console.WriteLine(Environment.NewLine & "Control de Excepciones:")
        Try
            Dim nu As Integer = 10
            Console.WriteLine($"Resultado: {nu / 0}")
        Catch e As DivideByZeroException
            Console.WriteLine($"Error división: {e.Message}")
        Finally
            Console.WriteLine("finally")
        End Try

        ' 3. Ejercicio:
        ' *************
        ' Crea un programa que imprima por consola todos los números comprendidos entre
        ' 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
        Console.WriteLine(Environment.NewLine & "Ejercicio:")

        For numero As Integer = 10 To 55
            If numero Mod 2 = 0 AndAlso numero <> 16 AndAlso numero Mod 3 <> 0 Then
                Console.WriteLine(numero)
            End If
        Next

    End Sub
End Module
