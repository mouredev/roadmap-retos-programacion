


//valor
 let persona1 = 'Jose'
 let persona2 = persona1
 persona1 = 'Pedro'
//  console.log(persona2) // => Jose
//  console.log(persona1)  // => Pedro

 //referencia

  let personas1 = ['Pedro','Jose','Teresa']
  let personas2 = personas1
 personas1.push('Diego')
//  console.log(personas1) // ['Pedro','Jose','Teresa','Diego']
//  console.log(personas2) // ['Pedro','Jose','Teresa','Diego']

 //funciones 

let variablePorValor = 10

 function myfunctionValor ( variable) {

    variable =20
    // return console.log(variable)

 }

 myfunctionValor(variablePorValor)
//  console.log(variablePorValor)

 //funciones por referencia

 let valorPorReferencia = [1, 2, 3]

 function myFunctionReferencia ( referencia ) {

    referencia.push(6)
    // console.log( referencia)

    let valorPorRef2= referencia
    valorPorRef2.push(9)
    // console.log(valorPorRef2)

 }

 myFunctionReferencia(valorPorReferencia)
//  console.log(valorPorReferencia)


 //extra 

//  Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
//  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
//  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
//  *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
//  *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
//  *   Comprueba también que se ha conservado el valor original en las primeras.

let valor1 = 10
let valor2 = 20

// programa1
function programa1 (parametro1, parametro2) {
    let axu =parametro1
    parametro1 = parametro2
    parametro2 = axu
    return [parametro1, parametro2]

}
//desestructuracion de un array
let [nuevoValo1, nuevoValo2] = programa1(valor1, valor2)

console.log(valor1+ 'valor orginal ', + valor2 + 'valor original')
// 10 - 20
console.log(nuevoValo1 + 'valor invertido ' + nuevoValo2 + 'valor invertido' ) 
// 20 - 10



let referencia1 = [1, 2, 3]
let referencia2 = [11, 12, 30]

// programa2
function programa2 (parametro11, parametro22) {

    parametro11 = referencia2
    parametro22 = referencia1

    return [parametro11, parametro22]
}

let [nuevaReferencia1, nuevaReferencia2] = programa2(referencia1, referencia2)

console.log(`${referencia1} valor origina - ${referencia2} valor original `)
// 1,2,3 valor origina - 11,12,30 valor original
console.log(`${nuevaReferencia1} valor invertido - ${nuevaReferencia2} valor ivertido `)
// 11,12,30 valor invertido - 1,2,3 valor ibertido