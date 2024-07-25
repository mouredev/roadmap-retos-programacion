// El WriteLine es una función ya creada en el lenguaje.
// Variables globales
int num1 = 4;
int num2 = 5;

// Función sin retorno ni parámetro
void FuncionSinParametro()
{
    Console.WriteLine("Pues eso, no te devuelvo nada");
}

FuncionSinParametro();

void FuncionConParametros(int a, int b)
{
    int suma = a + b;
    Console.WriteLine($"La suma de a y b es: {suma}");
}

FuncionConParametros(3, 5);

// En el ejemplo anterior se muestra el Scope de la variable Local
// Esto marca error ya que intentamos imprimir una variable local del método anterior.
// Console.WriteLine(suma);

string FuncionQueTeSaluda(string nombre)
{
    return $"¡¡Hola {nombre}!!";
}

Console.WriteLine(FuncionQueTeSaluda("José"));

// Funcion dentro de funcion

void FuncionConFunciones(string nombre)
{
    // Mas funciones del Lenguaje que quitan espacios al principio, final y alacance de variables
    
    void LongitudDeNombre()
    {
        int longitud = nombre.TrimStart().TrimEnd().Length;
        Console.WriteLine($"Tu nombre tiene {longitud} carácteres");
    }

    void PrimeraLetra()
    {
        string nombreSinEspacios = nombre.TrimStart().TrimEnd();
        char letra = nombreSinEspacios[0];
        Console.WriteLine($"La primera letra de tu nombre es {letra}");
    }
    
    LongitudDeNombre();
    PrimeraLetra();
}

FuncionConFunciones(" José ");

// OPCIONAL

int DificultadExtra(string a, string b)
{
    int conteoNum = 0;

    for (int i = 1; i <= 100; i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
        {
            Console.WriteLine($"{a}, {b}");
        }
        else if (i % 3 == 0)
        {
            Console.WriteLine(a);
            
        }
        else if(i % 5 == 0 )
        {
            Console.WriteLine(b);
        }
        else
        {
            Console.WriteLine(i);
            conteoNum++;
        }
    }
    
    return conteoNum;
}


Console.WriteLine(DificultadExtra("Multiplo de 3", "Multiplo de 5"));