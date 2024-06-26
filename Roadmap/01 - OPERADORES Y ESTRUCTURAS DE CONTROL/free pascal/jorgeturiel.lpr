program jorgeturiel;

{
/*
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
 */
 }
uses
  SysUtils;

var
  A: single;
  B: single;
  R: single;
  AEntero: integer;
  BEntero: integer;
  REntero, I: integer;
  Logico: boolean;
  Byte1: byte;
  Byte2, Bin: byte;
begin
  A := 5;
  B := 4;
  AEntero := 5;
  BEntero := 4;

  Write('A = ' + FloatToStr(A));
  Writeln(', B = ' + FloatToStr(b));
  //Sumar
  R := A + b;
  Writeln('La suma de A más B es: ' + FloatToStr(R));

  //Restar
  R := A - B;
  Writeln('La resta de A menos B es: ' + FloatToStr(R));

  //Multiplicación
  R := A * B;
  Writeln('La multiplicación de A x B es: ' + FloatToStr(R));

  //Divisíón
  R := A / B;
  Writeln('La división de A / B es: ' + FloatToStr(R));

  //División entera
  REntero := AEntero div BEntero;
  Writeln('La división entera de A / B es: ' + FloatToStr(REntero));

  //Resto de la división
  R := AEntero mod BEntero;
  Writeln('El resto de la división de A / B es: ' + FloatToStr(r));

  // Operadores Logicos

  //Mayor
  Logico := A > B;
  Writeln('¿Es mayor A que B?: ' + BoolToStr(Logico, 'Verdad', 'Falso'));
  //Menor
  Logico := A < B;
  Writeln('¿Es menor A que B?: ' + BoolToStr(Logico, 'Verdad', 'Falso'));

  //Igual
  Logico := A = B;
  Writeln('¿Es igual A que B?: ' + BoolToStr(Logico, 'Verdad', 'Falso'));

  //Mayor o igual
  Logico := A >= B;
  Writeln('¿Es A mayor o igual que B?: ' + BoolToStr(Logico, 'Verdad', 'Falso'));

  //Menor o igual
  Logico := A <= B;
  Writeln('¿Es A menor o igual que B?: ' + BoolToStr(Logico, 'Verdad', 'Falso'));


  //Operadores Byte
  Byte1 := 10;
  Byte2 := 1;


  //Operador Or
  Bin := Byte1 or Byte2;
  Writeln('Operador Or ' + BinStr(bin, 8));

  ////Operador And
  Bin := Byte1 and Byte2;
  Writeln('Operador And ' + BinStr(bin, 8));

  //Operador Xor
  Bin := Byte1 xor Byte2;
  Writeln('Operador XOR ' + BinStr(bin, 8));

  ////Operador Not
  Bin := not Byte1;
  Writeln('Operador NOT ' + BinStr(bin, 8));

  //Desplazar bit a la derecha
  Bin := Byte1 shr 1;
  Writeln('Desplazar 1 byte a la derecha ' + BinStr(bin, 8));

  //Desplazar bit a la izquierda
  Bin := Byte1 shl 1;
  Writeln('Desplazar 1 byte a la izquierda ' + BinStr(bin, 8));

  WriteLn('Pulsa una tecla para la segunda parte');
  For I := 10 to 55 do
  begin
   If (I<> 16) and (I mod 2 = 0) and (I mod 3 <> 0) then
   begin
     Writeln('Número: ',I);
   end;
  end;
  ReadLn;
end.
