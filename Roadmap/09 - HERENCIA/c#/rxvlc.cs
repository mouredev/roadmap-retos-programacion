using System;
using System.Collections.Generic;

namespace R09___2024
{
    //Superclase
    class Animal
    {
        //Defino atributos Puedes poner protected (Es para que la clase heredera pueda manipular los atributos sin necesidad de propiedades/getters/setters)
        protected string nombre;
        int edad;

        public Animal(string nombre,int edad)
        {
            this.nombre = nombre;
            this.edad = edad;
        }
    }

    //Heredera perro:
    class Perro : Animal
    {
        public Perro(string nombre,int edad):base(nombre,edad){ }

        public void Sonido()
        {
            Console.WriteLine("guau guau!");
        }
    }

    //Heredera gato:
    class Gato : Animal
    {
        public Gato(string nombre, int edad) : base(nombre, edad) { }

        public void Sonido()
        {
            Console.WriteLine("miau miau!");
        }
    }

    //Dificultad adicional:
    // Clase base abstracta para representar a un empleado genérico
    class Empleado
    {
        // Defino atributos como protected (para que las clases heredadas puedan acceder directamente a ellos)
        protected int id;
        protected string nombre;

        // Constructor
        public Empleado(int id, string nombre)
        {
            this.id = id;
            this.nombre = nombre;
        }

        // Método virtual para obtener información del empleado
        public virtual void Informacion()
        {
            Console.WriteLine($"ID: {id}, Nombre: {nombre}");
        }
    }

    // Clase Gerente hereda de Empleado
    class Gerente : Empleado
    {
        // Lista de empleados a cargo
        protected List<Empleado> empleadosACargo;

        // Constructor
        public Gerente(int id, string nombre) : base(id, nombre)
        {
            empleadosACargo = new List<Empleado>();
        }

        // Método para agregar un empleado a su lista de empleados a cargo
        public void AgregarEmpleado(Empleado empleado)
        {
            empleadosACargo.Add(empleado);
        }

        // Sobrescribe el método de la clase base para incluir información adicional
        public override void Informacion()
        {
            base.Informacion();
            Console.WriteLine("Tipo: Gerente");
            Console.WriteLine($"Empleados a cargo: {empleadosACargo.Count}");
        }
    }

    // Clase GerenteProyecto hereda de Gerente
    class GerenteProyecto : Gerente
    {
        // Propiedad específica de un Gerente de Proyectos
        protected string areaProyecto;

        // Constructor
        public GerenteProyecto(int id, string nombre, string areaProyecto) : base(id, nombre)
        {
            this.areaProyecto = areaProyecto;
        }

        // Sobrescribe el método de la clase base para incluir información adicional
        public override void Informacion()
        {
            base.Informacion();
            Console.WriteLine($"Área del Proyecto: {areaProyecto}");
        }
    }

    // Clase Programador hereda de Empleado
    class Programador : Empleado
    {
        // Propiedad específica de un Programador
        protected string lenguaje;

        // Constructor
        public Programador(int id, string nombre, string lenguaje) : base(id, nombre)
        {
            this.lenguaje = lenguaje;
        }

        // Sobrescribe el método de la clase base para incluir información adicional
        public override void Informacion()
        {
            base.Informacion();
            Console.WriteLine($"Lenguaje: {lenguaje}");
        }
    }
    class Program
    {
        static void Main(string[] args)
        {

            // Creación de instancias de Perro y Gato
            Perro miPerro = new Perro("Bobby", 5);
            Gato miGato = new Gato("Whiskers", 3);

            // Llamada a los métodos específicos de cada clase
            miPerro.Sonido(); // Salida: ¡Guau Guau!
            miGato.Sonido(); // Salida: ¡Miau Miau!

            // Creación de instancias de empleados
            Gerente gerente1 = new Gerente(1, "Juan");
            GerenteProyecto gerenteProyecto1 = new GerenteProyecto(2, "María", "Desarrollo Web");
            Programador programador1 = new Programador(3, "Pedro", "C#");

            // Agregar empleados a cargo del gerente
            gerente1.AgregarEmpleado(gerenteProyecto1);
            gerenteProyecto1.AgregarEmpleado(programador1);

            // Mostrar información de los empleados
            Console.WriteLine("Información del Gerente:");
            gerente1.Informacion();
            Console.WriteLine("\nInformación del Gerente de Proyecto:");
            gerenteProyecto1.Informacion();
            Console.WriteLine("\nInformación del Programador:");
            programador1.Informacion();
        }
    }
}
