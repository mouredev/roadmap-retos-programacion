/******************************************************************************/
// Author: Luis Rodriguez
// github: https//github.com/lurtur
// Date: 15 August 2024
/******************************************************************************/

namespace _32_WolverineVsDeadpool;

/// <summary>
/// Defines the state contract
/// </summary>
public interface IState
{
    public void RunAction(Character context, Character oponent, Battle battle);
}

/// <summary>
/// Defines the action when the character is in Attacking state.
/// </summary>
public class Attacking() : IState
{
    public void RunAction(Character context, Character oponent, Battle battle)
    {
        if (context.Regenerate == true)
        {
            context.Regenerate = false;
            Console.WriteLine($"{context.Name} is regenerating...skip attack this turn.");
        }
        else
        {
            int damage = context.Attack(oponent);

            oponent.Defend();

            battle.UpdateHealth(oponent, damage);
        }

        context.SetState(new Defending());
    }
}

/// <summary>
/// Defines the action when the character is in Defending state
/// </summary>
public class Defending() : IState
{
    public void RunAction(Character context, Character oponent, Battle battle)
    {
        context.SetState(new Attacking());
    }
}

/// <summary>
/// Defines the character class.
/// It is the context on the State design pattern.
/// </summary>
/// <param name="name">The name of the character</param>
/// <param name="health">The health level of the character</param>
/// <param name="minDamage">The minimum damage the character can inflict</param>
/// <param name="maxDamage">The maximum damage the character can inflict</param>
/// <param name="elusionThreshold">Threshold to elude attacks</param>
/// <param name="initialState">Initial state of the character</param>
public class Character(string name, int health, int minDamage, int maxDamage, int elusionThreshold, IState initialState)
{
    public string Name { get; set; } = name;
    public int Health { get; set; } = health;
    public int MinDamage { get; set; } = minDamage;
    public int MaxDamage { get; set; } = maxDamage;
    public bool Elude { get; set; }
    public int ElusionThreshold { get; set; } = elusionThreshold;
    public bool Regenerate { get; set; }

    private IState _state = initialState;

    public void SetState(IState state)
    {
        _state = state;
    }

    public void RunAction(Character oponent, Battle battle)
    {
        _state.RunAction(this, oponent, battle);
    }

    public int Attack(Character oponent)
    {
        // Generate a random damage value
        Random rnd = new();
        int damage = rnd.Next(MinDamage, MaxDamage + 1);

        // Determine if it is a critical damage
        if (damage == MaxDamage)
        {
            // The oponent will regenerate next turn, hence skip the attack
            // This just set the Regenerate property based on the potential damage
            // but the final value is determined by defending which can set it to 
            // false upon eluding the attack.
            oponent.Regenerate = true;

            Console.WriteLine($"AMAZING CRITICAL!!! {Name} attacks with {damage} units of damage.");
        }
        else
        {
            Console.WriteLine($"{Name} attacks with {damage} units of damage.");
        }

        return damage;
    }

    public void Defend()
    {
        // Get a random value as the probability of eluding the attack
        Random rnd = new();
        int elusionChance = rnd.Next(1, 100);

        // Determine if the attack is eluded
        if (elusionChance < ElusionThreshold)
        {
            Elude = true;

            // In case the attack is eluded the character will not regenerate
            // since the damaged was not inflicted
            Regenerate = false;

            Console.WriteLine($"UNBELIEVABLE!!! {Name} eludes the attack.");
        }
        else
        {
            Console.WriteLine($"TOO LATE!!! {Name} received the attack.");
        }
    }
}

/// <summary>
/// Defines the battle class.
/// It handles the battle by:
/// - Updating the health of the oponents.
/// - Displaying the health on the console.
/// - Running the actions of the characters.
/// </summary>
/// <param name="character1">The first character in the battle</param>
/// <param name="character2">The second character in the battle</param>
public class Battle(Character character1, Character character2)
{
    private Character _character1 = character1;
    private Character _character2 = character2;

    private int _turn;

    public void Start()
    {
        int counter = 0;
        Console.WriteLine("The battle begins!\n");
        while (_character1.Health > 0 && _character2.Health > 0)
        {
            // Each turn implies the counter increment two numbers.
            // e.g. counter = 1 means the first character attacking and
            // counter = 2 means the second character attacking. Therefore,
            // every two iterations _turn is incremented.
            if ((counter % 2) == 0)
            {
                ++_turn;
                counter = 0;
                Console.WriteLine($"\nTurn {_turn}");
            }
            ++counter;

            _character1.RunAction(_character2, this);
            if (_character2.Health > 0)
            {
                _character2.RunAction(_character1, this);
            }

            DisplayHealth();

            if (counter ==  2)
            {
                Console.WriteLine("Waiting 1 second...");
                Thread.Sleep(1000);
            }
        }

        // Determine which character wins
        if (_character1.Health > 0)
        {
            Console.WriteLine("-------------------------------------------");
            Console.WriteLine($"{_character1.Name} wins the battle.");
            Console.WriteLine("-------------------------------------------");
        }
        else
        {
            Console.WriteLine("-------------------------------------------");
            Console.WriteLine($"{_character2.Name} wins the battle.");
            Console.WriteLine("-------------------------------------------");
        }
    }

    public void UpdateHealth(Character oponent, int damage)
    {
        if (oponent.Elude == false)
        {
            oponent.Health -= damage;
            if (oponent.Health < 0)
            {
                oponent.Health = 0;
            }
        }
        else
        {
            oponent.Elude = false;
        }
    }

    private void DisplayHealth()
    {
        Console.WriteLine($"{_character1.Name} health {_character1.Health}");
        Console.WriteLine($"{_character2.Name} health {_character2.Health}");
    }
}


class Program
{
    static void Main(string[] args)
    {
        // Console.WriteLine("Enter the health for Wolverine");
        // int deadpoolHealth = int.Parse(Console.ReadLine()!);
        int deadpoolHealth = 1000;

        //Console.WriteLine("Enter the health for Deadpool");
        //int wolwerineHealth = int.Parse(Console.ReadLine()!);
        int wolwerineHealth = 1000;

        Character deadpool = new("Deadpool", deadpoolHealth, 10, 100, 25, new Attacking());
        Character wolwerine = new("Wolverine", wolwerineHealth, 10, 120, 20, new Defending());

        Battle battle = new(deadpool, wolwerine);
        battle.Start();
    }
}