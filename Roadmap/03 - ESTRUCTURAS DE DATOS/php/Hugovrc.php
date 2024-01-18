<?php

// Arrays
echo "----- Arrays ---- \n";
$marcas_autos = ["BMW","Ford","Chevrolet","Honda","Mazda"];
print_r($marcas_autos);

// Diccionarios
echo "----- Diccionario ---- \n";
$modelo_anio = array("BMW M3"=>2012, "Focus"=>2015, "Camaro"=>2023, "Civic"=>2021);
print_r($modelo_anio);

echo "----- Agregar elemento ---- \n";
// Insercion de elemento
$marcas_autos[] = "Mitsubishi";
print_r($marcas_autos);

// Borrado
echo "----- Borrar elemento ---- \n";
unset($marcas_autos[2]); //Se agrega el indice del elemento entre corchetes que se quiere borrar
print_r($marcas_autos);

// Actualizacion
echo "----- Modificar elemento ---- \n";
$marcas_autos[0] = "Toyota"; // entre corchetes el numero del elemento que se quiere modificar
print_r($marcas_autos);

// ordenacion
//ascendente
echo "----- Ordenar elementos de forma ascendente ---- \n";
sort($marcas_autos);
print_r($marcas_autos);

//descendente
echo "----- Ordenar elementos de forma descendente ---- \n";
rsort($marcas_autos);
print_r($marcas_autos);

//Ascendente segun el valor
echo "----- Ordenar elementos de forma ascendente por el valor ---- \n";
asort($marcas_autos);
print_r($marcas_autos);

//descendente sugun el valor
echo "----- Ordenar elementos de forma descendente por el valor ---- \n";
arsort($marcas_autos);
print_r($marcas_autos);

//Ascendente segun la clave
echo "----- Ordenar elementos de forma ascendente por la clave ---- \n";
ksort($marcas_autos);
print_r($marcas_autos);

//descendente segun la clave
echo "----- Ordenar elementos de forma descendente por la clave ---- \n";
krsort($marcas_autos);
print_r($marcas_autos);

// DIFICULTAD EXTRA
echo "----- DIFICULTAD EXTRA ---- \n";

$agenda_contactos = array();

/*echo "Menu: 
        1.- Buscar 
        2.- Insertar
        3.- Actualizar
        4.- Eliminar
        5.- Salir \n";
echo "Que deseas realizar: ";
fscanf(STDIN, "%s", $accion);
*/
while ($accion < 5) {
    echo "Menu: 
            1.- Buscar 
            2.- Insertar
            3.- Actualizar
            4.- Eliminar
            5.- Salir \n";
    echo "Que deseas realizar: ";
    fscanf(STDIN, "%s", $accion);
    if ($accion == 5) break;
    elseif ($accion == 1) {
        echo "que nombre deseas buscar: ";
        $nombre = trim(fgets(STDIN));
        if (array_key_exists($nombre, $agenda_contactos)) {
            echo "Nombre: " .$nombre. "Telefono: " .$agenda_contactos[$nombre];
        } else {
            echo $nombre. " No existe en la agenda \n";
        }
    } elseif ($accion == 2) {
        echo "Ingresa Nombre: ";
        $nombre = fgets(STDIN);
        echo "Ingresa el telefono: ";
        $telefono = trim(fgets(STDIN));
        if (strlen($telefono) <= 10 and is_numeric($telefono)) {
            $agenda_contactos[$nombre] = $telefono;
            print_r($agenda_contactos);
        } else {
            echo "El numero de telefono no puede contener mas de 10 digitos y debe ser numerico\n";
        }
        
    } elseif ($accion == 3) {
        echo "Ingresa el nombre del contacto a modificar: ";
        $nombre = fgets(STDIN);
        if (array_key_exists($nombre, $agenda_contactos)) {
            echo "ingresa el nuevo numero de telefono: ";
            $telefono = fgets(STDIN);
            if (strlen($telefono) <= 10 and is_numeric($telefono)) {
                $agenda_contactos[$nombre] = $telefono;
            } else {
                echo "El numero de telefono no puede contener mas de 10 digitos y debe ser numerico\n";
            }
        } else {
            echo "Ese contacto no existe en la agenda, intenta de nuevo\n";
        }
    } elseif ($accion == 4) {
        echo "Ingresa el nombre del contacto a eliminar: ";
        $nombre = fgets(STDIN);
        if (array_key_exists($nombre, $agenda_contactos)) {
            unset($agenda_contactos[$nombre]);
            echo "Contacto eliminado!!";
        } else {
            echo "Ese contacto no existe en la agenda, intenta de nuevo\n";
        }
    }
}
?>