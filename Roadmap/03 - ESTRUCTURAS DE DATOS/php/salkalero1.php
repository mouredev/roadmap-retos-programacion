<?php 
// arrays
echo "Arrays Indexados(Listas)\n";

$ciudades = [
    'Córdoba',
    'Málaga',
    'Cádiz',
    'Sevilla',
    'Jaén',
    'Almería',
    'Huelva',
    'Granada'
];

echo "\n\nInserción\n";
 $ciudades[] = 'Madrid';

 array_push($ciudades , 'Bilbao');

foreach($ciudades as $ciudad){
    echo ' Ciudad:' . $ciudad . ",";
}

 echo "\n\nBorrado\n";
 unset($ciudades[1]); // Borra el índice pero no reorganiza el índice, el índice 1 ya no existe.

echo "\n";
 foreach($ciudades as $ciudad){
    echo ' Ciudad:' . $ciudad . ",";
}

array_splice($ciudades, 2, 3); // Borra el índice y reorganiza el índice.


echo "\n";
 foreach($ciudades as $ciudad){
    echo ' Ciudad:' . $ciudad . ",";
}
echo "\n\nActualización\n";

$ciudades[0] = "Málaga";

echo "\n";
 foreach($ciudades as $ciudad){
    echo ' Ciudad:' . $ciudad . ",";
}

echo "\n\nOrdenación\n";
sort($ciudades);
 foreach($ciudades as $ciudad){
    echo ' Ciudad:' . $ciudad . ",";
}

echo "\n\nArrays Asociativos (Diccionarios)\n";/////////////////////////////////////////////


$productos = ["id" => 101, "nombre" => "Portátil", "precio" => 800];

echo "\n\nInserción\n";
$productos["stock"] = 50;

foreach ($productos as $clave => $valor) {
    echo "$clave:$valor\n";
}

print_r($productos);

var_dump($productos);

 echo "\n\nBorrado\n";
unset($productos["precio"]);

foreach ($productos as $clave => $valor) {
    echo "$clave:$valor\n";
}

echo "\n\nActualización\n";
$productos["stock"] = 750;

foreach ($productos as $clave => $valor) {
    echo "$clave:$valor\n";
}

echo "\n\nOrdenación\n";

ksort($productos); // Por clave.
foreach ($productos as $clave => $valor) {
    echo "$clave:$valor\n";
}

echo "\n";

asort($productos); // Por Valores
foreach ($productos as $clave => $valor) {
    echo "$clave:$valor\n";
}
/////////////////////////////////////////////////////////////////////////////////////////
// EJERCICIO EXTRA
/////////////////////////////////////////////////////////////////////////////////////////
echo "\n\nEJERCICIO EXTRA\n";

// 1- Primero se crea el almacen.
$agenda = [];

// 2- Se crea un bucle para que el programa no se cierre solo.
while(true) {
    // Se pinta el menú para que el usuario sepa qué puede hacer.
    echo "\n--- AGENDA TELEFÓNICA ---\n";
    echo " 1.- Buscar | 2.- Insertar | 3.- Actualizar | 4.- Eliminar | 5.- Mostrar | 6.- Salir\n";

    // Espero a que el usuario escriba su opción.
    $opcion = trim(readline("Elige una opción (1-6): "));
    

    // 3- El enrutador (switch).
    switch ($opcion) {
        case "1":
            buscarContacto($agenda);
            break;
        case "2":
            insertarContacto($agenda); 
            break;
        case "3":
            actualizarContacto($agenda);
            break;
        case "4":
            eliminarContacto($agenda);
            break;
        case "5":
            mostrarContacto($agenda);
            break;
        case "6":
            salirAgenda($agenda);
            exit;
        default:
            echo "\nSeleccione una opción.\n";
            break;
    }

}

