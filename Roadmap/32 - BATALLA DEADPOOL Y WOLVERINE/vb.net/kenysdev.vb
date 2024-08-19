' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------------
'* BATALLA DEADPOOL Y WOLVERINE
'-----------------------------------------------------
'* EJERCICIO
' * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
' * Crea un programa que simule la pelea y determine un ganador.
' * El programa simula un combate por turnos, donde cada protagonista posee unos
' * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
' * de regeneración y evasión de ataques.
' * Requisitos:
' * 1. El usuario debe determinar la vida inicial de cada protagonista.
' * 2. Cada personaje puede impartir un daño aleatorio:
' *    - Deadpool Entre 10 y 100.
' *    - Wolverine: Entre 10 y 120.
' * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
' * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
' * 4. Cada personaje puede evitar el ataque contrario:
' *    - Deadpool 25% de posibilidades.
' *    - Wolverine: 20% de posibilidades.
' * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
' * Acciones:
' * 1. Simula una batalla.
' * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
' * 3. Muestra qué pasa en cada turno.
' * 4. Muestra la vida en cada turno.
' * 5. Muestra el resultado final.
' ____________________________________________________
'' NOTA: Estoy intentando practicar los principios SOLID. XD 😂 

Imports System.Text

' ---------------------------------------
' INYECCIÓN DE DEPENDENCIAS
' ---------------------------------------
''' <summary>Definirá las interfaces con valores predeterminados.</summary>
Public Class Features
    Implements IFeatures

    Public Property GlobalConfig As IGlobalConfig = New DefaultConfig() Implements IFeatures.GlobalConfig
    Public Property Input As IInput = New ConsoleInput() Implements IFeatures.Input
    Public Property CharacterSetup As ICharacterSetup = New CharacterSetup() Implements IFeatures.CharacterSetup
    Public Property Strategy As IBattleStrategy = New DefaultBattleStrategy() Implements IFeatures.Strategy
    Public Property Player1 As ICharacter = New DefaultCharacter() Implements IFeatures.Player1
    Public Property Player2 As ICharacter = New DefaultCharacter() Implements IFeatures.Player2
End Class

''' <summary>
''' Recibimos instancias de 'Features' con las características del programa que dependen de las interfaces.
''' </summary>
Public Class Program
    Private ReadOnly _Ft As IFeatures
    Private ReadOnly _Simulation As Simulation

    Public Sub New(features As IFeatures, simulation As Simulation)
        Me._Ft = features
        Me._Simulation = simulation
    End Sub

    Public Shared Sub Main()
        Console.OutputEncoding = Encoding.UTF8

        Dim features As IFeatures = New Features()
        Dim simulation As New Simulation(features)
        Dim program As New Program(features, simulation)
        program.Run()
    End Sub

    Public Sub Run()
        Console.WriteLine(_Ft.GlobalConfig.Menu)
        While True
            Dim option_ As Integer = _Ft.Input.GetInt(vbCrLf & "Opción: ")
            Select Case option_
                Case 1
                    _Simulation.Start()

                Case 2
                    Console.WriteLine("Adios")
                    Return
                Case Else
                    Console.WriteLine("Seleccionar de '1 o 2'")
            End Select
        End While
    End Sub
End Class

Public Class Simulation
    Private ReadOnly Ft As IFeatures

    Public Sub New(features As IFeatures)
        Me.Ft = features
    End Sub

    Public Sub ShowHp()
        Console.WriteLine("____________________________")
        Console.WriteLine($"|{Ft.Player1.Name}: ❤️ {Ft.Player1.Hp}| |{Ft.Player2.Name}: ❤️ {Ft.Player2.Hp}|")
    End Sub

    ''' <summary>Llevará a cabo el turno de la batalla.</summary>
    Private Sub InitBattle()
        Dim turn As Integer = 1
        While True
            Console.WriteLine(vbCrLf & "----------------------------" & vbCrLf & $"Turno #{turn}" & vbCrLf & "----------------------------")

            ' Ataque de personaje #1 hacia #2
            ShowHp()
            If Not Ft.Strategy.Execute(Ft.Player1, Ft.Player2) Then
                Exit While
            End If

            ' Ataque de personaje #2 hacia #1
            ShowHp()
            If Not Ft.Strategy.Execute(Ft.Player2, Ft.Player1) Then
                Exit While
            End If

            turn += 1
            Threading.Thread.Sleep(Ft.GlobalConfig.TurnInterval * 1000)
        End While

        ShowHp()
    End Sub

    Public Sub Start()
        Console.WriteLine("Personajes disponibles:")
        Dim characters As List(Of String) = Ft.GlobalConfig.Characters.Keys.ToList()
        For i As Integer = 0 To characters.Count - 1
            Console.WriteLine($"{i}. {characters(i)}")
        Next

        ' Configurar Personajes
        Ft.CharacterSetup.Add(Ft, vbCrLf & "'Primer' personaje: ", Ft.Player1)
        Ft.CharacterSetup.Add(Ft, "'Segundo' personaje: ", Ft.Player2)

        InitBattle()

        Ft.Player1.Name = String.Empty ' Restablecer para iniciar nueva simulación.
        Console.WriteLine(Ft.GlobalConfig.Menu)
    End Sub
End Class

'' ---------------------------------------
'' INTERFACES
'' ---------------------------------------
Public Interface IFeatures
    ''' <summary>Configuración global del juego.</summary>
    Property GlobalConfig As IGlobalConfig
    ''' <summary>Interfaz para la entrada del usuario.</summary>
    Property Input As IInput
    ''' <summary>Interfaz para la configuración de los personajes.</summary>
    Property CharacterSetup As ICharacterSetup
    ''' <summary>Estrategia de batalla.</summary>
    Property Strategy As IBattleStrategy
    Property Player1 As ICharacter
    Property Player2 As ICharacter
End Interface

''' <summary>Contrato para la configuración global.</summary>
Public Interface IGlobalConfig
    ReadOnly Property TurnInterval As Integer
    ReadOnly Property MinimumHp As Integer
    ''' <summary>
    ''' Diccionario de personajes, con sus habilidades, Daño posible, Probabilidad de defensa.
    ''' Fácil de adaptar a un Json de personajes.
    ''' {"Character": {"attacks": ["Attack1", "Attack2"], "damage_range": (10, 100), "defense_chance": 0.25}}
    ''' </summary>
    ReadOnly Property Characters As IDictionary(Of String, TCharacterConfig)
    ReadOnly Property Menu As String
End Interface

''' <summary>Clase que define la configuración del personaje</summary>
Public Class TCharacterConfig
    Public Property Attacks As List(Of String)
    Public Property DamageRange As (Min As Integer, Max As Integer)
    Public Property DefenseChance As Double
