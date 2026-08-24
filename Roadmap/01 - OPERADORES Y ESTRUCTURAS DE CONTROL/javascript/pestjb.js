//Operadores Aritméticos
let a = 35
console.log ("100 + 5670 es: ", 100 + 5670) //Suma
console.log(500 - 189) //Resta
console.log(456 * 24) //Multiplicación
console.log(79 / 6) //División
console.log(45 % 2) //Módulo
console.log(5 ** 2) //Exponenciación
console.log(a++) //Incremento
console.log(a--) //Decremento   

//Operadores de Comparación
let x = 100

console.log(x == 99) //Comparación de igualdad
console.log(x === 100) //Comparación de igualdad estricta
console.log(x != 10) //Comparación de desigualdad
console.log(x !== 100) //Comparación de desigualdad estricta
console.log(x > 50) //Mayor que
console.log(x < 200) //Menor que
console.log(x >= 100) //Mayor o igual que
console.log(x <= 99) //Menor o igual que

//Operadores Lógicos

let p = true
let q = false

console.log(p && q)// AND lógico, devuelve true si ambos operandos son verdaderos
console.log(p || q) // OR lógico, devuelve true si al menos uno de los operandos es verdadero
console.log(!p) // NOT lógico, devuelve el valor contrario del operando


//operadores de asignación

let y = 10 //Para asignar un valor a una variable se utiliza el operador de asignación (=)
y += 5 //Equivale a y = y + 5
console.log(y) //15
console.log(y -= 3) //Equivale a y = y - 3, resultado: 12
console.log(y *= 2) //Equivale a y = y * 2, resultado: 24
console.log(y /= 4) //Equivale a y = y / 4, resultado: 6
console.log(y **= 3) //Equivale a y = y ** 3, resultado: 216
console.log(y %= 5) //Equivale a y = y % 5, resultado: 1




// Identidad (typeof)
console.log(typeof 123);
console.log(typeof "hola");

// Pertenencia (in)
const obj = { nombre: "Juan", edad: 20 };
console.log("nombre" in obj);



// operadores de bit

let m = 6
let n = 7
console.log(m & n) //AND bit a bit, devuelve un número con los bits establecidos en 1 solo si ambos operandos tienen ese bit establecido en 1
console.log(m | n) //OR bit a bit, devuelve un número con los bits establecidos en 1 si al menos uno de los operandos tiene ese bit establecido en 1
console.log(m ^ n) //XOR bit a bit, devuelve un número con los bits establecidos en 1 solo si uno de los operandos tiene ese bit establecido en 1, pero no ambos
console.log(~m) //NOT bit a bit, devuelve un número con los bits invertidos del operando
console.log(m << 1) //Desplazamiento a la izquierda, desplaza los bits del operando hacia la izquierda un número especificado de posiciones
console.log(m >> 1) //Desplazamiento a la derecha, desplaza los bits del operando hacia la derecha un número especificado de posiciones
console.log(m >>> 1) //Desplazamiento a la derecha sin signo, desplaza los bits del operando hacia la derecha un número especificado de posiciones, llenando los bits vacíos con ceros

//ESTRUCTURAS DE CONTROL

//condicionales

let edad = 18


if(edad >= 18){
    console.log("puedes votar y conducir")  //if es una estructura de control que ejecuta un bloque de código si es verdadera
}
else if(edad < 18){
    console.log("no puedes votar ni conducir") //else if es una estructura de control que ejecuta un bloque de código si la condición anterior es falsa y esta condición es verdadera
}
else{
    console.log("edad no válida") //else es una estructura de control que ejecuta un bloque de código si todas las condiciones anteriores son falsas
}

switch(edad){   //switch es una estructura de control que ejecuta un bloque de código dependiendo del valor de una expresión
    case 10:
        console.log("eres un niño, no puedes votar ni conducir")
        break;
    case 16:
        console.log("eres un adolescente, puedes conducir, pero no votar")
        break;
    case 18:
        console.log("eres un adulto, puedes votar y conducir")
        break;
        default:
            console.log("por favor ingresa un numero válido")
}

//bucles/ estructuras iterativas/de repetición

// imprimir los numeros del 0 al 100 utilizando un bucle for
for(let i = 0; i < 101; i++){
    console.log(i) //for es una estructura de control que repite un bloque de código un número específico de veces
}

// imprimir los numeros del 0 al 10, pero solo los numeros pares utilizando un bucle while.
let i = 0
while(i < 11){
    console.log(i) //while es una estructura de control que repite un bloque de código mientras una condición sea verdadera
    i = i + 2   
}

//manejo de excepciones/errores

try {
  let x = y + 1; // y no está definida → error
  console.log("Esto no se ejecuta");
} catch (error) {
  console.log("Ocurrió un error:", error.message);
}


//ejercicio extra, imprimir los numeros del 10 al 55 pero solo los numeros pares y que no sean múltiplos de 3, ni el numero 16. 

for(let i = 10; i < 56; i = i + 2){
  if(i != 16 && i % 3 != 0){
    console.log(i)
  }
}
