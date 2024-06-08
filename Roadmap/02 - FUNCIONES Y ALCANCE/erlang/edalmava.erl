% La información contenida en este archivo se obtuvo del libro
% Erlang/OTP Volumen I 3a Edición de Manuel Ángel Rubio Jiménez
%
% El código de erlang se organiza en módulos y dentro de cada módulo se 
%  pueden encontrar funciones.  Un módulo se define en un fichero a través 
%  de unas instrucciones de preprocesador iniciales que permiten definir 
%  el nombre y las funciones que se quieren exportar(para emplear fuera del módulo).
%  En un módulo se pueden importar y exportar funciones.
%  La declaración export es una lista de las referencias a funciones que 
%  se deseen publicar y la declaración import es una lista de funciones que se 
%  importan desde otro módulo
%
% Las funciones en Erlang siguen la estructura:
%     function_name([Param1, [Param2, [...]]]) [guardas] ->
%         código.  
% 
% El nombre de la función debe ser un átomo válido.
% El bloque de código dentro de la función es un conjunto de expresiones
%  separadas por comas y finaliza con un punto.
% La última expresión evaluada será la responsable de dar el valor de 
%  retorno a la función.
% Las funciones de Erlang disponen de Polimorfismo y concordancia.  Así que se pueden definir
%  funciones con el mismo nombre pero con distinto número de parámetros.

-module(edalmava).
-export([imprimir/0, imprimir/1, area/2, area/3, get/1]).
% -compile([export_all]). % Para exportar todas las funciones del módulo.  No es recomendable hacer esto
-import(proplists, [get_value/2]).

% Sin parámetros
imprimir() ->
    "Hola Mundo".
% Con parámetros
imprimir(Mensaje) ->
    io:format(Mensaje).

% Se pueden tener funciones con el mismo nombre y número de parámetros pero con diferente comportamiento
area(cuadrado, Base) ->
 Base * Base;
area(circulo, Radio) ->
 math:pi() * Radio * Radio.

area(rectangulo, Base, Altura) ->
 Base * Altura;
area(triangulo, Base, Altura) ->
 Base * Altura / 2.
% Para usarlas se emplea
% edalmava:area(circulo, 10) para un círculo
% edalmava:area(cuadrado, 10) para un cuadrado
% edalmava:area(rectangulo, 10, 10) para un rectángulo
% edalmava:area(triangulo, 10, 10) para un triángulo

% Uso de funciones importadas de módulos del lenguaje
% La función data es privada no se puede invocar desde afuera
data() ->
    [{"hi", "hola"}, {"bye", "adios"}].
% La función get es pública se puede invocar desde afuera del módulo
get(Key) ->
    get_value(Key, data()). % Función get_value de la libreria o módulo proplists. En este caso se uso import (No recomendable)

% Ejemplo de uso:
% edalmava:get("hi") retorna "hola"
% edalmava:data() retorna un error 
