%
%EJERCICIO:
%- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
%  Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
%  (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
%- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
%  que representen todos los tipos de estructuras de control que existan
%  en tu lenguaje:
%  Condicionales, iterativas, excepciones...
%- Debes hacer print por consola del resultado de todos los ejemplos.
%
%DIFICULTAD EXTRA:
%Crea un programa que imprima por consola todos los números comprendidos
%entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
%
%Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
%

% OPERADORES LóGICOS
% AND ,
ambos_son_0(X, Y) :-
    X =:= 0,
    Y =:= 0.
% OR ;
uno_es_0(X, Y) :-
    X =:= 0;
    Y =:= 0.
% mayor que >
mayor_que(X, Y) :- X > Y.
% menor que <
menor_que(X, Y) :- X < Y.
% mayor o igual >=
mayor_igual_que(X, Y) :- X >= Y.
% menor o igual =<
menor_igual_que(X, Y) :- X =< Y.
% igual que =:=
igual_que(X, Y) :- X =:= Y.
% diferente =\=
diferente_que(X, Y) :- X =\= Y.
% OPERADORES ARITMéTICOS
% añadir +
anadir(X, Y, R) :- R is X + Y.
% sustraer -
sustraer(X, Y, R) :- R is X - Y.
% multiplicar *
multiplicar(X, Y, R) :- R is X * Y.
% dividir /
dividir(X, Y, R) :- R is X / Y.
% potencia **
potencia(X, Y, R) :- R is X**Y.
% division entera //
division_entera(X, Y, R) :- R is X // Y.
% módulo mod
modulo(X, Y, R) :- R is X mod Y.
% negacion
no_entero(X) :- not(integer(X)).

% PERTENENCIA
% cabeza de lista
list_member(X, [X|_]).
% parte de la cola
list_member(X,[_|TAIL]) :- list_member(X, TAIL).

% ESTRUCTURAS DE CONTROL
% en prolog no hay estructuras de control, se basa en la recursion
% se simula el if-then con predicados and/or
es_par(X) :-
    (X mod 2 =:= 0 -> 
        write("es par"), nl
    ; 
        write("no es par"), nl
    ).

 main :- write("¡Hola, prolog!").