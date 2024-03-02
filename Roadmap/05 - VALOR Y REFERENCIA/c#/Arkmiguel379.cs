// ======= ASIGNACION POR VALOR =======

Console.WriteLine("=== ASIGNACION POR VALOR === \n");

int x = 5;
int y = x;

Console.WriteLine(x); // Salida: 5 (Valor de la variable original)
Console.WriteLine(y); // Salida: 5 (Es la copia de la variable original)

y = 10;

Console.WriteLine(x); // Salida: 5 (La variable original no cambia)
Console.WriteLine(y); // Salida: 10 (El valor de la copia de la variable cambia sin afectar el valor de la variable original)

Console.WriteLine();

// ==================================

string cadena = "C Sharp";
string cadena2 = cadena;

Console.WriteLine(cadena); // Salida: C Sharp (Valor de la variable original)
Console.WriteLine(cadena2); // Salida: C Sharp (Es la copia de la variable original)

Console.WriteLine();

cadena2 = "Python";

Console.WriteLine(cadena); // Salida: C Sharp (La variable original no cambia)
Console.WriteLine(cadena2); // Salida: Python (El valor de la copia de la variable cambia sin afectar el valor de la variable original)

Console.WriteLine();


// ======= ASIGNACION POR REFERENCIA =======

Console.WriteLine("=== ASIGNACION POR REFERENCIA === \n");

int[] array1 = {1,2,3,4,5};

int[] array2 = array1;

foreach (var i in array1)
{
    Console.WriteLine(i); // Salida: 1 2 3 4 5 (Valores del arreglo original)
}

Console.WriteLine();

foreach (var i in array2) // Salida: 1 2 3 4 5 (Valores de la copia del arreglo original)
{
    Console.WriteLine(i);
}

Console.WriteLine();

array2[0] = 33; // Se cambia el valor del indice 0 de la copia del arreglo original

foreach (var i in array1)
{
    Console.WriteLine(i); // Salida: 33 2 3 4 5 (El valor del indice 0 del arreglo original ha sido modificado
}                         // a causa de la modificacion hecha en la copia)

Console.WriteLine();

foreach (var i in array2)
{
    Console.WriteLine(i); // Salida: 33 2 3 4 5 (Valores del arreglo que se modificó directamente)
}

Console.WriteLine();

// =======================

List<string> list = new List<string> {"Lobo", "Koala", "Leopardo", "Caballo"};

Console.WriteLine("Valores de la lista original \n");

foreach (var i in list)  // Valores de la lista original
{
    Console.WriteLine(i);
}

Console.WriteLine();

List<string> list2 = list;

Console.WriteLine("Valores de la segunda lista, una copia de la primera \n");

foreach (var i in list2) // Valores de la segunda lista, siendo esta una copia de la primera
{
    Console.WriteLine(i);
}

Console.WriteLine();

list2[0] = "Tiburon";  // Se modifica el indice 0 de la segunda lista

Console.WriteLine("Valores de la segunda lista, modificando el indice 0 \n");

foreach (var i in list2) // Valores de la segunda lista, con el indice 0 modificado directamente
{
    Console.WriteLine(i);
}

Console.WriteLine();

Console.WriteLine("Valores de la lista original pero con el indice 0 modificado mediante la segunda lista \n");

foreach (var i in list) // El indice 0 de la primera lista es afectado por la modificacion hecha a la segunda lista
{
    Console.WriteLine(i);
}

Console.WriteLine();


// ======= FUNCIONES CON PARAMETROS POR VALOR =======

Console.WriteLine("=== FUNCIONES CON PARAMETROS POR VALOR === \n");

int z = 3;

Console.WriteLine($"El valor de Z es: {z}"); // Valor de la variable original

ValorIntModificado(z); // Funcion que modifica el valor de la variable e imprime su nuevo valor

Console.WriteLine($"El valor de Z despues de la llamada de la funcion es: {z}"); // Valor de la variable original despues de que la funcion
                                                                                 // haya "modificado su valor"

Console.WriteLine();

// =====================

string c = "Hola mundo"; 

Console.WriteLine($"El valor de C es: {c}"); // Valor de la variable original

ValorStrModificado(c); // Funcion que modifica el valor de la variable e imprime su nuevo valor

Console.WriteLine($"El valor de C despues de la llamada de la funcion es: {c}"); // Valor de la variable original despues de que la funcion
                                                                                 // haya "modificado su valor"

Console.WriteLine();


// ======= FUNCIONES CON PARAMETROS POR REFERENCIA =======

Console.WriteLine("=== FUNCIONES CON PARAMETROS POR REFERENCIA === \n");

List<int> ints = new List<int> {5, 6, 7, 8, 9};

Console.WriteLine("Los valores de la lista ints son: \n");

foreach (int i in ints) // Valores de la lista original
{
    Console.WriteLine(i);
}

Console.WriteLine();

ReferenciaIntModificada(ints, 0, 333); // Funcion que modifica el valor del indice indicado e imprime su nuevo valor

Console.WriteLine();

foreach (int i in ints) // Valores de la lista original despues de la llamada de la funcion
{
    Console.WriteLine(i);
}

Console.WriteLine();


// ====== METODOS ======
void ValorStrModificado(string parS)
{
    parS = "Cadena Modificada";
    Console.WriteLine($"El valor modificado del parametro es {parS}");
}
void ValorIntModificado(int parI)
{
    parI = 9;
    Console.WriteLine($"El valor modificado del parametro es: {parI}");
};

void ReferenciaIntModificada(List<int> parI, int indice, int newValue)
{
    parI[indice] = newValue;
    Console.WriteLine($"El nuevo valor del indice {indice} es: {parI[indice]}");
}


// ===== EXTRA =====

// Programa de parametros por valor

int var1 = 3;
int var2 = 9;

var retorno = ProgramValue(var1, var2);

int varD1 = retorno.Item1;
int varD2 = retorno.Item2;

Console.WriteLine($"El valor de var1 es: {var1}");
Console.WriteLine($"El valor de var2 es: {var2}");
Console.WriteLine();
Console.WriteLine($"El valor de varD1 es: {varD1}");
Console.WriteLine($"El valor de varD2 es: {varD2}");

Console.WriteLine();

// Programa de parametros por referencia

List<string> lista1 = new List<string> {"Bicicleta", "Moto", "Carro","Avion"};

List<string> lista2 = new List<string> { "Gato", "Perro", "Leopardo", "Aguila" };

var returnStr = ProgramParameter(lista1[0], lista2[3]);

string strD1 = returnStr.Item1;
string strD2 = returnStr.Item2;

Console.WriteLine($"El valor del indice lista1[0] que antes era {lista1[0]} ahora es {strD1}");
Console.WriteLine($"El valor del indice lista2[3] que antes era {lista2[3]} ahora es {strD2}");

// =====================================


(int, int) ProgramValue(int parameter1, int parameter2)
{
    int store = parameter1;
    parameter1 = parameter2;
    parameter2 = store;

    return (parameter1, parameter2);
}

(string, string) ProgramParameter(string parameter1, string parameter2)
{
    string store = parameter1;
    parameter1 = parameter2;
    parameter2 = store;

    return (parameter1, parameter2);
}