program miguelex;

var
  x: integer;

function sumaRecursiva(n, m: integer): integer;
begin
  if m = 0 then
    sumaRecursiva := n
  else
    sumaRecursiva := 1 + sumaRecursiva(n, m - 1);
end;

function potenciaRecursiva(base, exponente: integer): integer;
begin
  if exponente = 0 then
    potenciaRecursiva := 1
  else
    potenciaRecursiva := base * potenciaRecursiva(base, exponente - 1);
end;

function factorialRecursivo(n: integer): integer;
begin
  if n = 0 then
    factorialRecursivo := 1
  else
    factorialRecursivo := n * factorialRecursivo(n - 1);
end;

function fibonacciRecursivo(n: integer): integer;
begin
  if n = 0 then
    fibonacciRecursivo := 0
  else if n = 1 then
    fibonacciRecursivo := 1
  else
    fibonacciRecursivo := fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2);
end;

function contadorRecursivo(n: integer): integer;
begin
  if n = 0 then
    contadorRecursivo := 0
  else
  begin
    write(n, ' ');
    contadorRecursivo := contadorRecursivo(n - 1);
  end;
end;

begin
  WriteLn('De 100 a 0 de forma recursiva: ',contadorRecursivo(100));
  WriteLn();

  writeln('Suma recursiva de 3 + 5: ', sumaRecursiva(3, 5));
  writeln('Potencia recursiva de 2^3: ', potenciaRecursiva(2, 3));
  writeln('Factorial recursivo de 5: ', factorialRecursivo(5));
  writeln('Fibonacci recursivo de 7: ', fibonacciRecursivo(10));
  
  writeLn('Introduce el numero del que quieres calcular el factorial: ');
  readLn(x);
  writeln('Factorial recursivo de ', x, ': ', factorialRecursivo(x));

  writeLn('Introduce el numero del que quieres calcular el fibonacci: ');
  readln(x);
  writeln('Fibonacci recursivo de ', x, ': ', fibonacciRecursivo(x));

end.