#!/bin/bash

# Crear archivo con información personal
function crear_archivo() {
    file="h4ckxel.txt"
    f=("Me llamo H4ckxel" "Mi edad es de 23 años" "Mi lenguaje de programacion favorito es Python/Bash")
    printf "%s\n" "${f[@]}" > "$file"    
    echo -e "\nEl archivo h4ckxel.txt ha sido creado\n"
}

# Leer el contenido del archivo
function leer_archivo() {
    cat "h4ckxel.txt"
}

# Borrar archivo
function borrar_archivo() { 
    if [ -e "h4ckxel.txt" ]; then
        rm "h4ckxel.txt"
        echo -e "\nEl archivo 'h4ckxel.txt' ha sido eliminado\n"
    else
        echo -e "\nEl archivo no existe\n"
    fi
}

crear_archivo
leer_archivo
borrar_archivo

# Parte extra: Gestión de ventas
store="sales.txt"

# Añadir producto
function add_product() {
    read -p "Nombre: " name 
    read -p "Cantidad vendida: " quantity
    read -p "Precio: " price
    echo "$name, $quantity, $price" >> "$store"
}

# Consultar producto
function consult_product() {
    read -p "Nombre: " name
    grep -i "^$name," "$store" || echo "Producto no encontrado"
}

# Eliminar producto
function delete_product() {
    read -p "Nombre: " name
    sed -i "/^$name,/d" "$store"
}

# Actualizar producto
function update_product() {
    delete_product
    add_product 
}

# Leer archivo completo
function read_file() {
    cat "$store"
}

# Calcular ventas por producto
function product_sales() {
    total=0
    read -p "Nombre: " name
    while IFS=, read -r prod quantity price; do
        if [[ "$prod" == "$name" ]]; then
            total=$(echo "$quantity * $price" | bc)
            echo -e "\nEl total de las ventas de $name es: $total\n"
            return
        fi
    done < "$store"
    echo "Producto no encontrado"
}

# Calcular ventas totales
function total_sales() {
    total=0
    while IFS=, read -r _ quantity price; do
        total=$(echo "$total + $quantity * $price" | bc)
    done < "$store"
    echo -e "\nEl total de las ventas es: $total\n"
}

# Salir y borrar archivo de ventas
function exit_program() {
    rm -f "$store"
    echo -e "[!] Archivo 'sales.txt' eliminado. Saliendo del programa...\n"
}

# Menú de opciones
while true; do
    echo -e "\n--- Menú de gestión de ventas ---"
    echo "1) Añadir producto"
    echo "2) Consultar producto"
    echo "3) Eliminar producto"
    echo "4) Actualizar producto"
    echo "5) Consultar archivo completo"
    echo "6) Calcular ventas por producto"
    echo "7) Calcular ventas totales"
    echo "8) Salir"
    
    read -p "Elige una opción: " option
    
    case $option in
        1) add_product ;;
        2) consult_product ;;
        3) delete_product ;;
        4) update_product ;;
        5) read_file ;;
        6) product_sales ;;
        7) total_sales ;;
        8) exit_program; break ;;
        *) echo "Opción no válida, intenta de nuevo" ;;
    esac
done
