<?php

// --------------------------------------------------
// ESTRUCTURAS DE DATOS DE PHP
// --------------------------------------------------

### ARRAY NUMÉRICO ( INDEXADO ) ###

// --- CREACIÓN ---
$animales =  ["Perro", "Conejo", "Paloma"];
print_r($animales);

// --- INSERCIÓN ---
// Se añade al final con corchetes vacíos o array_push()
$animales[] = "Gato";
array_push($animales, "Hurón");
echo "Tras insertar:\n";
print_r($animales);

// --- ACTUALIZACIÓN ---
// Se actualiza el valor de un indice específico
$animales[0] = "Lobo";
echo "Tras actualizar: " . implode(", ", $animales) . "\n"; // implode() convierte un array en una cadena de texto

// --- BORRADO ---
// unset() elimina un elemento del array por su índice, pero no reindexa
unset($animales[2]);
echo "Tras borrar:\n";
print_r($animales);

// Comprobamos que el indice 2 ya no existe, así que reindexamos con array_values()
$animales = array_values($animales);
echo "Tras reindexar:\n";
print_r($animales);

// --- ORDENACIÓN ---
// sort() ordena alfabéticamente para cadenas (de menor a mayor para números) y los reindexa 
sort($animales);
echo "Tras ordenar:\n\n";
print_r($animales);



### ARRAY ASOCIATIVO ( CLAVE => VALOR ) ###

// --- CREACIÓN ---
$mascota = [
    'especie' => 'Gato',
    'nombre' => 'Luna',
    'edad' => 9
];
echo "Mascota creada: Nombre: {$mascota['nombre']}, Especie: {$mascota['especie']}, Edad: {$mascota['edad']} \n";

// --- INSERCIÓN ---
//Agregamos una clave nueva entre corchetes con su valor
$mascota['raza'] = 'Siamesa red point';
$mascota['color'] = "Blanco con orejas y cola crema";
echo "Tras insertar: Luna es una gata {$mascota['raza']}, de color {$mascota['color']}\n";

// --- ACTUALIZACIÓN ---
//Modificamos el valor de una clave existente
$mascota['edad'] = 10;
echo "Tras actualizar: Luna es una gata {$mascota['raza']}, de color {$mascota['color']} que recientemente ha cumplido {$mascota['edad']} años\n";


// --- BORRADO ---
unset($mascota['color']);
echo "Sabemos el color de {$mascota['nombre']} tras eliminarlo? " . (isset($mascota['color']) ? 'Si' : 'No') . "\n";


// --- ORDENACIÓN ---
// ksort() ordena por clave
ksort($mascota);
echo "Tras ordenar por clave: \n";
foreach ($mascota as $clave => $valor) {
    echo " - $clave: $valor\n";
}



### SPLQUEUE (Cola FIFO: First In, First Out) ###

// --- CREACIÓN ---
$salaEspera = new SplQueue();

// --- INSERCIÓN ---
//enqueue() añade al final de la cola
$salaEspera->enqueue('Naruto');
$salaEspera->enqueue('Valkiria');
$salaEspera->enqueue('Melo');
echo "Pacientes en cola: " . $salaEspera->count() . "\n";

// --- ACTUALIZACIÓN ---
// Se accede por indice posicional como si fuera un array
$salaEspera[2] = 'Melo (vacuna urgente)';
echo "Paciente en turno 2 actualizado: {$salaEspera[2]}\n";

// --- BORRADO ---
// dequeue() atiende y saca al primero que llegó (FIFO)
$atendido = $salaEspera->dequeue(); // Sale Naruto
echo "Atendido en consulta: $atendido\n";
echo "Pacientes restantes: " . $salaEspera->count() . "\n";

// --- ORDENACIÓN ---
// iterator_to_array() para ordenar la cola, volcamos a array y aplicamos orden con sort
$pacientes = iterator_to_array($salaEspera);
sort($pacientes);
echo "Pacientes restantes: " .  implode(', ', $pacientes) . "\n\n";



### SPLSTACK (Pila LIFO: Last In, First Out) ###
// --- CREACIÓN ---
$transportines = new SplStack();

