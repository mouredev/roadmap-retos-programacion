//Operadores

/*
Operadores aritméticos
*/

//Suma
let n1 = 10;
let n2 = 15;
let suma = n1 + n2;
console.log("La suma de", n1, "y", n2, "es:", suma);

//Resta
let n3 = 10;
let n4 = 15;
let resta = n3 - n4;
console.log("La resta de", n3, "y", n4, "es", resta);

//Multiplicación
let n5 = 10;
let n6 = 15;
let multiplicacion = n5 * n6;
console.log("La multiplicación de", n5, "y", n6, "es", multiplicacion);

//División
let n7 = 10;
let n8 = 15;
let division = n7 / n8;
console.log("La división de", n5, "y", n6, "es", division);

//Módulo
let n9 = 10;
let n10 = 15;
let modulo = n9 % n10;
console.log("El módulo de", n9, "y", n10, "es", modulo);

//Exponente
let n11 = 10;
let n12 = 15;
let exponente = n11 ** n12;
console.log("El exponente de", n11, "y", n12, "es", exponente);

//Incremento
let n13 = 10;
let incremento = ++n13;
console.log("El incremento de", n13, "es", incremento);

//Decremento
let n15 = 10;
let decremento = --n15;
console.log("El decremento de", n15, "es", decremento);



/*
Operadores de asignación
*/

let numero = 10;
console.log("Valor inicial:", numero);

//Asignación con suma
numero += 5;
console.log("Después de += 5:", numero); //15

//Asignación con resta
numero -= 3;
console.log("Después de -= 3:", numero); //12

//Asignación con multiplicación
numero *= 2;
console.log("Después de *= 2:", numero); //24

//Asignación con división
numero /= 4;
console.log("Después de /= 4:", numero); //6

//Asignación con módulo
numero %= 4;
console.log("Después de %= 4:", numero); //2

//Asignación con exponente
numero **= 3;
console.log("Después de **=3:", numero); //8

let a= 10;
let b = 5;
let c= "10";

console.log("a =", a, ", b =", b, ", c=", c);

//Igualdad (==) Compara valores sin importar el tipo
console.log("a == c:", a== c); //true

//Estrictamente igual (===) -> Compara valores y tipos de datos
console.log("a === c:", a === c); //false

//Desigualdad (!=) -> Compara valores sin importar el tipo
console.log("a != b:", b); //true

//Estrictamente desigual (!==) -> Compara valores y tipos de datos
console.log("a !== c:", a !== c); //true

//Mayor que (>) -> Compara si el valor de la izquierda es mayor que el de la derecha
console.log("a > b:", a > b); //true

//Menor que (<) -> Compara si el valor de la izquierda es menor que el de la derecha
console.log("a < b:", a < b); //false

//Mayor o igual que (>=) -> Compara si el valor de la izquierda es mayor o igual que el de la derecha
console.log("a >= 10:", a >= 10); //true

//Menor o igual que (<=) -> Compara si el valor de la izquierda es menor o igual que el de la derecha
console.log("b <= 5:",  b <= 5); //false


/* Operadores lógicos*/

let a1 = true;
let b1 = false;

console.log("a1 =", a,  ", b1 =", b1);

//AND lógico (&&) -> Devuelve true si ambos operandos son verdaderos
console.log("a && b:", a && b); //false

//OR lógico (||) -> Devuelve true si al menos uno de los operandos es verdadero
console.log("a || b:", a || b); //true

//OR lógico (!) Inverte el valor booleano
console.log("!a:", !a); //false
console.log("!b:", !b); //true

/*
&& devuelve true solo si ambas condiciones son true.

|| devuelve true si al menos una condición es true.

! invierte el valor (true se vuelve false y viceversa).
*/

/* Opereradores bit a bit */
let x = 5;  //  0101 en binario
let y = 3;  //  0011 en binario

console.log("x =", x, ", y =", y);

// AND bit a bit (&) -> Compara bit a bit y devuelve 1 solo si ambos bits son 1
console.log("x & y:", x & y);  // 1 (0001 en binario)

// OR bit a bit (|) -> Devuelve 1 si al menos un bit es 1
console.log("x | y:", x | y);  // 7 (0111 en binario)

// XOR bit a bit (^) -> Devuelve 1 si los bits son diferentes
console.log("x ^ y:", x ^ y);  // 6 (0110 en binario)

// Desplazamiento a la izquierda (<<) -> Mueve los bits a la izquierda y multiplica por 2
console.log("x << 1:", x << 1);  // 10 (1010 en binario)

// Desplazamiento a la derecha (>>) -> Mueve los bits a la derecha y divide por 2
console.log("x >> 1:", x >> 1);  // 2 (0010 en binario)

let valor = 10;

//Uso de if, else if y else

if ( valor > 10) {
    console.log("El número es mayor que 10.");

} else if (valor === 10) {
    console.log("El número es igual a 10.");

} else {
    console.log("El número es menor que 10.");
}

//Usando Switch

let operacion = "+";
switch (operacion) {
    case "+":
        console.log("Has elegido suma.");
        break;
    case "-":
        console.log("Has elegido resta.");
        break;
    default:
        console.log("Operación no válida.");
        break;
}


// For: Imprimir los primeros 5 múltiplos de 3

for (let i = 1; i <= 5; i++) {
    console.log('3 x $ {i} = $ (3 * i}');
}

// While: Contar hacia atrás desde 5
let contador = 5;
while (contador > 0) {
    console.log("Contador:", contador);
    contador--;
}

// Do-While: Se ejecuta al menos una vez

let n = 0;
do {
    console.log("Valor de n:", n);
    n++;
} while (n < 5);

// ForEach: Itera sobre los elementos de un array

let numeros = [2, 4, 6, 8];
numeros.forEach(num => console.log("Número:", num));

// Map: Crea un nuevo array con los números duplicados

let duplicados = numeros.map(num => num * 2);
console.log("Duplicados:", duplicados);


function dividir(a, b) {
    try {
        if (b === 0) throw "No se puede dividir entre 0";
        console.log('Resultado: ${a / b}');
    } catch (error) {
        console.log("Error:", error);
    } finally {
        console.log("Operación finalizada.");
    }

}

dividir(10, 2); //Correcto
dividir (10, 0); //Error

