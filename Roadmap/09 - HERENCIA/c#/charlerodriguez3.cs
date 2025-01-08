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

 Animal gato1 = new Gato("Marcelo",4,"lamer patas","leche");
Animal perro1 = new Perro("Max",10,"Lucas");

gato1.EmitirSonido();
perro1.EmitirSonido();


class Animal
{
    public int Edad { get; set; }
    public string Nombre { get; set; }


    public Animal(string nombre, int edad)
    {
        Nombre = nombre;
        Edad = edad;
    }
    public virtual void EmitirSonido()
    {
        Console.WriteLine("Sonido de animal predeterminado");
    }
}

class Gato : Animal
{
    public string ActividadFavorita { get; set; }

    public string Bebida { get; set; }
    public Gato(string nombre, int edad, string actividadFavorita, string bebida) : base(nombre, edad)
    {
        ActividadFavorita = actividadFavorita;
        Bebida = bebida;
    }
    public override void EmitirSonido()
    {
        Console.WriteLine("Miau miau");
    }
}


class Perro : Animal
{
    public string AmoPreferido { get; set; }
    public Perro(string nombre, int edad, string amoPreferido) : base(nombre, edad)
    {
        AmoPreferido = amoPreferido;
    }
    public override void EmitirSonido()
    {
        Console.WriteLine("Guau guau");
    }
}
