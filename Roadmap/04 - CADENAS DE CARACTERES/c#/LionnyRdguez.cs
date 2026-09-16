using System;
using System.Dynamic;
using System.Linq;


namespace Ejercicio_04
{
    //Es importante mencionar que las cadenas de texto en C# no se pueden modificar, por lo tanto
    //cuando usamos alguna de las opciones para trabajar con cadenas de texto en C#, la mayoria
    //lo que hacen es devolver una nueva cadena con las modificaciones que hicimos o devolver
    //informacion sobre la cadena con la que estamos trabajando
    class Program
    {
        static void Main(string[] args)
        {
            Ejercicio ejercicio = new Ejercicio();
            ejercicio.AccesoACaracterEspecifico();
            ejercicio.Comparacion();
            ejercicio.Concatenacion();
            ejercicio.ConvertirArray();
            ejercicio.ConvertirMayMin();
            ejercicio.Division();
            ejercicio.Eliminacion();
            ejercicio.Interpolacion();
            ejercicio.Insercion();
            ejercicio.Longitud();
            ejercicio.Recorrido();
            ejercicio.Reemplazo();
            ejercicio.Repeticion();
            ejercicio.Relleno();
            ejercicio.Substring();
            ejercicio.Verificaciones();
            ejercicio.VerificarNuloVacio();
           
            DificultadExtra dificultadExtra = new DificultadExtra("reconocer", "reconocer");
            bool[] palindromos = dificultadExtra.Palindromos();
            Console.WriteLine($"La primera palabra es palindromo? {palindromos[0]}");
            Console.WriteLine($"La segunda palabra es palindromo? {palindromos[1]}");
            bool anagramas = dificultadExtra.Anagramas();
            Console.WriteLine($"Las palabras son anagramas? {anagramas}");
            bool[] isogramas = dificultadExtra.Isograma();
            Console.WriteLine($"La primera palabra es isograma? {isogramas[0]}");
            Console.WriteLine($"La segunda palabra es isograma? {isogramas[1]}");



        }
    }

    public class Ejercicio
    {
        private string Cadena_1 {get; set;} = "Tangamandapio";
        private string Cadena_2 {get; set;} = "Paulo Londra Transexual";

        

        public void AccesoACaracterEspecifico()
        {
            char caracterEspecifico = Cadena_1[3];
            //esta variable toma el valor de la cuarta letra de la palabra porque recordar que las cadenas
            //de caracteres en C# empiezan en la posicion cero
            Console.WriteLine("La cuarta letra de la palabra Tangamandapio es: " + caracterEspecifico);
        }

        public void Longitud()
        {
            sbyte longitudCadena = (sbyte)Cadena_2.Length;
            Console.WriteLine("La longitud de la cadena es: " + longitudCadena);
        }

        public void Substring()
        {
            string subCadena = Cadena_2.Substring(6, 7); //Se para en la posicion 6 y toma 7 caracteres
            string subCadena2 = Cadena_1.Substring(3); // Se para en la posicion 3 y toma todos los caracteres a la derecha
            Console.WriteLine("La subcadena de la cadena 2 es: " + subCadena);
            Console.WriteLine("La subcadena de la cadena 1 es: " + subCadena2);
        }

        public void Concatenacion()
        {
            string concatenacionV1 = Cadena_1 + Cadena_2;
            string concatenacionV2 = String.Concat(Cadena_1,Cadena_2);
            string concatenacionV3 = string.Concat(Cadena_1," ", Cadena_2); //Se pueden concatenar mas de dos cadenas
            
            string[] palabras = {"Hola","soy","LionnyRdguez"};
            string concatenacionV4 = string.Join(" ", palabras);

            Console.WriteLine("ConcatenacionV1: "+ concatenacionV1);
            Console.WriteLine("ConcatenacionV2: "+ concatenacionV2);
            Console.WriteLine("ConcatenacionV3: "+ concatenacionV3);
            Console.WriteLine("ConcatenacionV4: "+ concatenacionV4);

        }

        public void Repeticion()
        {
            string cadenaRepetida = string.Concat(Enumerable.Repeat("Hola",3));
            Console.WriteLine("Repetir Hola 3 veces" + cadenaRepetida);
        }

        public void Recorrido()
        {
            foreach (char c in Cadena_1) //Primera forma 
            {
                Console.WriteLine(c + " ");
            }

            for(int i = 0; i < Cadena_2.Length; i++) //segunda forma
            {
                Console.WriteLine(Cadena_2[i] + " ");
            }

        }

