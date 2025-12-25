// Tipo de datos por valor

let a = 10
let b = a
console.log(b)
b = 20

console.log(a)
console.log(b)

//Tipo de datos por referencia

let persona = { nombre: 'Juan' }
let persona2 = persona
persona2.nombre = 'Pedro'
console.log(persona)
console.log(persona2)

//Funciones con dato por valor

function cambiarValor(a) {
    a = 20
    console.log(a)
}

let c = 10
console.log(c)
cambiarValor(c)
console.log(c)

// Funciones por datos de referencias

function cambiarValorObjeto(objeto) {
    objeto.nombre = 'Pedro'
    console.log(objeto)
}

let personaFunc = { nombre: 'Juan' }
console.log(personaFunc)
cambiarValorObjeto(personaFunc)
console.log(personaFunc)

//Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
//Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
//Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
//se asigna a dos variables diferentes a las originales. A continuación, imprime
//el valor de las variables originales y las nuevas, comprobando que se ha invertido
//su valor en las segundas.
//Comprueba también que se ha conservado el valor original en las primeras.

let valor1 = 10
let valor2 = 20

function intercambiarValoresPorValor (valor1, valor2) {
    let aux = valor1
    valor1 = valor2
    valor2 = aux
    return [valor1, valor2]
}

let [valor1Nuevo, valor2Nuevo] = intercambiarValoresPorValor(valor1, valor2)
console.log(valor1)
console.log(valor2)
console.log(valor1Nuevo)
console.log(valor2Nuevo)

let persona1 = {nombre: "Miguel"}
let persona2 = {nombre: "Angle"}

function intercambiarValoresPorReferencia (persona1, persona2) {
    let aux = persona1
    persona1 = persona2
    persona2 = aux
    return [persona1, persona2]
}


let [persona1Nuevo, persona2Nuevo] = intercambiarValoresPorReferencia(persona1, persona2)
console.log(persona1)
console.log(persona2)
console.log(persona1Nuevo)
console.log(persona2Nuevo)



