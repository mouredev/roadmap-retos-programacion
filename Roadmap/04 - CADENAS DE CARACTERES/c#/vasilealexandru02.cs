public class vasilealexandru02
{

    static void Main(string[] args)
    {


        /*
         * EJERCICIO:
         * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
         * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
         * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
         *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
         */


        string miCadena = "Hola";
        string miCadena2 = " Mundo";
        string holaMundo = miCadena + miCadena2;
        Console.WriteLine("Cadena concatenada: " + holaMundo);
        string subcadena = holaMundo.Substring(miCadena.Length);
        Console.WriteLine("Subcadena: " + subcadena);

        char miCaracterEspecifico = subcadena[1];

        Console.WriteLine("Carácter específico: " + miCaracterEspecifico);
        string largoCadenaInterpolacion = $"El largo de mi cadena: {holaMundo}, es de {holaMundo.Length} caracteres ";
        Console.WriteLine(largoCadenaInterpolacion);

        Console.WriteLine($" Mi texto en mayúsculas: {largoCadenaInterpolacion.ToUpper()}");
        Console.WriteLine($" Mi texto en minúsculas: {largoCadenaInterpolacion.ToLower()}");

        Console.WriteLine($"Estas dos cadenas son iguales: {miCadena.Equals(miCadena2)}");

        var cadenaComoLista = holaMundo.ToList();

        cadenaComoLista.ForEach(letra =>
        {
            Console.WriteLine($"Letra {letra}");
        });

        Console.WriteLine("Mi cadena: " + holaMundo + ", contiene la subcadena" + miCadena2 + ": " + holaMundo.Contains(miCadena2));


        var caracteres = holaMundo.ToCharArray();
        string cadenaSeparadaPorComas = String.Join(",", caracteres);

        Console.WriteLine("Letras separadas por un caracter: " + cadenaSeparadaPorComas); ;

        string holaMundoI = holaMundo.Replace('o', 'i');

        Console.WriteLine("Intercambiando caracteres: " + holaMundoI);

        //compararPalabras("amor", "ana"); --> test palabras palíndromas
        //compararPalabras("lacteo", "coleta"); --> test palabras anagramas
        compararPalabras("fotolitografia", "litofotografia"); //--> test palabras anagramas
        //compararPalabras("murciélago", "mewing"); --> test palabras isogramas

        /*
        * DIFICULTAD EXTRA (opcional):
        * Crea un programa que analice dos palabras diferentes y realice comprobaciones
        * para descubrir si son:
        * - Palíndromos
        * - Anagramas
        * - Isogramas
        */

        void compararPalabras(string palabra, string palabraDos)
        {
            // Comprobar si las palabras son palíndromas

            string palabraInversa = String.Join("", palabra.Reverse());
            Console.WriteLine($"La palabra {palabra} es palíndroma: {palabraInversa.Equals(palabra)}");

            string palabraDosInversa = String.Join("", palabraDos.Reverse());
            Console.WriteLine($"La palabra {palabraDos} es palíndroma: {palabraDosInversa.Equals(palabraDos)}");
            var test2 = palabraDos.Reverse();

            bool anagrama = false;
            List<bool> checks = new List<bool>();
            // Comprobar si las palabras son anagramas
            if (palabra.Length == palabraDos.Length && !palabra.Equals(palabraDos))
            {

                var palabraArray = palabra.ToList();
                palabraArray.ForEach(c =>
                {
                    checks.Add(palabraDos.Contains(c));
                });
                anagrama = !checks.Contains(false);
            }


            Console.WriteLine($"Las palabras: {palabra} y {palabraDos} son anagramas: {anagrama}");
            // Comprobar si las palabras son isogramas

            HashSet<char> caracteres = new HashSet<char>();

            palabra.ToList().ForEach(c => caracteres.Add(c));
            Console.WriteLine($"La palabra {palabra} es isograma: {palabra.Length == caracteres.Count}");

            caracteres.Clear();

            palabraDos.ToList().ForEach(c => caracteres.Add(c));

            Console.WriteLine($"La palabra {palabraDos} es isograma: {palabraDos.Length == caracteres.Count}");

        }
    }
}