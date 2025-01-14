/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */


function mecanismo1 () {  
  console.log('\nUsando un bucle for');
  for (let i = 1; i <= 10; i++) {
    console.log(i);    
  }
}

function mecanismo2 () {
  console.log('\nUsando un bucle while');
  let i=1
  while (i<=10) {
    console.log(i);
    i++;
  }
}

function mecanismo3 () {
  console.log('\nUsando un bucle do while');
  let i=1
  do {
    console.log(i);
    i++;    
  } while (i<=10);
}

function mecanismo4(desde, hasta) {
  if (hasta > 0) {
    console.log(Math.abs(hasta-10) + 1);
    mecanismo4(desde, hasta -1)
  }
  
}

function mecanismo5() {
  console.log('\nUsar foreach');
  let array = []
  for (let index = 1; index <= 10; index++) {
    array.push(index)    
  }
  array.forEach((element) => console.log(element))
}

function mecanismo5() {
  console.log('\nUsar for in');
  let array = []
  for (let index = 1; index <= 10; index++) {
    array.push(index)    
  }
  for (const i in array) {
    console.log(i);
  }
}

function mecanismo6() {
  console.log('\nbucle while(true)');
  let i=1;
  while(true) {
    if (i<=10) {
      console.log(i)
      i++      
    } else {
      break;
    }
  }
}



mecanismo1();
mecanismo2();
mecanismo3();
console.log('Usando una funcion recursiva');
mecanismo4(1, 10);
mecanismo5();
mecanismo6();

