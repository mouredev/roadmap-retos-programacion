<?php

    // Crearcion del fichero

    $fichero = fopen("miguelex.txt", "w");

    // Escribir en el fichero

    fwrite($fichero, "Nombre: Miguel Angel\n");
    fwrite($fichero, "Edad: 48\n");
    fwrite($fichero, "Lenguaje favorito: PHP\n");

    // Cerrar el fichero

    fclose($fichero);

    // Mostrar el contenido del fichero

    echo file_get_contents("miguelex.txt");

    // Borrar el fichero

    unlink("miguelex.txt");


    // EJERCICIO EXTRA


    $fichero = fopen("ventas.txt", "w");

    fwrite($fichero, "Nombre\t\t Cantidad\t\t Precio\n");

    do {
        system('cls');
        echo "\nMenú\n";
        echo "1. Añadir venta\n";
        echo "2. Ver ventas\n";
        echo "3. Eliminar producto\n";
        echo "4. Calcular ventas totales\n";
        echo "5. Calcular ventas de un producto\n";
        echo "6. Salir\n";
        echo "Elige una opción: ";
        $option = trim(fgets(STDIN));

        switch ($option) {
            case 1:
                
                echo "Introduce el nombre del producto: ";
                $nombre = trim(fgets(STDIN));
                echo "Introduce la cantidad: ";
                $cantidad = trim(fgets(STDIN));
                echo "Introduce el precio: ";
                $precio = trim(fgets(STDIN));

                fwrite($fichero, "$nombre\t\t $cantidad\t\t $precio\n");
                break;
            case 2:
                echo file_get_contents("ventas.txt");
                break;
            case 3:
                echo "Introduce el nombre del producto a borrar: ";
                $producto_a_borrar = trim(fgets(STDIN));

                $contenido = file_get_contents("ventas.txt");

                $lineas = explode("\n", $contenido);

                foreach ($lineas as $indice => $linea) {
                    if (strpos($linea, $producto_a_borrar) !== false) {
                        unset($lineas[$indice]); 
                    }
                }

                file_put_contents("ventas.txt", implode("\n", $lineas));
                break;
            case 4:
                
                $contenido = file_get_contents("ventas.txt");
    
                
                $lineas = explode("\n", $contenido);
    
                $total = 0;
                
                foreach ($lineas as $linea) {
                    $columnas = explode("\t\t", $linea);
                    if (count($columnas) == 3) {
                        $cantidad = intval(trim($columnas[1]));
                        $precio = floatval(trim($columnas[2]));
                        $total += $cantidad * $precio;
                    }
                }
    
                echo "El total de ventas es: $total\n";
                break;
            case 5:
                echo "Introduce el nombre del producto para calcular el total de ventas: ";
                $producto_a_buscar = trim(fgets(STDIN));
            
                // Leer el contenido actual del archivo
                $contenido = file_get_contents("ventas.txt");
            
                // Separar el contenido por líneas
                $lineas = explode("\n", $contenido);
            
                $total_producto = 0;
                // Recorrer todas las líneas y calcular el total de ventas del producto indicado
                foreach ($lineas as $linea) {
                    if (strpos($linea, $producto_a_buscar) !== false) {
                        $columnas = explode("\t\t", $linea);
                        if (count($columnas) == 3) {
                            $cantidad = intval(trim($columnas[1]));
                            $precio = floatval(trim($columnas[2]));
                            $total_producto += $cantidad * $precio;
                        }
                    }
                }
            
                echo "El total de ventas para el producto $producto_a_buscar es: $total_producto\n";
                break;
            default:
                    echo "Opción no válida\n";
                    break;
        }
    } while ($option != 6); 

    unlink("ventas.txt");