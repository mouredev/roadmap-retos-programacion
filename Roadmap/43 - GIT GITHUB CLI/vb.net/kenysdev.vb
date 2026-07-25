' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 43 GIT GITHUB CLI
' ------------------------------------
'* EJERCICIO
' * ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
' *
' * Desarrolla un CLI (Command Line Interface) que permita 
' * interactuar con Git y GitHub de manera real desde terminal.
' * 
' * El programa debe permitir las siguientes opciones:
' * 1. Establecer el directorio de trabajo
' * 2. Crear un nuevo repositorio
' * 3. Crear una nueva rama
' * 4. Cambiar de rama
' * 5. Mostrar ficheros pendientes de hacer commit
' * 6. Hacer commit (junto con un add de todos los ficheros)
' * 7. Mostrar el historial de commits
' * 8. Eliminar rama
' * 9. Establecer repositorio remoto
' * 10. Hacer pull
' * 11. Hacer push
' * 12. Salir

Imports System.IO

Module GitCommandTool
    Private ReadOnly MENU As String = " Comandos Git:: " & vbCrLf &
        "------------------------------------------------------------" & vbCrLf &
        "| 1. Establecer directorio       | 7. Historial de commits |" & vbCrLf &
        "| 2. Crear repositorio           | 8. Eliminar rama        |" & vbCrLf &
        "| 3. Crear rama                  | 9. Configurar remoto    |" & vbCrLf &
        "| 4. Cambiar rama                | 10. pull                |" & vbCrLf &
        "| 5. Mostrar cambios pendientes  | 11. push                |" & vbCrLf &
        "| 6. 'add' + 'commit'            | 12. Salir               |" & vbCrLf &
        "------------------------------------------------------------"

    Private Class GitCommand
        Public Property Name As String
        Public Property Command As String
        Public Property Prompt As String

        Public Sub New(name As String, command As String, Optional prompt As String = Nothing)
            Me.Name = name
            Me.Command = command
            Me.Prompt = prompt
        End Sub
    End Class

    Private ReadOnly COMMANDS As GitCommand() = {
        New GitCommand("Establecer directorio", "cd", "Ruta: "),
        New GitCommand("Crear repositorio", "git init && git branch -M main"),
        New GitCommand("Crear rama", "git branch -c", "Nombre: "),
        New GitCommand("Cambiar rama", "git switch", "Nombre: "),
        New GitCommand("Mostrar cambios", "git status -s"),
        New GitCommand("Commit", "git add . && git commit -m", "Mensaje: "),
        New GitCommand("Historial", "git log --oneline"),
        New GitCommand("Eliminar rama", "git branch -d", "Nombre: "),
        New GitCommand("Configurar remoto", "git remote add origin", "URL: "),
        New GitCommand("Pull", "git pull origin", "rama: "),
        New GitCommand("Push", "git push origin", "rama: "),
        New GitCommand("Exit", "exit")
    }

    Private Function RunCommand(command As String) As Boolean
        Try
            Dim processInfo As New ProcessStartInfo("cmd.exe", $"/c {command}")
            processInfo.RedirectStandardOutput = True
            processInfo.RedirectStandardError = True
            processInfo.UseShellExecute = False
            processInfo.CreateNoWindow = True

            Using process As Process = Process.Start(processInfo)
                Dim output As String = process.StandardOutput.ReadToEnd()
                Dim error_ As String = process.StandardError.ReadToEnd()
                process.WaitForExit()

                If Not String.IsNullOrEmpty(output) Then
                    Console.ForegroundColor = ConsoleColor.Green
                    Console.WriteLine($"'^': {output.Trim()}")
                    Console.ResetColor()
                End If

                If Not String.IsNullOrEmpty(error_) Then
                    Console.ForegroundColor = ConsoleColor.Red
                    Console.WriteLine($"'X': {error_.Trim()}")
                    Console.ResetColor()
                End If

                Return process.ExitCode = 0
            End Using
        Catch ex As Exception
            Console.ForegroundColor = ConsoleColor.Red
            Console.WriteLine($"❌: Error ejecutando el comando: {ex.Message}")
            Console.ResetColor()
            Return False
        End Try
    End Function

    Private Function ReadInput(prompt As String) As String
        Console.Write(prompt)
        Return Console.ReadLine()?.Trim()
    End Function

    Private Sub Execute(cmd As GitCommand)
        Console.WriteLine($"{vbCrLf}=> {cmd.Name}")
        Console.WriteLine("--------------------")
        If cmd.Name = "Exit" Then
            Console.WriteLine("Bye")
            End
        End If

        If Not String.IsNullOrEmpty(cmd.Prompt) Then
            Dim userInput As String = ReadInput(cmd.Prompt)

            If cmd.Name = "Establecer directorio" Then
                If Directory.Exists(userInput) Then
                    Try
                        Environment.CurrentDirectory = userInput
                        Console.WriteLine($"Directorio cambiado a: {userInput}")
                    Catch ex As Exception
                        Console.WriteLine($"Error cambiando directorio: {ex.Message}")
                    End Try
                Else
                    Console.WriteLine("Esta ruta no existe.")
                End If
            Else
                RunCommand($"{cmd.Command} {userInput}")
            End If
        Else
            RunCommand(cmd.Command)
        End If
    End Sub

    Sub Main()
        While True
            Console.WriteLine(MENU)
            Console.WriteLine($"Directorio actual: {Environment.CurrentDirectory}")
            Console.WriteLine("--------------------")

            Dim input As String = ReadInput(vbCrLf & "Opción: ")
            Dim option_ As Integer

            If Integer.TryParse(input, option_) AndAlso option_ > 0 AndAlso option_ <= COMMANDS.Length Then
                If option_ = COMMANDS.Length + 1 Then
                    Exit While
                Else
                    Execute(COMMANDS(option_ - 1))
                End If
            Else
                Console.WriteLine("Opción inválida")
            End If
        End While
    End Sub
End Module
