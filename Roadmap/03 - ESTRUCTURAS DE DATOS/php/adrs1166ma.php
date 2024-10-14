<?php 

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
function _start(){echo 'Invocacion<pre>';} // 🔹funciones para el ejemplo
function _end(){echo '</pre><br>';} // 🔹funciones para el ejemplo
/*
    🟢 Estructuras de Datos
*/
// 🟠 Forma 1 
$carrito1 = array (
    'carne' => "🥩",
    'papitas' => "🍟",
    'pizza' => "🍕",
    'chocolate' => "🍫",
    'whafle' => "🧇",
    'huevo' => "🥚"
);


// 🟠 Forma 2 
class tienda {
    public $Dato1 = "🥩";
    public $Dato2 = "🍟";
    public $Dato3 = "🍕";
    public $Dato4 = "🍫";
    public $Dato5 = "🧇";
    public $Dato6 = "🥚";
}
$carrito2 = new tienda();


// 🟠 Forma 3 
$carrito3 = array('🥩','🍟','🍕','🍫','🧇','🥚'); // mas usada en Wordpress


// 🟠 Forma 4 
$carrito4 = ['🥩','🍟','🍕','🍫','🧇','🥚']; // mas usada en Laravel
//             0  , 1  ,  2  ,  3 ,  4  , 5    |  Indices/posicion general

// Mostrar en pantalla 🔹
_start();
// Forma en pantalla
var_dump($carrito1);
var_dump($carrito2);
var_dump($carrito3);
var_dump($carrito4);
// Extrar un Dato en pantalla
echo $carrito1['chocolate']; // Extraer 🍫
echo $carrito2 -> Dato4; // Extraer 🍫
echo $carrito3[3]; // Extraer 🍫
echo $carrito4[3]; // Extraer 🍫
_end();


// 🟠 Ordenamiento 
$abecedario = ['z', 'b', 'h', 'n', 'q', 'v', 'y', 'a', 'c', 'e', 'i', 'o', 'u', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'p', 'r', 's', 't', 'w', 'x'];
$numeros = [4, 6 , 2, 1, 9, 3, 5, 8, 7, 11, 19, 13, 10, 20, 14, 18, 12, 17, 15, 16];
// De menor a mayor
_start();
sort($abecedario);
sort($numeros);
sort($carrito4);
// Imprimir
print_r($abecedario);
print_r($numeros);
print_r($carrito4);
_end();

// Al reves
_start();
rsort($abecedario);
rsort($numeros);
rsort($carrito4);
// Imprimir
print_r($abecedario);
print_r($numeros);
print_r($carrito4);
_end();

echo "🟠 Añadir<br>"; 
$carrito4 = ['🥩','🍟','🍕','🍫','🧇','🥚']; //array original

_start();
$carrito4[6] = '🍔'; // agregarlo en el indice 6
print_r($carrito4); 
// Ahora tendra estos datos '🥩','🍟','🍕','🍫','🧇','🥚','🍔'
_end();
_start();
array_push($carrito4,'🥓'); // agregarlo al final del arreglo
print_r($carrito4); 
// Ahora tendra estos datos '🥩','🍟','🍕','🍫','🧇','🥚','🍔','🥓'
_end();
_start();
array_unshift($carrito4,'🍙'); // agregarlo al inicio del arreglo
print_r($carrito4); 
// Ahora tendra estos datos '🍙','🥩','🍟','🍕','🍫','🧇','🥚','🍔','🥓'
_end();

echo "🟠 Eliminar"; 
_start();
unset($carrito4[4]); // Eliminamso chocolate 
print_r($carrito4); // '🍙','🥩','🍟','🍕','🧇','🥚','🍔','🥓'
_end();
_end();



echo "🟠 Mostrar<br>"; 
_start();
foreach ($carrito4 as $producto) {
    echo $producto.'<br>';
}
_end();




// 🟠 Associative Arrays
$carrito1 = array (
    'carne' => "🥩",
    'papitas' => "🍟",
    'pizza' => "🍕",
    'chocolate' => "🍫",
    'whafle' => "🧇",
    'huevo' => [
        'magnitud' => "kl",
        'precio' => 5.50,
        'informacion' => [
            'Descripcion' => "Excelente fuente de vitaminas y minerales",
            'icono' => "🥚"
        ]
    ]   
);

// Imprimirlo
_start();
echo $carrito1['huevo']; // ❌
echo '<br>';
echo $carrito1['huevo']['informacion']['Descripcion']; // ✅
echo '<br>';
echo $carrito1['huevo']['informacion']['icono']; // ✅
_end();

echo '<br>';

_start();
echo $carrito1['huevo']['informacion']['pronombre'] = 'Huevito hacker'; // ✅
echo '<br>';
var_dump($carrito1);
_end();



echo '<br>🔥 Extra <br>';
/*
    🔥 Extra
*/
$agenda = [];

_start();
function extra() {

    global $agenda;

    while (true) {
    
        $opcion = readline("\n\n--------------------------- \n/- Agenda de Contactos -/ \n1. Buscar contacto \n2. Insertar contacto \n3. Actualizar contacto \n4. Eliminar contacto \n5. Salir \n--------------------------- \nSeleccione una opción (1-5): ");
    
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
                echo "Saliendo del programa\n";
                exit;
            default:
                echo "Inténtelo de nuevo.\n";
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
        $agenda = array_values($agenda);
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
_end();

?>