// --- INSERCIÓN ---
// push() apila uno encima de otro
$transportines->push('Transportin de Naru');
$transportines->push('Transportin de Auri');
$transportines->push('Transportin de Melo');
$transportines->push('Transportin de Luna');
$transportines->push('Transportin de Valkiria');
echo "Tenemos apilados " . $transportines->count() . " transportines\n";
echo "El que está más alto: {$transportines->top()}\n";

// --- ACTUALIZACIÓN ---
// El indice 0 siempre apunta a la cima de la pila
$transportines[0] = 'Transportin de Valkiria (con mantita)';
echo "Cima de transportines actualizada: {$transportines[0]}\n";

// --- BORRADO ---
//pop() retira el que está arriba del todo (LIFO)
$bajado = $transportines->pop(); // Saca el que está mas arriba
echo "Transportin retirado: $bajado\n";
echo "Ahora en la cima tenemos: {$transportines->top()}\n";

// --- ORDENACIÓN ---
// iterator_to_array() para ordenar la pila, volcamos a array y aplicamos orden con sort
$lista = iterator_to_array($transportines);
sort($lista);
echo "Transportines volcados y reordenados: " .  implode(', ', $lista) . "\n\n";



### SPLOBJECTSTORAGE ( Set / Mapa donde la clave es un objeto) ###
// --- CREACIÓN ---
$censoClinica = new SplObjectStorage();

// Creamos instancias de objetos para cada animal
$gato = (object) ['nombre' => 'Naru', 'especie' => 'Felino'];
$perro = (object) ['nombre' => 'Lupen', 'especie' => 'Canino'];
$cuervo = (object) ['nombre' => 'Vlad', 'especie' => 'Corvido'];

// --- INSERCIÓN ---
// attach($objetoAnimal, $datosAsociados)
$censoClinica->attach($gato, ['microchip' => true, 'peso_kg' => 8.2]);
$censoClinica->attach($perro, ['microchip' => true, 'peso_kg' => 15.6]);
$censoClinica->attach($cuervo, ['microchip' => false, 'peso_kg' => 1.6]);
echo "Animales registrados: " .  $censoClinica->count() . "\n";

// --- ACTUALIZACIÓN ---
// Usamos el propio objeto como clave para actualizar sus datos
$censoClinica[$gato] = ['microchip' => true, 'peso_kg' => 7.9];
$datosGato = $censoClinica[$gato];
echo "Peso actualizado de {$gato->nombre}: {$datosGato['peso_kg']} kg\n";

// --- BORRADO ---
// detach() retira el objeto y toda su información vinculada
$censoClinica->detach($perro);
echo "Está {$perro->nombre} en el censo tras el borrado? " . ($censoClinica->contains($perro) ? 'Si' : 'No') . "\n";

// --- ORDENACIÓN ---
// Al ser un mapa de referencias en memoria, se itera a un array temporal para ordenar por alguna propiedad
$animalesOrdenados = [];
foreach ($censoClinica as $animal) {
    $animalesOrdenados[] = [
        'nombre' => $animal->nombre,
        'peso' => $censoClinica[$animal]['peso_kg']
    ];
}

usort($animalesOrdenados, fn($a, $b) => strcmp($a['nombre'], $b['nombre']));
echo "Listado ordenado: \n";
foreach ($animalesOrdenados as $item) {
    echo " - {$item['nombre']}: {$item['peso']} kg\n";
}


//-----------------------------------------------------------
// En PHP no hay tuplas como tal. Se usa un array normal y se "desempaqueta" en variables separadas.
//-----------------------------------------------------------

### - - - EJEMPLO 1 DE "TUPLA": DESEMPAQUETAR CON [...] - - - ###

// La función devuelve un array simple con 2 datos
function getGatito(): array {
    return ['Luna', 4]; // [nombre, edad]
}

// En lugar de guardar el array, lo desempaquetamos directamente en variables
[$nombre, $edad] = getGatito();

// Ya tenemos las variables listas para usar
echo "Nombre: $nombre\n";
echo "Edad: $edad años\n";


### - - - EJEMPLO 2 DE "TUPLA": Existo/Fallo, mensaje - - - ###
// La función valida y devuelve el paquete: [bool, string]
function validarMascota(string $nombre, int $edad) : array {
    if (empty($nombre)) {
        return [false, 'El nombre no puede estar vacío'];
    }

    if ($edad < 0) {
        return [false, 'La edad no puede ser negativa'];
    }

    return [true, "Mascota $nombre registrada con éxito"];
}

