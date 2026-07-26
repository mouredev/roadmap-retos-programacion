<?php
// Creación e interpolación ( Unir variables dentro de texto )
echo "Creación e interpolación ( Unir variables dentro de texto )\n";
$nombre = "Salvador";
echo "\n";


// Interpolación, se requiere colas dobles.
echo "Interpolación, se requiere colas dobles.\n";
$presentacion ="Hola, mi nombre es $nombre\n";
echo $presentacion;
echo "\n";


// Con comillas simple NO interpola.
echo "Con comillas simple NO interpola.\n";
$literal = 'Hola, mi nombre es $nombre\n';
echo $literal;
echo "\n";


// Concatenación y repetición
echo "Concatenación y repetición\n";
$texto1 = "Hola";
$texto2 = "Mundo";
echo "\n";


// Concatenación básica.
echo "Concatenación básica.\n";
$union = $texto1 . $texto2 . "\n";
echo $union;
echo "\n";


// Concatenación con asignación (.=).
echo "Concatenación con asignación (.=).\n";
$frase = "Programar en ";
$frase .= "PHP es la polla.\n";
echo $frase;
echo "\n";


// Repetición
echo "Repetición\n";
$linea_separadora = str_repeat("-",100);
echo $linea_separadora;
echo "\n";


//Longitud y acceso a caracteres específicos.
echo "Longitud y acceso a caracteres específicos.\n";
$cadena = "Tecnologias";
echo "\n";


// Longitud
echo "Longitud\n";
echo "El texto $cadena tiene " . strlen($cadena) . " letras.";
echo "\n";


// Acceso por posición.
echo "Acceso por posición.\n";
echo $cadena[0]; 
echo "\n";
echo $cadena[8];
echo "\n";


// Extracción de subcadenas( trocea texto )
echo "Extracción de subcadenas( trocea texto )\n";
$texto_completo = "Desarrollando páginas web";
echo "\n";


 // Extraigo desde la posición 0 a la 15.
echo "Extraigo desde la posición 0 a la 15.\n";
 $subcadena1 = substr($texto_completo,0,14);
 $subcadena2 = substr($texto_completo,14);


 echo $texto_completo . "\n";
 echo $subcadena1 . "\n";
 echo $subcadena2 . "\n";
echo "\n";


// Conversión a Mayúsculas y a Minúsculas.
echo "Conversión a Mayúsculas y a Minúsculas.\n";
$mi_texto = "Hola PHP";
$mayusculas = strtoupper($mi_texto);
$minusculas = strtolower($mi_texto);

echo "Mayúsculas $mayusculas";
echo "\n";
echo "Minúsculas $minusculas";
echo "\n";


// Solo la primera letra
echo "Solo la primera letra\n";
$primera_letra = ucfirst("php");
echo "\n";


// La primera letra de cada palabra.
echo "La primera letra de cada palabra.\n";
$titulo = ucwords("diseño web");

echo $primera_letra;
echo "\n";
echo $titulo;
echo "\n";


// Reemplazo de texto
echo "Reemplazo de texto\n";
$plantilla = "Bienvenido al curso de Javascript\n";
$corregido = str_replace("Javascript","PHP",$plantilla);
echo $plantilla;
echo "\n";
echo $corregido;
echo "\n";


// Convertir texto en array.
echo "Convertir texto en array.\n";
$lista_tecnologia = "PHP,Java,HTML\n";
$array_tecnologia = explode(",",$lista_tecnologia);
echo "\n";
foreach($array_tecnologia as $tecnologia) {
    echo $tecnologia . "\n";
}
echo "\n";


// convertir de array a texto.
echo "convertir de array a texto.\n";
$nombres = ["Salvador","Marcos","María"];
$texto_nombres = implode("-", $nombres);
echo "\n";
echo $texto_nombres ."\n";
echo "\n";


// Recorrido de una cadena.
echo "Recorrido de una cadena.\n";
$palabra = "PHP";
for ($i = 0; $i < strlen($palabra); $i++) {
    echo "Letra " . ($i + 1) . ":" . $palabra[$i] . "\n";
}
echo "\n";


// Verificación y búsqueda
echo "Verificación y búsqueda\n";
$correo = "salvador@ejemplo.com";
echo "\n";


// ¿Contiene una palabra?
echo "¿Contiene una palabra?\n";
if (str_contains($correo, "@")) {
    echo "Es un correo válido\n";
}
echo "\n";


