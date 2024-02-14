#!/usr/bin/tclsh

# EJERCICIO:
# Entiende el concepto de recursividad creando una función recursiva que imprima
# números del 100 al 0.

set NUMBER 5

proc recuproc { NUM } {
		if { $NUM <= 0 } {
			return
		} else {
			puts $NUM	
			recuproc [ expr $NUM - 1 ]
		}
}
recuproc $NUMBER ; # Ejemplo de uso 

#######################
# DIFICULTAD EXTRA (opcional):
# Utiliza el concepto de recursividad para 
# - Calcular el factorial de un número concreto (la función recibe ese número).
# - Calcular el valor de un elemento concreto (según su posición) en la 
# sucesión de Fibonacci (la función recibe la posición).
########################

proc factorial { NUM } {
		if { $NUM  == 1} {
			return 1
		} else {
			return [ expr $NUM * [ factorial [ expr $NUM - 1 ] ] ]  
		}
} 
puts [ factorial $NUMBER ] ; # Ejemplo de uso 

#######################

proc fibonacci { NUM } {
	if { $NUM == 0 } {
		return 0
	} elseif { $NUM == 1} {
		return 1
	} else { 
		return [ expr [ fibonacci [ expr $NUM - 1 ] ] + [ fibonacci [ expr $NUM - 2 ] ] ]
	}
}

puts [ fibonacci  8 ] ; # Ejemplo de  uso
