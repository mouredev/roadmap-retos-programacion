let myNumber: number = 25;
let myString: string = "Hola Mundo";

console.log(myNumber);
console.log(myString);

// Declaramos dos nuevas variables por valor 

let myNumber2: number = myNumber;
let myString2: string = myString;

console.log(myNumber2);
console.log(myString2);

// Cambiamos el valor de las variables originales

myNumber = 50;
myString = "Adios Mundo";

console.log("El valor de variable numérica original es: " + myNumber + " y el valor de la variable numérica nueva es: " + myNumber2);
console.log("El valor de variable string original es: " + myString + " y el valor de la variable string nueva es: " + myString2);

// Ejemplo por referencia

interface User {
    name: string;
    age: number;
}

let obj1: User = {
    name: "Miguel",
    age: 25
};

console.log(obj1);

// Declaramos un nuevo objeto y le asignamos el valor del objeto original

let obj2: User = obj1;

// Imprimimos el valor del nuevo objeto

console.log(obj2);

// Cambiamos el valor de una propiedad del objeto original

obj1.name = "Miguelex";

console.log("El valor de la propiedad name del objeto original es: " + obj1.name + " y el valor de la propiedad name del objeto nuevo es: " + obj2.name);

// Ejemplo de funcion con paso por valor

function changeValue(a): void {
    a = 50;
}

let num = 25;
changeValue(num);
console.log(num);

// Ejemplo de funcion con paso por referencia

function changeValueObj(obj): void {
    obj.name = "Miguelex";
}

let obj = {
    name: "Miguel",
    age: 25
};

changeValueObj(obj);
console.log(obj.name);

// Extra

function byValor(a, b): number[] {
    let aux: number = a;
    a = b;
    b = aux;
    return [a, b];  
}

function byReference(obj1, obj2): User[] {
    let aux: User = obj1;
    obj1 = obj2;
    obj2 = aux;
    return [obj1, obj2];
}

let a: number  = 5;
let b: number = 10;

let user1: User = {
    name: "Miguel",
    age: 25
};

let user2: User = {
    name: "Juan",
    age: 30
};

console.log("Antes de llamar a la función --> El valor de a es: " + a + " y el valor de b es: " + b);

[a, b] = byValor(a, b);

console.log("Después de llamar a la función --> El valor de a es: " + a + " y el valor de b es: " + b);

console.log("Antes de llamar a la función --> El valor de user1 es: " + JSON.stringify(user1) + " y el valor de user2 es: " + JSON.stringify(user2));

let [newUser1, newUser2]: User[] = byReference(user1, user2);

console.log("Despues de llamar a la función --> El valor de user1 es: " + JSON.stringify(newUser1) + " y el valor de user2 es: " + JSON.stringify(newUser2));