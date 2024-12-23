using System;
class Program
{
    static void Main()
    {
        Videogame videogame1 = new Videogame("Lies Of Pi", 2023, "Souls");
        Videogame videogame2 = new Videogame("Sekiro", 2019, "Souls");
        Videogame.Conteo();
    }
}
class Videogame
{
    public string Nombre { get; set; }
    public int Lanzamiento { get; set; }
    public string Genero { get; set; }
    public static int Total = 0;
    /*Dado que el campo Total debe mantener un conteo compartido 
     * entre todas las instancias de la clase Videogame, 
     * este debe ser un miembro estático. De lo contrario, 
     * cada instancia tendrá su propio Total y el conteo no funcionará correctamente. 
     */
    
    public Videogame (string nombre, int lanzamiento, string genero)
    {
        Nombre = nombre;
        Lanzamiento = lanzamiento;
        Genero = genero;
        Total += 1;
    }
    public static void Conteo()
    {
        Console.WriteLine($"Tienes {Total} videojuegos en la bibilioteca");
    }
}
