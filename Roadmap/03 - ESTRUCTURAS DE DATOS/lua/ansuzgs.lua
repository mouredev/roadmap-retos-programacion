-- Estructuras de datos en lua
-- Lua solo tiene un tipo de dato compuesto: las tablas

-- Definimos una tabla vacia
mi_tabla = {}

-- Le asignamos un valor a un campo
mi_tabla["nombre"] = "Juan"
mi_tabla["apellido"] = "Perez"

-- Accedemos a un campo
print(mi_tabla["nombre"])

-- Actualizamos un campo
mi_tabla["nombre"] = "Carlos"
print(mi_tabla["nombre"])

-- Otra forma de acceder a un campo
print(mi_tabla.apellido)

-- Definimos una tabla con campos
mi_tabla2 = {nombre="Maria", apellido="Gomez"}

-- Accedemos a un campo
print(mi_tabla2.nombre)

-- Definimos una tabla con campos y una tabla anidada
mi_tabla3 = {nombre="Pedro", apellido="Gonzalez", direccion = {calle="Av. Siempre Viva", numero=1234}}

-- Accedemos a un campo
print(mi_tabla3.direccion.calle)

-- Eliminamos un valor de una tabla
mi_tabla3.direccion.calle = nil
print(mi_tabla3.direccion.calle)

-- Ordenamos una tabla que contiene numeros
mi_tabla4 = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}
table.sort(mi_tabla4)
for i, v in ipairs(mi_tabla4) do
  print(i, v)
end

-- Definimos una tabla con varias personas y la Ordenamos
-- por el campo nombre 
personas = {
  {nombre="Juan", apellido="Perez"},
  {nombre="Maria", apellido="Gomez"},
  {nombre="Pedro", apellido="Gonzalez"}
}
table.sort(personas, function(a, b) return a.nombre < b.nombre end)
for i, v in ipairs(personas) do
  print(i, v.nombre, v.apellido)
end

--[[
--EXTRA
--]]

-- Agenda

agenda = {}

function agregar_contacto(nombre, telefono)
  agenda[nombre] = telefono
end

function buscar_contacto(nombre)
  return agenda[nombre]
end

function actualizar_contacto(nombre, telefono)
  agenda[nombre] = telefono
end

function eliminar_contacto(nombre)
  agenda[nombre] = nil
end

-- bucle infinito
while true do
  print("1. Agregar contacto")
  print("2. Buscar contacto")
  print("3. Actualizar contacto")
  print("4. Eliminar contacto")
  print("5. Salir")
  print("Opcion:")
  opcion = io.read("*n", "*l")
  if opcion == 1 then
    print("Nombre:")
    nombre = io.read()
    print("Telefono: ")
    telefono = io.read()
    agregar_contacto(nombre, telefono)
  elseif opcion == 2 then
    print("Nombre: ")
    nombre = io.read()
    telefono = buscar_contacto(nombre)
    if telefono then
      print("Telefono: " .. telefono)
    else
      print("No se encontro el contacto")
    end
  elseif opcion == 3 then
    print("Nombre: ")
    nombre = io.read()
    print("Telefono: ")
    telefono = io.read()
    actualizar_contacto(nombre, telefono)
  elseif opcion == 4 then
    print("Nombre: ")
    nombre = io.read()
    eliminar_contacto(nombre)
  elseif opcion == 5 then
    break
  end
end



