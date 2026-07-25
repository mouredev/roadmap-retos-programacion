// Funcion sin parametros ni retorno.
void SinParametros()
{
    Console.WriteLine("Esto es una función sin valores ni retorno.");
}

SinParametros();

// Función con dos parametros y retorno.
int area = CalcularAreaRectangulo(10, 5);
Console.WriteLine($"El area es: {area}");

int CalcularAreaRectangulo(int bas, int alt) 
{
    return bas * alt;
}

// Otra función un poco mas compleja.
Usuario("Iván",21);
Usuario("Alfonso",8);
void Usuario(string nombre, int edad)
{
    Console.WriteLine($"Hola, {nombre} tienes {edad} años.");
    
    if (edad < 18)
    {
        int contador = 0;
        for (int i = edad; i < 18; i++ )
        {
            contador++;
        }
        Console.WriteLine($"A este usuario todavía le faltan {contador} para ser mayor de edad.");  
        
    } 
    else
    {
        Console.WriteLine("Este usuario es mayor de edad");
    }
}

// Comprueba si puedes crear una función dentro de una función.

void Padre()
{
    void Hijo()
    {
        Console.WriteLine("Hola Soy una función llamada Hijo que esta dentro de una llamada Padre.");
    }
    Hijo();
}
Padre();

Console.WriteLine("Inserta un valor: ");
Console.ReadLine();
//Console.Clear() (Limpia la pantalla de la terminal.)
Math.Round(1.23454, 2); //Redondea un número a los decimales que le pidas (vital para facturación).
Math.Max(1, 100); //Te devuelve el número más grande entre dos valores.
Math.Abs(-20); //Devuelve el valor absoluto (convierte negativos en positivos).



// - Pon a prueba el concepto de variable LOCAL y GLOBAL.

// variable Local:

void EdadLocal()
{
    int edadLocal = 10;
    Console.WriteLine(edadLocal);
}

EdadLocal();



Usuario usuario1 = new Usuario();
usuario1.Nombre();
usuario1.Edad();


Producto producto1 = new();
producto1.MostrarInfo();


// Ejecucion del Ejercicio Extra.
Console.WriteLine("---------Ejercicio Extra-------------");

RetornoParam("Iván", "Calero");

Console.WriteLine("---------Fin----------");
int RetornoParam(string nombre, string apellido)
{
    int contador = 0;
    for (int i = 1; i <= 100; i++)
    {
        

        if (i % 3 == 0  && i % 5 == 0)
        {
            Console.WriteLine(nombre + apellido);
        } 
        else if (i % 3 == 0)
        {
            Console.WriteLine(nombre);
        }
        else if (i % 5 == 0)
        {
            Console.WriteLine(apellido);
        }
        else
        {
            Console.WriteLine(i);
            contador++;
        }
    }
    return contador;
}
// Global
class Usuario
{
    int edadGlobal = 21;
    string nombreUsuario = "Iván";
    public void Edad()
    {
        Console.WriteLine(edadGlobal);
    }
    public void Nombre()
    {
        Console.WriteLine(nombreUsuario);
    }
}

class Producto
{
    int idProducto = 1;
    string nombreProducto = "Camiseta";
    public void MostrarInfo()
    {
        Console.WriteLine(idProducto);
        Console.WriteLine(nombreProducto);
    }
}
