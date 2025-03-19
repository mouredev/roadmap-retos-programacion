//Operadores en JavaScript

//✅ Operadores aritmeticos
  let suma = 1 + 2;
  let resta = 2 - 1;
  let division = 4 / 2;
  let multiplicacion = 2 * 2;
  let residuo = 8 % 2;
  let exponenciacion = 2 ** 8;

//✅ Operadores relacionales
  // in
  let micoche = { marca: "Honda", modelo: "Accord", año: 1998 };
  "marca" in micoche; // devuelve true
  "modelo" in micoche; // devuelve true
  // instanceOf
  let color1 = new String("verde");
  console.log(color1 instanceof String);
  //< menor que
  let a = 10 < 11;
  //> mayor que 
  let b = 11 > 10;
  //<= menor igual que
  let c = 10 <= 10;
  //>= mayor igual que
  let d = 11 >= 11;

  //✅ Operadores de igualdad
    //operador de igualdad
    let e = 10 == 10
    //operador de desigualdad
    let f = 10 != 9
    //operador de igualdad estricta
    let g = 10 === 10
    //operador de disigualda estricta
    let h = 10 !== 9

  //✅ Operadores de desplazamiento binario
    console.log(9 << 3);
    console.log(9 >> 3);
    console.log(-9 >>> 3)

  //✅ Operadores binarios bit a bit
  console.log(14 & 9);
  console.log(13 | 2);
  console.log(11 ^ 1);

  //✅ Operadores logicos binarios y operador ternario
  10 === 10 && 2 === 2
  10 === 10 || 2 === 2 ? true : false

  // Operadores de  asignacion
  let x = 5;   // Operador de asignación simple (=)
  let y = 10;
  y += 5;      // Operador de asignación de suma (+=)
  let z = 15;
  z -= 3;      // Operador de asignación de resta (-=)
  let l = 4;
  l *= 2;      // Operador de asignación de multiplicación (*=)
  let m = 8;
  m /= 4;      // Operador de asignación de división (/=)
  let k = 7;
  k %= 3;      // Operador de asignación de módulo (%=)
  let n = 2;
  n **= 3;     // Operador de asignación de exponenciación (**=)

  for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
      console.log(`${i} es par y cumple con las condiciones`);
    }
  }
  