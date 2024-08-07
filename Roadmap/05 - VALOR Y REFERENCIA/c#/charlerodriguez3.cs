//*EJERCICIO:
// *-Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
// *   su tipo de dato.
// * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
// *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
// * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)


/*
*DIFICULTAD EXTRA(opcional):
 *Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

//ejemplo Asignaciones por valor // solo cambia su valor en el contexto actual

//tipos como int, float, double, entre otros. Son tipos de variable x valor

int num1 = 3;
float num2 = 20.5f;
Console.WriteLine($"Valores actuales antes del metodo:  Numero {num1} y Flotante: {num2}\n");

(int numNuevo, float floatNuevo) = CambiarParametrosPorValor(num1, num2);

Console.WriteLine($"Valores despues del metodo:  Numero {numNuevo} y FlotanteNuevo: {floatNuevo}\n");



//ejemplo Asignacion por referencia, cambia su valor a pesar de modificarse en otro metodo o contexto

// tipos como arrays, objects, list, string(Array char), entre otros.Son tipos de variable x referencia
string palabra = "hola";
int[] numeros = new int[]{ 1, 2, 3, 4, 5 };
Console.WriteLine($"Valores actuales antes del metodo:  Palabra {palabra} y Arreglo:\n");
foreach(int num in numeros)
{
    Console.Write(" "+num);
}

Console.WriteLine("");
//ALERT! :
//Aqui se esta utilizando variables de referencia pero no se estan pasando por referencia
(string palabraNueva, int[] arregloInvertido) = CambiarParametrosPorReferencia(palabra, numeros); 


Console.WriteLine($"Valores despues del metodo:  Palabra {palabraNueva} y Arreglo:\n");
foreach (int num in arregloInvertido)
{
    Console.Write(" " + num);
}
Console.WriteLine("");


(string palabraNueva2, int[] arregloInvertido2) = CambiarParametrosPorReferencia2(ref palabra,ref numeros);

Console.WriteLine($"Valores despues del metodo POR REFERENCIA LAS VARAIBLES:  Palabra {palabraNueva2} y Arreglo:\n");
foreach (int num in arregloInvertido2)
{
    Console.Write(" " + num);
}
Console.WriteLine("");


static (int, float) CambiarParametrosPorValor(int valor1, float valor2)
{
    valor1 += 100;
    valor2 /= 4;

    return (valor1,valor2);
}
static (string, int[]) CambiarParametrosPorReferencia(string valor1 , int[] valor2)//Al ser por referencia solo se modifican en su contexto del metodo y no en el global
{
    valor1.Reverse();//Invertir la palabra
    valor2.Reverse();//Invertir la secuencia de numeros en el array


    return (valor1, valor2);
}

static (string, int[]) CambiarParametrosPorReferencia2(ref string valor1 , ref int[] valor2)//Al utilizar la palabra reservada out o ref, estos tipos de variables por referencia
{//al modificarlos en un contexto menor como un metodo, tambien modifican su valor en el global
    valor1 = new string(valor1.Reverse().ToArray());//Invertir la palabra
    Array.Reverse(valor2);//Invertir la secuencia de numeros en el array
    return (valor1, valor2);
}