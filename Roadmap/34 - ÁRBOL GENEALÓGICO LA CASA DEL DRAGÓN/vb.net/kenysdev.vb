' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------------
'* 34 ÁRBOL GENEALÓGICO DE LA CASA DEL DRAGÓN
'-----------------------------------------------------
'* ¡La Casa del Dragón ha finalizado y no volverá hasta 2026! 
' * ¿Alguien se entera de todas las relaciones de parentesco
' * entre personajes que aparecen en la saga?
' * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
' * Requisitos:
' * 1. Estará formado por personas con las siguientes propiedades
' *    - Identificador único (obligatorio)
' *    - Nombre (obligatorio)
' *    - Pareja (opcional)
' *    - Hijos (opcional)
' * 2. Una persona sólo puede tener una pareja (para simplificarlo).
' * 3. Las relaciones deben validarse dentro de lo posible.
' *    Ejemplo: Un hijo no puede tener tres padres.
' * Acciones:
' * 1. Crea un programa que permita crear y modificar el árbol.
' *    - Añadir y eliminar personas
' *    - Modificar pareja e hijos
' * 2. Podrás imprimir el árbol (de la manera que consideres).
' * 
' * NOTA: Ten en cuenta que la complejidad puede ser alta si
' * se implementan todas las posibles relaciones. Intenta marcar
' * tus propias reglas y límites para que te resulte asumible.

'_______
' NOTE Here Is the 'people.json' file with the data if you want to test it:
'      https://pastebin.com/29kWWgPU
'      Just paste it into the base folder.

Imports System.IO
Imports System.Text
Imports System.Text.Json

'___________________________________________________
Public Class Person
    Public Property Id As Integer
    Public Property Name As String
    Public Property Parents As New List(Of Integer)
    Public Property Partners As New List(Of Integer)
    Public Property Children As New Dictionary(Of Integer, List(Of Integer))
    Public Property Deleted As Boolean

    Public Sub New(id As Integer, name As String)
        Me.Id = id
        Me.Name = name
    End Sub

    Public Function ToDict() As Dictionary(Of String, Object)
        Return New Dictionary(Of String, Object) From {
            {"id", Id},
            {"name", Name},
            {"parents", Parents},
            {"partners", Partners},
            {"children", Children},
            {"deleted", Deleted}
        }
    End Function

    Public Shared Function FromDict(data As Dictionary(Of String, Object)) As Person
        Dim person As New Person(CInt(data("id")), CStr(data("name")))

        If data.ContainsKey("parents") Then
            person.Parents = DirectCast(data("parents"), List(Of Integer))
        End If

        If data.ContainsKey("partners") Then
            person.Partners = DirectCast(data("partners"), List(Of Integer))
        End If

        If data.ContainsKey("children") Then
            person.Children = JsonSerializer.Deserialize(Of Dictionary(Of Integer, List(Of Integer)))(
                DirectCast(data("children"), JsonElement).GetRawText()
            )
        End If

        If data.ContainsKey("deleted") Then
            person.Deleted = CBool(data("deleted"))
        End If

        Return person
    End Function

    Public Overrides Function ToString() As String
        Return $"Person(id={Id}, name='{Name}')"
    End Function
End Class

'___________________________________________________
Public Module Input
    Public Function GetStr(msg As String) As String
        Do
            Console.Write(msg)
            Dim txt As String = Console.ReadLine()
            If Not String.IsNullOrEmpty(txt) Then
                Return txt
            End If

            Console.WriteLine(vbCrLf & "❌ This field cannot be empty.")
        Loop
    End Function

    Public Function GetInt(msg As String) As Integer
        Do
            Dim txt As String = GetStr(msg)
            Dim result As Integer
            If Integer.TryParse(txt, result) Then
                Return result
            End If

            Console.WriteLine(vbCrLf & "❌ Enter an integer.")
        Loop
    End Function
End Module

