// CADENAS DE CARACTERES

using System.Xml.Linq;

string str = "Miguel Angel Moreno";

// Acceso a caracteres especificos

Console.WriteLine("=== ACCESO A CARACTERES ESPECIFICOS === \n");

char primerCaracter = str[0];
char ultimoCaracter = str[18];

Console.WriteLine(primerCaracter);
Console.WriteLine(ultimoCaracter);

Console.WriteLine();

// Subcadenas

Console.WriteLine("=== SUBCADENAS === \n");

string subCadena = str.Substring(7);
string subCadena2 = str.Substring(7,5);

Console.WriteLine(subCadena);
Console.WriteLine(subCadena2);

Console.WriteLine();

// Logitud

Console.WriteLine("=== LONGITUD === \n");

int strLen = str.Length;

Console.WriteLine(strLen);

Console.WriteLine();

// Concatenacion

Console.WriteLine("=== CONCATENACION === \n");

string str1 = "Hola";
string str2 = "Mundo";

Console.WriteLine($"{str1} {str2}");

Console.WriteLine();

// Repeticion

Console.WriteLine("=== REPETICION === \n");

for (int i = 0; i < 3; i++) Console.WriteLine(str);

Console.WriteLine();

// Recorrido

Console.WriteLine("=== RECORRIDO === \n");

foreach (char c in str)
{
    Console.WriteLine(c);
}

Console.WriteLine();

// Conversion a mayusculas y minusculas

Console.WriteLine("=== MAYUSCULAS Y MINUSCULAS === \n");

string mayusculas = str.ToUpper();
string minusculas = str.ToLower();

Console.WriteLine(mayusculas);
Console.WriteLine(minusculas);

Console.WriteLine();

// Reemplazo

Console.WriteLine("=== REEMPLAZO === \n");

string reemplazo = str.Replace("Miguel", "Logan");

Console.WriteLine(reemplazo);

Console.WriteLine();

// Division

Console.WriteLine("=== DIVISION === \n");

string[] partes = str.Split(' ');

foreach (string parte in partes)
{
    Console.WriteLine(parte);
}

Console.WriteLine();

// Union

Console.WriteLine("=== UNION === \n");

string union = string.Join("-", partes);

Console.WriteLine(union);

Console.WriteLine();


string[] lista = {"1", "2", "3", "4"};

string fusion = string.Join("*", lista); 

Console.WriteLine(fusion);

Console.WriteLine();

// Interpolacion

Console.WriteLine("=== INTERPOLACION === \n");

string nombre = "Logan";
int edad = 30;

Console.WriteLine($"Hola me llamo {nombre}, y mi edad es {edad}");

Console.WriteLine();

// Verificacion

Console.WriteLine("=== VERIFICACION === \n");

string programacion = "Programacion en CSharp";

bool contiene = programacion.Contains("en");
bool comienzaCon = programacion.StartsWith("Programacion");
bool terminaCon = programacion.EndsWith("CSharp");

Console.WriteLine($"{contiene} {comienzaCon} {terminaCon}");

Console.WriteLine();

// Comparacion

Console.WriteLine("=== COMPARACION === \n");

string saludo1 = "Hola";
string saludo2 = "Hello";

bool sonIguales = saludo1.Equals(saludo2);
int comparacion = string.Compare(saludo1, saludo2);  // Compara dos cadenas y devuelve un valor entero que indica su orden relativo

Console.WriteLine(sonIguales);
Console.WriteLine(comparacion);

Console.WriteLine();

// Eliminacion de espacios en blanco

Console.WriteLine("=== ELIMINACION ESPACIOS EN BLANCO === \n");

string cadenaConEspacios = "  Programacion en CSharp  ";

string sinEspacios = cadenaConEspacios.Trim();

Console.WriteLine(sinEspacios);

Console.WriteLine();

// Busqueda

Console.WriteLine("=== BUSQUEDA === \n");

int indice = str.IndexOf("Angel");
bool verificacion = str.Contains("Moreno");

Console.WriteLine(indice);
Console.WriteLine(verificacion);

Console.WriteLine();

// ========== EXTRA =============

Console.WriteLine("=== EXTRA === \n");

void AnalyzeWords(string str1, string str2)
{
    void Palindromo(string str1, string str2)
    {
        char[] newStr1 = str1.ToLower().ToCharArray();
        Array.Reverse(newStr1);
        string Str1R = new (newStr1);

        bool like1 = str1.Equals(Str1R);


        char[] newStr2 = str2.ToLower().ToCharArray();
        Array.Reverse(newStr2);
        string Str2R = new (newStr2);

        bool like2 = str2.Equals(Str2R);

        if (like1 && like2)
        {
            Console.WriteLine("Las dos palabras son palindromas");
        }
        else if (like1 && !like2)
        {
            Console.WriteLine("Solo la primera palabra es palindroma");
        }
        else if (!like1 && like2)
        {
            Console.WriteLine("Solo la segunda palabra es palindroma");
        }
        else if (!like1 && !like2) 
        { 
             Console.WriteLine("Ninguna palabra es palindroma"); 
        }

        Console.WriteLine();
    }

    void Anagrama(string str1, string str2)
    {
        char[] newStr1 = str1.ToCharArray();
        Array.Sort(newStr1);
        string str1S = new(newStr1);

        char[] newStr2 = str2.ToCharArray();
        Array.Sort(newStr2);
        string str2S = new(newStr2);

        bool sortWord = str1S.Equals(str2S);

        if (sortWord)
        {
            Console.WriteLine("Las palabras son un anagrama");
        }
        else
        {
            Console.WriteLine("Las palabras no son un anagrama");
        }

        Console.WriteLine();
    }

    void Isograma(string str1, string str2)
    {
        if (str1.Length == str1.Distinct().Count())
        {
            Console.WriteLine("La primera palabra es un isograma");
        }
        else
        {
            Console.WriteLine("La primera palabra no es un isograma");
        }

        Console.WriteLine();

        if (str2.Length == str2.Distinct().Count())
        {
            Console.WriteLine("La segunda palabra es un isograma");
        }
        else
        {
            Console.WriteLine("La segunda palabra no es un isograma");
        }

        Console.WriteLine();
    }

    Palindromo(str1, str2);
    Anagrama(str1, str2);
    Isograma(str1, str2);
        
}

AnalyzeWords("murcielago", "reconocer");






