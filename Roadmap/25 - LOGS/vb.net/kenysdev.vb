' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* LOGS
'-----------------------------------------------
'Mas info: https://nlog-project.org/

Imports NLog
Imports NLog.Config
Imports NLog.Targets

Module Program

    Private Logger As Logger = LogManager.GetCurrentClassLogger()

    Sub Main()
        '* EJERCICIO #1:
        '* Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
        '* un ejemplo con cada nivel de "severidad" disponible.

        ' Configuración manual
        Dim config As New LoggingConfiguration()

        ' Definir el destino del log)
        Dim consoleTarget As New ConsoleTarget("console")
        config.AddTarget("console", consoleTarget)

        ' Definir las reglas de log
        config.AddRuleForAllLevels(consoleTarget)

        ' Aplicar la configuración
        LogManager.Configuration = config

        ' Ejemplo de uso:
        Logger.Trace("msg Trace")
        Logger.Debug("msg Debug")
        Logger.Info("msg Info")
        Logger.Warn("msg Warn")
        Logger.Error("msg Error")
        Logger.Fatal("msg Fatal")

        '_________________________________________________
        Console.WriteLine(vbLf & "EJERCICIO #2")
        Dim tasks As New ProgramTask()

        tasks.Add("a", "1")
        tasks.Add("b", "2")
        tasks.Add("c", "3")

        tasks.Delete("b")
        tasks.ShowList()

    End Sub

    '-----------------------------------------------
    '* EJERCICIO #2
    '* Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
    '* y listar dichas tareas.
    '* - Añadir: recibe nombre y descripción.
    '* - Eliminar: por nombre de la tarea.
    '* Implementa diferentes mensajes de log que muestren información según la 
    '* tarea ejecutada (a tu elección).
    '* Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 

    Public Class ProgramTask
        Private Shared ReadOnly logger As Logger = LogManager.GetCurrentClassLogger()
        Private ReadOnly tasks As Dictionary(Of String, String)

        Public Sub New()
            tasks = New Dictionary(Of String, String)()
            logger.Debug("Se inició instancia de la clase ProgramTask.")
        End Sub

        Public Sub Add(name As String, description As String)
            tasks(name) = description
            logger.Info("Se agregó una tarea.")
        End Sub

        Public Sub Delete(name As String)
            If tasks.Remove(name) Then
                logger.Info($"Tarea '{name}' eliminada.")
            Else
                Console.WriteLine()
                logger.Warn($"No se encontró la tarea '{name}'.")
            End If
        End Sub

        Public Sub ShowList()
            logger.Info("Lista de tareas")
            For Each task In tasks
                Console.WriteLine($"{task.Key} -- {task.Value}")
            Next
        End Sub
    End Class
End Module
