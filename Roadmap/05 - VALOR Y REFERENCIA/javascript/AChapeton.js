//Variables por Valor
var a = 'Hola Mundo';
var b = a; //El valor de "a" se asigna a "b"
a += '!'; //Se modifica el valor de "a"
console.log("a", a);
console.log("b", b);

//Variables por Referencia
//Con estructuras, no se crea un nuevo valor, sino que ambas variables apuntan a un mismo espacio en memoria
var c = [1, 2, 3];
var d = c;
c.push(4);
console.log('c', c);
console.log('d', d);

//Funciones utilizando Variables por Valor
var firstFunction = function (str) {
    str = 'nuevo valor dentro de la funcion';
    return str;
};
var strOriginal = 'Fuera de la funcion';
console.log('Por valor - Dentro de la funcion: ', firstFunction(strOriginal));
console.log('Por valor - Fuera de la funcion: ', strOriginal);

//Funciones utilizando Varibles por Referencia
var secondFunction = function (arr) {
    arr.push('Moure');
    return arr;
};
var arrOriginal = ['Andres', 'Brais', 'Chape'];
console.log('Por referencia - Dentro de la funcion: ', secondFunction(arrOriginal));
console.log('Por referencia - Fuera de la funcion: ', arrOriginal);

// EJERCICIO EXTRA
//Funcion para intercarbiar variables por valor
var intercambiarValor = function (num1, num2) {
    var temp = num1;
    num1 = num2;
    num2 = temp;
    return [num1, num2];
};
var primerValor = 10;
var segundoValor = 5;

console.group('Valores antes del intercambio');
console.log('primerValor: ', primerValor);
console.log('segundoValor: ', segundoValor);
console.groupEnd();

var _a = intercambiarValor(primerValor, segundoValor), nuevoPrimerValor = _a[0], nuevoSegundoValor = _a[1];

console.group('Valores despues del intercambio');
console.log('primerValor: ', primerValor);
console.log('segundoValor: ', segundoValor);
console.groupEnd();

console.group('Nuevos valores intercambiados');
console.log('nuevoPrimerValor: ', nuevoPrimerValor);
console.log('nuevoSegundoValor: ', nuevoSegundoValor);
console.groupEnd();

//Funcion para intercarbiar variables por referencia
var intercambiarReferencias = function (user) {
    var temp = user.mainEmail;
    user.mainEmail = user.secondEmail;
    user.secondEmail = temp;
    return user;
};

var usuarioOriginal = {
    name: 'Andres',
    mainEmail: 'andres@new.com',
    secondEmail: 'andres@test.com',
};

console.group('Referencias antes del intercambio');
console.log('usuarioOriginal: ', usuarioOriginal);
console.groupEnd();

var nuevoUsuario = intercambiarReferencias(usuarioOriginal);

console.group('Referencias despues del intercambio');
console.log('usuarioOriginal: ', usuarioOriginal);
console.groupEnd();

console.group('Nuevas Referencias intercambiadas');
console.log('nuevoUsuario: ', nuevoUsuario);
console.groupEnd();
