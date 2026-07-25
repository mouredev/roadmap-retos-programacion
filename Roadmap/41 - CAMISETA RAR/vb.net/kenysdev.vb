' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 41 CAMISETA RAR
' ------------------------------------
'* EJERCICIO
'* ¿Has visto la camiseta.rar?
'* https://x.com/MoureDev/status/1841531938961592740
'*
'* Crea un programa capaz de comprimir un archivo 
'* en formato .zip (o el que tú quieras).
'* - No subas el archivo o el zip.

Imports System.IO
Imports System.IO.Compression


Public Class FileCompressor
    Public Shared Sub CompressFile(sourceFile As String, zipFile As String)
        If Not File.Exists(sourceFile) Then
            Throw New FileNotFoundException($"El archivo fuente '{sourceFile}' no existe.")
        End If

        Dim zipDir = If(Path.GetDirectoryName(zipFile), Directory.GetCurrentDirectory())

        If Not Directory.Exists(zipDir) Then
            Throw New DirectoryNotFoundException($"El directorio '{zipDir}' no existe.")
        End If

        If File.Exists(zipFile) Then
            Throw New IOException($"El archivo zip '{zipFile}' ya existe.")
        End If

        Try
            Using zipToCreate As New FileStream(zipFile, FileMode.Create),
                  archive As New ZipArchive(zipToCreate, ZipArchiveMode.Create)

                archive.CreateEntryFromFile(sourceFile, Path.GetFileName(sourceFile), CompressionLevel.Optimal)
            End Using

            Console.WriteLine($"Comprimido exitosamente '{sourceFile}' a '{zipFile}'")

        Catch ex As UnauthorizedAccessException
            Throw New UnauthorizedAccessException($"No tienes permiso de escritura para '{zipFile}'")
        Catch ex As Exception
            Throw New Exception($"Se produjo un error al comprimir el archivo: {ex.Message}", ex)
        End Try
    End Sub

    Public Shared Sub Main()
        Try
            CompressFile("D:\dev\tmp\tmp.txt", "D:\dev\tmp\file.zip")
        Catch ex As Exception
            Console.WriteLine($"Error al comprimir: {ex.Message}")
        End Try
    End Sub
End Class
