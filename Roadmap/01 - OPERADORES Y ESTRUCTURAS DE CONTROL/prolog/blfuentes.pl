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
% diferente =\= (aritmético)
diferente_que(X, Y) :- X =\= Y.
% diferente \= (términos)
diferente_que_t(X, Y) :- X \= Y.
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

% BUCLES
% hay que simularlo con recursión
contar_desde_hasta(LOW, HIGH) :-
    LOW > HIGH.
contar_desde_hasta(LOW, HIGH) :-
    LOW =< HIGH,
    writeln(LOW),  
    NextLow is LOW + 1,
    contar_desde_hasta(NextLow, HIGH).

% EXCEPCIONES
% no existen, hay que simularlas con cláusulas de failure
numero_positivo(X) :-
    X > 0, !.  % success si se cumple
numero_positivo(X) :-
    atom_concat('Exception. No es positivo: ', X, ERROR),
    writeln(ERROR), nl,
    fail.     % Fallo!

% ejercicio
numero_valido(X) :-
    X mod 2 =:= 0, X =\= 16, X mod 3 =\= 0.

mostrar_pares_no16_nomultiplo3(DESDE, HASTA) :-
    DESDE > HASTA.
mostrar_pares_no16_nomultiplo3(DESDE, HASTA) :-
    DESDE =< HASTA,
    (numero_valido(DESDE) ->
        writeln(DESDE),
        NextDESDE is DESDE + 1,
        mostrar_pares_no16_nomultiplo3(NextDESDE, HASTA)
    ;
    NextDESDE is DESDE + 1,
    mostrar_pares_no16_nomultiplo3(NextDESDE, HASTA)).

% otra forma de hacerlo simplificado
mostrar_pares_no16_nomultiplo3_simplificado(DESDE, HASTA, NUM) :-
    between(DESDE, HASTA, NUM),
    NUM mod 2 =:= 0, NUM \= 16, NUM mod 3 =\= 0.
% ejecutar con 
% forall(mostrar_pares_no16_nomultiplo3_simplificado(10, 55, Number), writeln(Number)).

 main :- write("¡OPERADORES Y ESTRUCTURAS DE CONTROL!").