program miguelex;

var
  cadena1, cadena2: string;
  longitud, position: integer;
  
{ Funcion que verifica si una cadena es un palindromo }
function esPalindromo(cadena: string): boolean;
var
  i: integer;
begin
    esPalindromo := true;
    { Pasamos la cadena a minusculas }
    cadena := lowercase(cadena);
    for i := 1 to length(cadena) do
        if cadena[i] <> cadena[length(cadena) - i + 1] then
            esPalindromo := false;
end;

{ Funcion que verifica si una cadena es anagrama }
function esAnagrama(cadena1, cadena2: string): boolean;
var
  i, j: integer;
  encontrado: boolean;
begin
    esAnagrama := true;
    { Pasamos las cadenas a minusculas }
    cadena1 := lowercase(cadena1);
    cadena2 := lowercase(cadena2);
    for i := 1 to length(cadena1) do
    begin
        encontrado := false;
        for j := 1 to length(cadena2) do
            if cadena1[i] = cadena2[j] then
                encontrado := true;
        if not encontrado then
            esAnagrama := false;
    end;
end;

{ Funcion que verifica de una cadena es Isogramas }
function esIsograma(cadena: string): boolean;
var
  i, j: integer;
begin
    esIsograma := true;
    { Pasamos la cadena a minusculas }
    cadena := lowercase(cadena);
    for i := 1 to length(cadena) do
        for j := i + 1 to length(cadena) do
            if cadena[i] = cadena[j] then
                esIsograma := false;
end;

begin

    writeln('Introduzca la primera cadena');
    readln(cadena1);
    
    writeln('Vamos a hacer las pruebas sobre la cadena ', cadena1);
    writeln();

    { Longitud de la cadena }
    longitud := length(cadena1);
    writeln('La longitud de la cadena es --> ', longitud);
    writeln();
    
    { Concatenar cadenas }
    writeln('Introduzca la segunda cadena');
    readln(cadena2);
    writeln('Vamos a concatenar la cadena ', cadena1, ' con la cadena ', cadena2);
    writeln('El resultado es --> ', cadena1 + ' ' + cadena2);
    writeln();

    { Comparar cadenas }
    writeln('Vamos a comparar la cadena ', cadena1, ' con la cadena ', cadena2);
    if cadena1 = cadena2 then
        writeln('Las cadenas son iguales')
    else
        writeln('Las cadenas son distintas');
    writeln();
    
    { Copiar cadenas }
    writeln('Vamos a copiar la cadena ', cadena1, ' en la cadena ', cadena2);
    cadena2 := cadena1;
    writeln('El resultado es -->  ', cadena2);
    writeln();

    { Extraer una subcadena }
    writeln('Vamos a extraer una subcadena de la cadena ', cadena1);
    writeln('Introduzca la posicion inicial');
    readln(position);
    writeln('Introduzca la longitud');
    readln(longitud);
    cadena2 := copy(cadena1, position, longitud);
    writeln('El resultado es --> ', cadena2);
    writeln();

    { Insertar una subcadena }
    writeln('Vamos a insertar una subcadena en la cadena ', cadena1);
    writeln('Introduzca la posicion inicial');
    readln(position);
    writeln('Introduzca la subcadena');
    readln(cadena2);
    insert(cadena2, cadena1, position);
    writeln('El resultado es --> ', cadena1);
    writeln();

    { Eliminar una subcadena }
    writeln('Vamos a eliminar una subcadena en la cadena ', cadena1);
    writeln('Introduzca la posicion inicial');
    readln(position);
    writeln('Introduzca la longitud');
    readln(longitud);
    delete(cadena1, position, longitud);
    writeln('El resultado es --> ', cadena1);
    writeln();

    { Buscar una subcadena }
    writeln('Vamos a buscar una subcadena en la cadena ', cadena1);
    writeln('Introduzca la subcadena');
    readln(cadena2);
    position := pos(cadena2, cadena1);
    if position <> 0 then
        writeln('La subcadena se encuentra en la posicion ', position)
    else
        writeln('La subcadena no se encuentra en la cadena');
    writeln();

    { Convertir a mayusculas }
    writeln('Vamos a convertir la cadena ', cadena1, ' a mayusculas');
    cadena2 := upcase(cadena1);
    writeln('El resultado es --> ', cadena2);
    writeln();

    { Convertir a minusculas }
    writeln('Vamos a convertir la cadena ', cadena1, ' a minusculas');
    cadena2 := lowercase(cadena1);
    writeln('El resultado es --> ', cadena2);
    writeln();

    { Invertir cadena }
    writeln('Vamos a invertir la cadena ', cadena1);
    cadena2 := '';
    for position := length(cadena1) downto 1 do
        cadena2 := cadena2 + cadena1[position];
    writeln('El resultado es --> ', cadena2);
    writeln();

    { Eliminar espacios en blanco }
    writeln('Vamos a eliminar los espacios en blanco de la cadena ', cadena1);
    cadena2 := '';
    for position := 1 to length(cadena1) do
        if cadena1[position] <> ' ' then
            cadena2 := cadena2 + cadena1[position];
    writeln('El resultado es --> ', cadena2);
    writeln();

    { Eliminar caracteres no alfabeticos }
    writeln('Vamos a eliminar los caracteres no alfabeticos de la cadena ', cadena1);
    cadena2 := '';
    for position := 1 to length(cadena1) do
        if cadena1[position] in ['a'..'z', 'A'..'Z'] then
            cadena2 := cadena2 + cadena1[position];
    writeln('El resultado es --> ', cadena2);
    writeln();

    { Eliminar vocales }
    writeln('Vamos a eliminar las vocales de la cadena ', cadena1);
    cadena2 := '';
    for position := 1 to length(cadena1) do
        if cadena1[position] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] then
            cadena2 := cadena2 + cadena1[position];
    writeln('El resultado es --> ', cadena2);
    writeln();

    { Extra }

    WriteLn(esPalindromo('Ana'));
    WriteLn(esPalindromo('Esto no es un palindromo'));
    WriteLn(esPalindromo('Ana lava lana'));

    WriteLn(esAnagrama('amor', 'roma'));
    WriteLn(esAnagrama('monja', 'jamon'));
    WriteLn(esAnagrama('monja', 'jamoncito'));

    WriteLn(esIsograma('murcielago'));
    WriteLn(esIsograma('murcielagoo'));

end.    