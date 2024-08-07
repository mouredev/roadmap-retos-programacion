/* 
# Ejercicios de Programación

## Operadores

- [X] Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
  - Aritméticos
  - Lógicos
  - De comparación
  - Asignación
  - Identidad
  - Pertenencia
  - Bits

## Estructuras de Control

- [] Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:
  - Condicionales
  - Iterativas
  - Excepciones
- [] Debes hacer print por consola del resultado de todos los ejemplos.

## Dificultad Extra (Opcional)

- [] Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

- [] Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo. 
*/


// Operadores Aritméticos:

var a:number = 44;
var b:number = 15;
// Suma (+)
console.log(`La suma de a+b es ${a+b}`);

// Resta (-)
console.log(`La resta de a-b es ${a-b}`);

// Multiplicación (*)
console.log(`La multiplicación de a*b es ${a*b}`);

// División (/)
console.log(`La división entre a/b es ${a/b}`);

// Módulo (%)
console.log(`El modulo de a%b es ${a%b}`);

// Incremento (++)
console.log(`El incremento automatico de  a++ es ${a++}`);

// Decremento (--)
console.log(`El decremento automatico de  a- es ${a--}`);


// Operadores de Comparación:

// Igual (==)
console.log(`Comparando igualdad a==b ${a==b}`);

// No igual (!=)
console.log(`Comparando desigualdad a!=b ${a!=b}`);

// Estrictamente igual (===)
console.log(`Comparación estricta a===b ${a===b}`);

// Estrictamente no igual (!==)
console.log(`Comparación estricta negada a!=b ${a!==b}`);

// Mayor que (>)
console.log(`Mayor que ${a>b}`);

// Menor que (<)
console.log(`Menor que ${a<b}`);

// Mayor o igual que (>=)
console.log(`Mayor igual que ${a>=b}`);

// Menor o igual que (<=)
console.log(`Menor igual que ${a<=b}`);


// Operadores Lógicos:

// AND lógico (&&)
console.log(`Operador logico AND ${a&b}`);

// OR lógico (||)
console.log(`Operador logico OR ${a|b}`);

// NOT lógico (!)
console.log(`Operador logico NOT ${a!=b}`);


// Operadores de Asignación:
var saldo:number= 0; 
// Asignación (=)
const nombre:string= "Lenin Mendoza";
console.log(`El valor de nombre es ${nombre}`);


// Suma y asignación (+=)
saldo += 44; 
console.log(`Suma asignada a la variable de saldo es ${saldo}`);

// Resta y asignación (-=)
saldo -= 44; 
console.log(`Resta asignada a la variable de saldo es ${saldo}`);

// Multiplicación y asignación (*=)
saldo *= 1.5; 
console.log(`Multiplicación asignada a la variable de saldo es ${saldo}`);

// División y asignación (/=)
saldo /= 2; 
console.log(`División asignada a la variable de saldo es ${saldo}`);


// Operadores de Bits:
let verdadero:number = 1;
let falso:number = 0;

// AND a nivel de bits (&)
console.log(`AND a nivel de Bits ${verdadero && falso}`);

// OR a nivel de bits (|)
console.log(`OR a nivel de Bits ${verdadero || falso}`);

// XOR a nivel de bits (^)
console.log(`XOR a nivel de Bits ${verdadero ^ falso}`);

// Complemento a nivel de bits (~)
console.log(`Complemento a nivel de Bits ${~ falso}`);

// Desplazamiento a la izquierda (<<)
console.log(`Desplazamiento a la izquierda a nivel de Bits ${verdadero << falso}`);

// Desplazamiento a la derecha (>>)
console.log(`Desplazamiento a la derecha a nivel de Bits ${verdadero >> falso}`);


// Estructuras de Control

// Condicionales

// Estructura de control condicional donde se determina si un usuario es mayor o menor de edad para alguna acción

const usuario:string | null = prompt("Ingresa tu edad", "17");
const edad:number = Number(usuario);
const mensaje:string = edad < 18 ? "Eres menor de edad" : "Eres mayor de edad";
alert(mensaje);

// Iterativas

const cero:number = 0;
for (let index = 0; index < 10; index++) {
    const element = index;   
}

// Excepciones

const div:number = 4;
const divd:number = 0;

try {
    console.log(div/divd);
    
} catch (error) {
    console.log(`No se puede dividir entre cero, el error es de tipo = ${error}`);
    
}finally{
    console.log("Mensaje de finalización");
    
}

// Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for(let i=0; i <= 55; i++){
    if((i%2 == 0) && (i != 16) && (i%3 != 0)){
        console.log(i);
        
    }
}