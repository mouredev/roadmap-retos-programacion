/*
 * EJERCICIO:
 ! - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje: Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 ! - Comprueba si puedes crear funciones dentro de funciones.
 ! - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 ! - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 ! - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */


// FUNCION BASICA
const myFunction = ()=>{
    console.log("hola funcion 1")
}
myFunction()

// FUNCION CON RETORNO
const myFunction2: ()=> string = ()=>{
    return "hola como estas funcion 2?"
}

console.log(myFunction2())

//FUNCION CON PARAMETROS

const myFunction3: (saludo: string, lenguaje:string) => string = (saludo, lenguaje) =>{
    return `${saludo} ${lenguaje}`
}

console.log(myFunction3("Hola", "TypeScript"))

//FUNCION DENTRO DE UNA FUNCION

const myFunction4: (saludar: string) => string = (saludar)=>{
    const myFunction5: (lenguaje: string) => string = (lenguaje)=>{
        return `${saludar} ${lenguaje}`
    }
    return myFunction5("TypeScript, funcion dentro de una funcion")
}

console.log(myFunction4("hola"))

// console.log(Math.random()) // FUNCION DEL LENGUAJE

//VARIABLE LOCAL Y GLOBAR

const saludar: string = "hola"

const myFunction6: (lenguaje: string) => string = (lenguaje)=>{
    return `${saludar}, ${lenguaje}`
}
console.log(myFunction6("TypeScript")) // variable global

const myFunction7: (lenguaje: string) => string = (lenguaje)=>{
    const saludo: string = "hola"
    return `${saludo} ${lenguaje}`
}

console.log(myFunction7("TypeScript con variable local"))


//EXTRA

const functionExtra: (param1:string, param2:string)=> number = (param1, param2)=>{
    let num: number = 0
    for (let i = 1; i < 100 ; i++) {
        if (i % 3 === 0) {
            console.log(param1)
            num++
        }else if (i % 5 === 0){
            console.log(param2)
            num++
        } else if (i % 3 === 0 && i % 5 === 0){
            console.log(`${param1}${param2}`)
            num++
        }else {
            console.log(i)
        }
    }
    return num
}

console.log(functionExtra("Type", "Script"))