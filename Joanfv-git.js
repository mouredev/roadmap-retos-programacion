//Operadores Aritméticos
console.log("Suma:" + 5 + 5);
console.log("Resta:" + 5 - 5);
console.log("Multiplicación:" + 5 * 5);
console.log("División:" + 5 / 5);
console.log("Módulo:" + 5 % 5);
console.log("Incremento:" + 5++);
console.log("Decremento:" + 5--);

//Operadores Logicos
console.log("AND:" + (true && true));
console.log("OR:" + (true || false));
console.log("NOT:" + !true);

//Operadores de comparación
console.log("Igualdad:" + (5 == 5));
console.log("Desigualdad:" + (5 != 5));
console.log("Mayor que:" + (5 > 5));
console.log("Menor que:" + (5 < 5));
console.log("Mayor o igual que:" + (5 >= 5));
console.log("Menor o igual que:" + (5 <= 5));

//Operdaores de asignación
let a = 5;
console.log("Asignación:" + a);
a += 5;
console.log("Suma:" + a);
a -= 5;
console.log("Resta:" + a);
a *= 5;
console.log("Multiplicación:" + a);
a /= 5;
console.log("División:" + a);
a %= 5;
console.log("Módulo:" + a);

//Operadores de identidad
console.log("Igualdad de valor y tipo:" + (5 === 5));
console.log("Desigualdad de valor y tipo:" + (5 !== 5));

//Operadores de pertenencia
let b = [1, 2, 3, 4, 5];
console.log("Incluido:" + (5 in b));
console.log("No incluido:" + (6 in b));

//Estructuras de control

//Estructuras de control de condicionales
//If
let c = 5;
if (c == 5) {
    console.log("Es 5");
} else if (c == 6) {
    console.log("No es 5");
}   else {
    console.log("No es 5 ni 6");
}
//Switch
let d = 5;
switch (d) {
    case 5:
        console.log("Es 5");
        break;
    case 6:
        console.log("Es 6");
        break;
    default:
        console.log("No es 5 ni 6");
}

//Estructuras de control de iteración
//While
let e = 5;
while (e > 0) {
    console.log(e);
    e--;
}
//Do-While
let f = 5;
do {
    console.log(f);
    f--;
}
while (f > 0);
//Break
let l = 0;
while (l < 5) {
    console.log(l);
    l++;
    if (l == 3) {
        break;
    }
}
//Continue
let m = 0;
while (m < 5) {
    m++;
    if (m == 3) {
        continue;
    }
    console.log(m);
}
//For
for (let g = 0; g < 5; g++) {
    console.log(g);
}
//For-In
let h = [1, 2, 3, 4, 5];
for (let i in h) {
    console.log(h[i]);
}
//For-Of
let j = [1, 2, 3, 4, 5];
for (let k of j) {
    console.log(k);
}

//Estructuras de control de excepciones
try {
    throw "Error";
}
catch (error) {
    console.log(error);
}
finally {
    console.log("Fin");
}

//Ejericio extra
let array = [];
for (let n = 10; n < 56; n++) {
    if (n % 2 == 0 && n!=16 && n % 3 != 0) {
        array.push(n);
    }
    
}
console.log(array);



