--[[
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
]]

local tabla = { --equivalencia a lista
    3,8,6,2,7,10,1,11
}

print("")
print("\ntabla original : " .. table.concat(tabla , ","))

-- aunque la clase table es util , solo funciona para tablas de listas no para clave y valor
-- su uso es mas recomendable para lista de numeros

table.insert(tabla , 20)
print("agregar valor a tabla : " .. table.concat(tabla , ","))

table.remove(tabla , 1)
print("eliminar valor de tabla : " .. table.concat(tabla , ","))

table.sort(tabla)
print("ordenar la tabla : ".. table.concat(tabla , ","))

tabla[1] = 5
print("actualizar valor de tabla : " .. table.concat(tabla , ",") )


local tabla2 = { -- equivalencia a Diccionarios o JSON
    Erno_rubik = "cubo3X3X3",
    Einstein = "E = MC^2",
    Euler = "e",
    Emmy_noether = "Algebra"
}

-- Para imprimir una tabla de tipo diccionario, necesitas iterar sobre sus pares clave-valor.
local function mostra_json()
    for clave, valor in pairs(tabla2) do
        print(clave .. " : " .. valor)
    end
end
print("\ntabla json original :")
mostra_json()

-- Para agregar un nuevo par clave-valor, simplemente asigna el valor a la clave
tabla2["steve_hawkings"] = "agujero negro"
print("\nDespues de agregar un nuevo par clave-valor:")
mostra_json()

-- eliminar valor de json/tabla

tabla2.Emmy_noether = nil -- nil significa nada
print("\neliminando un valor del json")
mostra_json()

-- actualización de json
tabla2.Einstein = "relatividad"
tabla2["Euler"] = "nodos"       -- esta es otra forma de cambiar el valor , y si el valor no existe lo crea
print("\nactualizacion de valores en el json")
mostra_json()

-- extra

local function busqueda(lista)
    print("Ingrese el nombre : ")
    local valor = io.read()
    return lista[valor]

end

local function insercion(lista)
    print("Ingresa el nombre del contacto a agregar : ")
    local nombre = io.read("*l")
    print("Ingresa el numero del contacto : ")
    local numero = io.read("*n")
    lista[nombre] = numero

end

local function eliminacion(lista)
    print("Ingrese el nombre del contacto a eliminar : ")
    local nombre = io.read()
    lista[nombre] = nil

end

local function actualizacion(lista)
    print("Ingrese el nombre del contacto : ")
    local valor = io.read()
    print("Ingrese el nuevo nombre del contacto  :")
    local nombre = io.read()
    print("Ingrese el nuevo numero del usuario :")
    local numero = io.read()
    lista[valor] = nil
    lista[nombre] = numero

end

local function main ()
    local agenda = {}
    while true do

        print("\nBienvenido a tu agenda de contactos que vas hacer : ")
        print("1.Agregar nuevo contacto")
        print("2.Buscar entre los contactos")
        print("3.actualizar un contacto ")
        print("4.eliminar un contacto ")
        print("5.salir de la agenda de contactos")
        print("elige conforme al indice : ")
        local opcion = io.read("*n")
        io.read()

        if opcion == 1 then
            insercion(agenda)

        elseif opcion == 2 then
            local contacto = busqueda(agenda)
            if contacto then
                print("contacto : " .. contacto)

            else
                print("contacto no existente")
            end

        elseif opcion == 3  then
            actualizacion(agenda)

        elseif opcion == 4 then
            eliminacion(agenda)

        elseif opcion == 5 then
            print("salistes de la agenda")
            break

        else
            print("opcion no disponible")

        end
    end
end

main()