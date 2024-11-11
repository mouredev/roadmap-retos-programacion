(* Para mi papá, la razón de ser quien soy.
 *
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 *)
program fduron;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils,
  System.Generics.Collections;

function MenuDeOpciones: Char;
begin
  WriteLn;
  WriteLn('**********************************');
  WriteLn('*        DIFICULTAD EXTRA        *');
  WriteLn('**********************************');
  WriteLn('1. Simular el mecanismo Adelante/Atras de un navegador web');
  WriteLn('2. Simular el mecanismo de una impresora compartida');
  WriteLn('X. Salir');

  Repeat
    Write('Selecciona una opción: ');
    ReadLn(Result);
    case Result of
      '1', '2', 'X', 'x': Exit;
    else
      WriteLn('Opción incorrecta');
    end;
  Until UpperCase(Result) = 'X';
end;

procedure SimulacionDeNavegador;
var
  PilaAtras, PilaAdelante: TStack<String>;
  Comando: String;
begin
  WriteLn;
  WriteLn('SIMULACIÓN DE NAVEGADOR WEB');
  WriteLn('  Instrucciones:');
  WriteLn('  Escribe una direccion URL para agregarla a la pila');
  WriteLn('  Escribe la palabra "adelante" para avanzar en el historial');
  WriteLn('  Escribe la palabra "atras" para regresar en el historial');
  WriteLn('  Escribe la palabra "quit" para salir de la simulación');
  WriteLn;
  PilaAtras := TStack<String>.Create;
  PilaAdelante := TStack<String>.Create;
  try
    PilaAtras.Push('home');

    while true do
    begin
      Write('Estas en "', PilaAtras.Peek, '" URL o comando: ');
      ReadLn(Comando);

      if Comando = 'atras' then
      begin
        if PilaAtras.Count = 1 then
          WriteLn('* Err - Has llegado al primer elemento del historial.')
        else
        begin
          PilaAdelante.Push(PilaAtras.Peek);
          PilaAtras.Pop;
        end;
      end
      else
      if Comando = 'adelante' then
      begin
        if PilaAdelante.Count = 0 then
          WriteLn('* Err - Has llegado al ultimo elemento del historial.')
        else
        begin
          PilaAtras.Push(PilaAdelante.Peek);
          PilaAdelante.Pop;
        end;
      end
      else
      if Comando <> 'quit' then
      begin
        PilaAtras.Push(Comando);
        PilaAdelante.Clear;
      end
      else
        Break;

    end;
  finally
    PilaAtras.Free;
    PilaAdelante.Free;
  end;
end;

procedure SimuladorDeImpresora;
var
  ColaDocumentos: TQueue<string>;
  Comando: String;
begin
  WriteLn;
  WriteLn('SIMULACIÓN DE COLA DE IMPRESIÓN');
  WriteLn('  Instrucciones:');
  WriteLn('  Escribe nombres de documentos PEj. documento1.doc para agregarlo a la lista');
  WriteLn('  Escribe la palabra "imprimir" para imprimir el elemento y eliminarlo de la lista');
  WriteLn('  Escribe la palabra "quit" para salir de la simulación');
  WriteLn;
  ColaDocumentos := TQueue<String>.Create;
  try
    while True do
    begin
      Write('Nombre del documento o "imprimir":');
      ReadLn(Comando);

      if Comando = 'imprimir' then
      begin
        if ColaDocumentos.Count = 0 then
          WriteLn('* Err - No hay documetos en la cola.')
        else
        begin
          WriteLn(' -Imprimiendo documento ', ColaDocumentos.Dequeue, '...');
          WriteLn(' -Impresión terminada.');
        end;
      end
      else
      if Comando <> 'quit' then
      begin
        ColaDocumentos.Enqueue(Comando);
        WriteLn('Documento agregado a la cola');
      end
      else
        Break;
    end;
  finally
    ColaDocumentos.Free;
  end;
end;

procedure DificultadExtra;
var
  Opcion: Char;
begin
  while True do
  begin
    Opcion := MenuDeOpciones;
    case Opcion of
      '1' : SimulacionDeNavegador;
      '2' : SimuladorDeImpresora;
      else
        break;
    end;
  end;
end;

var
  S: TStack<String>;
  Q: TQueue<String>;
begin
  S := TStack<String>.Create;
  Q := TQueue<String>.Create;
  try
    // Introducción de datos en una pila
    S.Push('Valor Uno');
    S.Push('Valor Dos');
    S.Push('Valor Tres');
    S.Push('Valor Cuatro');
    S.Push('Valor Cinco');
    S.Push('Valor Seis');
    WriteLn('Se introdujeron ', S.Count, ' elementos en la pila');
    WriteLn;

    // Introducción de datos en una pila
    Q.Enqueue('Valor Uno');
    Q.Enqueue('Valor Dos');
    Q.Enqueue('Valor Tres');
    Q.Enqueue('Valor Cuatro');
    Q.Enqueue('Valor Cinco');
    Q.Enqueue('Valor Seis');
    WriteLn('Se introdujeron ', S.Count, ' elementos en la cola');
    WriteLn;

    WriteLn('Recuperación de datos de una pila (LIFO):');
    while S.Count > 0 do
      WriteLn(S.Pop);

    WriteLn;

    WriteLn('Recuperación de datos de una cola (FIFO):');
    while Q.Count > 0 do
      WriteLn(Q.Dequeue);

  finally
    S.Free;
    Q.Free;
  end;

  DificultadExtra;

end.
