// EJERCICIO:
// Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
// (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
// Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:
// Condicionales, iterativas, excepciones...
// Debes hacer print por consola del resultado de todos los ejemplos.

(() => {
    // OPERADORES

    // ARITMETICOS
    // suma
    console.log(10 + 10)
    // resta
    console.log(10 - 10)
    // division
    console.log(10 / 2)
    // multiplicacion
    console.log(25 * 4)
    //modulo
    console.log(4 % 3)
    // potencia
    console.log(2 ** 3)


    // LÓGICOS
    // and ( los dos deben ser true para que devuelva true de otra manera devolvera false)
    console.log(true && false)
    // or ( solamente es necesario que uno de las dos expresiones sea true para devolver true )
    console.log(true || false)
    // not ( negacion )
    console.log(!true)


    // DE COMPARACIÓN
    // mayor que
    console.log(10 > 9)     
    // menor que
    console.log(7 < 49)     
    // mayor o igual que
    console.log(6 >= 6)    
    // menor o igual que
    console.log(11 <= 12)    


    // DE ASIGNACIÓN

    // Suma y asignación
    let suma: number = 8
    suma += 2          
    console.log(suma)

    // Resta y asignación
    let resta: number = 10
    resta -= 9                
    console.log(resta)      

    // Multiplicación y asignación
    let multiplicacion: number = 5
    multiplicacion *= 5          
    console.log(multiplicacion) 

    // División y asignación
    let division: number = 100
    division /= 10                
    console.log(division)       

    // Módulo y asignación
    let modulo: number = 33
    modulo %= 3                  
    console.log(modulo)

    // Potencia y asignación
    let potencia: number = 2
    potencia **= 8                    
    console.log(potencia)


    // DE PERTENENCIA

    let arr: number[] = [12, 14, 16, 18, 20, 40, 60, 80, 100];
    // 40 pertenece al conjunto 
    console.log(40 in arr);
    // 11 pertenece al conjunto
    console.log(99 in arr);

    // ESTRUCTURA DE CONTROL:
    let motivado: boolean = true
    if(motivado) {
        console.log("Estoy motivado")
    } else if(!motivado) {
        console.log("No estoy motivado")
    } else {
        console.log("Bloque inaccesible")
    }


    // DIFICULTAD EXTRA (opcional):
    // Crea un programa que imprima por consola todos los números comprendidos
    // entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
    for (let index = 10; index <= 55; index++) {
        if(index % 2 === 0 && index !== 16 && index % 3 !== 0) {
            console.log(index)
        }
    }
})()
