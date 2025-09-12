/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

 using System.ComponentModel.Design;

namespace AppParaRetos
{
    public class estuardodev
    {
        public static void Main(string[] args)
        {
            Animal perro = new Perro("Firulais", 5);
            Animal gato = new Gato("Garfield", 3);

            perro.Ruido();
            gato.Ruido();

            Empleado gerente = new Gerenete("Estuardo", "Gerente");
            Console.WriteLine($"El empleado {gerente.nombre} con puesto de {gerente.puesto} con identificador {gerente.getIdentificador()}");
            gerente.Laborar();

            Empleado gerenteProyecto = new GerenteProyecto("Estuardo", "Gerente de Proyecto");
            Console.WriteLine($"El empleado {gerenteProyecto.nombre} con puesto de {gerenteProyecto.puesto} con identificador {gerenteProyecto.getIdentificador()}");
            gerenteProyecto.Laborar();

            Empleado programador = new Programador("Estuardo", "Programador");
            Console.WriteLine($"El empleado {programador.nombre} con puesto de {programador.puesto} con identificador {programador.getIdentificador()}");
            programador.Laborar();
        }
    }

    public abstract class Animal
    {
        public string Nombre { get; set; }
        public int anios { get; set; }

        public Animal(string Nombre, int anios)
        {
            this.Nombre = Nombre;
            this.anios = anios;
        }

        public virtual void Ruido()
        {
            Console.WriteLine("Hace ruido");
        }
    }

    public class Perro : Animal
    {
        public Perro(string Nombre, int anios) : base(Nombre, anios){ }

        public override void Ruido()
        {
            Console.WriteLine("Hace guau");
        }
    }

    public class Gato : Animal
    {
        public Gato(string Nombre, int anios) : base(Nombre, anios) { }

        public override void Ruido()
        {
            Console.WriteLine("Hace miau");
        }
    }

    public abstract class Empleado
    {
        public string nombre { get; set; }
        private string identificador = "";
        public string puesto { get; set; }

        public Empleado(string nombre, string puesto)
        {
            this.nombre = nombre;
            this.puesto = puesto;
        }

        public string getIdentificador()
        {
            string concat = nombre.ToLower().Replace(" ", "").Trim() + puesto.ToLower().Replace(" ", "").Trim();
            int size = concat.Length;
            Random random = new Random();

            for (int i = 0; identificador.Length < 7 ; i++)
            {
                
                int num = random.Next(0, size);
                if (!identificador.Contains(concat[num].ToString()))
                {
                    identificador += concat[num];
                }
                
            }

            return identificador;
        }

        public virtual void Laborar()
        {
            Console.WriteLine("Laborando");
        }
    }

    public class Gerenete : Empleado
    {
        public Gerenete(string nombre, string puesto) : base(nombre, puesto) { }

        public override void Laborar()
        {
            Console.WriteLine("Dirigiendo");
        }
    }

    public class GerenteProyecto : Empleado
    {
        public GerenteProyecto(string nombre, string puesto) : base(nombre, puesto) { }

        public override void Laborar()
        {
            Console.WriteLine("Planificando");
        }
    }

    public class Programador : Empleado
    {
        public Programador(string nombre, string puesto) : base(nombre, puesto) { }

        public override void Laborar()
        {
            Console.WriteLine("Programando");
        }
    }
}
