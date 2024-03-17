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
        echo "1. Añadir venta\n";
        echo "2. Ver ventas\n";
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
                break;
            default:
                echo "Opción no válida\n";
                break;
        }
    } while ($option != 6); 

