// Operadores aritméticos:

    // Operador + (Suma)
        let a = 10;
        let b = 5;
        console.log(a + b);

    // Operador - (Resta)
        console.log(a - b);
    
    // Operador * (Multiplicación)
        console.log(a * b);
    
    // Operador / (División)
        console.log(a / b);
    
    // Operador % (Módulo)
        console.log(a % b);
    
    // Operador ++ (Incremento)
        console.log(++a);
    
    // Operador -- (Decremento)
        console.log(--b);
    
    // Operador ** (Potencia)
        console.log(a ** b);

// Operadores de asignación:

    // Operador = (Asignación)
        let numero = 5;
        console.log(numero);

    // Operador += (Asignación de suma)
        numero += 5;
        console.log(numero);
    
    // Operador -= (Asignación de resta)
        numero -= 5;
        console.log(numero);
    
    // Operador *= (Asignación de multiplicación)
        numero *= 5;
        console.log(numero);
    
    // Operador /= (Asignación de división)
        numero /= 5;
        console.log(numero);
    
    // Operador %= (Asignación de módulo)
        numero %= 5;
        console.log(numero);


// Operadores de comparación:

    // Operador == (Igualdad)
        console.log(5 == '5');  // true
    
    // Operador === (Igualdad estricta)
        console.log(5 === '5'); // false

    // Operador Desigualdad !==
        console.log(5!== '5'); // true
    
    // Operador > (Mayor que)
        console.log(10 > 5); // true
    
    // Operador < (Menor que)
        console.log(5 < 10); // true
    
    // Operador >= (Mayor o igual que)
        console.log(5 >= 5); // true
    
    // Operador <= (Menor o igual que)
        console.log(5 <= 5); // true
    

// Operadores lógicos:

    // Operador && (AND lógico)
        console.log(10 + 3 == 13 && 5 - 1 == 4); // true
    
    // Operador || (OR lógico)
        console.log(10 + 3 == 13 || 5 - 1 == 4); // true
    
    // Operador NOT logico !
        console.log(!(10 + 3 == 13)); // true


// Operadores de bit a bit:

    // Operador & (AND)
        console.log(10 & 3); // 2
    
    // Operador | (OR)
        console.log(10 | 3); // 11
    
    // Operador ^ (XOR)
        console.log(10 ^ 3); // 9
    
    // Operador ~ (NOT)
        console.log(~10); // -11
    
    // Operador << (Desplazamiento a la izquierda)
        console.log(10 << 3); // 80
    
    // Operador >> (Desplazamiento a la derecha)
        console.log(10 >> 3); // 2
    
    // Operador >>> (Desplazamiento a la derecha sin signo)
        console.log(10 >>> 3); // 2


// Operadores de cadena:

    // Operador + (Concatenación de cadenas)
        console.log('Hola' +'mundo'); // Hola mundo
    
    // Operador += (Asignación de concatenación)
        let cadena = 'Hola';
        cadena +='mundo';
        console.log(cadena); // Hola mundo


// Operadores de tipo:

    // Operador typeof (Devuelve el tipo de una variable)
        console.log(typeof 10); // number
    
    // Operador instanceof (Devuelve verdadero si un objeto es una instancia de un objeto)
        console.log(10 instanceof Number); // true

// Operadores unarios:

    // Operador + (Conversión a número)
        let str = "123";
        let numerito = +str;
        console.log(numerito); // 123
        console.log(typeof numerito); // "number"

   // Operador - (Negación unaria)
        let number = -3;
        let negatedNum = -number;
        console.log(negatedNum); // 3
   
   // Operador NOT lógico ! 
        let boolean = true;
        let notBoolean =!boolean;
        console.log(notBoolean); // false
   
   // Operador delete (Elimina una propiedad de un objeto)
        let obj = {a: 1, b: 2};
        delete obj.a;
        console.log(obj); // {b: 2}
   
   // Operador void (Evalúa una expresión y devuelve undefined)
        void 0; // undefined
   
   // Operador typeof (Devuelve el tipo de una variable)
        console.log(typeof 10); // "number"

   // Operador ~ (NOT a nivel de bits): invierte el valor binario de una variable

        let num = 5;          // 5 en binario es 00000000000000000000000000000101
        let inverted = ~num;  // ~5 en binario es 11111111111111111111111111111010
        console.log(inverted); // -6
   

// Operadores ternarios:

    let edad = 18;
    let voto = edad >= 18 ? "Puede votar" : "No puede votar";
    console.log(voto); // "Puede votar"


// Operadores de coma (para evaluar multiples expresiones en una declaracion):

    for (let i = 0, j = 2; i <= j; i++, j--){
        console.log(i, j); // 0 1, 1 0, 2 1
    }

// Operadores relacional in : Verifica si una propiedad concreta existe en un objeto.

    let persona = {
        nombre: "Juan",
        edad: 30
    };

    console.log("nombre" in persona); // true
    console.log("edad" in persona); // true
    console.log("direccion" in persona); // false

/* Ejercicio extra:
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

let numbers = [];

for (let i = 10; i <= 55; i++){
  if (i % 3 === 0){
    continue;
  } else if (i % 2 !== 0){
    continue;
  } else if (i === 16){
    continue;
  } else {
    numbers.push(i);
  }
}

console.log(numbers);





