//Operadores aritmeticos
const a = 3
const b = 5
//Suma
let suma = a + b
//Resta
let resta = a - b
//Multiplicacion
let mult = a * b
//Division
let div = a / b
//Modulo
let mod = a % b
//Potenciacion
let pot = a ** b

console.log(suma)
console.log(resta)
console.log(mult)
console.log(div)
console.log(mod)
console.log(pot)

let c = 3
let d = 5

//Operadores de asignación 
c += 5// al valor a sumarle 5 y guardar. Resultado = 8
console.log(c)
c -= 2 // ahora a vale 6 ya que le reste 2
console.log(c)
c *= 1 // mismo valor ya que multiplique por 1
console.log(c)
c /= 2 // ahora equivale a 3 ya que dividi por 2
console.log(c)
c %= 2 // el cociente al dividir 3 / 2 es 1
console.log(c)
c **= 2 // Sigue siendo 1 ya que eleve dos veces 1*1*1 = 1
console.log(c)
// Operadores de comparacion
//Igualdad y Igualdad exacta
console.log(c == d) // false
d = "2"
console.log(c === d) // False
//Diferencia y diferencia exacta
d = 3
console.log(c != d) // True
console.log(c !== d) // True
//Mayor que y mayor o igual que
const num1 = 5
const num2 = 3
console.log(num1 > num2) // True
console.log(num1 >= num2)//True
//Menor que y menor o igual que
console.log(num1 < num2) // False
console.log(num1 <= num2) // False

// Operadores de bits
console.log(5 & 1)      // 1 (AND bit a bit: 0101 & 0001 = 0001)
console.log(5 | 1)      // 5 (OR bit a bit: 0101 | 0001 = 0101)
console.log(5 ^ 1)      // 4 (XOR bit a bit: 0101 ^ 0001 = 0100)
console.log(~5)         // -6 (NOT bit a bit)
console.log(5 << 1)     // 10 (desplazamiento izquierda: 0101 -> 1010)
console.log(5 >> 1)     // 2 (desplazamiento derecha: 0101 -> 0010)

//Estructuras de control(condicionales)
// if, else if, else (si, sino, si)
const edad = 22
if (edad >= 65) {
    console.log("Adulto mayor") 
} else if (edad >= 18) {
    console.log("Adulto") 
} else if (edad >= 0) {
    console.log("Menor de edad") 
} else {
    console.log("Edad no válida") 
}
//Switch
let diaSemana = 3  
switch (diaSemana) {
    case 1:
        console.log("Lunes: inicio de semana") 
        break   // ¡Importante! Sin break, sigue ejecutando los demás
    case 2:
        console.log("Martes: segundo día") 
        break 
    case 3:
        console.log("Miércoles: mitad de semana") 
        break 
    case 4:
        console.log("Jueves: casi viernes") 
        break 
    case 5:
        console.log("Viernes: último día laboral") 
        break 
    case 6:
        console.log("Sabado: dia de descanso ")
        break 
    case 7:
        console.log("Domingo: Ultimo dia de descanso :(")
    default:
        console.log("Dia no valido") 
}
// Resultado: "Miércoles: mitad de semana"

//Estructuras de control(Bucles)
//for (cuando sabes cuántas veces repetir)
for(let i=1;  i<11;  i++){
    console.log(i)
}
//while(Hasta que no se cumpla la condición no se cierra el ciclo)
conteo = 0
while(conteo <= 10){
    console.log(conteo)
    conteo++ 
}
// do while(al menos se ejecuta una vez)              
let contador = 1;

do {
  console.log("Número: " + contador);
  contador++;
} while (contador <= 3);

//Estructuras de control(Excepciones)
try {
    let resultado = 10 / 0 
    console.log("El resultado es: " + resultado) 
}catch (error) {
    // Si algo sale mal, aca se captura el error y se muestra
    console.log("Ocurrió un error: " + error.message) 
    
} finally {
    // Esto se ejecuta SIEMPRE, haya error o no
    console.log("Programa finalizado") 
}

//Dificultad extra
for (let i = 1;  i <= 55;  i++) {
    if(i <= 9){
        continue
    }
    else if(i % 3 == 0){
        continue
    }
    else if(i == 16){
        continue
    }
    else if(i % 2 == 0){
        console.log(i)
    }
}
//version simplificada por IA
for (let i = 10; i <= 55; i++) {  // Empieza en 10 directamente
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}