' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------------
'* SIMULADOR JUEGOS OLÍMPICOS
'-----------------------------------------------------

'* EJERCICIO
'* ¡Los JJOO de París 2024 han comenzado!
'* Crea un programa que simule la celebración de los juegos.
'* El programa debe permitir al usuario registrar eventos y participantes,
'* realizar la simulación de los eventos asignando posiciones de manera aleatoria
'* y generar un informe final. Todo ello por terminal.
' * Requisitos:
' * 1. Registrar eventos deportivos.
' * 2. Registrar participantes por nombre y país.
' * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
' * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
' * 5. Mostrar los ganadores por cada evento.
' * 6. Mostrar el ranking de países según el número de medallas.
' * Acciones:
' * 1. Registro de eventos.
' * 2. Registro de participantes.
' * 3. Simulación de eventos.
' * 4. Creación de informes.
' * 5. Salir del programa.

' _________________
'' NOTA: Esto es un intento de aplicar los principios SOLID.

Imports System.Text

'''<summary>Contrato sobre las constantes globales.</summary>
Public Interface IConstants
    Function GetMenu() As String
    Function GetMedals() As String()
End Interface

' ____________________________________________________
'' CONTRATOS para la capa de datos.
''' <summary>
''' Contrato sobre los métodos requeridos para cada tabla creada.
''' </summary>
Public Interface IDataTable(Of T)
    Sub Add(item As T)

    ''' <returns>El número de elementos.</returns>
    Function Count() As Integer

    ''' <returns>Una lista de elementos.</returns>
    Function GetList() As List(Of T)
End Interface

''' <summary>
''' Define un contrato para implementar diferentes formas de almacenamiento de datos.
''' </summary>
Public Interface IData
    ReadOnly Property EventsTable As IDataTable(Of String)
    ReadOnly Property ParticipantsTable As IDataTable(Of (Name As String, Country As String, EventId As Integer))
    ReadOnly Property SimulationTable As IDataTable(Of SimulationType)
End Interface

''' <summary>
''' Define una estructura para representar los datos en una simulación.
''' </summary>
Public Structure SimulationType
    Public Property Events As List(Of (EventName As String, Results As List(Of (Name As String, Country As String, EventId As Integer, Score As Integer, Medal As String))))

    Public Sub New(events As List(Of (EventName As String, Results As List(Of (Name As String, Country As String, EventId As Integer, Score As Integer, Medal As String)))))
        Me.Events = events
    End Sub
End Structure

''' <summary>
''' Define el contrato para la entrada de datos del usuario.
''' </summary>
Public Interface IInput
    ''' <returns>Una cadena no vacía.</returns>
    Function GetStr(msg As String) As String
    ''' <returns>Un número entero.</returns>
    Function GetInt(msg As String) As Integer
End Interface

' ____________________________________________________
' CONTRATOS sobre la comunicación entre la interacción del usuario y la capa de datos.
Public Interface IEvents
    Sub Add()
End Interface

Public Interface IParticipants
    Sub Add()
End Interface

Public Interface ISimulations
    Sub Start()
End Interface

Public Interface IReports
    Sub Generate()
End Interface

' ____________________________________________________
' IMPLEMENTAR CONTRATOS

' ____________________________________________________
Public Class DefaultConstants
    Implements IConstants

    Private Const Menu As String = "
SIMULADOR JUEGOS OLÍMPICOS:
--------------------------------------------------
| 1. Registrar evento        | 4. Crear informes |  
| 2. Registrar participante  | 5. Salir          |
| 3. Simulación de eventos   |                   |
--------------------------------------------------
"

    Private Shared ReadOnly Medals As String() = {"🥇 Oro", "🥈 Plata", "🥉 Bronce"}

    Public Function GetMenu() As String Implements IConstants.GetMenu
        Return Menu
    End Function

    Public Function GetMedals() As String() Implements IConstants.GetMedals
        Return Medals
    End Function
End Class

''' <summary>
''' Implementación de <see cref="IDataTable(Of String)"/> para la tabla de eventos.
''' </summary>
Public Class EventsTable
    Implements IDataTable(Of String)

    Private ReadOnly dt As New List(Of String)()

    Public Sub Add(sport As String) Implements IDataTable(Of String).Add
        dt.Add(sport)
    End Sub

    Public Function Count() As Integer Implements IDataTable(Of String).Count
        Return dt.Count
    End Function

    Public Function GetList() As List(Of String) Implements IDataTable(Of String).GetList
        Return New List(Of String)(dt)
    End Function
End Class

