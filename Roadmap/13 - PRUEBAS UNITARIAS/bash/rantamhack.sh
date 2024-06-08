#!/bin/bash

#  EJERCICIO:
#  Crea una funcion que se encargue de sumar dos numeros y retornar
#  su resultado.
#  Crea un test, utilizando las herramientas de tu lenguaje, que sea
#  capaz de determinar si esa funcion se ejecuta correctamente.


# PARA REALIZAR LOS TEST UNITARIOS CON BASHUNIT HAY QUE PASAR ESTE SCRIPT POR  EL SCRIPT BASHUNIT QUEDARIA ASI:

# ./lib/bashunit ./13-Pruebas_unitarias.sh

# bashunit - 0.11.0
# Test case 1 passed
# Test case 2 passed
# Test case 3 passed
# Test case 4 passed
# Running ./prueba.sh
# Test case 1 passed
# Test case 2 passed
# Test case 3 passed
# Test case 4 passed
#âœ“ Passed: Sum

# Tests:      1 passed, 1 total
# Assertions: 0 passed, 0 total

#  All tests passed 
#  Time taken: 344 ms


sum() {
    local num1=$1
    local num2=$2
    echo $(($num1 + $num2))
}


test_sum() {
    local result=$(sum 4 2)
    if [ $result -eq 6 ]; then
        echo "Test case 1 passed"
    else
        echo "Test case 1 failed"
    fi

    result=$(sum -4 2)
    if [ $result -eq -2 ]; then
        echo "Test case 2 passed"
    else
        echo "Test case 2 failed"
    fi

    result=$(sum 4 -2)
    if [ $result -eq 2 ]; then
        echo "Test case 3 passed"
    else
        echo "Test case 3 failed"
    fi

    result=$(sum 2,3 4,7)
    if [ $(echo "$result == 7.0" | bc -l) -eq 1 ]; then
        echo "Test case 4 passed"
    else
        echo "Test case 4 failed"
    fi
}

test_sum


# * DIFICULTAD EXTRA (opcional):
# * Crea un diccionario con las siguientes claves y valores:
# * "name": "Tu nombre"
# * "age": "Tu edad"
# * "birth_date": "Tu fecha de nacimiento"
# * "programming_languages": ["Listado de lenguajes de programacion"]
# * Crea dos test:
# * - Un primero que determine que existen todos los campos.
# * - Un segundo que determine que los datos introducidos son correctos.



#!/bin/bash

data=(
    "name=rantam"
    "age=15"
    "birth_date=15-04"
    "programming_languages=Python,Bash,Java"
)

# Test fields
for field in "name" "age" "birth_date" "programming_languages"; do
    found=false
    for item in "${data[@]}"; do
        if [[ "$item" == "$field="* ]]; then
            found=true
            echo "Field $field exists"
            break
        fi
    done
    if ! $found; then
        echo "Field $field not found"
    fi
done

# Test data types
for item in "${data[@]}"; do
    field="${item%%=*}"
    value="${item#*=}"
    case "$field" in
        "name")
            if [[ ! "$value" =~ ^[a-zA-Z]+$ ]]; then
                echo "Invalid data type for field $field"
            else
                echo "The value of the field '$field' is a string"
            fi
            ;;
        "age")
            if [[ ! "$value" =~ ^[0-9]+$ ]]; then
                echo "Invalid data type for field $field"
            else
                echo "The value of the field '$field' is a integer"
            fi
            ;;
        "birth_date")
            if [[ ! "$value" =~ ^[0-9]{2}-[0-9]{2}$ ]]; then
                echo "Invalid data type for field $field"
            else
                echo "The value of the field '$field' is a integer"
            fi
            ;;
        "programming_languages")
            if [[ ! "$value" =~ ^[a-zA-Z,]+$ ]]; then
                echo "Invalid data type for field $field"
            else
                echo "The value of the field '$field' is a string"
            fi
            ;;
        *)
            echo "Unknown field $field"
            ;;
    esac
done
