-- Este es un comentario de una sola línea

--[[
Este es un comentario
de múltiples líneas.
]]

-- Sitio oficial: https://www.lua.org/

-- Lua es un lenguaje tipado dinámicamente.  Por defecto, todas las variables en Lua son globales.

-- Declaración de variables
lenguaje = "Lua"            -- variable global
mensaje = "¡Hola, "         -- variable global
local z                     -- Si no se asigna un valor inicial, el valor es nil
local a, b, c = 1, 2, 3     -- Asignación múltiple

-- Tipos básicos en Lua

local sinValor = nil        -- Nil: Representa la ausencia de un valor. 
local esVerdadero = true    -- Booleano verdadero
local esFalso = false       -- Booleano falso
local entero = 42           -- Número entero
local decimal = 3.14        -- Número decimal
local saludo = "Hola"       -- Cadena con comillas dobles
local mundo = 'Mundo'     -- Cadena con comilla sencilla
-- Tipos tablas que pueden usarse para crear arrays, listas, diccionarios
local tabla = {1, 2, 3, "cuatro", "cinco"}
local diccionario = {nombre = "Juan", edad = 30}

--[[
    Las funciones se tratan como valores de primera clase, lo que significa que puedes 
    almacenarlas en variables, pasarlas como argumentos y retornarlas desde otras funciones.
]]
local function saludar()
    return mensaje
end

print(saludar() .. lenguaje .. " :)!")
