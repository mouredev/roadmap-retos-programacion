class Program
{
    static void Main(string[] args)
    {
        string cadena = "Hola, Mundo!";

        // Acceder a carácter en específico 
        // Se indica un indice como en un Array
        Console.WriteLine("---Acceder a carácter en específico---");
        Console.WriteLine($"Cadena de texto original: {cadena}");
        Console.WriteLine($"La letra en la tercer posicion de la cadena es: {cadena[2]}.");

        // Subcadena
        // En C# existe la función Substring
        Console.WriteLine("---Subcadena---");
        string subcadena = cadena.Substring(6); // Se indica el índice a partir del cual empieza la subcadena
        Console.WriteLine($"Se creó la siguiente subcadena a partir del 7 carácter: {subcadena}");
        string subcadenaRango = cadena.Substring(0, 4); //Ademá del inicio de la subcadena se puede especificar la longitud
        Console.WriteLine($"Se creó la siguiente subcadena a partir del primer carácter y " +
            $"con una longitud de 4 carácteres: {subcadenaRango}");

        // Longitud
        // Podemos acceder a la longitud de una cadena por medio de la propiedad Length
        Console.WriteLine("---Longitud---");
        int longitud = cadena.Length;
        Console.WriteLine($"La longitud de la cadena original ({cadena}) es de {longitud} carácteres");

        // Concatenación
        // Para poder concatenar varias cadenas de texto podemos usar el símbolo '+'
        Console.WriteLine("---Concatenación---");
        string nombre = "Emilio";
        string apellido = "Quezada";
        Console.WriteLine($"Primer cadena de texto: {nombre}");
        Console.WriteLine($"Segunda cadena de texto: {apellido}");
        string nombreCompleto = nombre + " " + apellido; // => "Emilio Quezada"
        Console.WriteLine($"Cadena creada a partir de concatenar las cadenas anteriores y un espacio en blanco: {nombreCompleto}");

        // Repetición
        Console.WriteLine("---Repetición---");
        string repetición = new string('A', 5);
        Console.WriteLine($"Se creó la siguiente cadena repitiendo el carácter 'A' 5 veces: {repetición}");

        // Recorrido
        // Se puede usar un ciclo para recorrer todos los carácteres una cadena de texto
        Console.WriteLine("---Recorrido---");
        foreach (var caracter in cadena)
            Console.Write($"{caracter} | ");
        Console.WriteLine();

        // Conversión a mayúsculas y minúsculas
        /* En C# existen las funcións ToUpper() y ToLower para convertir
         * una cadena en mayúsculas y minusculas respectivamente
         */
        Console.WriteLine("---Conversión a mayúsculas y minúsculas---");
        string cadenaOriginal = "esTa eS lA CADeNa a maNIPulAR";
        Console.WriteLine($"Cadena original: {cadenaOriginal}");
        string cadenaMayusculas = cadenaOriginal.ToUpper();
        Console.WriteLine($"Cadena en mayúsculas: {cadenaMayusculas}");
        string cadenaMinusculas = cadenaOriginal.ToLower();
        Console.WriteLine($"Cadena en miníusculas: {cadenaMinusculas}");

        // Reemplazo
        /* En C# existe la función Replace() en la cual indicamos el
         * carácter a reemplazar y el carácter por el cual se va a 
         * reemplazar, se reemplazan todos los caracteres que coinciden
         * con el primer parámetro. Para filtros más específicos se puede
         * hacer uso de Expresiones Regulares
         */
        Console.WriteLine("---Reemplazo---");
        cadena = "Exist3n varios caráct3r3s incorr3ctos 3n 3sta cad3na a r33mplazar";
        Console.WriteLine($"Cadena con carácteres a reemplazar: {cadena}");
        string cadenaReemplazo = cadena.Replace('3', 'e');
        Console.WriteLine($"Cadena con reemplazo de carácteres: {cadenaReemplazo}");

        // División
        /* En C# podemos hacer uso de la función Split, la cual divide la cadena
         * de texto en base a un carácter en específico y guarda los resultados
         * en un Array de cadenas
         */
        Console.WriteLine("---División---");
        cadena = "Esta es la cadena a dividir por cada espacio en blanco";
        Console.WriteLine($"Cadena original: {cadena}");
        string[] palabras = cadena.Split(' ');
        Console.WriteLine("Mostramos cada uno de los elemento del arreglo creado:");
        foreach (var palabra in palabras)
            Console.WriteLine($"{palabra}");

        // Unión

        Console.WriteLine("---Unión---");
        string[] arreglo = { "Este", "arreglo", "se", "convertirá", "en", "una", "cadena", "de", "texto" };
        Console.WriteLine("Se creó un Array de cadenas de texto con los siguientes elementos:");
        foreach (var elemento in arreglo)
            Console.WriteLine(elemento);
        string cadenaUnion = string.Join(" ", arreglo);
        Console.WriteLine("Se unieron todos los elementos del arreglo agregando un espacio en blanco entre cada uno");
        Console.WriteLine($"Resultado: {cadenaUnion}");

        // Interpolación 
        /* Una alternativa a la concatenación es la interpolación de cadenas de
         * texto.
         * Agregamos un símbolo $ al inicio de la cadena y dentro de llaves ({}) indicamos
         * la variable que queremos utilizasr en la cadena
         */
        Console.WriteLine("---Interpolación---");
        nombre = "Carlos";
        apellido = "Santana";
        Console.WriteLine($"Mi nombre es {nombre} y me apellido {apellido}");

        // Verificación
        /* Existen varios tipos de verificación dentro de las cadenas de texto:
         * - Igualdad
         * - Empieza o Termina con
         * - Contiene una subcadena
         */

        Console.WriteLine("---Verificación---");
        // Igualdad
        Console.WriteLine("1.- Igualdad");
        // Se puede comparar si una cadena es igual a otra
        cadena = "Peras";
        string cadena2 = "Manzanas.";
        Console.WriteLine($"{cadena} == {cadena2} es: {cadena == cadena2}");
        if (cadena == cadena2)
            Console.WriteLine("Las cadenas de texto son iguales");
        else
            Console.WriteLine("Las cadenas de texto son diferentes");
        // Empieza o termina con
        /* En C# las funciones StartsWith() y EndsWith() regresan un booleano
         * indicando si cadena empieza o termina con el parámetro enviado
         */
        Console.WriteLine("2.- Empieza o termina con");
        cadena = "Pablito clavó un clavito";
        Console.WriteLine($"cadena = {cadena}");
        Console.WriteLine($"cadena.StartsWith(\"P\") es: {cadena.StartsWith("P")}");
        Console.WriteLine($"cadena.EndsWith(\"a\") es : {cadena.EndsWith("a")}");
        // Contiene
        /* En C# la función Contains() regresa un booleano indicando si dentro de la
         * cadena existe la subcadena especificada
         */
        Console.WriteLine("3.- Contiene");
        Console.WriteLine($"cadena.Contains(\"p\") es: {cadena.Contains("p")}");

        // Recortar
        cadena = " Cadena con espacios en blanco al inicio y al final de la cadena ";
        string cadenaRecortada = cadena.Trim(); // => "Cadena con espacios en blanco al inicio y al final de la cadena"

        // Comprobar si la cadena está vacía o es nula
        Console.WriteLine("---Comporbar si una cadena está vacía o es nula");
        cadena = "";
        Console.WriteLine($"cadena = \"\"");
        Console.WriteLine($"string.IsNullOrEmpty(cadena) es : {string.IsNullOrEmpty(cadena)}");
        Console.ReadLine();

        // Ejercicio extra
        Console.Clear();
        Console.WriteLine("----EJERCICIO EXTRA----");
        bool salir = false;
        Console.WriteLine("Ingresa la primera palabra:");
        string primerPalabra = Console.ReadLine();
        Console.WriteLine("Ingresa la segunda palabra:");
        string segundaPalabra = Console.ReadLine();
        Console.Clear();
        string opcion;
        do
        {
            MostrarMenu();
            opcion = Console.ReadLine();
            switch (opcion)
            {
                case "A":
                case "a":
                    if (EsPalindromo(primerPalabra.ToLower()))
                        Console.WriteLine($"La palabra {primerPalabra} es un palíndromo.");
                    else
                        Console.WriteLine($"La palabra {primerPalabra} no es un palíndromo.");
                    if (EsPalindromo(segundaPalabra.ToLower()))
                        Console.WriteLine($"La palabra {segundaPalabra} es un palíndromo.");
                    else
                        Console.WriteLine($"La palabra {segundaPalabra} no es un palíndromo.");
                    break;
                case "B":
                case "b":
                    EsAnagrama(primerPalabra, segundaPalabra);
                    break;
                case "C": 
                case "c":
                    if (EsIsograma(primerPalabra.ToLower()))
                        Console.WriteLine($"La palabra {primerPalabra} es un isograma.");
                    else
                        Console.WriteLine($"La palabra {primerPalabra} no es un isograma.");
                    if (EsIsograma(segundaPalabra.ToLower()))
                        Console.WriteLine($"La palabra {segundaPalabra} es un isograma.");
                    else
                        Console.WriteLine($"La palabra {segundaPalabra} no es un isograma.");
                    break;
                case "D":
                case "d":
                    salir = true;
                    Console.WriteLine("Hasta la próxima...");
                    Thread.Sleep(2000);
                    break;
                default:
                    Console.WriteLine("Opción no válida...");
                    break;
            }

        } while (!salir); 

    }

    static bool EsPalindromo(string palabra)
    {
        for (int i = 0; i < palabra.Length / 2; i++)
        {
            char c = palabra[i];
            char c2 = palabra[palabra.Length - i - 1];
            if (palabra[i] != palabra[palabra.Length - i - 1])
                return false;
        }
        return true;
    }
    static void EsAnagrama(string primerPalabra, string segundaPalabra)
    {
        var primerArreglo = primerPalabra.ToCharArray();
        var segundoArreglo = segundaPalabra.ToCharArray();

        Array.Sort(primerArreglo);
        Array.Sort(segundoArreglo);

        if (string.Join("", primerArreglo) == string.Join("", segundoArreglo))
            Console.WriteLine($"Las palabras {primerPalabra} y {segundaPalabra} son anagramas");
        else
            Console.WriteLine($"Las palabras {primerPalabra} y {segundaPalabra} no son anagramas");
    }
    static bool EsIsograma(string palabra)
    {  
        var hash = palabra.ToHashSet<char>();
        if (hash.Count != palabra.Length)
            return false;
        return true;
    }
    static void MostrarMenu()
    {
        Console.WriteLine("a.- Comporbar si las palabras son Palíndromos");
        Console.WriteLine("b.- Comprobar si las palabras son Anagramas");
        Console.WriteLine("c.- Comprobar si las palabras son Isogramas");
        Console.WriteLine("d.- Salir");
        Console.WriteLine("Elige la opción a consultar");
    }
}