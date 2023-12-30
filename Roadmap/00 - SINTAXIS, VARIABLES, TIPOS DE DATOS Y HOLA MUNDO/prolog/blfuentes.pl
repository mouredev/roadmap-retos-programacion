% https://www.swi-prolog.org/

% Esto también es para
% comentarios multi-línea

% Tipos de datos
% Data objets
% - Structures
% - Simple Objects
%   - Variables
%   - Constants
%       - Numbers
%       - Atoms

% variables en un fact
persona(blfuentes, 38, ingeniero).
% pare recuperar los valores en variables. ejecutando por ejemplo persona(X, Y, ingeniero).
% ?- persona(X, Y, ingeniero).
% X = blfuentes,
% Y = 38.

% variables en una rule
parent(uno, dos).
parent(dos, tres).
male(uno).

padre(X, Y) :- parent(X, Y), male(X).

% en prolog no hay booleanos, los facts se evalúan en éxito o fracaso
% ?- male(uno). -> devuelve true.
% ?- male(dos). -> devuelve false.

main :- write("¡Hola, prolog!").