var _a;
var myNumber = 25;
var myString = "Hola Mundo";
console.log(myNumber);
console.log(myString);
// Declaramos dos nuevas variables por valor 
var myNumber2 = myNumber;
var myString2 = myString;
console.log(myNumber2);
console.log(myString2);
// Cambiamos el valor de las variables originales
myNumber = 50;
myString = "Adios Mundo";
console.log("El valor de variable numérica original es: " + myNumber + " y el valor de la variable numérica nueva es: " + myNumber2);
console.log("El valor de variable string original es: " + myString + " y el valor de la variable string nueva es: " + myString2);
// Ejemplo por referencia
var obj1 = {
    name: "Miguel",
    age: 25
};
console.log(obj1);
// Declaramos un nuevo objeto y le asignamos el valor del objeto original
var obj2 = obj1;
// Imprimimos el valor del nuevo objeto
console.log(obj2);
// Cambiamos el valor de una propiedad del objeto original
obj1.name = "Miguelex";
console.log("El valor de la propiedad name del objeto original es: " + obj1.name + " y el valor de la propiedad name del objeto nuevo es: " + obj2.name);
// Ejemplo de funcion con paso por valor
function changeValue(a) {
    a = 50;
}
var num = 25;
changeValue(num);
console.log(num);
// Ejemplo de funcion con paso por referencia
function changeValueObj(obj) {
    obj.name = "Miguelex";
}
var obj = {
    name: "Miguel",
    age: 25
};
changeValueObj(obj);
console.log(obj.name);
// Extra
function byValor(a, b) {
    var aux = a;
    a = b;
    b = aux;
    return [a, b];
}
function byReference(obj1, obj2) {
    var aux = obj1;
    obj1 = obj2;
    obj2 = aux;
    return [obj1, obj2];
}
var a = 5;
var b = 10;
var user1 = {
    name: "Miguel",
    age: 25
};
var user2 = {
    name: "Juan",
    age: 30
};
console.log("Antes de llamar a la función --> El valor de a es: " + a + " y el valor de b es: " + b);
_a = byValor(a, b), a = _a[0], b = _a[1];
console.log("Después de llamar a la función --> El valor de a es: " + a + " y el valor de b es: " + b);
console.log("Antes de llamar a la función --> El valor de user1 es: " + JSON.stringify(user1) + " y el valor de user2 es: " + JSON.stringify(user2));
var _b = byReference(user1, user2), newUser1 = _b[0], newUser2 = _b[1];
console.log("Despues de llamar a la función --> El valor de user1 es: " + JSON.stringify(newUser1) + " y el valor de user2 es: " + JSON.stringify(newUser2));
