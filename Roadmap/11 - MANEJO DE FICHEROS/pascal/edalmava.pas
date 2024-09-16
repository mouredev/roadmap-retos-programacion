program Archivos;

uses Crt;

var
    f : Text;   // Declaracion de una variable archivo de tipo texto
    linea : String;

begin

    ClrScr;

    Assign (f, 'edalmava.txt');   // Asocia la variable de archivo a un nombre de archivo en disco
    ReWrite (f);                  // Crea un nuevo archivo para operacion de escritura edalmava.txt

    WriteLn (f, 'Edalmava');      // Escribir datos en el archivo de texto
    WriteLn (f, '30');
    WriteLn (f, 'PHP');

    Reset (f);                    // Abrir archivo edalmava.txt para lectura

    // Leyendo archivo edalmava.txt
    While not eof (f) do          // leer linea a linea hasta alcanzar el final del archivo
    begin
        ReadLn (f, linea);
        WriteLn (linea);          // Imprimir linea por consola o pantalla
    end;

    close (f);                    // Cierra todas las entradas y salidas al archivo f

    {I+}
    Erase (f);                    // Borra el archivo
    {I-}
    if IOResult = 0 then
        WriteLn ('Se ha borrado el archivo')
    else
        WriteLn ('Error al borrar el archivo');

end.
