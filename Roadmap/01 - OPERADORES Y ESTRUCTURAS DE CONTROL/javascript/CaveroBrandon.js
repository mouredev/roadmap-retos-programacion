/*
EJERCICIO:
 - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

// Arithmetics operators 
const first_num = 5;
const second_num = 6;

let sum = first_num + second_num;   // Addition
let subs = second_num - first_num;  // Substraction
let mul = first_num * second_num;   // Multiplication
let div = second_num / 2;           // Division
let rem = second_num % 2;           // Remainder

// Logical operators
const first_bool = true;
const second_bool = false;

let and_operator = first_bool && second_bool;   // AND
let or_operator = first_bool || second_bool;    // OR
let not_operator = !(first_bool);               // NOT

// Comparison operators, identity operators
let equal_to = first_bool == 5;                 // Equal to
let equal_value = first_bool === '5';           // Equal value
let not_equal = first_bool != 5;                // Not equal to
let not_equal_value = first_bool !== '5';       // Not equal value
let greater_than = first_bool > second_bool;    // Greater than
let less_than = first_bool < second_bool;       // Less than
let greater_or_equal = first_bool >= 5;         // Greater than or equal to
let less_or_equal = first_bool <= 5;            // Less than or equal to


// Assignment operators
let simple_assignment = 5;      // Simple assignment
let addition_assignment = 5;
addition_assignment += 10;      // Addition assignment
let substraction_assignment = 10;
substraction_assignment -= 5;   // Substraction assignment
let multiplication_assignment = 10;
multiplication_assignment *= 5; // Multiplication assignment
let exponential_assignment = 10;
exponential_assignment **= 2;   // Exponential assignment
let division_assignment = 10;
division_assignment /= 5;       // Division assignment
let remainder_operator = 10;
remainder_operator %= 2;        // Remainder assignment

// Bitwise operators
let and_bit_operator = first_bool & second_bool;    // And
let or_bit_operator = first_bool | second_bool;     // Or
let xor_bit_operator = first_bool ^ second_bool;    // Xor

let bit_const = 7
let zero_fill_left =  bit_const << 1;       // Zero fill left shift
let signed_right_shift = bit_const >> 1;    // Signed right shift

 /*
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
- Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
 */
console.log('*********** If ***********');
let condition = true;
if (condition) {
    console.log('The condition is "true" so this will be printed');
}
else if (condition == false) {
    console.log('This should be printed if the condition is "false"');
}
else if (condition == '0') {
    console.log('This condition should be printed if the value of condition is "0"');
}

console.log('*********** For ***********');
for (let i = 0; i < 5; i++) {
    console.log('Counting using a for loop: ' + i);
}

console.log('*********** While ***********');
let while_condition = 5;
while (while_condition > 0) {
    console.log('Counting using a while loop: ' + while_condition);
    while_condition -= 1;
}

console.log('*********** Try - Catch ***********');
try {
    nonExistingFunction();
}
catch (error) {
    console.error('This is being printed because of the error: '+ error)
}

 /*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

 for (i = 10; i < 56; i++) {
    if (! (i == 16 || i % 3 == 0) && (i % 2 == 0) || (i == 55)) {
        console.log(i)
    }
 }
 