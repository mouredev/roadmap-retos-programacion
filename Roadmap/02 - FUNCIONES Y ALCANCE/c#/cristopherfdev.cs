
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
 */

 using System;

 namespace Funciones; 

 class program 
 {
    static string vGlobal = "Variable Global"; 

    static void Main(string[] args)
    {
        Hello();

        greetPerson("Cristopher"); 

        int additionS = addition (5,10);
        Console.WriteLine (" " + additionS);
        
        //Funcion creada en el lenguaje
        string text = "hola mundo";
        Console.WriteLine("ToUpper convierte el texto a mayúscula: " + text.ToUpper());

        ShowVariable(); 

    }

    //Función sin parámetros ni retorno 
    static void Hello()
    {
        Console.WriteLine("Hola! Esta es la función sin parámetros"); 
    }

    //Función con parámetro sin retorno
    static void greetPerson(string name)
    {
        Console.WriteLine ("Hola, "+ name + "!");
    }

    //Función con parámetro y retorno 
    static int addition (int fNum, int sNum)
    {
        return fNum + sNum; 
    }

    //Variable Local y Global
    static void ShowVariable() 
    {
        string Vlocal = "Variable Local"; 
        Console.WriteLine(Vlocal); 
        Console.WriteLine(vGlobal); 
    }

}
 