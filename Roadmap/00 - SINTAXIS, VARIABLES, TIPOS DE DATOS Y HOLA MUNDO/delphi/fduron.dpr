{La web oficial de delphi: https://www.embarcadero.com/products/delphi/}

//Este es un comentario en una sola linea

{Este es otro comentario
  en varias lineas}

(* Tambi�n de esta manera se realizan
   comentarios en varias l�neas *)

program fduron;

{$APPTYPE CONSOLE}

{$R *.res}
uses
  System.SysUtils;

//Las constantes se declaran sin tipo
const
  EstaEsUnaConstante = 'A';
  EstaEsOtraConstante = 1;

var
  UnEntero: Integer;
  UnEnteroCorto: ShortInt;
  UnEnteroPeque�o: SmallInt;
  UnEnteroLargo: LongInt;

  UnNumeroSencillo: Single; //Numero Real de 4 bytes
  UnNumeroDoble: Double; //Numero Real de 8 bytes
  UnNumeroExtendido: Extended; //Numero Real de 10 bytes
  UnNumeroReal: Real; //Igual al Double

  UnCaracterLargo: WideChar; //Caracter de tipo Unicode
  UnCaracter: Char; //Igual que WideChar

  UnTexto: String; //Texto
  UnTextoAncho: WideString; //Texto con terminaci�n null (aplicaciones de escritorio)
  UnTextoEnorme: AnsiString; //Texto de asignaci�n dinamica tama�o esta limitado por el tama�o de la memoria disponible

  UnBoleano: Boolean;

  UnSubRango: 1..100;

  UnConjunto: set of 1..10;

  UnApuntadorEntero: ^Integer;

  UnRegistro: record
    Campo1: Integer;
    Campo2: String;
  end;

  UnArregloDeEnteros: array[1..5] of Integer;

  UnaEnumeracion: (Primero, Segundo, Tercero);
begin
  Write('�Hola, Delphi!');
  ReadLn; //Esperar que el usuario presione una tecla
end.
