program getURL;
{$mode objfpc}

uses
    Classes, Crt, fphttpclient, opensslsockets, sysutils;

var
    ClienteHttp : TFPHTTPClient;
    Respuesta   : TStringStream;
    URL         : string;

begin
  try
    ClrScr;
    URL := 'https://pokeapi.co/api/v2/pokemon/ditto';

    ClienteHttp := TFPHTTPClient.Create(nil);
    Respuesta   := TStringStream.Create('');

    try
        ClienteHttp.Get(URL, Respuesta);

        if ClienteHttp.ResponseStatusCode = 200 then
        begin
            Writeln('Respuesta 200 OK: ');
            Writeln(Respuesta.DataString)
        end
        else
        begin
            Writeln('La solicitud fallo.  Codigo de Respuesta: ', ClienteHttp.ResponseStatusCode)
        end;
    except
        on E: Exception do
        begin
            Writeln('Error al realizar la solicitud: ', E.Message);
        end;
    end;
  finally
        ClienteHttp.free;
        Respuesta.free;
  end;
end.
