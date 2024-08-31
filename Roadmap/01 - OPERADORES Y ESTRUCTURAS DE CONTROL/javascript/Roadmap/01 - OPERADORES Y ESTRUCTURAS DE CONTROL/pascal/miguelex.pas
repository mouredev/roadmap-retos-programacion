program miguelex;

uses sysutils;

var
  a, b: integer;
  x: real;
  bool1, bool2: Boolean;
  
begin
    { Asignación }
    writeln('Ejemplo de asignacion');
    a := 5;
    x := a;
    writeln('Mostramos el valor de a, que la teniamos declarada como entero => ', a);
    writeln('Mostramos el valor de x, que la teniamos declarada como real y le hemos asigando el valor de a => ', x);
    WriteLn('Notese como se añaden los decimales a la variable real');

    { Aritméticos }
    writeln('Ejemplo de operadores aritmeticos');
    a := 5;
    b := 2;
    writeln('Mostramos el valor de a => ', a);
    writeln('Mostramos el valor de b => ', b);
    writeln('Suma de a + b => ', a + b);
    writeln('Resta de a - b => ', a - b);
    writeln('Multiplicacion de a * b => ', a * b);
    writeln('Division de a / b => ', a / b);
    writeln('Modulo de a mod b => ', a mod b);
    
    { Relacionales }
    writeln('Ejemplo de operadores relacionales');
    a := 5;
    b := 2;
    writeln('Mostramos el valor de a => ', a);
    writeln('Mostramos el valor de b => ', b);
    writeln('a > b => ', a > b);  
    writeln('a < b => ', a < b);
    writeln('a >= b => ', a >= b);
    writeln('a <= b => ', a <= b);
    writeln('a = b => ', a = b);
    writeln('a <> b => ', a <> b);
    
    { Lógicos }
    writeln('Ejemplo de operadores logicos');
    bool1 := True;
    bool2 := False;
    writeln('Mostramos el valor de a => ', bool1);
    writeln('Mostramos el valor de b => ', bool2);
    writeln('bool1 and bool2 => ', bool1 and bool2);
    writeln('bool1 or bool2 => ', bool1 or bool2);
    writeln('not bool1 => ', not bool1);
    writeln('not bool2 => ', not bool2);
    
  { Ejemplo de try catch }
  try
    writeln('Ejemplo de try catch');
    writeln('Mostramos el valor de a => ', a);
    writeln('Mostramos el valor de b => ', b);
    writeln('a div b => ', a div b);
  except
    on E: EDivByZero do
      writeln('Error: ', E.Message);
  end;
  
  { Ejemplo de if }
  writeln('Ejemplo de if');
  if a > b then
    writeln('a es mayor que b')
  else
    writeln('a es menor que b');
    
  { Ejemplo de case }
  writeln('Ejemplo de case');
  case a of
    1: writeln('a vale 1');
    2: writeln('a vale 2');
    3: writeln('a vale 3');
    4: writeln('a vale 4');
    5: writeln('a vale 5');
    6: writeln('a vale 6');
    7: writeln('a vale 7');
    8: writeln('a vale 8');
    9: writeln('a vale 9');
    10: writeln('a vale 10');
  end;
  
  { Ejemplo de for }
  writeln('Ejemplo de for');
  for a := 1 to 10 do
    writeln('a vale ', a);
    
  { Ejemplo de while }
  writeln('Ejemplo de while');
  a := 1;
  while a <= 10 do
  begin
    writeln('a vale ', a);
    a := a + 1;
  end;
  
  { Ejemplo de repeat }
  writeln('Ejemplo de repeat');
  a := 1;
  repeat
    writeln('a vale ', a);
    a := a + 1;
  until a > 10;
  
  { Ejemplo de break }
  writeln('Ejemplo de break');
  for a := 1 to 10 do
  begin
    writeln('a vale ', a);
    if a = 5 then
      break;
  end;
  
  { Ejemplo de continue }
  writeln('Ejemplo de continue');
  for a := 1 to 10 do
  begin
    if a = 5 then
      continue;
    writeln('a vale ', a);
  end;
  
  { Extra }
  writeln('Ejemplo extra');
  for a := 10 to 55 do
  begin
    if (a mod 2 = 0) and (a <> 16) and (a mod 3 <> 0) then
      writeln(a);
  end;
    
end.