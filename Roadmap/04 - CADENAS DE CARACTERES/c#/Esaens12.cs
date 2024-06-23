namespace _04_CADENAS_DE_CARACTERES
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
      * EJERCICIO:
      * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
      * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
      * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
      *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
      *   interpolación, verificación...
      *
      * DIFICULTAD EXTRA (opcional):
      * Crea un programa que analice dos palabras diferentes y realice comprobaciones
      * para descubrir si son:
      * - Palíndromos
      * - Anagramas
      * - Isogramas
      */


            // Acceso a Caracteres Específicos
            string cadena = "Hola Mundo";
            char caracter = cadena[1];  // 'o'
            Console.WriteLine(caracter);

            // Subcadenas
            string subcadena = cadena.Substring(0, 4);  // "Hola"
            Console.WriteLine(subcadena);

            // Longitud
            int longitud = cadena.Length;  // 10
            Console.WriteLine(longitud);

            // Concatenación
            string saludo = "Hola" + " " + "Mundo";
            Console.WriteLine(saludo);

            string saludo2 = string.Concat("Hola", " ", "Mundo");
            Console.WriteLine(saludo2);

            // Repetición
            string repetido = new string('a', 5);  // "aaaaa"
            Console.WriteLine(repetido);

            // Recorrido
            foreach (char c in cadena)
            {
                Console.Write(c + " ");
            }
            Console.WriteLine();

            // Conversión a Mayúsculas y Minúsculas
            string mayusculas = cadena.ToUpper();  // "HOLA MUNDO"
            Console.WriteLine(mayusculas);

            string minusculas = cadena.ToLower();  // "hola mundo"
            Console.WriteLine(minusculas);

            // Reemplazo
            string reemplazada = cadena.Replace("Mundo", "C#");  // "Hola C#"
            Console.WriteLine(reemplazada);

            // División
            string[] partes = cadena.Split(' ');  // ["Hola", "Mundo"]
            foreach (var parte in partes)
            {
                Console.WriteLine(parte);
            }

            // Unión
            string[] palabras = { "Hola", "Mundo" };
            string unida = string.Join(" ", palabras);  // "Hola Mundo"
            Console.WriteLine(unida);

            // Interpolación
            string nombre = "C#";
            string interpolada = $"Hola, {nombre}";  // "Hola, C#"
            Console.WriteLine(interpolada);

            // Verificación
            bool contiene = cadena.Contains("Mundo");  // true
            Console.WriteLine(contiene);

            bool empieza = cadena.StartsWith("Hola");  // true
            Console.WriteLine(empieza);

            bool termina = cadena.EndsWith("Mundo");  // true
            Console.WriteLine(termina);

            // Eliminar Espacios en Blanco
            string cadenaConEspacios = "  Hola Mundo  ";
            string sinEspacios = cadenaConEspacios.Trim();  // "Hola Mundo"
            Console.WriteLine(sinEspacios);

            string sinEspaciosInicio = cadenaConEspacios.TrimStart();  // "Hola Mundo  "
            Console.WriteLine(sinEspaciosInicio);

            string sinEspaciosFinal = cadenaConEspacios.TrimEnd();  // "  Hola Mundo"
            Console.WriteLine(sinEspaciosFinal);

            Console.WriteLine();

            // Metodos siendo llamados

            EsPalindromo();
            EsAnagrama();
            EsIsograma();

        }

        // METODO PALABRAS PALINDROMO

        public static void EsPalindromo()
        {
            Console.WriteLine("Escribe una palabra:");
            string palabra = Console.ReadLine();

            char[] letrasPalabra = palabra.ToCharArray();

            int i = 0;
            int j = letrasPalabra.Length - 1;

            bool esPalindromo = true;

            while (i < j)
            {
                if (letrasPalabra[i] != letrasPalabra[j])
                {
                    esPalindromo = false;
                    break;
                }

                i++;
                j--;
            }

            if (esPalindromo)
            {
                Console.WriteLine($@"La palabra ""{palabra}"" es un palíndromo");
            }
            else
            {
                Console.WriteLine($@"La palabra ""{palabra}"" no es un palíndromo");
            }

        }

        // METODO PALABRAS ANAGRAMA
        public static void EsAnagrama()
        {
            Console.WriteLine("escribe dos palabras");

            string[] palabras = new string[2];

            for (int i = 0; i < 2; i++)
            {
                Console.Write($"palabra {i + 1}: ");
                palabras[i] = Console.ReadLine().ToLower();
            }

            if (palabras[0].Length == palabras[1].Length)
            {
                char[] palabra1 = palabras[0].ToCharArray();
                char[] palabra2 = palabras[1].ToCharArray();

                Array.Sort(palabra1);
                Array.Sort(palabra2);

                string x = new string(palabra1);
                string y = new string(palabra2);

                int z = string.Compare(x, y);

                if (z == 0)
                {
                    Console.WriteLine($@" las palabras ""{palabras[0]}"" y ""{palabras[1]}"" son anagramas");
                }
                else
                {
                    Console.WriteLine($@" las palabras ""{palabras[0]}"" y ""{palabras[1]}"" no son anagramas");
                }
            }
            else
            {
                Console.WriteLine("las palabras ingresadas no tienen la misma longitud");
            }

        }

        // METODO PALABRAS ISOGRAMA
        public static void EsIsograma()
        {
            Console.WriteLine("escribe una palabra");
            string palabra = Console.ReadLine();

            char[] letrasPalabra = palabra.ToCharArray();

            HashSet<char> letrasUnicas = new HashSet<char>();
            HashSet<char> letrasRepetidas = new HashSet<char>();

            foreach (char letra in letrasPalabra)
            {

                if (letrasUnicas.Contains(letra))
                {
                    letrasRepetidas.Add(letra);
                }
                else
                {
                    letrasUnicas.Add(letra);
                }

            }

            if (letrasRepetidas.Count >= 1)
            {
                Console.WriteLine($@"la palabra ""{palabra}"" no es un isograma");
            }
            else
            {
                Console.WriteLine($@"la palabra ""{palabra}"" es un isograma");
            }


        }
    }
}