'___________________________________________________
Public Class People
    Private _people As New List(Of Person)()
    Private ReadOnly _filename As String
    Private Shared ReadOnly _jsonOptions As New JsonSerializerOptions(JsonSerializerDefaults.Web) With {.WriteIndented = True}

    Public Sub New(Optional filename As String = "people.json")
        _filename = filename
        LoadFromJson()
    End Sub

    Public Function GetPeople() As IReadOnlyList(Of Person)
        Return _people.AsReadOnly()
    End Function

    Public Sub LoadFromJson()
        Try
            Dim jsonString As String = File.ReadAllText(_filename)
            _people = JsonSerializer.Deserialize(Of List(Of Person))(jsonString, _jsonOptions)
            If _people Is Nothing Then _people = New List(Of Person)()
            Console.WriteLine($"✅ The file '{_filename}' has been successfully loaded.")
        Catch ex As Exception
            Console.WriteLine($"⚠️ The file '{_filename}' not found. Starting with an empty list.")
            _people = New List(Of Person) From {New Person(0, "unknown")}
        End Try
    End Sub

    Public Sub SaveToJson()
        Try
            Dim jsonString As String = JsonSerializer.Serialize(_people, _jsonOptions)
            File.WriteAllText(_filename, jsonString)
            Console.WriteLine($"✅ Data saved successfully to {_filename}")
        Catch e As Exception
            Console.WriteLine($"❌ An error occurred while saving to '{_filename}': {e.Message}. Data may not have been saved.")
        End Try
    End Sub

    Public Sub PrintPeople()
        Console.WriteLine(New String("_"c, 32))
        Console.WriteLine($"|{"id",4}|{"Name",-25}|")
        Console.WriteLine(New String("_"c, 32))
        For Each person In _people.Where(Function(p) Not p.Deleted)
            Console.WriteLine($"|{person.Id,4}|{person.Name,-25}|")
        Next
        Console.WriteLine(New String("_"c, 32))
    End Sub

    Public Function GetPersonById(id As Integer) As Person
        Dim person = _people.FirstOrDefault(Function(p) p.Id = id)
        If person Is Nothing Then
            Console.WriteLine("❌ ID not found.")
        End If
        Return person
    End Function

    Public Sub AddPerson()
        Console.WriteLine("Add Person or 'x' to Exit")
        Dim name As String = Input.GetStr("Name: ")
        If name.Equals("x", StringComparison.CurrentCultureIgnoreCase) Then
            Console.WriteLine("Exit")
            Return
        End If

        Dim newId As Integer = If(_people.Count > 0, _people.Max(Function(p) p.Id) + 1, 0)
        Dim newPerson As New Person(newId, name)
        _people.Add(newPerson)
        Console.WriteLine($"✅ Added: {newPerson}")
        SaveToJson()
    End Sub

    Public Sub RemovePerson()
        PrintPeople()
        Console.WriteLine(vbCrLf & "Person ID to mark as deleted or a letter to exit.")
        Dim idStr As String = Input.GetStr("ID: ")
        Dim id As Integer
        If Not Integer.TryParse(idStr, id) Then
            Console.WriteLine("Exit")
            Return
        End If

        Dim person = GetPersonById(id)
        If person Is Nothing Then Return

        If person.Partners.Count <> 0 OrElse person.Parents.Count <> 0 Then
            Console.WriteLine("❌ You cannot delete a person who is linked to parents or partners.")
            Return
        End If

        person.Deleted = True
        Console.WriteLine($"✅ '{person.Name}' is marked as deleted.")
        SaveToJson()
    End Sub

    Public ReadOnly Property Count As Integer
        Get
            Return _people.Count
        End Get
    End Property
End Class

