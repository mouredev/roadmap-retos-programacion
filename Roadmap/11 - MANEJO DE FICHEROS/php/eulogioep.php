<?php
// Constantes para los nombres de archivo
define('FILENAME', 'info_personal.txt');
define('SALES_FILENAME', 'ventas.txt');

// Función principal
function main() {
    crearArchivoPersonal();
    gestionVentas();
}

// Función para crear y manipular el archivo personal
function crearArchivoPersonal() {
    // Crear y escribir en el archivo
    $content = "Nombre: Juan\nEdad: 30\nLenguaje de programación favorito: PHP";
    file_put_contents(FILENAME, $content);
    echo "Archivo creado y escrito con éxito.\n";

    // Leer y mostrar el contenido
    $contenido = file_get_contents(FILENAME);
    echo "Contenido del archivo:\n$contenido\n";

    // Borrar el archivo
    unlink(FILENAME);
    echo "Archivo borrado con éxito.\n";
}

// Función para la gestión de ventas
function gestionVentas() {
    $salir = false;

    while (!$salir) {
        echo "\n--- Gestión de Ventas ---\n";
        echo "1. Añadir producto\n";
        echo "2. Consultar productos\n";
        echo "3. Actualizar producto\n";
        echo "4. Eliminar producto\n";
        echo "5. Calcular venta total\n";
        echo "6. Calcular venta por producto\n";
        echo "7. Salir\n";

        $opcion = readline("Seleccione una opción: ");

        switch ($opcion) {
            case '1':
                anadirProducto();
                break;
            case '2':
                consultarProductos();
                break;
            case '3':
                actualizarProducto();
                break;
            case '4':
                eliminarProducto();
                break;
            case '5':
                calcularVentaTotal();
                break;
            case '6':
                calcularVentaPorProducto();
                break;
            case '7':
                $salir = true;
                borrarArchivoVentas();
                break;
            default:
                echo "Opción no válida.\n";
        }
    }
}

// Función para añadir un producto
function anadirProducto() {
    $nombre = readline("Nombre del producto: ");
    $cantidad = readline("Cantidad vendida: ");
    $precio = readline("Precio: ");

    $linea = "$nombre, $cantidad, $precio\n";
    file_put_contents(SALES_FILENAME, $linea, FILE_APPEND);
    echo "Producto añadido con éxito.\n";
}

// Función para consultar productos
function consultarProductos() {
    if (file_exists(SALES_FILENAME)) {
        $contenido = file_get_contents(SALES_FILENAME);
        echo "\nProductos:\n$contenido";
    } else {
        echo "No hay productos registrados.\n";
    }
}

// Función para actualizar un producto
function actualizarProducto() {
    $nombreActualizar = readline("Nombre del producto a actualizar: ");
    $nuevaCantidad = readline("Nueva cantidad vendida: ");
    $nuevoPrecio = readline("Nuevo precio: ");

    $contenido = file(SALES_FILENAME);
    $encontrado = false;

    foreach ($contenido as $key => $linea) {
        $datos = explode(', ', $linea);
        if (trim($datos[0]) === $nombreActualizar) {
            $contenido[$key] = "$nombreActualizar, $nuevaCantidad, $nuevoPrecio\n";
            $encontrado = true;
            break;
        }
    }

    if ($encontrado) {
        file_put_contents(SALES_FILENAME, implode('', $contenido));
        echo "Producto actualizado con éxito.\n";
    } else {
        echo "Producto no encontrado.\n";
    }
}

// Función para eliminar un producto
function eliminarProducto() {
    $nombreEliminar = readline("Nombre del producto a eliminar: ");

    $contenido = file(SALES_FILENAME);
    $encontrado = false;

    foreach ($contenido as $key => $linea) {
        $datos = explode(', ', $linea);
        if (trim($datos[0]) === $nombreEliminar) {
            unset($contenido[$key]);
            $encontrado = true;
            break;
        }
    }

    if ($encontrado) {
        file_put_contents(SALES_FILENAME, implode('', $contenido));
        echo "Producto eliminado con éxito.\n";
    } else {
        echo "Producto no encontrado.\n";
    }
}

// Función para calcular la venta total
function calcularVentaTotal() {
    $ventaTotal = 0;

    if (file_exists(SALES_FILENAME)) {
        $contenido = file(SALES_FILENAME);

        foreach ($contenido as $linea) {
            $datos = explode(', ', $linea);
            if (count($datos) === 3) {
                $ventaTotal += floatval($datos[1]) * floatval($datos[2]);
            }
        }

        echo "Venta total: " . number_format($ventaTotal, 2) . "\n";
    } else {
        echo "No hay ventas registradas.\n";
    }
}

// Función para calcular la venta por producto
function calcularVentaPorProducto() {
    $nombreProducto = readline("Nombre del producto: ");
    $encontrado = false;

    if (file_exists(SALES_FILENAME)) {
        $contenido = file(SALES_FILENAME);

        foreach ($contenido as $linea) {
            $datos = explode(', ', $linea);
            if (trim($datos[0]) === $nombreProducto) {
                $ventaProducto = floatval($datos[1]) * floatval($datos[2]);
                echo "Venta de $nombreProducto: " . number_format($ventaProducto, 2) . "\n";
                $encontrado = true;
                break;
            }
        }

        if (!$encontrado) {
            echo "Producto no encontrado.\n";
        }
    } else {
        echo "No hay ventas registradas.\n";
    }
}

// Función para borrar el archivo de ventas
function borrarArchivoVentas() {
    if (file_exists(SALES_FILENAME)) {
        unlink(SALES_FILENAME);
        echo "Archivo de ventas borrado con éxito.\n";
    } else {
        echo "El archivo de ventas no existe.\n";
    }
}

// Ejecutar el programa principal
main();
?>