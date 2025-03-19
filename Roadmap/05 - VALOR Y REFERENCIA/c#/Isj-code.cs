// En los tipo de datos primitivos la asignacion es por valor

int a = 10;
int a1 = a;
a1 = 11;

Console.WriteLine($"El valor de a es: {a}, el valor de a1 es: {a1}");

string palabraUno = "Uno";
string palabraDos = palabraUno;
palabraDos += ", dos";

Console.WriteLine($"La palabra uno es {palabraUno} y la palabra 2 es  {palabraDos}");

// En los tipos compuestos es por referencia

int[] numeros = {1,2,3,4,5};
int[] numeros2 = numeros;

Console.Write("El array numeros es: ");
foreach (var item in numeros)
{
    Console.Write($"{item} ");
}

Console.WriteLine("");
Console.WriteLine("Asignamos numeros2 = numeros1 y cambiamos la posicion 0 por el numero 0");
numeros2[0] = 0;

Console.Write("Ahora el array numeros es: ");
foreach (var item in numeros)
{
    Console.Write($"{item} ");
}

// Funciones con parametro por Valor

void FuncionPorValor(int numA)
{
    numA++;
    Console.WriteLine($"la variable global dentro a vale {numA}");
}

FuncionPorValor(a);
Console.WriteLine($"Despues de pasar por la funcion a vale {a}");

// Funcion con parametro por referencia

List<int> listaNumeros = [1,2,3,4,5];
Console.WriteLine("Lista de numero original");
foreach (var item in listaNumeros)
{
    Console.Write($"{item} ");
}

void FuncionPorReferencia(List<int> lista)
{
    for (int i = 0; i < lista.Count; i++)
    {
        lista[i] = lista[i] * 5;
    }
}

FuncionPorReferencia(listaNumeros);
// Transformamos la lista

Console.WriteLine("");
Console.WriteLine("Despues de multiplicar x 5");
foreach (var item in listaNumeros)
{
    Console.Write($"{item} ");
}

// ## Dificultad Extra
Console.WriteLine("");
int datoA = 5;
int datoB = 10;

Console.WriteLine($"Dato A original: {datoA}");
Console.WriteLine($"Dato B original: {datoB}");

int[] FuncionParaValor(int a1, int b1)
{
    int x = b1;
    b1 = a1;
    a1 = x;

    return [a1, b1];
}

int[] resp = FuncionParaValor(datoA, datoB);

Console.WriteLine($"Dato A devuelto por la funcion: {resp[0]}");
Console.WriteLine($"Dato B devuelto por la funcion: {resp[1]}");
Console.WriteLine($"Dato A original: {datoA}");
Console.WriteLine($"Dato B original: {datoB}");

int[] numerosA = [1,2];
int[] numerosB = [3,4];

Console.WriteLine($"La primera dupla original es {numerosA[0]} y {numerosA[1]}");
Console.WriteLine($"La segunda dupla original es {numerosB[0]} y {numerosB[1]}");

int[][] FuncionParaReferencia(int[] a1, int[] b1)
{
    int[] x = b1;
    b1 = a1;
    a1 = x;

    return [a1, b1];
}

int[][] numerosDevueltos = FuncionParaReferencia(numerosA, numerosB);
Console.WriteLine($"Los numeros devueltos en la primera dupla son {numerosDevueltos[0][0]} y {numerosDevueltos[0][1]}"); 
Console.WriteLine($"Los numeros devueltos en la segunda dupla son {numerosDevueltos[1][0]} y {numerosDevueltos[1][1]}");

Console.WriteLine($"La primera dupla original es {numerosA[0]} y {numerosA[1]}");
Console.WriteLine($"La segunda dupla original es {numerosB[0]} y {numerosB[1]}");