'___________________________________________________
Public Class Partners
    Inherits People

    Private Sub Add(partners As List(Of Integer), idPerson As Integer)
        Console.WriteLine("Select Partner ID")
        Dim idPartner As Integer = Input.GetInt("ID: ")
        Dim partner = GetPersonById(idPartner)
        If partner Is Nothing OrElse partner.Deleted Then
            Console.WriteLine("❌ ID not found or the person is deleted.")
            Return
        End If

        If partners.Contains(idPartner) Then
            Console.WriteLine("❌ This partner is already added.")
            Return
        End If

        partners.Add(idPartner)
        partner.Partners.Add(idPerson)

        Console.WriteLine("✅ Partner successfully added.")
        SaveToJson()
    End Sub

    Private Sub Remove(partners As List(Of Integer), idPerson As Integer)
        Console.WriteLine("Select Partner ID to Delete")
        Dim id As Integer = Input.GetInt("ID: ")
        If Not partners.Contains(id) Then
            Console.WriteLine("❌ ID not found.")
            Return
        End If

        Dim partner = GetPersonById(id)
        If partner Is Nothing Then
            Console.WriteLine("❌ Partner not found.")
            Return
        End If

        If partner.Children.Count <> 0 Then
            Console.WriteLine("❌ Cannot delete a partner who has children.")
            Return
        End If

        partners.Remove(id)
        partner.Partners.Remove(idPerson)

        Console.WriteLine("✅ Partner deleted")
        SaveToJson()
    End Sub

    Private Sub Options(partners As List(Of Integer), idPerson As Integer)
        Console.WriteLine(vbCrLf & "1. Add partner | 2. Remove partner | 3. Exit")
        Dim option_ As Integer = Input.GetInt(vbCrLf & "Option: ")

        Select Case option_
            Case 1
                Add(partners, idPerson)
            Case 2
                Remove(partners, idPerson)
            Case 3
                Return
            Case Else
                Console.WriteLine("❌ Invalid option.")
        End Select
    End Sub

    Public Sub EditPartners()
        PrintPeople()
        Console.WriteLine(vbCrLf & "Person ID to edit partners or a letter to exit.")
        Dim idStr As String = Input.GetStr("ID: ")
        Dim id As Integer
        If Not Integer.TryParse(idStr, id) Then
            Console.WriteLine("Exit")
            Return
        End If

        Dim person = GetPersonById(id)
        If person Is Nothing OrElse person.Deleted Then
            Console.WriteLine("❌ ID not found or the person is deleted.")
            Return
        End If

        Console.WriteLine($"You selected '{person.Name}'")
        Dim partners = person.Partners

        If partners.Count <> 0 Then
            Console.WriteLine("Partners:")
            For Each idP In partners
                Dim partner = GetPersonById(idP)
                If partner IsNot Nothing Then
                    Console.WriteLine($"ID: {partner.Id} -> {partner.Name}")
                End If
            Next
        Else
            Console.WriteLine("🚫 This person has no partners.")
        End If

        Options(partners, id)
    End Sub
End Class

