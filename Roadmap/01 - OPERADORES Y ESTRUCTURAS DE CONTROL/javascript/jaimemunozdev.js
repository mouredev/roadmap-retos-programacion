// OPERADORES JAVASCRIPT

    // Asignacióm

        // Operador de asignación (=)
        let asignacionSimple = 'Soy igual a este string'
        console.log(asignacionSimple) // 'Soy igual a este string'

        // Asignación de adicióm (+=)
        let asignaAdicion = 10
        asignaAdicion += 5
        console.log(asignaAdicion) // 15

        // Asignación de resta (-=)
        let asignaResta = 10
        asignaResta -= 5
        console.log(asignaResta) // 5

        // Asignación de multiplicación (*=)
        let asignaMultiplica = 5
        asignaMultiplica *=5
        console.log(asignaMultiplica) // 25

        // Asignación de división (/=)
        let asignaDivide = 10
        asignaDivide /= 2
        console.log(asignaDivide) // 5

        // Asignación de módulo (%=)
        let asignaModulo = 18
        asignaModulo %= 2
        console.log(asignaModulo) // 0

        // Asignación de exponenciación (**=)
        let asignaExponencia = 2
        asignaExponencia **= 3  // Sería como decir: "2 al cubo"
        console.log(asignaExponencia) // 8

    // Aritméticos

        // Operador de suma (+)
        let sumando1 = 20,
        sumando2 = 10;
        let suma = sumando1 + sumando2
        console.log(suma) // 30

        // Operador de resta (-)
        let minuendo = 50,
        sustraendo = 20;
        let resta = minuendo - sustraendo
        console.log(resta) // 30

        // Operador de multiplicación (*)
        let multiplo1 = 5,
        multiplo2 = 10;
        let multiplicacion = multiplo1 * multiplo2
        console.log(multiplicacion) // 50

        // Operador de división (/)
        let dividendo = 60,
        divisor = 15;
        let division = dividendo / divisor
        console.log(division) // 4

        // Exponenciación (**)
        let numeroExponenciar = 5,
        alCubo = 3;
        let exponenciado = numeroExponenciar ** alCubo
        console.log(exponenciado) // 125

        // Operador de módulo (%)
        let modulo1 = 10,
        modulo2 = 3;
        let moduloResto = modulo1 % modulo2
        console.log(moduloResto) // 1

        // Operador de incremento (++)
        let aIncrementar = 20
        let incrementado = ++aIncrementar
        console.log(incrementado) // 21

        // Operador de decremento (--)
        let aDecrementar = 24
        let decrementado = --aDecrementar
        console.log(decrementado) // 23

        // Negación Unaria (-'variable')
        let aNegar = 10
        let negado = -aNegar
        console.log(negado) // -10
        
        // Positivo Unario (+'variable')
        let stringNumero = '100'
        console.log(stringNumero)
        let ahoraNumber = +stringNumero
        console.log(ahoraNumber) // 100 como Number

    // De Comparación

        // Igualdad no estricta (==)
        let cincoCinco = 5 + 5,
        diez = 10;
        let igualdad = cincoCinco == diez
        console.log(igualdad) // true

        // Igualdad estricta (===)
        let valorEstrictoBooleano = diez === '10'
        console.log(valorEstrictoBooleano) // false

        // Desigualdad no estricta (!=)
        let valorNoEstricto = cincoCinco != diez
        console.log(valorNoEstricto) // false
        
        // Desigualdad estricta (!==)
        let desigualEstricto = cincoCinco !== 11
        console.log(desigualEstricto) // true

        // Mayor que (>)
        let mayorQue = 5 > 4
        console.log(mayorQue) // true

        // Menor que (<)
        let menorQue = 10 < 30
        console.log(menorQue) // true

        // Mayor o igual que (>=)
        let mayorIgualQue = cincoCinco >= diez
        console.log(mayorIgualQue) // true

        // Menor o igual que (<=)
        let menorIgualQue = cincoCinco <= 8
        console.log(menorIgualQue) // false
    
    // Operadores Lógicos

        // Operador "Y" (&&)
        let y = 10 < 20 && 5 > 4
        console.log(y) // true

        // Operador "O" / (||)
        let o = 10 < 5 || 20 < 30
        console.log(o) // true

        // Operador de negación
        let verdadero = true
        let loNiego = !verdadero
        console.log(loNiego) //false

    // Operadores de Concatenación

        // Operador concatenador (+)
        let soy = 'Soy'
        let miNombre = 'Jaime'
        console.log(soy + ' ' + miNombre) // Soy Jaime

        // Operador concatenador asignador
        let concatenaAsigna = soy += ' también Jaime'
        console.log(concatenaAsigna) // Soy también Jaime

    // Operadores condicionales
        
        // Operador ternario (? :)
        let soyDelMalaga = true
        let mensaje = soyDelMalaga = true ? "Si, eres del Málaga" : "No, eres un chaquetero"
        console.log(mensaje) // "Si, eres del Málaga"
    
    // Operadores de tipo
    
        // typeof
        let soyString = 'Qué soy?'
        let soyNumber = 15
        let soyBooleano = true
        let soyObjeto = {nombre: 'Jaime',
                        apellido: 'Muñoz'}
        console.log(typeof soyString) // string
        console.log(typeof soyNumber) // number
        console.log(typeof soyBooleano) // boolean
        console.log(typeof soyObjeto) // object

        // instanceof
        console.log(soyObjeto instanceof Object) // true
        console.log(soyString instanceof String) // false -> esto funciona con objetos

    // Operadores de bits

        // AND a nivel de bits (&)
        let primero = 5 // 101 binario
        let segundo = 3 // 011 binario
        let ANDbits = primero & segundo
        console.log(ANDbits) // 1

        // OR a nivel de bits (|)
        let ORbits = primero | segundo
        console.log(ORbits) // 7 (binario 111)

        // XOR a nivel de bits (^)
        let XORbits = primero ^ segundo
        console.log(XORbits) // 6 (binario 110)

        // NOT a nivel de bits (~)
        let NOTbits = ~primero
        console.log(NOTbits) // -6

        // Desplazamiento a la izquierda (<<)
        let lefteo = primero << 1
        console.log(lefteo) // 10 (binario 1010)

        // Desplazamiento a la derecha (>>)
        let righteo = primero >> 1
        console.log(righteo) // 2 (binario 10)

        // Desplazamiento a la derecha sin signo
        let sinSigno = -primero >>> 1
        console.log(sinSigno) // 2147483645 (binario 01111111111111111111111111111101)
        

// EXTRA

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}
