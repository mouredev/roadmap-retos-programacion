(*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 *)

program fduron;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils,
  System.Generics.Collections;

type
  TContacto = Record
     Nombre,
     Telefono: String;
     RegistroActivo: Boolean;
  end;

  TRegistro = Record
    Campo1: Integer;
    Campo2: String;
    Campo3: 1..20;
    Campo4: String[40];
  end;

  TRegistroDefinido = record
    Nombre, Apellido: string[40];
    Nacimiento: TDate;
    case SueldoAnual: boolean of
      True: (MontoAnual: Currency);
      False: (MontoMensual: Currency);
  end;

  TRegistroAvanzado = record
    type
      TNumeroDeColor = Integer;
    var
      FRojo: Integer;
    class var
      FAzul: Integer;
    procedure imprimeRojo();
    constructor Create(Val: Integer);
    property Rojo: TNumeroDeColor read FRojo write FRojo;
    class property Azul: TNumeroDeColor read FAzul write FAzul;
  end;

  TElementos = (Elemento1, Elemento2, Elemento3, Elemento4, Elemento5);
var
  Conjunto: set of TElementos;
  UnElemento: TElementos;
  Arreglo: array [64..120] of Char;
  Matriz: array[1..100,1..100] of Real;
  ArregloDinamico: array of Real; //El tamaño se define en tiempo de ejecusión
  ArregloClase: TArray<integer>;
  Registro: TRegistro;
  RegistroAvanzado: TRegistroAvanzado;
  UnDiccionario: TDictionary<string, TRegistro>;
  PilaFIFO: TQueue<String>;
  Lista: TList<Integer>;
  PilaLIFO: TStack<String>;
  //Dificultad Extra
  Agenda: TList<TContacto>;

/// <summary>
///  Para el reto de dificultad extra se utiliza un TList por ser uno de los tipos
///  de estructura mas basicos en Delphi (después del Array simple), para cumplir
///  con este reto se pueden utilizar clases, objetos, diccionarios o arreglos
///  dinamicos con metodos que evaluen los campos del contacto. Sin embargo
///  por ser de los primeros retos preferí omitit el uso de estructuras
///  más avanzadas ya que supongo que se verán mas adelante. F
/// </summary>
procedure DificultadExtra;
  procedure VerMenuPrincipal;
  begin
    WriteLn;
    WriteLn('******************************************');
    WriteLn('****       AGENDA DE CONTACTOS        ****');
    WriteLn('******************************************');
    WriteLn;
    WriteLn('<?> Menú de opciones');
    WriteLn('------------------');
    WriteLn('<A> Insertar');
    WriteLn('<B> Buscar');
    WriteLn('<C> Actualizar');
    WriteLn('<D> Eliminar');
    WriteLn('<L> Lista de contactos');
    WriteLn('------------------');
    WriteLn('<X> Salir');
  end;

  function ContactoCorrecto(const Contacto: TContacto): boolean;
  begin
    Result := True;
    if Contacto.Nombre.IsEmpty then
    begin
      WriteLn('El nombre no puede estar vacio');
      Result := False;
    end;
    if (Contacto.telefono.Length < 11) then
    begin
      for var I := 1 to Contacto.Telefono.Length do
        if not (Contacto.Telefono[I] in ['0'..'9']) then
        begin
          WriteLn('#Solo se aceptan numeros en el campo teléfono.');
          Exit(False);
        end;
      end
    else
    begin
      WriteLn('#El telefono no puede tener mas de 11 numeros');
      Result := False;
    end;
  end;

  /// <summary>
  ///  se utiliza el metodo mas simple de busqueda, ya que la busqueda se realiza
  ///  únicamente por el nombre no se utiliza BinarySearch, así que no es
  ///  necesario que el arreglo este ordenado.
  ///  En caso de que el NombreBuscado no exista se recorre
  ///  el arreglo por completo, si NombreBuscado es localizado se detiene la
  ///  busqueda y se regresa el Indice de la posición donde se encontró
  /// </summary>
  /// <param name="NombreBuscado">
  ///   Nombre del contacto que se esta buscando
  /// </param>
  /// <param name="Indice">
  ///   Regresa la posición donde se encontro el nombre o -1 en caso contrario
  /// </param>
  /// <returns>
  ///   Verdadero si el nombre se encuentra en la agenda, Falso en caso contrario
  /// </returns>
  function NombreEncontrado(const NombreBuscado: String; var Indice: Integer): Boolean;
  begin
    Result := False;
    Indice := -1;
    for var Contacto in Agenda do //Extraer cada contacto de la agenda
    begin
      if Contacto.Nombre = NombreBuscado then
      begin
        Indice := Agenda.IndexOf(Contacto);
        //se utiliza Exit(True); en lugar de Result := True; para romper el cilo for
        Exit(True);
      end
    end;
  end;

  function InsertarContacto: Boolean;
  var
    Contacto: TContacto;
    C: Char;
    idx: Integer;
  begin
    Result := False;
    Contacto.RegistroActivo := True;

    WriteLn('-- Insertar contacto');
    Write('Nombre: ');
    ReadLn(Contacto.Nombre);
    Write('Teléfono: ');
    ReadLn(Contacto.Telefono);
    Write('¿Datos correctos? (S/N) ');
    ReadLn(C);
    if (UpperCase(C) = 'S') and ContactoCorrecto(Contacto) then
    begin
      if not NombreEncontrado(Contacto.Nombre, idx) then
      begin
        Agenda.Add(Contacto);
        WriteLn('# Contacto "', Contacto.Nombre, '" agregado');
        Result := True;
      end
      else
      begin
        WriteLn('# El contacto "', Contacto.Nombre, '" ya existe en la agenda');
        Result := True;
      end;
    end;
  end;

  function BuscarContacto: boolean;
  var
    Contacto: TContacto;
    Nombre: String;
    Idx: Integer;
  begin
    WriteLn('-- Buscar un contacto');
    Write('Nombre: ');
    ReadLn(Nombre);
    Result := NombreEncontrado(Nombre, Idx);
    if Result then
    begin
      WriteLn('# Contacto encontrado:');
      Contacto := Agenda[Idx];
      WriteLn('Nombre: ', Contacto.Nombre, ', Teléfono: ', Contacto.Telefono);
    end
    else
      WriteLn('# El contacto "', Nombre, '" no se enuentra en la agenda')
  end;

  function ActualizarContacto: Boolean;
  var
    Contacto: TContacto;
    Nombre: String;
    Idx: Integer;
    C: Char;
  begin
    WriteLn('-- Actualizar un contacto');
    Write('Escriba el nombre del contacto: ');
    ReadLn(Nombre);
    if NombreEncontrado(Nombre, Idx) then
    begin
      Contacto := Agenda[Idx];
      WriteLn('Nombre: ', Contacto.Nombre, ', Teléfono: ', Contacto.Telefono);
      Write('Nuevo nombre: ');
      ReadLn(Contacto.Nombre);
      Write('Nuevo Teléfono: ');
      ReadLn(Contacto.Telefono);
      Write('¿Datos correctos? (S/N) ');
      ReadLn(C);
      if (UpperCase(C) = 'S') and ContactoCorrecto(Contacto) then
      begin
        Agenda[Idx] := Contacto;
        Result := True;
      end;
    end
    else
      Write('# El contacto "', Nombre, '" no se encuentra en la agenda');
  end;

  function EliminarContacto: Boolean;
  var
    Nombre: String;
    Idx: Integer;
    C: Char;
  begin
    Result := False;
    WriteLn('-- Eliminar un contacto');
    Write('Escriba el nombre del contacto: ');
    ReadLn(Nombre);
    if NombreEncontrado(Nombre, Idx) then
    begin
      Write('¿Esta seguro de eliminar al contacto? (S/N) ');
      ReadLn(C);
      if UpperCase(C) = 'S' then
      begin
        Agenda.Delete(Idx);
        WriteLn('# El contacto "', Nombre, '" Ha sido eliminado de la agenda');
        Result := True;
      end;
    end
    else
      Write('# El contacto "', Nombre, '" no se encuentra en la agenda');
  end;

  procedure ListarContactos;
  begin
    WriteLn;
    if Agenda.Count = 0 then
      WriteLn('# No hay contactos en la agenda')
    else
    for var Contacto in Agenda do
      WriteLn('Nombre: ', Contacto.Nombre, ', Teléfono: ', Contacto.Telefono);

    WriteLn;
  end;

var
  C: Char;
  S: String;
begin
  WriteLn;
  Write('Deseas iniciar la agenda de contactos? (S/N) ');
  ReadLn(C);
  if UpperCase(C) = 'S' then
  try
    Agenda := TList<Tcontacto>.Create;
    VerMenuPrincipal;
    Repeat
      WriteLn;
      Write('Elija una opción: ');
      ReadLn(C);
      {Convertir el contenido de la variable "C" a mayusculas, y obtener
       solamente el primer caracter [1] para usarlo en la instrucción CASE}
      C := UpperCase(C)[1];
      case C of
        'A': InsertarContacto;
        'B': BuscarContacto;
        'C': ActualizarContacto;
        'D': EliminarContacto;
        'L': ListarContactos;
        '?': VerMenuPrincipal;
      else
        WriteLn('# Opción incorrecta use ? para ver el menú');
      end;
    Until C = 'X';
  finally
    Agenda.Free;
  end;
end;

{ TRegistroAvanzado }
constructor TRegistroAvanzado.Create(Val: Integer);
begin
  Rojo := Val;
end;

procedure TRegistroAvanzado.imprimeRojo;
begin
  WriteLn('Rojo: ', Rojo);
end;

var
  R, R2: TRegistro;
  IndiceEncontrado: integer;
