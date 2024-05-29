-- www.lua.org

-- Esto es un comentario en una linea

--[[Esta es la
manera de hacer
un comentario en varias
lineas]]

--[[En LUA solo existen variables, mas no constantes, y las mismas pueden ser de tipo globales o locales
usadas dentro de funciones.]]

-- TIPOS DE VALORES QUE PUEDEN USAR ALMACENAR LAS VARIABLES

a = nil -- Nulo, ausencia de valor
b = true -- booleano, pueden ser true o false (verdadero o falso)
c = 120 -- number (numericos)
d = "Cadena" -- String o cadena de texto de hasta 8 bist

local e = function(args)
    print("Funcion: ", args)
end

e = {2,"Hola" , 4,5} -- tabla que almacena valores

print("¡Hola Lua!")