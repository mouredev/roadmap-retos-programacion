<?php


/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */


//Operadores aritméticos

print ("Suma: 5 + 2 = " . (5 + 2));
print ("Resta: 5 - 2 = " . (5 - 2));
print ("Multiplicación: 5 * 2 = " . (5 * 2));
print ("División: 5 / 2 = " . (5 / 2));
print ("Módulo: 5 % 2 = " . (5 % 2));
print ("Exponenciación: 5 ** 2 = " . (5 ** 2));
print ("División entera: 5 // 2 = " . (ROUND(5 / 2)));

//Operadores de comparación

print("Igualdad: 5 == 2 = " . (5 == 2));
print("Desigualdad: 5 != 2 = " . (5 != 2));
print("Mayor que: 5 > 2 = " . (5 > 2));
print("Menor que: 5 < 2 = " . (5 < 2));
print("Mayor o igual que: 5 >= 2 = " . (5 >= 2));
print ("Menor o igual que: 5 <= 2 = " . (5 <= 2));

//Operadores lógicos

print("AND: 5 == 5 && 2 == 2 = " . (5 == 5 && 2 == 2));
print("OR: 5 == 5 || 2 == 3 = " . (5 == 5 || 2 == 3));
print("NOT: !(5 == 5) = " . !(5 == 5));

//Operadores de asignación

$variable = 5;
print("Asignación: variable = 5 = " . $variable);
$variable += 2;
print("Suma: variable += 2 = " . $variable);
$variable -= 2;
print("Resta: variable -= 2 = " . $variable);
$variable *= 2;
print("Multiplicación: variable *= 2 = " . $variable);
$variable /= 2;
print("División: variable /= 2 = " . $variable);
$variable %= 2;
print("Módulo: variable %= 2 = " . $variable);
$variable **= 2;
print("Exponenciación: variable **= 2 = " . $variable);

//Operadores de identidad
$number = 5;
print ($number is $my_number);


//Operadores de pertenencia
$numbers = array(1, 2, 3, 4, 5);
print (3 in $numbers);

//Operadores de bits
print("AND: 5 & 2 = " . (5 & 2));
print("OR: 5 | 2 = " . (5 | 2));
print("XOR: 5 ^ 2 = " . (5 ^ 2));
print("Desplazamiento a la izquierda: 5 << 2 = " . (5 << 2));
print("Desplazamiento a la derecha: 5 >> 2 = " . (5 >> 2));
print("Negación: ~5 = " . (~5));


//Estructura de control 

//condicional
$number = 5;
if($number == 5){
    print("El número es 5");
} else {
    print("El número no es 5");
}

$string = "Hola";

switch($string){
    case "Hola":
        print("Hola");
        break;
    case "Adiós":
        print("Adiós");
        break;
    default:
        print("No es ni Hola ni Adiós");
}

//iterativa
for($i = 10; $i <= 55; $i++){
    if($i % 2 == 0 && $i != 16 && $i % 3 != 0){
        print($i);
    }
}

//Manejador de excepciones
try {
    if (0 == 0) {
        throw new Exception("División por cero");
    }
    print (10 / 0);
} catch (Exception $e) {
    print($e->getMessage());
}


