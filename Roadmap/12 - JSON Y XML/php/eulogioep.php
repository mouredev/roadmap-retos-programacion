<?php

// Datos de ejemplo
$persona = [
    'nombre' => 'Juan',
    'edad' => 30,
    'fechaNacimiento' => '1993-05-15',
    'lenguajesProgramacion' => ['PHP', 'JavaScript', 'Python']
];

// Función para crear el archivo XML
function crearArchivoXML($datos) {
    $xml = new SimpleXMLElement('<persona></persona>');
    array_walk_recursive($datos, function($value, $key) use ($xml) {
        if (is_array($value)) {
            $child = $xml->addChild($key);
            foreach ($value as $subvalue) {
                $child->addChild('lenguaje', $subvalue);
            }
        } else {
            $xml->addChild($key, $value);
        }
    });
    $xml->asXML('datos.xml');
    echo "Archivo XML creado.\n";
}

// Función para crear el archivo JSON
function crearArchivoJSON($datos) {
    file_put_contents('datos.json', json_encode($datos, JSON_PRETTY_PRINT));
    echo "Archivo JSON creado.\n";
}

// Función para mostrar el contenido de un archivo
function mostrarContenidoArchivo($nombreArchivo) {
    echo "Contenido del archivo $nombreArchivo:\n";
    echo file_get_contents($nombreArchivo) . "\n";
}

// Función para borrar un archivo
function borrarArchivo($nombreArchivo) {
    if (unlink($nombreArchivo)) {
        echo "El archivo $nombreArchivo ha sido borrado.\n";
    } else {
        echo "No se pudo borrar el archivo $nombreArchivo.\n";
    }
}

// Función para leer el archivo XML
function leerXML($nombreArchivo) {
    $xml = simplexml_load_file($nombreArchivo);
    $datos = json_decode(json_encode($xml), true);
    return $datos;
}

// Función para leer el archivo JSON
function leerJSON($nombreArchivo) {
    $jsonData = file_get_contents($nombreArchivo);
    return json_decode($jsonData, true);
}

// Función principal
function main() {
    global $persona;

    // Crear y mostrar archivo XML
    crearArchivoXML($persona);
    mostrarContenidoArchivo('datos.xml');

    // Crear y mostrar archivo JSON
    crearArchivoJSON($persona);
    mostrarContenidoArchivo('datos.json');

    // Borrar archivos
    borrarArchivo('datos.xml');
    borrarArchivo('datos.json');

    // DIFICULTAD EXTRA
    // Crear archivos nuevamente para la lectura
    crearArchivoXML($persona);
    crearArchivoJSON($persona);

    // Leer y transformar datos
    $personaXML = leerXML('datos.xml');
    $personaJSON = leerJSON('datos.json');

    echo "\nDatos leídos del XML:\n";
    print_r($personaXML);
    echo "\nDatos leídos del JSON:\n";
    print_r($personaJSON);

    // Borrar archivos nuevamente
    borrarArchivo('datos.xml');
    borrarArchivo('datos.json');
}

// Ejecutar la función principal
main();

?>