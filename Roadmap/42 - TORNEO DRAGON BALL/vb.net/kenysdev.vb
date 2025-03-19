' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 42 TORNEO DRAGON BALL
' ------------------------------------
'* EJERCICIO
' * ¡El último videojuego de Dragon Ball ya está aquí!
' * Se llama Dragon Ball: Sparking! ZERO.
' *
' * Simula un Torneo de Artes Marciales, al más puro estilo
' * de la saga, donde participarán diferentes luchadores, y el
' * sistema decidirá quién es el ganador.
' *
' * Luchadores:
' * - Nombre.
' * - Tres atributos: velocidad, ataque y defensa
' *   (con valores entre 0 a 100 que tú decidirás).
' * - Comienza cada batalla con 100 de salud.
' * Batalla:
' * - En cada batalla se enfrentan 2 luchadores.
' * - El luchador con más velocidad comienza atacando.
' * - El daño se calcula restando el daño de ataque del
' *   atacante menos la defensa del oponente.
' * - El oponente siempre tiene un 20% de posibilidad de
' *   esquivar el ataque.
' * - Si la defensa es mayor que el ataque, recibe un 10%
' *   del daño de ataque.
' * - Después de cada turno y ataque, el oponente pierde salud.
' * - La batalla finaliza cuando un luchador pierde toda su salud.
' * Torneo:
' * - Un torneo sólo es válido con un número de luchadores
' *   potencia de 2.
' * - El torneo debe crear parejas al azar en cada ronda.
' * - Los luchadores se enfrentan en rondas eliminatorias.
' * - El ganador avanza a la siguiente ronda hasta que sólo
' *   quede uno.
' * - Debes mostrar por consola todo lo que sucede en el torneo,
' *   así como el ganador.

Public Class Fighter
    Public ReadOnly Property Name As String
    Public ReadOnly Property Speed As Integer
    Public ReadOnly Property Attack As Integer
    Public ReadOnly Property Defense As Integer
    Public Property Health As Double = 100

    Public Sub New(name As String, speed As Integer, attack As Integer, defense As Integer)
        Me.Name = name
        Me.Speed = speed
        Me.Attack = attack
        Me.Defense = defense
    End Sub

    Public Sub ExecuteAttack(opponent As Fighter)
        Console.WriteLine($"'{Name}' ataca a '{opponent.Name}'")

        Dim damage As Double = If(opponent.Defense >= Attack,
                                 Attack * 0.1, ' 10%
                                 Attack - opponent.Defense)

        If Not ActivateDefense() Then
            opponent.Health -= damage
            Console.WriteLine($"'{opponent.Name}' ha recibido '{damage}' de daño")
            Console.WriteLine($"Salud restante '{opponent.Health}'{Environment.NewLine}")
        Else
            Console.WriteLine($"'{opponent.Name}' ha esquivado el ataque.{Environment.NewLine}")
        End If
    End Sub

    Private Shared Function ActivateDefense() As Boolean
        Return Random.Shared.NextDouble() <= 0.2 ' 20%
    End Function
End Class

'  __________________________________________________________
Public Class Battle
    Private ReadOnly _fighter1 As Fighter
    Private ReadOnly _fighter2 As Fighter

    Public Sub New(fighter1 As Fighter, fighter2 As Fighter)
        _fighter1 = fighter1
        _fighter2 = fighter2
        Console.WriteLine($"__'{_fighter1.Name} VS '{_fighter2.Name}'__{Environment.NewLine}")
    End Sub

    Private Shared Function Combat(fighterA As Fighter, fighterB As Fighter) As Fighter
        While True
            fighterA.ExecuteAttack(fighterB)
            If fighterB.Health <= 0 Then
                Console.WriteLine($"--> '{fighterA.Name}' gana la batalla.__{Environment.NewLine}")
                Return fighterA
            End If

            fighterB.ExecuteAttack(fighterA)
            If fighterA.Health <= 0 Then
                Console.WriteLine($"--> '{fighterB.Name}' gana la batalla.{Environment.NewLine}")
                Return fighterB
            End If
        End While

        Return Nothing
    End Function

    Public Function Start() As Fighter
        Return If(_fighter1.Speed > _fighter2.Speed,
                 Combat(_fighter1, _fighter2),
                 Combat(_fighter2, _fighter1))
    End Function
End Class

'  __________________________________________________________
Public Class FighterStats
    Public Property Speed As Integer
    Public Property Attack As Integer
    Public Property Defense As Integer

    Public Sub New(speed As Integer, attack As Integer, defense As Integer)
        Me.Speed = speed
        Me.Attack = attack
        Me.Defense = defense
    End Sub
End Class

Public Class Tournament
    Private _fighters As Dictionary(Of String, FighterStats)

    Public Sub New(fighters As Dictionary(Of String, FighterStats))
        _fighters = fighters
    End Sub

    Private Function IsPowerOf2() As Boolean
        Return _fighters.Count > 1 AndAlso Math.Log2(_fighters.Count) Mod 1 = 0
    End Function

    Private Function GetRandomPairs() As (Fighter1 As Fighter, Fighter2 As Fighter)
        Dim names = _fighters.Keys.ToList()
        Dim selected = names.OrderBy(Function(x) Random.Shared.Next()).Take(2).ToList()

        Dim stats1 = _fighters(selected(0))
        Dim stats2 = _fighters(selected(1))
        _fighters.Remove(selected(0))
        _fighters.Remove(selected(1))

        Dim fighter1 = New Fighter(selected(0), stats1.Speed, stats1.Attack, stats1.Defense)
        Dim fighter2 = New Fighter(selected(1), stats2.Speed, stats2.Attack, stats2.Defense)

        Return (fighter1, fighter2)
    End Function

    Public Sub StartRounds(Optional roundNum As Integer = 1)
        If Not IsPowerOf2() Then
            Console.WriteLine("El número de luchadores debe ser una potencia de 2.")
            Return
        End If

        Console.WriteLine($"{Environment.NewLine}__Ronda #{roundNum}__")
        Dim nextRound As New Dictionary(Of String, FighterStats)

        While True
            Dim pair = GetRandomPairs()
            Dim fighter1 = pair.Fighter1
            Dim fighter2 = pair.Fighter2
            Dim battle = New Battle(fighter1, fighter2)
            Dim winner = battle.Start()

            nextRound(winner.Name) = New FighterStats(winner.Speed, winner.Attack, winner.Defense)

            If _fighters.Count = 0 Then
                If nextRound.Count > 1 Then
                    _fighters = nextRound
                    StartRounds(roundNum + 1)
                    Exit While
                Else
                    Console.WriteLine($"{Environment.NewLine}--> El vencedor del torneo es '{winner.Name}'.")
                    Exit While
                End If
            End If
        End While
    End Sub
End Class

'  __________________________________________________________
Public Module Program
    Private ReadOnly Fighters As New Dictionary(Of String, FighterStats) From {
        {"Goku", New FighterStats(100, 95, 85)},
        {"Vegeta", New FighterStats(95, 90, 90)},
        {"Gohan", New FighterStats(85, 95, 85)},
        {"Freezer", New FighterStats(90, 90, 90)},
        {"Piccolo", New FighterStats(90, 85, 90)},
        {"Krillin", New FighterStats(85, 75, 75)},
        {"Cell", New FighterStats(90, 95, 85)},
        {"Majin Buu", New FighterStats(80, 85, 95)}
    }

    Public Sub Main()
        Console.WriteLine("Simulación del Torneo de Artes Marciales")
        Dim tournament = New Tournament(Fighters)
        tournament.StartRounds()
    End Sub
End Module