'___________________________________________________
Public Class Children
    Inherits Partners

    Private _idParent As Integer
    Private _children As Dictionary(Of Integer, List(Of Integer))
    Private _idChild As Integer
    Private _idPartner As Integer

    Private Function SelectPartner(partners As List(Of Integer)) As Integer?
        Console.WriteLine("Partners:")
        For Each idP In partners
            Dim partnerPerson = GetPersonById(idP)
            If partnerPerson IsNot Nothing Then
                Console.WriteLine($"ID: {partnerPerson.Id} -> {partnerPerson.Name}")
            End If
        Next

        Console.WriteLine("Select the ID of the partner with whom you have the child.")
        Dim idPartner As Integer = Input.GetInt("ID: ")
        Dim partner = GetPersonById(idPartner)
        If Not partners.Contains(idPartner) OrElse partner Is Nothing OrElse partner.Deleted Then
            Console.WriteLine("❌ ID not found or the person is deleted.")
            Return Nothing
        End If

        Return idPartner
    End Function

    Private Function UpdateChildParent() As Integer?
        Dim idPartner As Integer = _idPartner
        Console.WriteLine("Select Child ID")
        Dim idChild As Integer = Input.GetInt("ID: ")
        Dim child = GetPersonById(idChild)
        If child Is Nothing Then
            Return Nothing
        End If

        If child.Parents.Count <> 0 Then
            Console.WriteLine("❌ This person already has parents.")
            Return Nothing
        End If

        If _children Is Nothing Then
            _children = New Dictionary(Of Integer, List(Of Integer))()
        End If

        Dim childrenList As List(Of Integer) = Nothing
        If _children.TryGetValue(idPartner, childrenList) Then
            If childrenList IsNot Nothing AndAlso Not childrenList.Contains(idChild) Then
                childrenList.Add(idChild)
            End If
        Else
            _children(idPartner) = New List(Of Integer) From {idChild}
        End If

        Dim parent = GetPersonById(_idParent)
        If parent IsNot Nothing Then
            parent.Children = _children
        End If

        child.Parents = New List(Of Integer) From {_idParent, idPartner}

        Return idChild
    End Function

    Private Sub UpdateChildPartner(partner As Person)
        Dim childrenList As List(Of Integer) = Nothing
        If partner.Children.TryGetValue(_idParent, childrenList) Then
            If childrenList IsNot Nothing AndAlso Not childrenList.Contains(_idChild) Then
                childrenList.Add(_idChild)
            End If
        Else
            partner.Children(_idParent) = New List(Of Integer) From {_idChild}
        End If
    End Sub

    Private Sub Add()
        Dim parent = GetPersonById(_idParent)
        If parent Is Nothing Then
            Console.WriteLine("❌ Parent not found.")
            Return
        End If

        Dim partners = parent.Partners
        If partners.Count = 0 Then
            Console.WriteLine("❌ This person does not have a partner with whom to have children.")
            Return
        End If

        Dim idPartner = SelectPartner(partners)
        If Not idPartner.HasValue Then
            Return
        End If

        Dim partner = GetPersonById(idPartner.Value)
        If partner Is Nothing Then
            Console.WriteLine("❌ Partner not found.")
            Return
        End If

        _idPartner = idPartner.Value
        Dim idChild = UpdateChildParent()
        If Not idChild.HasValue Then
            Return
        End If

        _idChild = idChild.Value
        UpdateChildPartner(partner)

        Console.WriteLine("✅ Child successfully added.")
        SaveToJson()
    End Sub

    Private Sub RemoveAndUpdate(idParent As Integer, idPartner As Integer)
        Dim parent = GetPersonById(idParent)
        If parent Is Nothing Then
            Console.WriteLine("❌ Parent not found.")
            Return
        End If

        Dim childrenWithPartner As List(Of Integer) = Nothing
        If parent.Children.TryGetValue(idPartner, childrenWithPartner) Then
            If childrenWithPartner IsNot Nothing Then
                childrenWithPartner.Remove(_idChild)
                If childrenWithPartner.Count = 0 Then
                    parent.Children.Remove(idPartner)
                Else
                    parent.Children(idPartner) = childrenWithPartner
                End If
            End If
        End If

        Dim child = GetPersonById(_idChild)
        If child IsNot Nothing Then
            child.Parents.Remove(idParent)
        End If

        Console.WriteLine($"✅ Child deleted in parent: (ID: {idParent})")
        SaveToJson()
    End Sub

    Private Sub Remove()
        Console.WriteLine("Select Child ID to Delete")
        _idChild = Input.GetInt("ID: ")
        Dim child = GetPersonById(_idChild)
        If child Is Nothing Then
            Return
        End If

        Dim parents = child.Parents
        If parents.Count <> 2 Then
            Console.WriteLine("❌ Child does not have two parents.")
            Return
        End If

        Dim idP1 As Integer = parents(0), idP2 As Integer = parents(1)
        RemoveAndUpdate(idP1, idP2)
        RemoveAndUpdate(idP2, idP1)
    End Sub

    Private Sub Options()
        Console.WriteLine(vbCrLf & "1. Add child | 2. Remove child | 3. Exit")
        Dim option_ As Integer = Input.GetInt(vbCrLf & "Option: ")

        Select Case option_
            Case 1
                Add()
            Case 2
                Remove()
            Case 3
                Return
            Case Else
                Console.WriteLine("❌ Invalid option.")
        End Select
    End Sub

    Public Sub EditChildren()
        PrintPeople()
        Console.WriteLine(vbCrLf & "Person ID to edit Children or a letter to exit.")
        Dim idStr As String = Input.GetStr("ID: ")
        Dim id As Integer
        If Not Integer.TryParse(idStr, id) Then
            Console.WriteLine("Exit")
            Return
        End If

        Dim parent = GetPersonById(id)
        If parent Is Nothing OrElse parent.Deleted Then
            Console.WriteLine("❌ ID not found or the person is deleted.")
            Return
        End If

        Console.WriteLine($"You selected '{parent.Name}'")
        Dim children = parent.Children
        If children.Count <> 0 Then
            Console.WriteLine("Children:")
            For Each kvp In children
                Dim partner = GetPersonById(kvp.Key)
                Dim partnerName As String = If(partner IsNot Nothing, partner.Name, "Unknown")
                Console.WriteLine($"With ID: {kvp.Key} -> '{partnerName}':")
                For Each childId In kvp.Value
                    Dim child = GetPersonById(childId)
                    Dim childName As String = If(child IsNot Nothing, child.Name, "Unknown")
                    Console.WriteLine($"    ID: {childId} -> '{childName}'")
                Next
            Next
        Else
            Console.WriteLine("🚫 This person has no children.")
        End If

        _idParent = id
        _children = children
        Options()
    End Sub
End Class

