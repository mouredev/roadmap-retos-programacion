program Conjuntos;
uses Crt;

type
    Digitos = set of 0 .. 100;   // Tipos conjunto (set)

var
    Impares, Primos, Set1 : Digitos;

function mostrarSet(s : Digitos) : String;
var
    i : Integer;
    c : String;
    num : String;
begin
    c := '';
    for i := 0 to 100 do
        if i in s then
        begin
            if (c <> '') then c := c + ', ';
            Str(i, num);
            c := c + num;
        end;
    mostrarSet := '{' + c + '}';
end;

begin
    ClrScr;

    Impares := [11, 13, 15, 17, 19, 21, 23, 25, 27, 29];
    Primos := [1, 3, 5, 7, 11, 13, 17];

    WriteLn('Dados dos conjuntos I = {11, 13, 15, 17, 19, 21, 23, 25, 27, 29} y P = {1, 3, 5, 7, 11, 13, 17}');
    WriteLn('');

    Set1 := Impares + Primos;

    WriteLn('Union de conjuntos -> I + P = ' + mostrarSet(Set1));
    WriteLn('');

    WriteLn('Diferencia de conjuntos');
    Set1 := Impares - Primos;
    WriteLn('I - P = ' + mostrarSet(Set1));
    Set1 := Primos - Impares;
    WriteLn('P - I = ' + mostrarSet(Set1));
    WriteLn('');

    Set1 := Impares * Primos;
    WriteLn('Interseccion de conjuntos -> I * P = ', mostrarSet(Set1));
    WriteLn('');

    Set1 := Impares >< Primos;
    WriteLn('Diferencia simetrica de conjuntos -> I >< P = ', mostrarSet(Set1));
    WriteLn('');

    Include(Impares, 31);
    WriteLn('Incluir el elemento 31 al conjunto I:');
    WriteLn('I = ', mostrarSet(Impares));
    WriteLn('');

    Exclude(Primos, 17);
    WriteLn('Excluir el elemento 17 al conjunto P:');
    WriteLn('P = ', mostrarSet(Primos));
    WriteLn('');

    WriteLn('Verificar si el elemento 31 esta en el conjunto I : ', 31 in Impares);
    WriteLn('Verificar si el elemento 17 esta en el conjunto P : ', 17 in Primos);
end.
