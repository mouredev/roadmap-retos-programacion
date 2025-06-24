// Ejemplo de asignación por valor

let numA = 10
let numB = numA // numB es una copia en este momento de numA
numB = 20

console.log(numA) // 10
console.log(numB)// 20

// Ejemplo de asignación por referencia
let obj1 = {nombre: "Esteban"}
let obj2 = obj1 // obj 2 es referencia a obj1, toma la referencia de memoria de obj1
obj2.nombre = "Carlos"
console.log(obj1.nombre)//"Carlos"
console.log(obj2.nombre)//"Carlos"

// Función con parámetro por valor
function modificarValor(x){
    x = 20
    console.log("dentro de la funcion", x)// 20
}

let num = 10
modificarValor(num)
console.log("fuera de la funcion", num )//10

// Función con parámetro por referencia
function modificarObjeto(obj){
    obj.nombre = "Carlos"
    console.log(obj.nombre)//Carlos
}

let persona = { nombre: "Esteban"}
modificarObjeto(persona)
console.log(persona.nombre)//Carlos


// Ejercicio Extra: Intercambio por valor

function intercambioValor(x,y){
    let valor = x
    x = y
    y = valor
    console.log(x,y)
    return [x,y]
}

let valor1 = 1
let valor2 = 2
let [nuevoValor1, nuevoValor2] = intercambioValor(valor1,valor2)
console.log("Valores originales", valor1,valor2)
console.log("Valores intercambiados", nuevoValor1,nuevoValor2)

// Ejercicio Extra: Intercambio por referencia
function intercambioReferencia(obj1, obj2) {
    let ref = obj1.valor
    obj1.valor = obj2.valor
    obj2.valor = ref
}

let ref1 = { valor:1 }
let ref2 = { valor:2 }
intercambioReferencia(ref1, ref2)
console.log("Valores originales", ref1.valor,ref2.valor)
