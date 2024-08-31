//operadores.

let a = 2;
let b =4;

//operadores de incremento y decremento
a++;
console.log(a);
b--;
console.log(b);

//operadores aritmeticos
console.log(a + b, 'suma');
console.log(a - b, 'resta');
console.log(a / b, 'division');
console.log(a * b, 'multiplicacion');
console.log(a % b), 'modulo';
console.log(a ** b, 'potencia');
//operadores de asignacion.
a +=5;
a -=5;
a /=5;
a *=5;
a %=5;
a **=5;
console.log(a)
//operadores de comparacion.
console.log(a>b);
console.log(a>=b);
console.log(a<b);
console.log(a<=b);
//operadores de igualdad y desigualdad
console.log(a == b);
console.log(a != b);
console.log(a === b);
console.log(a !== b);
//operadores logicos.
let mayor = true;
let suscrito = false;

//AND
console.log( mayor && suscrito );

//OR
console.log( mayor || suscrito );

//NOT
console.log( !suscrito );

//operador ternario
let edad = 25;
let acceso = edad > 17 ? 'permitir acceso' : 'no permitir acceso';
console.log(acceso);

//operador de pertenencia
let array = [7, 2, 4, 9, 8];
let confir = 2 in array;
console.log(confir);

//operador bitwise
let and = a & b;
console.log(and);

let or = a | b;
console.log(or);

let xor = a ^ b;
console.log(xor);

console.log(~a);//el operador not en bitwise

let despla_dere = a >> 1;
console.log(despla_dere);

let despla_izq = a << 1;
console.log(despla_izq);

//estructura de control

//if y else y while

let d = 5

while ( d < 15){
    if( d % 2 == 0 ){
        console.log ('numero par', d);
    }else if ( d % 2 != 0){
    console.log( 'numero impar', d);
}else { console.log( 'error');};
++d;
}

//operador switch

let c =10;

switch (c){
  case 10 :
    console.log('correcto');
    break;
  case 15 :
    console.log('incorrecto');
    break;
  default:
    console.log('accion no definida');
}

//operador do while.

let e = 0;

do {
    if (e % 2 == 0){
        console.log( 'numero par', e);
    }
    ++e;
}while(e < 10)

// for.

for (let f = 2; f < 20; f++){
  if ( f % 2 == 0){
    console.log( 'numero par2', f );
}
}

//for of.

let array2 = [2, 3, 1, 7, 9, 6];
for( numero of array){
  console.log(numero);
}

// for in.

let persona ={
  nombre:'josue',
  edad:15,
  colo_cabe:'negro',
};
for ( rasgos in persona){
  console.log(rasgos, persona[rasgos]);
};

//ejersicio dificultad extra
let z = 10;
while(z <= 55){
    ++z;
    if (z === 16){
        continue;
    }else if (z % 3 === 0){
        continue;
    }else if (z % 2 === 0){
        console.log('numero par', z);
    }

};
  



