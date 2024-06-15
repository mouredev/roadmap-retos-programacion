-- Lua posee operadores Aritmeticos, Relacionales y Logicos:
-- ARITMETICOS

print('Suma: 5 + 5 = ' .. 5 + 5)
print('Resta: 10 - 5 = ' .. 10 - 5)
print('Multiplicación: 40 * 2 = ' .. 40 * 2)
print('División: 8 / 2 = ' .. 8 / 2)
print('Modulo: 15 % 3 = ' .. 15 % 3)
print('Exponente: 15 ^ 3 = ' .. 15 ^ 3)

-- RELACIONALES
-- Los operadores relacionales devuelven siempre un resultado "true" o "false"

print('Igualdad: 10 == 10', 10 == 10)
print('Desigualdad: 10 ~= 10', 10 ~= 10)
print('Es mayor que: 10 > 5', 10 > 5)
print('Es menor que: 10 < 5', 10 < 5)
print('Es mayor o igual que: 10 <= 5', 10 <= 5)
print('Es menor o igual que: 10 >= 5', 10 >= 5)

-- LOGICOS
-- Son and, or y not, como las estructuras de contol, todos los operadores logicos consideran false y nil
-- como falso y todo lo demas verdadero.

print('AND: 5 + 5 = 10 and 10 - 5 = 5 es', 5 + 5 == 10 and 10 - 5 == 5)
print('OR: 5 + 5 = 14 or 10 - 5 = 5 es', 5 + 5 == 14 and 10 - 5 == 5)
print('NOT: NOT 5 + 5 = 14 es', not (5 + 5 == 14))

-- ESTRUCTURAS DE CONTROL
mi_variable = "Estructuras de Control"

-- Condicionales
if mi_variable == "Estructuras de Control" then
    print('mi_variable es "Estructuras de Control"')
elseif mi_variable == "Estructuras" then
    print('mi_variable es "Estructuras"')
else
    print('mi_variable no es "Estructuras de Control"')
end

-- Iterativas
i = 0

for i=0,5  do
    print(i)
end

while i <= 10 do
    print(i)
    i = i + 1
end
---------------------- Ejecicio Adicional-------------------------------------
for i=10, 55 do
    if i % 2 == 0 and i ~= 16 and i % 3 ~= 0 then
        print(i)
    end
end
