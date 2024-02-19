#!/bin/bash


echo -e "\n\n=====================================PILAS=====================================\n\n"


# Una pila es una colección ordenada de elementos donde la adición de un nuevo elemento y 
# la eliminación de los existentes siempre ocurren desde el mismo extremo.


stack=()

function push(){   
    stack=(1 "${stack[@]}")
    echo "${stack[@]}"
    stack=(2 "${stack[@]}")
    echo "${stack[@]}"
    stack=(3 "${stack[@]}")
    echo "${stack[@]}"
    stack=(4 "${stack[@]}")
    echo "${stack[@]}"
    stack=(5 "${stack[@]}")
    echo "${stack[@]}"
}
push

function pop(){

    unset stack[0]
    echo "${stack[@]}"
    unset stack[1]
    echo "${stack[@]}"
    unset stack[2]
    echo "${stack[@]}"
    unset stack[3]
    echo "${stack[@]}"
    unset stack[4]
    echo "${stack[@]}"
    
}
pop

echo -e "\n\n=====================================COLAS=====================================\n\n"


# Una  cola  es una colección ordenada de elementos donde la adición de nuevos elementos ocurre en un extremo 
# y la eliminación de elementos existentes ocurre en el otro extremo. Se denominan delante y detrás respectivamente.




function push2(){

    queue=("${queue[@]}" Miguel)
    echo "${queue[@]}"
    
    queue=("${queue[@]}" Jose)
    echo "${queue[@]}"
    
    queue=("${queue[@]}" Maria)
    echo "${queue[@]}"

    queue=("${queue[@]}" Mar)
    echo "${queue[@]}"

    queue=("${queue[@]}" Helena)
    echo "${queue[@]}"
}
push2

function pop2(){
    
    unset 'queue[0]'
    queue=("${queue[@]}")

}
    
pop2
echo "${queue[@]}"

pop2
echo "${queue[@]}"

pop2
echo "${queue[@]}"

pop2
echo "${queue[@]}"

pop2
echo "${queue[@]}"


echo -e "\n\n=====================================DIFICULTAD EXTRA=====================================\n\n"


# Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
# de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
# que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
# Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
# el nombre de una nueva web.


stack=("program_languages")

function python(){
    echo -e "Las paginas visitadas son: \n${stack[@]}\n"
    echo -e "\nBienvenido a la pagina de python"
    read -p "¿Que pagina quieres visitar ahora?:  siguiente / anterior: " new_page
    if [[ $new_page == "anterior" ]]; then
        stack=("${stack[@]:0:${#stack[@]}-1}")
        program_languages
    elif [[ $new_page == "siguiente" ]];then
        stack+=(javascript)
        javascript
    else
        echo -e "Has elegido una opción no disponible \n [+] Saliendo del programa ....."
        exit
    fi
}
        
function javascript(){
    echo -e "Las paginas visitadas son: \n${stack[@]}\n"
    echo -e "\nBienvenido a la pagina de javascript"
    read -p "¿Que pagina quieres visitar ahora?:  siguiente / anterior: " new_page
    if [[ $new_page == "anterior" ]]; then
        stack=("${stack[@]:0:${#stack[@]}-1}")
        python
    elif [[ $new_page == "siguiente" ]];then
        stack+=(java)
        java
    else
        echo -e "Has elegido una opción no disponible \n [+] Saliendo del programa ....."
        exit
    fi
}
        
function java(){
    echo -e "Las paginas visitadas son: \n${stack[@]}\n"
    echo -e "\nBienvenido a la pagina de java"
    read -p "¿Que pagina quieres visitar ahora?:  siguiente / anterior: " new_page
    if [[ $new_page == "anterior" ]]; then
        stack=("${stack[@]:0:${#stack[@]}-1}")
        javascript
    elif [[ $new_page == "siguiente" ]];then
        stack+=(typescript)
        typescript
    else
        echo -e "Has elegido una opción no disponible \n [+] Saliendo del programa ....."
        exit
    fi
}

function typescript(){
    echo -e "Las paginas visitadas son: \n${stack[@]}\n"
    echo -e "\nBienvenido a la pagina de typescript"
    read -p "¿Quieres volver a visitar la página anterior? si / no: " back
    if [[ $back == "si" ]]; then
        stack=("${stack[@]:0:${#stack[@]}-1}")
        java
    else
        echo "[+] Saliendo del programa ....."
        exit
    fi
}
    

function program_languages(){
    echo -e "\n${stack[@]}\n"
    echo -e "Bienvenido a la pagina principal\n Los 4 lenguajes mas usados en el roadmap del gran Mouredev son: \n 1º python\n 2º javascript\n 3º java\n 4º typescript"
    read -p "Quieres visitar la página de python?: si / no: "  languages
    
    if [[ $languages == "si" ]];then
        stack+=(python)
        python 
    elif [[ $languages == "no" ]];then
        echo "[+] Saliendo del programa ....."
    else
        echo -e "Has elegido una opción no disponible \n [+] Saliendo del programa ....."
        exit
    fi
}

program_languages


echo -e "\n\n=====================================DIFICULTAD EXTRA=====================================\n\n"
    

# Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
# impresora compartida que recibe documentos y los imprime cuando así­ se le indica.
# La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
# interpretan como nombres de documentos.


queue=()  

queue=("${queue[@]}" doc1.txt)
queue=("${queue[@]}" doc2.txt)
queue=("${queue[@]}" doc3.txt)
queue=("${queue[@]}" doc4.txt)
queue=("${queue[@]}" doc5.txt)

echo -e "\nDocumentos en cola de impresión:\n\n${queue[@]}"

function impresion(){
    echo -e "\nImprimiéndose el documento ${queue[0]}"
    queue=("${queue[@]:1}")
    
}    


function imprimir(){
    read -p "¿Quieres imprimir el primer documento de la cola de impresión?: imprimir / no imprimir: " result
    while [[ $result -eq "imprimir" ]]; do
    impresion
    echo -e "\n${queue[@]}\n"
        if [[ ${#queue[@]} -gt 0 ]];then
            read -p "¿Quieres imprimir el siguiente documento de la cola de impresión?: imprimir / no imprimir: " result
        else
            echo -e "\nNo hay documentos en la cola de impresión"
            break
        fi
    done
}

imprimir

