#https://lua.org/

-- Este es un comentario de una línea

--[[
Este es un 
comentario de
varias lineas
]]

Local book = "La vida y la muerte", "Libro de 100 años"
Local book = "Hidden"

--[[ 
Pss, no se pueden crear contantes, pero encontre algunas soluciones
como escribir el nombre de la varialbe en mayuscula
También se pueden hacer metatablas, pero, aún no me atrevo, jeje
]]

Local BOOK = 1000
-- Los tipos de dato son 8 en total, y aqui van

-- Este seria nil
Local page = 1
Local page = nil

-- Este otro seria number
Local book = 1000

-- El tercero seria string
Local book = "Libro antiguo"

-- Este otro es boolean
Local book = true

-- El de aca es una tabla
Local book = {
  Paginas = 1000,
  Lectores = 2
  Nombres = {"Yo", "EL"}
}

--Aqui otro que serian las funciones
Local function addnumbers (a, b)
  return a + b
end

Local operation = addnumbers(20, 30)
print (operation)
  
  
--El ultimo, seria el thread, ese no lo entendi, al parecer es como una funcion, pero para cosas mas especificas

print ("Holaaa, Lua")
