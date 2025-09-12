
let a=9
let b=12


console.log(`Operadores Aritmeticos`);
console.log(`La suma de ${a} + ${b} es igual a ${a+b}`);
console.log(`La resta de ${b} - ${a} es igual a ${b-a}`);
console.log(`La multiplicacion de ${b} * ${a} es igual a ${b*a}`);
console.log(`La division de ${b} / ${b} es igual a ${b/b}`);
console.log(`Operadores de Asignacion`);
console.log(`La asignacion de adicion es ${b +=a}`);
console.log(`La asignacion de resta es ${b -=a}`);
console.log(`La asignacion de multiplicacion es ${b *=a}`);
console.log(`La asignacion de division es ${b /=a}`);
console.log(`Operadores de comparacion`);
console.log(`El resultado de si ${b} es igual a ${b} es  ${b===b}`);
console.log(`El resultado de si ${b} es diferente de ${b} es  ${b!=b}`);
console.log(`El resultado de si ${b} es menor o igual${a} es  ${b<=a}`);
console.log(`El resultado de si ${b} es mayor o igual ${a} es  ${b>=a}`);
console.log(`Operadores logicos bit a bit`);
console.log(`La operacion AND binaria de ${a} y ${b} es  ${a & b}`);
console.log(`La operacion OR binaria de ${a} y ${b} es  ${a | b}`);
console.log(`La operacion XOR binaria de ${a} y ${b} es  ${a ^ b}`);
console.log(`Estructuras de control`);
/**Estructura condicional if else */
if (a<=b) {
    console.log(`El valor ${a} es menor o igual a ${b} `);
    
} else {
    console.log(`El valor ${b} es menor o igual a ${a} `);

}
/**Estructura condicional switch */
switch (b>a) {
    case true:
        console.log(`El valor ${b} es mayor que ${a} `);

        break;
    

    default:
        console.log(`El valor ${a} es menor o igual a ${b} `);

        break;
}
/**Estructura condicional for */
for (let i=10 ; i>=0; i--) {
    console.log(`El valor de i es ${i} `);

}
/**Estructura condicional while */
let j = 0;
while (j<9) { 
alert (j); 
j++;
console.log(`El valor de j es ${j} `);

}
/**Estructura condicional try catch */

function doSomething() {
    throw new Error('something terrible happened');
  }
  try {
    doSomething();
  } catch (e) {
    console.log(e); // Logs the error
  }

console.log('Los numeros comprendidos entre 10 y 55: ');

for (let k =10; k<=55; k++) {
    if ( (k!==16 && !(k%3 ===0 ) && k%2 === 0 ) || k===55) {
        console.log(k);

    }
    
}










