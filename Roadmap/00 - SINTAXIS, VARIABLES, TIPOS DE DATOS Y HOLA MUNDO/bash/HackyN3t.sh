#!/bin/bash

# Página oficial de referencia de Bash:
# https://www.gnu.org/software/bash/manual/

# Esto es un comentario en Bash (línea única).

# En Bash no existen comentarios multilínea nativos.
# Sin embargo, se puede simular un bloque ignorado usando un *heredoc*:

: <<'COMENTARIO'
Este bloque no será ejecutado por Bash.
Aunque no es un comentario real, funciona como tal.
Es útil para descripciones largas o documentación temporal.
¡¡¡NO RECOMENDADO!!! PUEDE EJECUTAR COMANDOS EN ALGUNAS SITUACIONES, POR LO TANTO, NO ES SEGURO.
COMENTARIO

# Variables
# Las variables no pueden comenzar con un número y no pueden contener espacios.


# En Bash, las variables no son tipadas.
# Es decir, no se define el tipo de dato al declarar una variable.
# Todo se trata internamente como texto (strings), aunque Bash puede operar con enteros si se requiere.

# Ejemplos de variables sin tipo:

x=42 			# Número (entero)
y="Hola Mundo!" # Cadena (string)


# Bash trata ambas como texto, a menos que se usen en contextos aritméticos:

echo $x			# Muestra: 42

echo $y			# Muestra: "Hola Mundo!"


# Si la Variable x se utiliza en un contexto aritmetico se interpreta como entero:

echo $((x+1)) 	# Muestra:43

# En Bash no existen constantes verdaderas.
# Sin embargo, se pueden simular usando Variables readonly o convenciones de nomenclatura.

# Ejemplo de Variable readonly

PI=3.1415
readonly PI 	# Ahora PI no se puede modificar.
echo "$PI"

PI=3.0  		# Error: bash: PI: readonly variable.

#Las constantes por convención tienen el nombre en mayúsculas.


#Las Variables en Bash pueden almacenar los resultados de ejecuciones de comandos.

resultadols=`ls`
resultadols2=$(ls -la)

echo "$resultadols"
echo "$resultadols2"
