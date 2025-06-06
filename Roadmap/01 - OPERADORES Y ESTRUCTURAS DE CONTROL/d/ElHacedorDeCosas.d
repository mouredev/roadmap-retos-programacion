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

void main()
{
    import std.stdio: writeln;

    // - Operadores - //
    writeln("\n___Operadores___");

    float a = 70f;
    float b = 30f;
    writeln("a = ", a, ", b = ", b);

    // Operadores aritmeticos
    writeln("Suma: a + b = ", (a + b));
    writeln("Resta: a - b = ", (a - b));
    writeln("Multiplicación: a * b = ", (a * b));
    writeln("División: a / b = ", (a / b));
    writeln("Resto: a % b = ", (a % b));
    writeln("Exponencial: a^^b = ", cast(int)(a^^b));
    writeln("Exponencial: a^^b = ", (a^^b));
    writeln("Incremento: ++a = ", (++a));
    writeln("Decremento: --b = ", (--b));

    // Operadores de comparación
    writeln("Igual: a == b = ", (a == b));
    writeln("Distinto: a != b = ", (a != b));
    writeln("Mayor: a > b = ", (a > b));
    writeln("Menor: a < b = ", (a < b));
    writeln("Mayor o igual: a >= b = ", (a >= b));
    writeln("Menor o igual: a <= b = ", (a <= b));

    // Operadores logicos
    writeln("and: a > 12 && b > 100 = ", (a > 12 && b > 100));
    writeln("or: a > 12 || b > 100 = ", (a > 12 || b > 2));
    writeln("not: !(a < b) = ", !(a < b));

    // Operadores de asignación
    writeln("a += b ; a = ", (a += b));
    writeln("a -= b ; a = ", (a -= b));
    writeln("a *= b ; a = ", (a *= b));
    writeln("a /= b ; a = ", (a /= b));
    writeln("a %= b ; a = ", (a %= b));
    writeln("a ^^= b ; a = ", (a ^^= b));


    // - Control de flujo - //
    writeln("\n___Control de flujo___");

    // Condicionales (if, else if, else)
    if (b < 10)
    {
        writeln("b es mayor que c");
    }
    else if (a > b)
    {
        writeln("a es mayor que b");
    }
    else
    {
        writeln("Nada de lo anterior se cumple");
    }

    // Bucle for
    for (int e = 0; e < b; e++)
    {
        writeln("\'e\' en este momento vale: ", e);
    }

    // Bucle while
    int q = 0;
    while (q != 10)
    {
        writeln("q = ", q);
        q += 1; // en este caso es lo mismo que hacer q++;
    }

    // Bucle do while
    int p = 0;
    do
    {
        writeln("p aún no es igual a 10");
    }while (++p != 10);

    // Bucle switch
    string z = "D";
    switch (z)
    {
    case "C":
        writeln("\'C\' Un buen lenguaje");
        break;
    case "C++":
        writeln("\'C++\' Un horrible lenguaje");
        break;
    case "D":
        writeln("\'D\' El mejor lenguaje");
        break;
    default:
        break;
    }

    // Bucle foreach
    string saludo = "Hola";
    foreach (letra; saludo)
    {
        writeln(letra);
    }


    // - Ejercicio extra - //
    writeln("\n___Ejercicio Extra___");
    extra();
}

void extra()
{
    import std.stdio: writeln; // En D se prefiere la importación de librerias a nivel local (de función)
                               // en lugar de importaciones globales, además de importar especificamente
                               // los simbolos que se van a utilizar, aunque esto solo es preferencia y no es obligatorio

    for (int i = 10; i < 56; i++)
    {
        if (i == 16)
        {
            continue;
        }
        else if ((i % 3) == 0)
        {
            continue;
        }
        else if ((i % 2) == 0)
        {
            writeln(i);
        }
    }
}
