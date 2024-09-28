' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'MANEJO DE FICHEROS 
'-----------------------------------------------
Imports System.IO
Module Program
    Public Class FileMg
        Public Property _path As String

        Public Sub New(path As String)
            Me._path = path
        End Sub

        Public Sub CreateFile()
            Try
                If Not File.Exists(_path) Then
                    Dim archivo As FileStream = File.Create(_path)
                    archivo.Close()
                End If
            Catch ex As Exception
                Console.WriteLine("Error->f.CreateFile->" & ex.Message)
            End Try
        End Sub

        Public Sub AppendLine(line As String)
            Try
                Using writer As StreamWriter = File.AppendText(_path)
                    writer.WriteLine(line)
                End Using
            Catch ex As Exception
                Console.WriteLine("Error->f.AppendLine->" & ex.Message)
            End Try
        End Sub

        Public Sub WriteLines(lines As List(Of String))
            Try
                File.WriteAllLines(_path, lines)
            Catch ex As Exception
                Console.WriteLine("Error->f.WriteLines->" & ex.Message)
            End Try
        End Sub

        Public Function ReadLines() As List(Of String)
            Try
                Dim lines As List(Of String) = New List(Of String)(File.ReadAllLines(_path))
                Return lines
            Catch ex As Exception
                Console.WriteLine("Error->f.ReadLines->" & ex.Message)
                Return Nothing
            End Try
        End Function

        Public Sub Print()
            Try
                Dim lines As String() = File.ReadAllLines(_path)
                For Each line As String In lines
                    Console.WriteLine(line)
                Next
            Catch ex As Exception
                Console.WriteLine("Error->f.Print->" & ex.Message)
            End Try
        End Sub

        Public Function QueryFile(qry As String) As Integer
            Try
                Dim lines As String() = File.ReadAllLines(_path)
                Dim i As Integer = 0
                For Each ln As String In lines
                    Dim parts As String() = ln.Split(","c)
                    Dim name As String = parts(0)
                    If name = $"[{qry}]" Then
                        Console.WriteLine(ln)
                        Return i
                    End If
                    i += 1
                Next
                Console.WriteLine("No existe.")
                Return -1
            Catch ex As Exception
                Console.WriteLine("Error->QueryFile->" & ex.Message)
                Return -1
            End Try
        End Function

        Public Sub DeleteFile()
            Try
                File.Delete(_path)
                Console.WriteLine(_path & "-> Eliminado.")
            Catch ex As Exception
                Console.WriteLine("Error->DeleteFile->" & ex.Message)
            End Try
        End Sub
    End Class

    '* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
    '* archivo .txt.
    '* - Cada producto se guarda en una línea del arhivo de la siguiente manera:
    '*   [nombre_producto], [cantidad_vendida], [precio].
    '* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
    '*   actualizar, eliminar productos y salir.
    '* - También debe poseer opciones para calcular la venta total y por producto.
    '* - La opción salir borra el .txt.

    Const PATH As String = "sale_mgt.txt"
    Const MSG As String = "
        Gestión de Ventas:
