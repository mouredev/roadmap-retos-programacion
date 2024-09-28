with Ada.Text_IO;

procedure Operadores is
   A, B             : constant Boolean := True;
   C, D             : constant Boolean := False;
   Numero1, Numero2 : Integer          := 5;
begin
   -- Operadores Aritmeticos
   Ada.Text_IO.Put_Line ("Suma:" & Integer'Image (Numero1 + Numero2));
   Ada.Text_IO.Put_Line ("Resta:" & Integer'Image (Numero1 - Numero2));
   Ada.Text_IO.Put_Line
     ("Multiplicacion:" & Integer'Image (Numero1 * Numero2));
   Ada.Text_IO.Put_Line
     ("Division:" & Float'Image (Float (Numero1) / Float (2)));
   Ada.Text_IO.Put_Line ("Resta_Division:" & Integer'Image (Numero1 rem 3));
   Ada.Text_IO.Put_Line ("Exponencial:" & Float'Image (Float (Numero1**2)));
   -- Cambio de signo usando + o -
   Numero2 := -Numero2;
   Ada.Text_IO.Put_Line
     ("Cambio de signo:" & Integer'Image (Numero1 + Numero2));

   -- Operadores Logicos
   if A and B then
      Ada.Text_IO.Put_Line ("A y B son True");
   else
      Ada.Text_IO.Put_Line ("A y B son False");
   end if;

   if C or D then
      Ada.Text_IO.Put_Line ("C o D son True");
   else
      Ada.Text_IO.Put_Line ("C o D son False");
   end if;

   if not C then
      Ada.Text_IO.Put_Line ("Negacion de C es True");
   else
      Ada.Text_IO.Put_Line ("Negacion de C es False");
   end if;

   if A xor C then
      Ada.Text_IO.Put_Line ("A xor C es True");
   else
      Ada.Text_IO.Put_Line ("A xor C es False");
   end if;

   -- LOOPS
   declare
      Contador : Integer := 10;
   begin
      -- Simple Loop
      loop
         Ada.Text_IO.Put_Line (Integer'Image (Contador));
         Contador := Contador - 1;
         exit when Contador = 0;
      end loop;
      -- While
      while Contador < 10 loop
         Contador := Contador + 1;
         Ada.Text_IO.Put_Line (Integer'Image (Contador));
      end loop;
   end;

   -- Ejercicio
   for J in 10 .. 55 loop
      declare
         isPar          : Boolean;
         isMultiploTres : Boolean;
      begin
         isPar          := J rem 2 = 0;
         isMultiploTres := J rem 3 = 0;
         if isPar and not (isMultiploTres or J = 16) then
            Ada.Text_IO.Put_Line ("Numero: " & Integer'Image (J));
         end if;
      end;
   end loop;
end Operadores;
