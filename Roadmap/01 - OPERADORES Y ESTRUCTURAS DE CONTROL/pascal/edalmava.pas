program Operadores;
uses Crt, Math;
type
    dias = (Domingo, Lunes, Martes, Miercoles, Jueves, Viernes, Sabado);
var
    x, y, I : Integer;
    cad1, cad2 : String;
    c : Char;
    d : dias;

begin
    ClrScr;
    WriteLn('Operador de asignacion := ');
    WriteLn('x := 5  -> 5 se asigna a x');
    WriteLn('y := 10 -> 10 se asigna a y');
    x := 5;
    y := 10;
    WriteLn('');
    WriteLn('Operadores Aritmeticos Binarios');
    WriteLn('Suma: x + y = ', x + y);
    WriteLn('Resta: y - x = ', y - x);
    WriteLn('Multiplicacion: x * y = ', x * y);
    WriteLn('Exponenciacion: y ** x = ', y ** x);      // Para usar el operador ** se debe agregar la unidad Math
    WriteLn('Division: x / y = ', (x / y):2:2);
    WriteLn('Division Entera: x Div y = ', x Div y);
    WriteLn('Modulo: y mod 2 = ', y mod 2);
    WriteLn('');
    WriteLn('Operadores Aritmeticos Unarios');
    x := +7;
    y := -7;
    Writeln('+ especifica que el valor es positivo: +', x);
    WriteLn('- especifica que el valor es negativo: ', y);
    WriteLn('');
    WriteLn('Operadores Relacionales');
    WriteLn('Igual: 5 = 5 se evalua a ', 5 = 5);
    WriteLn('No Igual: 5 <> 4 se evalua a ', 5 <> 4);
    WriteLn('Menor que: 20 < 20 se evalua a ', 20 < 20);
    WriteLn('Menor o igual que: 20 <= 20 se evalua a ', 20 <= 20);
    WriteLn('Mayor que: 20 > 10 se evalua a ', 20 > 10);
    WriteLn('Mayor o igual que: 20 >= 20 se evalua a ', 20 >= 20);
    WriteLn('');
    WriteLn('Operadores Booleanos');
    WriteLn('Negacion not: not true se evalua a ', not true);
    WriteLn('Negacion not: not false se evalua a ', not false);
    WriteLn('Y logico: true and true se avalua a ', true and true);
    WriteLn('O logico: true or false se evalua a ', true or false);
    WriteLn('XOR logico: false xor false se evalua a ', false xor false);
    WriteLn('');
    WriteLn('Operador de Concatenacion de Cadenas +');
    cad1 := 'Hola ';
    cad2 := 'Pascal';
    WriteLn('Cadena 1: ', cad1);
    WriteLn('Cadena 2: ', cad2);
    Writeln('Concatenando Cadena 1 + Cadena2: ', cad1 + cad2);
    WriteLn('');
    WriteLn('Operadores de Conjuntos (Set) - Se tratan en el ejercicio #18 sobre conjuntos');
    WriteLn('');
    WriteLn('Estructuras de Control');
    WriteLn('Sentencia Case');
    c := 'b';
    Case c of
        'a' : WriteLn('Se selecciono a');
        'b' : WriteLn('Se selecciono b');
        'c' : WriteLn('Se selecciono c');
    else
        Writeln('Opcion seleccionada invalida');
    end;
    WriteLn('Sentencia if .. then .. else');
    d := Lunes;
    Write('Lunes es: ');
    If d in [Lunes..Viernes] then
        Write('Dia de trabajo')
    else
        Write('Dia de descanso');
    WriteLn('');
    WriteLn('');
    WriteLn('Sentencia for..to/downto..do');
    for I := 1 to 5 do
        WriteLn(I ** 2);
    for I := 5 downto 1 do
        WriteLn(I);
    WriteLn('');

    WriteLn('*****RETO EXTRA*****');
    for I := 10 to 55 do
    begin
        If (I mod 2 = 0) and (I <> 16) and (I mod 3 <> 0) then
            WriteLn(I);
    end;
end.
