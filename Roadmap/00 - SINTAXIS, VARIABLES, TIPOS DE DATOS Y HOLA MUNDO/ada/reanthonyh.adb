-- https://learn.adacore.com/

-- Comentario de una linea

-- Ada no tiene equivalente para comentarios de multiples lineas como /**/
-- Solo se usa varias lineas de con `--`

with Ada.Text_IO;

procedure Principal is
   -- Creacion de una variable
   Numero : Integer := 20;
   -- Creacion de una variable float CONSTANTE
   Pi : constant Float := 3.14;
   Is_True : Boolean := True;
   My_Char : Character := 'A';
   My_String : String := "Hello, Ada!";
begin
   -- Creacion de una variable en un bloque de codigo
   declare
      Alpha : Integer := 0;
   begin
      Alpha := Alpha + 1;
   end;
   -- Fin del bloque
   
   Ada.Text_IO.Put_Line ("¡Hola, Ada!");
end Principal;

