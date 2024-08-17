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
        public class Wolverine
        {
            private int hp;
            private readonly int attack_min;
            private readonly int attack_max;
            private bool isMaxAttack;

            public int HP { get { return hp; } }
            public bool IsMaxAttack { get { return isMaxAttack; } }

            public Wolverine(int hp)
            {
                this.hp = hp;
                this.attack_min = 10;
                this.attack_max = 120;
            }

            public int Attack()
            {                
                Random random = new Random();
                int attack = random.Next(attack_min, attack_max);

                if (attack == this.attack_max)
                    this.isMaxAttack = true;
                else
                    this.isMaxAttack = false;

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
            private readonly int attack_min = 10;
            private readonly int attack_max = 100;
            private bool isMaxAttack = false;

            public int HP { get { return hp; } }

            public bool IsMaxAttack { get { return isMaxAttack; } }

            public Deadpool(int hp) 
            {
                this.hp = hp;
            }

            public int Attack()
            {
                Random random = new Random();
                int attack = random.Next(attack_min, attack_max);

                if (attack == this.attack_max)
                    this.isMaxAttack = true;
                else
                    this.isMaxAttack = false;

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
        
        static void Main(string[] args)
        {
            Console.Write("Introduce la vida de Wolverine:");
            int wolverineHP = Int16.Parse(Console.ReadLine());
            Console.Write("Introduce la vida de Deadpool:");
            int deadPoolHP = Int16.Parse(Console.ReadLine());
            Wolverine wolverine = new Wolverine(wolverineHP);
            Deadpool deadpool = new Deadpool(deadPoolHP);
            var turno = 0;
            var esCritico = false;

            while (wolverine.HP > 0 && deadpool.HP > 0)
            {
                Console.WriteLine($"\nTurno {++turno}");

                if (!esCritico && deadpool.HP > 0) // Turno de Deadpool si el ataque de Wolverine no ha sido crítico
                {
                    var deadpoolDamage = deadpool.Attack();
                    esCritico = deadpool.IsMaxAttack;

                    if (!wolverine.Dodge())
                    {
                        wolverine.RecievesDamage(deadpoolDamage);
                        Console.WriteLine($"Deadpool ataca a Wolverine y le hace {deadpoolDamage} puntos de vida");
                    }
                    else
                    {
                        Console.WriteLine("Wolverine esquiva el ataque de Deadpool");
                    }
                }
                else if (esCritico)
                {
                    Console.WriteLine("Deadpool no atacará este turno porque se tiene que regenerar");
                    esCritico = false;
                }

                if (!esCritico && wolverine.HP > 0) //Turno de Wolverine si el ataque de Deadpool no ha sido crítico
                {
                    var wolverineDamage = wolverine.Attack();
                    esCritico = wolverine.IsMaxAttack;

                    if (!deadpool.Dodge())
                    {
                        deadpool.RecievesDamage(wolverineDamage);
                        Console.WriteLine($"Wolverine ataca a Deadpool y le hace {wolverineDamage} puntos de vida");
                    }
                    else
                    {
                        Console.WriteLine("Deadpool esquiva el ataque de Wolverine");
                    }
                }
                else if (esCritico)
                {
                    Console.WriteLine("Wolverine no atacará este turno porque se tiene que regenerar");
                    esCritico = false;
                }

                Console.WriteLine($"A Deadpool le quedan {deadpool.HP} puntos de vida");
                Console.WriteLine($"A Wolverine le quedan {wolverine.HP} puntos de vida");

                Thread.Sleep(1000);
            }

            if (deadpool.HP <= 0)
                Console.WriteLine("El ganador es WOLVERINE");
            else
                Console.WriteLine("El ganador es DEADPOOL");

            Console.ReadKey();
        }
    }
}
