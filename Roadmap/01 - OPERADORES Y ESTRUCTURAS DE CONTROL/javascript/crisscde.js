// * MARK: OPERADORES
/* Operadores de Asignación  */
let myNumber = 5; // => Assigment Operator
console.log(myNumber) // => 5

// Operadores de Asignacion Aritmética
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
myNumber >>>= 3; // => myNumber >>> 3 -> 32768 >>> 3 -> 001000000000000 >>> 3 
console.log(myNumber) // => 4096
console.log(myNumber.toString(2)); // => 1000000000000

// Operadores de Asignación Bit a Bit
let myNumber2 = 9321; /// => Binary => 10010001101001
myNumber2 &= 7982; // => myNumber2 & 7982 -> 9321 & 7982 -> 10010001101001 & 01111100101110 
console.log(myNumber2); // => 1064
console.log(myNumber2.toString(2)); // => 10000101000
myNumber2 ^= 1840; // => myNumber2 ^ 1840 -> 1064 ^ 1840 -> 10000101000 ^ 11100110000
console.log(myNumber2); // => 792
console.log(myNumber2.toString(2)); // => 1100011000
myNumber2 |= 974; // => myNumber2 | 974 -> 792 | 974 -> 1100011000 | 1111001110
console.log(myNumber2); // => 990
console.log(myNumber2.toString(2)); // => 1111011110

// Operadores de Asignación Lógicos
let canGoToNightClub = true;
let haveId = false;
canGoToNightClub &&= haveId; // => canGoToNightClub && haveId -> true && false
console.log(canGoToNightClub) // => false

let notValue = "";
notValue ||= "defaultValue";
console.log(notValue);

let user = null;
user ??= {userID: 1, username: "GuestUser"} // => (user === null || user === undefined) ? {userID: 1, username: "GuestUser"} : user;
console.log(user);