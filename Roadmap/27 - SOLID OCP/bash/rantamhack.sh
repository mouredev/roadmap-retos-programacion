#!/bin/bash

echo -e "\n\n=======================================EJERCICIO=======================================\n\n"
# * EJERCICIO:
# * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
# * y crea un ejemplo simple donde se muestre su funcionamiento
# * de forma correcta e incorrecta.

function triangle(){
    local base=$1
    local height=$2
    echo -e "scale=2; ($base * $height) / 2" | bc
}


function square(){
    local side="$1"
    echo -e "scale=2; $side ^ 2" | bc
}


function rectangle(){
    local base="$1"
    local height="$2"
    echo -e "scale=2; $base * $height" | bc
}
        

function calculate_area(){
    local shape=$1
    shift
    case $shape in
        triangle)
            triangle "$@"
            ;;
        square)
            square "$@"
            ;;
        rectangle)
            rectangle "$@"
            ;;
        *)
            "forma no reconocida"
    esac
}

echo -e "\n[+] El area del triangulo es:" "$(calculate_area triangle 7 5)"

echo -e "\n[+] El area del cuadrado es:" "$(calculate_area square 6)" 

echo -e "\n[+] El area del rectangulo es:" "$(calculate_area rectangle 8 6)" 


# SI QUEREMOS AÑADIR NUEVAS FUNCIONALIDADES SOLO AÑADIMOS LA NUEVA FUNCION Y LA AGREGAMOS AL "CASE"
# EXTENDIENDO EL CODIGO SIN MODIFICAR EL EXISTENTE


function circle(){
    local radius="$1"
    echo "scale=2; ($radius ^ 2) * 3.1416" | bc

}

function calculate_area(){
    local shape=$1
    shift
    case $shape in
        triangle)
            triangle "$@"
            ;;
        square)
            square "$@"
            ;;
        rectangle)
            rectangle "$@"
            ;;
        circle)
            circle "$@"
            ;;
        *)
            "formula no reconocida"
    esac
}


echo -e "\n[+] El area del triangulo es:" "$(calculate_area triangle 7 5)"

echo -e "\n[+] El area del cuadrado es:" "$(calculate_area square 6)" 

echo -e "\n[+] El area del rectangulo es:" "$(calculate_area rectangle 8 6)" 

echo -e "\n[+] El area del circulo es:" "$(calculate_area circle 5)"





echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"




# * DIFICULTAD EXTRA (opcional):
# * Desarrolla una calculadora que necesita realizar diversas operaciones matematicas. 
# * Requisitos:
# * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
# * Instrucciones:
# * 1. Implementa las operaciones de suma, resta, multiplicacion y division.
# * 2. Comprueba que el sistema funciona.
# * 3. Agrega una quinta operacion para calcular potencias.
# * 4. Comprueba que se cumple el OCP.

    
function sum(){
    local num1="$1"
    local num2="$2"
    echo "scale=2; $num1 + $num2" | bc
}        
    

function subtract(){
    local num1="$1"
    local num2="$2"
    echo "scale=2; $num1 - $num2" | bc
}


function multiply(){
    local num1="$1"
    local num2="$2"
    echo "scale=2; $num1 * $num2" | bc
}

        
function division(){
    local num1="$1"
    local num2="$2"
    echo "scale=2; $num1 / $num2" | bc
}
        
    
function calculator(){
    local shape="$1"
    shift
    case $shape in
        sum)
            sum "$@"
            ;;
        subtract)
            subtract "$@"
            ;;
        multiply)
            multiply "$@"
            ;;
        division)
            division "$@"
            ;;
        *)
            echo "forma no reconocida"
            ;;
    esac
}

echo -e "\n[+] El resultado de la suma es:" "$(calculator sum 9 5)"
echo -e "\n[+] El resultado de la resta es:" "$(calculator subtract 10 6)" 
echo -e "\n[+] El resultado de la multiplicacion es:" "$(calculator multiply 9 7)"
echo -e "\n[+] El resultado de la division es:" "$(calculator division 15 4)"


# AHORA VAMOS A AÑADIR LA FUNCION POTENCIA NO HAY QUE MODIFICAR EL CODIGO
# EXISTENTE SOLO ESCRIBIR LA NUEVA FUNCION Y AÑADIRLA AL "CASE"

function pow(){    
    local base="$1"
    local exponent="$2"
    echo "scale=2; $base ^ $exponent" | bc
}

function calculator(){
    local shape="$1"
    shift
    case $shape in
        sum)
            sum "$@"
            ;;
        subtract)
            subtract "$@"
            ;;
        multiply)
            multiply "$@"
            ;;
        division)
            division "$@"
            ;;
        pow)
            pow "$@"
            ;;
        *)
            echo "forma no reconocida"
            ;;
    esac 
}

echo -e "\n[+] El resultado de la suma es:" "$(calculator sum 25 16)"
echo -e "\n[+] El resultado de la resta es:" "$(calculator subtract 30 10)" 
echo -e "\n[+] El resultado de la multiplicacion es:" "$(calculator multiply 46 54)"
echo -e "\n[+] El resultado de la division es:" "$(calculator division 1523 41)"
echo -e "\n[+] El resultado de la potencia es:" "$(calculator pow 5 3)"
 
