// --------------------- OPERADORES ---------------------
  // DE ASIGNACION
    let resultAsignacion
    let y = 5
    resultAsignacion = y 
    console.log(resultAsignacion)
    resultAsignacion += y // de adición
    console.log(resultAsignacion)
    resultAsignacion -= y // de resta
    console.log(resultAsignacion)
    resultAsignacion *= y // de multiplicación
    console.log(resultAsignacion)
    resultAsignacion /= y // de división 
    console.log(resultAsignacion)
    resultAsignacion %= y // de residuo ej: x = 10  y = 3 --> 10/3 = 3 * 3 + 1 --> residuo = 1 --> x = 1
    console.log(resultAsignacion)
    resultAsignacion **= y // de exponenciación
    console.log(resultAsignacion)
    resultAsignacion <<= y // desplazamiento a la izquierda ej: x = 5 (0000 0101)  y = 2 --> 0001 0100 --> x = 20
    console.log(resultAsignacion)
    resultAsignacion >>= y // desplazamiento a la derecha ej: x = 20 (0001 0100)  y = 2 --> 0000 0101 --> x = 5
    console.log(resultAsignacion)
    resultAsignacion >>>= y // desplazamiento a la derecha sin signo
    console.log(resultAsignacion)
    resultAsignacion &= y // AND bit a bit ej: x = 5 (0000 0101)  y = 3 (0000 0011) --> 0000 0001 --> x = 1
    console.log(resultAsignacion)
    resultAsignacion ^= y // XOR bit a bit ej: x = 5 (0000 0101)  y = 3 (0000 0011) --> 0000 0110 --> x = 6
    console.log(resultAsignacion)
    resultAsignacion |= y // OR bit a bit ej: x = 5 (0000 0101)  y = 3 (0000 0011) --> 0000 0111 --> x = 7
    console.log(resultAsignacion)
    resultAsignacion &&= y // AND lógico si x = 0, null, '', false, undefined o Nan NO le asigna el valor de y
    console.log(resultAsignacion)
    resultAsignacion ||= y // OR lógico si x = 0, null, '', false, undefined o Nan SI le asigna el valor de y
    console.log(resultAsignacion)
    resultAsignacion ??= y // anulación lógica si x = null o undefined SI le asigna el valor de y
    console.log(resultAsignacion)

  // DE COMPARACION
    let resultComparacion
    resultComparacion = x == y // igualdad ej: 3 == 3 --> true '3' == 3 --> true
    console.log(resultComparacion)
    resultComparacion = x != y // desigualdad
    console.log(resultComparacion)
    resultComparacion = x === y // igualdad extricta ej: 3 === 3 --> true '3' === 3 --> false
    console.log(resultComparacion)
    resultComparacion = x !== y // desigualdad extricta
    console.log(resultComparacion)
    resultComparacion = x > y // mayor que
    console.log(resultComparacion)
    resultComparacion = x < y // menor que
    console.log(resultComparacion)
    resultComparacion = x >= y // mayor o igual que
    console.log(resultComparacion)
    resultComparacion = x <= y // menor o igual que
    console.log(resultComparacion)

  // ARITMETICOS
    let resultAritmeticos
    let ar1 = 5 
    let ar2 = 2
    resultAritmeticos = ar1 % ar2 // residuo
    console.log(resultAritmeticos)
    resultAritmeticos = ar1++ // incremento
    console.log(resultAritmeticos)
    resultAritmeticos = ar1-- // decremento
    console.log(resultAritmeticos)
    resultAritmeticos = -ar1 // negación unaria
    console.log(resultAritmeticos)
    resultAritmeticos = +'3' // positivo unario --> intenta convertir el operando en un número ej: +true = 1; +false, +null, +'', +' ' = 0; +undefined, +'hola' = NaN
    console.log(resultAritmeticos)
    resultAritmeticos = ar1 ** ar2 // exponenciación
    console.log(resultAritmeticos)

  // BIT A BIT
    let resultBitABit
    let bit1 = 5
    let bit2 = 3
    bit1 & bit2 // AND bit a bit ej: bit1 = 5 (0000 0101)  bit2 = 3 (0000 0011) --> 0000 0001 --> bit1 = 1
    console.log(resultBitABit)
    bit1 | bit2 // OR bit a bit ej: bit1 = 5 (0000 0101)  bit2 = 3 (0000 0011) --> 0000 0111 --> bit1 = 7
    console.log(resultBitABit)
    bit1 ^ bit2 // XOR bit a bit ej: bit1 = 5 (0000 0101)  bit2 = 3 (0000 0011) --> 0000 0110 --> bit1 = 6
    console.log(resultBitABit)
    ~ bit2 // XOR bit a bit ej: bit1 = 5 (0000 0101)  bit2 = 3 (0000 0011) --> 0000 0110 --> bit1 = 6
    console.log(resultBitABit)
    bit1 <<= bit2 // desplazamiento a la izquierda ej: bit1 = 5 (0000 0101)  bit2 = 2 --> 0001 0100 --> bit1 = 20
    console.log(resultBitABit)
    bit1 >>= bit2 // desplazamiento a la derecha de propagación de signo ej: bit1 = -20 (1110 1100)  bit2 = 2 --> 1111 1011 --> bit1 = -5
    console.log(resultBitABit)
    bit1 >>>= bit2 // desplazamiento a la derecha de relleno de ceros ej: bit1 = -20 (1110 1100)  bit2 = 2 --> 0011 1011 --> bit1 = 59
    console.log(resultBitABit)

  // LOGICOS
    let resultLogico
    resultLogico = true && false // AND lógico devuelve true unicamente si todos los valores son true
    console.log(resultLogico)
    resultLogico = true || false // OR lógico devuelve false unicamente si todos los valores son false
    console.log(resultLogico)
    resultLogico = !false // NOT lógico invierte el valor boleano
    console.log(resultLogico)

  // DE CADENA
    let resultCadena
    let cad1 = 'Hola '
    let cad2 = 'mundo'
    resultCadena = cad1 + cad2 // concatenación
    console.log(resultCadena)
    cad1 += cad2 // asignación abreviada 
    console.log(resultCadena)

  // CONDICIONAL (TERNARIO)
    let resultCondicional
    let edad = 18
    resultCondicional = edad >= 18 ? 'adulto' : 'menor' 
    console.log(resultCondicional)

  // COMA
    let com1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let com2 = [x, x, x, x, x];

    for (var i = 0, j = 9; i <= j; i++, j--)
      //                              ^
      console.log("com2[" + i + "][" + j + "]= " + com2[i][j]);

  // UNARIOS
    let resultUnarios
    let persona = {
      nombre: 'Pepe',
      edad: 68,
      casado: true
    }
    resultUnarios = delete persona.casado // elimina la propiedad de un objeto
    console.log(resultUnarios)
    resultUnarios = typeof persona.edad // devuelve el tipo de dato
    console.log(resultUnarios)
    resultUnarios = void (persona.edad) // devuelve undefined
    console.log(resultUnarios)

  // RELACIONALES
    let resultRalacionales
    let rel = [10, 20, 30, 40, 50]
    resultRalacionales = 3 in rel // devuelve true si la propiedad o el indice existe en el objeto
    console.log(resultRalacionales)
    resultRalacionales = rel instanceof Array // devuelve true si el objeto es del tipo del objeto especificado
    console.log(resultRalacionales)