function buscarContacto($agenda){
   echo "\n------------------------ BUSCAR CONTACTO ------------------------\n";
   // Pedimos el nombre a buscar.
   $nombreImput = trim(readline("Introduce el nombre a buscar: "));
   $nombre = strtolower($nombreImput); // Guardamos el texto en minúsculas
   // Verificamos que el contacto existe en la agenda.
   if(!isset($agenda[$nombre])) {
            echo "\nError. el contacto no existe en la agenda.\n";
            return;
        }
   echo "\nEl contacto existe. $nombre, con el Teléfono: " . $agenda[$nombre] . "\n";
}
function insertarContacto(&$agenda){ // El & se usa para que al modificar el array dentro de la función , los cambios se reflejen en el array externo.            
    // Pedimos el nombre.
    echo "\nINSERTAR CONTACTO\n";
    $nombreImput = trim(readline("\nIntroduce el Nombre: "));
    $nombre = strtolower($nombreImput); // Guardamos el texto en minúsculas
    if(empty($nombre)) {
        echo "\nError. El nombre no puede estar vacío\n";
        return; // Salimos de la función y regresamos al menú,
    }
    // Pedimos el teléfono.
    $tlf = trim(readline("\nIntroduce el número de teléfono(máx 11 caracteres): \n"));
    // Validamos las condiciones del Tlf.
    if(!ctype_digit($tlf)) { // Valída que sean sólo números.
        echo "\nError. Sólo se permiten números\n";
        return;
    }
    if(strlen($tlf) > 11) { // Valída que sólo tenga hasta 11 caracteres.
        echo "\nError. El teléfono no puede tener más de 11 números\n";
        return;
    }
    // Si el valor introduciso en $tlf cumple con las condiciones, se guarda en el array asociativo.
    $agenda[$nombre] = $tlf;
    echo "Contacto guardado correctamente\n";
}
function actualizarContacto(&$agenda) {
        echo "\n------------------------ ACTUALIZAR TLF CONTACTO ------------------------\n";
        // Pedimos el nombre de contacto para actualizar.
        $nombreImput = trim(readline("\nIntroduce el nombre para actualizar: "));
        $nombre = strtolower($nombreImput); // Guardamos el texto en minúsculas
        // Verificamos que el contacto existe en la agenda.
        if(!isset($agenda[$nombre])) {
            echo "\nError. el contacto no existe en la agenda.\n";
            return;
        }
        // Mostramos el contacto con el valor actual.
        echo "\nNombre: $nombre\nTeléfono: " . $agenda[$nombre] . "\n";
        // Pedimos el teléfono nuevo y alidamos las condiciones del Tlf.
        $nuevoTlf = trim(readline("\nIntroduce el nuevo número de teléfono(máx 11 caracteres): \n"));
        if(!ctype_digit($nuevoTlf)) { // Valída que sean sólo números.
            echo "\nError. Sólo se permiten números.\n";
            return;
        }
        if(strlen($nuevoTlf) > 11) { // Valída que sólo tenga hasta 11 caracteres.
            echo "\nError. El nº de teléfono no puede tener más de 11 números.\n";
            return;
        }
        $agenda[$nombre] = $nuevoTlf;
        // Mostramos el contacto con el nuevo nº de teléfono.
        echo "\nContacto actualizado.\n";
        echo "\n$nombre : $nuevoTlf \n";
}
function eliminarContacto(&$agenda) {
        echo "\n------------------------ ELIMINAR CONTACTO ------------------------\n";
        // Pedimos el nombre del contacto a eliminar.
        $nombreImput = trim(readline("\nIntroduzca el nombre a eliminar: "));
        $nombre = strtolower($nombreImput); // Guardamos el texto en minúsculas
        // Verificamos que el contacto existe en la agenda.
        if(!isset($agenda[$nombre])) {
            echo "\nError. el contacto no existe en la agenda.\n";
            return;
        }
        // Eliminamos el contacto.
        unset ($agenda[$nombre]);
        echo "\nContacto borrado de la agenda.\n";
        // unset($productos["precio"]);
}
function mostrarContacto($agenda) {
    echo "\nMOSTRAR AGENDA\n";
    if(!empty($agenda)) {
        echo "\nNombre => Teléfono\n\n";
        foreach ($agenda as $key => $valor) {
        echo "$key => $valor\n";
    }
        
    }else {
        echo "\nLa agenda está vacía\n";
    }
    
}
function salirAgenda($agenda) {
    echo "Saliendo...\n";
}
