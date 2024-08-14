namespace exs32;
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
-----------------------------------------------------
* BATALLA DEADPOOL Y WOLVERINE
-----------------------------------------------------

 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
*/
using System.Text;

// _____
// NOTA: Estoy intentando practicar los principios SOLID. XD 😂

// ---------------------------------------
// INYECCIÓN DE DEPENDENCIAS
// ---------------------------------------
// _______________________________________
/// <summary>Definirá las interfaces que requieren ser configuradas</summary>
public class Factory
{
    public required IGlobalConfig GlobalConfig { get; set; }
    public required IInput Input { get; set; }
    public required IBattleStrategy Strategy { get; set; }
    public required ICharacter Character1 { get; set; }
    public required ICharacter Character2 { get; set; }
}

// _______________________________________
/// <summary>Recibe la inyección de dependencias</summary>
public class Program(Factory _factory, Simulation simulation)
{
    public static void Main()
    {
        Console.OutputEncoding = Encoding.UTF8;
        Factory factory = ConfigureFactory();
        Simulation simulation = new(factory);
        Program program = new(factory, simulation);
        program.Run();
    }
    public void Run()
    {
        Console.WriteLine(_factory.GlobalConfig.Menu);
        while (true)
        {
            int option = _factory.Input.Get("\nOpción: ");
            switch (option)
            {
                case 1: simulation.Start(); break;
                case 2: Console.WriteLine("Adios"); return;
                default: Console.WriteLine("Seleccionar de '1 a 5'"); break;
            }
        }
    }

    /// <summary>Asignará y retornará las instancias de clases que dependen de las interfaces.</summary>
    private static Factory ConfigureFactory()
    {
        return new Factory
        {
            GlobalConfig = new DefaultConfig(),
            Input = new ConsoleInput(),
            Strategy = new DefaultBattleStrategy(),
            Character1 = new DefaultCharacter(),
            Character2 = new DefaultCharacter()
        };
    }
}

// _______________________________________
/// <summary>Realizar simulación de la batalla</summary>
public class Simulation(Factory factory)
{
    /// <summary>Agrega datos de los personajes</summary>
    public void AddCharacter(string msg, ICharacter character)
    {
        while (true)
        {
            int index = factory.Input.Get(msg);
            var keys = factory.GlobalConfig.Characters.Keys.ToList();

            if (index < 0 || index >= keys.Count)
            {
                Console.WriteLine("Número de personaje incorrecto.");
                continue; // Volver a solicitar
            }

            if (keys[index] == factory.Character1.Name)
            {
                Console.WriteLine("El personaje ya fue utilizado.");
                continue;
            }

            int hp = factory.Input.Get($"Establecer una vida >= que '{factory.GlobalConfig.MinimumHp}': ");
            if (hp < factory.GlobalConfig.MinimumHp)
            {
                Console.WriteLine($"La vida debe ser mayor o igual que '{factory.GlobalConfig.MinimumHp}'.");
                continue;
            }

            string name = keys[index];
            TCharacterConfig attributes = factory.GlobalConfig.Characters[name];
            character.Add(name, hp, attributes);
            break;
        }
    }

    public void ShowHp()
    {
        Console.WriteLine("____________________________");
        Console.WriteLine($"|{factory.Character1.Name}: ❤️ {factory.Character1.Hp}| |{factory.Character2.Name}: ❤️ {factory.Character2.Hp}|");
    }

    /// <summary>Llevará a cabo el turno de la batalla.</summary>
    public void Battle()
    {
        int turn = 1;
        while (true)
        {
            Console.WriteLine($"\n----------------------------\nTurno #{turn}\n----------------------------");

            // Ataque de personaje #1 hacia #2
            ShowHp();
            if (!factory.Strategy.Execute(factory.Character1, factory.Character2))
            {
                break;
            }

            // Ataque de personaje #2 hacia #1
            ShowHp();
            if (!factory.Strategy.Execute(factory.Character2, factory.Character1))
            {
                break;
            }

            turn++;
            Thread.Sleep(factory.GlobalConfig.TurnInterval * 1000);
        }

        ShowHp();
    }

