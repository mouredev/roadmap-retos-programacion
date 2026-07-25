#!/bin/bash
: '
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
'
# variables
a=5
b=2
arr=("uno" "dos" "tres")

# operadores aritmeticos
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
echo "operaciones de:" "$a" "y" "$b"
echo "suma:" "$(( a + b ))"
echo "resta:" "$(( a - b ))"
echo "multiplicacion:" "$(( a * b ))"
echo "division:" "$(( a / b ))"
echo "modulo:" "$(( a % b ))"
echo "exponencial:" "$(( a ** b ))"
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
# operadores logicos
echo "and:" "$(( a && b ))"
echo "or:"  "$(( a || b ))"
echo "not:" "$(( ! a ))"
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
# operadores de comparacion
echo "igual:"          "$(( a == b ))"
echo "distinto:"       "$(( a != b ))"
echo "menor:"          "$(( a < b ))"
echo "mayor:"          "$(( a > b ))"
echo "menor o igual:"  "$(( a <= b ))"
echo "mayor o igual:"  "$(( a >= b ))"
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
# operadores de asignacion
x=$a
echo "asignacion simple x=\$a:"          "$x"
echo "asignacion directa x=b:"          "$(( x=b ))"
echo "suma compuesta x+=b:"             "$(( x+=b ))"
echo "resta compuesta x-=b:"            "$(( x-=b ))"
echo "multiplicacion compuesta x*=b:"   "$(( x*=b ))"
echo "division compuesta x/=b:"         "$(( x/=b ))"
echo "modulo compuesto x%=b:"           "$(( x%=b ))"
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
# operadores de pertenencia
echo "archivo existe -e /etc/passwd:"     "$([ -e /etc/passwd ] && echo 1 || echo 0)"
echo "directorio existe -d /tmp:"         "$([ -d /tmp ] && echo 1 || echo 0)"
val="dos"
echo "valor en array dos:"               "$([[ " ${arr[@]} " =~ " ${val} " ]] && echo 1 || echo 0)"
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
# operadores bit a bit, me costo entender esto
echo "and bit"                     "$(( a & b ))"
echo "or bit"                      "$(( a | b ))"
echo "xor:"                        "$(( a ^ b ))"
echo "desplazamiento izq:"         "$(( a << b ))"
echo "desplazamiento der"          "$(( a >> b ))"
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
# condicionales (if)
if [[ $a -gt $b ]]; then
  echo "a mayor que b"
elif [[ $a -lt $b ]]; then
  echo "a menor que b"
else
  echo "a igual b"
fi
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
# bucles iterativos

# for en shell (for in)
for item in "${arr[@]}"; do
  echo "item: $item"
done
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

# for estilo c (for comun)
for (( i=0; i<b; i++ )); do
  echo "for en c i: $i"
done
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

# while
i=0
while [[ $i -lt 3 ]]; do
  echo "while i: $i"
  (( i++ ))
done
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

# until
i=0
until [[ $i -ge 3 ]]; do
  echo "until i: $i"
  (( i++ ))
done
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
# gestion de errores (excepciones)

#redirije el output del error para que no lo muestre
ls /ruta/que/no/existe
ls /ruta/que/no/existe 2>/dev/null

# salir si un comando falla
set -e
# atrapar cualquier error
trap 'echo "error en el script"; exit 1' ERR

