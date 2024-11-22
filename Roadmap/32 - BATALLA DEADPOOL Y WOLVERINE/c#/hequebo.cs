class DeadpoolVsWolverine
{
    static void Main(string[] args)
    {
        Hero hero1;
        Hero hero2;
        Random random = new Random();
        Console.WriteLine("---SIMULADOR DE PELEA DEADPOOL VS WOLVERINE---");
        if (random.NextDouble() > 0.5)
        {
            Console.WriteLine("Establece la vida inicial de Deadpool");
            int hp = int.Parse(Console.ReadLine());
            hero1 = new Hero("Deadpool", hp, 10, 100, 0.25);
            Console.WriteLine("Establece la vida inicial de Wolverine");
            hp = int.Parse(Console.ReadLine());
            hero2 = new Hero("Wolverine", hp, 10, 120, 0.20);

        }
        else
        {
            Console.WriteLine("Establece la vida inicial de Wolverine");
            int hp = int.Parse(Console.ReadLine());
            hero1 = new Hero("Wolverine", hp, 10, 120, 0.20);
            Console.WriteLine("Establece la vida inicial de Deadpool");
            hp = int.Parse(Console.ReadLine());
            hero2 = new Hero("Deadpool", hp, 10, 100, 0.25);
        }  
        int turn = 0;   
        
        while(hero1.Hp > 0 && hero2.Hp > 0)
        {
            turn++;
            Console.WriteLine($"Turno {turn}");
            SimulateTurn(ref hero1 , ref hero2);
            if (hero2.Hp > 0)
                SimulateTurn(ref hero2 , ref hero1);
            Thread.Sleep(1000);
        }
        Console.ReadLine();

    }
    static void SimulateTurn(ref Hero hero1, ref Hero hero2)
    {
        if (hero1.Regenarate)
        {
            Console.WriteLine($"{hero1.Name} se está regenerando, no puede atacar este turno...");
        }
        else
        {
            int attack = hero1.Attack();
            Console.WriteLine($"{hero1.Name} Ataca con {attack} puntos de daño");
            bool dogde = hero2.Dodge();
            if (dogde)
            {
                Console.WriteLine($"{hero2.Name} esquivó el ataque y no recibió daño...");
            }
            else
            {
                hero2.TakeDamage(attack);
                Console.WriteLine($"{hero2.Name} recibe {attack} puntos de daño...");
                if (attack == hero1.MaxDamage)
                {
                    Console.WriteLine($"Golpe crítico de {hero1.Name}, {hero2.Name} " +
                        $"no podrá atacar el siguiente turno...");
                    hero2.Regenarate = true;
                }
                if (hero2.Hp <= 0)
                {
                    Console.WriteLine($"La vida de {hero2.Name} ha llegado a 0...");
                    Console.WriteLine($"{hero1.Name} ha ganado la pelea..");
                } 
                else
                    Console.WriteLine($"La salud de {hero2.Name} está en {hero2.Hp}hp...");
            }
        }
        hero1.Regenarate = false;
    }
}

class Hero
{
    private string _name;
    private int _hp;
    private int _minDamage;
    private int _maxDamage;
    private bool _regenarate;
    private double _dodgeChances;

    public string Name { get { return _name; } }
    public int Hp { get { return _hp; } }
    public int MaxDamage{  get { return _maxDamage; } }
    public bool Regenarate
    {
        get => _regenarate;
        set => _regenarate = value;
    }

    public Hero(string name, int hp, int minDamage, int maxDamage, double dodgeChances)
    {
        _name = name;
        _hp = hp;
        _minDamage = minDamage;
        _maxDamage = maxDamage;
        _regenarate = false;
        _dodgeChances = dodgeChances;
    }

    public int Attack()
    {
        Random random = new Random();
        return random.Next(_minDamage, _maxDamage + 1);
    }
    public void TakeDamage(int damage)
    {
        _hp -= damage;
    }
    public bool Dodge()
    {
        Random random = new Random();
        if (random.NextDouble() > _dodgeChances)
        {
            return false;
        }
        return true;
    }
}
