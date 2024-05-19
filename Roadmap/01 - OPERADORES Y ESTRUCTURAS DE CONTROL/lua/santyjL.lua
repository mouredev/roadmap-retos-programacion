--[[
    /*
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
 */
]]

--#region aritmetica
local suma = 5 + 5
local resta = 5 - 5
local multiplicacion = 5 * 5
local division = 5 / 5

local modulo = 10 % 7
local potencia = 5 ^ 5

print("suma : ", suma)
print("resta : ", resta)
print("multiplicacion : ", multiplicacion)
print("division : ", division)
print("modulo : ", modulo)
print("potencia : ", potencia)

--#region Logicos

-- and
local and1 = true and true -- verdadero
local and2 = true and false -- falso
local and3 = false and true -- falso
local and4 = false and false -- falso

print("and1 (true and true): ", and1)
print("and2 (true and false): ", and2)
print("and3 (false and true): ", and3)
print("and4 (false and false): ", and4)

-- or
local or1 = true or true -- verdadero
local or2 = true or false -- verdadero
local or3 = false or true -- verdadero
local or4 = false or false -- falso

print("or1 (true or true): ", or1)
print("or2 (true or false): ", or2)
print("or3 (false or true): ", or3)
print("or4 (false or false): ", or4)

-- not
local not_true = not true -- falso
local not_false = not false -- verdadero

print("not_true (not true): ", not_true)
print("not_false (not false): ", not_false)

--#region comparacion

local mayor = 5 > 6 -- falso
local menor = 5 < 6 -- verdadero
local igual = 5 == 6 -- falso
local es_diferente = 5 ~= 6 -- verdadero
local mayor_o_igual = 5 >= 6 -- falso
local menor_o_igual = 5 <= 6 -- verdadero

print("mayor (5 > 6): ", mayor)
print("menor (5 < 6): ", menor)
print("igual (5 == 6): ", igual)
print("es_diferente (5 ~= 6): ", es_diferente)
print("mayor_o_igual (5 >= 6): ", mayor_o_igual)
print("menor_o_igual (5 <= 6): ", menor_o_igual)

--#region asignacion
suma = suma + 4
resta = resta - 4
multiplicacion = multiplicacion * 4
division = division / 4
modulo = modulo % 4
potencia = potencia ^ 4

print("nueva suma : ", suma)
print("nueva resta : ", resta)
print("nueva multiplicacion : ", multiplicacion)
print("nueva division : ", division)
print("nuevo modulo : ", modulo)
print("nueva potencia : ", potencia)

--#region control de flujo

--condiciones
local edad = 14

if edad > 18 and edad < 45 then -- si entonces
    print("eres mayor de edad")

elseif edad > 45 then           -- si no si entonces
    print("ya estas consado jefe ")

else
    print("sos un pete")

end

-- bucles for
for niveles= 1 , 10 do
    print("nivel actual : " , niveles)

end

for niveles_x2 = 10 , 20 , 2 do
    print("nivel actual : " , niveles_x2)

end --end para cerrar el bucle

--bucle while
local i = 1

while i < 15 do
    print("hi hitler" , i)
    i = i + 1
end

--#region Extra

for i = 10, 55, 2 do
    if i ~= 16 and i % 3 ~= 0 then
      print(i)
    end
  end

print(55)