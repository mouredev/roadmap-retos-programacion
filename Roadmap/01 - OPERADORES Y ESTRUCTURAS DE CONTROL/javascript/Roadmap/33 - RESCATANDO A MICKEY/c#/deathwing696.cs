using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Policy;
using System.Text;

namespace reto33
{
    public class deathwing696
    {
        const string kMENSAJE = "Movimiento no permitido";
        public class Posicion
        {
            private int x, y;

            public int X { get { return x; } }
            public int Y { get { return y; } }

            public Posicion(int x, int y)
            {
                this.x = x;
                this.y = y;
            }

            public void MoverDerecha()
            {
                this.y += 1;
            }

            public void MoverIzquierda()
            {
                this.y -= 1;
            }

            public void MoverArriba()
            {
                this.x -= 1;
            }

            public void MoverAbajo()
            {
                this.x += 1;
            }

        }
        public class Tablero
        {
            private string[,] tablero;
            private Posicion posicion;
            private bool llegada = false;

            public bool Llegada { get { return llegada; } }

            public Tablero() 
            {
                tablero = new string[6, 6];

                for (int i = 0; i  < tablero.GetLength(0); i++)
                {
                    for (int j = 0; j < tablero.GetLength(1); j++)
                    {
                        tablero[i,j] = "_";
                    }
                }

                GeneraObstaculos();
                GeneraSalida();
                GeneraInicioMickey();
            }

            private void GeneraInicioMickey()
            {
                Random random = new Random();
                int fila, columna;

                do
                {
                    fila = random.Next(0, 5);
                    columna = random.Next(0, 5);
                } while (tablero[fila, columna] != "_");

                tablero[fila, columna] = "M";
                posicion = new Posicion(fila, columna);
            }

            private void GeneraSalida()
            {
                Random random = new Random();
                int fila, columna;

                do
                {
                    fila = random.Next(0, 5);
                    columna = random.Next(0, 5);
                } while (tablero[fila, columna] != "_");

                tablero[fila, columna] = "S";
            }

            private void GeneraObstaculos()
            {
                Random random = new Random();
                var numObstaculos = random.Next(6, 12);

                for (int i = 0; i < numObstaculos; i++)
                {
                    int fila, columna;

                    do
                    {
                        fila = random.Next(0, 5);
                        columna = random.Next(0, 5);
                    } while (tablero[fila, columna] != "_");

                    tablero[fila, columna] = "X";
                }
            }

            public void MuestraTablero()
            {
                Console.WriteLine("Leyenda:");
                Console.WriteLine("_ -> Hueco");
                Console.WriteLine("X -> Obstaculo");
                Console.WriteLine("M -> Mickey");
                Console.WriteLine("S -> Salida");
                Console.WriteLine("Tablero:");

                for (int i = 0; i < tablero.GetLength(0); i++)
                {
                    for (int j = 0; j < tablero.GetLength(1); j++)
                    {
                        Console.Write(tablero[i,j] + " ");
                    }

                    Console.WriteLine();
                }                
            }

            public bool MueveDerecha()
            {
                if (posicion.Y + 1 < tablero.GetLength(0))
                {
                    if (tablero[posicion.X, posicion.Y + 1] != "X")
                    {
                        if (tablero[posicion.X, posicion.Y + 1] == "S")
                        {
                            llegada = true;
                        }

                        tablero[posicion.X, posicion.Y] = "_";
                        tablero[posicion.X, posicion.Y + 1] = "M";
                        posicion.MoverDerecha();

                        return true;
                    }
                }

                return false;
            }

            public bool MueveIzquierda()
            {
                if (posicion.Y - 1 >= 0)
                {
                    if (tablero[posicion.X, posicion.Y - 1] != "X")
                    {
                        if (tablero[posicion.X, posicion.Y - 1] == "S")
                        {
                            llegada = true;
                        }

                        tablero[posicion.X, posicion.Y] = "_";
                        tablero[posicion.X, posicion.Y - 1] = "M";
                        posicion.MoverIzquierda();

                        return true;
                    }
                }

                return false;
            }

            public bool MueveArriba()
            {
                if (posicion.X - 1 >= 0)
                {
                    if (tablero[posicion.X - 1, posicion.Y] != "X")
                    {
                        if (tablero[posicion.X - 1, posicion.Y] == "S")
                        {
                            llegada = true;
                        }

                        tablero[posicion.X, posicion.Y] = "_";
                        tablero[posicion.X - 1, posicion.Y] = "M";
                        posicion.MoverArriba();

                        return true;
                    }
                }

                return false;
            }

            public bool MueveAbajo()
            {
                if (posicion.X + 1 < tablero.GetLength(1))
                {
                    if (tablero[posicion.X + 1, posicion.Y] != "X")
                    {
                        if (tablero[posicion.X + 1, posicion.Y] == "S")
                        {
                            llegada = true;
                        }

                        tablero[posicion.X, posicion.Y] = "_";
                        tablero[posicion.X + 1, posicion.Y] = "M";
                        posicion.MoverAbajo();

                        return true;
                    }
                }

                return false;
            }
        }
        static void Main(string[] args)
        {
            Tablero tablero = new Tablero();

            while (!tablero.Llegada)
            {
                tablero.MuestraTablero();
                Console.WriteLine("¿Hacia dónde quieres moverte?");
                Console.WriteLine("1. Derecha");
                Console.WriteLine("2. Izquierda");
                Console.WriteLine("3. Arriba");
                Console.WriteLine("4. Abajo");
                Console.Write("Opcion: ");
                var opcion = Int16.Parse(Console.ReadLine());

                switch (opcion)
                {
                    case 1:
                        if (!tablero.MueveDerecha())
                            Console.WriteLine(kMENSAJE);
                        break;
                    case 2:
                        if (!tablero.MueveIzquierda())
                            Console.WriteLine(kMENSAJE);
                        break;
                    case 3:
                        if (!tablero.MueveArriba())
                            Console.WriteLine(kMENSAJE);
                        break;
                    case 4:
                        if (!tablero.MueveAbajo())
                            Console.WriteLine(kMENSAJE);
                        break;
                    default:
                        Console.WriteLine("Opción incorrecta");
                        break;
                }
            }
            Console.WriteLine("¡Enhorabuena! Has ayudado a Mickey a escapar del laberinto");

            Console.ReadKey();
        }
    }
}