        public void ConvertirMayMin()
        {
            Console.WriteLine("Cadena_1 en Mayusculas: " + Cadena_1.ToUpper());
            Console.WriteLine("Cadena_2 en Minucula: " + Cadena_2.ToLower());
        }

        public void Reemplazo()
        {
            string reemplazoV1 = Cadena_2.Replace("Paulo","Buuuuuuuenas");
            string reemplazoV2 = Cadena_1.Replace("i" , "I");
            Console.WriteLine("Reemplaza una palabra por otra: " + Cadena_2 +
            "es reemplazada por: " + reemplazoV1);
            Console.WriteLine("Reemplaza caracteres individuales: " + Cadena_1 +
            "es reemplazado un caracter por otro: " + reemplazoV2);
        }

        public void Division()
        {
            string frase = "Manzana,Pera,Mamoncillo,Chirimolla";
            string[] frutas = frase.Split(','); 
            // Devuelve un arreglo cuyos elementos contienen las subcadenas 
            //del string original separadas por un caracter que especificamos.

            foreach(string fruta in frutas)
            {
                Console.WriteLine(" " + fruta);
            }

            string datos = "uno,,cero, ,uno";
            string[] bits = datos.Split(new char[] {',' , ' '}, StringSplitOptions.RemoveEmptyEntries);
            //Devuelve un arreglo de las subcadenas delimitadas por uno o mas separadores en el arreglo que
            //hay dentro del parentesis despues de Split. La segunda entrada es una opcion que elimina entradas
            //vacias

            Console.WriteLine("El bit mas significativo es: " + bits[0]);
        }

        public void Interpolacion()
        {
            int edad = 21;
            string nombre = "Lionny";
            string pais = "Cuba";

            string mensaje = $"Hola me llamo {nombre}, tengo {edad} años, vivo en {pais}";
            Console.WriteLine(mensaje);
        }

        public void Verificaciones()
        {
            string texto = "El perro corre en el parque";
            Console.WriteLine($"Texto: {texto}");
            Console.WriteLine($"Contiene 'perro'? {texto.Contains("perro")}"); //Devuelve bool si contiene o no la cadena
            Console.WriteLine($"Contiene 'gato'? {texto.Contains("gato")}");
            Console.WriteLine($"Empieza con 'El'? {texto.StartsWith("El")}"); //Devuelve bool si empieza o no con la cadena
            Console.WriteLine($"Empieza con 'el'? {texto.StartsWith("el")}"); // distingue mayusculas
            Console.WriteLine($"Termina con 'parque'? {texto.EndsWith("parque")}"); //Devuelve bool si termina o no con la cadena
            Console.WriteLine($"Posicion inicial de 'perro': {texto.IndexOf("perro")}");
            //Devuelve la posision inicial de la cadena o -1 si no la encuentra
        }

        public void EliminarEspacios()
        {
            string Cadena = "   Hola   ";
            Console.WriteLine("Cadena sin espacios: " + Cadena.Trim()); //devuelve una cadena sin espacios delante o detras
            Console.WriteLine("Cadena sin espacios delante: " + Cadena.TrimStart());
            Console.WriteLine("Cadena sin espacios detras: " + Cadena.TrimEnd());

        }

        public void Comparacion()
        {
            string a = "hola";
            string b = "HOLA";
            Console.WriteLine($"a = '{a}', b = '{b}'");
            Console.WriteLine($"a == b? {a == b}"); // false, distingue mayusculas
            Console.WriteLine($"a.Equals(b)? {a.Equals(b)}"); // false
            // Comparacion ignorando mayúsculas
            Console.WriteLine($"Equals con ignoreCase: {string.Equals(a, b, StringComparison.OrdinalIgnoreCase)}");
            // CompareTo devuelve negativo, cero, positivo segun el orden
            Console.WriteLine($"CompareTo: {a.CompareTo(b)}"); // positivo porque 'h' > 'H' en ASCII

        }

        public void Insercion()
        {
            string mensaje = Cadena_1.Insert(4 , Cadena_2); //Inserta la cadena 2 en el indice 4 de la cadena 1
            Console.WriteLine("Insercion: " + mensaje);
        }

        public void Eliminacion()
        {
            string eliminar = "Extraño a mi ex.";
            Console.WriteLine("Eliminar a partir de indice: " + eliminar.Remove(7)); //devuelve una cadena sin 'a mi ex'
            Console.WriteLine("Elimina una longitud especifica a partir de un indice: " +
            eliminar.Remove(7,4)); //A partir del indice 7 elimina 4 caracteres
        }

