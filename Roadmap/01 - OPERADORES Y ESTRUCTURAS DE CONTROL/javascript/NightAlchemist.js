//Operadores de asignación
//Asignacion
console.log('//Operadores de asignación');
   const x = 'asignacion';
   console.log("Resultado de la asignacionde. Operacion -> (x = 'asignacion'):"+ x);
// Asignacion de Adicion
    let y = 0;
    y += 2;
    console.log("Resultado de la asignacionde de adicion, Operqacion -> (y += 2):"+ y);
    //Asignacion de resta
    let e = 0;
    e -= 4;
    console.log('Resultado de la asignacionde Resto. Operacion -> (e -= 4):'+ e);

//Operadores con Desestructuración
//Sin desestructuracion
 let comida = ['pera','manzana','azucar'];
 //Con desestructuracion
 let [pera,manzana,azucar] = comida;
 
 console.log(`let comida = ['pera','manzana','azucar']; 
    //Sin desestructuracion
    La comida[0]=${comida[0]}
    La comida[1]=${comida[1]}
    La modida[2]=${comida[2]}

    //Con desestructuracion
    let [pera,manzana,azucar] = comida;
    La comida en la posicion 0 es: ${pera};
    La comida en la posicion 1 es: ${manzana};
 `);

 //Operadores de comparación
 let var1 = 1;
 let var2 = 3;
 console.log('Operadores de comparación');
 
 console.log(` 
 let var1 = 1;
 let var2 = 3;
 var1 == 1:${var1 == 1};
 var2 != 3:${var2 != 3};
 var1 >= 2:${var1 >= 2};
 var1 <= 2:${var1 <= 2};
 `)
 


//Operadores aritmeticos
console.log('Operadores aritmeticos');
let suma = 2 + 4;
console.log(`La suma  de 2 + 4 es:${suma}`);

 let resta= 2-1;
console.log(`La resta de 2-1 es:${resta}`);

let multiplicacion = 2*5;
console.log(`La multiplicacion de 2*5 es:${multiplicacion}`);

let divicion = 10 / 2;
console.log(`La divicion de 10/2 es:${divicion}`);

let residuo = 12 / 5;
console.log(`El residuo de 12/5 es:${residuo}`);


//Operadores lógicos
console.log('Operadores lógicos');
let num1 = true;
let num2 = false;
console.log(`
let num1 = true;
let num2 = false;
 console.log(num1 && num2); // Se espera un false ->: ${(num1 && num2)}
 console.log(num1 || num2);// Se espera un true ->: ${(num1 || num2)} 
 console.log(!num1);// Se espera un false ->: ${(!num1)}
 `);

 //Estructura de Control
 //Condicional if
 console.log("//Estructura de Control");
 console.log(" //Condicional if");
 let auto = 'fiat'
if( auto == 'ford'){
    console.log(`Mi aunto es un:${auto}`);
}else if(auto == 'fiat'){
    console.log(`Mi aunto es un:${auto}`);
}else{
    console.log('No es ni uno u otro');
}
//operador ternario
console.log("//operador ternario");
auto === "ford"? console.log(`Mi auto es un: ${auto}`): console.log("Tu auto no es Ford");

//switch
console.log("//Switch case");
let piso = 5;
console.log("Quiero ir a mi apartamento que esta en el piso:"+piso);

switch (piso){
  case 10:
    calificacion = "PenHouse";
    break;
    case 8:
    calificacion = "No es tu piso";
    break;
  case 7:
  case 5:
    calificacion = "Llegamos a tu Piso:"+piso+", por favor bajase aquí";
    break;
  case 5:
  case 4:
  case 3:
  case 2:
  case 1:
  case 0:
    calificacion = "Pisos bajos";
    break;
  default:
    // Cualquier otro caso
    calificacion = "Emergencia se ha ido la electricidad";
    break;
}
console.log(calificacion);

//Esctructura de Control
//While
console.log("//Esctructura de Control - While");
let numero = 0;
while(numero <= 4){
  console.log("El numero actual es:"+numero);
  numero +=1;
}
//Do While
console.log("Do-While");
do{
  console.log("Me ejecute con el Do While aun y que la condicion no sea True")
  numero += 2;
}
while(numero < 0);

//For
console.log("Bucle For")
for(let i = 20;i > 9; --i){
  console.log(`Soy for en:${i}`);
}

for (let i = 0; i < 11; i++) {
  if (i == 5) {
    continue; // Para saltar en esta condicion
  }
  console.log("Valor de i:", i);
}


//Dificultad Extra
console.log("Dificultad Extra");
for (let a = 55; a >= 10; a--){
  if(a%2 == 0 && a != 16 && a%3 !=0){
    console.log(a);
  }  
}
