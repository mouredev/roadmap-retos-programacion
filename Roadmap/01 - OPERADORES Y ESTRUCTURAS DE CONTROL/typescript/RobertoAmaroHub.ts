function log(text: string) {
  console.log(text);
}

let a: number = 3;
let b: number = 2;
let res;
log(`datos iniciales:`);
log(`a = ${a} y b = ${b}`);

//Se utilizan para realizar operaciones matemáticas en programación.
log("\nOperadores aritméticos:");
res = a + b;
log(`la suma de ${a}+${b} = ${res}`);
res = a - b;
log(`la resta de ${a}-${b} = ${res}`);
res = a * b;
log(`la multiplicación de ${a}*${b} = ${res}`);
res = a / b;
log(`la división de ${a}/${b} = ${res}`);
res = a % b;
log(`el módulo de ${a}%${b} = ${res}`);
res = Math.floor(a / b);
log(`la división entera de ${a}//${b} = ${res}`);
res = a ** b;
log(`la exponenciación de ${a}**${b} = ${res}`);

//Se utilizan para comparar dos valores y devolver un resultado booleano que indica la relación entre esos valores.
log("\nOperadores de comparación o relacionales:");
res = a == b;
log(`¿${a} es igual a ${b}? respuesta: ${res}`);
res = a != b;
log(`¿${a} es diferente de ${b}? respuesta: ${res}`);
res = a < b;
log(`¿${a} es menor que ${b}? respuesta: ${res}`);
res = a > b;
log(`¿${a} es mayor que ${b}? respuesta: ${res}`);
res = a <= b;
log(`¿${a} es menor o igual que ${b}? respuesta: ${res}`);
res = a >= b;
log(`¿${a} es mayor o igual que ${b}? respuesta: ${res}`);
res = ~b;
log(`~b = ${res}`);

//Se utilizan para combinar expresiones booleanas y realizar operaciones lógicas en programación.
log("\nOperadores lógicos:");
res = a < 3 && b < 3;
log(`¿es ${a} menor que 3 Y ${b} menor que 3? respuesta: ${res}`);
res = a < 3 || b < 3;
log(`¿es ${a} menor que 3 O ${b} menor que 3? respuesta: ${res}`);
res = a != b;
log(`¿${a} es diferente de ${b}? respuesta: ${res}`);

//Estructuras de control

//Condicionales

//if - else
if (a == b) {
  log(`${a} no es igual a ${b}`);
} else {
  log(`${a} es igual a ${b}`);
}

//Switch
switch (b) {
  case 1:
    console.log("Lunes");
    break;
  case 2:
    console.log("Martes");
    break;
  case 3:
    console.log("Miércoles");
    break;
  case 4:
    console.log("Jueves");
    break;
  case 5:
    console.log("Viernes");
    break;
  case 6:
    console.log("Sábado");
    break;
  case 7:
    console.log("Domingo");
    break;
  default:
    console.log("Ese no es un día válido");
    break;
}

//Ternario
res = b==a ? `${b} es igual a ${a}` : `${b} no es igual a ${a}`;
log(res);

//Bucles

//for Loop
for (let i = 0; i < b; i++) {
  console.log ("Bloque de ejecución n°: " + i);
}

//for...of Loop
let arrOf: number[] = [10, 20, 30, 40];
for (var val of arrOf) {
  console.log(val);
}

let str = "Hello World";
for (var char of str) {
  console.log(char); 
}

//for...in Loop
let arrIn: number[] =[10, 11, 12, 13]

for (var index in arrIn) {
  console.log(`index: ${index}, Value: ${arrIn[index]}`); 
}

//While Loop
let whileLoop: number = 0;
while (whileLoop < 4) {
  console.log( "whileLoop: " + whileLoop )
  whileLoop++;
}

//do..while loop
let doWhileLoop: number = 1;
do {
    console.log("doWhileLoop: " + doWhileLoop )
    doWhileLoop++;
} while ( doWhileLoop < 4)

//Try Catch errors
function ejemplo1(valor: string){
 throw new Error(valor) 
}

try{
  ejemplo1("Este es un error");
}catch(error){
  log("error esperado: "+error)
}

//DIFICULTAD EXTRA

for(let i=10; i<=55; i++){
  if(i!=16 && i%2==0 && i%3!=0){
    log(`n°:${i}`);
  }
}