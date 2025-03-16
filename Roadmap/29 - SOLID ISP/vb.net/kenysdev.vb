' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------------
'* SOLID: PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP)
'-----------------------------------------------------
' - Una clase no debería estar obligada a implementar interfaces que no utiliza.
'   Evitando crear grandes clases monolíticas.

'__________________________
' NOTA: Este ejemplo muestra el uso CORRECTO. Para suponer un ejemplo que viole el principio, sería. 
'       Imaginar todos los métodos siguientes, en una sola interfaz, entonces algunos dispositivos
'       implementarían una interfaz que no necesitan.

Public Interface IPlayable
    Sub Play()
End Interface

Public Interface IDisplayable
    Sub Display()
End Interface

' ____________________________________________________
' Implementar
Public Class Speaker
    Implements IPlayable

    Public Sub Play() Implements IPlayable.Play
        Console.WriteLine("El altavoz está reproduciendo música.")
    End Sub
End Class

Public Class Phone
    Implements IPlayable, IDisplayable

    Public Sub Play() Implements IPlayable.Play
        Console.WriteLine("El teléfono está reproduciendo una canción.")
    End Sub

    Public Sub Display() Implements IDisplayable.Display
        Console.WriteLine("El teléfono está mostrando la pantalla de reproducción.")
    End Sub
End Class

'__________________________
'* EJERCICIO
'* Crea un gestor de impresoras.
'* Requisitos:
'* 1. Algunas impresoras sólo imprimen en blanco y negro.
'* 2. Otras sólo a color.
'* 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
'* Instrucciones:
'* 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
'* 2. Aplica el ISP a la implementación.
'* 3. Desarrolla un código que compruebe que se cumple el principio.

Public Interface IPrinter
    Sub PrintFile(file As String)
End Interface

Public Interface IScanner
    Sub ToScan(pathSave As String)
End Interface

Public Interface IFax
    Sub SendFile(file As String, phoneNumber As Integer)
End Interface

' ____________________________________________________
' Implementaciones
Public Class MonoPrinter
    Implements IPrinter

    Public Sub PrintFile(file As String) Implements IPrinter.PrintFile
        Console.WriteLine(vbCrLf + "Impresora blanco y negro:")
        Console.WriteLine(file + " se imprimió.")
    End Sub
End Class

Public Class ColorPrinter
    Implements IPrinter

    Public Sub PrintFile(file As String) Implements IPrinter.PrintFile
        Console.WriteLine(vbCrLf + "Impresora a color:")
        Console.WriteLine(file + " se imprimió.")
    End Sub
End Class

Public Class Scanner
    Implements IScanner

    Public Sub ToScan(pathSave As String) Implements IScanner.ToScan
        Console.WriteLine(vbCrLf + "Escaneo realizado, Guardado en: " + pathSave)
    End Sub
End Class

Public Class Fax
    Implements IFax

    Public Sub SendFile(file As String, phoneNumber As Integer) Implements IFax.SendFile
        Console.WriteLine(vbCrLf + $"{file} Fue enviado a: {phoneNumber}")
    End Sub
End Class

Public Class MultiFunctionPrinter
    Public monoPrinter As New MonoPrinter
    Public colorPrinter As New ColorPrinter
    Public theScanner As New Scanner
    Public fax As New Fax
End Class

' ____________________________________________________
Public Module Program
    Public Sub Main()
        ' Exs 1
        Dim phone As New Phone()
        phone.Play()
        phone.Display()

        Dim speaker As New Speaker()
        speaker.Play()

        '_____________________________________________
        ' Exs 2
        Console.WriteLine(vbCrLf + "Exs #2")

        Dim MonoPrinter As New MonoPrinter
        MonoPrinter.PrintFile("filex.pdf")

        Dim ColorPrinter As New ColorPrinter
        ColorPrinter.PrintFile("filex.pdf")

        Dim theScanner As New Scanner
        theScanner.ToScan("c:\\docs")

        Dim Fax As New Fax
        Fax.SendFile("filex.pdf", 12345678)

        Console.WriteLine(vbCrLf + "___________" + vbCrLf + "Multifunción")

        Dim MultiFunctionPrinter As New MultiFunctionPrinter
        MultiFunctionPrinter.monoPrinter.PrintFile("filex.pdf")
        MultiFunctionPrinter.colorPrinter.PrintFile("filex.pdf")
        MultiFunctionPrinter.theScanner.ToScan("c:\\docs")
        MultiFunctionPrinter.fax.SendFile("filex.pdf", 12345678)

    End Sub
End Module