    public void Start()
    {
        Console.WriteLine("Personajes disponibles:");
        var characters = factory.GlobalConfig.Characters.Keys.ToList();
        for (int i = 0; i < characters.Count; i++)
        {
            Console.WriteLine($"{i}. {characters[i]}");
        }

        AddCharacter("\n'Primer' personaje: ", factory.Character1);

        AddCharacter("'Segundo' personaje: ", factory.Character2);

        Battle();

        factory.Character1.Name = "";
        Console.WriteLine(factory.GlobalConfig.Menu);
    }
}

// ---------------------------------------
// INTERFACES
// ---------------------------------------
// _______________________________________
/// <summary>Contrato para la configuración global.</summary>
public interface IGlobalConfig
{
    /// <summary>Tiempo de espera en segundos entre cada turno.</summary>
    int TurnInterval { get; }

    /// <summary>Mínima cantidad de vida inicial permitida.</summary>
    int MinimumHp { get; }

    /// <summary>
    /// Diccionario de personajes, con sus habilidades, Daño posible, Probabilidad de defensa.
    /// {"Character": {"attacks": ["Attack1", "Attack2"], "damage_range": (10, 100), "defense_chance": 0.25}}
    /// </summary>
    IDictionary<string, TCharacterConfig> Characters { get; }

    /// <summary>Acciones del menú principal.</summary>
    string Menu { get; }
}


/// <summary>Tipos requeridos en el diccionario./// </summary>
public class TCharacterConfig
{
    public required List<string> Attacks { get; set; }
    public (int Min, int Max) DamageRange { get; set; }
    public double DefenseChance { get; set; }
}

// _______________________________________
/// <summary> Contrato sobre la entra de datos.</summary>
public interface IInput
{
    /// <param name="msg">Mensaje a mostrar al usuario.</param>
    /// <returns>un dato entero que no debe ser vacio.</returns>
    int Get(string msg);
}

// _______________________________________
/// <summary> Contrato sobre los datos y metodos de un personaje que participara en la batalla.</summary>
public interface ICharacter
{
    // Propiedades
    string Name { get; set; }
    int Hp { get; set; }
    bool CanAttack { get; set; }
    List<string> Attacks { get; set; }
    (int MinDamage, int MaxDamage) DamageRange { get; set; }
    double DefenseChance { get; set; }

    void Add(string name, int hp, TCharacterConfig attributes);

    // Métodos
    /// <summary> Verifica si puede atacar, realiza un ataque y devuelve el daño infligido.</summary>
    int Attack();

    /// <summary> Determina si el personaje puede defenderse.</summary>
    bool Defend();
}

// _______________________________________
/// <summary>Lógica para la batalla.</summary>
public interface IBattleStrategy
{
    /// <summary>Ejecuta la estrategia de batalla entre el atacante y el defensor.</summary>
    /// <returns>Retorna verdadero si el defensor sigue en pie, falso si el atacante gana la batalla.</returns>
    bool Execute(ICharacter attacker, ICharacter defender);
}

// ---------------------------------------
// IMPLEMENTACIÓN DE INTERFACES
// ---------------------------------------
// _______________________________________
/// <summary>Constantes globales.</summary>
public class DefaultConfig : IGlobalConfig
{
    private const int TIME = 1; // segundos
    private readonly int MINIMUM_HP = 200;

