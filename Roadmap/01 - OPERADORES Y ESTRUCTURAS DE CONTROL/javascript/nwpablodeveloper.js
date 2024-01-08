// #01 OPERADORES Y ESTRUCTURAS DE CONTROL

(() => {
    /*
        OPERADOR DE ASIGNACIÓN

        El operador de asignación va a evaluar todo lo que esta a la derecha
        del signo = y se lo va a asignar a la variable que esta a su izquierda
    */
    console.warn("Operador de asignacion ( = )");
    let texto = "Este contenido pá la variable";
    console.log(texto)
    /*
        OPERADOR DE CONCATENACIÓN

        Utilizaremos el signo + para unir cadenas de textos u otras variables. 
    */

    console.warn("Operador de concatenación ( + )");
    let nombre  = "Pablo";
    let edad    = 35;
    let frase   = `Me llamo ${ nombre } y tengo ${ edad } años`;
    console.log( frase )


    /* 
        OPERADORES ARITMETICOS

        sumar
        restar
        multiplicar
        dividir
        resto de la división 
    */
    console.warn("Operadores Aritmeticos ( + , - , *, /, % )");
    let a = 15;
    let b = 7;
    let suma            = a + b;
    let resta           = a - b;
    let multiplicacion  = a * b;
    let potencia        = a ** b;
    let division        = a / b;
    let resto           = a % b;
    console.log( "suma:              15 + 7 = " + suma );
    console.log( "resta:             15 - 7 = " + resta );
    console.log( "multiplicacion:    15 * 7 = " + multiplicacion );
    console.log( "multiplicacion:    15 ** 7 = " + potencia );
    console.log( "division:          15 / 7 = " + division );
    console.log( "resto:             15 % 7 = " + resto );


    /* 
        OPERADORES DE ASIGNACIÓN COMPUESTA

        Se juntaron el operador de aritmetico con el de asignación. 
        Este atajo se puede realizar para otras operaciones además de la suma. 
        Es útil cuando la operación contiene como primer operando al 
        valor de la misma variable en la que se almacena el resultado.
    */
    console.warn("Operador de asignacion compuesta ( signo= )");

    a = 35, b = 6;
    console.warn("a = 35; b = 6 \n");

    console.log("a += b = " + ( a += b ) );   // a = a + b  

    a = 35; b = 6;
    console.log("a -= b = " + ( a -= b ) );   // a = a - b  

    a = 35; b = 6;
    console.log("a *= b = " + ( a *= b ) );   // a = a + b  

    a = 35; b = 6;
    console.log("a /= b = " + ( a /= b ) );   // a = a + b  

    a = 35; b = 6;
    console.log("a %= b = " + ( a %= b ) );   // a = a % b  

    a = 2; b = 8;
    console.log("a **= b = " + ( a **= b ) );   // a = a ** b  
    /*
        OPERADORES UNARIOS
        
    */
    console.warn("Operadores unarios ( -, --, ++ )");

    // Operador unario, para cambiar el signo
    console.log("Operador unario para cambiar el signo Ej: \na = 35");
    a = 35;
    b = -a;
    console.log("b = -a ");
    console.log("b = "+ b + "\n"); 

    // Suma pre-incremento
    // 1ro hace el incremento al suendo operando y luego lo asigna a la variable
    console.log("Suma unaria Ej: \na = 35");
    a = 35;
    b = ++a;
    console.log("b = ++a ");
    console.log("b = "+ b + "\n"); 
    console.log("a = "+ a + "\n"); 


    // Resta pre-decremento
    // 1ro hace el decremento al sugundo operando y leugo lo asigna a la variable
    console.log("Resta unaria Ej: \na = 35");
    a = 35;
    b = --a;
    console.log("b = --a ");
    console.log("b = "+ b + "\n");  
    console.log("a = "+ a + "\n"); 

    // Operador post-incremento
    // 1ro asigna el valor del sugundo operando a la variable y luego hace el incremento
    console.log("post-incremento Ej: \na = 35");
    a = 35;
    b = a++;
    console.log("b = a++ ");
    console.log("b = "+ b  );  
    console.log("a = "+ a + "\n");  

    // Operador post-decremento
    // 1ro asigna el valor del sugundo operando a la variable y luego hace el decremento
    console.log("post-decremento Ej: \na = 35");
    a = 35;
    b = a--;
    console.log("b = a++ ");
    console.log("b = "+ b  );  
    console.log("a = "+ a );  

    /* 
        OPERADORES RELACIONALES
        Devuelven un valor booleano ( true o false ) a partir de una comparación de 2 variables.
    */
    console.warn("Operadores relacionales ( ==, !=, <, >, <=, >= ) ");
    a = 38;             
    b = 17;   
    c = "17";          
    let nombre2 = "Pablo";    
    let nombre3 = "Javier";  
    console.log("Invertir condición          " + ( !true ));       
    console.log("38 es igual a 37 ?          " + ( a == b ));
    console.log('"17" es igual a 17 ?        ' + ( c == b ));
    console.log('"17" es igual a 17 ?        ' + ( c === b ));
    console.log('"17" es igual a 17 ?        ' + ( c !== b ));
    console.log("Pablo es igual a Javier?    " + ( nombre2 == nombre3 ) );
    console.log("38 es distinto a 17?        " + ( a != b ) );
    console.log("38 es menor a 17?           " + ( a < b ) );
    console.log("38 es mayor a 17?           " + ( a > b ) );


    /*
        OPERADORES CONDICIONALES 
        Realiza la comparación entre datos booleanos y da 
        como resultado otro valor booleano
    */
    console.warn("Operadores condicionales ( ||, && )");
    a = 38;             
    b = 17;             
    nombre2 = "Pablo";    
    nombre3 = "Javier";  
    let ressultado;

    // || ( OR ) Una de las 2 o mas evaluaciones tiene que ser verdadera Ej. 1
    ressultado = (a == b) || ( nombre2 == nombre3 );
    console.log("38 es igual a 17 ? o Pablo es igual a Javier ? "+  ressultado);

    // || ( OR ) Una de las 2 o mas evaluaciones tiene que ser verdadera Ej. 2
    ressultado = (a == 38 ) || ( nombre2 == nombre3 );
    console.log("38 es igual a 38 ? o Pablo es igual a Javier ? "+  ressultado);

    // && ( AND )Las 2 o mas evaluaciones tiene que ser verdadera Ej. 1
    ressultado = (a == 38 ) && ( nombre2 == "Pablo" );
    console.log("38 es igual a 38 ? y Pablo es igual a Pablo ? "+  ressultado);

    // && ( AND ) Las 2 o mas evaluaciones tiene que ser verdadera Ej. 2
    ressultado = (a == 38 ) && ( nombre2 == nombre3 );
    console.log("38 es igual a 38 ? y Pablo es igual a Javier ? "+  ressultado);


    /*
        OPERADOR TERNARIO 
        Si el resultado a a evaluar es verdadero devuelve un resultado luego de
        la primera expresión o caso contrario luego de la segunda expresión
    */
    console.warn("Operador ternario ( ?: )");
    edad = 17; 
    var resultado = ( edad >= 18 )? "Es mayorcito" : "todavia no tiene preocupaciones";
    console.log(resultado);


    /*
        SENTENCIAS DE CONTROL
        Las sentencias de control se utilizan para ejecutar ciertos bloques de 
        codigo respecto a un resultado anterior 
    */
    // Sentencia de control If-Else
    console.warn("Sentencia If-Else");
    
    if ( edad >= 18 ) {
        console.log("Es mayor de edad");
    } else {
        console.log("Todavia te falta para ser mayorcito");
    }

    // Sentencia de control Switch
    console.warn("Sentencia de control switch");
    
    let mensaje;
    let numero = 8;
    
    // Ejemplo 1, si se cumple una condición se ejecuta cierto codigo, el breack le da finalización al Switch
    switch ( numero ) {
        case 1:
            mensaje = "Es uno";
            break;
        case 2:
            mensaje = "Es dos";
            break;
        case 5:
            mensaje = "Es cinco";
            break;
        case 8:
            mensaje = "Es ocho";
            break;
        default:
            mensaje = "No hay coincidencias";
            break;
    }
    console.log("Ejemplo 1: " + mensaje);
    
    // Ejemplo 2, pueden se pueden convinar combinaciones de Case para ejecutar cierto codigo
    numero = 13;
    switch ( numero ) {
        case 1:
        case 3:
        case 5:
            mensaje = "El numero puede ser uno, tres o cinco";
            break;
        case 6:
        case 7:
        case 8:
            mensaje = "El numero puede ser seis, siete u ocho";
            break;
        default:
            mensaje = "El numero no es ni uno, tres, cinco, seis, siete u ocho";
            break;
    }
    console.log("Ejemplo 2: " + mensaje);


    /*
        SENTENCIA DE CONTROL CICLO While
        El ciclo while 1ro va a evualer que la condición que sea verdadera 
        para ejecutar el codigo de su interior, lo va a hacer 
        todas las veces necesarias hasta que la condición cambie a false
    */
    console.warn("Sentencia de control While");
    
    contador = 0;
    while ( contador <= 4 ) {
        console.log( "Contador While: " + contador );
        contador++;
    }

    /*
        SENTENCIA DE CONTROL DO-WHILE
        1ro ejecuta el codigo dentro del bucle y luego verifica
        si la condición booleana es true, en caso que sea false
        se termina el bucle pero ya logramos almenos 1 vez
        el bloque de codigo
    */
    console.warn("Sentencia Do-While");

    contador = 3;
    do {
        console.log("Contador Do-While: " + contador);
    } while ( contador > 5 ); 


    /*
        SENENTENCIA DE CONTROL FOR
        El ciclo for repite un codigo todas las veces que nosotros
        se lo indiquemos, el mismo recibe 3 parametros que son
        el 1ro, el contador
        2do la condición booleana
        3ro el incrementador del contador
    */
    console.warn("sentencia ciclo For");
    
    // Ejemplo 1
    for (contador = 0; contador <= 8; contador++) {
        console.log("Ej. 1 - contador ciclo For: " + contador);    
    }
    
    console.log("");
    // Ejemplo 2
    for (contador = 0; contador <= 9 ; contador += 2 ) {
        console.log("Ej. 2 - contador ciclo For: " + contador);    
    }

    /*
        USO DE LA PALABRA CONTINUE
        Cuando se encuentra la palabra CONTINUE dentro de un bucle
        la misma finaliza esa vuelta de bucle y pasa a la que sigue 
    */
    
    console.log("");
    // Ejemplo 3
    for (contador = 0; contador <= 9 ; contador += 2 ) {
        if ( contador == 4 ) {
            console.log("Saltear cuatro");
            continue;
        }
        console.log("Ej. 3 - contador ciclo For: " + contador);    
    }

    /*
        USO DE LA PALABRA BREK
        Cuando se encuentra la palabra BREAK dentro de un bucle
        la misma da por finalizado todo el bucle sin importar
        si se cumple su condición final
    */
    
    console.log("");
    // Ejemplo 4
    for (contador = 0; contador <= 9 ; contador += 2 ) {
        if ( contador == 6 ) {
            console.log("finalizar bucle");
            break;
        }
        console.log("Ej. 4 - contador ciclo For: " + contador);    
    }

    /*
        SENTENCIA DE CONTROL TRYCATCH
        Se utiliza para atrapar errores 
    */
    console.warn("Sentencia de control TRYCATCH");
    try {
        console.log("Si todo va bien entro por aquí");
    } catch (error) {
        // EXPLOTO LA APP
        console.log("Si hay errores entro por aquí");
        console.error("Causa del error" , error)
        // Por ejemplo conectar a un DB con una contraseña incorrecta
    } finally {
        // El finally es opcional
        console.log("Me voy a ejecutar siempre que use el FINALLY");
    }


    /*
        DIFICULTAD EXTRA (opcional):
        Crea un programa que imprima por consola todos los números comprendidos
        entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. 
    */
    console.warn("Dificultad extra");
    let nro = 9;
    while( nro < 55 ){
        nro++
        if( nro == 55 ) console.log(nro)
        if( nro == 16 ) continue;
        if( nro % 3 == 0 ) continue;
        if( nro % 2 != 0 ) continue;
        console.log(nro)
    }

})()
