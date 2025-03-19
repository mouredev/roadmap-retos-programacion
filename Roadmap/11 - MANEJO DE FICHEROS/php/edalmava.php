<?php    
    function reto11($archivo, $nombre, $edad, $lenguaje) {
        echo "Creando archivo edalmava.txt\n\n";

        file_put_contents($archivo, $nombre, FILE_APPEND);
        file_put_contents($archivo, $edad, FILE_APPEND);
        file_put_contents($archivo, $lenguaje, FILE_APPEND);

        $cadena_archivo = file_get_contents($archivo);

        echo "Contenido del archivo edalmava.txt: \n";
        echo $cadena_archivo;

        echo "\n\nEliminando el archivo edalmava.txt";
        unlink($archivo);
    }

    function agregar_producto($archivo) {
        echo "Nombre del Producto: ";
        fscanf(STDIN, "%s\n", $nombre_producto);
        echo "Cantidad Vendida: ";
        fscanf(STDIN, "%d\n", $cantidad_vendida);
        echo "Precio: ";
        fscanf(STDIN, "%f\n", $precio);

        $linea = "$nombre_producto, $cantidad_vendida, $precio\n";

        file_put_contents($archivo, $linea, FILE_APPEND);
    }

    function consultar_producto($archivo) {        
        $gestor = @fopen($archivo, "r");
        if ($gestor) {
            echo "Nombre del Producto: ";
            fscanf(STDIN, "%s\n", $nombre_producto);
            $encontrado = false;
            while (($búfer = fgets($gestor)) !== false) {
                list($nombre, $cantidad, $precio) = explode(",", $búfer);
                if (strtolower($nombre_producto) === strtolower($nombre)) {
                    echo "Cantidad Vendida: $cantidad Precio: $precio\n";
                    $encontrado = true;
                    break;
                }
            } 
            if (!$encontrado) {
                echo "Producto no encontrado\n";
            }            
            fclose($gestor);
        }
    }

    function total_ventas($archivo) {
        $gestor = @fopen($archivo, "r");
        if ($gestor) {
            $total_ventas = 0;
            while (($búfer = fgets($gestor)) !== false) {
                list($nombre, $cantidad, $precio) = explode(",", $búfer);
                $total_ventas += $cantidad * $precio;
            } 
            fclose($gestor);

            return $total_ventas;                      
        }
    }

    function opcion($opcion, $archivo) {
        switch ($opcion) {
            case 1:
                echo "\nAñadir Producto\n";
                agregar_producto($archivo);
                break;
            case 2:
                if (is_file($archivo)) {
                    echo "\nConsultar Producto\n";
                    consultar_producto($archivo);
                } else {
                    echo "\nNo se han añadido productos\n";
                }
                break;
            case 3:
                echo "\nActualizar Producto\n";
                break;
            case 4:
                echo "\nEliminar Producto\n";
                break;
            case 5:
                if (is_file($archivo)) {
                    echo "\nListando Productos\n\n";
                    echo file_get_contents($archivo);
                } else {
                    echo "\nNo se han añadido productos\n";
                }
                break;
            case 6:
                if (is_file($archivo)) {
                    $total_ventas =  total_ventas($archivo);
                    echo "\nTotal Ventas: $total_ventas\n";                   
                } else {
                    echo "\nNo se han añadido productos\n";
                }
                break;
            case 7:                
                if (is_file($archivo)) {
                    echo "\nEliminando el archivo $archivo\n";
                    unlink($archivo);
                }                
                echo "Saliendo";
                break;
            default:
                echo "\nOpción no válida\n";                
        }
    }

    function menu($archivo) {
        do {    
            $opcion = null;
            system('cls');
            echo "\n1. Añadir Producto\n";
            echo "2. Consultar Producto\n";
            echo "3. Actualizar Producto\n";
            echo "4. Eliminar Producto\n";
            echo "5. Listar Productos\n";
            echo "6. Total de Ventas\n";
            echo "7. Salir\n";
            echo "\nEscoja una opción: ";
            fscanf(STDIN, "%d\n", $opcion);
            opcion($opcion, $archivo);
        } while ($opcion != 7);
    }

    $archivo = "edalmava.txt";
    $nombre = "Edalmava\n";
    $edad = "30\n";
    $lenguaje = "PHP";

    reto11($archivo, $nombre, $edad, $lenguaje);

    echo "\n\n*****RETO EXTRA*****\n";

    menu("ventas.txt");
