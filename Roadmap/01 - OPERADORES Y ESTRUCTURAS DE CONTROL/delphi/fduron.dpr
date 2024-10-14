(*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 *)

program fduron;

{$APPTYPE CONSOLE}

{$R *.res}


uses
  System.SysUtils;

type
  TElementos = (Elemento1, Elemento2, Elemento3, Elemento4, Elemento5, Elemento6);
  TConjuntoElementos = set of TElementos;
const
  IntA = 20;
  IntB = 11;
  BoolA = True;
  BoolB = False;
  UnConjunto: TConjuntoElementos = [Elemento1, Elemento3, Elemento5];
  OtroConjunto: TConjuntoElementos = [Elemento2, Elemento6];
var
  VariableEntera: Integer;
  VariableString: String;
  VariableConjunto: TConjuntoElementos;
  UnObjeto: TObject;
  I: Integer;
  R: Real;

procedure MostrarElementosDelConjunto(const UnConjuntoLocal: TConjuntoElementos);
begin
  //Ejemplo de ciclo FOR con elementos de un conjunto
  for var Elemento in UnConjuntoLocal do
    case Elemento of
      Elemento1: Write('Elemento1 ');
      Elemento2: Write('Elemento2 ');
      Elemento3: Write('Elemento3 ');
      Elemento4: Write('Elemento4 ');
      Elemento5: Write('Elemento5 ');
      Elemento6: Write('Elemento6 ');
    end;
    WriteLn;
end;

begin
  WriteLn('*** Operadores Aritméticos ***');
  WriteLn('Suma: ', IntA + IntB);
  WriteLn('Resta: ', IntA - IntB);
  WriteLn('Multiplicación: ', IntA * IntB);
  WriteLn('división real: ', IntA / IntB);
  WriteLn('división entera: ', IntA div IntB);
  WriteLn('residuo: ', IntA mod IntB);
  WriteLn;
  WriteLn('*** Operadores lógicos ***');
  WriteLn('NOT lógico (Negación):', not BoolA);
  WriteLn('AND lógico (Conjunción):', BoolA and BoolB);
  WriteLn('OR lógico (Disyunción):', BoolA or BoolB);
  WriteLn('XOR lógico (Disyunción exclusiva):', BoolA xor BoolB);
  WriteLn;
  WriteLn('*** Operadores de comparacion ***');
  WriteLn('Es mayor que: ', IntA > IntB);
  WriteLn('Es menor que: ', IntA < IntB);
  WriteLn('Es mayor o igual que: ', IntA >= IntB);
  WriteLn('Es menor o igual que: ', IntA <= IntB);
  WriteLn('Es igual a: ', IntA = IntB);
  WriteLn('Es diferente a: ', IntA <> IntB);
  WriteLn;
  WriteLn('*** Asignacion ***');
  VariableEntera := 12;
  VariableString := 'Valor string';
  VariableConjunto := [Elemento1, Elemento2];
  WriteLn;
  WriteLn('*** Operadores de identidad ***');
  WriteLn('La variable es de la clase TObject: ', UnObjeto is TObject);
  WriteLn;
  WriteLn('*** Operadores de pertenencia ***');
  WriteLn('El elemento pertenece a un conjunto: ', Elemento4 in UnConjunto);
  WriteLn('El elemento NO pertenece a un conjunto: ', not(Elemento4 in UnConjunto));
  WriteLn;
  WriteLn('*** Operadores de bits ***');
  {IntA es un valor entero de 64Bits, su valor (20) en binario es:
   0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0001 0100
  al invertir todos los bits (not IntA) se convierte en
  1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1110 1011
  que es -21 entero}
  WriteLn('NOT a nivel de bits (invertir): ', not IntA);
  WriteLn('AND a nivel de bits: ', IntA and IntB);
  WriteLn('OR a nivel de bits: ', IntA or IntB);
  WriteLn('XOR a nivel de bits: ', IntA xor IntB);
  WriteLn('Desplazamiento de X bits a la izquierda: ', IntA shl 2);
  WriteLn('Desplazamiento de X bits a la derecha: ', IntA shr 2);
  WriteLn;
  WriteLn('*** Operadores de conjuntos ***');
  Write('Union: ');
  MostrarElementosDelConjunto(UnConjunto + OtroConjunto);
  Write('Diferencia: ');
  MostrarElementosDelConjunto(UnConjunto - OtroConjunto);
  Write('Intersección: ');
  MostrarElementosDelConjunto(UnConjunto * OtroConjunto);
  WriteLn('Es subconjunto de: ', UnConjunto <= OtroConjunto);
  WriteLn('Es sperconjunto de: ', UnConjunto >= OtroConjunto);
  WriteLn('Igualdad: ', UnConjunto = OtroConjunto);
  WriteLn('Diferencia: ', UnConjunto <> OtroConjunto);
  WriteLn('Pertenencia de ordinal en un conjunto: ', Elemento1 in OtroConjunto);
  WriteLn;
  WriteLn('*** Apuntadores ***');
  var x := @VariableEntera; //Apuntador a la dirección de memoria que ocupa la variable
  WriteLn('Dereferenciar un apuntador: ', Integer(^x));
  WriteLn;
  WriteLn('*** Estructuras de control ***');
  if IntA > IntB then
  begin
    WriteLn('IntA es mayor que IntB')
  end
  else
  begin
    WriteLn('IntA no es mayor que IntB')
  end;

  case IntA of
    10: WriteLn('IntA es igual a 10');
    20: WriteLn('IntA es igual a 20');
    30: WriteLn('IntA es igual a 30');
    31..40: WriteLn('IntA esta entre 31 y 40');
  else
    WriteLn('IntA es igual a otro valor');
  end;

  WriteLn('Numeros del 1 al 10 en un ciclo FOR:');
  for I := 1 to 10 do
  begin
    Write(I, ' ');
  end;

  WriteLn;
  WriteLn('Numeros del 1 al 10 en un ciclo WHILE:');
  I := 1;
  while I <= 10 do
  begin
    Write(I, ' ');
    I := I + 1;
  end;

  WriteLn;
  WriteLn('Numeros del 1 al 10 en un ciclo REPEAT:');
  I := 1;
  repeat
    Write(I, ' ');
    I := I + 1;
  until I > 10;

  WriteLn;
  try
    WriteLn('Prueba de finally');
    VariableEntera := IntA + IntB;
    R := IntB * 2.25;
  finally
    WriteLn('''
      Esta línea se imprimirá independientemente de lo que ocurra
      en el código del bloque T R Y
      ''');
  end;

  WriteLn;
  WriteLn('''
    ******************************************************************
    **  DIFICULTAD EXTRA                                            **
    ******************************************************************
    ''');
  WriteLn('Números del 10 al 55, excluyendo el 16 y multiplos de 3');
  for I := 10 to 55 do
    if (I <> 16) and ((I mod 3) <> 0) then
      Write(I, ', ');
  WriteLn;

  try
    writeLn('Prueba de excepciones');
    I := 1;
    while I <= 1 do
    begin
      R := IntA div I; //Provocar una Division por 0
      I := I - 1;
    end;
  except
    on E: Exception do
      WriteLn('Ocurrio el error: ', E.Message);
  end;

  ReadLn;

end.
