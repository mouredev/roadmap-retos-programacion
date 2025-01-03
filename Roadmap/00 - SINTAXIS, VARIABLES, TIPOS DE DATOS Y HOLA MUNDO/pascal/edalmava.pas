(* Este es un comentario *)
{ Este es otro comentario }

{ Sitio de FreePascal: https://www.freepascal.org/ }

{ Los programas en Pascal siguen una estructura }

program Inicio;
uses Crt;

{ Definicion de constantes (const) }
const
    NumAlumnos = 10;
    Cadena = 'Hola, Pascal!';

{ Definicion de tipos (type) }
type
    DiasSemana = (Domingo, Lunes, Martes, Miercoles, Jueves, Viernes, Sabado); { Tipos enumerados }
    Digitos = 1..NumAlumnos;   { Tipos subrango (intervalo) }
    { Tipo registro }
    Estudiante = record
        Nombre : String[30];
        Edad   : Integer;
        Curso  : Integer
    end;

{ Declaracion de variables (var) }
var
    { Valores enteros (Integer) }
    a : Byte = 0;
    b : ShortInt = -128;
    c : Integer = -32768;
    d : Word = 65535;
    e : LongInt = 2147483647;

    { Valores Reales }
    r : Real = 1.7E38;
    s : Single = 3.4E38;
    de : Double = 1.7E100;
    ed : Extended = 1.1E400;

    { Valores logicos (Boolean) }
    falso : Boolean = false;
    verdadero : Boolean = true;

    { Tipo Caracter (Char) }
    car : Char = 'A';

    { Cadenas de caracteres }
    cadena2 : String = 'Cadena en Pascal';

{ Declaracion de procedimientos y funciones }

{ Cuerpo principal del programa }
begin
    ClrScr; { Procedimiento de la unidad Crt que borra la pantalla completa o la ventana actual }

    WriteLn(Cadena) { Enviar valores a la pantalla anadiendo caracteres de control de retorno de carro y avance de linea }
end.