// Desempaquetamos el resultado en dos variables
[$ok, $mensaje] = validarMascota('Luna', 8);

if ($ok) {
    echo "EXITO: $mensaje\n";
} else {
    echo "ERROR: $mensaje\n";
}

### - - - EJEMPLO 3 DE "TUPLA": Intercambiar dos variables sin una tercera variable temporal - - - ###
$primerTurno = 'Luna';
$segundoTurno = 'Naru';

// Intercambiamos los valores en una sola linea usando la sintaxis de tupla
[$primerTurno, $segundoTurno] = [$segundoTurno, $primerTurno];

echo "1º: $primerTurno, 2º: $segundoTurno\n";


/* --------------------------------------------------

    DIFICULTAD EXTRA:

    Crea una agenda de contactos por terminal.

    - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
    - Cada contacto debe tener un nombre y un número de teléfono.
    - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos
        para llevarla a cabo.
    - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos ( o el número
        que quieras).
    - También se debe proponer una operación de finalización del programa.

----------------------------------------------------- */

$agenda = [];

// Funcion para validar el teléfono
function validarTelefono(string $tel): bool {
    /*
        Comprobamos:
        - is_numeric(): que sea un valor numérico
        - strlen() === 9: que tenga 9 caracteres
        - !str_contains(): descargamos signos negativos y decimales
    */
    return is_numeric($tel)     && strlen($tel) === 9 
    && !str_contains($tel, '-') && !str_contains($tel, '.') && !str_contains($tel, ',');
}

// Funcion auxiliar para solicitar y obligar a añadir un teléfono válido
function pedirTeléfono(): string {
    while (true) {
        // readline() pide el texto por consola y trim() quita espacios
        $tel = trim(readline("Teléfono (9 dígitos): "));

        // Si cumple las condiciones, lo devolvemos y rompemos el bucle
        if (validarTelefono($tel)) {
            return $tel;
        }

        // Si no es válido, muestra el aviso y vuelve a empezar el bucle
        echo "Error: Debe contener 9 dígitos numéricos positivos\n";
    }
}

// Bucle para el menú interactivo
while(true) {
    echo "\n ====== BIENVENIDO A TU AGENDA ====== \n";
    echo "1. Buscar || 2. Insertar || 3. Actualizar || 4. Eliminar || 5. Salir\n";
    $opcion = trim(readline("Elige una opción: \n"));

    // Si elige la opción 5, se rompe el bucle infinito y finaliza
    if ($opcion === '5') {
        echo "Hasta luego! \n";
        break;
    }

    // Pedimos el nombre del contacto para las opciones
    $nombre = trim(readline("Introduce el nombre: "));

    switch ($opcion) {
        case '1': // -- Buscar --
            // isset() comprueba si la clave ya existe dentro del array
            if (isset($agenda[$nombre])) {
                echo "Teléfono de $nombre: {$agenda[$nombre]}\n";
            } else {
                echo "Contacto no encontrado\n";
            }
            break;

        case '2': // -- Insertar --
            if (isset($agenda[$nombre])) {
                echo "El contacto ya existe. Para modificar, usa la opción de Actualizar\n";
            } else {
                // Guardamos el nuevo contacto
                $agenda[$nombre] = pedirTeléfono();
                echo "Contacto guardado correctamente\n";
            }
            break;
            
        case '3': // -- Actualizar --
            if (!isset($agenda[$nombre])) {
                echo "No existe ese contacto para actualizar\n";
            } else {
                // Sobreescribimos el valor existente
                $agenda[$nombre] = pedirTeléfono();
                echo "Contacto actualizado correctamente\n";
            }
            break;
            
        case '4': // -- Eliminar --
            if (isset($agenda[$nombre])) {
                // unset() destruye la clave y su valor del array
                unset($agenda[$nombre]);
                echo "Contacto eliminado correctamente\n";
            } else {
                echo "No existe ese contacto\n";
            }
            break;
        
        default:
            echo "Opción no válida. Introduce un número del 1 al 5\n";
        break;
    }
}