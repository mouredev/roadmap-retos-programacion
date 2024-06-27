-module(edalmava).
-export([listas/0, tuplas/0, listasProps/0, registros/0, mapas/0, extra/0]).
-record(agenda, {nombre, telefono}).   % Estructura registro.  Se emplea esta directiva de preprocesamiento

% Listas: vectores de información heterogénea.  Erlang maneja las listas como 
%         lenguaje de alto nivel
listas() ->
    % Definición de una lista
    Lista = [1, 2, 3, 4, 5],

    % Agregar elementos a la lista
    ListaA = Lista ++ [6, 7, 8, 9, 0], % [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    % Sustraer elementos a la lista
    ListaS = ListaA -- [0],            % [1, 2, 3, 4, 5, 6, 7, 8, 9]

    % Extrayendo elementos de la cabecera dejando el resto en sublistas
    [H | T] = ListaS,

    io:format("Primer elemento: ~w~n", [H]), % Primer elemento de la lista  % 1
    io:format("Resto de la lista: ~w~n", [T]). % Resto de la lista            % [2, 3, 4, 5, 6, 7, 8, 9]

% TODO: Listas binarias
% TODO: Listas E/S

% Tuplas: tipos de datos organizativos.  A diferencia de las listas no pueden incrementar ni decrementar
%         su tamaño salvo por la redefinición completa de su estructura o el uso de funciones específicas.  
%         Se emplean para agrupar datos con un propósito específico.
tuplas() ->
    Tamano = 100,
    Tupla = {"Ruta", "Nombre", Tamano},  % Tupla que guarda la información de un fichero

    % Modificación dinámica de tuplas
    % Cambiar un elemento de una tupla
    TuplaM = erlang:setelement(1, Tupla, "/home/edalmava/archivo.erl"), % Cambiar el primer elemento
    % Agregar un elemento al final de la tupla
    TuplaA = erlang:append_element(TuplaM, {date(), time()}),           % Agregar la fecha de modificación
    TuplaA2 = erlang:append_element(TuplaA, {date(), time()}),          % Agregar la fecha de modificación
    % Eliminar un elemento de la tupla
    TuplaE = erlang:delete_element(5, TuplaA2),                         % Eliminar el último elemento

    io:format("~p~n", [TuplaE]).

% Listas de Propiedades: lista de tuplas de dos elementos: clave, valor.  Se gestiona mediante la librería
%     proplists.  Son usadas para almacenar configuraciones
data() ->
    [{path, "/"}, debug, {days, 7}].
listasProps() ->
    io:format(proplists:get_value(debug, data())).   % Obtener el valor de debug 

% Registros: son un tipo específico de tupla  que facilita el acceso a los datos individuales dentro 
% de la misma mediante un nombre y una sintaxis de acceso mucho más cómoda para el programador. 
registros() ->    
    A = #agenda{nombre="Edalmava", telefono="573100000000"},
    io:format("Nombre: "),
    io:format(A#agenda.nombre),
    io:format("~nTeléfono: "),
    io:format(A#agenda.telefono),
    A2 = {agenda, "Pedro", "573101010100"},
    io:format("~nNombre: "),
    io:format(A2#agenda.nombre),
    io:format("~nTeléfono: "),
    io:format(A2#agenda.telefono).

% Mapas: son estructuras de datos.  Cada elemento se almacena bajo un índice o clave y contiene un valor.
% El índice puede ser de cualquier tipo al igual que su contenido
mapas() ->
    % Definición de un mapa
    M = #{nombre => "Edalmava"},
    % Agregar datos a un mapa
    M2 = M#{telefono => "573100000000"},
    % Cambio sobre un índice existente
    M3 = M2#{telefono := "573150000000"},
    io:format("Nombre: "),
    io:format(maps:get(nombre, M3)),
    io:format("~nTeléfono: "),
    io:format(maps:get(telefono, M3)).

% RETO EXTRA
buscar() ->
    "",
    extra().
insertar() ->
    "",
    extra().
actualizar() ->
    "",
    extra().
eliminar() -> 
    "",
    extra().
extra() ->
    io:format("~n"),
    io:format("1. Buscar Contacto~n"),
    io:format("2. Insertar Contacto~n"),
    io:format("3. Actualizar Contacto~n"),
    io:format("4. Eliminar Contacto~n"),
    io:format("5. Salir~n"),
    Opcion = string:trim(io:get_line("Escoja una opción: "), both, "\n"),
    case Opcion of
        "1" -> buscar();
        "2" -> insertar();
        "3" -> actualizar();
        "4" -> eliminar();
        "5" -> ok;
        _   -> extra()
    end.  
