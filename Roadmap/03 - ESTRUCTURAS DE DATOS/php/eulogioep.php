<?php

// Función para ejemplificar las estructuras de datos en PHP
function ejemplosEstructurasDatos() {
    // Array indexado: equivalente a ArrayList en Java
    $array = ['Java', 'Python', 'PHP'];
    echo "Array indexado: " . implode(", ", $array) . "\n";

    // Array asociativo: equivalente a HashMap en Java
    $arrayAsociativo = [
        'Uno' => 1,
        'Dos' => 2,
        'Tres' => 3
    ];
    echo "Array asociativo: ";
    print_r($arrayAsociativo);

    // SplFixedArray: array de tamaño fijo
    $splArray = new SplFixedArray(3);
    $splArray[0] = 'Rojo';
    $splArray[1] = 'Verde';
    $splArray[2] = 'Azul';
    echo "SplFixedArray: " . implode(", ", $splArray) . "\n";

    // Operaciones
    unset($array[1]); // Borrado (elimina 'Python')
    $array[] = 'JavaScript'; // Inserción
    $array[1] = 'TypeScript'; // Actualización
    sort($array); // Ordenación

    echo "Array después de operaciones: " . implode(", ", $array) . "\n";
}

// Función principal para la agenda de contactos
function agendaContactos() {
    $agenda = [];

    while (true) {
        echo "\n--- Agenda de Contactos ---\n";
        echo "1. Buscar contacto\n";
        echo "2. Añadir contacto\n";
        echo "3. Actualizar contacto\n";
        echo "4. Eliminar contacto\n";
        echo "5. Mostrar todos los contactos\n";
        echo "6. Salir\n";
        echo "Seleccione una opción: ";

        $opcion = trim(fgets(STDIN));

        switch ($opcion) {
            case '1':
                buscarContacto($agenda);
                break;
            case '2':
                anadirContacto($agenda);
                break;
            case '3':
                actualizarContacto($agenda);
                break;
            case '4':
                eliminarContacto($agenda);
                break;
            case '5':
                mostrarContactos($agenda);
                break;
            case '6':
                echo "¡Hasta luego!\n";
                return;
            default:
                echo "Opción no válida.\n";
        }
    }
}

function buscarContacto(&$agenda) {
    echo "Ingrese el nombre del contacto: ";
    $nombre = trim(fgets(STDIN));
    if (isset($agenda[$nombre])) {
        echo "Teléfono de $nombre: {$agenda[$nombre]}\n";
    } else {
        echo "Contacto no encontrado.\n";
    }
}

function anadirContacto(&$agenda) {
    echo "Ingrese el nombre del contacto: ";
    $nombre = trim(fgets(STDIN));
    $telefono = solicitarTelefono();
    $agenda[$nombre] = $telefono;
    echo "Contacto añadido con éxito.\n";
}

function actualizarContacto(&$agenda) {
    echo "Ingrese el nombre del contacto a actualizar: ";
    $nombre = trim(fgets(STDIN));
    if (isset($agenda[$nombre])) {
        $telefono = solicitarTelefono();
        $agenda[$nombre] = $telefono;
        echo "Contacto actualizado con éxito.\n";
    } else {
        echo "Contacto no encontrado.\n";
    }
}

function eliminarContacto(&$agenda) {
    echo "Ingrese el nombre del contacto a eliminar: ";
    $nombre = trim(fgets(STDIN));
    if (isset($agenda[$nombre])) {
        unset($agenda[$nombre]);
        echo "Contacto eliminado con éxito.\n";
    } else {
        echo "Contacto no encontrado.\n";
    }
}

function mostrarContactos($agenda) {
    if (empty($agenda)) {
        echo "La agenda está vacía.\n";
    } else {
        foreach ($agenda as $nombre => $telefono) {
            echo "$nombre: $telefono\n";
        }
    }
}

function solicitarTelefono() {
    while (true) {
        echo "Ingrese el número de teléfono (máximo 11 dígitos): ";
        $telefono = trim(fgets(STDIN));
        if (preg_match('/^\d{1,11}$/', $telefono)) {
            return $telefono;
        }
        echo "Número no válido. Debe ser numérico y tener máximo 11 dígitos.\n";
    }
}

// Ejecutamos los ejemplos y la agenda
echo "Ejemplos de estructuras de datos en PHP:\n";
ejemplosEstructurasDatos();

echo "\nIniciando la agenda de contactos...\n";
agendaContactos();

?>