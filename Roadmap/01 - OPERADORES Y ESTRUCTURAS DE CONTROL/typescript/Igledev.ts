// Tipos de Operadores en TypeScript
// 1º Aritméticos: Son operaciones básicas:
    // -- Suma
    let suma : number = 10 + 5;
    console.log(suma); // 15
    // -- Resta
    let resta : number = 10 - 5;
    console.log(resta); // 5
    // -- Multiplicación
    let multiplicacion : number = 10 * 5;
    console.log(multiplicacion); // 50
    // -- División
    let divisio : number = 10 / 5;
    console.log(divisio); // 2
    // -- Incremento
    let incremento : number = ++suma;
    // -- Decremento
    let decremento : number = --resta;
    console.log(divisio); // 2
// 2º Lógicos : Son operaciones que comparan 2 o más valores y devuelven un boolean
    let nombre1 : string = 'Igledev';
    let nombre2 : string = 'Igledeb';
    let valido : boolean = false;
    // -- Operador AND (&&)
    if(nombre1 === 'Igledev' && nombre2 === 'Igledeb'){valido = true}
    // Devuelve TRUE si los dos son validos
    // -- Operador OR (||)
    if(nombre1 === 'Igledev' || nombre2 === 'Igledeb'){valido = true}
    // Devuelve TRUE si alguno de los dos son validos
    // -- Operador NOT (!)
    let noes_dev : boolean = false;
    console.log(!noes_dev) // True
    // Devuelve TRUE porque niega que es un FALSE.
// 3º Comparación : Son Operadores que comparan
    // -- ==
    let valido2 : boolean = nombre1 == nombre2; // Devuelve TRUE si los dos nombres son iguales.
    // -- !=
    valido2 = nombre1 != nombre2; // Devuelve TRUE si los operadores no son iguales.
    // -- ===
    valido2 = nombre1 === nombre2; // Devuelve TRUE si los dos operadores coinciden en tipo y dato
    // -- !==
    valido2 = nombre1 !== nombre2; // Devuelve TRUE si los dos operadores no coinciden ni en tipo ni en dato
    // -- >
    valido2 = 10 > 5; // Devuelve TRUE si el operador izquierdo es más grande que el derecho
    // -- >=
    valido2 = 10 >= 10; // Devuelve TRUE si el operador izquierdo es más grande o igual que el derecho
    // -- <
    valido2 = 5 < 10; // Devuelve TRUE si el operador derecho es más grande que el izquierdo
    // -- <=
    valido2 = 10 <= 10; // Devuelve TRUE si el operador derecho es más grande o igual que el izquierdo
// 4º Asignación: Son Operadores que asignan un valor a sus operador izquierdo basandose en el derecho
    // -- Asignación    
    let num1 : number = 10; let num2 : number = num1;
    // -- Asignación de Adición
    num1 += num2;
    // -- Asignación de Resta
    num1 -= num2;
    // -- Asignación de Multiplicación
    num1 *= num2;
    // -- Asignación de División
    num1 /= num2;
    // -- Asignación de Residuó
    num1 %= num2;
    // -- Asignación de Exponenciación
    num1 **= num2;
    // -- Asignación de Desplazamiento a la izquierda
    num1 <<= num2;
    // -- Asignación de Desplazamiento a la derecha
    num1 >>= num2;
    // -- Asignación de Desplazamiento a la derecha sin tipo
    num1 >>>= num2;
    // -- Asignación AND bit a bit
    num1 &= num2;
    // -- Asignación XOR bit a bit
    num1 ^= num2;
    // -- Asignación OR bit a bit
    num1 |= num2;
    // -- Asignación AND lógico
    num1 &&= num2;
    // -- Asignación OR lógico
    num1 ||= num2;
    // -- Asignación de anulación lógico
    num1 ??= num2;
