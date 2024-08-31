//******FUNCIONES
//FUNCIONES DE ORDEN SUPERIOR
//map
const numbers =[1,2,3,4]

const double = numbers.map(number => number*2);
console.log(double);

//filter
const even =numbers.filter(n=>n%2===0);;

console.log(even);

//reduce

const sum = numbers.reduce((total, number) => total + number, 0);
console.log(sum);

//every

const allEven = numbers.every(n=>n%2===0);
console.log(allEven);

//some

const hasEven = numbers.some(n=>n%2===0);
console.log(hasEven);   

//MANIPULACION DE CADENAS
//split

const sentence = 'Hello, World!';
const words = sentence.split(' ');
console.log(words);

//join

const joinedWords = words.join('-');
console.log(joinedWords);

//replace

const replaced = sentence.replace('World!', 'JavaScript!');
console.log(replaced);

//substring

const substring = sentence.substring(0, 5);
console.log(substring);

//length

const length = sentence.length;
console.log(length);

//MANIPULACION DE OBJETOS   
//keys

const person = {name: 'John', age: 30};
const keys = Object.keys(person);
console.log(keys);

//values

const values = Object.values(person);
console.log(values);

//entries   

const entries = Object.entries(person);
console.log(entries);

//OPERACIONES MATEMATICAS
//math random

const random = Math.random();
console.log(random);

//math floor

const floor = Math.floor(random * 10);
console.log(floor);

//math ceil

const ceil = Math.ceil(random * 10);
console.log(ceil);

//math round

const round = Math.round(random * 10);
console.log(round);

//math max

const max = Math.max(1, 2, 3, 4, 5);
console.log(max);

//math min

const min = Math.min(1, 2, 3, 4, 5);
console.log(min);

//MANIPULACION DE FECHAS
//date

const date = new Date();
console.log(date);

//year

const year = date.getFullYear();
console.log(year);

//FUNCION  SIN PARAMETROS NI RETORNO
function sinparametro (){
    console.log('funcion sin parametro ni retorno');
}
sinparametro();

//FUNCION CON UN PARAMETRO SIN RETORNO
function unparametro(parametro){
    console.log(`hola ${parametro}`);

}
unparametro("Pedro");

//FUNCION CON UN PARAMETRO CON RETORNO
function number(numero){
    return numero + numero

}
console.log(number(2));

//FUNCION CON VARIOS PARAMETROS SIN RETORNO
function number (numero1, numero2){
    let numero3 = numero1+numero2;
    console.log(`La suma de ${numero1} + ${numero2} = ${numero3}`)
}
number(3,2);

//FUNCION CON VARIOS PARAMETROS Y CON RETORNO
function numeros (num1, num2){
    return num1*num2
}
console.log(numeros(5,2));

//FUNCION ANONIMA
const color = function(col){
    return "Mi color Preferido es " + col;
}
console.log(color("BLUE"));

//ARROW FUNCION
const planta = (plant)=>{
    return "Mi planta favorita es "+ plant;
}
console.log(planta("Orquidea"));

// Si la función de flecha tiene una sola expresión, se puede omitir el bloque {} y el return:\
const plantas =(plants)=> "Mis Plantas Favorita son " + plants;
console.log(plantas("Cactus"));

//FUNCION CON VALOR POR DEFECTO
function say(sal='JOse'){
    return "Saludar a "+ sal;
}
console.log(say());
console.log(say("chris"));

// FUNCION QUE UTILIZA EL OPERADOR REST
//EL OPERADOR REST PERMITE A UNA FUNCION ACEPTAR UN NUMERO INDEFINIDO DE ARGUMENTOS COMO UN ARRAY
const suma=(...rest)=>{
return rest.reduce((total, numero)=>total + numero,0);
}
console.log(suma(1,2,3,4,5));

//FUNCION CON TRY CATCH
function division(x, y){
    try{
     if(y===0){
     console.log("Division 0");
    }
    return x/y;
    }
    catch(error){
      console.log(error.message);
      return null;
    }
}
console.log(division(10,2));
console.log(division(10,0));

//DIFICULTAD EXTRA
function cadena(str1, str2) {
    let contador = 0;

    for (let i = 1; i <= 100; i++) {
        let output = '';

        if (i % 3 === 0) output += str1;
        if (i % 5 === 0) output += str2;

        if (output === '') {
            console.log(i);
            contador++;
        } else {
            console.log(output);
        }
    }

    return contador;
}

const str1 = "Javascript ";
const str2 = "The Best";
const result = cadena(str1, str2);
console.log("Veces que se ha impreso el número en vez de texto:", result);
