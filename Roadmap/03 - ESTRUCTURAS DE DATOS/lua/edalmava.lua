-- Las estructuras de datos en Lua son las tablas

-- Matrices

local a = {}
for i = 1, 1000 do
    a[i] = 0
end

-- Puede iniciar una matriz en el índice 0, 1 o cualquier otro valor:
-- Sin embargo, es costumbre en Lua iniciar matrices con el índice 1

a = {}
for i = -5, 5 do
    a[i] = 0
end

local squares = {1, 4, 9, 16, 25, 36, 49, 64, 81}
print("Cantidad de elementos de la matriz: ", #squares)  --[[
  Si la tabla es una tabla secuencial (índices numéricos consecutivos, 
  comenzando desde 1), puedes usar el operador # para obtener el tamaño.
]]

--[[
  Si la matriz tiene índices no consecutivos o mixtos (es decir, una tabla 
  no secuencial), puedes contar los elementos manualmente.
]]
local matriz = {10, 20, [5] = 50, ["clave"] = "valor"}
local size = 0
for _ in pairs(matriz) do
    size = size + 1
end
print(size)

-- Insertar elementos
a = {}
print("Insertando elementos")
table.insert(a, "Hola")
table.insert(a, "Mundo")
table.insert(a, "Lua")
table.insert(a, 1, "#")
print("Número de elementos insertados: ", #a)

-- Borrar elementos
print("Removiendo primer elemento")
table.remove(a, 1)  -- Remueve el elemento de la posición 1
--[[
for i = 1, #a do
    print(a[i])
end
]]

print(table.concat(a, " "))
a = {5, 4, 1, 2, 3}
table.sort(a)
print("Organizando elementos: ", table.concat(a, ","))

local agenda = {}

function agregar_contacto()
    print("Nombre: ")
    local nombre = io.read()
    print("Teléfono: ")
    local telefono = io.read()
    agenda[nombre] = telefono
end

function buscar_contacto()
    print("Nombre: ")
    local nombre = io.read()
    if agenda[nombre] then
        print("Teléfono: " .. agenda[nombre])
    else
        print("No se encontro el contacto")
    end
end

function eliminar_contacto()
    print("Nombre: ")
    local nombre = io.read()
    if agenda[nombre] then 
        agenda[nombre] = nil
        print("Contacto eliminado")
    else
        print("Contacto no encontrado")
    end
end

function actualizar_contacto()
    print("Nombre: ")
    local nombre = io.read()
    if agenda[nombre] then
        print("Teléfono: ")
        local telefono = io.read()
        agenda[nombre] = telefono
        print("Contacto actualizado")
    else
        print("Contacto no encontrado")
    end
end

local function menu()
    while true do
        print("\n\nMenú Principal\n")
        print("1. Agregar nuevo contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Actualizar contacto")
        print("5. Salir")
        print("\nEscoja su opción: ")
        local opcion = io.read("n", "l")

        if opcion == 1 then
            agregar_contacto()
        elseif opcion == 2 then
            buscar_contacto()
        elseif opcion == 3 then
            eliminar_contacto()
        elseif opcion == 4 then
            actualizar_contacto()
        elseif opcion == 5 then
            break
        end
    end
end

menu()
