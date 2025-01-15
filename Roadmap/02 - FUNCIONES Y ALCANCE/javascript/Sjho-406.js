//Funcion sin parámetros ni retorno
function Hello() {
    console.log('Hola')
}

Hello()

//Funcion con uno o varios parámetros
function HelloName(name) {
    console.log(`Hola ${name}`)
}

HelloName('Jose')

//Funcion con retorno
function Sum(a, b) {
    return a + b;
}

console.log(Sum(2, 2))

//Funciones dentro de funciones
function SumCall() {
    console.log(`Tu resultado es: ${Sum(2, 2)}`)
}

SumCall()

//Reto extra
function PrintNumbers(a, b) {
    let count = 0
    for (let i = 0; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(a + b)
            count++
        }
        else if (i % 3 === 0) {
            console.log(a)
            count++
        }
        else if (i % 5 === 0) {
            console.log(b)
            count++
        }
    }

    return count
}
console.log(PrintNumbers('hola', 'como estas'))
