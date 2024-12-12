' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 47  CALENDARIO DE ADVIENTO
' ------------------------------------
'* EJERCICIO:
'* ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
'* developers. Del 1 al 24 de diciembre: https : //adviento.dev
'* 
'* Dibuja un calendario por terminal e implementa una
'* funcionalidad para seleccionar días y mostrar regalos.
'* - El calendario mostrará los días del 1 al 24 repartidos
'*   en 6 columnas a modo de cuadrícula.
'* - Cada cuadrícula correspondiente a un día tendrá un tamaño 
'*   de 4x3 caracteres, y sus bordes serán asteríscos.
'* - Las cuadrículas dejarán un espacio entre ellas.
'* - En el medio de cada cuadrícula aparecerá el día entre el
'*   01 y el 24.
'*
'* Ejemplo de cuadrículas:
'* **** **** ****
'* *01* *02* *03* ...
'* **** **** ****
'*
'* - El usuario seleccioná qué día quiere descubrir.
'* - Si está sin descubrir, se le dirá que ha abierto ese día
'*   y se mostrará de nuevo el calendario con esa cuadrícula
'*   cubierta de asteríscos (sin mostrar el día).
'*
'* Ejemplo de selección del día 1
'* **** **** ****
'* **** *02* *03* ...
'* **** **** ****
'*   
'* - Si se selecciona un número ya descubierto, se le notifica
'*   al usuario.

Module exs47
    Sub Main()
        Dim mtx(3, 5) As String
        For i As Integer = 0 To 3
            For j As Integer = 0 To 5
                mtx(i, j) = $"*{(i * 6 + j + 1):00}*"
            Next
        Next

        Dim ln As String = String.Join(" ", Enumerable.Repeat("****", 6))

        While True
            For i As Integer = 0 To 3
                Console.WriteLine(ln)
                Dim currentRow As Integer = i
                For j As Integer = 0 To 5
                    Console.Write(mtx(currentRow, j) & " ")
                Next
                Console.WriteLine(vbCrLf & ln & vbCrLf)
            Next

            Console.Write("Día a descubrir: ")
            Dim day As String = Console.ReadLine()

            If Not Integer.TryParse(day, Nothing) Then
                Console.WriteLine("Entrada inválida. Debe ser un número.")
                Continue While
            End If

            Dim dayInt As Integer = Convert.ToInt32(day)
            If dayInt < 1 Or dayInt > 24 Then
                Console.WriteLine("Día inválido, debe ser entre 1 y 24.")
                Continue While
            End If

            Dim r As Integer = (dayInt - 1) \ 6
            Dim c As Integer = (dayInt - 1) Mod 6

            If mtx(r, c) = "****" Then
                Console.WriteLine($"El día {day} ya está descubierto.")
                Continue While
            End If

            mtx(r, c) = "****"
        End While
    End Sub
End Module
