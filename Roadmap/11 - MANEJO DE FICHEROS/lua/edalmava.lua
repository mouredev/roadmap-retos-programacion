-- Nombre de usuario de GitHub
local usuario_github = "edalmava"

-- Crear el archivo con extensión .txt
local nombre_archivo = usuario_github .. ".txt"

-- Abrir el archivo en modo escritura
local archivo = io.open(nombre_archivo, "w")
print("Creando y abriendo archivo " .. nombre_archivo)

if not archivo then
    print("Error al crear el archivo.")
    return
end

print("Escribiendo información en el archivo...")
-- Escribir información en el archivo
archivo:write("Edalmava\n")
archivo:write("30\n")
archivo:write("Lua\n")

-- Cerrar el archivo
archivo:close()

-- Leer y mostrar el contenido del archivo
archivo = io.open(nombre_archivo, "r")
if not archivo then
    print("Error al abrir el archivo para lectura.")
    return
end

print("Contenido del archivo:")
for linea in archivo:lines() do
    print(linea)
end

-- Cerrar el archivo después de leerlo
archivo:close()

-- Borrar el archivo
os.remove(nombre_archivo)
print("El archivo ha sido borrado.")
