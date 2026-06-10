<?php
// --------------------------------------------------
// TIPOS DE OPERADORES
// --------------------------------------------------

#### ARITMÉTICOS ####

print("OPERADORES ARITMÉTICOS\n");

$cats = 6;
$dogs = 3;

// Suma
$animals = $cats + $dogs;
echo "Hay " . ($animals) . " animales en total\n";

// Resta
$animals = $cats - $dogs;
echo "Hay " . ($animals) . " gato más que perros\n";

// Multiplicación
$animals = $cats * $dogs;
echo "Si cada gato fuese dueño de " . ($dogs) . " perros, habría " . ($animals) . " perros en total\n";

// División
$animals = $cats / $dogs;
echo "Si repartimos a los perros entre los gatos, cada gato tendría " . ($animals) . " perros\n";

// Módulo (Resto de la división)
$animals = $cats % $dogs;
echo "Si repartimos a los gatos entre los perros, sobrarían " . ($animals) . " gatos\n";

// Exponenciación
$animals = $cats ** $dogs;
echo "Tenemos " . ($cats) . " gatos. Cada uno tiene " . ($cats) . " vidas. Todos los gatos en conjunto tienen " . ($animals) . " vidas\n\n";


#### ASIGNACIÓN ####

print("OPERADORES DE ASIGNACIÓN\n");

// Asignación con suma
$points = 8;
$points += 4;
echo "Puntos: " . ($points) . "\n";

// Asignación con resta
$points = 8;
$points -= 6;
echo "Puntos: " . ($points) . "\n";

// Asignación con multiplicación
$points = 8;
$points *= 2;
echo "Puntos: " . ($points) . "\n";

// Asignación con división
$points = 8;
$points /= 4;
echo "Puntos: " . ($points) . "\n";

// Asignación con módulo
$points = 8;
$points %= 5;
echo "Puntos: " . ($points) . "\n";

// Asignación con exponenciación
$points = 8;
$points **= 2;
echo "Puntos: " . ($points) . "\n";

// Asignación y concatenación
$shopping_list = "Mi lista: ";
$shopping_list .= "- Huevos";
$shopping_list .= "- Naranjas";
$shopping_list .= "- Sandía\n";
echo $shopping_list . "\n";


#### COMPARACIÓN ####

print("OPERADORES DE COMPARACIÓN\n");

$a = 3;
$b = 7;
$c = "3";

// Igual ==
if ($a == $b) {
    echo "a y b son iguales\n";
} else {
    echo "a y b no son iguales\n";
}

// Idéntico ===
if ($a === $c) {
    echo "a y c son iguales y del mismo tipo\n";
} else {
    echo "a y c no son iguales y/o no son del mismo tipo\n";
}

// Diferente != o <>
if ($a != $b) {
    echo "a y b son diferentes\n";
} else {
    echo "a y b no son diferentes\n";
}

// No idéntico !==
if ($a !== $c) {
    echo "a y c son diferentes y/o no son del mismo tipo\n";
} else {
    echo "a y c no son diferentes y son del mismo tipo\n";
}

// Mayor que >
if ($a > $b) {
    echo "a es mayor que b\n";
} else {
    echo "a no es mayor que b\n";
}

// Menor que <
if ($a < $b) {
    echo "a es menor que b\n";
} else {
    echo "a no es menor que b\n";
}

// Mayor o igual que >=
if ($a >= $b) {
    echo "a es mayor o igual que b\n";
} else {
    echo "a no es mayor o igualque b\n";
}

// Menor o igual que <=
if ($a <= $b) {
    echo "a es menor o igual que b\n";
} else {
    echo "a no es menor o igual que b\n";
}

// Combinado: Nave espacial <=>
$result = $a <=> $b;
echo "Resultado de a <=> b: " . ($result) . "\n\n";


#### INCREMENTO Y DECREMENTO ####

print("OPERADORES DE INCREMENTO Y DECREMENTO\n");

// Pre-incremento
$x = 5;
echo "Pre-incremento: " . (++$x) . "\n";

// Post-incremento
$y = 5;
echo "Post-incremento: " . ($y++) . "\n";
echo "Valor de y después del post-incremento: " . ($y) . "\n";

// Pre-decremento
$x = 5;
echo "Pre-decremento: " . (--$x) . "\n";

// Post-decremento
$y = 5;
echo "Post-decremento: " . ($y--) . "\n";
echo "Valor de y después del post-decremento: " . ($y) . "\n\n";


#### LÓGICOS ####

print("OPERADORES LÓGICOS\n");

// AND &&
$age = 35;
$has_license = true;

if ($age >= 18 && $has_license) {
    echo "Puedes conducir\n";
} else {
    echo "No puedes conducir\n";
}

// OR ||
$cat_person = true;
$dog_person = false;

