// * MARK: OPERADORES
let myNumber = 5; // => Assignment Operator
console.log(myNumber) // -> 5

// ** MARK: Operadores de Asignacion Aritmética
myNumber += 15; // => myNumber + 15 -> 5 + 15
console.log(myNumber) // => 20
myNumber -= 4; // => myNumber - 4 -> 20 - 4
console.log(myNumber) // => 16
myNumber *= 8; // => myNumber * 8 -> 16 * 8
console.log(myNumber) // => 128
myNumber /= 4; // => myNumber / 4 -> 128 / 4
console.log(myNumber) // => 32
myNumber **= 4; // => myNumber ** 4 -> 32 ** 4 -> 32 * 32 * 32 * 32
console.log(myNumber) // => 1048576
myNumber <<= 1; // => myNumber << 1 ->  1048576 << 1 -> 100000000000000000000 << 1
console.log(myNumber) // => 2097152
console.log(myNumber.toString(2)) // => 1000000000000000000000
myNumber >>= 6; // => myNumber >> 6 -> 2097152 >> 6 -> 1000000000000000000000 >> 6
console.log(myNumber) // => 32768
console.log(myNumber.toString(2)) // => 1000000000000000
myNumber >>>= 3; // => myNumber >>> 3 -> 32768 >>> 3 -> 0001000000000000 >>> 3 
console.log(myNumber) // => 4096
console.log(myNumber.toString(2)); // -> 1000000000000

// ** MARK: Operadores de Asignación Bit a Bit
let myNumber2 = 9321; /// => 10010001101001

myNumber2 &= 7982; // => myNumber2 & 7982 -> 9321 & 7982 -> 10010001101001 & 01111100101110 
console.log(myNumber2); // => 1064
console.log(myNumber2.toString(2)); // => 10000101000

myNumber2 ^= 1840; // => myNumber2 ^ 1840 -> 1064 ^ 1840 -> 10000101000 ^ 11100110000
console.log(myNumber2); // => 792
console.log(myNumber2.toString(2)); // => 1100011000

myNumber2 |= 974; // => myNumber2 | 974 -> 792 | 974 -> 1100011000 | 1111001110
console.log(myNumber2); // => 990
console.log(myNumber2.toString(2)); // => 1111011110

/* 
  Antes de ver los operadores lógicos, me gustaria mencionar que los valores se manejan a base de
  booleanos, entonces todo valor es pasado a booleano, por ejemplo "false" es pasado a true, mientras que ""
  es pasado a false.
  A esto hay otra forma de llamarle, true se les trata también como Truthy y false como Falsy
    Valores Falsy
    Existen 9 valores Falsy:
      - null
      - undefined
      - false
      - NaN
      - 0
      - -0
      - 0n
      - ""
      - document.all
      ! Antes de continuar, debes de saber que null y undefined también se les llega a conocer como Nullish
    Todos los demas valores serán tratados como Truthy  
*/

// ** MARK: Operadores de Asignación Lógicos
let canGoToNightClub = true;
let isOlder = false;
canGoToNightClub &&= isOlder; // => canGoToNightClub && isOlder -> true && false
console.log(canGoToNightClub); // => false

let notValue = "";
notValue ||= "defaultValue"; // => "" || "defaultValue" => "" is Falsy, "defaultValue" is assigned
console.log(notValue); /// => "defaultValue"

let user = null;
user ??= {userID: 1, username: "GuestUser"} // => (user === null || user === undefined) ? {userID: 1, username: "GuestUser"} : user;
console.log(user); // => {userID: 1, username: "GuestUser"}

/* 
  ** MARK: Operadores de Comparación
  En JS comparar strings con números se puede hacer.
  Para evitar esto trata de usar los operadores de comparación estrictos (===, !==)
*/
console.log(`'20' == 20: ${ '20' == 20 }`); // => true - Permite coerción de tipos (LOOSE EQUALITY)
console.log(`'20' === 20: ${ '20' === 20 }`); // => false - No permite coerción de tipos (STRICT EQUALITY)

console.log(`'20' != 20: ${ '20' != 20 }`); // => false - Permite coerción de tipos (LOOSE EQUALITY)
console.log(`'20' !== 20: ${ '20' !== 20 }`); // => true - No permite coerción de tipos (STRICT EQUALITY)

console.log(`21 > 30: ${ 21 > 30 }`); // => false
console.log(`32 >= 30: ${ 32 >= 30 }`); // => true
console.log(`40 < 30: ${ 40 < 30 }`); // => false
console.log(`21 <= 21: ${ 21 <= 21 }`); // => true

// ** MARK: Operadores Aritméticos
console.log(`20 + 30: ${20 + 30}`); // => 20 + 30: 50
console.log(`20 - 7: ${20 - 7}`); // => 20 - 7: 13
console.log(`20 * 6: ${20 * 6}`); // => 20 * 6: 120
console.log(`20 / 8: ${20 / 8}`); // => 20 / 8: 2.5
console.log(`20 % 7: ${20 % 7}`); // => 20 % 7: 6
console.log(`20 ** 8: ${20 ** 8}`); // => 20 ** 8: 25600000000