// ¿Empieza por ...?
echo "¿Empieza por ...?\n";
$url = "https://acerogourmet.es";
    if(str_starts_with($url, "https")) {
    echo "Es una conexión segura\n";
}
echo "\n";


// ¿Termina en ...?
echo "¿Termina en ...?\n";
$archivo = "SalvadorCalero.php";
if(str_ends_with($archivo, "php")) {
    echo "Es un script de PHP\n";
}
echo "\n";


// Limpieza de espacios en blanco.
echo "Limpieza de espacios en blanco.\n";
$entrada_sucia = "  mi_usuario_  ";
$entrada_limpia = trim($entrada_sucia);

echo $entrada_sucia . "\n";
echo $entrada_limpia . "\n";

$limpiar_izquierda = ltrim ($entrada_sucia);
$limpiar_derecha = rtrim($entrada_sucia);
echo $limpiar_izquierda . "\n";
echo $limpiar_derecha . "\n";
echo "\n";


/**
 * Ejercicio Extra
 */


// Pedimos al usuario dos palabras para ser analizadas.
$palabraA = strtolower(trim(readline("Introduce la primera palabra: "))); 
$palabraB = strtolower(trim(readline("Introduce la segunda palabra: ")));

// Evitamos el problema de las tildes
$buscar = ["á","é","í","ó","ú"]; 
$reemplazar = ["a","e","i","o","u"];

// Reemplazamos el contenido de las variables por texto normalizado, minúsculas y sin tildes
$palabraA = str_replace($buscar, $reemplazar, $palabraA);
$palabraB = str_replace($buscar, $reemplazar, $palabraB);

function validarLetras($palabraA, $palabraB) {

    // Valifamos que el texto sólo contenga letras y no números
    if(preg_match("/^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$/", $palabraA)&&preg_match("/^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$/", $palabraB)) {
        return true; // Contiene solo letras
    }else {
        return false; // Contiene números, espacios o símbolos.
    }
}

// ¿Son palíndromos las dos palabras?



// Comparamos las dos palabras para saber ci son palíndromos.
function palindromos($palabraA, $palabraB) {
    $espejo_palabraA = strrev($palabraA); // Con strrev() le damos la vuelta a las palabras como si fuera un espejo.
    $espejo_palabraB = strrev($palabraB);

    if ($palabraA === $espejo_palabraA) {
        echo "La palabra $palabraA es palíndromo.\n";
    }else{
        echo "La palabra $palabraA no es palíndromo\n";
    }
    if ($palabraB === $espejo_palabraB) {
        echo "La palabra $palabraB es palíndromo.\n";
    }else {
        echo "La palabra $palabraB no es palíndromo\n";
    }
}

function anagramas($palabraA, $palabraB) {
    $arrayA = str_split($palabraA);
    sort ($arrayA);
    $ordenadaA = implode($arrayA);

    $arrayB = str_split($palabraB);
    sort ($arrayB);
    $ordenadaB = implode($arrayB);

    if ($ordenadaA === $ordenadaB) {
        echo "La palabra $palabraA y la palabra $palabraB son anagramas\n";
    }else {
        echo "La palabra $palabraA y la palabra $palabraB NO son anagramas\n";
    }
}

function isograma($palabraA, $palabraB) {
    $longitudA = strlen($palabraA);
    $arrayA = str_split($palabraA);
    $arrayA_noRepetidos = array_unique($arrayA);

    $longitudB = strlen($palabraB);
    $arrayB = str_split($palabraB);
    $arrayB_noRepetidos = array_unique($arrayB);

    if ($longitudA === count($arrayA_noRepetidos)){
        echo "La palabra $palabraA es isograma\n";
    }else {
        echo "La palabra $palabraA NO es isograma\n";
    }

    if ($longitudB === count($arrayB_noRepetidos)){
        echo "La palabra $palabraB es isograma\n";
    }else {
        echo "La palabra $palabraB NO es isograma\n";
    }

}






if(!validarLetras($palabraA, $palabraB)) {
    echo "Error. Sólo se aceptan letras\n";
}else {
    echo "\n";
    palindromos($palabraA, $palabraB);
    echo "\n";
    anagramas($palabraA, $palabraB);
    echo "\n";
    isograma($palabraA, $palabraB);
}


