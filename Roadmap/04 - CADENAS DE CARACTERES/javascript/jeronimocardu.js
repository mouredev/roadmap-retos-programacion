let ejemplo1 = 'Hola mundo';
let ejemplo2 = 'Soy jeronimo';
// Acceso a un caracter especifico
console.log('Acceso a un caracter en especifico: ', ejemplo1[0]);

// Subcadenas
console.log('Subcadena de un string', ejemplo1.substring(0, 5));

// Longitud
console.log('Longitud del string: ', ejemplo1.length);

// Concatenacion
let concatenacion = ejemplo1 + ', ' + ejemplo2;
console.log('Concatenacion: ', concatenacion);

// Repeticion
let cadenaRepetida = ejemplo1.repeat(5);
console.log('Cadena repetida: ', cadenaRepetida);

// Recorrido
for(let i of ejemplo1){
    console.log(i);
}

// Conversion a Mayus y Minus
console.log('String en Minusculas: ', ejemplo1.toLowerCase());
console.log('String en Mayusculas: ', ejemplo1.toUpperCase());

// Reemplazo
console.log('String remplazado: ', ejemplo1.replace('Hola', 'Chau'));

// Division
let cadenaWords = ejemplo1.split(' ');
console.log('Division de string: ', cadenaWords);

// Union
console.log('Union del string: ', cadenaWords.join(' '));

// Interpolacion
console.log(`Esto es interpolacion: '${ejemplo1}' usando $ {}`);

// Verificacion
let contiene = ejemplo1.includes('Hola');
console.log('Contiene "Hola":', contiene);

////////////////////////////////////////////////////////
//              EXTRA

function comparaciones(str1, str2){
    // Políndromos
    if(str1.toLowerCase() === str1.toLowerCase().split('').reverse().join('')){
        console.log(`'${str1}' es Polídromos`);
    }
    if(str2.toLowerCase() === str2.toLowerCase().split('').reverse().join('')){
        console.log(`'${str2}' es Polídromos`);
    }

    // Anagramas
    if(str1.toLowerCase().split('').sort().join('') === str2.toLowerCase().split('').sort().join('')){
        console.log(`${str1} y ${str2} Son Anagramas`);
    }

    // Isogramas
    let isIsogram = true;
    for(let i of str1.toLowerCase()){
        if(str2.toLowerCase().includes(i)){
            isIsogram = false;
        }
    }
    if(isIsogram) console.log(`${str1} y ${str2} son Isogramas`);
}

comparaciones('hola', 'efe')