-module(edalmava).
-export([imprimir/1, factorial/1, fibonacci/1]).

imprimir(Num) -> imprimir(Num, 0).

imprimir(0, Result) -> Result; 
imprimir(Num, Result) ->
    io:format("~w~n", [Num]),
    imprimir(Num - 1, Result).

factorial(N) -> factorial(N, 1).

factorial(0, Result) -> Result;
factorial(N, Result) -> factorial(N - 1, Result * N).

fibonacci(N) -> fibonacci(N, 0, 1).

fibonacci(0, Result, _Next) -> Result;
fibonacci(N, Result, Next) -> fibonacci(N - 1, Next, Result + Next).
