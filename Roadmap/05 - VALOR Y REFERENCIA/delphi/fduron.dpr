(*
 * EJERCICIO:
 * - Muestra ejemplos de asignaci�n de variables "por valor" y "por referencia", seg�n
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y c�mo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayor�a de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos par�metros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos par�metros por valor, y en otro caso, por referencia.
 *   Estos par�metros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuaci�n, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba tambi�n que se ha conservado el valor original en las primeras.
 *)
program fduron;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils;

procedure SumarPorReferencia(ValorBase: Integer; var Valor1: Integer; var Valor2: Integer);
begin
  { Los par�metros por referencia son modificados dentro del contexto del
    procedimiento o funci�n que los manda llamar }
  Valor1 := ValorBase + Valor1;
  Valor2 := ValorBase + Valor2;
end;

procedure ConcatenarPorReferencia(var Cadena1: String; Cadena2: String);
begin
  { El resultado de la concatenaci�n se almacena en la variable Cadena1, que es
    un par�metro por referencia }
  Cadena1 := Cadena1 + '+' + Cadena2;
end;

function ConcatenarPorValor(Cadena1, Cadena2: String): String;
begin
  { El resultado de la concatenaci�n se regresa en el resultado de la funci�n
    ya que ambos par�metros son por valor }

  // Los par�metros pueden cambiar su valor en el contexto de esta funci�n
  Cadena1 := Cadena1+ '+';
  Result := Cadena1 + Cadena2;
end;

procedure SumarPorValor(ValorBase, Valor1, Valor2: Integer);
begin
  Valor1 := ValorBase + Valor1;
  Valor2 := ValorBase + Valor2;
  WriteLn('"SumaPorValor"');
  WriteLn('Valor1: ', Valor1);
  WriteLn('Valor2: ', Valor2);
end;

procedure DificultadExtraPorValor(ParametroUno, ParametroDos: String);
var
  VariableTemporal: String;
begin
  VariableTemporal := ParametroUno;
  ParametroUno := ParametroDos;
  ParametroDos := VariableTemporal;
end;

procedure DificultadExtraPorReferencia(var ParametroUno, ParametroDos: String);
var
  VariableTemporal: String;
begin
  VariableTemporal := ParametroUno;
  ParametroUno := ParametroDos;
  ParametroDos := VariableTemporal;
end;

Var
  VarEjemplo1, VarEjemplo2: Integer;
  CadenaUno, CadenaDos: String;
  OriginalUno, OriginalDos, NuevaUno, NuevaDos: String;

begin
  VarEjemplo1 := 15;
  VarEjemplo2 := 23;
  CadenaUno := 'quince';
  CadenaDos := 'veintitr�s';

  SumarPorReferencia(10, VarEjemplo1, VarEjemplo2);
  WriteLn('los valores + 10 son: ', VarEjemplo1, ' ', VarEjemplo2);

  CadenaUno := 'quince';
  CadenaDos := 'veintitr�s';
  ConcatenarPorReferencia(CadenaUno, CadenaDos);
  WriteLn('Concatenar texto usando un procedimiento con par�metros por referencia: ',
    CadenaUno);

  CadenaUno := 'quince';
  CadenaDos := 'veintitr�s';
  WriteLn('Concatenar texto usando una funci�n con par�metros por valor: ',
    ConcatenarPorValor(CadenaUno, CadenaDos) );

  SumarPorValor(10, 27, 16);

  WriteLn;
  WriteLn('************************************************');
  WriteLn(' DIFICULTAD EXTRA');
  WriteLn('************************************************');
  WriteLn;

  OriginalUno := '*Texto n�mero uno*';
  OriginalDos := '-TEXTO N�MERO DOS-';
  NuevaUno := OriginalUno;
  NuevaDos := OriginalDos;

  DificultadExtraPorValor(NuevaUno, NuevaDos);
  WriteLn('Ejemplo "Por valor"');
  WriteLn('Varialbes originales: ', OriginalUno, ' ', OriginalDos);
  WriteLn('Varialbes nuevas: ', NuevaUno, ' ', NuevaDos);
  WriteLn;

  OriginalUno := '*Texto n�mero uno*';
  OriginalDos := '-TEXTO N�MERO DOS-';
  NuevaUno := OriginalUno;
  NuevaDos := OriginalDos;
  DificultadExtraPorReferencia(NuevaUno, NuevaDos);
  WriteLn('Ejemplo "Por referencia"');
  WriteLn('Varialbes originales: ', OriginalUno, ' ', OriginalDos);
  WriteLn('Varialbes nuevas: ', NuevaUno, ' ', NuevaDos);
  ReadLn;
end.
