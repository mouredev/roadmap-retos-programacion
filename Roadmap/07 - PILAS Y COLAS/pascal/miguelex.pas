{ OJO, el codigo que viene a continuación debe ir en un fichero aparte llamado ColaYPilaUnit.pas }
unit ColaYPilaUnit;

{$mode objfpc}{$H+}

interface

type
  Cola = class
  private
    cola: array of Integer;
    inicio: Integer;
    fin: Integer;
    max: Integer; // Opcional para limitar el tamaño de la cola
  public
    constructor Create;
    procedure encolar(elemento: Integer);
    function desencolar: Integer;
    procedure mostrar;
  end;

  Pila = class
  private
    pila: array of Integer;
    tope: Integer;
    max: Integer; // Opcional para limitar el tamaño de la pila
  public
    constructor Create;
    procedure apilar(elemento: Integer);
    function desapilar: Integer;
    procedure mostrar;
    function getPosition(i: Integer): Integer;
    function getTope: Integer;
  end;

implementation

constructor Cola.Create;
begin
  SetLength(cola, 10); // Tamaño predeterminado de la cola
  inicio := 0;
  fin := 0;
  max := 10; // Opcional para limitar el tamaño de la cola
end;

procedure Cola.encolar(elemento: Integer);
begin
  if fin < max then
  begin
    cola[fin] := elemento;
    fin := fin + 1;
  end
  else
    WriteLn('La cola está llena');
end;

function Cola.desencolar: Integer;
begin
  if inicio < fin then
  begin
    Result := cola[inicio];
    inicio := inicio + 1;
  end
  else
  begin
    WriteLn('La cola está vacía');
    Result := 0; // Puedes elegir un valor de retorno apropiado aquí
  end;
end;

procedure Cola.mostrar;
var
  i: Integer;
begin
  if inicio = fin then
    WriteLn('La cola está vacía')
  else
  begin
    for i := inicio to fin - 1 do
      Write(cola[i], ' ');
    WriteLn;
  end;
end;

constructor Pila.Create;
begin
  SetLength(pila, 7); // Tamaño predeterminado de la pila
  tope := 0;
  max := 7; // Opcional para limitar el tamaño de la pila
end;

procedure Pila.apilar(elemento: Integer);
begin
  if tope < max then
  begin
    pila[tope] := elemento;
    tope := tope + 1;
  end
  else
    WriteLn('La pila está llena');
end;

function Pila.desapilar: Integer;
begin
  if tope > 0 then
  begin
    tope := tope - 1;
    Result := pila[tope];
  end
  else
  begin
    WriteLn('La pila está vacía');
    Result := 0; // Puedes elegir un valor de retorno apropiado aquí
  end;
end;

procedure Pila.mostrar;
var
  i: Integer;
begin
  if tope = 0 then
    WriteLn('La pila está vacía')
  else
  begin
    for i := tope - 1 downto 0 do
      Write(pila[i], ' ');
    WriteLn;
  end;
end;

function Pila.getPosition(i: Integer): Integer;
begin
  Result := pila[i];
end;

function Pila.getTope: Integer;
begin
  Result := tope;
end;

end.

{ Aqui acaba el codigo a incluir en el fichero ColaYPilaUnit.pas Lo que sigue es el programa principal y se queda en este archivo}

program miguelex;

{$mode objfpc}{$H+}

uses
  ColaYPilaUnit;

var
  miCola: Cola;
  miPila: Pila;
  entrada: String;
  ultimoIndexVisitado: Integer;
  cabeza: Integer;
  documento: Integer;

