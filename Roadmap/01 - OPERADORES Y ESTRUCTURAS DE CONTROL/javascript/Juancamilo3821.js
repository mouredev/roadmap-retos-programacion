//Operadores Js//
/*Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)*/

//Operadores Aritmeticos//
//operador de asignacion//
let n = 4
let z = 88

let k = 10;
k += 5;
k -= 2; 
k *= 3;
k /= 3;
k %= 5;
console.log("k:", k);

console.log( `Suma:     ${n} + ${z} = ${ n + z }` );
console.log( `Resta:     ${n} - ${z} = ${ n - z }` );
console.log( `Multiplicacion:     ${n} * ${z} = ${ n * z }` );
console.log( `Division:     ${n} / ${z} = ${ n / z }` );
console.log( `Residuo:     ${n} % ${z} = ${ n % z }` );
console.log( `Exponenciacion:     ${n} ** ${z} = ${ n ** z }` );

//Suma de cadenas//
let firstName = "Juan Camilo ";
let lastName = "Gomez Armenta";

let fullName = firstName + lastName;

console.log(fullName)

//Suma de Cadenas y numeros//
let nom = "Juan";
let number = 5;
let concat = "6" + 7;
let x = "hola" + 33;


console.log(number)
console.log(nom)
console.log(concat)
console.log(nom, concat)
console.log(x)

//Operadores Logicos//

let a = 6;
let b = 3;
let c = (a < 10 && b > 0 );
let d = (a < 10 || b < 0);
let e = (5 == 8);
let f = !(5 == 8);


let hablar = null;
let talk = "missing";
let result = hablar ?? talk;


console.log(c)
console.log(d)
console.log(e)
console.log(f)
console.log(result)

//Operadores de Comparacion//
let yz = (10 == 3)
console.log("10 == 3 es", yz)

let yx = (10 != 3)
console.log("10 != 3 es", yx)

let yy = (10 > 3 )
console.log("10 > 3 es", yy)

let ya = (10 < 3 )
console.log("10 < 3 es", ya)

let yb = (10 >= 3 )
console.log("10 >= 3 es", yb)

let yc = (10 <= 3 )
console.log("10 <= 3 es", yc)

//Operadores de Identidad//
// Identidad (===)
let n1 = 44;
let n2 = 44;
console.log("n1 === n2:", n1 === n2); // true (primitivos por valor)

let obj1 = { valor: 44 };
let obj2 = { valor: 44 };
console.log("obj1 === obj2:", obj1 === obj2); // false (objetos por referencia)

let obj3 = obj1;
console.log("obj3 === obj1:", obj3 === obj1); // true



// Operadores de pertenencia
const obj = { valor: 44 };
console.log("'valor' in obj:", 'valor' in obj); // true

const arr = [1, 2, 3];
console.log("arr includes 2:", arr.includes(2)); // true (no es operador, pero es pertenencia práctica)

console.log("arr instanceof Array:", arr instanceof Array); // true


//Operadores bit a bit
//AND a nivel de bits
let j = (11 & 12);
console.log("esto es j: ", j)

//OR a nivel de bits
let l = (11 | 12);
console.log("esto es l: ", l)

//XOR a nivel de bits
let m = (11 ^ 12);
console.log("esto es m: ", m)

//NOT a nivel de bits
let o = ~11;
console.log("esto es o: ", o)

//Desplazamiento a la izquierda
let p = (11 << 12);
console.log("esto es p: ", p)

//Desplazamiento a la derecha de propagación de signo
let q = (11 >> 12);
console.log("esto es q: ", q)

//Desplazamiento a la derecha de relleno cero
let r = (11 >>> 12);
console.log("esto es r: ", r)


/*Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...*/

//Estructuras de control
//Condicionales 
//if/else

let nota = 70;
    if (nota < 80) {
        console.log("No aprobo");
    } else {
        console.log("Aprobo")
    }

let edad = 17;

    if(edad < 18 ) console.log("Menor");
    else if (edad < 65) console.log("Adulto");
    else console.log("Abuelo");

let dia = 4;

switch (dia) {
    case 1: console.log("Lunes"); break;
    case 2: console.log("Martes"); break;
    case 3: console.log("Miercoles"); break;
    default: console.log("Otro");
}

//Iterativas(Bucles)

for (let i = 1; i <= 10; i++){
    console.log("for i=", i)
}

let i = 1;
while (i<=10){
    console.log("while i =", i);
    i++;
}

let s = 1;
do {
  console.log("do-while s =", s);
  s++;
} while (s <= 3);

//Excepciones/Try/Catch/Finally

try {
  let x = JSON.parse("esto no es json");
  console.log(x);
} catch (error) {
  console.log("Error atrapado:", error.message);
} finally {
  console.log("Esto siempre se ejecuta");
}