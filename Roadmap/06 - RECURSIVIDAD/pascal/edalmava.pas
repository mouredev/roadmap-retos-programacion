program Recursividad;
uses Crt;

procedure mostrarNumeros(num : Integer);
begin
    if num >= 0 then
    begin
        WriteLn(num);
        mostrarNumeros(num - 1);
    end;
end;

function factorial(num : Integer): QWord;
begin
    if num = 1 then
        factorial := 1
    else
        factorial := num * factorial(num - 1);
end;

function fibonacci(num : Integer): QWord;
begin
    if num = 0 then
        fibonacci := 0
    else if num = 1 then
        fibonacci := 1
    else
        fibonacci := fibonacci(num - 1) + fibonacci(num - 2);
end;

begin
    ClrScr;
    mostrarNumeros(100);
    WriteLn('Factorial de 6 = ', factorial(6));
    WriteLn('Posicion 8 de la serie de Fibonacci = ', fibonacci(8));
end.
