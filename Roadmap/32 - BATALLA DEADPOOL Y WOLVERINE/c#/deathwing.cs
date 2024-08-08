/*
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

using System;
using System.CodeDom;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Threading;
using System.Threading.Tasks;

namespace deathwing696
{
    public class deathwing696
    {
        const string kMENSAJE_ERROR = "No hay batalla en curso, simular primero una batalla";

        public class Wolverine
        {
            private int hp;
            private int attack_min;
            private int attack_max;

            public int HP { get { return hp; } }

            public Wolverine(int hp)
            {
                this.hp = hp;
                this.attack_min = 10;
                this.attack_max = 120;
            }

            public int Attack(out bool isMaxAttack)
            {                
                Random random = new Random();
                int attack = random.Next(attack_min, attack_max);
                isMaxAttack = attack == this.attack_max;

                return attack;

            }

            public bool Dodge()
            {
                Random random = new Random();
                int prob = random.Next(1, 5);

                return prob == 1;
            }

            public bool RecievesDamage(int damage)
            {
                this.hp -= damage;

                return this.hp <= 0;
            }
        }
        public class Deadpool
        {
            private int hp;
            private int attack_min = 10;
            private int attack_max = 100;

            public int HP { get { return hp; } }

            public Deadpool(int hp) 
            {
                this.hp = hp;
            }

            public int Attack(out bool isMaxAttack)
            {
                Random random = new Random();
                int attack = random.Next(attack_min, attack_max);
                isMaxAttack = attack == this.attack_max;

                return attack;

            }

            public bool Dodge()
            {
                Random random = new Random();
                int prob = random.Next(1, 4);

                return prob == 1;
            }

            public bool RecievesDamage(int damage)
            {
                this.hp -= damage;

                return this.hp <= 0;
            }

        }
        public class Battle
        {
            private int wolverineHP;
            private int deadpoolHP;
            private int turn;
            private string description;
            private static string winner;

            public int WolverineHP { get { return wolverineHP; } }
            public int DeadpoolHP { get { return deadpoolHP; } }
            public int Turn { get { return turn; } }
            public string Description { get { return description; } }
            public static string Winner { get; set; }

            public Battle(int wolverineHP, int deadpoolHP, int turn, string description)
            {
                this.wolverineHP = wolverineHP;
                this.deadpoolHP = deadpoolHP;
                this.turn = turn;
                this.description = description;
            }

            public string ShowBattleLog()
            {
                return $"turno {this.turn}: {this.description}";
            }

            public string ShowBattleHP()
            {
                return $"turno {this.turn}: La vida de Wolverine es {this.wolverineHP}. La vida de Deadpool es {this.deadpoolHP}";
            }
        }

        static void Main(string[] args)
        {
            Console.Write("Introduce la vida de Wolverine:");
            int wolverineHP = Int16.Parse(Console.ReadLine());
            Console.Write("Introduce la vida de Deadpool:");
            int deadPoolHP = Int16.Parse(Console.ReadLine());
            Wolverine wolverine = new Wolverine(wolverineHP);
            Deadpool deadpool = new Deadpool(deadPoolHP);
            List<Battle> log = new List<Battle>();
            bool isSimulating = false;

            while(true)
            {
                Console.WriteLine("1.Simula una batalla.");
                Console.WriteLine("2.Muestra el número del turno(pausa de 1 segundo entre turnos).");
                Console.WriteLine("3.Muestra qué pasa en cada turno.");
                Console.WriteLine("4.Muestra la vida en cada turno.");
                Console.WriteLine("5.Muestra el resultado final.");                
                Console.Write("Introduce una opción:");

                int option = Int16.Parse(Console.ReadLine());

                switch(option) 
                {
                    case 1:
                        if (!isSimulating)
                        {
                            Task.Run(() => SimulaBatalla(wolverine, deadpool, log));
                            isSimulating = true;
                        }
                        break;
                    case 2:
                        if (log.Count == 0)
                        {
                            Console.WriteLine(kMENSAJE_ERROR);
                        }
                        else
                        {
                            Battle battle = log[log.Count - 1];

                            if (battle != null)
                                Console.WriteLine($"Turno {battle.Turn}");
                        }
                        break;
                    case 3:
                        if (log.Count == 0)
                        {
                            Console.WriteLine(kMENSAJE_ERROR);
                        }
                        else
                        {
                            foreach (Battle turn in log)
                                Console.Write(turn.ShowBattleLog());
                        }
                        break;
                    case 4:
                        if (log.Count == 0)
                        {
                            Console.WriteLine(kMENSAJE_ERROR);
                        }
                        else
                        {
                            foreach (Battle turn in log)
                                Console.WriteLine(turn.ShowBattleHP());
                        }
                        break;
                    case 5:
                        if (log.Count == 0)
                        {
                            Console.WriteLine("No ha habido batalla");
                        }
                        else
                        {
                            Console.WriteLine($"El ganador de la batalla ha sido {Battle.Winner}");
                        }

                        Console.Write("Batalla terminada");
                        Console.ReadKey();
                        return;                        
                    default:
                        Console.WriteLine("Opción inválida");
                        break;
                }
            }            
        }

        private static async void SimulaBatalla(Wolverine wolverine, Deadpool deadpool, List<Battle> log)
        {
            bool isMaxAttackWolverin = false;
            bool isMaxAttackDeadpool = false;
            int turn = 1;            

            while (wolverine.HP > 0 && deadpool.HP > 0)
            {
                string description = String.Empty;

                if (!isMaxAttackWolverin)
                {
                    int wolverineAttack = wolverine.Attack(out isMaxAttackWolverin);
                    if (!deadpool.Dodge())
                    {
                        deadpool.RecievesDamage(wolverineAttack);
                        description += $"Wolverine ataca a Deadpool y le hace {wolverineAttack} puntos de daño dejando a Deadpool con {deadpool.HP} puntos de vida\n";
                    }
                    else
                    {
                        description += $"Wolverine ataca a Deadpool pero este esquiva el ataque\n";
                    }
                }

                if (!isMaxAttackDeadpool)
                {
                    int deadpoolAttack = deadpool.Attack(out isMaxAttackDeadpool);

                    if (!wolverine.Dodge())
                    {
                        wolverine.RecievesDamage(deadpoolAttack);
                        description += $"Deadpool ataca a Wolverine y le hace {deadpoolAttack} puntos de daño dejando a Wolverine con {wolverine.HP} puntos de vida\n";
                    }
                    else 
                    {
                        description += $"Deadpool ataca a Wolverine pero este consigue esquivar el ataque\n";
                    }
                }

                Battle battle = new Battle(wolverine.HP, deadpool.HP, turn, description);
                log.Add(battle);
                
                turn++;
                await Task.Delay(1000);
            }

            if (wolverine.HP <= 0 && deadpool.HP > 0)
                Battle.Winner = "Deadpool";
            else if (deadpool.HP <= 0 && wolverine.HP > 0)
                Battle.Winner = "Wolverine";
            else
                Battle.Winner = "Empate";            
        }
    }
}