// --------------------- ESTRUCTURAS DE CONTROL ---------------------
  // CONDICIONALES
    let puntuacion = 75;
    if (puntuacion >= 90) {  // IF 
        console.log("Puntuacón excelente!"); 
    } else if (puntuacion >= 70) {  // ELSE IF
        console.log("Buen trabajo!");
    } else {  // ELSE
        console.log("Puedes mejorar.");
    }

    let usuario = 'admin'
    switch (usuario) {
      case 'admin':
        console.log('Tú eres el admin')
        break;
      case 'registrado':
        console.log('Hola de nuevo!!')
        break;
      default: console.log('No estas registrado')
        break;
    }

  // BUCLES
    for (let i = 0; i < 5; i++) {  // FOR
      console.log("Iteración " + i);
    }
    let count = 0
    while (count < 3) {  //WHILE
        console.log("Valor del contador " + count);
        count++;
    }
    let number = 0;
    do {  // DO WHILE
        console.log("Number is " + number);
        number++;
    } while (number < 3);
    const arr = [3, 5, 7];
    arr.foo = "hola";
    for (let i in arr) { // FOR IN
      console.log(i); // logs "0", "1", "2", "foo"
    }
    for (let i of arr) {  // FOR OF
      console.log(i); // logs 3, 5, 7
    }

  // EXEPCIONES
    try {
        let data = JSON.parse("invalid json");
    } catch (error) {
        console.log("Error parsing JSON.");
    } finally {
        console.log("Execution completed.");
    }

// --------------------- DIFICULTAD EXTRA ---------------------

for (let i = 10; i <=55 ; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(`El numero ${i} es par, no es 16 y no es multiplo de 3`)
  }
}