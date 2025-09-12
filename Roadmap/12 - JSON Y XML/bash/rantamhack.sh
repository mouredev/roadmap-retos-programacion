#!/bin/bash

# * IMPORTANTE: Solo debes subir el fichero de codigo como parte del ejercicio.
# * 
# * EJERCICIO:
# * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
# * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
# * - Nombre
# * - Edad
# * - Fecha de nacimiento
# * - Listado de lenguajes de programacion
# * Muestra el contenido de los archivos.
# * Borra los archivos.
#!/bin/bash


# Archivo json

    read -p "Por favor indica tu nombre: " name
    read -p "Indica tu nick de usuario: " username
    read -p "Confirma tu edad: " age
    read -p "Enumera los lenguajes de programacion que conoces: " -a languages

echo "{ 
    'user1':{
        'name':'$name'
        'username':'$username'
        'age':'$age'
        'languages':['${languages[*]}']
    }
}" > datos.json

cat datos.json      # Imprime el archivo en varias lineas

data=$(cat datos.json)       # Imprime el archivo en una soloa linea
echo $data

if [ -f datos.json ]; then
    rm datos.json
    echo -e "\n[!] El archivo datos.json se ha borrado ....\n"
else
    echo -e "\n[!] El archivo no existe ....\n"
fi


# Archivo XML

read -p "Por favor indica tu nombre: " name
read -p "Indica tu nick de usuario: " username
read -p "Confirma tu edad: " age
read -p "Enumera los lenguajes de programacion que conoces: " -a languages


echo "<name>$name</name>" > datos.xml
echo "<nick>$username</nick>" >> datos.xml
echo "<age>$age</age>" >> datos.xml
echo "<languages>[${languages[*]}]</languages>" >> datos.xml

cat datos.xml       # Escribiendo el fichero en distintas lineas

data=$(cat datos.xml)       # Escribiendo el fichero en una sola linea
echo $data

if [ -f datos.xml ]; then
    rm datos.xml
    echo -e "\n[!] El archivo datos.xml se ha borrado ....\n"
else
    echo -e "\n[!] El archivo no existe ....\n"
fi



# * DIFICULTAD EXTRA (opcional):
# * Utilizando la logica de creacion de los archivos anteriores, crea un
# * programa capaz de leer y transformar en una misma clase custom de tu 
# * lenguaje los datos almacenados en el XML y el JSON.
# * Borra los archivos.

function create_json() {

    user2='{
        "name": "Juan",
        "nick": "rantamplan",
        "age": "61",
        "languages": ["python", "bash", "java"]
    }'
    
    echo $user2 > file_json

    echo -e "\n"

    data=$(cat file_json)       
    echo $data

    if [ -f file_json ]; then
        rm file_json
        echo -e "\n[!] El archivo file_json se ha borrado ....\n"
    else
        echo -e "\n[!] El archivo no existe ....\n"
    fi
}


        
        
function create_xml() {
    
    
    echo '<?xml version="1.0" encoding="UTF-8"?>
        <file_xml>
            "<name>Jose</name" 
            "<nick>rantamplan</nick>" 
            "<age>28</age>" 
            "<languages>[java, python, bash]</languages>" 
        </file_xml>' >> file_xml

    echo -e "\n"

    cat file_xml       

    echo -e "\n"

    data=$(cat file_xml)       
    echo $data

    if [ -f file_xml ]; then
        rm file_xml
        echo -e "\n[!] El archivo file_xml se ha borrado ....\n"
    else
        echo -e "\n[!] El archivo no existe ....\n"
    fi
    
} 


create_json
create_xml


