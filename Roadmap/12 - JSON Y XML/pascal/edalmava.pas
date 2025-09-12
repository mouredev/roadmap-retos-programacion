program json;
uses Crt, SysUtils;
var
    xmlFile, jsonFile: Text;
    name, birthdate, linea: string;
    age: Integer;
    languages: array[1..3] of string;

begin
    ClrScr;

    name := 'Edwin Alberto Martinez Vanegas';
    age := 30;
    birthdate := '1994-08-11';
    languages[1] := 'Pascal';
    languages[2] := 'Python';
    languages[3] := 'JavaScript';

    // Crear archivo XML
    Assign(xmlFile, 'data.xml');
    Rewrite(xmlFile);
    Writeln(xmlFile, '<?xml version="1.0" encoding="UTF-8"?>');
    Writeln(xmlFile, '<person>');
    Writeln(xmlFile, '  <name>', name, '</name>');
    Writeln(xmlFile, '  <age>', age, '</age>');
    Writeln(xmlFile, '  <birthdate>', birthdate, '</birthdate>');
    Writeln(xmlFile, '  <languages>');
    Writeln(xmlFile, '    <language>', languages[1], '</language>');
    Writeln(xmlFile, '    <language>', languages[2], '</language>');
    Writeln(xmlFile, '    <language>', languages[3], '</language>');
    Writeln(xmlFile, '  </languages>');
    Writeln(xmlFile, '</person>');

    // Crear archivo JSON
    Assign(jsonFile, 'data.json');
    Rewrite(jsonFile);
    Writeln(jsonFile, '{');
    Writeln(jsonFile, '  "name": "', name, '",');
    Writeln(jsonFile, '  "age": ', age, ',');
    Writeln(jsonFile, '  "birthdate": "', birthdate, '",');
    Writeln(jsonFile, '  "languages": [');
    Writeln(jsonFile, '    "', languages[1], '",');
    Writeln(jsonFile, '    "', languages[2], '",');
    Writeln(jsonFile, '    "', languages[3], '"');
    Writeln(jsonFile, '  ]');
    Writeln(jsonFile, '}');

    // Mostrar contenido de los archivos

    Reset(xmlFile);
    Writeln('Contenido del archivo XML:');
    while not Eof(xmlFile) do
    begin
        Readln(xmlFile, linea);
        Writeln(linea);
    end;
    Close(xmlFile);

    Reset(jsonFile);
    Writeln('Contenido del archivo JSON:');
    while not Eof(jsonFile) do
    begin
        Readln(jsonFile, linea);
        Writeln(linea);
    end;
    Close(jsonFile);

    // Borrar los archivos
    {I+}
    Erase(xmlFile);
    {I-}
    if IOResult = 0 then
        Writeln('Archivo XML borrado con exito.')
    else
        Writeln('Error al borrar el archivo XML.');

    {I+}
    Erase(jsonFile);
    {I-}
    if IOResult = 0 then
        Writeln('Archivo JSON borrado con exito.')
    else
        Writeln('Error al borrar el archivo JSON.');
end.
