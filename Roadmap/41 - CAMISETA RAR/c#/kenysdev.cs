namespace exs41;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
41 CAMISETA RAR
------------------------------------

* EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip
*/

using System.IO;
using System.IO.Compression;

public class FileCompressor
{
    public static void CompressFile(string sourceFile, string zipFile)
    {
        if (!File.Exists(sourceFile))
            throw new FileNotFoundException($"El archivo fuente '{sourceFile}' no existe.");

        string zipDir = Path.GetDirectoryName(zipFile) ?? Directory.GetCurrentDirectory();
        if (!Directory.Exists(zipDir))
            throw new DirectoryNotFoundException($"El directorio '{zipDir}' no existe.");

        if (File.Exists(zipFile))
            throw new IOException($"El archivo zip '{zipFile}' ya existe.");

        try
        {
            using (FileStream zipToCreate = new(zipFile, FileMode.Create))
            {
                using ZipArchive archive = new(zipToCreate, ZipArchiveMode.Create);
                archive.CreateEntryFromFile(sourceFile, Path.GetFileName(sourceFile), CompressionLevel.Optimal);
            }

            Console.WriteLine($"Comprimido exitosamente '{sourceFile}' a '{zipFile}'");
        }
        catch (UnauthorizedAccessException)
        {
            throw new UnauthorizedAccessException($"No tienes permiso de escritura para '{zipFile}'");
        }
        catch (Exception ex)
        {
            throw new Exception($"Se produjo un error al comprimir el archivo: {ex.Message}", ex);
        }
    }

    public static void Main()
    {
        try
        {
            CompressFile("tmp.txt", @"D:\dev\tmp\file.zip");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error al comprimir: {ex.Message}");
        }
    }
}
