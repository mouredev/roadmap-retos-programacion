<?php
#Array indexados numéricamente
$data = ['Manuel', 'Bl4ck', 'Wolfy', 'Visionos'];
echo "Usando print_r():\n";
print_r($data);

#Array asociativo. También para simular diccionarios
$assocArray = ['nombre' => 'Juan', 'edad' => 25];
echo "Usando print_r():\n";
print_r($assocArray);

#Añadir elemento al final de array
array_push($data, 'Fresa');
print_r($data);

// Agregar un elemento al principio del array
array_unshift($data, 'Pera');
print_r($data);

// Agregar un elemento en una posición específica
array_splice($data, 2, 0, 'Uva');
print_r($data);
// Cambiar el elemento siguiente dentro del Array
$moverElemento = 'Pera';
$posicionActual = array_search($moverElemento, $data); // Obtener la posición actual del elemento
if ($posicionActual !== false) { // Si el elemento se encuentra en el array
    $nuevaPosicion = 2; // Nueva posición deseada
}
print_r($data);

#Listas enlazadas (Linked Lists)


#Pilas (Stacks)


#Colas (Queues)


#Árboles (Trees)


#Mapas (Maps)


#Conjuntos (Sets)


/* EXTRA */
    // Ejercicio extra

    $agenda = [];

    function extra() {

        global $agenda;

        while (true) {
            echo "---------- Agenda de Contactos ----------\n";
            echo "1. Buscar contacto\n";
            echo "2. Insertar contacto\n";
            echo "3. Actualizar contacto\n";
            echo "4. Eliminar contacto\n";
            echo "5. Salir\n";
            echo "-----------------------------------------\n";
        
            $opcion = readline("Seleccione una opción (1-5): ");
        
            switch ($opcion) {
                case 1:
                    buscarContacto($agenda);
                    break;
                case 2:
                    insertarContacto($agenda);
                    break;
                case 3:
                    actualizarContacto($agenda);
                    break;
                case 4:
                    eliminarContacto($agenda);
                    break;
                case 5:
                    echo "Saliendo del programa. ¡Hasta luego!\n";
                    exit;
                default:
                    echo "Opción no válida. Inténtelo de nuevo.\n";
            }
        }
    }

    extra();



    function buscarContacto($agenda) {
        $nombre = readline("Ingrese el nombre del contacto a buscar: ");
        $encontrado = false;

        foreach ($agenda as $contacto) {
            if ($contacto['nombre'] === $nombre) {
                echo "Nombre: {$contacto['nombre']}\n";
                echo "Teléfono: {$contacto['telefono']}\n";
                $encontrado = true;
                break;
            }
        }

        if (!$encontrado) {
            echo "Contacto no encontrado.\n";
        }
    }

    function insertarContacto(&$agenda) {
        $nombre = readline("Ingrese el nombre del nuevo contacto: ");
        $telefono = validarTelefono();

        $agenda[] = [
            'nombre' => $nombre,
            'telefono' => $telefono
        ];

        echo "Contacto insertado con éxito.\n";
    }

    function actualizarContacto(&$agenda) {
        $nombre = readline("Ingrese el nombre del contacto a actualizar: ");
        $indice = buscarIndiceContacto($agenda, $nombre);

        if ($indice !== -1) {
            $telefono = validarTelefono();
            $agenda[$indice]['telefono'] = $telefono;
            echo "Contacto actualizado con éxito.\n";
        } else {
            echo "Contacto no encontrado.\n";
        }
    }

    function eliminarContacto(&$agenda) {
        $nombre = readline("Ingrese el nombre del contacto a eliminar: ");
        $indice = buscarIndiceContacto($agenda, $nombre);

        if ($indice !== -1) {
            unset($agenda[$indice]);
            $agenda = array_values($agenda); // Reindexar el array después de eliminar un elemento
            echo "Contacto eliminado con éxito.\n";
        } else {
            echo "Contacto no encontrado.\n";
        }
    }

    function buscarIndiceContacto($agenda, $nombre) {
        foreach ($agenda as $indice => $contacto) {
            if ($contacto['nombre'] === $nombre) {
                return $indice;
            }
        }

        return -1;
    }

    function validarTelefono() {
        while (true) {
            $telefono = readline("Ingrese el número de teléfono: ");

            if (ctype_digit($telefono) && strlen($telefono) <= 8) {
                return $telefono;
            } else {
                echo "Número de teléfono no válido. Inténtelo de nuevo.\n";
            }
        }
    }
?>