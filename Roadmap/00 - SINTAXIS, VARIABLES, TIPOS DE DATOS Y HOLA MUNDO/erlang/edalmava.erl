% https://www.erlang.org/

% Comentario hasta el final de la línea

-module(edalmava).
-export([imprimir/0, imprimir/1, tiposDatos/0]).

imprimir() ->
    % Variables en Erlang
    % Comienzan por una letra Mayúscula y su valor no puede cambiar    
    Mensaje = "Hola, Erlang",
    io:format(Mensaje).
imprimir(Mensaje) ->    
    io:format(Mensaje).

% Tipos de dato en Erlang
% Un dato de cualquier tipo se denomina término
tiposDatos() ->      
    % Números
    Enteros = 5,    
    Flotantes = 5.0, % Aritmética de Punto Flotante
    % Átomos
    Atomo = nombre, % Atomos -> Es un literal, una constante con nombre que comienza por una letra minúscula
    OtroAtomo = 'Nombre',     % Comienza con Mayúscula se encierra entre comillas simples (').  Si comienza con un caracter distinto de minúscula
    % Booleanos
    % No existe el tipo booleano en Erlang.  Para denotar los valores booleanos se usan los átomos true y false   
    % Compuestos
    Tupla = {sistema, numero}, % Tuplas -> {} Son tipos de datos compuestos con un número fijo de términos
    Lista = [1, 2, 3, 4, 5], % Listas -> [] Son tipos de datos compuestos con un número variable de términos
    Cadena = "Una cadena es una forma corta de lista", % En Erlang no existe el tipo cadena.  
    Mapa = #{clave => valor}, % Mapas -> #{clave => valor} Son tipos compuestos con un número variable de asociaciones de clave => valor
    % TODO: Tipo Record     
    io:format("~w~n", [Enteros]), % Mostrar número entero
    io:format("~w~n", [Flotantes]), % Mostrar número Flotante
    io:format("Verdadero: ~w Falso: ~w ~n", [true, false]), % Mostrar átomos true y false
    io:format("~w~n", [Tupla]), % Mostrar Tupla
    io:format(maps:get(clave, Mapa)). 

% erl
% 1> c(edalmava). % Compilar el módulo edalmava
% {ok, edalmava}  % Si la compilación es exitosa 
% 2> edalmava:imprimir(). % Ejecutar la función imprimir del módulo edalmava
% Hola, Erlangok % Imprime la cadena 'Hola, Erlang'
% 3> Mensaje = '¡Bienvenido a Erlang!'.
% 4> edalmava:imprimir(Mensaje)
% ¡Bienvenido a Erlang! % Imprime la variable Mensaje