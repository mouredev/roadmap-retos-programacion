--[[
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
]]
-- Tablas
tabla = {1, 2, 3}
-- en lua solo existen tablas y strings
cadena_string = "Hola Mundo"

-- Insercion
table.insert(tabla, 4)
table.insert(tabla, 5)
print("insercion: ", table.concat(tabla, ", "))
-- actualizacion
tabla[1] = 5 -- el indice en lua comienza con el 1
print("actualizacion: ", table.concat(tabla, ", "))
-- borrar
table.remove(tabla, 2) -- eliminamos el elemento 2
print("borrar: ", table.concat(tabla, ", "))
-- ordenar
table.sort(tabla)
print("ordenar: ", table.concat(tabla, ", "))
--[[
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
]]

directorio = {}

function agregarContacto(name, pnum)
    if directorio[name] then
        print("El contacto ya existe")
    else
        directorio[name] = pnum
    end
end

function actualizarContacto(name, pnum)
    if directorio[name] then
        directorio[name] = pnum
        print("Contacto actualizado")
    else
        print("El contacto no existe")
    end
end

function eliminar_contacto(nombre)
    if directorio[nombre] then
        directorio[nombre] = nil
        print("Contacto aliminado")
    else
        print("Este contacto no existe")
    end    
end

function mostrarContacto()
    print("Directorio")
    if next(directorio) == nil then
        print("No hay contactos aun")
    else
        for name, pnum in pairs(directorio) do
            print(name.. ": ", pnum)
        end
    end
    
end

while true do
    
    print("1) AGREGAR CONTACTO")
    print("2) Actualizar contacto")
    print("3) Eliminar contacto")
    print("4) Directorio")
    print("5) Salir")

    local input = io.read()
    local opcion = tonumber(input)
    
    if opcion == 1 then
        print("Agregar contacto")
        print("Nombre: ")
        local name = io.read()
        print("Numero: ")
        local pnum = tonumber(io.read())
        agregarContacto(name, pnum)
    end
    if opcion == 2 then
        print("Actualizar contacto")
        print("Nombre")
        local name = io.read()
        print("Numero")
        local pnum = tonumber(io.read())
        actualizarContacto(name, pnum)
    end
    if opcion == 3 then
        print("Borrar contacto")
        print("Contacto a borrar")
        local name = io.read()
        eliminar_contacto(name)
    end

    if opcion == 4 then
        print("Directorio")
        mostrarContacto()
    end

    if opcion == 5 then
        break
    end
end

