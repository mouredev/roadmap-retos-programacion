program blueicaro;
{
#49 EL ALMACÉN DE PAPÁ NOEL

    Dificultad: Media | Publicación: 09/12/24 | Corrección: 23/12/24

Ejercicio

/*
 * EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 *
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 *
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 *
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
 */

Tienes toda la información extendida sobre el roadmap de retos de programación en retosdeprogramacion.com/roadmap.

Sigue las instrucciones, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

    Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde Twitch. Tienes el horario en la sección "eventos" del servidor de Discord.

}
uses
  Math,
  SysUtils,
  StrUtils;

const
  Letters: array  [1..3] of char = ('A', 'B', 'C');
  Numbers: array [1..3] of char = ('1', '2', '3');
var
  Password_elements: string;
  I, attemps: integer;
  Password, secret_password: string;

  function Generate_Password: string;
  var
    Listo: boolean;
    Valor: int64;
    Elemento: char;
  begin
    Result := '';
    Listo := False;
    repeat
      Randomize;
      Valor := RandomRange(1, Length(Password_elements));
      Elemento := Password_elements[Valor];
      if PosEx(Elemento, Result) = 0 then
      begin
        Result := Result + Elemento;
      end;
    until Length(Result) = 4;
  end;

  function ElementosCorrectos(Cadena: string): boolean;
  begin
    Result := True;
    for I := 1 to Length(Cadena) do
    begin
      if PosEx(Cadena[I], Password_elements) = 0 then
      begin
        Result := False;
        Break;
      end;
    end;
  end;

begin

  Password_elements := Letters + Numbers;
  secret_password := Generate_Password;
  Attemps := 1;
  repeat
    WriteLn('Intento: ' + IntToStr(attemps));
    WriteLn('Introduce la clave:');
    ReadLn(Password);
    Password := UpperCase(Password);
    if Length(Password) <> 4 then
    begin
      WriteLn('La clave debe tener 4 elementos');
      Continue;
    end;
    if not ElementosCorrectos(Password) then
    begin
      Writeln('Los elementos admitidos son: ' + Password_elements);
      Continue;
    end;
    if secret_password = Password then
    begin
      break;
    end;
    attemps := attemps + 1;
  until attemps = 10;
  if attemps = 10 then
  begin
    Writeln('No has podido descrifar la clave');
  end
  else
  begin
    WriteLn('Has conseguido descifrar la clave');
  end;
  {$IFDEF MSWINDOWS}
     Readln;
  {$ENDIF}
end.
