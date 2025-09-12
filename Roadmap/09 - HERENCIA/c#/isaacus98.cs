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

namespace Roadmap
{
    internal class Reto09
    {
        static void Main(string[] args)
        {
            Perro perro = new("perro", "guau");
            Gato gato = new("gato", "miau");

            perro.ImprimirSonido();
            gato.ImprimirSonido();

            // Reto extra
            Programador programador1 = new(1, "Isaac", "C#");
            Programador programador2 = new(2, "Sergi", "Java");
            Programador programador3 = new(3, "Gerard", "Kotlin");
            Programador programador4 = new(4, "Pol", "C#");
            Programador programador5 = new(5, "Josep", "Java");
            Programador programador6 = new(6, "Guillem", "Kotlin");
            programador1.Trabajar();
            programador2.Trabajar();
            programador3.Trabajar();
            programador4.Trabajar();
            programador5.Trabajar();
            programador6.Trabajar();

            GerenteProyectos gerenteProyectos1 = new(7, "Joan", "App C#");
            gerenteProyectos1.Add(programador1);
            gerenteProyectos1.Add(programador4);
            gerenteProyectos1.Trabajar();
            gerenteProyectos1.EmpleadosACargo();

            GerenteProyectos gerenteProyectos2 = new(8, "Max", "App Java");
            gerenteProyectos2.Add(programador2);
            gerenteProyectos2.Add(programador5);
            gerenteProyectos2.Trabajar();
            gerenteProyectos2.EmpleadosACargo();

            GerenteProyectos gerenteProyectos3 = new(9, "Nuria", "App Kotlin");
            gerenteProyectos3.Add(programador3);
            gerenteProyectos3.Add(programador6);
            gerenteProyectos3.Trabajar();
            gerenteProyectos3.EmpleadosACargo();


            Gerente gerente = new(10, "Ricard");
            gerente.Add(gerenteProyectos1);
            gerente.Add(gerenteProyectos2);
            gerente.Add(gerenteProyectos3);
            gerente.Trabajar();
            gerente.EmpleadosACargo();

        }
    }

    public class Animal
    {
        protected string Especie;
        protected string Sonido;

        public Animal(string especie, string sonido)
        {
            Especie = especie;
            Sonido = sonido;
        }

        public void ImprimirSonido()
        {
            Console.WriteLine($"El {Especie} hace {Sonido}");
        }
    }

    public class Perro(string especie, string sonido) : Animal(especie, sonido) { }

    public class Gato(string especie, string sonido) : Animal(especie, sonido) { }

    // Reto extra

    public abstract class Empleado
    {
        public readonly int Id;
        public readonly string Nombre;

        protected Empleado(int id, string nombre)
        {
            Id = id;
            Nombre = nombre;
        }
    }

    public class Gerente : Empleado
    {
        private List<GerenteProyectos> GerentesProyecto;
        public Gerente(int id, string nombre) : base(id, nombre) 
        {
            GerentesProyecto = new List<GerenteProyectos>();
        }

        public void Add(GerenteProyectos gerenteProyectos) => GerentesProyecto.Add(gerenteProyectos);
        public void Trabajar() => Console.WriteLine($"El gerente {Nombre} gestiona todos los proyectos.");
        public void EmpleadosACargo()
        {
            Console.WriteLine($"El gerente {Nombre} tiene los siguiente empleados a su cargo:");
            foreach (GerenteProyectos gerenteProyectos in GerentesProyecto)
            {
                Console.WriteLine(gerenteProyectos.Nombre);
            }
        }
    }

    public class GerenteProyectos : Empleado
    {
        private List<Programador> Programadores;
        private string Proyecto;
        public GerenteProyectos(int id, string nombre, string proyecto) : base(id, nombre) 
        {
            Proyecto = proyecto;
            Programadores = new List<Programador>();    
        }

        public void Add(Programador programador) => Programadores.Add(programador);
        public void Trabajar() => Console.WriteLine($"El gerente de proyecto {Nombre} gestiona el proyecto {Proyecto}.");
        public void EmpleadosACargo()
        {
            Console.WriteLine($"El gerente de proyecto {Nombre} tiene los siguiente empleados a su cargo:");
            foreach (Programador programador in Programadores)
            {
                Console.WriteLine(programador.Nombre);
            }
        }
    }

    public class Programador : Empleado
    {
        private string Lenguaje;

        public Programador(int id, string nombre, string lenguage) : base(id, nombre) 
        {
            Lenguaje = lenguage;
        }

        public void Trabajar() => Console.WriteLine($"El programador {Nombre} programa con el lenguaje de programación {Lenguaje}");
    }
}
