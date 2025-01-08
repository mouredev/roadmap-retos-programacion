//Pues no me da por poner aqui la url. XD. Anotare el titulo de la pull «#00 - C#»
/*
Esa doble diagonal toma por comentario el resto de la linea
Mientras que «/*» abre un comentario de varias lineas y «* /» lo cierra
De hecho, lo he tenido que poner separado (a diferencia de como se nota al final del comentario) porque se tomaba como cierre.
Osea, lo que haya de esos 2 signos en adelante si se ejecutara, al menos segun github. Tenerlo en cuenta
*/

/// <summary>
/// Esto es un comentario de documentación
/// </summary>
/// <returns></returns>

using System; //No termino de entender para que es el using, pero a finales del ejercicio estudie los otros que se enviaron
using System.Collections.Generic; //para ver si me faltaban tipos
using System.Linq; //y casi todos tenian estas cosas al mero inicio.
using System.Text;
using System.Threading.Tasks;

//Variables
////Puden escribirse asi nomas como el primer ejemplo, o con «private» y «public» segun el caso, ya que eso define desde que partes el codigo puedes acceder a la variable
string NombreDeVariable = "Para poner una variable basta con poner el tipo de dato y su nombre. En esta el tipo es «string»"; //se usa «PascalCase» para nombrar las cosas, consiste en poner cada primer letra en mayuscula

const string NOMBRECONSTANTE = "Poner «const» antes del tipo hace que sea una constante"; //solo pueden tener constantes de los tipos de estructura simple y se nombra con pura mayuscula

enum WeekDays { Monday, Tuesday, Wednsday, thursday, Friday, Saturday, Sunday}; //esto ya es una estructura de valores y no puede ser constante.
//aunque una manera de definir que es un enum, es «Un diccionario constante con claves string y valores int», segun tengo entendido

string? String_Nulleable = null //si pones un «?» despues del tipo la variable podra tener valores null, osea, nulo.

int[] Array = new int[5]; // cuando despues del tipo se pone «[]» es un array o arreglo, se debe poner un «new» seguido por el tipo y entre los «[]» el numero de espacios que tiene
string [] Array2 = new string[] { "cocina", "baño", "salon", "comedor", "dormitorio" }; // aqui observamos un array de tipo string tambien con 5 posiciones pero ya con su valor
//si no pones los valores de cada espacio agarra el predeterminado. Puedes escribir «Array[posision]=» para cambiar cualquier posicion pero el total de datos no pueden aumentar ni disminuir

int[,] MultiDimencional = new int[2, 3]; // los valores se refieren a 2 Filas, 3 Columnas
int[,,] MultiDimencional2 = new int[,,] { { { 1, 2, 3 }, { 4,   5,  6 } }, //Cada coma al incio junto al tipo indica una dimencion mas
                                        { { 7, 8, 9 }, { 10, 11, 12 } } }; //para tomar los valores de estas debes poner el index de cada dimencion: Multidimencional2[1,2,3] es el 6
var NoSeQueEsEstoTodavia = "al poner «var» se puede poner cualquier tipo de valor y el compilador identificara cual es y lo asignara";
dynamic puede_ser_lo_que_sea = "poniendo «dynamic» se puede cambiar el tipo de dato al cambiar el valor"; //en la doc note que para estas usan todo minusculas y separa con «_»


//Tipos de datos
////Numeros. cada variable tiene el valor maximo o minimo que puede tener el tipo de dato
//////Se pueden usar «_» para separar los numeros y facilitar la lectura.
public byte UnNumeroDe1BytePorDefecto = 255; //es el numero mas alto que puede tener un solo byte, osea, 8 bits
public sbyte UnNumeroDe1BytePositivo = 127; //con la s al principio, se indica que tiene valores negativos. Pero al seguir siendo un solo byte, se recorta a la mitad su valor maximo.
public sbyte UnNumeroDe1ByteNegativo = -128; //

public short UnNumeroDe2BytesMax = 32_767; //como indica, estos pueden almacenar numeros de 2 bytes, osea, 16 bits.
public short UnNumeroDe2BytesMin = -32_768;
public ushort UnNumeroDe2BytesSoloPositivo = 65_535; //con esa u, estos no pueden tener negativos

public int UnNumeroPositivo = 2_147_483_647; //el int soporta numeros de 32 bits (4 bytes), positivos y negativos
public int UnNumeroNegativo = -2_147_483_648; //
public uint UnNumeroSoloPositivo = 4_294_967_295; //con esa u, se indica que solo tiene valores positivos

public long NumerosMasGrandesPositivo = 9_223_372_036_854_775_807; // Estos son de 64 bits, osea de 8 bytes
public long NumerosMasGrandesNegaivo = -9_223_372_036_854_775_808; //
public ulong NumerosMasGrandesSoloPositivo = 18_446_744_073_709_551_615; // La u indica que solo puede tener positivos. ¡No te lo esperabas, ¿vea?!

//Creo yo, por el tema de exponentes de 2 y tal, que los numeros positivos tienen un valor absoluto menor porque en ellos cuentan el cero.
//Dado que, los «u» pueden tener cero y no negativos.