╔═════════════════════════════════╗
║ 1. Agregar        4. Editar     ║  
║ 2. Consultar      5. Facturar   ║
║ 3. Eliminar       6. salir.     ║
╚═════════════════════════════════╝
"

    Public Function AddProduct(Sale As FileMg, Optional prod As String = "", Optional qty As String = "",
                               Optional price As String = "") As String
        While True
            If String.IsNullOrWhiteSpace(prod) Then
                Console.WriteLine("Debe ingresar un nombre de producto.")
                Console.Write("Producto: ")
                prod = Console.ReadLine()
            ElseIf String.IsNullOrWhiteSpace(qty) OrElse Not Double.TryParse(qty, 0) Then
                Console.WriteLine("Debe ingresar una cantidad.")
                Console.Write("Cantidad: ")
                qty = Console.ReadLine()
            ElseIf String.IsNullOrWhiteSpace(price) OrElse Not Double.TryParse(price, 0) Then
                Console.WriteLine("Debe ingresar un precio.")
                Console.Write("Precio: ")
                price = Console.ReadLine()
            Else
                Dim line As String = $"[{prod}], [{qty}], [{price}]"
                Sale.AppendLine(line)
                Console.WriteLine($"{vbCrLf}Guardado")
                Console.WriteLine(MSG)
                Return $"{line}"
            End If
        End While
        Return ""
    End Function

    Public Sub QueryProduct(Sale As FileMg, Optional qry As String = "")
        If qry.Length = 0 Then
            Console.WriteLine(vbLf & "Consultar Producto.")
            Console.Write("Nombre: ")
            qry = Console.ReadLine()
        End If
        Sale.QueryFile(qry)
    End Sub

    Public Sub DeleteProduct(Sale As FileMg, Optional qry As String = "")
        If qry.Length = 0 Then
            Console.WriteLine(vbCrLf & "Eliminar Producto.")
            Console.Write("Nombre: ")
            qry = Console.ReadLine()
        End If
        Dim numLine As Integer = Sale.QueryFile(qry)
        If numLine <> -1 Then
            Dim products As List(Of String) = New List(Of String)(Sale.ReadLines())
            products.RemoveAt(numLine)
            Sale.WriteLines(products)
            Console.WriteLine("Producto eliminado")
        End If
    End Sub

    Public Sub UpdateProduct(Sale As FileMg, Optional qry As String = "")
        If qry.Length = 0 Then
            Console.WriteLine(vbCrLf & "Editar Producto.")
            Console.Write("Nombre: ")
            qry = Console.ReadLine()
        End If

        Dim numLine As Integer = Sale.QueryFile(qry)

        If numLine <> -1 Then
            Dim products As List(Of String) = New List(Of String)(Sale.ReadLines())
            Dim line As String = AddProduct(Sale)
            products(numLine) = line
            Sale.WriteLines(products)
        End If
    End Sub

    Public Sub Invoice(Sale As FileMg)
        Console.WriteLine(vbLf & "Factura" & vbLf & "---------------------------")
        Dim lines As List(Of String) = Sale.ReadLines()
        Dim total As Double = 0
        For Each line As String In lines
            Dim a = line.Split(","c)(1).Trim()
            Dim qty As Double = Double.Parse(a.Trim(" "c, "["c, "]"c), System.Globalization.CultureInfo.InvariantCulture)

            Dim b = line.Split(","c)(2).Trim()
            Dim price As Double = Double.Parse(b.Trim(" "c, "["c, "]"c), System.Globalization.CultureInfo.InvariantCulture)

            Dim ln = line.Trim(ControlChars.Lf)
            Dim subTotal As Double = qty * price
            Dim FsubTotal As String = $"${subTotal:0.00}"
            Console.WriteLine($"{ln} -> {FsubTotal}")
            total += subTotal
        Next
        Console.WriteLine(vbLf & $"Monto total: ${total:0.00}")
    End Sub

    Sub Main()
        Dim user As New FileMg("kenysdev.txt")
        user.CreateFile()
        Dim lines As New List(Of String) From {"Ken", "121"}
        user.WriteLines(lines)
        user.AppendLine(".py")
        user.Print()
        user.DeleteFile()

        '_________________________________
        Dim Sale As New FileMg(PATH)
        Sale.CreateFile()
        Console.WriteLine(MSG)

        While True
            Console.Write(vbCrLf & "Opción: ")
            Dim theoption As String = Console.ReadLine()

            Select Case theoption
                Case "1"
                    AddProduct(Sale)
                Case "2"
                    QueryProduct(Sale)
                Case "3"
                    DeleteProduct(Sale)
                Case "4"
                    UpdateProduct(Sale)
                Case "5"
                    Invoice(Sale)
                Case "6"
                    Console.WriteLine("Adios")
                    Sale.DeleteFile()
                    Return
                Case Else
                    Console.WriteLine("Opción 1 -> 6")
            End Select
        End While
    End Sub
End Module