''' <summary>
''' Implementación de <see cref="IDataTable(Of (String, String))"/> para la tabla de participantes.
''' </summary>
Public Class ParticipantsTable
    Implements IDataTable(Of (String, String, Integer))

    Private ReadOnly dt As New List(Of (String, String, Integer))()

    Public Sub Add(participant As (String, String, Integer)) Implements IDataTable(Of (String, String, Integer)).Add
        dt.Add(participant)
    End Sub

    Public Function Count() As Integer Implements IDataTable(Of (String, String, Integer)).Count
        Return dt.Count
    End Function

    Public Function GetList() As List(Of (String, String, Integer)) Implements IDataTable(Of (String, String, Integer)).GetList
        Return New List(Of (String, String, Integer))(dt)
    End Function
End Class

''' <summary>
''' Implementación de <see cref="IDataTable(Of Types.SimulationResult)"/> para la tabla de simulaciones.
''' </summary>
Public Class SimulationTable
    Implements IDataTable(Of SimulationType)

    Private ReadOnly dt As New List(Of SimulationType)()

    Public Sub Add(item As SimulationType) Implements IDataTable(Of SimulationType).Add
        dt.Add(item)
    End Sub

    Public Function Count() As Integer Implements IDataTable(Of SimulationType).Count
        Return dt.Count
    End Function

    Public Function GetList() As List(Of SimulationType) Implements IDataTable(Of SimulationType).GetList
        Return dt
    End Function
End Class


' ____________________________________________________
''' <summary>
''' Datos en memoria aplicando el patrón Singleton.
''' </summary>
Public Class DataInMemory
    Implements IData
    Private Shared _instance As DataInMemory

    ''' <summary>
    ''' Obtiene la instancia única de <see cref="DataInMemory"/>.
    ''' </summary>
    Public Shared ReadOnly Property Instance As DataInMemory
        Get
            If _instance Is Nothing Then
                _instance = New DataInMemory()
            End If
            Return _instance
        End Get
    End Property

    Public ReadOnly Property EventsTable As IDataTable(Of String) Implements IData.EventsTable
    Public ReadOnly Property ParticipantsTable As IDataTable(Of (String, String, Integer)) Implements IData.ParticipantsTable
    Public ReadOnly Property SimulationTable As IDataTable(Of SimulationType) Implements IData.SimulationTable

    Private Sub New()
        EventsTable = New EventsTable()
        ParticipantsTable = New ParticipantsTable()
        SimulationTable = New SimulationTable()
    End Sub
End Class

' ____________________________________________________
''' <summary>
''' Muestra un mensaje al usuario y devuelve su entrada.
''' </summary>
Public Class Input
    Implements IInput

    Public Function GetStr(msg As String) As String Implements IInput.GetStr
        While True
            Console.Write(msg)
            Dim txt As String = Console.ReadLine()
            If Not String.IsNullOrEmpty(txt) Then
                Return txt
            End If
        End While
        Return Nothing
    End Function

    Public Function GetInt(msg As String) As Integer Implements IInput.GetInt
        While True
            Console.Write(msg)
            Dim txt As String = Console.ReadLine()
            Dim input As Integer
            If Integer.TryParse(txt, input) Then
                Return input
            Else
                Console.WriteLine("Ingresa un número entero.")
            End If
        End While
        Return Nothing
    End Function
End Class

' ____________________________________________________
''' <summary>
''' 1. Registrar eventos deportivos.
''' </summary>
Public Class Events
    Implements IEvents

    Private ReadOnly _data As IData
    Private ReadOnly _input As IInput

    Public Sub New(data As IData, input As IInput)
        _data = data
        _input = input
    End Sub

    Public Sub Add() Implements IEvents.Add
        Console.WriteLine("AGREGAR EVENTO DEPORTIVO:")
        Dim sport As String = _input.GetStr("Deporte: ")
        _data.EventsTable.Add(sport)
        Console.WriteLine($"{sport} fue agregado")
        'Console.WriteLine(_constants.GetMenu())
    End Sub
End Class

