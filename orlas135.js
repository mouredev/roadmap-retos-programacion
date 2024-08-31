/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

/*Solución*/

/*Operadores en JavaScript*/

/*Operador de asignación: = */
/*Operadores de incremento y decremento: ++ (incrementa en uno), -- (decrementa en uno)*/
/*Operadores lógicos: !(negación), &&(AND), ||(OR)*/

/*Operadores relacionales: 
  >(mayor que), 
  <(menor que), 
  >=(mayor o igual que), 
  <=(menor o igual que),
  ==(igual que),
  !=(diferente que)
  ===(estrictamente igual en dato y en tipo de dato)
  !==(estrictamente diferente que)
*/

/*Operadores aritméticos:
Orden de prioridad: 

1. () Paréntesis
2. ** Exponenciación
3. *,/ Multiplicación y división
4. +,- Suma y resta
5. %,/ Residuo y cociente
6. Relacionales
7. Lógicos 
*/

const persona_uno = {
  nombre: "Camilo",
  apellido: "Vélez",
  edad: 25,
  saludar: function () {
    console.log(
      `Hola, mi nombre es ${this.nombre + " " + this.apellido}, y tengo ${this.edad} años.`
    );
  },
};

console.info('***************************')
persona_uno.saludar();

console.log();

console.info('*************If/Else**************')


/*Estructura de control If/Else y menor que*/
const esMenor = function () {
  if (persona_uno.edad < 18) {
    return console.log(`Esta persona es menor de edad`)
  } else {
    return console.log(`Esta persona es mayor de edad`)
  }
}
esMenor();

console.info('*************Operador Ternario**************')
/*Operador ternario*/

persona_uno.edad >= 18 
? console.log(`${persona_uno.nombre} sí es mayor de edad`) 
: console.log(`${persona_uno.nombre} no es mayor de edad`)


console.log(`/**Utilizando operadores aritméticos**/`)
/*Potenciación*/
let numero_uno = 25;
let numero_dos = 5;

/*Operaciones con operadores aritméticos*/

/* Suma y resta */
console.log(numero_uno + numero_dos)
console.log(numero_uno - numero_dos)

/*Multiplicación - División - Residuo/módulo*/
console.log(numero_uno * numero_dos)
console.log(numero_uno / numero_dos)
console.log(numero_uno % numero_dos)

/*Potenciación*/
console.log(numero_uno ** numero_dos)

/*Operaciones matematicas ordenadas por prioridad*/
console.log(((numero_dos*numero_uno) + numero_uno + (numero_dos ** numero_uno) / 5 + (numero_dos + 3)) % 5)


console.log(`/*********Utilizando operador de negación**********/`)
let esMujer = !true
let hombre= false
console.log(esMujer === hombre);
console.log(esMujer == hombre);

console.log(`/*******Ejercicio de dificultad extra********/`)

let dificultadExtra = 10
while (dificultadExtra <= 55) {
  if (dificultadExtra % 2 == 0 && dificultadExtra!= 16){
    if(dificultadExtra % 3 != 0) {
      console.log(`Número: ${dificultadExtra}`)
    }
  }

  dificultadExtra++;
}

console.log(`/*****Utilizando do/while*******/`)
do {
  console.log(`Mi edad es de ${persona_uno.edad}`)
  persona_uno.edad++
}while(persona_uno.edad < 30);

console.log(`/**********Utilizando FOR*********/`);

for (i = 0; i <= 20; i++) {
  console.log(`Número: ${i}. Residuo 4: ${i%4}`)
}

console.log(`/**********Utilizando estructura Switch/Case************/`)

dia_elegido = `juernes`

switch(dia_elegido) {
  case `lunes`:
    console.info `NOOOOOOOOOOOOOOOOOOOOOOOOO`
    break;
  case `martes`:
    console.log `¿Apenas es martes?`
    break;
  case `miercoles`:
    console.log `Ya casi es viernes`
    break;
  case `jueves`:
    console.log `Ya es juernes!!!!`
    break;
  case `viernes`:
    console.log `HOY ES VIERNEEEEEEEEEEEEEEES`
    break;
  case `sábado`:
    console.log `Hoy me emborracho`
    break;
  case `domingo`:
    console.log `Se acabó el fin de semana :(`
    break;
  default:
    console.log `Qué día es hoy`
}
