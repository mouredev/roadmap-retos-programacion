-- ================================================
-- Operadores en Lua
-- ================================================

-- Aritméticos
local suma = 5 + 3
local resta = 10 - 4
local multiplicacion = 2 * 6
local division = 8 / 2
local potencia = 2 ^ 3
local modulo = 10 % 3

print("Operadores Aritmeticos:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)
print("Potencia:", potencia)
print("Modulo:", modulo)

-- Comparación
print("\nOperadores de Comparacion:")
print("5 > 3:", 5 > 3) -- Mayor que
print("5 < 3:", 5 < 3) -- Menor que
print("5 == 5:", 5 == 5) -- Igual que
print("5 ~= 3:", 5 ~= 3) -- Distinto que
print("5 >= 5:", 5 >= 5) -- Mayor o igual que
print("3 <= 4:", 3 <= 4) -- Menor o igual que

-- Lógicos
local a, b = true, false
print("\nOperadores Logicos:")
print("true and false:", a and b)
print("true or false:", a or b)
print("not true:", not a)

-- Asignación (en Lua, el operador de asignación es solo `=`)
local x = 10
x = x + 5
print("\nOperador de Asignacion:")
print("x =", x)

-- Identidad (comparación de referencia para tablas)
local t1 = {1, 2}
local t2 = t1
local t3 = {1, 2}
print("\nOperador de Identidad (referencia de tablas):")
print("t1 == t2:", t1 == t2) -- true
print("t1 == t3:", t1 == t3) -- false

-- Pertenencia (no existe directamente en Lua, se simula con búsqueda en tabla)
print("\nSimulacion de Operador de Pertenencia:")
local frutas = {"manzana", "pera", "naranja"}
function contiene(tabla, valor)
  for _, v in ipairs(tabla) do
    if v == valor then return true end
  end
  return false
end
print("¿Contiene 'pera'?:", contiene(frutas, "pera"))

-- Operadores de bits (desde Lua 5.3)
print("\nOperadores de Bits:")
local bit_or = 5 | 3    -- 0101 OR 0011 = 0111 = 7
local bit_and = 5 & 3   -- 0101 AND 0011 = 0001 = 1
local bit_xor = 5 ~ 3   -- 0101 XOR 0011 = 0110 = 6
local bit_not = ~5      -- NOT 0101 = 1010 = -6 (complemento a dos)
print("5 | 3:", bit_or)
print("5 & 3:", bit_and)
print("5 ~ 3:", bit_xor)
print("~5:", bit_not)

-- ================================================
-- Estructuras de Control
-- ================================================

-- Condicional
print("\nEstructura Condicional:")
local edad = 20
if edad >= 18 then
  print("Eres mayor de edad")
elseif edad >= 13 then
  print("Eres adolescente")
else
  print("Eres menor")
end

-- Iterativa: for
print("\nEstructura Iterativa: for")
for i = 1, 5 do
  print("Iteracion:", i)
end

-- Iterativa: while
print("\nEstructura Iterativa: while")
local n = 1
while n <= 3 do
  print("n =", n)
  n = n + 1
end

-- Iterativa: repeat-until (como do-while)
print("\nEstructura Iterativa: repeat-until")
local m = 1
repeat
  print("m =", m)
  m = m + 1
until m > 3

-- Excepciones: pcall (protección de llamadas)
print("\nManejo de Excepciones con pcall:")
local function divide(a, b)
  return a / b
end

local success, result = pcall(divide, 10, 0)
if success then
  print("Resultado:", result)
else
  print("Error al dividir:", result)
end

-- ================================================
-- DIFICULTAD EXTRA
-- Números entre 10 y 55 que:
-- - Son pares
-- - No son 16
-- - No son múltiplos de 3
-- ================================================
print("\nDIFICULTAD EXTRA:")
for i = 10, 55 do
  if i % 2 == 0 and i ~= 16 and i % 3 ~= 0 then
    print(i)
  end
end
