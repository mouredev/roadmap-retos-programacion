 /* EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */
console.log('Acceso a caracteres específicos');
let texto = "Hola Mundo";
console.log(texto[0]);

console.log('Subcadenas');
console.log(texto.substring(0,4));

console.log('Longitud');
console.log(texto.length);

console.log('Concatenación');
let texto2 = "!";
console.log(texto + texto2);

console.log('Repetición');
console.log(texto.repeat(2));

console.log('Recorrido');
for(let char of texto){
    console.log(char);
}

console.log('Conversión a mayúsculas y minúsculas');
console.log(texto.toUpperCase());
console.log(texto.toLowerCase());

console.log('Reemplazo');
console.log(texto.replace("Hola", "Adiós"));

console.log('División');
console.log(texto.split(" "));

console.log('Unión');
let arr = ["Hola", "Mundo"];
console.log(arr.join(" "));

console.log('Interpolación');
let nombre = "Tomas";
console.log(`Hola, ${nombre}`);

console.log('Verificación');
console.log(texto.includes("Hola"));
console.log(texto.startsWith("Hola"));
console.log(texto.endsWith("Mundo"));


/* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos -> Palabra que se lee igual de izquierda a derecha y derecha a izquierda 
 * - Anagramas -> Palabras que se pueden reorganizar
 * - Isogramas -> Palabra o frase en la que cada letra aparece exactamente el mismo número de veces
 */

const readline = require("readline")
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

function palindromo(p1){
    const palabra = p1.toLowerCase();
    if(palabra===palabra.split('').reverse().join('')) console.log(`La palabra ${p1} es un Palindromo`)
    else console.log(`La palabra ${p1} no es un Palindromo`)
}

function anagrama(p1,p2){
    const palabra1= p1.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/\s+/g, ""); 
    const palabra2= p2.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/\s+/g, ""); 
    if(palabra1.split('').sort().join('')===palabra2.split('').sort().join('')) console.log(`La palabra ${p1} y ${p2} Son anagramas`)
    else console.log(`La palabra ${p1} y ${p2} No son anagramas`)
}

function isograma(p1){
    const palabra = p1.toLowerCase();

    const frecuencias = {};
    for (let letra of palabra) {
        frecuencias[letra] = (frecuencias[letra] || 0) + 1;
    }
    
    const repeticionesUnicas = new Set(Object.values(frecuencias));
    
    if (repeticionesUnicas.size === 1) {
        console.log(`La palabra ${p1}es un Isograma`);
    } else {
        console.log(`La palabra ${p1} NO es un Isograma`);
    }
}

function menu(){
    rl.question("Ingresa la primera palabra:",(p1)=>{
        rl.question("Ingresa la segunda palabra:", (p2)=>{
            palindromo(p1)
            palindromo(p2)
            anagrama(p1,p2)
            isograma(p1)
            isograma(p2)

            rl.question('Desea cerrar el programa? S/N\n', (resp) => {
                resp = resp.toUpperCase()
                if(resp == 'S'){
                    console.log('Saliendo....')
                    process.exit(0)
                }else{
                    inicio()
                }
            })
        })
    })
    
}