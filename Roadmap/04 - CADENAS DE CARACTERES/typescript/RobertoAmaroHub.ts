
let comillasDobles: string = "texto entre comillas dobles";
console.log(comillasDobles);
let comillasSimples: string = 'texto entre comillas simples';
console.log(comillasSimples);
let bt_test:string = "prueba dentro";
let backTicks: string =`texto entre backTicks: ${bt_test}`;//interpolación
console.log(backTicks);
//concadenación
console.log(backTicks+comillasDobles);
//iteración
let vocales: string="aeiou";
for(let vocal of vocales){
    console.log(vocal+" ")
}
//minúsculas
console.log("minúsculas: "+comillasDobles.toLowerCase());
//mayúsculas
console.log("mayúsculas: "+comillasDobles.toUpperCase());
//longitud
console.log("longitud: "+comillasDobles.length);
//eliminar espacios al inicio y final del texto
let textoEspacios:string="   texto     ";
console.log(textoEspacios.trim());
//posición de un carácter
console.log(comillasDobles[4]);
console.log(comillasDobles.charAt(4));
//validar comienzo de un texto
console.log(comillasDobles.startsWith("texto"));
//validar final de un texto
console.log(comillasSimples.endsWith("simples"));
//buscar el indexof dentro de una cadena
console.log("indexOf: "+comillasDobles.indexOf("dobles"));
//Cuando indexOf NO encuentra la subcadena devuelve -1
console.log("indexOf NO encontrado: "+comillasDobles.indexOf("simples"));
//includes, Valida si encuentra o no una subcadena
console.log(`¿la palabra "entre" fue encontrada? ${comillasDobles.includes("entre")}`);
console.log(`¿la palabra "dado" fue encontrada? ${comillasDobles.includes("dado")}`);
//slice divide el texto en el índice de inicio y final que nosotros especifiquemos
console.log("slice: "+comillasDobles.slice(2,7));
//replace reemplaza el texto especificado por algún otro
console.log("replace: "+comillasDobles.replace("texto","frase"));
//split divide el texto en subtextos dependiendo de el separador que especifiquemos devolviendo un arreglo
console.log("split: "+comillasDobles.split(" "));

/* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
var prompt = require("prompt-sync")();
import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
function cerrarApp(){
    console.log("Finalizando aplicación")
    rl.close();
}

console.log("\n******Analizando palabras*******")
let palabra1:string="";
let palabra2:string="";

function ingresandoPalabras(){
    palabra1=prompt("Ingresa la primera palabra: ")
    palabra2=prompt("Ingresa la segunda palabra: ")
}
function validandoPalabras(): boolean{
    let isCorrect:boolean=false;
    for(let char of palabra1){
        if(!isNaN(+char)){
            console.log("Las palabras no pueden contener números, inténtalo de nuevo");
            break;
        }
        if(palabra1.includes(" ") || palabra2.includes(" ")){
            console.log("Las palabras no pueden contener espacios, inténtalo de nuevo");
            break;
        }
    }
    for(let char of palabra2){
        if(!isNaN(+char)){
            console.log("Las palabras no pueden contener números, inténtalo de nuevo");
            break;
        }
    }
    if(palabra1.trim().toLowerCase()==palabra2.trim().toLowerCase()){
        console.log("Las palabras no pueden ser iguales, inténtalo de nuevo");
    } else if(palabra1.trim().length<1 || palabra2.trim().length<1){
        console.log("Las palabras no pueden estar vacías, inténtalo de nuevo");
    } else{
        isCorrect=true;
    }
    return isCorrect;
}

function isPalindromo(palabra:string){
    if(palabra.split("").toString()===palabra.split("").reverse().toString()){
        console.log(`la palabra ${palabra} es un palíndromo`)
    }else{
        console.log(`la palabra ${palabra} NO es un palíndromo`)
    }
}

function sonAnagramas(){
    let _pal1:string[]=palabra1.split("");
    let _pal2:string[]=palabra2.split("");
    if(_pal1.sort().toString()==_pal2.sort().toString()){
        console.log(`${palabra1} y ${palabra2} son anagramas`)
    } else {
        console.log(`${palabra1} y ${palabra2} NO son anagramas`)
    }
}

function esIsograma(palabra:string){
    let tempArray:string[]=[];
    for(let char of palabra){
        tempArray.push(char);
        if(tempArray.filter((valor)=>valor==char).length>1){
            console.log(`la ${palabra} NO es isograma`)
            return;
        }
    }
    console.log(`la ${palabra} es isograma`)
}

function analizandoPalabras(){
    ingresandoPalabras();
    if(!validandoPalabras()){
        analizandoPalabras()
    }
    console.log("\n")
    isPalindromo(palabra1);
    isPalindromo(palabra2);
    console.log("\n")
    sonAnagramas();
    console.log("\n")
    esIsograma(palabra1)
    esIsograma(palabra2)
    cerrarApp();
}

analizandoPalabras();
