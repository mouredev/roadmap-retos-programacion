#!/bin/bash



echo -e "\n\n=======================================EJERCICIO=======================================\n\n"


#  * EJERCICIO:
#  * Explora el "Principio SOLID de Segregacion de Interfaces (Interface Segregation Principle, ISP)" 
#  * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.



# function go_to(){
#     echo "Llendo a trabajar"
# }

# function park(){
#     echo "El coche esta aparcando"
# }

# function refueling(){
#     echo "El coche esta repostando"
# }
        
# function charging_batery(){
#     echo "El coche esta cargando las baterias"
# }
        
# function gas_car_actions(){
#     go_to
#     park
#     refueling
#     charging_batery               # ESTA FUNCION NO DEBERIA APARECER AQUI
# }
    
# function electric_car_actions(){
#     go_to
#     park
#     refueling                    # ESTA FUNCION NO DEBERIA APARECER AQUI
#     charging_batery
# }

# # Ejecutar acciones vehiculos combustion
# gas_car_actions

# # Ejecutar acciones vehiculos electricos
# electric_car_actions    
    


function go_to(){
    echo "Llendo a trabajar"
}

function park(){
    echo "El coche esta aparcando"
}

# Funcion para Gas-car
function refueling(){
    echo "El coche esta repostando"
}
        
# Funcion para Electric-car
function charging_batery(){
    echo "El coche esta cargando las baterias"
}


# My gas-car
function my_gas_car_actions(){
    go_to
    park
    refueling
}
    

# My Electric-car
function my_electric_car_actions(){
    go_to
    park
    charging_batery
}



echo -e "***********************************"
# Ejecutar acciones vehiculos combustion
my_gas_car_actions


echo -e "***********************************"

# Ejecutar acciones vehiculos electricos
my_electric_car_actions    





echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"


#  * DIFICULTAD EXTRA (opcional):
#  * Crea un gestor de impresoras.
#  * Requisitos:
#  * 1. Algunas impresoras solo imprimen en blanco y negro.
#  * 2. Otras solo a color.
#  * 3. Otras son multifuncion, pueden imprimir, escanear y enviar fax.
#  * Instrucciones:
#  * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
#  * 2. Aplica el ISP a la implementacion.
#  * 3. Desarrolla un codigo que compruebe que se cumple el principio.



function standby(){
    echo -e "Printer is on standby"
}

function print_bw(){
    echo -e "Printer is printing in black and white"
}
                
function color_print(){
    echo -e "Printer is printing in color"
}
    
function scan(){
    echo -e "Multifunction printer is scannig a document"
}
        
function send_fax(){
    echo -e "Multifunction printer is faxing"
}
    
# Acciones de la impresora de blanco y negro
function my_bw_printer_standby(){
    standby
}

function my_bw_printer_print(){
    print_bw
}

# Acciones de la impresora de color
function my_color_printer_standby(){
    standby
}

function my_color_printer_print(){
    color_print
}

# Acciones de la impresora multifuncion
function my_multifunction_printer_standby(){
    standby
}

function my_multifunction_printer_print_bw(){
    print_bw
}

function my_multifunction_printer_print_color(){
    color_print
}

function my_multifunction_printer_scan(){
    scan
}

function my_multifunction_printer_send_fax(){
    send_fax
}
echo -e "****************************************************"
my_bw_printer_standby
my_bw_printer_print
echo -e "****************************************************"
my_color_printer_standby
my_color_printer_print
echo -e "****************************************************"
my_multifunction_printer_standby
my_multifunction_printer_print_bw
my_multifunction_printer_print_color
my_multifunction_printer_scan
my_multifunction_printer_send_fax
