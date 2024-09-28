//Asignacion por valor
//*Esto sucede en variables de tipo primitivos (string, number, boolean, etc)

let deporte = 'running';
let deporte2 = deporte;

deporte = 'ciclismo';

console.log(deporte);//Se cambia el valor de la variable de 'running' a 'ciclismo'
console.log(deporte2);//Sigue mostrando 'running' porque es el primer valor con el que fue declarado

//Asignacion por referencia 
//*Esto sucede en tipos de datos objetos (objeto, array, funcion)

let zapatilla = {
    marca: 'Adidas'
}
let modelo = zapatilla;

// console.log(zapatilla); *Se imprimen ambas variables con los mismos valores*
// console.log(modelo);

zapatilla.marca = 'Nike';//Se cambia el valor de marca

console.log(zapatilla);//Ambos pasan a cambiar su valor en marca
console.log(modelo);

//Funcion con asignacion por valor

 function xValor(n1){
    n1 = 12345;
    console.log(n1);
 }
 xValor();

n1 = 54321;
xValor(); //No se modifica el valor de n1.

console.log(n1); //Se imprime el nuevo valor de n1.

//Funcion con asignacion por referencia.

function xReferencia(lista){
    lista.push(4);
}
let miArray = [1, 2, 3];
xReferencia(miArray);
console.log(miArray);
