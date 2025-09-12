// -1-

function funcion1(){
    console.log('Esto es una función')
}

funcion1()

function funcion2(numero){
    if (numero === 8) {
        console.log('El numero es 8')
    } else {
        console.log('El numero no 8')
    }
}

funcion2(8)

function funcion3(numero){
    numero += 8;
    return numero;
}

let resultado3 = funcion3(2)
console.log(resultado3)

// -2-

function funcionExt() {
    console.log("Función externa")
    function funcionInt() {
        console.log("Función interna")
    }

    funcionInt()
}

funcionExt()

// -3-

let random = Math.round(Math.random()*100)
console.log(random)

// -4-

var variableGlobal = 'Esto es una variable Global'

function funcionLocal(){
    var variableLocal = 'Esto es una variable Local'

    console.log(variableGlobal)
    console.log(variableLocal)
}

funcionLocal()

console.log(variableGlobal)
//console.log(variableLocal) --> Is not defined

// -5- EXTRA

function funcionExtra(string1, string2){
    for (let funcionExtraFor = 1; funcionExtraFor <= 100; funcionExtraFor++) {

        let funcionExtraForPrint

        if (funcionExtraFor % 3 === 0 && funcionExtraFor % 5 === 0) {
            funcionExtraForPrint = string1 + string2
        } else if (funcionExtraFor % 5 === 0) {
            funcionExtraForPrint = string2
        } else if (funcionExtraFor % 3 === 0) {
            funcionExtraForPrint = string1
        } else {
            funcionExtraForPrint = funcionExtraFor
        }

        console.log(funcionExtraForPrint)
    }

}

funcionExtra('pin', 'pon')