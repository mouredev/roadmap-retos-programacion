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
