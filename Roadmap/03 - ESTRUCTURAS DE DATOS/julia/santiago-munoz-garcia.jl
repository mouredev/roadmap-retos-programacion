# Estructuras de datos en Julia

# Array
array = [1, 2, 3, 4, 5]  # Definición
println("Array: ", array)
push!(array, 6)  # Inserción
println("Array después de insertar 6: ", array)
pop!(array)      # Borrado
println("Array después de borrar el último elemento: ", array)
array[2] = 10  # Actualización
println("Array después de actualizar el valor en la posición 2: ", array)
sort!(array)     # Ordenación
println("Array ordenado: ", array)

# Diccionario (Dict)
diccionario = Dict("uno" => 1, "dos" => 2, "tres" => 3) # Definición
println("\nDiccionario: ", diccionario)
diccionario["cuatro"] = 4  # Inserción
println("Diccionario después de insertar 'cuatro': ", diccionario)
diccionario["tres"] = 30  # Actualización
println("Diccionario después de actualizar el valor de 'tres': ", diccionario)
delete!(diccionario, "dos")  # Borrado
println("Diccionario después de borrar 'dos': ", diccionario)

# Conjunto (Set)
conjunto = Set([1, 2, 3])  # Definición
println("\nConjunto : ", conjunto)
push!(conjunto, 4)  # Inserción
println("Conjunto después de insertar 4: ", conjunto)
delete!(conjunto, 2)  # Borrado
println("Conjunto después de borrar 2: ", conjunto)

# Tupla (Tuple)
tupla = ("A", "B", "C")
println("\nTupla: ", tupla)

# Inserción (no es posible, pero se puede crear una nueva tupla)
nueva_tupla = (tupla..., "D")  
println("NUEVA tupla después de 'insertar' 'D': ", nueva_tupla)

# Borrado (no es posible, pero se puede crear una nueva tupla sin un elemento)
tupla_sin_B = filter(x -> x != "B", tupla)  
println("NUEVA tupla después de 'borrar' 'B': ", tupla_sin_B)

# Actualización (no es posible, pero se puede crear una nueva tupla con un elemento modificado)
tupla_actualizada = ("A", "X", "C")  
println("NUEVA tupla después de 'actualizar' 'B' a 'X': ", tupla_actualizada)


# Rango (Range)
rango = 1:10  # Definición un rango del 1 al 10
println("\nRango: ", rango)

# Convertir de rango a array
array_desde_rango = collect(rango)
println("Rango convertido a arreglo: ", array_desde_rango)

# Iterando sobre el rango
println("Iterando sobre el rango:")
for i in rango
    print("$i ")
end
println()

# Estructura (Struct)
struct Contacto
    nombre::String
    telefono::String
end
# Las estructuras (structs) son inmutables por defecto

# Agenda de contactos
agenda = Contacto[]

function validar_telefono(telefono::String)::Bool
    # Verifica que la longitud sea menor o igual a LONGITUD_MAXIMA_TLF
    LONGITUD_MAXIMA_TLF::Int = 11
    if length(telefono) > LONGITUD_MAXIMA_TLF
        return false
    end
    # Verifica que todos los caracteres sean dígitos
    for char in telefono
        if !(char >= '0' && char <= '9') 
            return false  # Si hay un carácter no numérico, retorna false
        end
    end
    return true 
end

# Función para agregar un contacto
function agregar_contacto(nombre::String, telefono::String)
    if validar_telefono(telefono)
        push!(agenda, Contacto(nombre, telefono))
        println("Contacto agregado:\nNombre: $nombre     Teléfono: $telefono")
    else
        println("Número de teléfono inválido. Contacto NO agregado.")
    end
end

# Función para buscar un contacto
function buscar_contacto(nombre::String)
    for contacto in agenda
        if contacto.nombre == nombre
            println("Contacto encontrado:\n Nombre: $(contacto.nombre)      Teléfono: $(contacto.telefono)")
            return
        end
    end
    println("Contacto no encontrado.")
end

# Función para actualizar un contacto
function actualizar_contacto(nombre::String, nuevo_telefono::String)
    for i in eachindex(agenda)
        if agenda[i].nombre == nombre
            if validar_telefono(nuevo_telefono)
                agenda[i] = Contacto(nombre, nuevo_telefono)
                println("Contacto actualizado:\nNombre: $nombre     Teléfono: $nuevo_telefono")
                return
            else
                println("Número de teléfono inválido.")
                return
            end
        end
    end
    println("Contacto no encontrado.")
end

# Función para eliminar un contacto
function eliminar_contacto(nombre::String)
    for i in eachindex(agenda)
        if agenda[i].nombre == nombre
            deleteat!(agenda, i)
            println("Contacto eliminado: $nombre")
            return
        end
    end
    println("Contacto no encontrado.")
end

# Función para mostrar todos los contactos
function mostrar_contactos()
    if isempty(agenda)
        println("Agenda vacía.")
    else
        println("\n--- Lista de Contactos ---")
        for contacto in agenda
            println("Nombre: $(contacto.nombre)     Teléfono: $(contacto.telefono)")
        end
    end
end

# Menú principal
function menu()
    while true
        println("\n--- Agenda de Contactos ---")
        println("1. Agregar contacto")
        println("2. Buscar contacto")
        println("3. Actualizar contacto")
        println("4. Eliminar contacto")
        println("5. Mostrar contactos")
        println("6. Salir")
        print("Seleccione una opción: ")
        opcion = readline()

        if opcion == "1"
            print("Ingrese el nombre: ")
            nombre = readline()
            print("Ingrese el número de teléfono: ")
            telefono = readline()
            agregar_contacto(nombre, telefono)
        elseif opcion == "2"
            print("Ingrese el nombre del contacto a buscar: ")
            nombre = readline()
            buscar_contacto(nombre)
        elseif opcion == "3"
            print("Ingrese el nombre del contacto a actualizar: ")
            nombre = readline()
            print("Ingrese el nuevo número de teléfono: ")
            nuevo_telefono = readline()
            actualizar_contacto(nombre, nuevo_telefono)
        elseif opcion == "4"
            print("Ingrese el nombre del contacto a eliminar: ")
            nombre = readline()
            eliminar_contacto(nombre)
        elseif opcion == "5"
            mostrar_contactos() 
        elseif opcion == "6"
            println("Saliendo de la agenda .....")
            break # Finalización del bucle while
        else
            println("Opción no válida. Intente de nuevo.")
        end
    end
end

# Ejecuta el menú
menu()