End Class

Public Interface IInput
    ''' <returns>Un dato entero que no debe ser vacío.</returns>
    Function GetInt(msg As String) As Integer
End Interface

''' <summary>Contrato para los datos y métodos de un personaje.</summary>
Public Interface ICharacter
    Property Name As String
    Property Hp As Integer
    Property CanAttack As Boolean
    Property Attacks As List(Of String)
    Property DamageRange As (MinDamage As Integer, MaxDamage As Integer)
    Property DefenseChance As Double

    Sub Add(name As String, hp As Integer, attributes As TCharacterConfig)

    ''' <summary>Verifica si puede atacar, realiza un ataque y devuelve el daño infligido.</summary>
    Function Attack() As Integer

    ''' <summary>Determina si el personaje puede defenderse y lo retorna.</summary>
    Function Defend() As Boolean
End Interface

''' <summary>Contrato para agrega datos de los personajes.</summary>
Public Interface ICharacterSetup
    '''<summary>Agrega datos de los personajes.</summary>
    ''' <param name="msg">Mensaje a mostrar al usuario.</param>
    ''' <param name="player">La instancia del personaje a configurar.</param>
    Sub Add(Ft As IFeatures, msg As String, player As ICharacter)
End Interface

Public Interface IBattleStrategy
    ''' <summary>Ejecuta la estrategia de batalla entre el atacante y el defensor.</summary>
    ''' <returns>Retorna verdadero si el defensor sigue en pie, falso si el atacante gana la batalla.</returns>
    Function Execute(attacker As ICharacter, defender As ICharacter) As Boolean
End Interface

'' ---------------------------------------
'' IMPLEMENTACIÓN DE INTERFACES
'' ---------------------------------------
''' <summary>Constantes globales.</summary>
Public Class DefaultConfig
    Implements IGlobalConfig

    Public ReadOnly Property TurnInterval As Integer Implements IGlobalConfig.TurnInterval
        Get
            Return 1
        End Get
    End Property

    Public ReadOnly Property MinimumHp As Integer Implements IGlobalConfig.MinimumHp
        Get
            Return 200
        End Get
    End Property

    ' Fácil de adaptar a un Json de personajes.
    Public ReadOnly Property Characters As IDictionary(Of String, TCharacterConfig) Implements IGlobalConfig.Characters
        Get
            Return New Dictionary(Of String, TCharacterConfig) From {
                {"Deadpool", New TCharacterConfig With {
                    .Attacks = New List(Of String) From {"Con arma", "Cuerpo a cuerpo", "Ataque imprudente"},
                    .DamageRange = (10, 100),
                    .DefenseChance = 0.25
                }},
                {"Wolverine", New TCharacterConfig With {
                    .Attacks = New List(Of String) From {"Con garras de adamantium", "Con arma", "Cuerpo a cuerpo"},
                    .DamageRange = (10, 120),
                    .DefenseChance = 0.2
                }}
            }   'Puedes añadir más personajes
        End Get
    End Property

    Public ReadOnly Property Menu As String Implements IGlobalConfig.Menu
        Get
            Return vbCrLf & "SIMULADOR DE BATALLAS:" & vbCrLf &
                   "------------------------------------------" & vbCrLf &
                   "| 1. Simular una batalla |    2. Salir    |" & vbCrLf &
                   "------------------------------------------"
        End Get
    End Property
End Class

' ____________________________________________________
'''<summary>Solicitud de entrada.</summary>
Public Class ConsoleInput
    Implements IInput

    Public Function GetInt(msg As String) As Integer Implements IInput.GetInt
        While True
            Console.Write(msg)
            Dim input As String = Console.ReadLine()

            If String.IsNullOrWhiteSpace(input) Then
                Console.WriteLine("La entrada no puede estar vacía.")
                Continue While
            End If

            Dim intValue As Integer
            If Integer.TryParse(input, intValue) Then
                Return intValue
            Else
                Console.WriteLine("Por favor, ingresa un número entero válido.")
            End If
        End While
        Return 0
    End Function
