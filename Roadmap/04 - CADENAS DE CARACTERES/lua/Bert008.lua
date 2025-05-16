--[[
```
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
```
]]

-- strings
local cadena = "Hola Mundo"
print(cadena)
print(string.len(cadena))
print(#cadena)

-- concatenacion
local palabra1 = "Hola"
local palabra2 = "Mundo"
print(palabra1 .. ", " .. palabra2)

-- repeticion
local repeticion = string.rep(palabra1 .." ", 5)
print(repeticion)

-- acceso a caracteres especificos
local cadena = "Mundo"
print(cadena:sub(2, 3))

-- subcadenas
local cadena = "Hola Mundo"
print(cadena:sub(1, 4))

local cadena = "Hola Mundo"
local encuentra = string.find(cadena, "Mundo")
print(encuentra) -- esto nos dice la posicion

-- conversion de mayusculas a minusculas
local cadena = "Hola Mundo"
print(string.upper(cadena))
print(string.lower(cadena))

-- remplazo (string.gsub)
local cadena = "Hola Mundo"
print(cadena:gsub("Mundo", "Lua"))

-- cadena
local cadena = "Hola, Mundo"
for i in cadena:gmatch("[^,]+") do
    print(i)
end

-- union
local cadena = {"Hola", "mundo", "Hola", "amigo"}
print(table.concat(cadena, " "))

local cadena = "Hola Mundo"
print(cadena:match("^Hola"))
print(cadena:match("Mundo$"))

-- interpolacion
local palabra1, palabra2 = "Hola", "mundo"
print(string.format("La palabra 1 es: %s, y la segunda palabra seria: %s", palabra1, palabra2))

-- extra
function analizarPalabra(palabra)
    return palabra:lower():gsub("%s+", "")
end

local function palindromo(palabra)
    palabra = analizarPalabra(palabra) 
    local longitud = #palabra

    for i = 1, math.floor(longitud / 2) do 
        if palabra:sub(i, i) ~= palabra:sub(longitud - i + 1, longitud - i + 1) then
            return false
        end
    end
    return true 
end

local function anagrama(palabra1, palabra2)
    palabra1 = analizarPalabra(palabra1)
    palabra2 = analizarPalabra(palabra2)

    if #palabra1 ~= #palabra2 then
        return false
    end

    local function contar_letras(palabra)
        local conteo = {}
        for letra in palabra:gmatch(".") do
            conteo[letra] = (conteo[letra] or 0) + 1
        end
        return conteo
    end

    local conteo1 = contar_letras(palabra1)
    local conteo2 = contar_letras(palabra2)

    for letra, cantidad in pairs(conteo1) do
        if conteo2[letra] ~= cantidad then
            return false
        end
    end

    return true
end

local function isograma(palabra)
    palabra = analizarPalabra(palabra)
    local letras_vistas = {}

    for letra in palabra:gmatch(".") do
        if letras_vistas[letra] then
            return false 
        end
        letras_vistas[letra] = true
    end
    return true
end

-- Pruebas
local word1 = "oso"
local word2 = "aibofobia"
print("¿La palabra '"..word1.."' es un palíndromo?: ", palindromo(word1))
print("¿La palabra '"..word2.."' es un palíndromo?: ", palindromo(word2))

print("\nPruebas de anagramas:")
print("roma - amor:", anagrama("roma", "amor"))     -- true
print("hola - aloh:", anagrama("hola", "aloh"))    -- true
print("lobo - bolo:", anagrama("lobo", "bolo"))    -- true
print("perro - pera:", anagrama("perro", "pera"))  -- false

print("\nPruebas de isogramas:")
print("murciélago:", isograma("murcielago"))  -- true
print("repetir:", isograma("repetir"))