// 5º Identidad: Son operadores que nos permiten comparar la igualdad estricta entre valores
    // -- ===
    valido2 = nombre1 === nombre2; // Devuelve TRUE si los dos operadores coinciden en tipo y dato
    // -- !==
    valido2 = nombre1 !== nombre2; // Devuelve TRUE si los dos operadores no coinciden ni en tipo ni en dato
// 6º Pertenencia
    // -- Como total TypeScript no tiene operadores de pertenencia pero si tiene métodos propios como un .includes()
// 7º Bits
    // -- Operador AND a nivel de Bits
    let bits = 5 & 3;  // 0101 & 0011 = 0001
    console.log(bits);  // 1
    // -- Operador OR a nivel de Bits
    bits = 5 | 3;  // 0101 | 0011 = 0111
    console.log(bits);  // 7
    // -- Operador XOR a nivel de Bits
    bits = 5 ^ 3;  // 0101 ^ 0011 = 0110
    console.log(bits);  // 6
    // -- Desplazamiento a la izquierda
    bits = 5 << 1;  // 0101 << 1 = 1010
    console.log(bits);  // 10
    // -- Desplazamiento a la derecha
    bits = 5 >> 1;  // 0101 >> 1 = 0010
    console.log(bits);  // 2
    // -- Desplazamiento a la derecha sin signo
    bits = -5 >>> 1;  // 11111111111111111111111111111011 >>> 1 = 01111111111111111111111111111101
    console.log(bits);  // 2147483645
// 8º Ternarios
    let edadTer: number = 20;
    let mensaje : string = (edadTer >= 18) ? "Eres mayor de edad" : "Eres menor de edad";
// 9º Tipos de estructuras de control
    // If con sus variantes:
    let edad : number = 19
    // -- if
    if(edad > 18){console.log('Eres mayor de edad');}
    // -- if con else
    if(edad > 18){console.log('Eres mayor de edad')}else{console.log('Aun te queda')}
    // Si una condición no se cumple se hace la otra
    // -- if con elseif y else
    if (edad < 18) {
        console.log("Eres menor de edad.");
    } else if (edad >= 18 && edad < 65) {
        console.log("Eres un adulto.");
    } else {
        console.log("Eres un viejito.");
    }
    // -- switch
    let dia : number = 1;
    let diaSemana : string = '';
    switch(dia){
        case 1:
            diaSemana = 'Lunes';
            break;
        case 2:
            diaSemana = 'Martes';
            break;
        case 3:
            diaSemana = 'Miércoles';
            break;     
    }
    console.log(diaSemana);
    // Se ejecuta el código pero solo la porción de texto que coindice con el case, si se quita el break, se ejecutará todo para abajo
    // -- for
    for(let i : number = 0; i < 10; i++){console.log(i);} // Nos hace un bucle que vaya printando el estado de la i durante su ejecución
    // -- for-in
    for (let i in Object) {
        console.log(i)
        // Se ejecuta para cada propiedad del objeto
    }
    // -- for-of
    let numeros : Array<number> = [1,2,3,4,5,6,7,8,9,0];
    for (let e of numeros) {
        console.log(e);
    }
    // -- break
    for (let i : number = 0; i < 10; i++) {
        if (i === 8) {
            console.log(i);
            break; // termina el bucle si i es igual a 8
        }
    }
    for (let i : number = 0; i < 10; i++) {
        if (i === 8) {
            console.log(i);
            continue; // pasa a la siguiente iteración si i es igual a 8
        }
        // Se ejecuta en cada iteración, excepto cuando i es igual a 8
    }      
    // -- while
    let condicion : number = 0;
    while(condicion < 10){
        console.log(condicion); 
        condicion++;
    }
    // Se ejecuta mientras lo que haya en el while sea verdadero
    // -- dowhile
    do {
        console.log(condicion);
        condicion++;
    } while (condicion < 10);
    // Se ejecuta al menos una vez y luego mientras la condición sea verdadera
// 10º Ejercicio Extra
for(let i : number = 10; i <= 55; i++){
    if(i % 2 == 0 && i != 16 && i % 3 != 0){
        console.log(i);
    }
}