with Ada.Text_IO; use Ada.Text_IO;

procedure Funciones_Ada is
   --  Declaracion de Funciones
   package Maths is
      function PrintTitulo return String;
      function SumaDosNumero (A, B : Integer) return Integer;
      function MultiplicacionDosNumero (A, B : Integer) return Integer;
   end Maths;

   --  Implementacion de Funciones
   package body Maths is
      function PrintTitulo return String is
        ("Matematicas Enteras y sus Funciones");

      function SumaDosNumero (A, B : Integer) return Integer is
      begin
         return A + B;
      end SumaDosNumero;

      function MultiplicacionDosNumero (A, B : Integer) return Integer is
        (A * B);
   end Maths;

   package Extra is
      function Ejercicio (A, B : String) return Integer;
   end Extra;

   package body Extra is
      function Ejercicio (A, B : String) return Integer is
         Conteo                          : Integer := 0;
         esMultiploTres, esMultiploCinco : Boolean := False;
      begin
         for I in 1 .. 100 loop
            esMultiploTres  := I rem 3 = 0;
            esMultiploCinco := I rem 5 = 0;

            if esMultiploTres and esMultiploCinco then
               Put (A);
               Put_Line (B);
            elsif esMultiploTres then
               Put_Line (A);
            elsif esMultiploCinco then
               Put_Line (B);
            else
               Put_Line (Integer'Image (I));
               Conteo := Conteo + 1;
            end if;
         end loop;
         return Conteo;
      end Ejercicio;

   end Extra;
begin
   Put_Line ("Funciones en Ada");
   Put_Line ("------------------");
   Put_Line
     ("in/out expresan los tipos de parametros que se usa en las funciones");

   --  Invocacion de Funciones
   Put_Line (Maths.PrintTitulo);
   Put_Line
     ("Suma de (5, 10): " & Integer'Image (Maths.SumaDosNumero (5, 10)));
   Put_Line
     ("Multiplicacion de 4 y 3: " &
      Integer'Image (Maths.MultiplicacionDosNumero (A => 4, B => 3)));

   Put_Line
     ("Ejercicio" &
      Integer'Image (Extra.Ejercicio (A => "Moure", B => "Dev")));

end Funciones_Ada;