public nint NumeroNativo; //con la «n» al incio de un int o uint, se usaran los numeros nativos del programa
public nuint NumeroNativo; //si se corre en una compu de 32bits funcionara como int/uint normal, si es de 64bits funcionara como long/ulong

public float UnDecimal =0.0f; //tiene una precicion de 6 a 9 dígitos aproximadamente, ya que usa 4 bytes. Termina con una f
public double UnDecimalMejor = 0.0; //es mas preciso usando 8 bytes, de 15 a 17 dígitos aproximadamente
public decimal ElMejorDecimal = 0.0m; //con 16 bytes es el tipo de decimal mas preciso, de 28-29 dígitos. Termina con una m
/* En este no pongo los valores maximos y minimos porque lo que pone la documentacion es esto:
float: De ±1,5 x 10^-45 a ±3,4 x 10^38
double: De ±5,0 × 10^−324 a ±1,7 × 10^308
decimal: De ±1,0 x 10^-28 to ±7,9228 x 10^28
Pero, cada tipo de numero decimal tiene sus constantes, citando doc: «Por ejemplo, el tipo double ofrece las siguientes constantes: Double.NaN, Double.NegativeInfinity y Double.PositiveInfinity»
Ademas, las tres tienen «MinValue» y «Max value» para representar esos numeros de arriba.
Al final del ejercicio estos seran mostrados por la consola por si interesa y para mostras como poner esos datos en medio del mensaje, ya que me lo encontre mientras buscaba lo demas
*/

public bool Verdadero = True; //estos son valores que solo cambian entre verdadero y falso
public bool Falso = False; //se deben poner los valores con la primera mayuscula
public bool Tambien_false = 0;//tambien, cuando se asigna sus valor se pueden poner numeros, 0 es false y cualquier otro es true
public bool Tambien_true = 31;

public char UnaSolaLetra = 'j'; //es como una string de solo 2 byte, por tanto, es solo una letra. Como representa los caracteres Unicode UTF-16
//internamente tiene valores de 0 a 65_535 (U+0000 a U+FFFF, en unicode). Notaras que en eso es como el ushort, pero no se pueden pasar valores numericos a char
//creo que era importante que para estos se usen las comillas simples
public char OtraLetra = NombreDeVariable[0]; //un char tambien puede hacerse tomando una letra de una string de este modo
var chars = new[] //para mostrar como funciona, todas estas siguen representando «j»
{
    (char)106,
    '\u006A', //esto es unicode, se debe poner «\u» seguido de los 4 digitos hexadecimales
    '\x006A', //sin embargo, poniendo  «\x» se identifica un codigo hexadecimal y se pueden omitir todos los ceros a la izquierda
    '\x06A', //haciendo que estas 3
    '\x6A', //tambien sean el mismo codigo
};

/*
C# tiene 2 tipos de variable, las de valor (la mayoria de ejemplos de arriba) y las de referencia. La primeras almacenan su valor, y las otras tienen referencias a un objeto
los tipos para declarar variables de referencia son: class, interface, delegate, record, dynamic, object y string.
Las arrays mencionadas al principio tambien son variables de referencia
Incluyo esto porque la string entra en lo de variables primitivas (creo).
Al ser de referencia, las variables strings guardan referencia a una cadena de char. 2 o mas variables pueden tener referencia a la misma instancia, si cambia una cambian todas
Pero, no por ser iguales refieren a la misma instancia. Por ejemplo:
*/
public string a = "hello";
public string b = "h";
b += "ello";
/*
Al final a y b tienen el mismo valor por lo cual, al comparar «a==b» dara true
Pero con object.ReferenceEquals(a, b) dara false, ya que siguen referenciando una instancia de string distinta
*/

/*Valores predeterminados
Cada tipo de dato tiene su valor predeterminado, si despues del nombre no asignas un valor, la varible toma el predeterminado

Todos los tipos numericos, tanto enteros como decimales, tienen el 0.
bool = false
char = '\0'
y todos los tipos que acepten null son null, incluye a los que les pones «?» cuando las declaras
*/

class Program {
    static void Main() { //por algun motivo, Main todos los que lo subian lo hacian con «string[] args», pero a mi el compilador que agarre para probar me lo deja usar asi
        Console.WriteLine("¡Hello, C#!");
        Console.WriteLine("Hoy si, aqui esta la URL: https://learn.microsoft.com/es-es/dotnet/csharp/ .XD");
        Console.WriteLine("El valor maximo de float es: {0}"+" Y su minimo es {1}", float.MaxValue, float.MinValue);
        Console.WriteLine("El valor maximo de double es: {0}"+" Y su minimo es {1}", Double.MaxValue, Double.MinValue);
        Console.WriteLine("El valor maximo de decimal es: {0}"+" Y su minimo es {1}", Decimal.MaxValue, Decimal.MinValue);
    }
} //ahorita lo voy a subier y me da que se olvida algo, pero de extrañar seria si lo he revisado 3 veces