' ____________________________________________________
''' <summary>
''' 2. Registrar participantes por nombre y país.
''' </summary>
Public Class Participants
    Implements IParticipants

    Private ReadOnly _constants As IConstants
    Private ReadOnly _data As IData
    Private ReadOnly _input As IInput

    Public Sub New(constants As IConstants, data As IData, input As IInput)
        _constants = constants
        _data = data
        _input = input
    End Sub

    Private Function GetEventId() As Integer
        Console.WriteLine("Seleccionar el evento donde participará:")
        Dim events = _data.EventsTable.GetList()

        For i As Integer = 0 To events.Count - 1
            Console.WriteLine($"{i}. {events(i)}")
        Next

        While True
            Dim index As Integer = _input.GetInt("Id de evento: ")
            If index < 0 OrElse index >= events.Count Then
                Console.WriteLine(vbCrLf & "Id no encontrada.")
            Else
                Return index
            End If
        End While
        Return 0
    End Function

    Public Sub Add() Implements IParticipants.Add
        Console.WriteLine("AGREGAR PARTICIPANTE:")
        Dim events = _data.EventsTable.GetList()
        If Not events.Count > 0 Then
            Console.WriteLine("No existe evento en cuál participar.")
            Return
        End If

        Dim eventId As Integer = GetEventId()
        Dim name As String = _input.GetStr("Nombre: ")
        Dim country As String = _input.GetStr("país: ")
        _data.ParticipantsTable.Add((name, country, eventId))
        Console.WriteLine($"{name} fue agregado")
        Console.WriteLine(_constants.GetMenu())
    End Sub
End Class

' ____________________________________________________
''' <summary>
''' 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
''' 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
''' </summary>
Public Class Simulation
    Implements ISimulations

    Private ReadOnly constants As IConstants
    Private Shared ReadOnly _random As New Random()
    Private ReadOnly data As IData

    Public Sub New(constants As IConstants, data As IData)
        Me.constants = constants
        Me.data = data
    End Sub

    Private Function QualifyParticipants(eventId As Integer) As List(Of List(Of Object))
        Dim participants = data.ParticipantsTable.GetList()

        ' Seleccionar solo los participantes que tienen el ID del evento.
        Dim ParticipantsOfEvent = participants.Where(Function(p) p.EventId = eventId).ToList()
        Dim qualifiedParticipants = ParticipantsOfEvent.Select(Function(p)
                                                                   Dim list As New List(Of Object) From {
                                                                p.Name,
                                                                p.Country,
                                                                p.EventId,
                                                                _random.Next(1, 101)
                                                            }
                                                                   Return list
                                                               End Function).ToList()

        qualifiedParticipants = qualifiedParticipants.OrderByDescending(Function(p) CInt(p(3))).ToList()

        Dim top3Participants = qualifiedParticipants.Take(3).ToList()

        Dim medals = constants.GetMedals()
        For i As Integer = 0 To top3Participants.Count - 1
            top3Participants(i).Add(medals(i))
        Next

        Return top3Participants
    End Function

    Private Sub AddResultEvents()
        Dim events = data.EventsTable.GetList()
        Dim allEvents As New List(Of (EventName As String, Results As List(Of (Name As String, Country As String, EventId As Integer, Score As Integer, Medal As String))))

        For id As Integer = 0 To events.Count - 1
            Dim qualifiedParticipants = QualifyParticipants(id)
            Dim eventResult = qualifiedParticipants.Select(Function(p)
                                                               Return (
                                                          Name:=If(p(0)?.ToString(), String.Empty),
                                                          Country:=If(p(1)?.ToString(), String.Empty),
                                                          EventId:=CInt(p(2)),
                                                          Score:=CInt(p(3)),
                                                          Medal:=If(p(4)?.ToString(), String.Empty)
                                                      )
                                                           End Function).ToList()

            allEvents.Add((EventName:=events(id), Results:=eventResult))
        Next

        ' Agregar una nueva simulación con todos los eventos
        Dim simulation As New SimulationType(allEvents)
        data.SimulationTable.Add(simulation)
    End Sub

    Public Sub Start() Implements ISimulations.Start
        If data.EventsTable.Count() >= 1 AndAlso data.ParticipantsTable.Count() >= 3 Then
            AddResultEvents()
            Dim totalSimulation = data.SimulationTable.Count()
            Console.WriteLine($"Simulación '#{totalSimulation}' creada.")
            Console.WriteLine("Puedes ver el resultado con opción: '4. Crear informes.'")
            'Console.WriteLine(GlobalConstants.Menu)
        Else
            Console.WriteLine("Debe haber al menos un evento y al menos 'tres' participantes.")
        End If
    End Sub

End Class

' ____________________________________________________
''' <summary>
''' 5. Mostrar los ganadores por cada evento.
''' 6. Mostrar el ranking de países según el número de medallas.
''' </summary>
Public Class Reports
    Implements IReports

    Private ReadOnly constants As IConstants
    Private ReadOnly rankingCountries As New Dictionary(Of String, (Medals As Integer, CurrentScore As Integer))()
    Private ReadOnly data As IData
    Public Sub New(constants As IConstants, data As IData)
        Me.constants = constants
        Me.data = data
    End Sub

    Private Sub GenerateTopCountries()
        Dim sortedRank = rankingCountries.OrderByDescending(Function(item) item.Value)

        Dim i As Integer = 1
        For Each entry In sortedRank
            Dim name As String = entry.Key
            Dim total As (Medals As Integer, CurrentScore As Integer) = entry.Value
            Console.WriteLine($"'{i}' - {name} -> Medallas: 🏅 {total.Medals} | Puntaje: 📊 {total.CurrentScore}")
            i += 1
        Next
    End Sub

    Private Sub IterateParticipants(participants As List(Of (Name As String, Country As String, EventId As Integer, Score As Integer, Medal As String)))
        For Each entry In participants.Select(Function(p, index) New With {
            Key .Index = index + 1,
            p.Name,
            p.Country,
            p.EventId,
            p.Score,
            p.Medal
    })
            Console.WriteLine($"'{entry.Index}' - {entry.Name} - {entry.Country} -> Score: {entry.Score}, Medal: {entry.Medal}")

            ' Registrar para generar ranking de países por número de medallas
            Dim value As (Medals As Integer, CurrentScore As Integer)
            If rankingCountries.TryGetValue(entry.Country, value) Then
                Dim medals As Integer = value.Medals
                Dim currentScore As Integer = value.CurrentScore
                rankingCountries(entry.Country) = (medals + 1, currentScore + entry.Score)
            Else
                rankingCountries(entry.Country) = (1, entry.Score)
            End If
        Next
    End Sub

    Private Sub IterateEvents(simulation As SimulationType)
        For Each eventResult In simulation.Events
            Console.WriteLine(vbCrLf + $"Event: {eventResult.EventName}:")
            If eventResult.Results.Count < 3 Then
                Console.WriteLine("Evento cancelado por falta de participantes.")
                Continue For
            End If

            IterateParticipants(eventResult.Results)
        Next
    End Sub

    Public Sub Generate() Implements IReports.Generate
        Dim simulations = data.SimulationTable.GetList()

        If simulations.Count = 0 Then
            Console.WriteLine("Aún no hay simulaciones creadas.")
            Return
        End If

        Dim i As Integer = 1
        For Each Simulation In simulations
            Console.WriteLine(vbCrLf + "_______________")
            Console.WriteLine($"Simulation {i}")

            ' Iterar sobre los eventos en cada simulación
            IterateEvents(Simulation)

            Console.WriteLine(vbCrLf + "Ranking de países, según el número de medallas y puntaje:")
            GenerateTopCountries()
            rankingCountries.Clear()

            i += 1
        Next

        Console.WriteLine(constants.GetMenu())
    End Sub
End Class

' ____________________________________________________
Public Class Features
    Public Property Constants As IConstants
    Public Property Data As IData
    Public Property Input As IInput
    Public Property Events As IEvents
    Public Property Participants As IParticipants
    Public Property Simulation As ISimulations
    Public Property Reports As IReports
End Class

' ____________________________________________________
''' <summary>
''' Recibimos instancias con las características del programa que dependen de las interfaces.
''' </summary>
Public Class Program
    Private ReadOnly Ft As Features
    Public Sub New(ft As Features)
        Me.Ft = ft
    End Sub

    Public Sub Run()
        Console.WriteLine(Ft.Constants.GetMenu())
        While True
            Dim option_ As String = Ft.Input.GetStr(vbCrLf & "Opción: ")
            Select Case option_
                Case "1"
                    Ft.Events.Add()
                Case "2"
                    Ft.Participants.Add()
                Case "3"
                    Ft.Simulation.Start()
                Case "4"
                    Ft.Reports.Generate()
                Case "5"
                    Console.WriteLine("Adios")
                    Return
                Case Else
                    Console.WriteLine("Seleccionar de '1 a 5'")
            End Select
        End While
    End Sub

    Public Shared Sub Main()
        Console.OutputEncoding = Encoding.UTF8
        Dim constants As IConstants = New DefaultConstants()
        Dim data As IData = DataInMemory.Instance
        Dim input As IInput = New Input()

        Dim features As New Features With {
            .Constants = constants,
            .Data = data,
            .Input = input,
            .Events = New Events(data, input),
            .Participants = New Participants(constants, data, input),
            .Simulation = New Simulation(constants, data),
            .Reports = New Reports(constants, data)
        }

        Dim program As New Program(features)
        program.Run()
    End Sub
End Class

' _________________
'' NOTA: Esto es un intento de aplicar los principios SOLID.

