# 01 OPERADORES Y ESTRUCTURAS DE CONTROL
#maussho

<?php

// 1. Crea ejemplos utilizando todos los tipos de operadors de tu lenguaje

# Operadores aritmeticos
# Valores 
$num1 = 14;
$num2 = 2;

# Suma
print "--Suma--" ."\n";
$suma = $num1 + $num2;
echo $suma ."\n";

# Resta
print "--Resta--" ."\n";
$resta = $num1 - $num2;
echo $resta ."\n";

# Multiplicación
print "--Multiplicación--" ."\n";
$multi = $num1 * $num2;
echo $multi ."\n";

# División
print "--División--" ."\n";
echo $num1 / $num2 ."\n";

# Modulo o Residuo
print "--Modulo o Residuo--" ."\n";
echo $num1 % $num2 ."\n";

# Operadores de asignación
# =
print "--Igual--" ."\n";
$valor1 = 10;
$valor2 = 9;

# Incremento
print "--Incremento--" ."\n";
$valor1 += 2;

echo $valor1 ."\n";

# decremento
print "--Decremento--" ."\n";
$valor2 -= 2;

echo $valor2 ."\n";

# Concatenación
print "--Concatenación--" ."\n";
$texto2 = "Hola";
$texto2 .= " mundo";
print $texto2 ."\n";

# Asignación por referencia
$a = 4;
$b = $a;
// echo $b ."\n"

# Operadores lógicos
print "--Operadores lógicos--" ."\n";
# and
$ab = true;
$ac = false;
if ($ab && $ab) {
    echo "true" ."\n";
}
if($ab && $ac){

}else{
    echo "false" ."\n";
}
# or
if ($ab || $ab) {
    echo "true" ."\n";
}
if($ab || $ac){
    echo "true" ."\n";
}

$a10 = 4;
if ($a10<5) {
    echo $a10 ."\n";
}


#Condicionales
print "--Condicionales--" ."\n";
$name = "mauri";
echo $name ."\n";

#Iterativas
print "--Iterativas--" ."\n";
# Ciclo For
for ($i=0; $i < 10; $i++) { 
    echo $i ."\n";
}

# Ciclo ForEach
$array = [1, 2, 3];
foreach ($array as $clave => $value) {
    echo $clave .- $value ."\n"; 
}

# Ciclo while
echo "Ciclo While" ."\n";
$i = 10;
while ($i <= 12) {
    echo $i ."\n";
    $i++;
}

# Dificultad Extra
echo "DIFICULTAD EXTRA" ."\n";
for ($i=10; $i<=55; $i++) { 
    if ($i % 2 == 0){
        if($i !== 16){
            if($i % 3 !== 0){
                echo $i ."\n";
            }
        }
        
    }
}

# Otra opción:
// for ($i=10; $i<=55; $i++) { 
//     if($i % 2 == 0 && $i !== 16 && $i % 3 !== 0){
//         echo $i . "\n";
//     }
// }
?>
