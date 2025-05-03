// ASIGNACIÓN POR VALOR Y POR REFERENCIA

/**ASIGNACIÓN POR VALOR:
Se asigna el contenido de la variable x a la variable y,
puedo modificar el valor de y sin alterar a x, 
puesto que cada variable tiene su propio espacio en memoria.
SI LA VARIABLES ASIGNADA CONTIENE UN VALOR PRIMITIVO ES UNA ASIGNACIÓN POR VALOR.*/

/**ASIGNACIÓN POR REFERENCIA:
Se asigna la referencia a la variable a,
es decir no se asigna una copia del valor de a,
por lo que ambas variables apuntan al mismo espacio en memoria.
Si se modifica el valor de b automáticamente se modifica a. 
SI LA VARIABLE ASIGNADA NO ES UN VALOR PRIMITIVO ES UNA ASIGNACIÓN POR REFERENCIA.*/

// Por valor:
let x, y;

x = 25;
y = x; //tipo number
y = 30;
console.log(x, y);

// Por Referencia
x = [1, 2, 3, 4];
y = x;
y.push(5);
console.log(x, y);

//Función con parámetro por valor:
let texto = 'Hola mundo!';

function funcionPorValor(texto:string){
    texto = 'Hola Mundo, desde dentro de la función!';
    return console.log(texto); 
}
funcionPorValor(texto); // Hola Mundo, desde dentro de la función!

console.log(texto); // Hola mundo!

//Función con parámetro por referencia:
let persona = {nombre:'Sharah', apellido:'Palacios'}

function funcionPorReferencia(persona){
    persona.edad = 20;
    return console.log(persona); 
}
funcionPorReferencia(persona); // { nombre: 'Sharah', apellido: 'Palacios', edad: 20 }

console.log(persona); // { nombre: 'Sharah', apellido: 'Palacios', edad: 20 }

//Extra:
// parámetros por valor:
let porValor1 = '1';
let porValor2 = '2';

function funcPorValor(porValor1, porValor2){
    let tem = porValor1;
    porValor1 = porValor2;
    porValor2 = tem;
    return [porValor1, porValor2];
}
let nuevosValores = funcPorValor(porValor1, porValor2);

let nuevoPorValor1 = nuevosValores[0];
let nuevoPorValor2 = nuevosValores[1];

console.log(porValor1, porValor2);  // 1 2
console.log(nuevoPorValor1, nuevoPorValor2); // 2 1

//Parámetros por referencia:
let porReferencia1 = [1, 2, 3];
let porReferencia2 = ['a','e','i','o','u'];

function funcPorReferencia(porReferencia1, porReferencia2){
    let tem = porReferencia1;
    porReferencia1 = porReferencia2;
    porReferencia2 = tem;
    return [porReferencia1, porReferencia2];
}
let newValores = funcPorReferencia(porReferencia1, porReferencia2);

let nuevoPorReferencia1 = newValores[0];
let nuevoPorReferencia2 = newValores[1];

console.log(porReferencia1, porReferencia2); //[ 1, 2, 3 ] [ 'a', 'e', 'i', 'o', 'u' ]
console.log(nuevoPorReferencia1, nuevoPorReferencia2); //[ 'a', 'e', 'i', 'o', 'u' ] [ 1, 2, 3 ]

