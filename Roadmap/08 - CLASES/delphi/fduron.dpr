(* Para mi papá, la razón de ser quien soy.
 *
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 *)
program fduron;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils;

type
  TPersona = Class
  private
    FNombre: String;
    FEdad: Integer;
    FColorFavorito: String;
    FHobbie: string;
    function GetNombre: String;
    procedure SetNombre(const Value: String);
    function GetEdad: Integer;
    procedure SetEdad(const Value: Integer);
  public
    constructor Create(ANombre: String; Edad: Integer);
    property Nombre: String read GetNombre write SetNombre;
    property Edad: Integer read GetEdad write SetEdad;
    property ColorFavorito: String read FColorFavorito write FColorFavorito;
    property Hobbie: string read FHobbie write FHobbie;
    procedure ImprimirDatos;
  end;

  TPila = Class //LIFO
  private
    FListaPila: Array of String;
    function GetCantidadDeElementos: Integer;
  public
    procedure Push(Valor: String);
    function Pop: String;
    property CantidadDeElementos: Integer read GetCantidadDeElementos;
    procedure ImprimirContenido;
  End;

  TCola = Class //FIFO
  private
    FListaCola: Array of String;
    function GetCantidadDeElementos: Integer;
  public
    procedure ALaCola(Valor: String);
    function DeLaCola: String;
    property CantidadDeElementos: Integer read GetCantidadDeElementos;
    procedure ImprimirContenido;
  End;

{ TPersona }

constructor TPersona.Create(ANombre: String; Edad: Integer);
begin
  FNombre := ANombre;
  FEdad := Edad;
end;

function TPersona.GetEdad: Integer;
begin
  Result := FEdad;
end;

function TPersona.GetNombre: String;
begin
  Result := FNombre;
end;

procedure TPersona.SetEdad(const Value: Integer);
begin
  FEdad := Value;
end;

procedure TPersona.SetNombre(const Value: String);
begin
  FNombre := Value;
end;

procedure TPersona.ImprimirDatos;
begin
  WriteLn('INFORMACIÓN DE LA PERSONA:');
  WriteLn('Nombre: ', Nombre);
  WriteLn('Edad: ', Edad);
  WriteLn('Color favorito: ', ColorFavorito);
  WriteLn('Hobbie: ', Hobbie);
  WriteLn;
end;

{ TPila }

function TPila.GetCantidadDeElementos: Integer;
begin
  Result := Length(FListaPila);
end;

procedure TPila.ImprimirContenido;
begin
  for var i := Length(FListaPila) - 1 downto 0 do
    WriteLn(FListaPila[i]);
end;

function TPila.Pop: String;
var
  Posicion: Integer;
begin
  Posicion := Length(FListaPila) - 1;
  Result := FListaPila[Posicion];
  SetLength(FListaPila, Posicion);
end;

procedure TPila.Push(Valor: String);
var
  Posicion: Integer;
begin
  Posicion := Length(FListaPila) + 1;
  SetLength(FListaPila, Posicion);
  FListaPila[Posicion - 1] := Valor;
end;

{ TCola }

procedure TCola.ALaCola(Valor: String);
var
  Posicion: Integer;
begin
  Posicion := Length(FListaCola) + 1;
  SetLength(FListaCola, Posicion);
  FListaCola[Posicion - 1] := Valor;
end;

function TCola.DeLaCola: String;
var
  Posicion: Integer;
begin
  Result := FListaCola[0];
  //Recorrer los elementos hacia atrás
  for var i := 0 to Length(FListaCola) - 2 do
    FListaCola[i] := FListaCola[i + 1];
  SetLength(FListaCola, Length(FListaCola) - 1);
end;

function TCola.GetCantidadDeElementos: Integer;
begin
  Result := Length(FListaCola);
end;

procedure TCola.ImprimirContenido;
begin
  for var Elemento in FListaCola do
    WriteLn(Elemento);
end;

var
  UnaPersona: TPersona;
  UnaPila: TPila;
  UnaCola: TCola;
begin
  UnaPersona := TPersona.Create('Juanita', 25);
  UnaPersona.Edad := 26;
  UnaPersona.ColorFavorito := 'Rojo';
  UnaPersona.Hobbie := 'Bailar';
  UnaPersona.ImprimirDatos;
  UnaPersona.free;
  WriteLn;

  WriteLn('**********************************');
  WriteLn('*        DIFICULTAD EXTRA        *');
  WriteLn('**********************************');
  UnaPila := TPila.Create;
  WriteLn('-= PILAS =-');
  UnaPila.Push('Valor en la pila uno');
  UnaPila.Push('Valor en la pila dos');
  UnaPila.Push('Valor en la pila tres');
  UnaPila.Push('Valor en la pila CUATRO');
  WriteLn('Elementos en la pila: ', UnaPila.CantidadDeElementos);
  WriteLn('Contenido de la pila:');
  UnaPila.ImprimirContenido;
  WriteLn;
  WriteLn('Elemento eliminado: ', UnaPila.Pop);
  WriteLn('Nuevo contenido de la pila:');
  UnaPila.ImprimirContenido;
  WriteLn;
  UnaPila.Free;

  UnaCola := TCola.Create;
  WriteLn('-= COLAS =-');
  UnaCola.ALaCola('Valor en la cola uno');
  UnaCola.ALaCola('Valor en la cola dos');
  UnaCola.ALaCola('Valor en la cola tres');
  UnaCola.ALaCola('Valor en la cola cuatro');
  UnaCola.ALaCola('Valor en la cola CINCO');
  WriteLn('Elementos en la cola: ', UnaCola.CantidadDeElementos);
  WriteLn('Contenido de la cola:');
  UnaCola.ImprimirContenido;
  WriteLn;
  WriteLn('Elemento eliminado: ', UnaCola.DeLaCola);
  WriteLn('Nuevo contenido de la pila:');
  UnaCola.ImprimirContenido;
  UnaCola.Free;

  ReadLn;

end.
