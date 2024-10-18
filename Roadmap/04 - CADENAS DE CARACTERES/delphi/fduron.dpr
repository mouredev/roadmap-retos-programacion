(*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 *)

program fduron;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils;

//Palabras o frases que se leen igual al derecho y al reves
function EsPalindromo(const Palabra1, Palabra2: String): Boolean;
begin
  Result := True;
  var P := Palabra1 + Palabra2;
  P := P.Replace(' ', '').ToUpper; //Eliminar los espacios
  var Centro := P.Length div 2;
  for var C := 1 to Centro do
    if P[C] <> P[P.Length - C + 1] then
      Exit(False);
end;

//Palabra o frase formada a partir de una primera palabra o frase
function EsAnagrama(const Palabra1, Palabra2: String): Boolean;
var
  Idx: Integer;
begin
  Result := True;
  var P1 := Palabra1.Replace(' ', '').ToUpper; //Eliminar los espacios
  var P2 := Palabra2.Replace(' ', '').ToUpper; //Eliminar los espacios

  if (P1.Length <> P2.Length) or (P1.Equals(P2)) then
    Exit(False);

  for var C := 1 to P1.Length do
  begin
    Idx := P2.IndexOf(P1[C]);
    P2 := P2.Remove(Idx, 1);
  end;

  Result := P2.IsEmpty;
end;

//Palabras o frases donde no se repite ninguna letra
function EsIsograma(const Palabra: String): Boolean;
var
  Idx: Integer;
begin
  Result := True;
  var P1 := Palabra.Replace(' ', '').ToUpper; //Eliminar los espacios

  for var C := 1 to P1.Length do
    if P1.CountChar(P1[C]) > 1 then
      Exit(False);
end;

procedure DificultadExtra;

  procedure EvaluarPalabras(const Palabra1, Palabra2: String);
  begin
    if EsPalindromo(Palabra1, Palabra2) then
      WriteLn('>>Las palabras forman un palíndromo')
    else
      WriteLn('>>Las palabras NO forman un palíndromo');

    if EsAnagrama(Palabra1, Palabra2) then
      WriteLn('>>Las palabras forman un anagrama')
    else
      WriteLn('>>Las palabras NO forman un anagrama');

    if EsIsograma(Palabra1) then
      WriteLn('>>La primera palabra es un isograma')
    else
      WriteLn('>>La primera palabra NO es un isograma');

    if EsIsograma(Palabra2) then
      WriteLn('>>La primera palabra es un isograma')
    else
      WriteLn('>>La primera palabra NO es un isograma');
  end;

var
  PrimeraPalabra: String;
  SegundaPalabra: String;
  Continua: Char;
begin
  WriteLn;
  WriteLn('************************************************');
  WriteLn(' DIFICULTAD EXTRA');
  WriteLn(' Escribe dos palabras o frases para analizarlas');
  WriteLn('************************************************');
  WriteLn;
  repeat
    Write('Escribe la primera palabra o frase: ');
    ReadLn(PrimeraPalabra);
    Write('Escribe la segunda palabra o frase: ');
    ReadLn(SegundaPalabra);

    EvaluarPalabras(PrimeraPalabra, SegundaPalabra);

    WriteLn;
    Write('¿Deseas intentar otra vez? (S/N): ');
    ReadLn(Continua);
  until UpperCase(Continua) = 'N';
end;

var
  Cadena1, Cadena2, Cad1EntreComillas: String;
  Resultado: Integer;