// ** MARK: Operadores unarios
let myNumber3 = 12;
console.log(`++12: ${++myNumber3}`, `myNumber3: ${myNumber3}`); // => ++12: 13, myNumber3: 13
console.log(`13++: ${myNumber3++}`, `myNumber3: ${myNumber3}`); // => 13++: 13, myNumber3: 14
console.log(`--13: ${--myNumber3}`, `myNumber3: ${myNumber3}`); // => --14: 13, myNumber3: 13
console.log(`12--: ${myNumber3--}`, `myNumber3: ${myNumber3}`); // => 13--: 13, myNumber3: 12
console.log(`+false: ${+false}`); // +false: 0
console.log(`-('3'): ${-('3')}`); // -('3'): -3

/* 
  ** MARK: Operadores Bit a Bit
  Todo los operadores bit a bit (Bitwise Operators), tratan a los números a 32 bits
*/
console.log(`98 & 42: ${98 & 42}`) // => 1100010 & 0101010 -> 0100010 -> 34
console.log(`98 | 42: ${98 | 42}`) // => 1100010 | 0101010 -> 1101010 -> 106
console.log(`98 ^ 42: ${98 ^ 42}`) // => 1100010 ^ 0101010 -> 1001000 -> 72
console.log(`~98: ${~98}`) // => 1100010 -> 0011101 -> -99
console.log(`98 << 2`) // =>  392
console.log(`42 >> 2`) // => 10 
console.log(`42 >>> 2`) // => 10

// ** MARK: Operadores lógicos
console.log(`true && false: ${true && false}` ) // => false
console.log(`"" || [] || 0: ${"" || 0 || []}`) // => []
console.log(`null ?? []: ${null ?? []}`) // => []
console.log(`!false: ${!false}`) // => true

// ** MARK: Ternario (Operador Condicional)
let age = 22;
console.log(age >= 18 ? "Yes, he has an ID" : "No, he doesn't have an ID"); // => "Yes, he has an ID"
age = 12;
console.log(age >= 18 ? "Yes, he has an ID" : "No, he doesn't have an ID"); // => "No, he doesn't have an ID"


// * MARK: If...else
let number = 3;
if(number % 2 === 0) {
  console.log("Your number is even");
} else {
  console.log("Your number is odd");
}

// * MARK: If...If else...else
let value;
if((value === null) || (value === undefined)) {
  console.log("Nullish Value");
} else if( !value) {
    console.log("Falsy Value");
} else {
    console.log("Truthy Value");
}

// * MARK: Switch
let color = "Red";
switch(color) {
  case "Crimson":
    console.log("rgb(205, 92, 92)");
    break;
  case "HotPink":
    console.log("rgb(255, 105, 180)");
    break;
  case "Coral": 
    console.log("rgb(255, 127, 80)");
    break;
  case "LemonChiffon": 
    console.log("rgb(255, 250, 205)");
    break;
  case "RebeccaPurple": 
    console.log("rgb(102, 51, 153)");
    break;
  case "Olive": 
    console.log("rgb(128, 128, 0)");
    break;
  case "MediumSlateBlue": 
    console.log("rgb(123, 104, 238)");
    break;
  default: 
    console.log("rgb(0, 0, 0)");
}

/* 
  * MARK: Try...Catch (Excepciones)
  Algunas ocasiones observarás que un código ejecutado lanzara un error, esto si lo ejecuta el usuario
  ocasionara un grave error, para detener esto, deberás de ver ese error a tiempo y hacer algo para 
  notificar al usuario del error.
  Para hacer esto se lanza un try{} catch(error){}
*/

// * MARK: Try...Catch (Excepciones)
function divide(a, b) {
  if (b === 0) {
    // Throw an error
    throw new Error("You can't divide by zero!");
  }
  return a / b;
}

try {
  let result = divide(10, 0);
  console.log("Result: ", result);
} catch (error) {
  console.log("An error occurred: ", error.message);
} finally {
  console.log("Execution finished.");
}


// * MARK: For Loop
for ( let i = 1; i <= 10; i++ ) {
  console.log(i);
}

// * MARK: While Loop
let numberWhile = 1;
while ( numberWhile <= 10 ) {
  console.log(numberWhile);
  numberWhile++;
}

// * MARK:Do-While Loop
let numberDoWhile = 10;
do {
  console.log(numberDoWhile)
  numberDoWhile++;
} while(numberDoWhile <= 10);
console.log(numberDoWhile);


// * EXTRA
for(let i = 10; i <= 55; i++) {
  if((i % 2 === 0) && !(i % 3 === 0) && i != 16) {
    console.log(i);
  }
}
