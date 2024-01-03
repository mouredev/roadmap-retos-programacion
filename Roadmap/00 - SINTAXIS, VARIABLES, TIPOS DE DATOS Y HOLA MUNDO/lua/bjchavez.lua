--[[
  EJERCICIO:
  Crea un comentario en el código y coloca la URL del sitio web oficial del
  lenguaje de programación que has seleccionado.
  Representa las diferentes sintaxis que existen de crear comentariosen
  en el lenguaje (en una línea, varias...).
  Crea una variable (y una constante si el lenguaje lo soporta).
  Crea variables representando todos los tipos de datos primitivos
  del lenguaje (cadenas de texto, enteros, booleanos...).
  Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
--]]

-- Lua Language: https://www.lua.org/
local language = "Lua"

-- Comentario de una sola linea

--[[
Este es un comentario de varias lineas
--]]


-- Lua no trabaja con CONSTANTES, en su lugar define el scope de las variables en locales y globales.

local page_url = "https://www.lua.org"              -- string
local number_one = 34                               -- number
local data = { name = "Hacker", username = "diabolico", id = 666 }          -- table
local deprecated = nil                              -- nil
local programming = true                            -- boolean
local get_data = function ()                        -- function
  print(data.name .. " " .. data.username .. " " .. data.id)
end

print("Hola, " .. language .. " es cool!!")
