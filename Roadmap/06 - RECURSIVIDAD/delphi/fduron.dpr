(*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una funci�n recursiva que imprima
 * n�meros del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un n�mero concreto (la funci�n recibe ese n�mero).
 * - Calcular el valor de un elemento concreto (seg�n su posici�n) en la
 *   sucesi�n de Fibonacci (la funci�n recibe la posici�n).
 *)

program fduron;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils;

procedure NumerosDescendentes(const Numero: integer);
begin
  if numero >= 0 then
  begin
    WriteLn(Numero);
    NumerosDescendentes(Numero - 1);
  end;
end;

function Factorial(const Numero: Integer): Integer;
begin
  if Numero > 1 then
    Result := Numero * Factorial(Numero - 1)
  else
    Result := 1;
end;

function Fibonacci(const Posicion: Integer): Integer;
begin
  if Posicion < 2 then
    Result := Posicion
  else
    Result := Fibonacci(Posicion - 1) + Fibonacci(Posicion - 2);
end;

var
  Numero: Integer;
begin
  NumerosDescendentes(100);

  WriteLn('*****************************');
  WriteLn(' Dificultad extra');
  WriteLn('*****************************');
  Write('Escribe un numero entero: ');
  ReadLn(Numero);
  WriteLn('El Factorial de ', Numero, ' es: ', Factorial(Numero));
  WriteLn;
  Write('Escribe la posicion de la serie fibonacci: ');
  ReadLn(Numero);
  WriteLn('En la posicion ', Numero, ' el valor fibonacci es: ', fibonacci(Numero));
  ReadLn;
end.
