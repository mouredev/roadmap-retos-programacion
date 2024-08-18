let cont = 0; //variable global

//funcion basica
function saludar(){
    console.log('Hola, buenos días')
}
saludar();

//funcion con parametro
function saludarConocido(nombre){
    console.log('Hola ' +nombre+ ' mucho gusto volver a verte')
}
saludarConocido("Victor");

//funcion IIFE
(function(){
    console.log('Soy una IIFE que me llamo sola')
})();

let numeros = [2,4,8,6,9,1]
//Arroy Function con return implícito
numeros.sort((a,b)=>a-b) //ordenamos los números y utilizamos una arrow function
console.log(numeros)

//funcion basica con retorno
function suma(a,b){
    return a+b
}

//funcion dentro de función
function resultadoMuliplicado(){
    const sum = suma(3,2)
    function multiplicacion(a,b){
    
        console.log('la multiplicacion es ' +a * b)
    }
    multiplicacion(sum,3)
}

resultadoMuliplicado()


//Función dificultad extra 
function palabras(a,b){

    for(let i=1;i<=100;i++){
        if(i%3 === 0 && i%5 === 0){
            console.log(a+b);
        }
        else if(i%3===0){
            console.log(a)
        }
        else if(i%5===0){
            console.log(b)
        }
        else{
            console.log(i)
            cont++;
        }
    }
    return cont;
}

const total= palabras('fizz','buzz')

console.log('En total se han mostrado por pantalla ' + total +' numeros en lugar de palabras');