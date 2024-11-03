<?php

function comprimirArchivoEnZip($archivo, $nombreZip) {
    $zip = new ZipArchive();
    if ($zip->open($nombreZip, ZipArchive::CREATE) === TRUE) {
        $zip->addFile($archivo, basename($archivo));
        $zip->close();
        echo "Archivo comprimido con éxito en $nombreZip\n";
    } else {
        echo "Error al crear el archivo ZIP\n";
    }
}

function comprimirDirectorioEnZip($directorio, $nombreZip) {
    $zip = new ZipArchive();

    function agregarDirectorioAlZip($carpeta, $zip, $carpetaRaiz) {
        $archivos = scandir($carpeta);
        foreach ($archivos as $archivo) {
            if ($archivo == '.' || $archivo == '..') continue;
            $rutaCompleta = $carpeta . '/' . $archivo;
            $rutaEnZip = $carpetaRaiz . '/' . $archivo;
            if (is_file($rutaCompleta)) {
                $zip->addFile($rutaCompleta, $rutaEnZip);
            } elseif (is_dir($rutaCompleta)) {
                $zip->addEmptyDir($rutaEnZip);
                agregarDirectorioAlZip($rutaCompleta, $zip, $rutaEnZip);
            }
        }
    }

    if ($zip->open($nombreZip, ZipArchive::CREATE) === TRUE) {
        agregarDirectorioAlZip($directorio, $zip, basename($directorio));
        $zip->close();
        echo "Directorio comprimido con éxito en $nombreZip\n";
    } else {
        echo "Error al crear el archivo ZIP\n";
    }
}

function comprimirEnRar($input, $nombreRar, $tipo) {
    if ($tipo == 'archivo') {
        $comando = "rar a $nombreRar $input";
    } else {
        $comando = "rar a -r $nombreRar $input"; // Opción -r para incluir subdirectorios
    }
    
    exec($comando, $salida, $resultado);
    if ($resultado === 0) {
        echo "Archivo/directorio comprimido en RAR con éxito: $nombreRar\n";
    } else {
        echo "Error al comprimir en RAR\n";
    }
}

function comprimir($input, $tipo, $formato, $nombreSalida) {
    if ($formato == 'zip') {
        if ($tipo == 'archivo') {
            comprimirArchivoEnZip($input, $nombreSalida);
        } else {
            comprimirDirectorioEnZip($input, $nombreSalida);
        }
    } elseif ($formato == 'rar') {
        comprimirEnRar($input, $nombreSalida, $tipo);
    } else {
        echo "Formato de compresión no soportado\n";
    }
}

echo "Selecciona lo que quieres comprimir:\n";
echo "1. Archivo\n";
echo "2. Directorio\n";
$tipoSeleccionado = trim(fgets(STDIN));

if ($tipoSeleccionado == '1') {
    $tipo = 'archivo';
} elseif ($tipoSeleccionado == '2') {
    $tipo = 'directorio';
} else {
    die("Selección no válida\n");
}

echo "Introduce la ruta del $tipo que deseas comprimir: ";
$input = trim(fgets(STDIN));

echo "Selecciona el formato de compresión:\n";
echo "1. ZIP\n";
echo "2. RAR\n";
$formatoSeleccionado = trim(fgets(STDIN));

if ($formatoSeleccionado == '1') {
    $formato = 'zip';
} elseif ($formatoSeleccionado == '2') {
    $formato = 'rar';
} else {
    die("Formato no válido\n");
}

echo "Introduce el nombre de salida (sin la extensión): ";
$nombreSalida = trim(fgets(STDIN));

if ($formato == 'zip') {
    $nombreSalida .= '.zip';
} elseif ($formato == 'rar') {
    $nombreSalida .= '.rar';
}

comprimir($input, $tipo, $formato, $nombreSalida);

?>
