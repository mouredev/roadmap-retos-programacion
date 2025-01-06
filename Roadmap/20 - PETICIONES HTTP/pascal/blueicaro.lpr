program blueicaro;
{

 EJERCICIO:
 Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 una petición a la web que tú quieras, verifica que dicha petición
 fue exitosa y muestra por consola el contenido de la web.

 DIFICULTAD EXTRA (opcional):
 Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 terminal al que le puedas solicitar información de un Pokémon concreto
 utilizando su nombre o número.
 - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 - Muestra el nombre de su cadena de evoluciones
 - Muestra los juegos en los que aparece
 - Controla posibles errores

 Este ejercicio se centra la realización del apartado:  DIFICULTAD EXTRA

}

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}
  cthreads,
  {$ENDIF}
  Classes,
  opensslsockets,
  fphttpclient,
  fpjson,
  jsonparser,
  crt,
  SysUtils;

var
  Opcion: integer;

  procedure MuestraDato(aJson: TJSONData; CampoJson: string; NombreDato: string);
  var
    info: string;
    dato: TJSONData;
  begin
    info := '';
    dato := aJson.FindPath(CampoJson);
    if dato <> nil then
    begin
      info := dato.AsString;
    end;
    WriteLn(NombreDato + ': ' + info);
  end;

  procedure ProcesarRespuesta(aRespuesta: string);
  var
    miJson, dato: TJSONData;
    I: integer;
  begin
    ClrScr;
    try
      miJson := GetJSON(aRespuesta, False);
      MuestraDato(miJson, 'ID', 'ID');
      MuestraDato(miJson, 'name', 'Nombre');
      MuestraDato(miJson, 'height', 'Alto');
      MuestraDato(miJson, 'weight', 'Peso');
      Dato := miJson.FindPath('types');
      if Dato <> nil then
      begin
        WriteLn('Tipo(s)q:');
        for I := 0 to dato.Count - 1 do
        begin
          Writeln(#09 + dato.Items[I].FindPath('type').FindPath('name').AsString);
        end;
      end;
    finally
      FreeAndNil(miJson);
    end;
  end;

  procedure ProcesarEvolucion(Respuesta: string);
  var
    miJson, Dato, Evolucion, Nombre: TJSONData;
    I, x: integer;

    procedure Evolves_to(adato: TJSONData);
    var
      Env: TJSONData;
    begin
      if adato.FindPath('species') <> nil then
        if adato.FindPath('species').FindPath('name') <> nil then
        begin
          Writeln('Nombre: ' + adato.FindPath('species').FindPath(
            'name').AsString);
          Env := adato.FindPath('evolves_to');
          if Env <> nil then
          begin
            Evolves_to(Env);
          end;
        end;
    end;

  begin
    try
      miJson := GetJSON(Respuesta);
      writeln('Cadena de evoluciones');
      Dato := miJson.FindPath('chain').FindPath('species');
      if Dato <> nil then
      begin
        MuestraDato(Dato, 'name', 'nombre');
      end;
      Dato := miJson.FindPath('chain').FindPath('evolves_to');
      if Dato <> nil then
      begin
        Nombre := Dato.items[0].FindPath('species').FindPath('name');
        if nombre <> nil then
        begin
          Writeln(Nombre.AsString);
          Evolves_to(Dato.items[0]);
        end;
      end;
    finally
      FreeAndNil(miJson);
    end;
  end;

  procedure ProcesarJuegos(aJuegos: string);
  var
    jsonData, Dato: TJSONData;
    i: integer;
  begin
    //Juegos
    try
      jsonData := GetJSON(aJuegos, False);
      Writeln('Juegos: ');
      if jsonData.FindPath('game_indices') <> nil then
      begin
        for i := 0 to jsonData.FindPath('game_indices').Count - 1 do
        begin
          Dato := jsonData.FindPath('game_indices').Items[I];
          Writeln(#09 + Dato.FindPath('version').FindPath('name').AsString);
        end;
      end;
    finally
      FreeAndNil(jsonData);
    end;
  end;

  function UrlEvolucion(aEvolucion: string): string;
  var
    json, Dato: TJSONData;
  begin
    Result := '';
    try
      json := GetJSON(aEvolucion, False);
      Dato := json.FindPath('evolution_chain').FindPath('url');
      Result := Dato.AsString;
    finally
      FreeAndNil(json);
    end;
  end;

  procedure Obtenerdatos(parametro: string);
  var
    Conexion: TFPHTTPClient;
    pokemon, species, pokemon_species: TStringList;
    jsonPokemon, Dato: TJSONData;
    Url: TJSONStringType;
    i: integer;
  begin
    Conexion := TFPHTTPClient.Create(nil);
    pokemon := TStringList.Create;
    pokemon_species := TStringList.Create;
    try
      try
        Conexion.Get('https://pokeapi.co/api/v2/pokemon/' + parametro, pokemon);
        if Conexion.ResponseStatusCode = 200 then
        begin
          ProcesarRespuesta(pokemon.Text);
          //Obtener evolucion
          Conexion.Get('https://pokeapi.co/api/v2/pokemon-species/' +
            parametro, pokemon_species);
          Url := UrlEvolucion(pokemon_species.Text);
          if Url <> '' then
          begin
            pokemon_species.Clear;
            Conexion.Get(url, pokemon_species);
            ProcesarEvolucion(pokemon_species.Text);
          end;
          ProcesarJuegos(pokemon.Text);
        end
        else
        begin
          Writeln('Error de conexión: ' + Conexion.ResponseStatusText);
        end;
      except
        on E: Exception do
        begin
          WriteLn(E.Message);
          ReadLn;
        end;
      end;

    finally
      FreeAndNil(pokemon_species);
      FreeAndNil(pokemon);
      FreeAndNil(Conexion);
      Writeln('Pulsa una tecla para continuar');
      ReadLn;
    end;
  end;

  procedure GetPokemonNombre();
  var
    Nombre: string;
  begin
    ClrScr;
    Writeln('Introduce el nombre del pokemon a buscar: ');
    try
      Readln(Nombre);
      Obtenerdatos(Nombre);
    except
      exit;
    end;
  end;

  procedure GetPokemonId();
  var
    ID: integer;
  begin
    ClrScr;
    Writeln('Introduce el ID del pokemon a buscar: ');
    try
      Readln(ID);
      Obtenerdatos(IntToStr(Id));
    except
      exit;
    end;
  end;

begin
  Opcion := 0;
  repeat
    ClrScr;
    Writeln('Menu PokeApi');
    Writeln('Escoge una opción');
    Writeln('1. Buscar pokemon por su ID');
    WriteLn('2. Buscar pokemon por su nombre');
    Writeln('0. Salir');
  try

    ReadLn(Opcion);
    case Opcion of
      1:
        GetPokemonId();
      2:
        GetPokemonNombre();
      else
        Continue;
    end;
  except
    Writeln('Valor de opción invalido');
  end;
  until Opcion = 0;

end.
