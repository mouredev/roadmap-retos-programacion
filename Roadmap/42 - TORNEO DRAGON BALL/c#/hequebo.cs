class Fighter
{
    private int _id;
    private string _name;
    private int _speed;
    private int _attack;
    private int _defense;
    private double _hp;

    public static int id = 1;

    public int Id {  get { return _id; } }
    public string Name { get { return _name; } }
    public int Speed { get { return _speed;} }
    public int Attack { get { return _attack;} }
    public int Defense { get { return _defense;} }
    public double Hp { get { return _hp;} set { _hp = value; } }


    public Fighter(string name, int speed, int attack, int defense)
    { 
        _id = id;
        id++;
        _name = name;
        _speed = speed;
        _attack = attack;
        _defense = defense;
        _hp = 100;
    }
    public void TakeDamage(int attack)
    {
        Random random = new Random();
        if (random.NextDouble() < 0.20)
        {
            Console.WriteLine($"{_name} ha esquivado el ataque y no recibió daño");
        }
        else
        {
            double damage;
            if (_defense >= attack)
                 damage = attack * 0.10;
            else
                damage = attack - _defense;
            Console.WriteLine($"{_name} ha recibido {damage} puntos de daño");
            _hp -= damage;
        }
        Console.WriteLine($"La salud de {_name} es de {(_hp > 0 ? _hp : 0)}hp");
    }   
}
class BattleSimulator
{
    private Fighter _fighter1;
    private Fighter _fighter2;

    public BattleSimulator(Fighter fighter1, Fighter fighter2)
    {
        _fighter1 = fighter1;
        _fighter2 = fighter2;
    }
    public Fighter Battle()
    {
        Console.WriteLine($"---{_fighter1.Name} VS {_fighter2.Name}---");

        while (_fighter1.Hp > 0 && _fighter2.Hp > 0)
        {
            if (_fighter1.Speed > _fighter2.Speed)
            {
                _fighter2.TakeDamage(_fighter1.Attack);
                Thread.Sleep(1500);
                if (_fighter2.Hp > 0)
                {
                    _fighter1.TakeDamage(_fighter2.Attack);
                    Thread.Sleep(1500);
                }
                    
            }
            else
            {
                _fighter1.TakeDamage(_fighter2.Attack);
                Thread.Sleep(1500);
                if (_fighter1.Hp > 0)
                {
                    _fighter2.TakeDamage(_fighter1.Attack);
                    Thread.Sleep(1500);
                }
                    
            }
        }
        var winner = _fighter1.Hp > 0 ? _fighter1 : _fighter2;
        Console.WriteLine($"¡{winner.Name} ha sido el ganador!");
        winner.Hp = 100;
        return winner;
        
    }
}
class Tournament
{
    private List<Fighter> _fighters;

