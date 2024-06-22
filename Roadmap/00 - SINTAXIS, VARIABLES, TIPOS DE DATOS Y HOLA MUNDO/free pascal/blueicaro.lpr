program blueicaro;
 //https://www.lazarus-ide.org/
{
 Lazarus es un entorno para programar Free Pascal.
 Free Pascal no es un lenguage obsoleto, es un una
 versión libre de Object Pascal, creado por Borland
 tras su éxito con Turbo Pascal.
 Se puede considerar una versión libre de Delphi.
}

Const
  MiConstante : string ='Free Pascal';
Var
  MiNumero : integer;
  MiCadena : string;
  MiBooleano : Boolean;
  MiChar : char;


begin
  Writeln ('!Hola, '+MiConstante+'¡');
  {
   Espera un tecla.
   En windows, si se lanza el programa desde Lazarus, la ventana se cierra
   al terminar sin dejar ver el resultado
  }
  Readln();
end.

