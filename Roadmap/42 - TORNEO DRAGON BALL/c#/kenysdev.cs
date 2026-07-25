namespace exs42;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
42 TORNEO DRAGON BALL
------------------------------------

* EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.
*/

using System;
using System.Collections.Generic;
using System.Linq;

public class Fighter(string name, int speed, int attack, int defense)
{
    public string Name { get; } = name;
    public int Speed { get; } = speed;
    public int Attack { get; } = attack;
    public int Defense { get; } = defense;
    public double Health { get; set; } = 100;

    public void ExecuteAttack(Fighter opponent)
    {
        Console.WriteLine($"'{Name}' ataca a '{opponent.Name}'");

        double damage = opponent.Defense >= Attack 
            ? Attack * 0.1 // 10%
            : Attack - opponent.Defense;

        if (!ActivateDefense())
        {
            opponent.Health -= damage;
            Console.WriteLine($"'{opponent.Name}' ha recibido '{damage}' de daño");
            Console.WriteLine($"Salud restante '{opponent.Health}'\n");
        }
        else
        {
            Console.WriteLine($"'{opponent.Name}' ha esquivado el ataque.\n");
        }
    }

    private static bool ActivateDefense() => Random.Shared.NextDouble() <= 0.2; // 20%

}

// __________________________________________________________
public class Battle
{
    private readonly Fighter _fighter1;
    private readonly Fighter _fighter2;

    public Battle(Fighter fighter1, Fighter fighter2)
    {
        _fighter1 = fighter1;
        _fighter2 = fighter2;
        Console.WriteLine($"__'{_fighter1.Name} VS '{_fighter2.Name}'__\n");
    }

    private static Fighter Combat(Fighter fighterA, Fighter fighterB)
    {
        while (true)
        {
            fighterA.ExecuteAttack(fighterB);
            if (fighterB.Health <= 0)
            {
                Console.WriteLine($"--> '{fighterA.Name}' gana la batalla.__\n");
                return fighterA;
            }

            fighterB.ExecuteAttack(fighterA);
            if (fighterA.Health <= 0)
            {
                Console.WriteLine($"--> '{fighterB.Name}' gana la batalla.\n");
                return fighterB;
            }
        }
    }

    public Fighter Start() =>
        _fighter1.Speed > _fighter2.Speed 
            ? Combat(_fighter1, _fighter2) 
            : Combat(_fighter2, _fighter1);
}

// __________________________________________________________
public record FighterStats(int Speed, int Attack, int Defense);

public class Tournament(Dictionary<string, FighterStats> fighters)
{
    private Dictionary<string, FighterStats> _fighters = fighters;

    private bool IsPowerOf2() =>
        _fighters.Count > 1 && Math.Log2(_fighters.Count) % 1 == 0;

    private (Fighter, Fighter) GetRandomPairs()
    {
        var randomFighters = _fighters.Keys.OrderBy(_ => Random.Shared.Next()).Take(2).ToArray();
        
        var fighter1Data = _fighters[randomFighters[0]];
        var fighter2Data = _fighters[randomFighters[1]];

        var fighter1 = new Fighter(randomFighters[0], fighter1Data.Speed, fighter1Data.Attack, fighter1Data.Defense);
        var fighter2 = new Fighter(randomFighters[1], fighter2Data.Speed, fighter2Data.Attack, fighter2Data.Defense);

        _fighters.Remove(randomFighters[0]);
        _fighters.Remove(randomFighters[1]);

        return (fighter1, fighter2);
    }

    public void StartRounds(int roundNum = 1)
    {
        if (!IsPowerOf2())
        {
            Console.WriteLine("El número de luchadores debe ser una potencia de 2.");
            return;
        }

        Console.WriteLine($"\n__Ronda #{roundNum}__");
        var nextRound = new Dictionary<string, FighterStats>();

        while (true)
        {
            var (fighter1, fighter2) = GetRandomPairs();
            var battle = new Battle(fighter1, fighter2);
            var winner = battle.Start();

            nextRound[winner.Name] = new FighterStats(
                Speed: fighter1.Speed,
                Attack: fighter1.Attack,
                Defense: fighter1.Defense
            );

            if (_fighters.Count == 0 && nextRound.Count > 1)
            {
                _fighters = nextRound;
                StartRounds(roundNum + 1);
                break;
            }

            if (_fighters.Count == 0 && nextRound.Count == 1)
            {
                Console.WriteLine($"\n--> El vencedor del torneo es '{winner.Name}'.");
                break;
            }
        }
    }
}

// __________________________________________________________
public static class Program
{
    private static readonly Dictionary<string, FighterStats> Fighters = new()
    {
        ["Goku"] = new(Speed: 100, Attack: 95, Defense: 85),
        ["Vegeta"] = new(Speed: 95, Attack: 90, Defense: 90),
        ["Gohan"] = new(Speed: 85, Attack: 95, Defense: 85),
        ["Freezer"] = new(Speed: 90, Attack: 90, Defense: 90),
        ["Piccolo"] = new(Speed: 90, Attack: 85, Defense: 90),
        ["Krillin"] = new(Speed: 85, Attack: 75, Defense: 75),
        ["Cell"] = new(Speed: 90, Attack: 95, Defense: 85),
        ["Majin Buu"] = new(Speed: 80, Attack: 85, Defense: 95)
    };

    public static void Main()
    {
        Console.WriteLine("Simulación del Torneo de Artes Marciales");
        var tournament = new Tournament(Fighters);
        tournament.StartRounds();
    }
}
