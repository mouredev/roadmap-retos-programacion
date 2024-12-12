using System.IO.Compression;

class Program
{
    static void Main(string[] args)
    {
        string filePath = @".\Semana 41";
        string zipPath = @".\result.zip";

        ZipFile.CreateFromDirectory(filePath, zipPath);
    }
}