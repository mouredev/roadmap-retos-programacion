' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 49 EL ALMACÉN DE PAPÁ NOEL
' ------------------------------------
'* EJERCICIO
' * Papá Noel tiene que comenzar a repartir los regalos...
' * ¡Pero ha olvidado el código secreto de apertura del almacén!
' *
' * Crea un programa donde introducir códigos y obtener pistas.
' * 
' * Código:
' * - El código es una combinación de letras y números aleatorios
' *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
' * - No hay repetidos.
' * - Se genera de manera aleatoria al iniciar el programa.
' * 
' * Usuario:
' * - Dispone de 10 intentos para acertarlo.
' * - En cada turno deberá escribir un código de 4 caracteres, y 
' *   el programa le indicará para cada uno lo siguiente:
' *   - Correcto: Si el caracter está en la posición correcta.
' *   - Presente: Si el caracter existe, pero esa no es su posición.
' *   - Incorrecto: Si el caracter no existe en el código secreto.
' * - Deben controlarse errores de longitud y caracteres soportados.
' * 
' * Finalización:
' * - Papa Noel gana si descrifra el código antes de 10 intentos.
' * - Pierde si no lo logra, ya que no podría entregar los regalos.

Module Program
    Function VerifyAllowedChar(codeEntry As String) As Boolean
        For Each ch As Char In codeEntry
            If Not "abc123".Contains(ch) Then
                Console.WriteLine("Uno de los caracteres no está entre los permitidos." & vbCrLf)
                Return False
            End If
        Next
        Return True
    End Function

    Function GetEntry() As String
        Do
            Console.Write("Código: ")
            Dim codeEntry As String = Console.ReadLine()

            If String.IsNullOrEmpty(codeEntry) OrElse codeEntry.Length <> 4 Then
                Console.WriteLine("El código debe ser de 4 dígitos." & vbCrLf)
                Continue Do
            End If

            If VerifyAllowedChar(codeEntry) Then
                Return codeEntry
            End If
        Loop
    End Function

    Function IsOpen(code As String) As Boolean
        Dim codeEntry As String = GetEntry()

        If codeEntry = code Then
            Return True
        End If

        Console.WriteLine("Código inválido." & vbCrLf)

        For i As Integer = 0 To codeEntry.Length - 1
            Dim ch As Char = codeEntry(i)

            If ch = code(i) Then
                Console.WriteLine($"'{ch}' está en la posición correcta.")
            ElseIf code.Contains(ch) Then
                Console.WriteLine($"'{ch}' está en el código, pero en otra posición.")
            Else
                Console.WriteLine($"'{ch}' no está presente en el código.")
            End If
        Next

        Return False
    End Function

    Sub Main()
        Console.WriteLine("*" & vbCrLf &
                  "* Papá Noel tiene que comenzar a repartir los regalos..." & vbCrLf &
                  "* ¡Pero ha olvidado el código secreto de apertura del almacén!" & vbCrLf & vbCrLf &
                  "- Tienes 10 intentos para adivinar el código que abre el almacén." & vbCrLf &
                  "- Código de 4 caracteres. Permitidos: a, b, c, 1, 2, 3." & vbCrLf &
                  "- Nota: No hay dígitos repetidos.")

        Dim characters As String = "abc123"
        Dim random As New Random()
        Dim code As New String(characters.OrderBy(Function(x) random.Next()).Take(4).ToArray())

        For attempts As Integer = 1 To 10
            Console.WriteLine(vbCrLf & "___________" & vbCrLf & $"Intento #{attempts}")

            If IsOpen(code) Then
                Console.WriteLine("Código correcto, almacén abierto.")
                Console.WriteLine("Papá Noel ahora podrá entregar los regalos.")
                Exit For
            End If

            If attempts = 10 Then
                Console.WriteLine(vbCrLf & "___________" & vbCrLf & "Has perdido.")
                Console.WriteLine("Papá Noel ya no podrá entregar los regalos.")
            End If
        Next
    End Sub
End Module