    public Tournament(List<Fighter> fighters)
    {
        _fighters = fighters;
    }
    public void Start()
    {
        int round = 1;
        _fighters = _fighters.OrderBy(f => Guid.NewGuid()).ToList();
        while (_fighters.Count > 1)
        {
            Console.WriteLine($"---Ronda {(_fighters.Count == 2 ? "Final" : round)}---");

            var winnersList = new List<Fighter>();

            for (int i = 0; i < _fighters.Count; i+= 2)
            {
                BattleSimulator battleSimulator = new BattleSimulator(_fighters[i], _fighters[i + 1]);
                var winner = battleSimulator.Battle();
                winnersList.Add(winner);
                Thread.Sleep(1500);
            }
            _fighters = winnersList; 
            round++;
        }
        Console.WriteLine($"¡{_fighters[0].Name} es el ganador del torneo!");
    }
}
class Program
{
    static void Main(string[] args)
    {

        List<Fighter> roster = new List<Fighter>
        {
            new Fighter("Gokú", 90, 85, 80),
            new Fighter("Vegeta", 85, 90, 80),
            new Fighter("Gohan", 80, 80, 80),
            new Fighter("Picoro", 80, 75, 80),
            new Fighter("Goten", 70, 75, 70),
            new Fighter("Trunks", 75, 75, 70),
            new Fighter("Trunks F", 85, 80, 90),
            new Fighter("Krilin", 65, 65, 60),
            new Fighter("Yamcha", 60, 55, 50),
            new Fighter("Tenchinhan", 75, 70, 65),
            new Fighter("Nappa", 65, 80, 70),
            new Fighter("Freezer", 85, 80, 75),
            new Fighter("Cell", 80, 85, 85),
            new Fighter("Majin Buu", 70, 80, 90),
            new Fighter("Bills", 90, 90, 85),
            new Fighter("Whis", 99, 99, 99),
            new Fighter("Hit", 95, 80, 85),
            new Fighter("Gokú Black", 85, 80, 75),
            new Fighter("Zamasu", 80, 85, 75),
            new Fighter("Jiren", 95, 90, 85),
            new Fighter("Gokú UI", 95, 85, 90),
            new Fighter("Vegeta UE", 85, 95, 80),
            new Fighter("Gohan B.", 80, 85, 90),
            new Fighter("O. Picoro", 80, 85, 90),
            new Fighter("Vegito", 95, 90, 95),
            new Fighter("Gogeta", 90, 95, 95),
            new Fighter("Kefla", 85, 85, 80),
            new Fighter("No. 17", 80, 80, 75),
            new Fighter("No. 18", 80, 80, 75),
            new Fighter("Bardock", 80, 75, 70),
            new Fighter("Gotenks", 90, 85, 80),
            new Fighter("Broly", 80, 95, 85)
        };

        Console.WriteLine("!Bienvenido al torneo de artes marciales¡");
        Console.WriteLine("Ingresa el número de peleadores a participar (Máx. 32)");
        int fightersAmount;
        if (!int.TryParse(Console.ReadLine(), out fightersAmount))
        {
            Console.WriteLine("No se ha ingresado una cantidad correcta...");
            return;
        }
        if (fightersAmount > 32)
        {
            Console.WriteLine("La cantidad máxima de participantes es 32...");
            return;
        }
        if (!IsPowerOfTwo(fightersAmount))
        {
            Console.WriteLine("La cantidad de participantes tiene que ser potencia de 2...");
            return;
        }

        for (int i = 0; i < roster.Count; i += 4)
        {
            Console.WriteLine($"{roster[i].Id}.- {roster[i].Name}\t\t" +
                $"{roster[i + 1].Id}.- {roster[i + 1].Name}\t\t" +
                $"{roster[i + 2].Id}.- {roster[i + 2].Name}\t\t" +
                $"{roster[i + 3].Id}.- {roster[i + 3].Name}");
        }
        Console.WriteLine("Ingresa los Id de los peleadores que desees seleccionar");
        Console.WriteLine("Si deseas elegir aleatoriamente ingresa la tecla 'R'");

        bool randomSelection = Console.ReadLine().ToLower() == "r";
        var participantsList = new List<Fighter>();
        if (randomSelection)
        {
            Console.WriteLine("Se seleccionarán los peleadores aleatoriamente... ");
            int selectedAmount = 0;
            Random random = new Random();
            while (selectedAmount < fightersAmount)
            {
                int index = random.Next(0, roster.Count);
                var fighter = roster[index];
                participantsList.Add(fighter);
                roster.RemoveAt(index);
                selectedAmount++;
            }
        }
        else
        {
            int selectedAmount = 0;
            while (selectedAmount < fightersAmount)
            {
                Console.WriteLine($"Selecciona un luchador ({selectedAmount + 1})");
                int id;
                if (!int.TryParse (Console.ReadLine(), out id))
                {
                    Console.WriteLine("No se ha ingresado un id válido...");
                }
                else
                {
                    var fighter = roster.Where(f => f.Id == id).FirstOrDefault();
                    if (fighter == null)
                    {
                        Console.WriteLine($"No se ha podido obtener el peleador con id {id}");
                    }
                    else
                    {
                        Console.WriteLine($"¡{fighter.Name} ha sido seleccionado!");
                        participantsList.Add(fighter);
                        roster.Remove(fighter);
                        selectedAmount++;
                    }
                }
            }
        }

        Console.WriteLine("Estos son los participantes del torneo:");
        foreach (var (figter, index) in participantsList.Select((item, index) => (item, index)))
            Console.WriteLine($"{index + 1}.- {figter.Name}");

        Tournament tournament = new Tournament(participantsList);
        tournament.Start();
    }
    static bool IsPowerOfTwo(int x)
    {
        return (x != 0) && ((x & (x - 1)) == 0);
    }
}