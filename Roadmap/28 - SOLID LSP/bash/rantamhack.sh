#!/bin/bash

echo -e "\n\n=======================================EJERCICIO=======================================\n\n"


# * EJERCICIO:
# * Explora el "Principio SOLID de Sustitucion de Liskov (Liskov Substitution Principle, LSP)" 
# * y crea un ejemplo simple donde se muestre su funcionamiento
# * de forma correcta e incorrecta.


# FORMA INCORRECTA LSP

    
function bird_have_beak(){
    echo -e "\n\tSoy un $1, soy un pajaro y mi boca es un pico" 
}      

function bird_fly(){
    echo -e  "\n\tSoy un $1, soy un pajaro y vuelo\n"
}

function  hawk_have_beak(){
    bird_have_beak "$1"
}

function hawk_fly(){
    bird_fly "$1"
}

function penguin_have_beak(){
    bird_have_beak "$1"
}

function penguin_fly(){
    echo -e "\n\tSoy un pingüino, soy un pajaro y nado, no vuelo\n"
    return 1
}


echo "Hawk:"
hawk_have_beak halcon
hawk_fly halcon

echo "Penguin"
penguin_have_beak pingüino
penguin_fly pingüino


# FORMA CORRECTA LSP

function bird_have_beak(){
    echo -e "\n\tSoy un $1, soy un pajaro y mi boca es un pico" 
}      

function flying_bird_have_beak(){
    bird_have_beak "$1"
}

function flying_bird_fly(){
    echo -e "\n\tSoy un $1, soy un pajaro y vuelo\n"
}

function  hawk_have_beak(){
    flying_bird_have_beak "$1"
}

function hawk_fly(){
    flying_bird_fly "$1"
}

function non_flying_bird_have_beak(){
    bird_have_beak "$1"
}

function penguin_have_beak(){
    non_flying_bird_have_beak "$1"
}

function penguin_swim(){
     echo -e "\n\tSoy un $1, soy un pajaro y nado, no vuelo\n"
}



echo "Hawk"
hawk_have_beak halcon
hawk_fly halcon

echo "Penguin"
penguin_have_beak pingüino
penguin_swim pingüino




echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"



# * DIFICULTAD EXTRA (opcional):
# * Crea una jerarquia de vehiculos. Todos ellos deben poder acelerar y frenar, asi como
# * cumplir el LSP.
# * Instrucciones:
# * 1. Crea la clase Vehiculo.
# * 2. Añade tres subclases de Vehiculo.
# * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
# * 4. Desarrolla un codigo que compruebe que se cumple el LSP.


function vehicle_init(){
    local name=$1
    echo $1
}
function vehicle_accelerate(){
    pass
}
    
function vehicle_brake(){
    pass
}
    
function engine_vehicle(){
    local name=$1
    echo -e "$1 es un vehi­culo de motor"
}   
    
    
function engine_vehicle_brake(){
    local name=$1
    echo -e "$1 esta frenando con los discos de freno"
}

function electric_motor_accelerate(){
    local name=$1
    echo -e "$1 está acelerando con el motor electrico"
}

function gas_motor_accelerate(){
    local name=$1
    echo -e "$1 está acelerando con el motor de gasoil"
}

function non_engine_vehicle(){
    local name=$1
    echo -e "$1 es un vehiculo sin motor"
}

function non_engine_accelerate(){
    local name=$1
    echo -e "$1 está acelerando con los pedales"
}

function non_engine_brake(){
    local name=$1
    echo -e "$1 está frenando con las zapatas"
}

camion_name=$(vehicle_init "camion")
engine_vehicle $camion_name
gas_motor_accelerate $camion_name
engine_vehicle_brake $camion_name

coche_name=$(vehicle_init "coche")
engine_vehicle $coche_name
electric_motor_accelerate $coche_name
engine_vehicle_brake $coche_name

bici_name=$(vehicle_init "bicicleta")
non_engine_vehicle $bici_name
non_engine_accelerate $bici_name
non_engine_brake $bici_name
