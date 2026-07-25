' #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot

Imports System
Imports System.Collections.Generic
Imports System.Linq

Module SisaRoot

    Class Participant
        Property Name As String
        Property Country As String
        Sub New(n As String, c As String) : Name=n : Country=c : End Sub
    End Class

    Class OlympicEvent
        Property Name As String
        Property Participants As New List(Of Participant)
        Sub New(n As String) : Name=n : End Sub
    End Class

    Class Medals
        Property Country As String
        Property Gold As Integer = 0
        Property Silver As Integer = 0
        Property Bronze As Integer = 0
        ReadOnly Property Total As Integer
            Get : Return Gold+Silver+Bronze : End Get
        End Property
        Sub New(c As String) : Country=c : End Sub
    End Class

    Dim events As New List(Of OlympicEvent)
    Dim medalTable As New Dictionary(Of String, Medals)
    Dim rng As New Random()

    Sub AddMedal(c As String, t As String)
        If Not medalTable.ContainsKey(c) Then medalTable(c) = New Medals(c)
        Select Case t
            Case "gold"   : medalTable(c).Gold   += 1
            Case "silver" : medalTable(c).Silver += 1
            Case Else     : medalTable(c).Bronze += 1
        End Select
    End Sub

    Sub RegisterEvent()
        Console.Write("Nombre del evento: ")
        Dim name As String = Console.ReadLine()?.Trim()
        If String.IsNullOrEmpty(name) Then Console.WriteLine("Invalido.") : Return
        If events.Any(Function(e) String.Equals(e.Name,name,StringComparison.OrdinalIgnoreCase)) Then Console.WriteLine("Ya existe.") : Return
        events.Add(New OlympicEvent(name))
        Console.WriteLine($"Evento '{name}' registrado.")
    End Sub

    Sub RegisterParticipant()
        If events.Count=0 Then Console.WriteLine("No hay eventos.") : Return
        For i=0 To events.Count-1 : Console.WriteLine($"  {i+1}. {events(i).Name}") : Next
        Console.Write("Número: ")
        Dim idx As Integer
        If Not Integer.TryParse(Console.ReadLine()?.Trim(),idx) OrElse idx<1 OrElse idx>events.Count Then Console.WriteLine("Invalido.") : Return
        Dim ev = events(idx-1)
        Console.Write("Nombre: ") : Dim pname = Console.ReadLine()?.Trim()
        Console.Write("País: ")   : Dim country = Console.ReadLine()?.Trim()
        ev.Participants.Add(New Participant(pname,country))
        Console.WriteLine($"'{pname} ({country})' añadido a '{ev.Name}'.")
    End Sub

    Sub SimulateEvents()
        If events.Count=0 Then Console.WriteLine("No hay eventos.") : Return
        For Each ev In events
            Console.WriteLine($"{Environment.NewLine}=== Simulando: {ev.Name} ===")
            If ev.Participants.Count<3 Then Console.WriteLine("  Necesita >=3. Saltando.") : Continue For
            Dim s = ev.Participants.OrderBy(Function(_) rng.Next()).ToList()
            Console.WriteLine($"  Oro:    {s(0).Name} ({s(0).Country})")
            Console.WriteLine($"  Plata:  {s(1).Name} ({s(1).Country})")
            Console.WriteLine($"  Bronce: {s(2).Name} ({s(2).Country})")
            AddMedal(s(0).Country,"gold") : AddMedal(s(1).Country,"silver") : AddMedal(s(2).Country,"bronze")
        Next
    End Sub

    Sub ShowReport()
        Console.WriteLine(Environment.NewLine & "== INFORME FINAL ==")
        If medalTable.Count=0 Then Console.WriteLine("Sin resultados.") : Return
        Dim ranking = medalTable.Values.OrderByDescending(Function(c) c.Gold).ThenByDescending(Function(c) c.Silver).ThenByDescending(Function(c) c.Bronze).ToList()
        For i=0 To ranking.Count-1
            Dim c = ranking(i)
            Console.WriteLine($"{i+1}. {c.Country.PadRight(20)} Oro:{c.Gold} Plata:{c.Silver} Bronce:{c.Bronze} Total:{c.Total}")
        Next
    End Sub

    Sub Main()
        While True
            Console.WriteLine(Environment.NewLine & "====== SIMULADOR JJOO ======")
            Console.WriteLine("1. Registrar evento" & Environment.NewLine & "2. Registrar participante" & Environment.NewLine & "3. Simular" & Environment.NewLine & "4. Informe" & Environment.NewLine & "5. Salir")
            Console.Write("Opción: ")
            Select Case Console.ReadLine()?.Trim()
                Case "1" : RegisterEvent()
                Case "2" : RegisterParticipant()
                Case "3" : SimulateEvents()
                Case "4" : ShowReport()
                Case "5" : Console.WriteLine("Hasta luego!") : Return
                Case Else : Console.WriteLine("Invalido.")
            End Select
        End While
    End Sub

End Module
