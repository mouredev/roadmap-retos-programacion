#include <stdio.h>
#include <windows.h>
/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 */
void BorrarArchivo(const char *nombreArchivo);
void LeerArchivo(const char *nombreArchivo);

int main()
{
    HANDLE hFile;
    DWORD dwBytesWritten = 0;
    char data[] = "Mi nombre es: john \n Edad: 21 \n Lenguaje de programción favorito: c";
    const char *nombreArchivo = "N0HagoNada.txt";
    hFile = CreateFile(nombreArchivo, // Nombre del archivo
                       GENERIC_WRITE, // Apertura para escritura
                       0,
                       NULL, // Atributos de seguridad predeterminados
                       CREATE_ALWAYS,
                       FILE_ATTRIBUTE_NORMAL,
                       NULL);
    if (hFile == INVALID_HANDLE_VALUE)
    {
        printf("Error al crear el archivo\n");
        return 1;
    }

    // Escribir en el archivo
    BOOL bErrorFlag = WriteFile(
        hFile,           // Manejador del archivo
        data,            // Buffer de datos a escribir
        strlen(data),    // Número de bytes a escribir
        &dwBytesWritten, // Número de bytes escritos
        NULL);           // Sin operación de escritura superpuesta

    if (FALSE == bErrorFlag)
    {
        printf("Error al escribir en el archivo\n");
    }
    else
    {
        if (dwBytesWritten != strlen(data))
        {
            // No se escribieron todos los bytes
            printf("Error: no todos los bytes fueron escritos\n");
        }
        else
        {
            // Escritura exitosa
            printf("Se escribieron %d bytes\n", dwBytesWritten);
        }
    }

    CloseHandle(hFile);

    LeerArchivo(nombreArchivo);

    // Borrar el archivo.
    BorrarArchivo(nombreArchivo);
    return 0;
}

void BorrarArchivo(const char *nombreArchivo)
{
    BOOL bErrorFlag = DeleteFileA(nombreArchivo);

    if (!bErrorFlag)
    {
        printf("No se puede borrar el archivo.\n");
    }
    else
    {
        printf("Archivo borrado exitosamente.\n");
    }
}
void LeerArchivo(const char *nombreArchivo)
{
    HANDLE hFile;
    DWORD dwBytesRead = 0;
    char buffer[1024] = {0}; // Asumiendo que el archivo es menor que 1024 bytes para simplificar

    hFile = CreateFile(nombreArchivo,
                       GENERIC_READ,
                       FILE_SHARE_READ,
                       NULL,
                       OPEN_EXISTING,
                       FILE_ATTRIBUTE_NORMAL,
                       NULL);

    if (hFile == INVALID_HANDLE_VALUE)
    {
        printf("No se puede abrir el archivo para leer.\n");
        return;
    }

    BOOL bErrorFlag = ReadFile(hFile, buffer, 1024, &dwBytesRead, NULL);

    if (!bErrorFlag)
    {
        printf("No se puede leer el archivo.\n");
    }
    else
    {
        printf("Contenido del archivo:\n%s\n", buffer);
    }

    CloseHandle(hFile);
}