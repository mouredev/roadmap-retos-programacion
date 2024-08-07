#!/bin/bash

echo -e "\n\n=====================================Â¿QUE ES UNA EXCEPCION?=====================================\n\n"


echo -e "Al programar en Bash algunas veces podemos anticipar errores de ejecucion, incluso en un programa sintactica y\nlogicamente correcto, pueden llegar a haber errores causados por entrada de datos invalidos o inconsistencias predecibles."

echo -e "\n\n=====================================EJERCICIO=====================================\n\n"


# Explora el concepto de manejo de excepciones segun tu lenguaje.
# Fuerza un error en tu codigo, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un i­ndice no existente
# de un listado para intentar provocar un error 




function index_error() {

    my_list=(1 2 3 4) 

    if [ ${#my_list[@]} -lt 5 ]; then
        echo -e "\nEl elemento no existe en my_list"
        echo -e "\nEl estado de salida es: ${?}"
    else
        echo ${my_list[4]}
    fi
}

index_error

echo -e "\nEl programa continua"

echo -e "\n\n=====================================EJERCICIO=====================================\n\n"

function division_zero() { 

    a=10 
    b=0 

    if [ ${b} == 0 ]; then
        echo -e "\nDividir por cero no es posible"
        echo -e "\nEl estado de salida es: ${?}"
    else
        division=$(( a/b ))
        echo $division
    fi
}

division_zero

echo -e "\nEl programa continua"

echo -e "\n\n=====================================DIFICULTAD EXTRA=====================================\n\n"



# Crea una funcion que sea capaz de procesar parametros, pero que tambien
# pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# corresponderse con un tipo de excepcion creada por nosotros de manera
# personalizada, y debe ser lanzada de manera manual) en caso de error.
# Captura todas las excepciones desde el lugar donde llamas a la funcion.
# Imprime el tipo de error.
# Imprime si no se ha producido ningun error.
# Imprime que la ejecucion ha finalizado '

function process_params(){

    if [ $# -lt 3 ]; then
        echo -e "\nEl numero de elementos de la lista debe ser mayor que dos"
        #exit 1
    elif [ $2 -eq 0 ]; then
        echo -e "\nEl segundo elemento de la lista no puede ser un cero"
        #exit 1
    elif [ -z "$3" ]; then
        echo -e "\nEl tercer elemento no puede ser una cadena de texto"
        #exit 1
    else
        echo -e "\No se ha producido ningun error"
    fi

    echo $3
    echo $(($1 / $2))
    echo $(($3 + 5))
}

process_params 1 2 3 4 || echo -e "\nSe ha producido un error inesperado"

echo -e "\nEl programa continua"

echo -e "\nEl programa ha finalizado"
