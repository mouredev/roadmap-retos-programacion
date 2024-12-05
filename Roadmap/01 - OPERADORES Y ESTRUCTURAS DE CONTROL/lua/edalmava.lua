-- Operadores aritméticos

local x, y = 10, 5

print("Dado los valores x = 10 y y = 5")
print("Suma: x + y = " .. x + y)
print("Resta: x - y = " .. x - y)
print("Multiplicación: x * y = " .. x * y)
print("División: x / y = " .. x / y)
print("Exponenciación: x ^ y = " .. x ^ y)
print("Negación: -x = " .. -x)
print("Módulo: x % 2 = " .. x % 2)

-- Operadores relacionales

local a, b, c = 5, 10, 5
print("\nDado los valores a = 5, b = 10, c = 5")
print("Igualdad: a == c : ", a == c)
print("Negación de la igualdad: a ~= b :", a ~= b)
print("a < b = ", a < b)
print("a > b = ", a > b)
print("a <= b = ", a <= b)
print("a >= b = ", a >= b)

-- Operadores lógicos

local m, n = true, false
print("\nDado los valores m = true y n = false")
print("m and n = ", m and n)
print("m or n = ", m or n)
print("not m = ", not m)
print("not n = ", not n)

-- Estructuras de Control

print("\nUso de if")

if a < 0 then a = 0 end

if a < b then
    print(a)
else
    print(b)
end

local op = "*"
local r
if op == "+" then
    r = a + b
  elseif op == "-" then
    r = a - b
  elseif op == "*" then
    r = a*b
  elseif op == "/" then
    r = a/b
  else
    error("Operación inválida")
  end
print(r)

print("\nUso de while")

local arr = {1, 2, 3, 4, 5}
local i = 1
while arr[i] do
    print(arr[i])
    i = i + 1
end

print("\nUso de repeat")

local line
repeat
    line = io.read()
until line ~= ""
print(line)

print("\nUso de for")
for j = 10, 1, -1 do
    print(j)
end

print("\nReto Extra")
for j = 10, 55, 2 do
    if j ~= 16 and j % 3 ~= 0 then
        print(j)
    end
end
