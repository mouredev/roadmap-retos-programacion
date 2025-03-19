using System;
using System.Collections.Generic;

namespace EjemploHerenciaYEmpresa
{
    // Parte 1: Herencia con Superclase Animal y Subclases Perro y Gato

    // Superclase Animal
    class Animal
    {

        public string Nombre { get; set; }

        public Animal(string nombre)
        {
            Nombre = nombre;
        }

        //Método virtual para el sonido del animal
        public virtual void HacerSonido()
        {
            Console.WriteLine("Sonido de animal");
        }
    }

    // Subclase Perro
    class Perro : Animal
    {
        public Perro (string nombre) : base(nombre) { }

        public override void HacerSonido()
        {
            Console.WriteLine($"{Nombre} dice: Guau");
        }
    }

    // Subclase Gato

    class Gato : Animal
    {
        public Gato(string nombre) : base(nombre) { }

        public override void HacerSonido()
        {
            Console.WriteLine($"{Nombre} dice Miau");
        }
    }

    // Parte 2: Jerarqía de una Empresa de Desarrollo

    // Superclase Empleado

    class Empleado 
    {
        public int Id { get; set; }
        public string Nombre { get; set; }

        public Empleado(int id nombre)
        {
            Id = id;
            Nombre = Nombre;
        }

        public virtual void MostrarInfo()
        {
            Console.WriteLine($"ID:{id}, Nombre: {Nombre}");
        }
    }

    // Subclase Gerente de Proyectos
    class Gerente : Empleado
    {
        public List<Empleado> EmpleadosAcargo { get; set; } = new List<Empleado>();
        public Gerente(int id, string nombre) : base(id, nombre) { }
        public override void MostrarInfo()
        {
            base.MostrarInfo();
            Console.WriteLine("Empleados a cargo: ");
            foreach (var empleado in EmpleadosAcargo)
            {
                Console.WriteLine($" - {empleado.Nombre}");
            }
        }
    }

    // Subclase Gerente de Proyectos
    class GerenteDeProyectos : Empleado
    {
        public List<Empleado> EmpleadosAcargo { get; set; } = new List<Empleado>();
        public  GerenteDeProyectos(int id, string nombre) : base(id, nombre) { }

        public override void MostrarInfo()
        {
            base.MostrarInfo();
            Console.WriteLine("Proyectos a cargo:");
            foreach(var empleado in EmpleadosAcargo)
            {
                Console.WriteLine($" - {empleado.Nombre}");
            }
        }
    }

    // Subclase Programador
    class Programador : Empleado
    {
        public string LenguajeDeProgramacion { get; set; }

        public Programador(in id, string nombre, string lenguaje) : base (id, nombre)
        {
            LenguajeDeProgramacion = lenguaje;
        }

        public override void MostrarInfo()
        {
            base.MostrarInfo();
            Console.WriteLine($"Lenguaje de programacion: {LenguajeDeProgramacion}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Parte 1: Uso de Animal, Perro y Gato
            Perro perro = new Perro("Rex");
            Gato gato = new Gato("Wiskers");

            perro.HacerSonido(); //Imprime " Rex dice: Guau"
            gato.HacerSonido();  // Imprime "Wiskers dice: Miau

            // Parte 2: Uso de Empleado, Gerente, GerenteDeProyectos y Programador
            Programador programador1 = new Programador(1, "Alice", "C#");
            Programador programador2 = new Programador(2, "Bob", "Java");
            GerenteDeProyectos gerenteDeProyectos = new GerenteDeProyectos(3, "Charlie");
            Gerente gerente = new Gerente(4, "Diana");

            // Asignar empleados a cargo
            gerenteDeProyectos.EmpleadosAcargo.Add(programador1);
            gerenteDeProyectos.EmpleadosAcargo.Add(programador2);
            gerente.EmpleadosAcargo.Add(gerenteDeProyectos);

            // Mostrar informacion de cada empleado
            programador1.MostrarInfo();
            programador2.MostrarInfo();
            gerenteDeProyectos.MostrarInfo();
            gerente.MostrarInfo();
        }
    }

  /*
Explicación 

- Parte 1: Herencia con Superclase Animal y Subclases Perro y Gato

Superclase Animal:
Define el atributo Nombre.
Tiene un constructor para inicializar Nombre.
Método virtual HacerSonido que puede ser sobrescrito por las subclases.

Subclase Perro:
Hereda de Animal.
Sobrescribe el método HacerSonido para imprimir "Guau".

Subclase Gato:
Hereda de Animal.
Sobrescribe el método HacerSonido para imprimir "Miau".

Programa Principal:
Crea instancias de Perro y Gato.
Llama al método HacerSonido para cada instancia.

- Parte 2: Jerarquía de una Empresa de Desarrollo

Superclase Empleado:
Define los atributos Id y Nombre.
Tiene un constructor para inicializar Id y Nombre.
Método virtual MostrarInfo para mostrar la información del empleado.

Subclase Gerente:
Hereda de Empleado.
Atributo EmpleadosACargo, una lista de empleados.
Sobrescribe el método MostrarInfo para mostrar información adicional de los empleados a cargo.
Subclase GerenteDeProyectos:

Hereda de Empleado.
Atributo EmpleadosACargo, una lista de empleados.
Sobrescribe el método MostrarInfo para mostrar información adicional de los proyectos a cargo.

Subclase Programador:
Hereda de Empleado.
Atributo LenguajeDeProgramacion.
Sobrescribe el método MostrarInfo para mostrar información adicional del lenguaje de programación.

Programa Principal:
Crea instancias de Programador, GerenteDeProyectos y Gerente.
Asigna empleados a cargo.
Llama al método MostrarInfo para cada instancia.

*/
}
