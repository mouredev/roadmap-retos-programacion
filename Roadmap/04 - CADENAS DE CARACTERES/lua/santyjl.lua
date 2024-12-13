-- 04 CADENAS DE CARACTERES
-- Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

-- Ejercicio

--[[
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
]]

local cadena_de_texto = "hola mundo"
local cadena_de_texto2 = "hola npc"

-- 1. Longitud de la cadena
print("Longitud de cadena_de_texto:" .. string.len(cadena_de_texto))

-- 2. Concatenación de cadenas
print("Concatenacion:", cadena_de_texto .. "--" .. cadena_de_texto2)

-- 3. Acceso a un carácter específico
-- En Lua, no puedes acceder directamente por índice, pero puedes usar string.sub
print("Primer caracter:" .. string.sub(cadena_de_texto, 1, 1))

-- 4. Subcadenas
print("Subcadena:" .. string.sub(cadena_de_texto, 6, 10)) -- Extrae "mundo"

-- 5. Repetición de la cadena
print("Repeticion:" .. string.rep(cadena_de_texto, 2)) -- Repite "hola mundo" dos veces

-- 6. Conversión a mayúsculas y minúsculas
print("Mayusculas:" .. string.upper(cadena_de_texto))
print("Minusculas:" .. string.lower(cadena_de_texto2))

-- 7. Reemplazo de subcadenas
print("Reemplazo de 'mundo' por 'npc':" .. string.gsub(cadena_de_texto, "mundo", "npc"))

-- 8. División de cadenas (No hay una función directa en Lua, pero puedes usar patrones)
local palabras = {}
for palabra in string.gmatch(cadena_de_texto, "%w+") do
    table.insert(palabras, palabra)
end
print("Division:" .. table.concat(palabras, ", "))

-- 9. Verificación de la existencia de una subcadena
print("Contiene 'mundo':", string.find(cadena_de_texto, "mundo") ~= nil)

-- 10. Interpolación (usando concatenación o string.format)
local nombre = "Santiago"
print(string.format("Hola, %s!" , nombre))

-- extra

local function palindromo (texto)
    local texto_volteado = string.reverse(texto)
    if texto == texto_volteado then
        return true

    else
        return false
    end
end


local function Isogramas (texto)
    local letras = {}

    for i=1 , #texto do  --esto es un bucle for lo que hace es recorrer cada elemento del texto
        local letra = string.sub(texto , i , i)

        if letras[letra] then
            return false
        else
            letras[letra] = letra
        end
    end

    return true
end

print("============================")

print("\npalindromos : ")
print("hola mundo : " , palindromo("hola mundo"))
print("sol : " , palindromo("sol"))
print("oso : " , palindromo("oso"))

print("\nIsogramas : ")
print("amateur : " , Isogramas("amateur"))
print("jose : " , Isogramas("jose"))
print("papa : " , Isogramas("papa"))
print("brais moure : " , Isogramas("brais moure"))