if ($cat_person || $dog_person) {
    echo "Te gustan los animales\n";
} else {
    echo "No te gustan los animales\n";
}

// XOR XOR
$likes_cats = true;
$likes_dogs = true;

if ($likes_cats XOR $likes_dogs) {
    echo "Te gusta un tipo de animal\n";
} else {
    echo "Te gustan ambos tipos de animales o ninguno\n";
}

// NOT !
$its_raining = false;
if (!$its_raining) {
    echo "No está lloviendo\n\n";
} else {
    echo "Está lloviendo\n\n";
}


#### ARRAYS ####

print("OPERADORES DE ARRAYS\n");

// Unión de arrays + 
// Si hay claves repetidas, se mantiene el valor del primer array, ignorando el valor del segundo array.

$names_1 = array('a' => "María", 'b' => "Marta", 'c' => "Angeles");
$names_2 = array('c' => "Diego", 'd' => "Francisco", 'a' => "José"); 
$names = $names_1 + $names_2;
var_dump($names);

// Igualdad de arrays ==
$array_1 = array(1 => "uno", 2 => "dos", 3 => "tres");
$array_2 = array(3 => "tres", 2 => "dos", 1 => "uno");
if ($array_1 == $array_2) {
    echo "\nLos arrays son iguales\n";
}

// Identidad de arrays ===
$array_1 = array(1 => "uno", 2 => "dos", 3 => "tres");
$array_2 = array(1 => "uno", 2 => "dos", 3 => "tres");
if ($array_1 === $array_2) {
    echo "\nLos arrays son idénticos\n";
}

// Desigualdad de arrays !=
$a = array(1 => "uno", 2 => "dos", 3 => "tres");
$b = array(4 => "cuatro", 5 => "cinco");
if ($a != $b) {
    echo "\nLos arrays son diferentes\n";
}

// No identidad de arrays !==
$a = array(1 => "uno", 2 => "dos", 3 => "tres");
$b = array(3 => "tres", 2 => "dos", 1 => "uno");
if ($a !== $b) {
    echo "\nLos arrays no son idénticos\n";
}


#### CONDICIONALES ESPECIALES ####

print("\nOPERADORES DE CONDICIONALES ESPECIALES\n");

// Ternario ?: Es un if / else en una linea. La sintaxis es: condición ? valor_si_verdadero : valor_si_falso
$score = 67;
$result = ($score >= 50) ? "Aprobado" : "Suspenso";
echo "Resultado: " . ($result) . "\n";

// Fusión de null ?? Devuelve el primer operando si no es null, si es null, devuelve el segundo.
$animal = $_POST['animal'] ?? 'Ningún animal seleccionado';
echo "Animal seleccionado: " . ($animal) . "\n";


#### BITS ####

print("\nOPERADORES DE BITS\n");

$a = 5; // En binario: 0101
$b = 3; // En binario: 0011

// AND & (El bit resultante es 1 solo si ambos bits son 1)
$result = $a & $b; // Resultado en binario: 0001    
echo "AND: " . ($result) . "\n";

// OR | (el bit resultante es 1 si al menos uno de los bits es 1)
$result = $a | $b; // Resultado en binario: 0111    
echo "OR: " . ($result) . "\n";

// XOR ^ (el bit resultante es 1 si los bits son diferentes)
$result = $a ^ $b; // Resultado en binario: 0110    
echo "XOR: " . ($result) . "\n";

// NOT ~ (el bit resultante es el contrario al original, 0 se convierte en 1 y 1 se convierte en 0)
$a = 5; // En binario: 0101
$result = ~$a; // Resultado en binario: 1010    
echo "NOT: " . ($result) . "\n";

// Desplazamiento a la izquierda << (desplaza los bits a la izquierda, agregando ceros a la derecha)
$a = 5; // En binario: 0101
$result = $a << 1; // Resultado en binario: 1010    
echo "Desplazamiento a la izquierda: " . ($result) . "\n";

// Desplazamiento a la derecha >> (desplaza los bits a la derecha, eliminando los bits de la derecha)
$a = 5; // En binario: 0101
$result = $a >> 1; // Resultado en binario: 0010
echo "Desplazamiento a la derecha: " . ($result) . "\n";


#### EJECUCIÓN ####

print("\nOPERADORES DE EJECUCIÓN\n");

// El operador de ejecución `` ejecuta el comando dentro de las comillas y devuelve la salida como una cadena.
$user_system = `whoami`;
echo "El servidor PHP está ejecutándose con el user: " . ($user_system) . "\n";


#### DE TIPO ####

print("OPERADORES DE TIPO\n");

// instanceof (verifica si un objeto es una instancia de una clase específica)
$actual_date = new DateTime();

if ($actual_date instanceof DateTime) {
    echo "actual_date es una instancia de la clase DateTime\n";
} else { 
    echo "actual_date no es una instancia de la clase DateTime\n"; 
    }