    private static readonly IDictionary<string, TCharacterConfig> CHARACTERS =
        new Dictionary<string, TCharacterConfig>
        {
            {
                "Deadpool",
                new TCharacterConfig
                {
                    Attacks = ["Con arma.", "Cuerpo a cuerpo.", "Con ataque imprudente."],
                    DamageRange = (10, 100),
                    DefenseChance = 0.25
                }
            },
            {
                "Wolverine",
                new TCharacterConfig
                {
                    Attacks = ["Con garras de adamantium.", "Con arma.", "Cuerpo a cuerpo."],
                    DamageRange = (10, 120),
                    DefenseChance = 0.20
                }
            }
            // Puedes añadir más personajes aquí.
        };

    private const string MENU = @"
SIMULADOR DE BATALLAS:
------------------------------------------
| 1. Simular una batalla | 2. Salir      |  
------------------------------------------";

    public int TurnInterval => TIME;
    public int MinimumHp => MINIMUM_HP;
    public IDictionary<string, TCharacterConfig> Characters => CHARACTERS;
    public string Menu => MENU;
}

// _______________________________________
/// <summary>Solicitud de entrada.</summary>
public class ConsoleInput : IInput
{
    public int Get(string msg)
    {
        while (true)
        {
            Console.Write(msg);
            string? input = Console.ReadLine();

            if (string.IsNullOrWhiteSpace(input))
            {
                Console.WriteLine("La entrada no puede estar vacía.");
                continue;
            }

            if (int.TryParse(input, out int intValue))
            {
                return intValue;
            }
            else
            {
                Console.WriteLine("Por favor, ingresa un número entero válido.");
            }
        }
    }
}

// _______________________________________
/// <summary>Datos y metodos de un personaje que participara en la batalla.</summary>
public class DefaultCharacter : ICharacter
{
    public string Name { get; set; } = "";
    public int Hp { get; set; } = 0;
    public bool CanAttack { get; set; } = true;
    public List<string> Attacks { get; set; } = [];
    public (int MinDamage, int MaxDamage) DamageRange { get; set; } = (0, 0);
    public double DefenseChance { get; set; } = 0.0;

    public void Add(string name, int hp, TCharacterConfig attributes)
    {
        Name = name;
        Hp = hp;
        Attacks = attributes.Attacks;
        DamageRange = attributes.DamageRange;
        DefenseChance = attributes.DefenseChance;
    }

    public int Attack()
    {
        if (CanAttack)
        {
            Random random = new();
            int damage = random.Next(DamageRange.MinDamage, DamageRange.MaxDamage + 1);
            string selectedAttack = Attacks[random.Next(Attacks.Count)];
            Console.WriteLine($"|'{Name}' ataca '{selectedAttack}' causando un: '-{damage}' 👊|");
            return damage;
        }
        else
        {
            Console.WriteLine($"|'{Name}' se está regenerando y no puede atacar. 😴|");
            return 0;
        }
    }

    public bool Defend()
    {
        Random random = new();
        bool defended = random.NextDouble() < DefenseChance;
        Console.WriteLine(defended
            ? $"|'{Name}' logró defenderse. 🛡️|"
            : $"|'{Name}' no pudo bloquear el ataque. 🤕|");
        return defended;
    }
}

// _______________________________________
/// <summary>Estrategia estabglecida.</summary>
public class DefaultBattleStrategy : IBattleStrategy
{
    public bool Execute(ICharacter attacker, ICharacter defender)
    {
        int damage = attacker.Attack();

        if (damage == attacker.DamageRange.MaxDamage)
        {
            Console.WriteLine($"|'{defender.Name}' 🚨recibió un ataque crítico y no podrá atacar.🚨|");
            defender.CanAttack = false;
        }

        if (attacker.CanAttack)
        {
            if (!defender.Defend())
            {
                defender.Hp -= damage;
            }
        }
        else
        {
            attacker.CanAttack = true;
        }

        if (defender.Hp <= 0)
        {
            Console.WriteLine("\n____________________________");
            Console.WriteLine($"|'{attacker.Name}' 🏆 gana la batalla. 🏆|");
            return false;
        }

        return true;
    }
}

// _____
// NOTA: Estoy intentando practicar los principios SOLID. XD 😂

