//EJERCICIO:
//- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
//(Ten en cuenta que cada lenguaje puede poseer unos diferentes)

    //1. Operadores Aritméticos

        //Suma (+) para realizar sumas en los operandos.
        let a = 12;
        let b = 10;
        let suma = a + b;
        console.log(suma); //22
        
        //Resta (-) para restar el operando derecho del operando izquierdo.
        let c = 10;
        let d = 4;
        let resta = c - d;
        console.log(resta); //6
        
        //Multiplicación (*) para multiplicar los operandos.
        let e = 10;
        let f = 4;
        let multiplicacion = e * f; 
        console.log(multiplicacion); //40
        
        //División (/) para realizar la división en los operandos.
        let g = 10;
        let h = 4;
        let division = g / h;
        console.log(division); //2.5
        
        //Módulo (%). En informática, la operación módulo obtiene el resto entero de la división de un número entre otro.​
        let i = 10;
        let j = 4;
        let modulo = i % j;
        console.log(modulo); //2

        //Exponenciación (**) para calcular la base a la potencia del exponente (base^exponente).
        let k = 3;
        console.log(k**4); //81

        //Incremento (++) para aumentar el valor entero en uno.
        let l = 3;
        console.log(++l); //4

        //Decremento (--) que disminuye el valor entero en uno.
        let m = 3;
        console.log(--m); //2

        //Operador unario más (+) para intentar convertir el operando en un número si aún no lo es
        console.log(typeof("10")); // string
        console.log(typeof(+"10")); // number
        console.log(typeof(false)); // boolean
        console.log(typeof(+false)); // number

        //Operador de negación unaria (-), que devuelve la negación de su operando.
        let n = 10;
        console.log(-n); //-10

    //2. Operadores de asignación

        //Operador de asignación (=) para asignar el valor del operando derecho al operando izquierdo.
        let o = 10;
        console.log(o); //10

        //Operador de asignación de suma (+=) para sumar los valores de los operandos izquierdo y derecho y asignar el resultado al operando izquierdo.
        let p = 10;
        let q = 5;
        // Equivalent to p = p+q
        p += q;
        console.log(p); //15

        //Operador de asignación de resta (-=) para restar el operando derecho del operando izquierdo y asignará el resultado al operando izquierdo.
        let r = 10;
        let s = 5;
        // Equivalent to r = r-s
        r -= s;
        console.log(r); //5

        //Operador de asignación de multiplicación (*=) para multiplicar los valores de los operandos izquierdo y derecho y asigne el resultado al operando izquierdo.
        let t = 10;
        let u = 5;
        // Equivalent to t = t*u
        t *= u;
        console.log(t); //50

        //Operador de asignación de división (/=) para dividir el valor del operando izquierdo por el valor del operando derecho y asignar el resultado al operando izquierdo.
        let v = 10;
        let w = 5;
        // Equivalent to v = v/w
        v /= w;
        console.log(v); //2

        //Operador de asignación de resto (%=), divide el operando izquierdo por el operando derecho y asigna el resto al operando izquierdo.
        let x = 10;
        let y = 5;
        // Equivalent to x = x%y
        x %= y;
        console.log(x); //0

        //Operador de Asignación de Exponenciación (**=), eleva el operando izquierdo a la potencia del operando derecho y asigna el resultado al operando izquierdo.
        let z = 10;
        let aa = 5;
        // Equivalent to z = z**aa
        z **= aa;
        console.log(z); //100000

    // 3. Operadores de cadena
        //El operador de concatenación (+) se usa para concatenar (agregar) cadenas de texto o también llamados strings.
        let result = "If" + "Geek" + "Then";
        console.log(result); //IfGeekThen

    // 4. Operadores de comparación
        //Operador igual (==), devuelve verdadero si los operandos son iguales. Solo compara los valores de los operandos, ignorando su tipo al comparar.
        console.log(2 == 4); //false
        console.log("2" == 2); //true

        //Operador no igual (!=), devuelve verdadero si los operandos no son iguales. También ignora el tipo de operandos al comparar.
        console.log(2 != 4); //true
        console.log(2 !="2"); //false}

        //Operador de igualdad estricta (===), devuelve verdadero si los operandos son iguales. Compara tanto los valores como los tipos de operandos mientras compara.
        console.log(2 === 4); //false
        console.log("2" === 2); //false

        //Operador estricto no igual (!==), devuelve verdadero si los operandos no son iguales. También compara ambos: los valores y el tipo de operandos mientras compara.
        console.log(2 !== 4); //true
        console.log(2 !== "2"); //true

        //Operador mayor que (>), devuelve verdadero si el operando izquierdo es mayor que el operando derecho.
        console.log(10 > 4); // true
        console.log(5 > 5); //false

        //Operador mayor que o igual (>=), devuelve verdadero si el operando izquierdo es mayor o igual que el operando derecho.
        console.log(10 >= 4); //true
        console.log(5 >= 5); //true

        //Operador menor que (<), devuelve verdadero si el operando izquierdo es menor que el operando derecho.
        console.log(10 < 4); //false
        console.log(5 < 5 ); //false

        //Operador menor o igual (<=), devuelve verdadero si el operando izquierdo es menor o igual que el operando derecho.
        console.log(10 <= 4); //false
        console.log(5 <= 5); //true

    // 5. Operadores lógicos
        //AND lógico (&&)
        //Uso: expr1 && expr2
        //Devuelve expr1 si se puede convertir a falso; de lo contrario, devuelve expr2. Cuando se usa con valores booleanos, && devuelve verdadero si ambos operandos son verdaderos; de lo contrario, devuelve falso.
        console.log(true || false); //true

        //NO lógico (!)
        //Uso: !expr
        //Devuelve falso si su único operando se puede convertir en verdadero; de lo contrario, devuelve verdadero.
        console.log(!true); //false
        
    // 6. Operadores Bitwise
        //Operador bitwise AND(&) - Este operador realiza una operación AND booleana en cada bit de sus argumentos enteros.        
        // In binary-
        // 4: 100
        // 1: 001
        console.log(4 & 1); //0

        //Operador Bitwise OR (|) - Este operador realiza una operación OR booleana en cada bit de sus argumentos enteros.
        console.log(4 | 1); //5

        //Operador Bitwise XOR (^) - Este operador realiza una operación OR exclusiva booleana en cada bit de sus argumentos enteros.
        console.log(4 ^ 1); //5

        //Operador Bitwise NOT (~) - Este operador invierte todos los bits del operando.
        console.log(~4); // -5

        //Operador de desplazamiento a la izquierda (<<)
        console.log(4<<1); //8

        //Operador de desplazamiento a la derecha (>>)
        console.log(4>>1); //2

    // 7. Operadores especiales
        //Operador Ternario: El operador ternario es la abreviatura de la instrucción if-else. Asigna valor a una variable en base a una condición, la sintaxis de la misma es:
        
        condition ? value1 : value2

        //Si la condición es verdadera, el operador devuelve el valor de value1. De lo contrario, devuelve el valor de value2.

        let resultado = (200 > 100) ? "Yes" : "No";
        console.log(resultado); //Yes

        //Operador Typeof
        //Se utiliza para encontrar el tipo de datos de un valor o variable.
        console.log(typeof(100)); //number
        console.log(typeof("100")); //string

    //8. Tipo de datos de objeto en JavaScript
        //Puede crear un objeto vacío en JavaScript usando la sintaxis de "constructor de objetos" (nuevo Objeto()) o la sintaxis de "objeto literal" (llaves {...}).
        let obj1 = new Object();
        let obj2 = {};

        let obj = {
            "key1" : "value1",
            "key2" : "value2"
            }
        console.log(obj.key1); //value1

// - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan
//en tu lenguaje: Condicionales, iterativas, excepciones...
//- Debes hacer print por consola del resultado de todos los ejemplos.

    //Condicionales
        const mayorEdad = 18;

        if(mayorEdad >= 18){
            console.log("Es mayor de edad");
        }else {
            console.log("Es menor de edad");
        }
    
    //Ciclos, Bucles o Loops
    //For

    const pasos = 5;

    for(let paso = 0; paso <= pasos; paso++){
        console.log("Estoy dando el siguiente paso: " + paso);
    }

    //For in
    var dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];
    
    for(i in dias) {
    console.log(dias[i]);
    }

    //While
    const contador = 0;

    while(contador < 3) {
        contador++
    }
    console.log("Contador es igual a : ", contador);

    //Switch

    switch(tipoFruta){
        case "Naranjas":
            console.log("Las Naranjas cuestan $5");
            break;
        case "Manzanas":
            console.log("Las Manzanas cuestan $10");
            break;
        case "Fresas":
            console.log("Las Fresas cuestan $15");
            break;
        default:
            console.log("Disculpa, no tenemos ese tipo de fruta: ", tipoFruta);
            break;
    }

//DIFICULTAD EXTRA (opcional):
//Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
//Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

for( let num = 10; num <= 55; num++){
    if(num % 2 === 0 && num !== 16 && num % 3 !== 0){
        console.log(num);
    }
}



