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
]]
-- https://www.lua.org/
-- Este es un comentario en Lua
--[[
Y este es un comentario de varias lineas.
Es importante no separar -- de [[ (siendo --[[ la syntaxis crrecta).
]]
valor_nulo = nil
entero = 10
local entero_local = 10
decimal = 3.1416
hex = 0xff
cadena = "Hola"
cadena_larga = [["Hola
Mundo"]]
booleanos = true
function hola()
  print("Hola")
end

hola()

print("Hola, Lua")
