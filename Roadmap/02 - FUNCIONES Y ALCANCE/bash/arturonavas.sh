#!/bin/bash
: '
/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
'

# funciones basicas!!!

# sin parametros ni retorno
saludar() {
  echo "hola mundo!"
}

# con un parametro
saludar_nombre() {
  local nombre="$1"
  echo "hola $nombre"
}

# con varios parametros
sumar() {
  local a="$1"
  local b="$2"
  echo "suma:" "$(( a + b ))"
}

# con retorno
cuadrado() {
  local n="$1"
  echo "$(( n * n ))"
}

# funciones dentro de funciones , se puede declarar pero no invocar antes de declararla

externa() {
  echo "soy funcion externa"
  interna() {
    echo "soy funcion interna"
  }
  interna
}


# variables local y global

global="soy global"

variable_scope() {
  local localvar="soy local"
  echo "dentro de la funcion: $localvar"
  echo "dentro de la funcion: $global"
}

# dificultad extra

impr_num() {
  local palabra1="$1"
  local palabra2="$2"
  local contador=0

  for (( i=1; i<=100; i++ )); do
    if (( i % 3 == 0 && i % 5 == 0 )); then
      echo "$palabra1$palabra2"
    elif (( i % 3 == 0 )); then
      echo "$palabra1"
    elif (( i % 5 == 0 )); then
      echo "$palabra2"
    else
      echo "$i"
      ((contador++))
    fi
  done

  echo "veces que se imprimieron numeros: $contador"
  return $contador
}

#pruebas

echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
saludar
saludar_nombre "bash"
sumar 5 7
echo "cuadrado de 4:" "$(cuadrado 4)"
externa
variable_scope
echo "fuera de la funcion (global): $global"
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
impr_num "fizz" "buzz"
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