// --------------------------------------------------
// ESTRUCTURAS DE CONTROL - CONDICIONALES
// --------------------------------------------------

#### IF - ELSE - ELSEIF ####

print("\n\nIF - ELSE - ELSEIF\n");

$traffic_light = "ámbar";

if ($traffic_light === "verde") {
    echo "Puedes seguir avanzando\n";
} elseif ($traffic_light === "ámbar") {
    echo "Ve frenando, puede cambiar a rojo pronto\n";
} else {
    echo "Debes parar!\n";
}


#### SWITCH ####

print("\nSWITCH\n");

$temperature = 26;

switch (true) {
    case ($temperature <= 0):
        echo "Más frío que en la comunión de Pingu\n";
        break;
    
    case ($temperature > 0 && $temperature <= 15):
        echo "Llevate una rebequia, que refresca\n";
        break;
    
    case ($temperature > 15 && $temperature <= 25):
        echo "Se comienza a estar bien en una terracita al sol\n";
        break;
    
    default:
        echo "Día de playa!\n";
        break;
       
}

#### MATCH #### (A partir de PHP 8.0)

print("\nMATCH\n");

$password = "12345";

$result = match (true) {
    strlen($password) < 6 => "Error: La contraseña debe tener más de 6 caracteres.",
    !preg_match('/[a-zA-Z]/', $password) => "Error: La contraseña debe contener al menos una letra.",
    !preg_match('/[0-9]/', $password) => "Error: La contraseña debe contener al menos un número.",
    default => "Contraseña válida." 
};
echo $result . "\n";


// --------------------------------------------------
// ESTRUCTURAS DE CONTROL - BUCLES
// --------------------------------------------------

#### WHILE ####

print("\nWHILE\n");

$countdown = 5;

while ($countdown >= 1) {
    echo "Lanzamiento en: " . $countdown . "\n";
    $countdown--;
}
echo "DESPEGAMOS!!\n";


#### DO-WHILE ####

print("\nDO-WHILE\n");

$attempts = 0;

do {
    echo "Intentando conectar a la base de datos... (Intento " . ($attempts + 1) . ")\n";
    $attempts++;
} while ($attempts < 3);


#### FOR ####

print("\nFOR\n");
// (Inicio ; Condición ; Incremento/Decremento)
for ($progress = 0; $progress <= 100; $progress += 20) {
    echo "Descargando actualización: " . $progress . "%\n";
}
echo "Descarga completada con éxito!\n";


#### FOREACH ####

print("\nFOREACH\n"); // Para arrays

$tasks = [
    "mañana" => "trabajar.",
    "tarde" => "estudiar PHP.",
    "noche" => "jugar y descansar."
];

foreach ($tasks as $moment => $description){
    echo "Por la $moment tengo que: $description\n";
}


// --------------------------------------------------
// ESTRUCTURAS DE CONTROL - SALTOS DE FLUJO
// --------------------------------------------------

#### CONTINUE ####

print("\nCONTINUE\n"); //Salta una iteración

$users = [
    "María" => "activo",
    "Jose" => "inactivo",
    "Estefania" => "activo"
];

foreach ($users as $name => $status) {
    if ($status == "inactivo") {
        continue;
    }
    echo "Los usuarios activos son: $name \n";
}


#### BREAK ####

print("\nBREAK\n");

for ($attempt = 1; $attempt <= 5; $attempt++) {
    echo "Intento fallido número $attempt\n";

    if ($attempt == 3) {
        echo "Demasiados errores. ¡Cuenta bloqueada!\n";
        break;
    }
}


// --------------------------------------------------
// ESTRUCTURAS DE CONTROL - EXCEPCIONES
// --------------------------------------------------

#### TRY - CATCH - FINALLY ####

print("\nTRY - CATCH - FINALLY\n");

try {
    $admitted_cats = 3;
    $current_cats = 6;

    if ($current_cats > $admitted_cats) {
        throw new Exception("Alerta: Demasiados gatos, no podemos acariciarlos a todos");
    }
    echo "Todo bajo control en la Casa de los Gatos\n";

} catch (Exception $e) {
    echo "Error capturado: " . $e->getMessage() . "\n";

} finally { 
    echo "Proceso de revisión finalizado\n";
}


// --------------------------------------------------
// ###### ---- EXTRA ---- ######
// --------------------------------------------------

/* 
    Crea un programa que imprima por consola todos
    los números comprendidos entre 10 y 55 (incluidos),
    pares, y que no son ni el 16 ni múltiplos de 3.

*/


for ($numbers = 10; $numbers <= 55; $numbers++) {
        
    if ($numbers % 2 === 0 && $numbers != 16 && $numbers % 3 !== 0) {
        echo "$numbers\n"; 
    }

}