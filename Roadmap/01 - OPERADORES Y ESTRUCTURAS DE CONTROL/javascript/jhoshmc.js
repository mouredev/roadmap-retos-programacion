let a = 6;
let b = 4;
const verdadero = true;
const falso = false;
//* aritmeticos
function operaciones_aritmeticas() {
  let multiplicacion = a * b;
  let divicion = a / b;
  let suma = a + b;
  let resta = a - b;
  let resto = a % b;
  console.log("\t aritmeticos: ");
  console.log(a + " + " + b + " = " + suma);
  console.log(a + " - " + b + " = " + resta);
  console.log(a + " * " + b + " = " + multiplicacion);
  console.log(a + " / " + b + " = " + divicion);
  console.log(a + " % " + b + " = " + resto);
}

//*operaciones logicos
function logicos() {
  let and_logico = a && b;
  let or_logico = a || b;
  let not_logico = !verdadero;
  console.log("\t operaciones logicas");
  console.log("verdadero o 1 " + " = " + verdadero);
  console.log("falso o 0 = " + falso);
  console.log(a + " && " + b + " = " + and_logico);
  console.log(a + " || " + b + " = " + or_logico);
  console.log("!" + verdadero + " = " + not_logico);
}

//* operaciones de comparacion
function comparacion() {
  let a_cadena = a.toString(); // convirte el nuemero en una cadena
  let igualdad_media = a == a_cadena; // no toma en cuenta el tipo de la variable
  let igualdad_estricta = a === a_cadena;
  let mayor = a > b;
  let menor = a < b;
  let mayor_igual = a >= b;
  let menor_igual = a <= b;
  let diferentes_medio = a != a_cadena; // no toma en cuenta el tipo de dato
  let diferentes_estricto = a !== a_cadena; // toma en cuenta el tipo de dato
  console.log("\t comparacion");
  console.log(a + " == " + a_cadena + " = " + igualdad_media);
  console.log(a + " === " + a_cadena + " = " + igualdad_estricta);
  console.log(a + " > " + b + " = " + mayor);
  console.log(a + " < " + b + " = " + menor);
  console.log(a + " >= " + b + " = " + mayor_igual);
  console.log(a + " <= " + b + " = " + menor_igual);
  console.log(a + " != " + a_cadena + " = " + diferentes_medio);
  console.log(a + " !== " + a_cadena + " = " + diferentes_estricto);
}

//*asignacion
function asignacion() {
  let n = 0;
  console.log(" n == " + n);
  console.log("n ahora le asignamos 5; n=5");
  n = 5;
  console.log("n= " + n);
}
//* pertenencia
function pertenencia() {
  let arr = [1, 2, 3, 4, 5, 6];
  console.log(arr.includes(5));
  console.log(arr.includes(8));
}
//* operadodes bit a bit
function bit() {
  let A = "1010";
  let B = "1011";
  console.log(A + " & " + B + " = " + (A & B));
  console.log(A + " | " + B + " = " + (A | B));
  console.log(A + " XOR " + B + " = " + (A ^ B));
}
//* estructuas de control
function control() {
  //* condicionales
  if (4 == "4") {
    console.log("es verdad porque == no ve el tipo del dato");
  }

  let c = 4 === "4" ? " " : "es falsa porque === si ve el tipo de dato";
  console.log(c);

  //* bucles
  console.log("for");
  for (let i = 0; i < 5; i++) {
    console.log(i);
  }
  console.log("while");
  while (a > 1) {
    console.log(a);
    a--;
  }
  console.log("doWhile");
  do {
    console.log(a);
    a++;
  } while (a <= 6);
}
//* excepciones (manejo de errores)
function excepciones() {
  try {
    throw "Error";
  } catch (error) {
    console.log(error);
  } finally {
    console.log("Fin");
  }
}

//* dificultad extra
function extra() {
  let i = 10;
  let fin = 55;
  for (i; i <= 55; i++) {
    if ((i % 2 === 0 && i !== 16 && i % 3 !== 0) || i === fin) {
      console.log(i);
    }
  }
}

operaciones_aritmeticas();
logicos();
comparacion();
asignacion();
pertenencia();
bit();
control();
// excepciones()
extra();
