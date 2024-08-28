' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------------
'* SOLID: PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP)
'-----------------------------------------------------
' - Los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de abstracciones. A su vez, las 
'   abstracciones no deben depender de detalles concretos; los detalles deben depender de las abstracciones.

' ____________________________________________________
' * EJERCICIO #1:
'* Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
'* Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
'* de forma correcta e incorrecta.

' ____________________________________________________
' De manera INCORRECTA

' Clase de bajo nivel
Public Class CsvExporter_
    Public Sub Export(Data As String)
        Console.WriteLine($"Exportando datos a CSV: {Data}")
    End Sub
End Class

' Clase de bajo nivel
Public Class JsonExporter_
    Public Sub Export(Data As String)
        Console.WriteLine($"Exportando datos a JSON: {Data}")
    End Sub
End Class

' Clase de alto nivel
Public Class ReportGenerator_
    Private _csvExporter As CsvExporter_
    Private _jsonExporter As JsonExporter_

    Public Sub New()
        ' Dependencia de clases especificas(módulos de bajo nivel)
        _csvExporter = New CsvExporter_
        _jsonExporter = New JsonExporter_
    End Sub

    Public Sub GenerateCsvReport(Data As String)
        _csvExporter.Export(Data)
    End Sub

    Public Sub GenerateJsonReport(Data As String)
        _jsonExporter.Export(Data)
    End Sub
End Class

' ____________________________________________________
' De manera CORRECTA

Public Interface IExporter
    Sub Export(Data As String)
End Interface

' Implementación
Public Class CsvExporter
    Implements IExporter

    Public Sub Export(Data As String) Implements IExporter.Export
        Console.WriteLine($"Exportando datos a CSV: {Data}")
    End Sub
End Class

' Implementación
Public Class JsonExporter
    Implements IExporter

    Public Sub Export(Data As String) Implements IExporter.Export
        Console.WriteLine($"Exportando datos a JSON: {Data}")
    End Sub
End Class

' Clase de alto nivel
Public Class ReportGenerator
    Private _Exporter As IExporter

    Public Sub New(Exporter As IExporter)
        ' Ya no está dependiendo de una clase específica(módulo de bajo nivel).
        ' Depende de las instancias que recibe, las cuales implementan la interfaz.
        _Exporter = Exporter
    End Sub

    Public Sub Generate(Data As String)
        _Exporter.Export(Data)
    End Sub
End Class

' ____________________________________________________
' * EJERCICIO #2:
'* Crea un sistema de notificaciones.
'* Requisitos:
'* 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
'* 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
'* Instrucciones:
'* 1. Crea la interfaz o clase abstracta.
'* 2. Desarrolla las implementaciones específicas.
'* 3. Crea el sistema de notificaciones usando el DIP.
'* 4. Desarrolla un código que compruebe que se cumple el principio.

Public Interface INotificationService
    Sub Send(To_ As Object, Msg As String)
End Interface

' Implementación
Public Class EmailService
    Implements INotificationService

    Public Sub Send(To_ As Object, Msg As String) Implements INotificationService.Send
        Console.WriteLine($"Correo enviado a: {To_}")
        Console.WriteLine($"Mensaje: {Msg}")
    End Sub
End Class

' Implementación
Public Class PUSHService
    Implements INotificationService

    Public Sub Send(To_ As Object, Msg As String) Implements INotificationService.Send
        Console.WriteLine($"Notificación PUSH enviado a: {To_}")
        Console.WriteLine($"Mensaje: {Msg}")
    End Sub
End Class

' Implementación
Public Class SMSService
    Implements INotificationService

    Public Sub Send(To_ As Object, Msg As String) Implements INotificationService.Send
        Console.WriteLine($"Mensaje SMS enviado a: {To_}")
        Console.WriteLine($"Mensaje: {Msg}")
    End Sub
End Class

' Clase de alto nivel
Public Class NotificationSystem
    Private _Service As INotificationService

    'Depende de las inatancias recibidas, las cuales implementan la interfaz.
    Public Sub New(Service As INotificationService)
        _Service = Service
    End Sub

    Public Sub Notify(To_ As Object, Msg As String)
        _Service.Send(To_, Msg)
    End Sub
End Class

' ____________________________________________________
Public Module Program

    ' Comprobación de exs 2
    Public Sub TestNotificationSystem(To_ As Object, Msg As String, Service As INotificationService)
        ' Inyeccion
        Dim ServiceNotifer As New NotificationSystem(Service)
        ServiceNotifer.Notify(To_, Msg)
    End Sub

    Public Sub Main()
        '________________________________________
        ' Exs 1
        Console.WriteLine(vbCrLf + "Exs #1")
        '_________
        Console.WriteLine("Implementación incorrecta:")

        Dim reportGenerator_ As New ReportGenerator_
        reportGenerator_.GenerateCsvReport("Contenido x")
        reportGenerator_.GenerateJsonReport("Contenido x")

        '_________
        Console.WriteLine("Implementación correcta:")

        ' Intancias de las implementaciones:
        Dim csvExporter As New CsvExporter
        Dim jsonExporter As New JsonExporter

        ' Instancia de Clase 'alto nivel' con Inyeccion de dependencia:
        Dim csvReport As New ReportGenerator(csvExporter)
        Dim jsonReport As New ReportGenerator(jsonExporter)

        ' Uso del metodo implementado:
        csvReport.Generate("Contenido x")
        jsonReport.Generate("Contenido x")

        '________________________________________
        ' Exs 2
        Console.WriteLine(vbCrLf + "Exs #2")

        ' Intancias de las implementaciones
        Dim emailService As New EmailService()
        Dim pUSHService As New PUSHService()
        Dim sMSService As New SMSService()

        ' Pruebas
        TestNotificationSystem("ejm@gg.com", "abcdsf", emailService)
        TestNotificationSystem("user01", "123456", pUSHService)
        TestNotificationSystem(123456789, "aeiou", sMSService)

    End Sub
End Module