End Class

' ____________________________________________________
'''<summary>Datos y metodos de un personaje que participara en la batalla.</summary>
Public Class DefaultCharacter
    Implements ICharacter

    Public Property Name As String = "" Implements ICharacter.Name
    Public Property Hp As Integer = 0 Implements ICharacter.Hp
    Public Property CanAttack As Boolean = True Implements ICharacter.CanAttack
    Public Property Attacks As List(Of String) = New List(Of String)() Implements ICharacter.Attacks
    Public Property DamageRange As (MinDamage As Integer, MaxDamage As Integer) = (0, 0) Implements ICharacter.DamageRange
    Public Property DefenseChance As Double = 0.0 Implements ICharacter.DefenseChance

    Public Sub Add(name As String, hp As Integer, attributes As TCharacterConfig) Implements ICharacter.Add
        Me.Name = name
        Me.Hp = hp
        Me.Attacks = attributes.Attacks
        Me.DamageRange = attributes.DamageRange
        Me.DefenseChance = attributes.DefenseChance
    End Sub

    Public Function Attack() As Integer Implements ICharacter.Attack
        If CanAttack Then
            Dim random As New Random()
            Dim damage As Integer = random.Next(DamageRange.MinDamage, DamageRange.MaxDamage + 1)
            Dim selectedAttack As String = Attacks(random.Next(Attacks.Count))
            Console.WriteLine($"|'{Name}' ataca '{selectedAttack}' causando un: '-{damage}' 👊|")
            Return damage
        Else
            Console.WriteLine($"|'{Name}' se está regenerando y no puede atacar. 😴|")
            Return 0
        End If
    End Function

    Public Function Defend() As Boolean Implements ICharacter.Defend
        Dim random As New Random()
        Dim defended As Boolean = random.NextDouble() < DefenseChance
        Console.WriteLine(If(defended,
                            $"|'{Name}' logró defenderse. 🛡️|",
                            $"|'{Name}' no pudo bloquear el ataque. 🤕|"))
        Return defended
    End Function
End Class

' ____________________________________________________
'''<summary>Agrega datos de los personajes.</summary>
Public Class CharacterSetup
    Implements ICharacterSetup

    Public Sub Add(Ft As IFeatures, msg As String, player As ICharacter) Implements ICharacterSetup.Add
        While True
            Dim index As Integer = Ft.Input.GetInt(msg)
            Dim keys As List(Of String) = Ft.GlobalConfig.Characters.Keys.ToList()
            Dim name As String = keys(index)
            Dim hp As Integer
            Dim attributes As TCharacterConfig = Ft.GlobalConfig.Characters(name)

            If index < 0 OrElse index >= keys.Count Then
                Console.WriteLine("Número de personaje incorrecto.")
                Continue While ' Volver a solicitar
            End If

            If name = Ft.Player1.Name Then
                Console.WriteLine("El personaje ya fue utilizado.")
                Continue While
            End If

            While True
                hp = Ft.Input.GetInt($"Establecer una vida >= que '{Ft.GlobalConfig.MinimumHp}': ")
                If hp < Ft.GlobalConfig.MinimumHp Then
                    Console.WriteLine($"La vida debe ser mayor o igual que '{Ft.GlobalConfig.MinimumHp}'.")
                Else
                    Exit While
                End If
            End While

            player.Add(name, hp, attributes)
            Exit While
        End While
    End Sub
End Class

' ____________________________________________________
'''<summary>Estrategia 'standard'.</summary>
Public Class DefaultBattleStrategy
    Implements IBattleStrategy

    Public Function Execute(attacker As ICharacter, defender As ICharacter) As Boolean Implements IBattleStrategy.Execute
        Dim damage As Integer = attacker.Attack()

        If damage = attacker.DamageRange.MaxDamage Then
            Console.WriteLine($"|'{defender.Name}' 🚨Recibió un ataque crítico y no podrá atacar.🚨|")
            defender.CanAttack = False
        End If

        If attacker.CanAttack Then
            If Not defender.Defend() Then
                defender.Hp -= damage
            End If
        Else
            attacker.CanAttack = True
        End If

        If defender.Hp <= 0 Then
            Console.WriteLine(vbCrLf & "____________________________")
            Console.WriteLine($"|'{attacker.Name}' 🏆Gana la batalla. 🏆|")
            Return False
        End If

        Return True
    End Function
End Class

' _________________
'' NOTA: Estoy intentando practicar los principios SOLID. XD 😂

