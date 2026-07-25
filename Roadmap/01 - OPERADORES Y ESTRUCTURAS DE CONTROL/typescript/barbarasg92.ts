/*/ * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes) /*/

 //Aritméticos:

 let suma= 5 + 6;
 console.log (suma);

 let resta= 5 - 6;
 console.log (resta);

 let division= 5 / 6;
 console.log (division);

 let multiplicacion= 5 * 6;
 console.log (multiplicacion);

 let remainder = 6 % 5;
 console.log (remainder);

 //Asignación:

 let a = 5;
 let b = 6;
 
 // Asignación compuesta: Asignar y operar

 a+= b;
 a-=b;
 a*=b;
 a/=b;
 a%=b;
 
 // Identidad:

 let tipo = typeof a;

 // Comparación:

 a == b; // Sin considerar el tipo (solo miramos el valor) aunque sea letra o número, el valor es el mismo
 a === b; // Considerando el tipo (se mira valor y tipo y tienen que coincidir)
 a != b; //Desigualdad
 a !== b; //Desigualdad estricta
 a > b; //Mayor qué
 a < b; //Menor qué
 a >= b; // Mayor o igual
 a <= b; // Menos o igual

 // Operadores lógicos: Operan sobre valores booleanos

// &&: Las dos son true
 let tieneDinero = true;
let Restaurante = true;

let irAcenar = tieneDinero && Restaurante && "Voy a cenar";
console.log(irAcenar);

// ||: Al menos uno de los dos es true
let haceSol = false;
let tengoParaguas = true;

let irAlParque = haceSol || tengoParaguas || "Me quedo en casa";
console.log(irAlParque);

// !: Convertir un true en un false
let tengoHambre = true;

let noTengoHambre = !tengoHambre;
console.log(tengoHambre);

//??: Sirve para garantizar un valor cuando podría no haber nada

let nombre: string | null = "Barbara";
let miNombre = nombre ?? "Sin Nombre";

console.log(miNombre);




 


/*/ * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */