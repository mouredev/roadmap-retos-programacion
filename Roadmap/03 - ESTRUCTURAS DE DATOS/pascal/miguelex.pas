program miguelex;

const
  MaxContactos = 100; { Lo usaremos para el ejercicio extra }

type
    tRegistro = record
        nombre: String[20];
        edad: Integer;
        direccion: String[50];
        telefono: String[9];
    end;

    Contacto = record { Lo usaremos para el ejercicio extra }
      Nombre: string;
      Telefono: string;
    end;

var

    ejemploArray: array[1..10] of Integer;
    i, j, aux: Integer;
    cadena : String[20];
    r: tRegistro;
    c: set of 1..10;
    Agenda: array[1..MaxContactos] of Contacto; { Lo usaremos para el ejercicio extra }
    NumContactos: integer; { Lo usaremos para el ejercicio extra }

procedure MostrarMenu;
begin
  writeln('1. Insertar contacto');
  writeln('2. Buscar contacto');
  writeln('3. Actualizar contacto');
  writeln('4. Eliminar contacto');
  writeln('5. Mostrar todos los contactos');
  writeln('6. Salir');
end;

procedure InsertarContacto;
var
  NuevoContacto: Contacto;
  TelefonoValido: Boolean;
begin
  writeln('Ingrese el nombre del contacto:');
  readln(NuevoContacto.Nombre);

  repeat
    writeln('Ingrese el número de teléfono:');
    readln(NuevoContacto.Telefono);

    // Validar que el número de teléfono sea numérico y tenga menos de 12 dígitos
    // (o el número de dígitos que prefieras)
    Val(NuevoContacto.Telefono, NumContactos, TelefonoValido);

    if (not TelefonoValido) or (Length(NuevoContacto.Telefono) > 11) then
      writeln('Número de teléfono no válido. Introduce nuevamente.');
  until TelefonoValido;

  if NumContactos < MaxContactos then
  begin
    NumContactos := NumContactos + 1;
    Agenda[NumContactos] := NuevoContacto;
    writeln('Contacto insertado correctamente.');
  end
  else
    writeln('La agenda está llena. Elimina algunos contactos antes de agregar nuevos.');
end;

procedure BuscarContacto;
var
  Busqueda: string;
  Encontrado: Boolean;
  i: Integer;
begin
  writeln('Ingrese el nombre o parte del nombre del contacto a buscar:');
  readln(Busqueda);

  Encontrado := False;
  for i := 1 to NumContactos do
  begin
    if Pos(upcase(Busqueda), upcase(Agenda[i].Nombre)) > 0 then
    begin
      writeln('Nombre: ', Agenda[i].Nombre);
      writeln('Teléfono: ', Agenda[i].Telefono);
      Encontrado := True;
    end;
  end;

  if not Encontrado then
    writeln('Contacto no encontrado.');
end;

procedure ActualizarContacto;
var
  NombreActualizar, NuevoTelefono: string;
  i: Integer;
  Encontrado: Boolean;
  TelefonoValido: Boolean;
begin
  writeln('Ingrese el nombre del contacto que desea actualizar:');
  readln(NombreActualizar);

  Encontrado := False;
  for i := 1 to NumContactos do
  begin
    if upcase(Agenda[i].Nombre) = upcase(NombreActualizar) then
    begin
      repeat
        writeln('Ingrese el nuevo número de teléfono:');
        readln(NuevoTelefono);

        Val(NuevoTelefono, NumContactos, TelefonoValido);

        if (not TelefonoValido) or (Length(NuevoTelefono) > 11) then
          writeln('Número de teléfono no válido. Introduce nuevamente.');
      until TelefonoValido;

      Agenda[i].Telefono := NuevoTelefono;
      writeln('Contacto actualizado correctamente.');
      Encontrado := True;
    end;
  end;

  if not Encontrado then
    writeln('Contacto no encontrado.');
end;

procedure EliminarContacto;
var
  NombreEliminar: string;
  i: Integer;
  Encontrado: Boolean;
begin
  writeln('Ingrese el nombre del contacto que desea eliminar:');
  readln(NombreEliminar);

  Encontrado := False;
  for i := 1 to NumContactos do
  begin
    if upcase(Agenda[i].Nombre) = upcase(NombreEliminar) then
    begin
      Agenda[i] := Agenda[NumContactos];
      NumContactos := NumContactos - 1;
      writeln('Contacto eliminado correctamente.');
      Encontrado := True;
    end;
  end;

  if not Encontrado then
    writeln('Contacto no encontrado.');
end;

procedure MostrarTodosLosContactos;
var
  i: Integer;
begin
  writeln('Lista de contactos:');
  for i := 1 to NumContactos do
  begin
    writeln('Nombre: ', Agenda[i].Nombre);
    writeln('Teléfono: ', Agenda[i].Telefono);
    writeln('--------------');
  end;
end;


var
  Opcion: integer;

begin  
    writeln('Ejemplos con arrays');
    writeln;

    writeln('Vamos a introducir 5 numeros aleatorios entre el 1 y 10');
    
    for i := 1 to 5 do
        ejemploArray[i] := random(10) + 1;

    writeln;

    writeln('Ahora vamos a mostrarlos');
    writeln;
    
    for i := 1 to 5 do
        writeln('Posicion ', i, ' valor ', ejemploArray[i]);
    writeln;

    writeln('Añadimos un nuevo numero al final');
    ejemploArray[6] := 100;

    writeln('Ahora vamos a mostrarlos');
    writeln;

    for i := 1 to 6 do
        writeln('Posicion ', i, ' valor ', ejemploArray[i]);
    writeln;

    writeln('Vamos a eliminar al elemento en la posicion 2');
    writeln;

    for i := 2 to 6 do
        ejemploArray[i] := ejemploArray[i + 1];
    
    writeln('Una vez eliminado el elemento en la posicion 2');
    writeln;

    for i := 1 to 5 do
        writeln('Posicion ', i, ' valor ', ejemploArray[i]);
    writeln;

    { Vamos a ordenar el array de menor a mayor }
    for i := 1 to 5 do
        for j := 1 to 5 do
            if ejemploArray[i] < ejemploArray[j] then
            begin
                aux := ejemploArray[i];
                ejemploArray[i] := ejemploArray[j];
                ejemploArray[j] := aux;
            end;
    
    writeln('Ordenados del menor al mayor:');
    for i := 1 to 5 do
        writeln('Posicion ', i, ' valor ', ejemploArray[i]);
    writeln;

    WriteLn('Se le nota los años a Pascal y no te da las facilidades de otros lenguajes para la ordenacion, por ejemplo, teniendo que hacerla de un modo mas manual');
    writeln;

    { Ejemplo con cadenas }
    writeln('Ejemplos con cadenas');

    writeln('Vamos a introducir una cadena');
    writeln;
    cadena := 'Miguelex';

    writeln('Vamos a mostrarla');
    writeln;
    writeln(cadena);
    writeln;

    writeln('Vamos a mostrarla al reves');
    writeln;
    for i := length(cadena) downto 1 do
        write(cadena[i]);
    writeln;

    { Vamos a mostrar la longitud de la cadena }
    writeln('La longitud de la cadena es ', length(cadena));
    writeln;

    { Vamos a mostrar la cadena en mayusculas }
    writeln('La cadena en mayusculas es ', upcase(cadena));
    writeln;

    { Vamos a mostrar la cadena en minusculas } 
    writeln('La cadena en minusculas es ', lowercase(cadena));
    writeln;

    { Vamos a añadir un caracter a la cadena }
    writeln('Vamos a añadir un caracter a la cadena');
    writeln;
    cadena := cadena + 'a';
    writeln('La cadena ahora es ', cadena);
    writeln;

    { Vamos a eliminar un caracter a la cadena }
    writeln('Vamos a eliminar un caracter a la cadena');
    writeln;
    cadena := copy(cadena, 1, length(cadena) - 1);
    writeln('La cadena ahora es ', cadena);
    writeln;

    { Ejemplo con registros }
    writeln('Ejemplos con registros');
    writeln;
    r.nombre := 'Pepe';
    r.edad := 20;
    r.direccion := 'Calle de la piruleta';
    r.telefono := '123456789';
    
    writeln('Vamos a mostrar el registro');
    writeln;
    writeln('Nombre: ', r.nombre);
    writeln('Edad: ', r.edad);
    writeln('Direccion: ', r.direccion);
    writeln('Telefono: ', r.telefono);
    writeln;

    { Ejemplo con conjuntos }

    writeln('Ejemplos con conjuntos');
    writeln;
    writeln('Vamos a crear un conjunto con los numeros del 1 al 10');
    writeln;
    
    for i := 1 to 10 do
        write(i, ' ');
    writeln;
   
    c := [1..10];
    writeln('Vamos a mostrar el conjunto');
    writeln;
    for i := 1 to 10 do
        if i in c then
            write(i, ' ');
    writeln;
    
    writeln('Vamos a añadir el 11 al conjunto');
    writeln;
    c := c + [11];
    
    writeln('Vamos a mostrar el conjunto');
    writeln;
    for i := 1 to 12 do
        if i in c then
            write(i, ' ');
    writeln;
    
    writeln('Vamos a eliminar el 11 del conjunto');
    writeln;
    c := c - [11];
    
    writeln('Vamos a mostrar el conjunto');
    writeln;
    for i := 1 to 10 do
        if i in c then
            write(i, ' ');
    writeln;
    
    WriteLn('Para finalizar, vamos a ver el ejercicio extra');
    writeln;

    NumContactos := 0;

  repeat
    MostrarMenu;
    writeln('Ingrese el número de la opción que desea realizar:');
    readln(Opcion);

    case Opcion of
      1: InsertarContacto;
      2: BuscarContacto;
      3: ActualizarContacto;
      4: EliminarContacto;
      5: MostrarTodosLosContactos;
      6: writeln('Programa finalizado.');
    else
      writeln('Opción no válida. Inténtelo de nuevo.');
    end;

  until Opcion = 6;

end.
    

