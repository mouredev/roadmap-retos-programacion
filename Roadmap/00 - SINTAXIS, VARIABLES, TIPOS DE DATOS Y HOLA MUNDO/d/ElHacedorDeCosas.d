/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

// https://dlang.org/

void main()
{
    int variable = 2025;
    const string constante = "Hola";


    // - Tipos de datos - //

    // Tipo buleano
    bool buleano = true; // (true o false) verdadero o falso

    // Tipos enteros con signo (pueden ser positivos o negativos)
    byte bit;                  // entero de 8  bits
    short corto;               // entero de 16 bits
    int entero;                // entero de 32 bits
    long largo;                // entero de 64 bits

    // Tipos enteros sin signo (solo pueden ser positivos)
    ubyte uBit;                // sin signo de 8  bits
    ushort uCorto;             // sin signo de 16 bits
    uint uEntero;              // sin signo de 32 bits
    ulong uLargo;              // sin signo de 64 bits

    // Tipo flotante (numeros con decimales)
    float flotante;            // flotante de 32 bits
    double doble;              // flotante de 64 bits
    real flotanteReal;         // el tamaño del punto flotante más grande disponible

    // Tipo caracter
    char caracter;             // sin signo de 8  bits (UTF-8  code)
    wchar wcaracter;           // sin signo de 16 bits (UTF-16 code)
    dchar dcaracter;           // sin signo de 32 bits (UTF-32 code)

    string cadena;             // alias de "immutable(char)[]"
    wstring wcadena;           // alias de "immutable(wchar)[]"
    dstring dcadena;           // alias de "immutable(dchar)[]"


    // - Saludo por terminal - //

    import std.stdio: writeln; // Estoy importando especificamente la función writeln
                               // desde la biblioteca estandar de D para escribir en terminal
    writeln("¡Hola, D o Dlang!");
}
