(*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 *)
program fduron;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils;

procedure SumarPorReferencia(ValorBase: Integer; var Valor1: Integer; var Valor2: Integer);
begin
  { Los parámetros por referencia son modificados dentro del contexto del
    procedimiento o función que los manda llamar }
  Valor1 := ValorBase + Valor1;
  Valor2 := ValorBase + Valor2;
end;

procedure ConcatenarPorReferencia(var Cadena1: String; Cadena2: String);
begin
  { El resultado de la concatenación se almacena en la variable Cadena1, que es
    un parámetro por referencia }
  Cadena1 := Cadena1 + '+' + Cadena2;
end;

function ConcatenarPorValor(Cadena1, Cadena2: String): String;
begin
  { El resultado de la concatenación se regresa en el resultado de la función
    ya que ambos parámetros son por valor }

  // Los parámetros pueden cambiar su valor en el contexto de esta función
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
  CadenaDos := 'veintitrés';

  SumarPorReferencia(10, VarEjemplo1, VarEjemplo2);
  WriteLn('los valores + 10 son: ', VarEjemplo1, ' ', VarEjemplo2);

  CadenaUno := 'quince';
  CadenaDos := 'veintitrés';
  ConcatenarPorReferencia(CadenaUno, CadenaDos);
  WriteLn('Concatenar texto usando un procedimiento con parámetros por referencia: ',
    CadenaUno);

  CadenaUno := 'quince';
  CadenaDos := 'veintitrés';
  WriteLn('Concatenar texto usando una función con parámetros por valor: ',
    ConcatenarPorValor(CadenaUno, CadenaDos) );

  SumarPorValor(10, 27, 16);

  WriteLn;
  WriteLn('************************************************');
  WriteLn(' DIFICULTAD EXTRA');
  WriteLn('************************************************');
  WriteLn;

  OriginalUno := '*Texto número uno*';
  OriginalDos := '-TEXTO NÚMERO DOS-';
  NuevaUno := OriginalUno;
  NuevaDos := OriginalDos;

  DificultadExtraPorValor(NuevaUno, NuevaDos);
  WriteLn('Ejemplo "Por valor"');
  WriteLn('Varialbes originales: ', OriginalUno, ' ', OriginalDos);
  WriteLn('Varialbes nuevas: ', NuevaUno, ' ', NuevaDos);
  WriteLn;

  OriginalUno := '*Texto número uno*';
  OriginalDos := '-TEXTO NÚMERO DOS-';
  NuevaUno := OriginalUno;
  NuevaDos := OriginalDos;
  DificultadExtraPorReferencia(NuevaUno, NuevaDos);
  WriteLn('Ejemplo "Por referencia"');
  WriteLn('Varialbes originales: ', OriginalUno, ' ', OriginalDos);
  WriteLn('Varialbes nuevas: ', NuevaUno, ' ', NuevaDos);
  ReadLn;
end.
