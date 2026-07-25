-- Los comentarios en Ada comienzan con dos guiones (--)
-- y se extienden hasta el final de la línea
-- El lenguaje Ada esta especificado en la norma ISO/IEC 8652:2023
-- a fecha 25-01-2025
-- Sitios oficiales de organizaciones vinculadas a su desarrollo y promoción:
-- https://www.adaic.org/
-- https://www.adacore.com/
-- https://learn.adacore.com/courses/intro-to-ada/index.html

with Ada.Text_IO; use Ada.Text_IO;

procedure Main is
   -- Los tipos de datos elementales en Ada son los punteros y los escalares
   -- Los tipos escalares se clasifican en discretos y reales
   -- Declaración de variables
   -- identificador { , identificador }: tipo [ := expresión ];   
   entero : Integer := 5;
   flotante : Float := 5.0;
   caracter : Character := 'X';
   verdadero : Boolean := True;
   
   -- Las constantes se declaran igual que las variables, pero añadiendo la palabra
   -- reservada constant
   -- identificador { , identificador } : constant [ tipo] [ := expresión ] ;
   lenguaje : Constant String := "¡Hola, Ada!";
   pi : Constant Float := 3.1416;
begin   
   Put_Line(lenguaje); --  Mostrar la cadena "¡Hola, Ada!"
end Main;
