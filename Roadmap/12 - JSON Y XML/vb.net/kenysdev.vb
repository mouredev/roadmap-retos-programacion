' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* JSON Y XML
'-----------------------------------------------
'- son formatos de intercambio de datos que estructuran información.
'- JSON (JavaScript Object Notation) y XML (eXtensible Markup Language)
Imports System.IO
Imports System.Text.Json
Imports System.Xml
Imports System.Xml.Linq

Module Program
    Sub Main()
        Dim userDic As New Dictionary(Of String, Object) From {
            {"name", "Ken"},
            {"age", 121},
            {"dob", "1903-03-19"},
            {"prog_langs", New List(Of String) From {"cs", "py", "vb", "rs", "js"}}
        }

        ' _______________________________________________
        ' * JSON
        ' serializar
        Dim options = New JsonSerializerOptions With {
            .WriteIndented = True
        }

        Dim json As String = JsonSerializer.Serialize(userDic, options)
        File.WriteAllText("user.json", json)

        ' Deserializar
        Dim readJson = File.ReadAllText("user.json")
        Dim DesUserJson = JsonSerializer.Deserialize(Of Dictionary(Of String, Object))(readJson)
        Console.WriteLine(DesUserJson("name"))

        ' _______________________________________________
        ' * XML
        ' serializar
        userDic("prog_langs") = "cs,py,vb,rs,js"
        Using writer As New XmlTextWriter("user.xml", Nothing)
            writer.Formatting = Formatting.Indented
            writer.WriteStartDocument()
            writer.WriteStartElement("user")

            For Each pair In userDic
                writer.WriteStartElement(pair.Key)
                writer.WriteValue(pair.Value)
                writer.WriteEndElement()
            Next

            writer.WriteEndElement()
            writer.WriteEndDocument()
        End Using

        ' Deserializar
        Dim doc = XDocument.Load("user.xml")
        Dim userElement = doc.Root
        Dim name = userElement.Element("name").Value
        Console.WriteLine(name)

        ' _______________________________________________
        ' * EJERCICIO
        ' * Utilizando la lógica de creación de los archivos anteriores, crea un
        ' * programa capaz de leer y transformar en una misma clase custom de tu 
        ' * lenguaje los datos almacenados en el XML y el JSON.
        ' * Borra los archivos.

        Dim theFile As New XmlOrJson("user.json")
        Dim dicUser = theFile.AsDictionary()
        Console.WriteLine(vbLf & "Documento JSON")
        For Each kv In dicUser
            If kv.Key <> "prog_langs" Then
                Console.WriteLine($"{kv.Key}: {kv.Value}")
            End If
        Next
        Dim progLangs As List(Of String) = DirectCast(dicUser("prog_langs"), List(Of String))
        Console.WriteLine(String.Join(", ", progLangs))

        '_________
        Dim theFile2 As New XmlOrJson("user.xml")
        Dim dicUser2 As Dictionary(Of String, Object) = theFile2.AsDictionary()
        Console.WriteLine(vbLf & "Documento XML")
        For Each kv In dicUser2
            If kv.Key <> "prog_langs" Then
                Console.WriteLine($"{kv.Key}: {kv.Value}")
            End If
        Next
        Dim progLangs2 As List(Of String) = DirectCast(dicUser2("prog_langs"), List(Of String))
        Console.WriteLine(String.Join(", ", progLangs2))

        '_________
        Console.WriteLine(vbLf & "Acceder directamente")
        Console.WriteLine(theFile2.name)
        Console.WriteLine(theFile2.age)
        Console.WriteLine(theFile2.dob)
        File.Delete("user.json")
        File.Delete("user.xml")

    End Sub

    Public Class XmlOrJson
        Private path As String
        Private extension As String
        Private dicUser As Dictionary(Of String, Object)
        Public name As String
        Public age As Integer
        Public dob As String
        Public langs As List(Of String)

        Public Sub New(ByVal path As String)
            If path Is Nothing Then
                Throw New ArgumentNullException("path", "Debe proporcionar una ruta.")
            End If
            Me.path = path
            Me.extension = path.Split("."c).LastOrDefault()
            Me.dicUser = New Dictionary(Of String, Object)()
            Me.name = String.Empty
            Me.age = 0
            Me.dob = String.Empty
            Me.langs = New List(Of String)()
        End Sub

        Private Sub AddToDic()
            dicUser("name") = name
            dicUser("age") = age
            dicUser("dob") = dob
            dicUser("prog_langs") = langs
        End Sub

        Public Function AsDictionary() As Dictionary(Of String, Object)
            Try
                If extension = "json" Then
                    Dim readJson As String = File.ReadAllText(path)
                    Using document = JsonDocument.Parse(readJson)
                        Dim root = document.RootElement
                        name = root.GetProperty("name").GetString()
                        age = root.GetProperty("age").GetInt32()
                        dob = root.GetProperty("dob").GetString()
                        For Each lang In root.GetProperty("prog_langs").EnumerateArray()
                            langs.Add(lang.GetString())
                        Next
                        AddToDic()
                        Return dicUser
                    End Using

                ElseIf extension = "xml" Then
                    Dim doc = XDocument.Load(path)
                    Dim userElement = doc.Root
                    name = userElement.Element("name").Value
                    age = Integer.Parse(userElement.Element("age").Value)
                    dob = userElement.Element("dob").Value
                    langs = userElement.Element("prog_langs").Value.Split(","c).ToList()
                    AddToDic()
                    Return dicUser
                Else
                    Console.WriteLine("Archivo no compatible.")
                    Return Nothing
                End If
            Catch ex As Exception
                Console.WriteLine($"Exception: {ex.GetType()}")
                Return Nothing
            End Try
        End Function
    End Class
End Module
