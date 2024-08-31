
// Operador Asignacion

let x = 10
let y = 20
console.log("Valor de x: " + x + " Valor de y: " + y)
// Asignacion de adicion
let adicion = x += y
console.log("Adicion: " + adicion)
// Asignacion de resta
let resta = x -= y
console.log("Resta: " + resta)
// Asignacion de multiplicacion
let multiplicacion = x *= y
console.log("Multiplicacion: " + multiplicacion)
// Asignacion de division
let division = x /= y
console.log("Division: " + division)
// Asignacion de residuo
let residuo = x %= y
console.log("Residuo: " + residuo)
// Asignacion de exponenciacion
let exponenciacion = x **= y
console.log("Exponenciacion: " + exponenciacion)



// Operador Comparacion

// Igual
let igual = x == y
console.log("el valor de x y el valor de y, son iguales?", igual)
// No es igual
let noigual = x != y
console.log("el valor de x y el valor de y, son diferentes?", noigual)
// Mayor que
let mayor = x > y
console.log("el valor de x es mayor que el valor de y?", mayor)
// Menor que
let menor = x < y
console.log("el valor de x es menor que el valor de y?", menor)
// Mayor o igual
let mayorigual = x >= y
console.log("el valor de x es mayor o igual a el valor de y?", mayorigual)
// Menor o igual
let menorigual = x <= y
console.log("el valor de x es menor o igual a el valor de y", menorigual)

// Operadores Aritmeticos

// incremento
let incremento = x++
console.log("Incremento: ", incremento)
// decremento
let decremento = x--
console.log("Decremento: ", decremento)

// Operadores logicos 

// AND
x && y
// OR
x || y
// NOT
!x


// ESTRUCTURAS DE CONTROL

// condicionales
if (x >= y) {
  console.log("El valor de x es mayor o igual a el valor de y")
} else {
  console.log("El valor de x es menor a y")
}

// bucle for
for(i=0; i<5; i++) {
  console.log("Resultado: " + i)
}

// bucle for con arrays
let animales = ["Perro", "Gato", "Pato", "Caballo"]
for (const animal of animales){
  console.log("Animal: ", animal)
}

let libro = {
  title: "1984",
  author: "George Owell",
  genre: "Fiction",
  yearPublished: 1949
}
for (i in libro) {
  console.log(`${i}: ${libro[i]}`)
}

// bucle while
let count = 0
while(count<5){
  console.log("count:" + count)
  count++
}

// bucle do while
do {
console.log("count: " + count)
count++
} while(count<5)

// switch
let color = "Azul"
switch(color) {
  case "Morado":
    console.log("Tu color favorito es el morado")
    break;
  case "Azul":
    console.log("Tu color favorito es el azul")
    break;
  case "Verde":
    console.log("Tu color favorito es el verde")
    break;
  default:
    console.log("Ninguna de las opciones anteriores es tu color favorito")
}


// DIFICULTAD EXTRA

for(let i=10; i<=55;i++) {
  if (i%2==0 && i!==16 && i%3!==0){
    console.log(i)
  }
}

