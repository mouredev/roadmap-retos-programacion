#!/usr/bin/env bash
: '
ejercicio:
- muestra ejemplos de todas las estructuras soportadas por defecto en bash
- utiliza operaciones de insercion, borrado, actualizacion y ordenacion

dificultad extra (opcional):
- agenda de contactos por terminal con busqueda, insercion, actualizacion, eliminacion
- valido telefono solo numerico y maximo 11 digitos
- menu con opcion de finalizacion
'

# estructuras de control basicas

# if-elif-else
ejemplo_if() {
  local n="$1"
  if (( n < 0 )); then
    echo "negativo"
  elif (( n == 0 )); then
    echo "cero"
  else
    echo "positivo"
  fi
}

# case
ejemplo_case() {
  local letra="$1"
  case "$letra" in
    [aeiou]) echo "vocal" ;;
    *)        echo "consonante" ;;
  esac
}

# for
ejemplo_for() {
  for i in {1..3}; do
    echo "for i: $i"
  done
}

# while
ejemplo_while() {
  local i=0
  while (( i < 3 )); do
    echo "while i: $i"
    (( i++ ))
  done
}

# until
ejemplo_until() {
  local i=0
  until (( i >= 3 )); do
    echo "until i: $i"
    (( i++ ))
  done
}

# funciones y retorno
cuadrado() {
  echo "$(( $1 * $1 ))"
}

# operaciones sobre lista (array)

lista=(3 1 4 1 5 9)

# insercion
insertar_en_lista() {
  lista+=("$1")
}

# borrado (elimina todas las ocurrencias)
borrar_de_lista() {
  local val="$1"
  local nueva=()
  for x in "${lista[@]}"; do
    [[ $x -eq $val ]] || nueva+=("$x")
  done
  lista=("${nueva[@]}")
}

# actualizacion (sustituye primer coincidencia)
actualizar_lista() {
  local old="$1" new="$2"
  for i in "${!lista[@]}"; do
    if (( lista[i] == old )); then
      lista[i]="$new"
      break
    fi
  done
}

# ordenacion
ordenar_lista() {
  IFS=$'\n' lista=($(sort -n <<<"${lista[*]}"))
  unset IFS
}

# mostrar lista
mostrar_lista() {
  echo "lista: ${lista[*]}"
}

# agenda de contactos 

declare -A contactos

validar_telefono() {
  [[ $1 =~ ^[0-9]{1,11}$ ]]
}

agregar_contacto() {
  read -r -p "nombre: " nombre
  read -r -p "telefono: " tel
  if validar_telefono "$tel"; then
    contactos["$nombre"]="$tel"
    echo "contacto agregado"
  else
    echo "telefono invalido"
  fi
}

buscar_contacto() {
  read -r -p "nombre a buscar: " nombre
  if [[ -v contactos["$nombre"] ]]; then
    echo "$nombre: ${contactos[$nombre]}"
  else
    echo "contacto no encontrado"
  fi
}

actualizar_contacto() {
  read -r -p "nombre a actualizar: " nombre
  if [[ -v contactos["$nombre"] ]]; then
    read -r -p "nuevo telefono: " tel
    if validar_telefono "$tel"; then
      contactos["$nombre"]="$tel"
      echo "contacto actualizado"
    else
      echo "telefono invalido"
    fi
  else
    echo "contacto no existe"
  fi
}

eliminar_contacto() {
  read -r -p "nombre a eliminar: " nombre
  if [[ -v contactos["$nombre"] ]]; then
    unset contactos["$nombre"]
    echo "contacto eliminado"
  else
    echo "contacto no existe"
  fi
}

listar_contactos() {
  echo "contactos ordenados:"
  for nombre in "${!contactos[@]}"; do
    echo "$nombre ${contactos[$nombre]}"
  done | sort
}

# menu principal

while true; do
  echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
  echo "menu: agregar, buscar, actualizar, eliminar, listar, salir"
  read -r -p "opcion: " opcion
  case "$opcion" in
    agregar)    agregar_contacto  ;;
    buscar)     buscar_contacto   ;;
    actualizar) actualizar_contacto ;;
    eliminar)   eliminar_contacto ;;
    listar)     listar_contactos  ;;
    salir)      echo "salir"; break ;;
    *)          echo "opcion invalida" ;;
  esac
done

echo "fin del programa"
