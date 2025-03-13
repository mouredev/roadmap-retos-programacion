--[[]
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
]]
print("Operadores Aritmeticos")
x = 10
y = 5
print("Suma (x + y) = ", x + y)
print("Resta (x - y) = ", x - y)
print("Multiplicacion (x * y) = ", x * y)
print("Divicion (x / y) = ", x / y)
print("Modulo (x % y) = ", x % y)
print("Exponente (x ^ y) = ", x ^ y)
print("Cociente (x // y) = ", x // y)

print("Operadores de comparacion")
print("Igual que (x == y): ", x == y)
print("Diferente de (x ~= y): ", x ~= y)
print("Menor que (x < y): ", x < y)
print("Mayor que (x > y): ", x > y)
print("Menor o igual que (x <= y): ", x <= y)
print("Mayor o igual que (x >= y): ", x >= y)

print("Operasores logicos")
print("And (x and y): ", x and y)
print("Or (x or y): ", x or y)
print("Not False: ", not false)

print("Operadores de concatenacion y longitud")
name = "Bert"
lastname = "008"
print(name .. lastname)
print(#lastname)

print("Estructuras de control")
print("Estructura if - else")
if x == y then
    print("son iguales")
elseif x < y then
    print("x es menor que y")
else
    print("x es mayor que")
end
print("Estructura while")
i = 0
while i <= 10 do
    print("bucle: ", i)
    i = i + 1
end
print("Estructura repeat")
i = 0
repeat
    print("bucle: ", i)
    i = i + 1
until i > 5
print("Estructura for")
for i = 1, 5 do
    print("i")
end

print("puntos extra")
for i = 10, 55, 2 do
    if i % 3 ~= 0 and i ~= 16 then
        print(i)
    end
end