begin
  Cadena1 := 'Cadena A';
  Cadena2 := 'Cadena B';

  //Existen varias versiones del método Compare, a continuación tres ejemplos:
  //Comparar dos cadenas:
  Resultado := String.Compare(Cadena1, Cadena2);
  //Comparar un substring de 6 caracteres iniciando en la posicion 0:
  Resultado := String.Compare(Cadena1, 0, Cadena2, 0, 6);
  //Comparar utilizando la cadena inicial como base:
  Resultado := Cadena1.CompareTo(Cadena2);
  //Resultado será < 0 cuando Cadena1 se encuentre antes de Cadena2
  //Resultado será = 0 cuando ambas cadenas sean iguales
  //Resultado será > 0 cuando Cadena1 se encuentre después de Cadena2

  if Resultado < 0 then
    WriteLn(Cadena1 , ' se ordena antes de ', Cadena2)
  else
  if Resultado > 0 then
    WriteLn(Cadena1, ' se ordena después de ', Cadena2)
  else
    WriteLn(Cadena1, ' y ', Cadena2, ' son iguales');

  Cad1EntreComillas := Cadena1.QuotedString('"');
  WriteLn(Cad1EntreComillas, ' en minusculas: ', Cadena1.ToLower);
  WriteLn(Cad1EntreComillas, ' contiene ', Cadena1.CountChar('a'), ' letras "a" ');
  WriteLn(Cad1EntreComillas, ' en Mayusculas: ', Cadena1.ToUpper);
  WriteLn(Cad1EntreComillas, ' contiene "ad": ', Cadena1.Contains('ad'));
  WriteLn(Cad1EntreComillas, ' sin comillas: ', Cad1EntreComillas.DeQuotedString('"') );
  WriteLn(Cad1EntreComillas, ' termina con "A": ', Cadena1.EndsWith('A'));
  WriteLn(Cad1EntreComillas, ' inicia con "Cad": ', Cadena1.EndsWith('Cad'));
  WriteLn(Cad1EntreComillas, ' posición de "A": ', Cadena1.IndexOf('A') );
  WriteLn(Cad1EntreComillas, ' posición de "A", "B" o "C": ',
    Cadena1.IndexOfAny(['A', 'B', 'C']) );
  WriteLn(Cad1EntreComillas, ' en la posición 0 es el delimitador " : ',
    Cad1EntreComillas.IsDelimiter('"', 0) );
  WriteLn(Cad1EntreComillas, ' está vacio: ', Cad1EntreComillas.IsEmpty);
  //Cadena1.IsNullOrEmpty
  //Cadena1.IsNullOrWhiteSpace
  WriteLn(Cad1EntreComillas, ' uniendo cadenas separadas con | : ',
    String.Join('|', [Cadena1, Cadena2, Cadena1])
    );
  WriteLn(Cad1EntreComillas, ' posición del último delimitador ["]: ',
    Cad1EntreComillas.LastDelimiter('"')
    );
  WriteLn(Cad1EntreComillas, ' última posición de "na": ',
    Cad1EntreComillas.LastIndexOf('na')
    );
  WriteLn(Cad1EntreComillas, ' removiendo 2 caracteres texto a partir de la posicion 3: ',
    Cad1EntreComillas.Remove(3, 2));
  WriteLn(Cad1EntreComillas, ' En tamaño 15, rellenando con # a la izquierda: ',
    Cadena1.PadLeft(15, '#') );
  WriteLn(Cad1EntreComillas, ' En tamaño 15, rellenando con # a la derecha: ',
    Cadena1.PadRight(15, '#') );
  WriteLn(Cad1EntreComillas, ' reemplazando a por 4: ',  Cadena1.Replace('a', '4') );
  WriteLn('Separando ', Cad1EntreComillas, ' en elementos delimitados por ''a'' :');
  var Splits := Cadena1.Split(['a']);
  for var Elemento in Splits do
    WriteLn(Elemento);

  WriteLn('Tamaño de ', Cadena1, ': ', Cadena1.Length);

  //Concatenación
  Cadena1 := '    ' + Cadena1 + Cadena2 + '    ';
  WriteLn('Cadena1 ahora es: ', Cadena1.QuotedString);
  WriteLn(Cadena1.QuotedString, ' sin espacios a la izquierda: ',
    Cadena1.TrimLeft.QuotedString);
  WriteLn(Cadena1.QuotedString, ' sin espacios a la derecha: ',
    Cadena1.TrimRight.QuotedString );

  DificultadExtra;

end.
