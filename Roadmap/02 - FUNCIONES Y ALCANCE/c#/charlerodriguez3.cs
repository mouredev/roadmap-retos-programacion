/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
*/



Number100("hello-3", "world-5");
WriteSomething();
WriteMyWord("This is the word. Hello my friend");
int num = 0;
num = NewValue();


//programming language function already created
string word3 = "This is not a word but a sentence";


//substring is a function which cuts a parts of a string, having in count that
//the first parameter will be the number of the index start to cut a part of the string, and the second parameter is the length
word3.Substring(0, 4);

//WITHOUT PARAMETERS
//WITHOUT RETURN
private static void WriteSomething()
{
    Console.WriteLine("tHiS iS A cRaZy TexT");
}




//WITH ONE PARAMETER AND NO RETURN

private static void WriteMyWord(string v)
{
    Console.WriteLine(v);
}



//WITH RETURN AND NO PARAMETERS

private static int NewValue()
{
    return 5;
}

//WITH TWO OR MORE PARAMETERS
//WITH RETURN

 public static int Number100(string word1,  string word2)
 {
     int times = 0;
     for(int i = 1; i <= 100; i++) {

         if(i % 3 == 0 && i % 5 == 0) Console.WriteLine($"{word1} {word2}");
         else if(i % 3 == 0) Console.WriteLine(word1);
         else if(i % 5 == 0) Console.WriteLine(word2);
         else
         {
            Console.WriteLine(i);
            times++;
         }
     }

     return times;
 }


//global and local variables

 static void Main(string[] args)
 { 
     int num = 0;

     num = NewValue(num);
     Console.WriteLine(num);
     //the variable numLocal only exists inside the method NewValue
     Console.WriteLine(numLocal); // this is an error 
 }

 
 private static int NewValue(int num)
 {
     int numLocal = 20;
     Console.WriteLine($" I can access to this global variable {num} from here beucase it is global");
     return num + numLocal;
 }



/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

Number100("hello-3", "world-5");

 public static int Number100(string word1,  string word2)
{
    int times = 0;
    for(int i = 1; i <= 100; i++) {

        if(i % 3 == 0 && i % 5 == 0) Console.WriteLine($"{word1} {word2}");
        else if(i % 3 == 0) Console.WriteLine(word1);
        else if(i % 5 == 0) Console.WriteLine(word2);
        else
        {
           Console.WriteLine(i);
           times++;
        }
    }

    return times;
}