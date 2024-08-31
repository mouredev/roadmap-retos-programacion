//====================== FUNCIONES ============================

// Funcion sin valor de retorno y sin parametros

void Saludar()
{
    Console.WriteLine("Hola mundo");
}

Saludar();

// Funcion con retorno sin parametros

int ObtenerNumero()
{
    return 379;
}

Console.WriteLine(ObtenerNumero());

//Funcion sin valor de retorno con parametros

void Mensaje(string mensaje)
{
    Console.WriteLine(mensaje);
}

Mensaje("Logan");

// Funcion con retorno y parametros

int Suma(int a, int b)
{
    return a + b;
}

Console.WriteLine(Suma(5, 3));

// Funcion con paremetros opcionales o predeterminados

void Informacion(string nombre, int edad, int categoria = 0)
{
    Console.WriteLine($"Nombre: {nombre}, Edad: {edad}, Categoria: {categoria}");
}

Informacion("Miguel", 28);

// Funciones con parametros de salida

int value1 = 10;
int value2 = 2;
int resultadocociente;
int resultadoresto;

void ResultadoDivision(int dividendo, int divisor, out int cociente, out int resto)
{
    cociente = dividendo / divisor;
    resto = dividendo % divisor;    
}

ResultadoDivision(value1, value2, out resultadocociente, out resultadoresto);

Console.WriteLine($"El resultado de la division es {resultadocociente}\nY el resto es {resultadoresto}");


//==================== FUNCIONES DENTRO DE FUNCIONES =============================

void FuncionExterna()
{
    Console.WriteLine("Inicio de la funcion externa");

    void FuncionInterna()
    {
        Console.WriteLine("Ejecucion de la funcion interna");
    }

    FuncionInterna();

    Console.WriteLine("Fin de la funcion externa");
}

FuncionExterna();

//======================= FUNCIONES DEL SISTEMA =============================

int numero = Convert.ToInt32("97"); // <-- Funcion para convertir a INT algún valor

string cadena = Convert.ToString("257"); // <-- Funcion para convertir a STRING algún valor

string mayusculas = "palabra".ToUpper(); // <-- Funcion para pasar a mayusculas todas las letras de una cadena
Console.WriteLine(mayusculas);

string minusculas = "FRASE PARA CAMBIAR A MINUSCULAS".ToLower(); // <-- Funcion para pasar a minusculas todas las letras de una cadena
Console.WriteLine(minusculas);

int[] funcionSuma = {2,4,6,8,10};
int suma = funcionSuma.Sum(); // <-- Funcion para sumar los valores dentro de una coleccion de valores

Console.WriteLine(suma);

DateTime hoy = DateTime.Now;
Console.WriteLine(hoy);

int año = hoy.Year;
Console.WriteLine(año);

//=============================== EXTRA ======================================

int funcionE(string str1, string str2)
{
    int contador = 0;

    for (int i = 1; i <= 100; i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
        {
            Console.WriteLine($"{str1} + {str2}");
        }
        else if (i % 3 == 0)
        {
            Console.WriteLine(str1);
        }
        else if (i % 5 == 0) 
        { 
            Console.WriteLine(str2);
        }
        else
        {
            Console.WriteLine(i);
            contador++;
        }
    }

    return contador;
}

funcionE("Primera cadena", "Segunda cadena");