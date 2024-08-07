//Variables
let x:number = 100;
let y:number = 200;
let z:number = 300;
let a:number = x + y;
let arr:number[] = [10,20,30,40];
let mostrarMensaje:boolean = true;
let dia:number = 7;
let veces:number = 0;

function holaMundo():string {
    return 'Hola mundo';
}

//Operadores de comparación
if(a == z){console.log(`Igual (==): ${a} ${z}`);}
if(x != z){console.log(`No es igual (!=): ${x} ${z}`);}
if(a === z){console.log(`Estrictamente igual (===): ${a} ${z}`);}
if(x !== y){console.log(`Desigualdad estricta (!==): ${a} ${z}`);}
if(a > x){console.log(`Mayor que (>): ${a} ${x}`);}
if(a >= z){console.log(`Mayor o igual que (>=): ${a} ${z}`);}
if(x < a){console.log(`Menor que (<): ${x} ${a}`);}
if(x <= a){console.log(`Menor o igual que (<=): ${x} ${a}`);}

//Operadores lógicos
if((a == z) && (x != z)){console.log('AND lógico (&&)');}
if((y == z) || (x != z)){console.log('OR lógico (||)');}
if(!(x != z)){console.log('NOT lógico (!)');}

//Operadores Aritméticos
console.log(`Residuo (%) ${z} % ${a}:`, z%a);
console.log(`Incremento (++) ++${z}:`, ++z);
console.log(`Decremento (--) --${z}:`, --z);
console.log(`Negación unaria (-) -${z}:`, -z);
console.log(`Exponenciación (**) ${z} ** ${a}:`, z**a);

//Operadores de Asignación
z = x;
console.log('Asignación (=):', z);
z += x;
console.log('Asignación de adición (+=):', z);
z -= x;
console.log('Asignación de reducción (-=):', z);
z *= y;
console.log('Asignación de multiplicación (*=):', z);
z /= x;
console.log('Asignación de división (/=):', z);
z **= x;
console.log('Asignación de exponenciación (**=):', z);
x %= y;
console.log('Asignación de residuo (%=):', x);

//Operadores bit a bit
console.log('AND a nivel de bits:', a & z);
console.log('OR a nivel de bits:', a | z);
console.log('XOR a nivel de bits:', a ^ z);
console.log('NOT a nivel de bits:', ~z);
console.log('Desplazamiento a la izquierda:', z << a);
console.log('Desplazamiento a la derecha:', z >> a);

//Estructura de control if...else
if(mostrarMensaje){
    console.log('Estructura if verdadera');
} else {
    console.log('Estructura if falsa');
}

//Estructura de control switch
switch(dia){
    case 1: console.log('Hoy es lunes'); break;
    case 2: console.log('Hoy es Martes'); break;
    case 3: console.log('Hoy es Miercoles'); break;
    case 4: console.log('Hoy es Jueves'); break;
    case 5: console.log('Hoy es Viernes'); break;
    case 6: console.log('Hoy es Sabado'); break;
    case 7: console.log('Hoy es Domingo'); break;
}

//Estructura while
while(veces < 4){
    console.log('Mensaje', veces);
    veces++;
}

//Estructura for in
for(let index in arr){
    console.log(arr[index]);
}

//Estructura try
try {
    console.log(holaMundo);
} catch (ex) {
    console.log('Hubo un error');  
} finally {
    console.log('Finally');
}

