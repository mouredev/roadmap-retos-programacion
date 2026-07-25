<?php
function crearYComprimirArchivo($mensaje, $nombreTxt = "mensaje.txt", $nombreZip = "archivo_comprimido.zip") {
    // Crear el archivo de texto con el mensaje
    file_put_contents($nombreTxt, $mensaje);
    echo "Archivo de texto '$nombreTxt' creado con el mensaje.\n";

    // Crear y abrir el archivo .zip
    $zip = new ZipArchive();
    if ($zip->open($nombreZip, ZipArchive::CREATE) === TRUE) {
        // Añadir el archivo de texto al archivo .zip
        $zip->addFile($nombreTxt, basename($nombreTxt));
        $zip->close();
        echo "Archivo comprimido como '$nombreZip'.\n";
    } else {
        echo "Error al crear el archivo .zip.\n";
    }

    // Eliminar el archivo de texto después de comprimirlo, si no quieres conservarlo
    if (file_exists($nombreTxt)) {
        unlink($nombreTxt);
        echo "Archivo de texto '$nombreTxt' eliminado después de la compresión.\n";
    }
}

// Ejemplo de uso
$mensaje = "Este es un mensaje corto dentro del archivo de texto.";
crearYComprimirArchivo($mensaje);