begin
  Conjunto := [Elemento1, Elemento3, Elemento4];
  UnElemento := Elemento1;
  if UnElemento in Conjunto then
    WriteLn('el contenido de la variable UnElemento se encuentra en la variable Conjunto')
  else
    WriteLn('el contenido de la variable UnElemento no se encuentra en la variable Conjunto');

  //Agregar elementos al Arreglo
  for var I := 64 to 120 do //Declaración en linea de una variable "I"
    Arreglo[I] := Chr(I);

  WriteLn('Arreglo en la posicion 65 es ', Arreglo[65]);
  WriteLn('Arreglo en la posicion 70 es ', Arreglo[70]);
  WriteLn('Arreglo en la posicion 110 es ', Arreglo[110]);

  SetLength(ArregloDinamico, 10);
  for var I := Low(ArregloDinamico) to High(ArregloDinamico) do
    ArregloDinamico[I] := I * 3.33;

  WriteLn('ArregloDinamico en la posición 5 es ', ArregloDinamico[5]);
  WriteLn('ArregloDinamico en la posición 9 es ', ArregloDinamico[9]);
  WriteLn('ArregloDinamico en la posición 8 es ', ArregloDinamico[8]);

  R.Campo1 := 1;
  R.Campo2 := 'Un nombre';
  R.Campo3 := 10;
  R.Campo4 := 'Texto adicional';

  R2.Campo1 := 2;
  R2.Campo2 := 'Nombre 2';
  R2.Campo3 := 20;
  R2.Campo4 := 'Texto adicional dos';

  UnDiccionario := TDictionary<string, TRegistro>.Create;
  ArregloClase := TArray<integer>.Create(100,250,28,57,110,2,44,68,25,215);
  PilaFIFO := TQueue<String>.Create;
  PilaLIFO := TStack<String>.Create;
  Lista := TList<Integer>.Create;

  try
    //Agregar nuevos valores a UnDiccionario
    UnDiccionario.Add('Uno', R);
    UnDiccionario.Add('Dos', R2);
    //Modificar valores a unDiccionario
    R2.Campo2 := 'Nombre numero dos';
    UnDiccionario.AddOrSetValue('Dos', R2);
    //Eliminar valores de UnDiccionario
    UnDiccionario.ExtractPair('Dos');
    //TDictionary no se puede ordenar directamente
    for var ElemDiccionario in UnDiccionario do
      WriteLn('Diccionario: "', ElemDiccionario.Key, '"',
        ' Campo1:', ElemDiccionario.Value.Campo1,
        ' Campo2:', ElemDiccionario.Value.Campo2,
        ' Campo3:', ElemDiccionario.Value.Campo3);

    //Insertar elementos a la pilaFIFO
    PilaFIFO.Enqueue('Texto 1');
    PilaFIFO.Enqueue('Texto 2');
    PilaFIFO.Enqueue('Texto 3');
    PilaFIFO.Enqueue('Texto 4');
    PilaFIFO.Enqueue('Texto 5');
    WriteLn('El primer elementos de la PilaFIFO es: ', PilaFIFO.Peek);

    //Extraer el primero de la pila "Texto 1"
    PilaFIFO.Extract;
    PilaFIFO.TrimExcess; //Ajustar la capacidad de la pila
    WriteLn('PilaFIFO contiene ', PilaFIFO.Count, ' elementos');
    //Limpiar la pila
    PilaFIFO.Clear;

    //Insertar elementos a la PilaLIFO
    PilaLIFO.Push('Texto 1');
    PilaLIFO.Push('Texto 2');
    PilaLIFO.Push('Texto 3');
    PilaLIFO.Push('Texto 4');
    PilaLIFO.Push('Texto 5');
    WriteLn('El último elemento agregado a PilaLIFO es: ', PilaLIFO.Peek);

    //Extraer el ultimo elemento de la pila "Texto 5"
    PilaLIFO.Extract;
    PilaLIFO.Pop;
    PilaLIFO.TrimExcess; //Ajustar la capacidad de la pila
    WriteLn('PilaLIFO contiene ', PilaLIFO.Count, ' elementos');
    //Limpiar la pila
    PilaLIFO.Clear;

    //Ordenar ArregloClase
    TArray.Sort<integer>(ArregloClase);
    //buscar en ArregloClase
    if TArray.BinarySearch<integer>(ArregloClase, 57, IndiceEncontrado) then
      WriteLn('Elemento encontrado en ', IndiceEncontrado);

    //Agregar elementos a Lista
    Lista.AddRange([10,5,7,83,9,62,4,1,81,9,32,12,5,45,1]);
    WriteLn('Indice del primer 1 en "Lista": ', Lista.IndexOf(1));
    WriteLn('Indice del ultimo 1 en "Lista": ', Lista.LastIndexOf(1));
    WriteLn('"Lista" contiene el numero 144 : ', Lista.Contains(144));

    Write('Elementos en "Lista": ');
    for var ItemLista in Lista do
      Write(ItemLista, ', ');
    WriteLn;

    //Agregar elementos a Lista
    Lista.Add(100);
    Lista.Insert(0, 5);
    Lista.InsertRange(0, [5,8,7,6,3]); //Insertar un rango a partir de la posición 0
    //Eliminar elementos
    Lista.Delete(0); //Eliminar el elemento 0 de Lista
    Lista.DeleteRange(0, 2); //Eleminar 2 elementos a partir del indice 0
    Lista.Extract(1); //Remover los elementos 1 de Lista

    Write('Elementos en "Lista": ');
    for var ItemLista in Lista do
      Write(ItemLista, ', ');
    WriteLn;

    //Ordenar Lista
    Lista.Sort;
    Write('Elementos ordenados en "Lista": ');
    for var ItemLista in Lista do
      Write(ItemLista, ', ');
    WriteLn;

    //Buscar
    if Lista.BinarySearch(62, IndiceEncontrado) then
      WriteLn('elemento 62 encontrado en la posición ', IndiceEncontrado);

    Lista.Reverse; //Invertir el orden

  finally
    UnDiccionario.Free;
    PilaFIFO.Free;
    Lista.Free;
    PilaLIFO.Free;
  end;

  DificultadExtra;
end.
