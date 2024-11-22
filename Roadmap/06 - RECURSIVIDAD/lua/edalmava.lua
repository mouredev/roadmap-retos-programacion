-- Definiendo una función recursiva
local function imprimir (n)
    print(n .. " ") 
    if n > 0 then
        imprimir(n - 1)
    end 
end

-- Definiendo la función factorial
local function fact (n)
    if n == 0 then
      return 1
    else
      return n * fact(n-1)
    end
  end
  

-- Definiendo la función Fibonacci
local function fib (n)
    if n == 0 then
        return 0
    elseif n == 1 then 
        return 1
    else 
        return fib(n - 1) + fib(n - 2)
    end
end

print("Imprimiendo los números del 100 al 0")
imprimir(100)
print("Ingresar un número: ")
local a = io.read("*number")        -- read a number
print("El factorial del número es: " .. fact(a))
print("Posición a calcular de la serie de Fibonacci: ")
local p = io.read("*number")
print("El valor es: " .. fib(p - 1))
