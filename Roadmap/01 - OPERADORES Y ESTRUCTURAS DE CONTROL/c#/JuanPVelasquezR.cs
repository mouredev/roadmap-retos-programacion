// Operadores en C#-------------------------------------------------------------------------------------------------------

//Aritm�ticos

int a = 24, b = 54;
int suma = a + b;
int resta = a - b;
int multiplicaci�n = a * b;
float divisi�n = a / b;
float resto = a % b;


Console.WriteLine($@" a = 24, b = 54...
            Suma = a + b: {suma}
            Resta = a + b: {resta}
            Multiplicaci�n = a + b: {multiplicaci�n}
            Divisi�n = a + b: {divisi�n}
            Resto = a % b: {resto}");


// Operadores de Asignaci�n

// Operador de asignaci�n simple
int x = 78;

// Operador de Suma y Asignaci�n
x += 55;

// Operador de Resta y Asignaci�n
x -= 10;

// Operador de Multiplicaci�n y Asignaci�n
x *= 10;

// Operador de Divisi�n y Asignaci�n
x /= 10;


// Operadores de Comparaci�n 


// Es verdadero si ambos valores son iguales
Console.WriteLine(a == b);


// Es verdadero si los valores son diferentes
Console.WriteLine(a != b);

//Devuelve verdadero o falso si se cumple que el indicado sea el mayor o el menor
Console.WriteLine(a > b);
Console.WriteLine(a < b);

//Devuelve verdadero o falso si se cumple que el indicado sea el mayor, menor o igual
Console.WriteLine(a >= b);
Console.WriteLine(a <= b);



// Operadores l�gicos

bool c = true;

bool d = false;

// Devuelve verdadero si ambos comparandos son verdaderos, de lo contrario, devuelve falso
Console.WriteLine(c && d);

// Devuvelve verdadero de alguno de los dos operandos son verdadedros
Console.WriteLine(c || d);

// Es una negaci�n del operando, si el operando es falso, se vuelve verdadero, y viceversa
Console.WriteLine(!c);


// Operadores iterativos

// Analiza una condici�n dada, en caso de cumplirse aquella condici�n, ejecuta el bloque de c�digo que se define entre las llaves, si no se cumple, no se
// ejecuta, se puede definir que comportamiento tener en caso de no cumplirse

if (c)
{
    Console.WriteLine("La condici�n fue verdadera");
}
else
{
    Console.WriteLine("La condici�n fue falsa");


}

Console.WriteLine("Esto se ejecutar� sin importar el resultado de la condici�n");

/* Es posible generar una cadena de condicionales if, no solamene con una contraparte else, tambi�n se puede hacer uso del else if, sin  embargo 
 * generalmente en los casos en que se presentan varios if anidados, es m�s correcto usar un Switch Case*/

//Estructura de contro switch  --  Permite asignar acciones concretas en funci�n del valor de una variable.
//

int productoId = 2;

switch (productoId)
{

    case 1:
        Console.WriteLine("Man�");
        break;

    case 2:
        Console.WriteLine("Chocolate");
        break;

    case 3:
        Console.WriteLine("Soda");
        break;

}


// Estructuras de control iterativas

//Bucle for, es un bucle que se usa para que cierta accion se repita un numero determinado de veces, se usa cuando se conoce cual es el numero de veces que se debe repetir

for (int i = 0; i < 5; i++)
{

    Console.WriteLine($"Esta es la iteraci�n n�mero {i + 1}");
}


// Bucle ForEach, se usa para realizar una acci�n determinada, con la diferencia de que este se har� hasta que se recorran todos los elementos de la estrcutura utilizada
// Como un arreglo, una Lista...


int[] numeros = { 1, 2, 3, 4, 5, 6, };

foreach (int i in numeros)
{


    Console.WriteLine($"Acutualmente se est� recorriendo el �ndice: {i}");
}


// Estructura do y do while. La estructura do define una acci�n que se va a ejecutar, luego se a�ade a un bucle while, la cual puede ejecutarse o no, en funcion de si se cumple una condici�n. el do siempre se ejecuta almenos una vez

bool flag = true;

do
{

    int i = 0;
    Console.WriteLine($"Valor de i: {i}");
    i++;

    flag = false;

}
while (flag);




//Excepciones y Control de Excepci�n, generalmente se usan, para que al tener un error o un improvisto en la ejecuci�n del c�digo, no se termine
// la ejecuci�n, sino que, se pueda controlar, se pueden as� mismo, enviar nosotreos mismos estas excepciones o "Errores" cuando pase o se cumpla algo que definimos

float h = 0, n = 4;
try
{

    float resultado = n / h;

    Console.WriteLine(resultado);


}

catch (Exception e)
{
    Console.WriteLine("No se puede dividir entre 0");

}

// Tambi�n existe la opci�n finally, que se ejecutar� sin importar si entra en el cath o no








//---------------------------------------------------------------------------------------------------------------------------------------------

//DIFICULTAD EXTRA


for (int i = 10; i <= 55; i++)
{
    if (i % 2 == 0 && i != 16 && i % 3 == 0)
    { Console.WriteLine(i); }


}


        