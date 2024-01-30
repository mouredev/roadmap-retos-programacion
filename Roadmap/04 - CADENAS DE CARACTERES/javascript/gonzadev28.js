//Operaciones con cadenas de caracteres

let texto = 'Aprendo javascript';

//Acceso a caracter en especifico
console.log(texto[0]); //Accede al caracter en la posicion [0] = 'A' de 'Aprendo'

//Acceso a subcadena 
console.log(texto.substring(8)); //Accede a los caracteres desde la posicion [8] en adelante
console.log(texto.substring(8, 12));//Accede a los caracteres desde la posicion [8] hasta [12]

//Acceso a la longitud de la cadena
console.log(texto.length); //Imprime el numero total de caracteres del string incluyendo el espacio

//Concatenacion
let texto2 = 'Retos de programacion';
console.log(texto, 'con ' + texto2); //Concatenacion de variable 'texto' + 'texto2'

//Repeticion
let textoRepetido = ('Texto en repeticion ');
console.log(textoRepetido.repeat(5)); //Cadena se repite 5 veces 

//Recorrido
for(let i = 0; i < texto.length; i++){
    console.log(texto[i]);//Recorre la cadena de caracteres 
}

//Coversion a MAYUSCULAS
console.log(texto.toUpperCase());//Convierte la cadena de caracteres en solo mayusculas 

//Conversion a minusculas
console.log(texto.toLowerCase());//Convierte la cadena de caracteres en solo minusculas

//Remplazo de caracteres
console.log(texto.replace('javascript', 'leguajes de programacion'));
//Remplaza string 'javascript' por string 'leguajes de programacion' 

//Division
console.log(texto.split('')); //Divide cada cadena de caracteres en un solo caracter
console.log(texto.split(' '));//Divide cada cadena de caracteres donde haya un espacio

//Union
let textoSeparado = ['Esto', 'es', 'un', 'texto'];
console.log(textoSeparado);//Imprime el texto separado
console.log(textoSeparado.join(' '));//Une el texto en una sola frase

//Interpolacion
let nombre = 'Gonzalo';
let lenguaje = 'Javascript';
console.log(`Hola mi nombre es ${nombre} e intento aprender ${lenguaje}`);

//Verificacion
let textoVerificado = 'Soy un texto que utilizare para verificar si se encuentra cierta palabra';
console.log(textoVerificado.includes('verificar'));
//Devuelve true porque 'verificar' si se encuentra en la variable 'textoVerificado'
console.log(textoVerificado.includes('verificando'));
//Devuelve false porque 'verificando' no se encuentra en la variable 'textoVerificado'

// DIFICULTAD EXTRA (opcional):
//  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
//  * para descubrir si son:
//  * - Palíndromos
//  * - Anagramas
//  * - Isogramas

//Palindromo
console.log('==========Palindromos==========');
function palindromo(palabra1){
    let palabraInvertida = palabra1.toLowerCase().split('').reverse().join('');
    if(palabra1 === palabraInvertida){
        console.log('Es un palindromo');
    }else{
        console.log('No es palindromo');
    }
}
palindromo('radar');
palindromo('gato');

//Anagrama
console.log('==========Anagramas=========='); 
function anagrama(palabra1, palabra2){
    let ordenPalabra1 = palabra1.toLowerCase().split('').sort().join('');
    let ordenPalabra2 = palabra2.toLowerCase().split('').sort().join('');
    if(ordenPalabra1 === ordenPalabra2){
        console.log('Es un anagrama');
    }else{
        console.log('No es un anagrama');
    }
}
anagrama('botines', 'bisonte');
anagrama('perro', 'gato');

//Isograma
console.log('==========Isogramas=========='); 
function isograma(palabra1){
    let letras = palabra1.toLowerCase().split('');
    let letrasSet = new Set(letras);
    if(letras.length === letrasSet.size){
        console.log('Es un isograma');
    }else{
        console.log('No es un isograma');
    }
}
isograma('murcielago');
isograma('programador');