        public void Relleno()
        {
            string num = "42";
            Console.WriteLine($"Original: '{num}'");
            Console.WriteLine($"PadLeft(5, '0'): '{num.PadLeft(5, '0')}'"); // "00042"
            Console.WriteLine($"PadRight(5, '*'): '{num.PadRight(5, '*')}'"); // "42***"
        }

        public void VerificarNuloVacio()
        {
            string nula = null;
            string vacia = "";
            string conContenido = "texto";
            Console.WriteLine($"string.IsNullOrEmpty(nula): {string.IsNullOrEmpty(nula)}"); // True
            Console.WriteLine($"string.IsNullOrEmpty(vacia): {string.IsNullOrEmpty(vacia)}"); // True
            Console.WriteLine($"string.IsNullOrEmpty(conContenido): {string.IsNullOrEmpty(conContenido)}"); // False
            Console.WriteLine($"string.IsNullOrWhiteSpace(vacia): {string.IsNullOrWhiteSpace(vacia)}"); // True
            
        }

        public void ConvertirArray()
        {
            char[] array = Cadena_1.ToCharArray();
            foreach(char c in array)
            {
                Console.WriteLine(c);
            }
        }

    }

    public class DificultadExtra
    {
        string Palabra_1 {get; set;} = String.Empty;
        string Palabra_2 {get; set;} = string.Empty;

        public DificultadExtra(){}

        public DificultadExtra(string palabra_1, string palabra_2)
        {
            this.Palabra_1 = palabra_1;
            this.Palabra_2 = palabra_2;
        }

        public bool[] Palindromos() // Se escribe igual al derecho y al reves
        {
            bool primeraPalabra;
            bool segundaPalabra;

            string palabra_1Min = (Palabra_1 == null) ? string.Empty : Palabra_1.ToLower();
            string palabra_2Min = (Palabra_2 == null) ? string.Empty : Palabra_2.ToLower();

            char[] primera = palabra_1Min.ToCharArray();
            char[] segunda = palabra_2Min.ToCharArray();
            
            string invertida1 = new string(primera.Reverse().ToArray());
            string invertida2 = new string(segunda.Reverse().ToArray());

            primeraPalabra = (palabra_1Min == invertida1);
            
            if(invertida2 == palabra_2Min)
            {
                segundaPalabra = true;
            }
            else
            {
                segundaPalabra = false;
            }

            bool[] Respuesta = {primeraPalabra, segundaPalabra};
            return Respuesta;
        }

        public bool Anagramas() //Una se puede formar reordenando las letras de la otra y viceversa
        {
            if(Palabra_1 == null || Palabra_2 == null)
            {
                return false;
            }

            if(Palabra_1.Length != Palabra_2.Length)
            {
                return false;
            }
            else
            {
            string primeraPalabraMin = Palabra_1.ToLower();
            string segundaPalabraMin = Palabra_2.ToLower();

            char[] arrayPrimera = primeraPalabraMin.ToCharArray();
            char[] arraySegunda = segundaPalabraMin.ToCharArray();

            Array.Sort(arrayPrimera);
            Array.Sort(arraySegunda);

            string PrimeraOrdenado = new string(arrayPrimera);
            string SegundaOrdenado = new string(arraySegunda);

            if(String.Compare(PrimeraOrdenado, SegundaOrdenado) == 0)
                {
                    return true;
                }
                else
                {
                    return false;
                }

            }
        }

        public bool[] Isograma() //No tiene letras repetidas
        {
            bool primeraPalabra = true;
            bool segundaPalabra = true;
            HashSet<char> caracteres1 = new HashSet<char>();
            HashSet<char> caracteres2 = new HashSet<char>();

            string palabra_1Min = (Palabra_1 == null) ? string.Empty : Palabra_1.ToLower();
            string palabra_2Min = (Palabra_2 == null) ? string.Empty : Palabra_2.ToLower();

            for(int i = 0; i < palabra_1Min.Length; i++){
                if (!caracteres1.Add(palabra_1Min[i]))
                {
                    primeraPalabra = false;
                    break;
                }
               

            }
            for(int i = 0; i < palabra_2Min.Length; i++){
                if (!caracteres2.Add(palabra_2Min[i]))
                {
                    segundaPalabra = false;
                    break;
                }
                
            
                    
                
            }
           
           

                bool[] Resultado = {primeraPalabra, segundaPalabra};
                return Resultado;
        
        }
        }}
    
