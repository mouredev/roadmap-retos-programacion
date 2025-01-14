// Author: Nicolas Tapia -> https://www.github.com/nicolastapiasanz

// EXERCISE #01

/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

public class Program
{
    private const int FirstValue = 10;
    private const int SecondValue = 5;

    public static void Main(string[] args)
    {
        Console.WriteLine("Operadores Aritmeticos");

        var suma = FirstValue + SecondValue;
        Console.WriteLine($"Suma {FirstValue} + {SecondValue} = {suma}"); //15

        var resta = FirstValue - SecondValue;
        Console.WriteLine($"Resta {FirstValue} - {SecondValue} = {resta}"); //5

        var multiplicacion = FirstValue * SecondValue;
        Console.WriteLine($"Multiplicación {FirstValue} * {SecondValue} = {multiplicacion}"); //50

        var division = FirstValue / SecondValue;
        Console.WriteLine($"Division {FirstValue} / {SecondValue} = {division}"); //2

        var resto = 1 % 1;
        Console.WriteLine($"Resto {FirstValue} % {SecondValue} = {resto}"); //0



        Console.WriteLine($"\nOperadores Lógicos");
        var and = true && true;
        Console.WriteLine($"AND True && True = {and}"); //True

        var or = true || false;
        Console.WriteLine($"OR True || False = {or}"); //True

        var not = !true;
        Console.WriteLine($"NOT !True = {not}"); //False



        Console.WriteLine($"\nOperadores Comparación");

        var igual = FirstValue == SecondValue;
        Console.WriteLine($"Igual {FirstValue} == {SecondValue} = {igual}"); //False

        var distinto = FirstValue != SecondValue;
        Console.WriteLine($"Distinto {FirstValue} != {SecondValue} = {distinto}"); //True

        var mayorQue = FirstValue > SecondValue;
        Console.WriteLine($"Mayor Que {FirstValue} > {SecondValue} = {mayorQue}"); //True

        var menorQue = FirstValue < SecondValue;
        Console.WriteLine($"Menor Que {FirstValue} < {SecondValue} = {menorQue}"); //False

        var mayorIgualQue = FirstValue >= SecondValue;
        Console.WriteLine($"Mayor O Igual Que {FirstValue} >= {SecondValue} = {mayorIgualQue}"); //True

        var menorIgualQue = FirstValue <= SecondValue;
        Console.WriteLine($"Menor O Igual Que {FirstValue} <= {SecondValue} = {menorIgualQue}"); //False



        Console.WriteLine($"\nOperadores De Asignación");

        var asignacion = FirstValue;
        Console.WriteLine($"Asignacion {FirstValue} = {asignacion}"); //10

        var masMas = FirstValue;
        masMas++;
        Console.WriteLine($"Mas Mas Post {FirstValue}++ = {masMas}"); //11
        ++masMas;
        Console.WriteLine($"Mas Mas Prev ++{FirstValue} = {masMas}"); //12

        var menosMenos = FirstValue;
        menosMenos--;
        Console.WriteLine($"Menos Menos Post {FirstValue}-- = {menosMenos}"); //9
        --menosMenos;
        Console.WriteLine($"Menos Menos Prev --{FirstValue} = {menosMenos}"); //8

        var masIgual = FirstValue;
        masIgual += 1;
        Console.WriteLine($"Mas Igual {FirstValue}+= 1 = {masIgual}"); //11

        var menosIgual = FirstValue;
        menosIgual -= 1;
        Console.WriteLine($"Menos Igual {FirstValue}-= 1 = {menosIgual}"); //9

        var multIgual = FirstValue;
        multIgual *= 2;
        Console.WriteLine($"Mult. Igual {FirstValue}*= 2 = {multIgual}"); //20

        var divIgual = FirstValue;
        divIgual /= 2;
        Console.WriteLine($"Div. Igual {FirstValue}/= 2 = {divIgual}"); //5

        var restIgual = FirstValue;
        restIgual %= 2;
        Console.WriteLine($"Rest. Igual {FirstValue}%= 2 = {restIgual}"); //0



        Console.WriteLine($"\nOperadores De Identidad");
        var firstValue1 = FirstValue;
        var firstValue2 = FirstValue;
        var porValor = firstValue1 == firstValue2;
        Console.WriteLine($"Comp. por valor: {firstValue1} == {firstValue2} = {porValor}"); //True

        var porReferencia = object.ReferenceEquals(firstValue1, firstValue2);
        Console.WriteLine($"Comp. por valor: {firstValue1}.Equals({firstValue2}) = {porReferencia}"); //False


        //OPERADORES DE BITS
        Console.WriteLine($"\nOperadores Binarios");
        var a = 75; // 0100 1011
        var b = 28; // 0001 1100

        var andOperation = a & b;
        Console.WriteLine($"AND {a} & {b} = {andOperation}"); //8 = 0000 1000

        var orOperation = a | b; //95 = 1010 1111
        Console.WriteLine($"OR {a} | {b} = {orOperation}"); //95 = 1010 1111

        var xorOperation = a ^ b;
        Console.WriteLine($"XOR {a} ^ {b} = {xorOperation}"); //87 = 0101 0111

        var notOperation = ~a;
        Console.WriteLine($"NOT ~{a} = {notOperation}"); //-76 = 1011 0100

        var despIzqOperation = a << 2;
        Console.WriteLine($"Desp. a la izquierda {a} << 2 = {despIzqOperation}"); //300 = 0001 0010 1100

        var despDerOperation = a >> 2;
        Console.WriteLine($"Desp. a la derecha {a} >> 2 = {despDerOperation}"); //18 = 0001 0010


        Console.WriteLine($"\nCondicionales");
        if (a > b)
        {
            Console.WriteLine($"a > b");
        }
        else if( b < a)
        {
            Console.WriteLine($"b < a");
            
        }
        else
        {
            Console.WriteLine($"b == a");
        }

        switch (a)
        {
            case 75:
                Console.WriteLine($"a == 75");
                break;
            default:
                Console.WriteLine($"a != 75");
                break;
        }

        Console.WriteLine($"\nIterativos");
        var i = 0;
        do
        {
            Console.Write($"{i} ");
            i++;
        } while (i != 10);

        Console.WriteLine();

        var f = 0;
        while(f != 10)
        {
            Console.Write($"{f} ");
            f++;
        }

        Console.WriteLine();

        for (var j = 0; j < 10; j++)
        {
            Console.Write($"{j} ");
        }

        Console.WriteLine();

        var values = Enumerable.Range(0, 10).ToList();
        foreach (var value in values)
        {
            Console.WriteLine($"{value}");
        }


        Console.WriteLine($"\nExcepciones");
        try
        {
            if (a != 75)
                throw new Exception($"EXCEPTION: a != 75");
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }


        //EJERCICIO EXTRA

        //NORMAL
        for (var x = 10; x < 56; x++)
            Console.Write($"{(x % 2 == 0 && x != 16 && x % 3 != 0 ? $"{x.ToString()}\n" : string.Empty)}");

        Console.WriteLine();

        //LINQ
        Enumerable.Range(10, 56 - 10)
            .Where(x => x % 2 == 0 && x != 16 && x % 3 != 0).ToList()
            .ForEach(Console.WriteLine);
    }
}