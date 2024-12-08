// #01 - OPERADORES Y ESTRUCTURAS DE CONTROL

let x = 0;
let y = 1;

// OPERADORES
console.clear();
console.log(`\nx:${x} \ny: ${y} \n\n`);
console.log("OPERADORES EN JS:\n");
console.log("x=y:", (x = y));
x = 0;
console.log("Operador de adición");
console.log("x+y:", x + y);
console.log("Operador de incremento");
console.log("x++:", x++);
x = 0;
console.log("Operador de resta");
console.log("x-y:", x - y);
console.log("Operador de decremento");
console.log("x--:", x--);
x = 0;
console.log("Operador de multiplicación");
console.log("x*y:", x * y);
console.log("Operador de división");
console.log("x/y:", x / y);
console.log("Operador de residuo");
console.log("x%y:", x % y);
console.log("Operador de exponenciación");
console.log("x**y:", x ** y);

console.log("Operador de desplazamiento a la izquierda");
console.log("x<<y:", x << y);

console.log("Operador de desplazamiento a la derecha");
console.log("x>>y:", x >> y);

console.log("Operador de desplazamiento a la derecha sin signo");
console.log("x>>>y:", x >>> y);

console.log("Operador AND bit a bit");
console.log("x&y:", x & y);

console.log("Operador XOR bit a bit");
console.log("x^y:", x ^ y);

console.log("Operador OR bit a bit");
console.log("x|y:", x | y);

console.log("Operador AND lógico");
console.log("x&&y:", x && y);

console.log("Operador OR lógico");
console.log("x||y:", x || y);

console.log("Operador de anulación lógica");
console.log("x??y:", x ?? y);

// EJEMPLOS CON ESTRUCTURAS DE CONTROL
console.log("\n\nEJEMPLOS CON ESTRUCTURAS DE CONTROL\n\n");
console.log("CONDICIONALES\n");

const condicional = (x, y) => {
  if (x > y) {
    return "x>y";
  } else if (x == y) {
    return "x==y";
  } else {
    return "x<y";
  }
};

console.log(
  "if(x>y){\nreturn 'x>y'\n} else if(x==y){\nreturn 'x==y'\n} else {\nreturn 'x<y'\n}\n\n Resultado: ",
  condicional(x, y)
);

// SWITCH

console.log("\n\nSWITCH");
switch (x) {
  case 1:
    console.log("x es 1");
    break;
  case 2:
    console.log("x es 2");
    break;
  default:
    console.log("x es otro valor");
}

console.log("\n\nFOR");

for (let i = 0; i < 10; i++) {
  console.log(i);
}

console.log("\n\nWHILE ");

while (x < 10) {
  console.log(x);
  x++;
}

x = 0;

console.log("\n\nDO WHILE ");

do {
  console.log(x);
  x++;
} while (x < 5);

x = 0;

console.log("\n\nEJECICIO EXTRA\n");

for (let i = 10; i <= 55; i++) {
  if (i != 16 && !(i % 3 == 0) && i % 2 == 0) console.log(i);
}

console.log(
  "\n\nGracias por su tiempo.\nSi lees esto vas a tener una vida muy exitosa. \nBendiciones <3"
);
