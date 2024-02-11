<?php

    // Ejemplos de estructuras de datos basicos en php
    
    // Array

    echo "Vamos a mostrar en priemr lugar un array \n";
    $array = array(5, 1, 4, 2, 3);

    echo "El array es: \n";
    print_r($array);
    echo "\n";

    echo "El array ordenado es: \n";
    sort($array);
    print_r($array);
    echo "\n";

    echo "El array ordenado al reves es: \n";
    rsort($array);
    print_r($array);
    echo "\n";

    $array = array(5, 1, 4, 2, 3); // Vamos volver al array original 
    echo "Vamos a volver al array original y a mostrar el contenido de la posicion 3: \n";
    echo $array[2]; // 4
    echo "\n";

    echo "\n\nAhora vamos a añadir un elemento al array y a mostrar su contenido: \n";
    $array[] = 6;
    print_r($array);
    echo "\n";

    echo "\n\nAhora vamos a eliminar el elemento con indice 3 del array y a mostrar su contenido: \n";
    unset($array[3]);
    print_r($array);
    echo "\n";

    echo "Vamos a mostrar el contenido de todas las posiciones del array: \n";
    foreach ($array as $valor) {
        echo "$valor \n";
    }
    echo "\n";

    echo "Vamos a mostrar el contenido de todas las posiciones del array con su indice: \n";
    foreach ($array as $indice => $valor) {
        echo "$indice: $valor \n";
    }
    echo "\n";

    // Array asociativo
    echo "\n\nAhora vamos a crear un array asociativo y a mostrar su contenido: \n";
    
    $arrayAsociativo = array("uno" => 1, "dos" => 2, "tres" => 3);
    print_r($arrayAsociativo);
    echo "\n";

    echo "Vamos a mostrar el contenido de todas las posiciones del array asociativo: \n";
    foreach ($arrayAsociativo as $valor) {
        echo "$valor \n";
    }
    echo "\n";

    echo "\n\nAhora vamos a añadir un elemento al array asociativo y a mostrar su contenido: \n";
    $arrayAsociativo["cuatro"] = 4;
    print_r($arrayAsociativo);
    echo "\n";

    echo "\n\nAhora vamos a ordenar el array asociativo y a mostrar su contenido: \n";
    ksort($arrayAsociativo);
    print_r($arrayAsociativo);
    echo "\n";

    echo "\n\nAhora vamos a eliminar el elemento con indice 'dos' del array asociativo y a mostrar su contenido: \n";
    unset($arrayAsociativo["dos"]);
    print_r($arrayAsociativo);
    echo "\n";

    // pilas
    echo "\n\nAhora vamos a crear una pila y a mostrar su contenido: \n";
    $pila = array();
    array_push($pila, 1);
    array_push($pila, 2);
    array_push($pila, 3);
    print_r($pila);
    echo "\n";
    
    echo "\n\nAhora vamos a mostrar el contenido de la pila: \n";
    foreach ($pila as $valor) {
        echo "$valor \n";
    }
    echo "\n";

    echo "\n\nAhora vamos a mostrar el ultimo elemento de la pila: \n";
    echo array_pop($pila);
    print_r($pila);
    echo "\n";

    // colas
    echo "\n\nAhora vamos a crear una cola y a mostrar su contenido: \n";
    $cola = array();
    array_push($cola, 1);
    array_push($cola, 2);
    array_push($cola, 3);
    print_r($cola);
    echo "\n";

    echo "\n\nAhora vamos a meter un elemento en la cola y a mostrar su contenido: \n";
    array_unshift($cola, 4);
    print_r($cola);
    echo "\n";

    echo "\n\nAhora vamos a mostrar el contenido de la cola: \n";
    foreach ($cola as $valor) {
        echo "$valor \n";
    }
    echo "\n";

    echo "\n\nAhora vamos a mostrar el primer elemento de la cola: \n";
    echo array_shift($cola);
    print_r($cola);
    echo "\n";

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

























