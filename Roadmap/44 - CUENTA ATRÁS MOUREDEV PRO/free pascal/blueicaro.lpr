program blueicaro;
 {
 /*
 * EJERCICIO:
 * ¡El 12 de noviembre lanzo mouredev pro!
 * El campus de la comunidad para estudiar programación de
 * una manera diferente: https://mouredev.pro
 *
 * Crea un programa que funcione como una cuenta atrás.
 *
 * - Al iniciarlo tendrás que indicarle el día, mes, año,
 *   hora, minuto y segundo en el que quieres que finalice.
 * - Deberás transformar esa fecha local a UTC.
 * - La cuenta atrás comenzará y mostrará los días, horas,
 *   minutos y segundos que faltan.
 * - Se actualizará cada segundo y borrará la terminal en
 *   cada nueva representación del tiempo restante.
 * - Una vez finalice, mostrará un mensaje.
 * - Realiza la ejecución, si el lenguaje lo soporta, en
 *   un hilo independiente.
 */
 }
uses
  {$ifdef unix}
  cthreads,
  {$endif}
  SysUtils,
  Classes,
  custapp,
  fptimer,
  DateUtils,
  Crt,
  keyboard;

type
  TTestTimerApp = class(TCustomApplication)
  private
    FTimer: TFPTimer;
    FFecha: TDateTime;  //Fecha límite
  public
    procedure DoRun; override;
    procedure DoTick(Sender: TObject);
  end;

  procedure TTestTimerApp.DoRun;
  var
    stHora, stFecha: string;
    FechaCorrecta: boolean;
  begin
    repeat
      ClrScr;
      GotoXY(1, 1);
      WriteLn('Hoy es: ' + DateToStr(Now) + ' ' + TimeToStr(Now));
      WriteLn('Escribe la FFecha límite (dia-mm-año):');
      Readln(stFecha);
      Writeln('Escribe la hora límite (h:mm:seg):');
      Readln(stHora);
      FechaCorrecta := TryStrToDateTime(stFecha + ' ' + stHora, FFecha);
      if (FechaCorrecta = False) then
      begin
        writeln('El formato es erroneo');
      end
      else if (FFecha <= Now()) then
      begin
        Writeln('La Fecha y la hora no puede ser anterior a hoy');
        FechaCorrecta := False;
      end;
    until FechaCorrecta = True;

    //Cambio a UTC
    FFecha := LocalTimeToUniversal(FFecha);

    FTimer := TFPTimer.Create(Self);
    FTimer.Interval := 1000;
    FTimer.OnTimer := @DoTick;
    FTimer.Enabled := True;
    try
      repeat
        Sleep(10);
        CheckSynchronize; // Needed, because we are not running in a GUI loop.
      until PollKeyEvent <> 0;
    finally
      FTimer.Enabled := False;
      FreeAndNil(FTimer);
    end;
    Terminate;
  end;

  procedure TTestTimerApp.DoTick(Sender: TObject);
  var
    FechaActual, HoraActual, HoraLimite: TDateTime;

    Horas, Segundos, Minutos: int64;
    Anos, Meses, Dias: word;
  begin
    FechaActual := LocalTimeToUniversal(Now);
    HoraActual := TimeOf(FechaActual);
    HoraLimite := TimeOf(FFecha);
    PeriodBetween(FechaActual, FFecha, Anos, Meses, Dias);


    Horas := HoursBetween(HoraActual, HoraLimite);
    Minutos := MinutesBetween(HoraActual, HoraLimite) - (Horas * 60);
    Segundos := SecondsBetween(HoraActual, HoraLimite);
    Segundos := Abs((Minutos * 60 - Segundos));

    ClrScr;
    GotoXY(1, 1);
    Writeln(Format('Quedan %d años, %d meses, %d dias, %d horas, %d minutos, %d segundos',
      [Anos, Meses, dias, horas, minutos, Segundos]));
  end;


begin

  with TTestTimerApp.Create(nil) do
  try
    Run
  finally
    Free;
    WriteLn('Exit');
  end;
end.
