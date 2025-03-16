program implevacui;

//Aquí esta la url del sitio web oficial de Pascal  https://www.freepascal.org/

(*Añado tambien un comentario
multilinea*)

{Aqui va otro comentario
multilinea}


Const
  pi=3.1416;

var
  cadena: string;
  caracter: char;
  opcion: boolean;

  enterocorto: shortint; //-128...127
  entero8bits: byte; //0...255
  entero16bits: integer; //-32768...32767
  entero32bits: longint; //-2.147.483.648...2.147.483.647
  enteropositivo: word;  //0...65535
  decimal: real;


begin
   writeln('Hola! Aprendiendo con Pascal');
   readln;
end.                  