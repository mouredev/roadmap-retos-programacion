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




