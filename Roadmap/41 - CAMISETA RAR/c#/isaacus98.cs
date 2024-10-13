/*
 * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.
 */



using System.IO.Compression;

namespace ComprimirArchivo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            using (ZipArchive zip = ZipFile.Open("test.zip", ZipArchiveMode.Create))
            {
                zip.CreateEntryFromFile("test.txt", "test.txt");
            }
        }
    }
}
