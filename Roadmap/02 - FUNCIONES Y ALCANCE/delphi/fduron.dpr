(*
 * EJERCICIO:
 * - Crea ejemplos de funciones b�sicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin par�metros ni retorno, con uno o varios par�metros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza alg�n ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer m�s o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una funci�n que reciba dos par�metros de tipo cadena de texto y retorne un n�mero.
 * - La funci�n imprime todos los n�meros del 1 al 100. Teniendo en cuenta que:
 *   - Si el n�mero es m�ltiplo de 3, muestra la cadena de texto del primer par�metro.
 *   - Si el n�mero es m�ltiplo de 5, muestra la cadena de texto del segundo par�metro.
 *   - Si el n�mero es m�ltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La funci�n retorna el n�mero de veces que se ha impreso el n�mero en lugar de los textos.
 *
 * Presta especial atenci�n a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el c�digo se entienda.
 *)
program fduron;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils;

var
  IGlobal: Integer;
  TextoObtenido: String;

procedure UnProcedimientoNoPNoR;
begin
  WriteLn('Esta linea se escribe desde un procedimiento sin par�metros ni retorno');
end;

function UnaFuncionSinParametros: String;
begin
  Result := 'Resultado de una funci�n sin par�metros';
end;

procedure UnProcedimientoNoR(const Valor1: String; var Valor2: Integer);
begin
  WriteLn('Procedimientos con dos prametros, por Valor y por Referencia: ',
    Valor1, ' ', Valor2);
  Valor2 := 100;
end;

function UnaFuncionConParametros(const Valor1: String; var Valor2: Integer): String;
var
  ILocal: Integer;
begin
  Result := 'Resultado de una funci�n con par�metros ' + Valor1;
  ILocal := IGlobal;
  Valor2 := 200 + ILocal;
end;

procedure ProcedimientoYFuncion(Valor1: String);

  function DentroDelProcedimiento: String;
  begin
    Result := 'Texto dentro de una funci�n, dentro de un procedimiento';
  end;

begin
  WriteLn('Variable: ', Valor1);
  WriteLn(DentroDelProcedimiento);
end;

function DificultadExtra(const Parametro1, Parametro2: String): Integer;
var
  I: Integer;
begin
  Result := 0;
  {se usa una coma ',' en todos los write para separar cada numero o variable}
  for I := 1 to 100 do
  begin
    if ((I mod 5) = 0) and ((I mod 3) = 0) then
      Write(Parametro1 + Parametro2, ',')
    else
    if (I mod 3) = 0 then
      Write(Parametro1, ',')
    else
    if (I mod 5) = 0 then
      Write(Parametro2, ',')
    else
    begin
      Write(I, ',');
      Result := Result + 1;
    end;
  end;
end;

begin
  var AquiRegresaValor2: Integer;
  IGlobal := 14;
  WriteLn('*** FUNCIONES Y ALCANCE ***');
  UnProcedimientoNoPNoR;
  WriteLn(UnaFuncionSinParametros);
  AquiRegresaValor2 := 123;
  UnProcedimientoNoR('Valor constante', AquiRegresaValor2);
  WriteLn('Valor almacenado en la variable desde el procedimiento: ', AquiRegresaValor2);
  WriteLn;
  TextoObtenido := UnaFuncionConParametros('Valor constante para la funci�n', AquiRegresaValor2);
  WriteLn(TextoObtenido);
  WriteLn('Valor almacenado en la variable desde la funci�n: ', AquiRegresaValor2);
  ProcedimientoYFuncion('Texto por valor');
  WriteLn;
  WriteLn('*** DIFICULTAD EXTRA ***');
  var NumerosImpresos := DificultadExtra('(El parametro uno)', '(El parametro dos)');
  WriteLn;
  WriteLn('Se han impreso ', NumerosImpresos, ' n�meros');
  ReadLn;
end.
