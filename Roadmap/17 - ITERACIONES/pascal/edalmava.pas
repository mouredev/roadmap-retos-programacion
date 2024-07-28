program Iteraciones;
uses Crt;
var
    i: Integer;

procedure imprimirNumeros(num : Integer);
begin
    if num <= 10 then
    begin
        WriteLn(num);
        imprimirNumeros(num + 1);
    end;
end;

begin
    ClrScr;
    // Usando un ciclo for
    WriteLn('Usando un ciclo for: ');
    for i := 1 to 10 do
        WriteLn(i);
    WriteLn('');

    // Usando un ciclo while
    WriteLn('Usando un ciclo while: ');
    i := 1;
    while i <= 10 do
    begin
        WriteLn(i);
        i := i + 1;
    end;
    WriteLn('');

    // Usando un ciclo repeat
    WriteLn('Usando un ciclo repeat: ');
    i := 1;
    repeat
        WriteLn(i);
        i := i + 1;
    until i > 10;
    WriteLn('');

    // Usando Recursividad
    WriteLn('Usando Recursividad: ');
    imprimirNumeros(1);
    WriteLn('');

    ReadLn;
end.
