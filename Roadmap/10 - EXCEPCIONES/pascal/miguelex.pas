program miguelex;

{$mode objfpc}

uses 
  SysUtils;

procedure warning_handler(ErrNo: longint; const ErrStr: string);
begin
  raise Exception.Create(ErrStr);
end;

function ejercicioExtra (nombre: string; reto: integer; lenguaje: string): string;
var
  resultado: string;
begin
  resultado := '';
  try
    if not (reto >= 0) then
      raise Exception.Create('El número debe ser un entero positivo');

    if lenguaje = '' then
      raise Exception.Create('El lenguaje debe ser una cadena no vacía');

    if nombre = 'Mouredev' then
      raise Exception.Create('El nombre no puede ser Mouredev');

    resultado := 'Solución reto # ' + IntToStr(reto) + ' - ' + lenguaje + ' del usuario ' + nombre + LineEnding;
  except
    on e: Exception do
      resultado := 'Error: ' + e.Message + LineEnding;
  end;
  resultado := resultado + 'La ejecución ha finalizado' + LineEnding;
  ejercicioExtra := resultado;
end;

var
  result: string;
begin
  try
    SetErrorHandler(@warning_handler);
    try
      result := '';
      result := result + FloatToStr(10 / 0) + LineEnding;
    except
      on e: Exception do
        result := result + e.Message + LineEnding;
    end;
    result := result + 'La ejecución ha finalizado' + LineEnding;
    
    try
      SetLength(result, 0);
      result := result + IntToStr([1, 2, 3][4]) + LineEnding;
    except
      on e: Exception do
        result := result + 'Error: ' + e.Message + LineEnding;
    end;
    result := result + 'La ejecución ha finalizado' + LineEnding;
    
    Writeln(result);

    Writeln('EJERCICIO EXTRA');
    Writeln(ejercicioExtra('Miguelex', 10, 'Pascal'));
    Writeln(ejercicioExtra('', -5, 'JavaScript'));
    Writeln(ejercicioExtra('Miguelex', 2, ''));
    Writeln(ejercicioExtra('Mouredev', 1, 'Python'));
  finally
    RestoreErrorHandler;
  end;
end.