'___________________________________________________
Public Class Tree
    Inherits Children

    Private Function FilteredGrandparents() As (Grandparents As List(Of Person), NoPartner As List(Of Person))
        Dim grandparents As New List(Of Person)()
        Dim noPartner As New List(Of Person)()

        For Each person In GetPeople()
            If person.Parents.Count = 0 AndAlso Not person.Deleted AndAlso person.Name <> "unknown" Then
                If person.Partners.Count = 0 Then
                    noPartner.Add(person)
                Else
                    Dim hasGrandparentPartner As Boolean = person.Partners.Any(
                        Function(partnerId)
                            Dim partner = GetPersonById(partnerId)
                            Return partner IsNot Nothing AndAlso grandparents.Contains(partner)
                        End Function
                    )

                    If Not hasGrandparentPartner Then
                        grandparents.Add(person)
                    End If
                End If
            End If
        Next

        Return (grandparents, noPartner)
    End Function

    Private Sub PrintChild(children As List(Of Integer), prefix As String, isLast As Boolean, isRoot As Boolean)
        For i As Integer = 0 To children.Count - 1
            Dim isLastChild As Boolean = i = children.Count - 1
            Dim newPrefix As String = If(isRoot, prefix, prefix.Substring(0, Math.Max(0, prefix.Length - 4)) & If(isLast, "    ", "│   "))

            PrintFamily(
                children(i),
                newPrefix & If(isLastChild, "└── ", "├── "),
                isLastChild,
                False
            )
        Next
    End Sub

    Private Sub PrintParents(id As Integer, partners As List(Of Integer), prefix As String, isLast As Boolean, isRoot As Boolean)
        For Each partnerId In partners
            Dim partner = GetPersonById(partnerId)
            If partner IsNot Nothing Then
                Console.WriteLine($"{prefix}💑 With: {partner.Name} (ID: {partner.Id})")
                Dim children As List(Of Integer) = Nothing
                If partner.Children.TryGetValue(id, children) AndAlso children.Count > 0 Then
                    PrintChild(children, prefix, isLast, isRoot)
                Else
                    Console.WriteLine($"{prefix}└── 🚫 Without children")
                End If
            End If
        Next
    End Sub

    Private Sub PrintFamily(id As Integer, Optional prefix As String = "", Optional isLast As Boolean = False, Optional isRoot As Boolean = True)
        Dim person = GetPersonById(id)
        If person Is Nothing Then Return

        Console.WriteLine($"{prefix}🙂 {person.Name} (ID: {person.Id})")

        If person.Partners.Count > 0 Then
            If Not isRoot Then
                prefix = prefix.Substring(0, Math.Max(0, prefix.Length - 4)) & If(isLast, "    ", "│   ")
            End If

            PrintParents(id, person.Partners, prefix, isLast, isRoot)
            If Not isLast Then
                Console.WriteLine(prefix)
            End If
        End If
    End Sub

    Public Sub PrintTree()
        Dim result = FilteredGrandparents()
        Dim grandparents = result.Grandparents
        Dim noPartner = result.NoPartner

        If grandparents.Count = 0 AndAlso noPartner.Count = 0 Then
            Console.WriteLine("⚠️ No users are registered.")
            Return
        End If

        If noPartner.Count > 0 Then
            Console.WriteLine("__________")
            Console.WriteLine("Parents unknown, without descendants and without a partner:")
            For Each p In noPartner
                Console.WriteLine($"😐 {p.Name} (ID: {p.Id})")
            Next
        End If

        Console.WriteLine()
        For i As Integer = 0 To grandparents.Count - 1
            Console.WriteLine("__________")
            Console.WriteLine($"Family #{i + 1}")
            PrintFamily(grandparents(i).Id)
        Next
    End Sub
End Class

'___________________________________________________
Public Class Program
    Inherits Tree

    Private Const MENU As String = "
---------------------------------------------
| 1. Add person     | 4. Edit children      |  
| 2. Remove person  | 5. Print tree         |
| 3. Edit partners  | 6. Exit               |
---------------------------------------------"

    Public Sub Run()
        While True
            Console.WriteLine(MENU)
            Dim option_ As Integer = Input.GetInt(vbLf & "Option: ")
            Select Case option_
                Case 1
                    AddPerson()
                Case 2
                    RemovePerson()
                Case 3
                    EditPartners()
                Case 4
                    EditChildren()
                Case 5
                    PrintTree()
                Case 6
                    Console.WriteLine("Bye")
                    Return
                Case Else
                    Console.WriteLine("❌ Invalid option.")
            End Select
        End While
    End Sub

    Public Shared Sub Main()
        Console.OutputEncoding = Encoding.UTF8
        Dim program As New Program()
        program.Run()
    End Sub
End Class
