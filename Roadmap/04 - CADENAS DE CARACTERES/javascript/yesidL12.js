// <------- Cadena de carácteres ---------->
 let nombre = 'Juan Perez';
 let nombre1 = "Juan Perez";
 let nombre2 = `Juan Perez`;

 console.log(typeof(nombre)); // Cadena
 console.log(typeof(nombre1));//Cadena
 console.log(typeof(nombre2)); // Cadena

 //<------- Concatenación de cadenas --------->

 let nombre4 = 'Juan';
 let apellido = 'Perez';
 let nombreCompleto = nombre + ' ' + apellido;
 console.log(nombreCompleto); // Juan Perez


let nombre5 = 'Juan';
let apellido1 = 'Perez';
let nombreCompleto1 = nombre5.concat(' ', apellido1);
console.log(nombreCompleto1); // Juan Perez


// Concatenación con plantillas literales

let nombre6 = 'Juan';
let apellido2 = 'Perez';
let nombreCompleto2 = `${nombre6} ${apellido2}`;
console.log(nombreCompleto2); // Juan Perez


//<-------- Convertir de mayusculas a minisculas y viceversa ----------->

let mensaje = 'Bienvenidos';
let mensajaeMayusculas = mensaje.toUpperCase();
let mensajeMinusculas = mensaje.toLocaleLowerCase();

console.log(mensajaeMayusculas); // BIENVENIDOS
console.log(mensajeMinusculas); // bienvenidos

//<------- Métodos del string ---------->

// Para encontrar el tamaño de un string

let browserType = 'mozilla';
browserType.length(); // 7

// Recuperar una cáracter especifico del string
browserType[1]; // o

browserType[browserType.length - 1]; //Forma recomendada para recuperar el último cáracter.


//Probar si una cadena tiene una subcadena

let buscador = 'mozilla';

if (buscador.includes('zilla')) {
    console.log('Encontré zilla!');
} else {
    console.log('No hay zilla aqui');
}

// Para saber si tiene una subcadena al incio

let buscador1 = 'mozilla';
if (buscador.startsWith('zilla')) {
    console.log('Encontré "zilla"!');
} else {
    console.log('No hay "zilla" aqui');
}

// Para saber si tiene una subcadena al final

let buscador2 = 'mozilla';
if(buscador2.endsWith('zilla')) {
    console.log('Encontré "zilla"!');
} else {
    console.log('No hay "zilla" aqui');
}

// Para encontrar la posición de una subcadena

let tagline = 'MDN - REsourcer for developers, by developers';
console.log(tagline.indexOf('developers')); // 20
// indexOF, devuelve el indice de la primera aparición de la subcadena.

//Para encontrar las subcadenas posteriores a la primera aparición

let firstOcurrence = tagline.indexOf('developers');
let secondOcurrence = tagline.indexOf('developers', firstOcurrence + 1);

console.log(firstOcurrence); // 20
console.log(secondOcurrence); // 35

// Para extraer una subacdena de una cadena

let buscador3 = 'mozilla';
console.log(buscador3.slice(1,4)); // 'azi

// Para actualizar partes de una cadena

let buscador4 = 'mozilla';
let update = buscador4.replace('moz', 'van');

console.log(update); // vanilla
console.log(buscador4);// mozilla

// <--------- Dificultad extra -------->

// Palindromo

const palindromo = (palabra1, palabra2) => {
    const palabraInvertida = palabra1.split('').reverse().join('');
   if ( palabra2 === palabraInvertida){
       console.log(`${palabra1} y ${palabra2} son palíndromos`);
   } else {
    console.log(`${palabra1} y ${palabra2} no son palíndromos`);
   }
}

palindromo('amor' , 'roma');
palindromo('Ana', 'Ana');

// anagrama

const anagrama = (palabra1, palabra2) =>{
    let esAnagrama = false;
    for (let i = 0; i < palabra1.length; i++) {
        for(let j = 0; j < palabra2.length; j++) {
            const check = (palabra1, palabra2) => {
                (palabra1[i] === palabra2[j]) ? esAnagrama = true : esAnagrama = false;
            }
            check(palabra1, palabra2);
        }
    }
    if(esAnagrama === true) {
        console.log(`${palabra1} y ${palabra2} son anagramas`)
    } else {
        console.log(`${palabra1} y ${palabra2} no son anagramas`);
    }
}

anagrama('llenaba', 'ballena');
anagrama('salame', 'melase');

//Isogramas

const isograma = (palabra1, palabra2) => {
    const checkLetters = (palabra) => {
        let letrasVistas = {};
        for (let i = 0; i < palabra.length; i++){
            const letra = palabra[i];
            if(letrasVistas[letra]) {
                return false;
            }
            letrasVistas[letra] = true;
        }
        return true;
    }
    console.log(checkLetters(palabra1) ? `${palabra1} es un isograma` : `${palabra1} no es un isograma`);
    console.log(checkLetters(palabra2) ? `${palabra2} es un isograma` : `${palabra2} no es un isograma`);
}

isograma('Nicolas', 'Nicole');
isograma('Andres', 'caca');