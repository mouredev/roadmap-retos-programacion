namespace _04_CADENAS
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declaracion de Cadenas
            string cadena1 = "Hola, soy Jose Esmil y estoy aprendiendo C#";
            var cadena2 = "Retos de Programacion!";

            // Acceso a caracteres especificos
            Console.WriteLine($"Primera Forma (Llaves): { cadena1[0] }");
            Console.WriteLine($"Segunda Forma (ElementAt): { cadena2.ElementAt(0) }");

            // Longitud de Cadenas
            Console.WriteLine($"Longitud (Length): { cadena1.Length }");
            Console.WriteLine($"Longitud (Count): { cadena2.Count() }");

            // Subcadenas
            Console.WriteLine($"Subcadena 1: {cadena1.Substring(6, 15)}");
            Console.WriteLine($"Subcadena 2: {cadena2.Substring(9, 13)}");

            // Concatenacion
            Console.WriteLine($"Concatenacion Concat: { string.Concat(cadena1, cadena2) }");
            Console.WriteLine($"Concatenacion +: {cadena2 + cadena1}");

            // Repeticion (Metodo new String)
            var numeral = cadena1[cadena1.Length - 1];
            Console.WriteLine($"Repeticion { new String(numeral, 7) }");

            // Recorrido
            foreach(var letra in cadena1)
            {
                Console.Write(letra + " ");
            }

            // Conversion a Mayusculas y Minusculas
            Console.WriteLine($"Mayusculas { cadena1.ToUpper() }");
            Console.WriteLine($"Minusculas { cadena2.ToLower() }");

            // Reemplazo
            var reemplazar1 = cadena1.Replace("soy", "me llamo");
            var reemplazar2 = cadena2.Replace("Retos", "Desafios");
            Console.WriteLine($"Reemplazo 1: {reemplazar1}");
            Console.WriteLine($"Reemplazo 2: {reemplazar2}");

            // Division
            string[] palabraArr = reemplazar1.Split(' ');
            Array.ForEach(palabraArr, (palabra) => Console.WriteLine(palabra));

            // Union
            string fraseUnida = string.Join('_', palabraArr);
            Console.WriteLine($"Frase Unida: {fraseUnida}");

            // Interpolacion
            string country = "Dominican Republic";
            string message = $"Made in {country}";
            Console.WriteLine($"Interpolacion: {message}");

            // Verificacion (Contains, StartsWith, EndsWith)
            Console.WriteLine($"Contains: {country.Contains("Republic")}");
            Console.WriteLine($"StartsWith: {country.StartsWith("Republic")}");
            Console.WriteLine($"EndsWith: {message.EndsWith("Dominican Republic")}");

            // Eliminar Espacios (Trim)
            string conEspacios = "    C# is cool    ";
            Console.WriteLine($"Trim: { conEspacios.Trim() }");
            Console.WriteLine($"TrimStart: { conEspacios.TrimStart() }");
            Console.WriteLine($"TrimEnd: { conEspacios.TrimEnd() }");


            // Equals (Equivalente)
            Console.WriteLine(country.Equals("Dominican Republic"));

            // IsNullOrEmpty
            string str = "";
            bool isNullOrEmpty = string.IsNullOrEmpty(str);
            Console.WriteLine(isNullOrEmpty);

            // EJERCICIO EXTRA (COMPROBACIONES)

            // Palindromo
            Console.WriteLine("Palindromo: " + Check.IsPalindrome("aprendiendo c#", "#c odneidnerpa"));

            // Isograma
            Console.WriteLine("Isograma: " + Check.IsIsogram("murcielago"));

            // Anagrama
            Console.WriteLine("Anagrama: " + Check.IsAnagram("roma", "amor"));

        }

        class Check
        {
            public static bool IsPalindrome(string word, string word2)
            {
                return word.Reverse().ToArray().SequenceEqual(word2.ToCharArray());
            }

            public static bool IsIsogram(string word)
            {
                var newString = word.ToLower();
                HashSet<char> chars = new HashSet<char>();

                foreach (char c in newString)
                {
                    if (chars.Contains(c))
                    {
                        return false;
                    }

                    chars.Add(c);
                }

                return true;
            }

            public static bool IsAnagram(string word1, string word2)
            {
                var arrWord1 = word1.ToCharArray();
                var arrWord2 = word2.ToCharArray();

                Array.Sort(arrWord1);
                Array.Sort(arrWord2);

                return arrWord1.SequenceEqual(arrWord2);
            }
        }
    }
}