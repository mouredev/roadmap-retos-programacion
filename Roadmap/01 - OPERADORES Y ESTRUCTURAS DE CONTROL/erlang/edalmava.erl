% https://www.erlang.org/doc/reference_manual/expressions
% https://www.erlang.org/doc/man/lists.html

-module(edalmava).
-export([imprimir/0, operadorMatch/0, operadoresA/0, operadoresL/0]).

extra([]) ->
    ok;
extra([H | T]) ->
    io:format("~p~n", [H]), extra(T).

% Operador de Coincidencia =
operadorMatch() ->
    {A, B} = T = {answer, 42},
    io:format("{A, B} = T = {answer, 42}.~n", []),
    io:format("A: ~w~n", [A]),
    io:format("B: ~w~n", [B]),
    io:format("T: ~w~n", [T]).

operadoresA() ->
    % Aritméticos: +, -, *, / (División en punto flotante), div (división entera), rem (resto de la división entera - módulo)
    io:format("Operadores Aritméticos~n", []),
    io:format("Uso de (+, -, *, / (División de punto flotante)) -> ((12+21-3)*3/9): ~w~n", [(12+21-3)*3/9]), % Se espera como resultado 10.0 (división en punto flotante - /)
    io:format("División entera(div) -> ((12+21-3)*3 div 9]): ~w~n", [(12+21-3)*3 div 9]), % Se espera como resultado 10 (división entera - div)
    io:format("Resto de la división entera -> (6 rem 2): ~w~n", [6 rem 2]), % Se espera como resultado 0 - Resto de la división entera entre 6 y 2
    io:format("Operadores de Lista~n", []),
    io:format("Expr1 ++ Expr2 -> ([1,2,3]++[4,5]): ~w~n", [[1,2,3]++[4,5]]), % Se espera [1, 2, 3, 4, 5]
    io:format("Expr1 -- Expr2 -> ([1,2,3,2,1,2]--[2,1,2]): ~w~n", [[1,2,3,2,1,2]--[2,1,2]]). % Se espera [3, 1, 2]

operadoresL() ->
    % Lógicos: not, and, or y xor
    io:format("Operadores Lógicos~n", []),
    io:format("Not -> (not true): ~w - (not false): ~w~n", [not true, not false]),
    io:format("And ->(true and false): ~w - (true and true): ~w - (false and true): ~w - (false and false): ~w~n", 
               [true and false, true and true, false and true, false and false]),
    io:format("Or -> (true or false): ~w - (true or true): ~w - (false or true): ~w - (false or false): ~w~n", 
               [true or false, true or true, false or true, false or false]),
    io:format("Xor -> (true xor false): ~w - (true xor true): ~w - (false xor true): ~w - (false xor false): ~w~n", 
               [true xor false, true xor true, false xor true, false xor false]).

imprimir() ->
    io:format("Imprime por consola los números del 10 al 55 (incluidos) que son pares y que no son ni el 16 ni los múltiplos de 3~n", []),
    extra([X || X <- lists:seq(10, 55), 
                         (X rem 2 =:= 0) 
                         and (X =/= 16) 
                         and (X rem 3 =/= 0)]).

% erl
% 1> c(edalmava). % Compila el código
% {ok,edalmava}   % Si la compilación es exitosa
% 2> edalmava:operadorMatch(). % Para mostrar la sección correspondiente al operador de coincidencia o de match
% 3> edalmava:operadoresA().   % Para mostrar la sección de los operadores aritméticos incluyendo operaciones con listas
% 4> edalmava:operadoresL().   % Para mostrar la sección de los operadores lógicos
% 5> edalmava:imprimir().      % Para mostrar el ejercicio extra 