program miguelex;

{ Ejemplo de una función que no tiene parametros ni retorno }
Procedure funcionSinNada;  
begin  
  Writeln ('Hola, soy una función que no tiene ni parametros ni retorno');
end;

{ Ejemplo de una función que tiene parametros pero no retorno }
Procedure funcionSinRetorno(parametro1, parametro2: Integer);
begin
  Writeln ('Hola, soy una función que no tiene retorno pero si parametros');
  Writeln ('El valor del parametro 1 es: ', parametro1);
  Writeln ('El valor del parametro 2 es: ', parametro2);
end;

{ Ejemplo de una función que tiene retorno pero no parametros }
Function funcionSinParametros: Integer;
begin
  Writeln ('Hola, soy una función que no tiene parametros pero si retorno');
  funcionSinParametros := 10;
end;

{ Ejemplo de una función que tiene parametros y retorno }
Function funcionConParametros(parametro1, parametro2: Integer): Integer;
begin
  Writeln ('Hola, soy una función que tiene parametros y retorno');
  Writeln ('El valor del parametro 1 es: ', parametro1);
  Writeln ('El valor del parametro 2 es: ', parametro2);
  funcionConParametros := parametro1 + parametro2;
end;

{ Ejemplo de uso de cariables locales y globales }
Var
  variableGlobal: Integer;
  
procedure ProcLocalVsGlobal;
  Var
    variableLocal: Integer;
  begin
    variableLocal := 10;
    variableGlobal := 20;
    WriteLn('El valor de la variable local es: ', variableLocal);
    WriteLn('El valor de la variable global es: ', variableGlobal);
end;

{ Ejemplo de paso por refeencia }
Procedure pasoPorReferencia(Var parametro1: Integer);
begin
  parametro1 := 10;
end;

{ Ejemplo de paso por valor }
Procedure pasoPorValor(parametro1: Integer);
begin
  parametro1 := 10;
end;

function extra (parametro1, parametro2: String): Integer;
  var
  numsImpresos: Integer;
  i: Integer; // Debes declarar i aquí
begin
  numsImpresos := 0;
  for i := 1 to 100 do
  begin
    if (i mod 15 = 0) then
      WriteLn(parametro1+parametro2)
    else if (i mod 3 = 0) then
      WriteLn(parametro1)
    else if (i mod 5 = 0) then
      WriteLn(parametro2)
    else
      WriteLn(i);
    Inc(numsImpresos);
  end;
  extra := numsImpresos;
end;

begin
  WriteLn();
  funcionSinNada;
  WriteLn();
  funcionSinRetorno(10,2);
  WriteLn();
  WriteLn('El valor de la funcion sin retorno es: ', funcionSinParametros);
  WriteLn();
  WriteLn('El valor de la funcion con retorno es: ', funcionConParametros(10,2));
  WriteLn();
  ProcLocalVsGlobal;
  WriteLn();
  WriteLn('Paso por referencia: ', pasoPorReferencia(5));
  WriteLn();
  WriteLn('Paso por valor: ', pasoPorValor(5));
  WriteLn();

  { Ejemplo de uso de una funcion del sistema }
  WriteLn('El valor de la funcion random es: ', Random(10));
  WriteLn();

  { Finalmente, el ejercicio extra }
  WriteLn('Ejercicio extra');
  WriteLn();
  WriteLn('Se han imprimido: ', extra('Miguelex','Dev'));



end.