begin
  WriteLn('Vamos a trabajar con la cola');
  WriteLn('Vamos a mostrar el contenido de la cola al inicio de la misma: ');
  miCola := Cola.Create;
  miCola.mostrar;
  WriteLn;

  WriteLn('Vamos a encolar 3 elementos: 1, 2 y 3');
  miCola.encolar(1);
  miCola.encolar(2);
  miCola.encolar(3);

  WriteLn('Vamos a mostrar el contenido de la cola después de encolar 3 elementos: ');
  miCola.mostrar;
  WriteLn;

  WriteLn('Vamos a desencolar un elemento');
  miCola.desencolar;

  WriteLn('Vamos a mostrar el contenido de la cola después de desencolar un elemento: ');
  miCola.mostrar;
  WriteLn;

  WriteLn('Vamos a encolar 2 elementos: 4 y 5 y vamos a desencolar dos');
  miCola.encolar(4);
  miCola.encolar(5);
  miCola.desencolar;
  miCola.desencolar;

  WriteLn('Vamos a mostrar el contenido de la cola después de encolar 2 elementos y desencolar dos: ');
  miCola.mostrar;
  WriteLn;

  WriteLn('Por último, vamos a desencolar tres elementos (recuerda que realmente solo nos quedan 2 dentro de la cola)');
  miCola.desencolar;
  miCola.desencolar;
  miCola.desencolar;

  WriteLn('Vamos a mostrar el contenido de la cola después de desencolar tres elementos: ');
  miCola.mostrar;
  WriteLn;

  WriteLn('Ahora, vamos a trabajar con la pila');
  WriteLn;

  miPila := Pila.Create;
  WriteLn('Vamos a mostrar el contenido de la pila al inicio de la misma: ');
  miPila.mostrar;
  WriteLn;

  WriteLn('Vamos a apilar 3 elementos: 1, 2 y 3');
  miPila.apilar(1);
  miPila.apilar(2);
  miPila.apilar(3);

  WriteLn('Vamos a mostrar el contenido de la pila después de apilar 3 elementos: ');
  miPila.mostrar;
  WriteLn;

  WriteLn('Vamos a desapilar un elemento');
  miPila.desapilar;

  WriteLn('Vamos a mostrar el contenido de la pila después de desapilar un elemento: ');
  miPila.mostrar;
  WriteLn;

  WriteLn('Vamos a apilar 2 elementos: 4 y 5 y vamos a desapilar dos');
  miPila.apilar(4);
  miPila.apilar(5);
  miPila.desapilar;
  miPila.desapilar;

  WriteLn('Vamos a mostrar el contenido de la pila después de apilar 2 elementos y desapilar dos: ');
  miPila.mostrar;
  WriteLn;

  WriteLn('Por último, vamos a desapilar tres elementos (recuerda que realmente solo nos quedan 2 dentro de la pila)');
  miPila.desapilar;
  miPila.desapilar;
  miPila.desapilar;

  WriteLn('Vamos a mostrar el contenido de la pila después de desapilar tres elementos: ');
  miPila.mostrar;
  WriteLn;

  WriteLn('Vamos a simular el mecanismo adelante/atrás de un navegador web');

  ultimoIndexVisitado := -1;

  repeat
    cabeza := miPila.getTope - 1;

    Write('Escribe el nombre de la web, adelante, atras o exit: ');
    ReadLn(entrada);
    if entrada = 'adelante' then
    begin
      if ultimoIndexVisitado < cabeza then
      begin
        ultimoIndexVisitado := ultimoIndexVisitado + 1;
        WriteLn('Navegando adelante a la web: ', miPila.getPosition(ultimoIndexVisitado));
      end
      else
        WriteLn('No hay más webs para navegar adelante');
    end
    else if entrada = 'atras' then
    begin
      if ultimoIndexVisitado > 0 then
      begin
        ultimoIndexVisitado := ultimoIndexVisitado - 1;
        WriteLn('Navegando atrás a la web: ', miPila.getPosition(ultimoIndexVisitado));
      end
      else
        WriteLn('No hay más webs para navegar atrás');
    end
    else if entrada <> 'exit' then
    begin
      miPila.apilar(StrToInt(entrada[1]));
      ultimoIndexVisitado := miPila.getTope - 1;
      WriteLn('Estás en la web: ', entrada);
    end;
  until entrada = 'exit';

  WriteLn('Vamos a simular el mecanismo de una cola de impresión');

  repeat
    Write('Escribe el nombre del documento, imprimir o exit: ');
    ReadLn(entrada);
    if entrada = 'imprimir' then
    begin
      documento := miCola.desencolar;
      if documento <> 0 then
        WriteLn('Imprimiendo documento: ', documento)
      else
        WriteLn('No hay documentos para imprimir');
    end
    else if entrada <> 'exit' then
    begin
      miCola.encolar(StrToInt(entrada[1]));
      WriteLn('Documento encolado: ', entrada);
    end;
  until entrada = 'exit';

end.
