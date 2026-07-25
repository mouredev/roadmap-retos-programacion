//* función sin paramatros ni retorno
let saludo = () => {
  console.log("hola a todos ");
};

//* función con parametros

let multiplicacion = (num_1, num_2) => {
  console.log("multiplicacion: " + num_1 * num_2);
};

//* funcion con retorno

let suma = (num_1, num_2) => {
  return num_1 + num_2;
};

//* funcion dentro de otra
function ingresar(numero) {
  let divicion = () => {
    return numero / 3;
  };
  return divicion();
}
// variable global
let variable_global = "hola, soy global";

let variable = () => {
  let variable_local = "hola, soy local";
  console.log(variable_local);
  console.log(variable_global);
};

// ejercicio extra

function extra(biz, buzz) {
  let contador = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 15 == 0) {
      console.log(biz + buzz);
    } else if (i % 5 == 0) {
      console.log(buzz);
    } else if (i % 3 == 0) {
      console.log(biz);
    } else {
      contador++;
    }
  }
  return contador;
}
//* llamado a las funciones
saludo();
multiplicacion(5, 6);
console.log("suma: " + suma(5, 8));
console.log(ingresar(6));
variable();
let contador = extra("biz", "buzz");
console.log("el numero que no se imprimio un texto es: " + contador);
