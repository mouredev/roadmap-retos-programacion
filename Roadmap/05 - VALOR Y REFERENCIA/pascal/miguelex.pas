program miguelex;

var
  num1V, num2V, num3V, num4V: integer; // Variables para el ejemplo por valor
  num1R, num2R, num3R, num4R: ^integer; // Variables para el ejemplo por referencia

{ Funcion con paso por valor }

procedure incValor(a, b: integer);
begin
  writeLn('El valor de a es: ', a + 1);
  writeLn('El valor de b es: ', b + 1);
end;

procedure incReferencia(var a, b: integer);
begin
  a := a + 1;
  b := b + 1;
end;

procedure byValor (a, b: integer);
var
  aux: integer;
begin
  aux := a;
  a := b;
  b := aux;
  writeln ('En la funcion byValor, a = ', a, ' y b = ', b);
end;

procedure byReferencia (var a, b: integer);
var
  aux: integer;
begin
  aux := a;
  a := b;
  b := aux;
  writeln ('En la funcion byReferencia, a = ', a, ' y b = ', b);
end;

{ Funcion con paso por referencia }

Begin

  writeln('Variables por valor');
  writeln();

  num1V := 10;
  num2V := 20;

  num3V := num1V;
  num4V := num2V;

  writeln('El valor de num1 es: ', num1V);
  writeln('El valor de num2 es: ', num2V);
  writeln('El valor de num3 es: ', num3V);
  writeln('El valor de num4 es: ', num4V);

  writeln('A continuación vamos a cambiar el valor de num1 y num2');
  writeln();

  num1V := 30;
  num2V := 40;

  writeln('El valor de num1 es: ', num1V);
  writeln('El valor de num2 es: ', num2V);
  writeln('El valor de num3 es: ', num3V);
  writeln('El valor de num4 es: ', num4V);
  writeln();

  writeln('Variables por referencia');
  writeln();
  { Por referencia }
  GetMem(num1R, SizeOf(integer));
  GetMem(num2R, SizeOf(integer));
  num3R := num1R;
  num4R := num2R;

  num1R^ := 10;
  num2R^ := 20;

  writeln('El valor de num1 es: ', num1R^);
  writeln('El valor de num2 es: ', num2R^);
  writeln('El valor de num3 es: ', num3R^);
  writeln('El valor de num4 es: ', num4R^);
  writeln();

  writeln('A continuación vamos a cambiar el valor de num1 y num2');
  writeln();
  num1R^ := 30;
  num2R^ := 40;

  writeln('El valor de num1 es: ', num1R^);
  writeln('El valor de num2 es: ', num2R^);
  writeln('El valor de num3 es: ', num3R^);
  writeln('El valor de num4 es: ', num4R^);

  writeln('Como podemos ver, el valor de num3 y num4 cambió, ya que son referencias a las variables originales');
  writeln();
  FreeMem(num1R);
  FreeMem(num2R);

  { Ejemplo de funcion con paso por valor }

  writeln('Ejemplo de función con paso por valor');
  writeln();

  num1V := 1;
  num2V := 2;

  writeln('Valores de num1 y num2 antes de llamar a la función incValor');
  writeln('Num1 = ', num1V); 
  writeln('Num2 = ', num2V);
  writeln();

  incValor(num1V, num2V);
  writeln();

  writeln('Valores de num1 y num2 después de llamar a la función incValor');
  writeln('Num1 = ', num1V);
  writeln('Num2 = ', num2V);
  writeln();

  writeln('Ejemplo de función con paso por valor');
  writeln();
  
  num1V := 1;
  num2V := 2;

  writeln('Valores de num1 y num2 antes de llamar a la función incReferencia');
  writeln('Num1 = ', num1V);
  writeln('Num2 = ', num2V);
  writeln();

  incReferencia(num1V, num2V);

  writeln('Valores de num1 y num2 después de llamar a la función incReferencia');
  writeln('Num1 = ', num1V);
  writeln('Num2 = ', num2V);
  writeln();

  { Extra }

  writeln('Ejemplo de función extra con paso por valor');
  writeln();

  num1V := 5;
  num2V := 10;

  writeln('Valores de num1 y num2 antes de llamar a la función byValor');
  writeln('Num1 = ', num1V);
  writeln('Num2 = ', num2V);
  writeln();

  byValor(num1V, num2V);
  writeln();

  writeln('Valores de num1 y num2 después de llamar a la función byValor');
  writeln('Num1 = ', num1V);
  writeln('Num2 = ', num2V);
  writeln();

  writeln('Ejemplo de función extra con paso por referencia');
  writeln();

  writeln('Valores de num1 y num2 antes de llamar a la función byReferencia');
  writeln('Num1 = ', num1V);
  writeln('Num2 = ', num2V);
  writeln();

  byReferencia(num1V, num2V);
  writeln();

  writeln('Valores de num1 y num2 después de llamar a la función byReferencia');
  writeln('Num1 = ', num1V);
  writeln('Num2 = ', num2V);
  writeln();

end.
