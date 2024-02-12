// #01 OPERADORES Y ESTRUCTURAS DE CONTROL

public class nwpablodeveloper {

    public static void main(String[] args) {
        
        int a, b, edad, contador;
        String texto, texto2;

        /*
            OPERADOR DE CONCATENACIÓN

            Utilizaremos el signo + para unir cadenas de textos u otras variables. 
        */
        titulo("Operador de concatenacion ( + ) ");
        String nombre = "Pablo";
        edad = 35;
        String concatenar = "Mi nombre es: " + nombre + " y tengo " + edad + " pirulos";
        System.out.println(concatenar);



        /*
            OPERADOR DE ASIGNACIÓN

            El operador de asignación va a evaluar todo lo que esta a la derecha
            del signo = y se lo va a asignar a la variable que esta a su izquierda
        */
        titulo("Operador de asignacion ( = )");
        texto = "Este contenido va pá la variable";
        System.out.println(texto);



        /* 
            OPERADORES ARITMETICOS

            sumar
            restar
            multiplicar
            dividir
            resto de la división 
        */
        titulo("Operadores Aritmeticos ( + , - , *, /, % )");
        a = 15;
        b = 7;
        int suma            = a + b;
        int resta           = a - b;
        int multiplicacion  = a * b;
        int division        = a / b;
        int resto           = a % b;
        System.out.println( "suma:              15 + 7 ---> " + suma );
        System.out.println( "resta:             15 - 7 ---> " + resta );
        System.out.println( "multiplicacion:    15 * 7 ---> " + multiplicacion );
        System.out.println( "division:          15 / 7 ---> " + division );
        System.out.println( "resto:             15 % 7 ---> " + resto );


        /* 
            OPERADORES DE ASIGNACIÓN COMPUESTA

            Se juntaron el operador de aritmetico con el de asignación. 
            Este atajo se puede realizar para otras operaciones además de la suma. 
            Es útil cuando la operación contiene como primer operando al 
            valor de la misma variable en la que se almacena el resultado.
        */
        titulo("Operador de asignacion compuesta ( signo= )");

        a = 35; b = 6;
        System.out.println("a = 35; b = 6 \n");

        System.out.println("a += b: ---> " + ( a += b ) );   // a = a + b  

        a = 35; b = 6;
        System.out.println("a -= b: ---> " + ( a -= b ) );   // a = a - b  

        a = 35; b = 6;
        System.out.println("a *= b: ---> " + ( a *= b ) );   // a = a + b  

        a = 35; b = 6;
        System.out.println("a /= b: ---> " + ( a /= b ) );   // a = a + b  

        a = 35; b = 6;
        System.out.println("a %= b: ---> " + ( a %= b ) );   // a = a % b  


        /*
            OPERADORES UNARIOS
            
        */
        titulo("Operadores unarios ( -, --, ++ )");

        // Operador unario, para cambiar el signo
        System.out.println("Operador unario para cambiar el signo Ej: \na = 35");
        a = 35;
        b = -a;
        System.out.println("b = -a ");
        System.out.println("b = "+ b + "\n"); 
        System.out.println("a = "+ a + "\n"); 
        
        // Suma pre-incremento
        // 1ro hace el incremento al suendo operando y luego lo asigna a la variable
        System.out.println("Suma unaria Ej: \na = 35");
        a = 35;
        b = ++a;
        System.out.println("b = ++a ");
        System.out.println("b = "+ b + "\n"); 
        System.out.println("a = "+ a + "\n"); 

        // Resta pre-decremento
        // 1ro hace el decremento al sugundo operando y leugo lo asigna a la variable
        System.out.println("Resta unaria Ej: \na = 35");
        a = 35;
        b = --a;
        System.out.println("b = --a ");
        System.out.println("b = "+ b + "\n");  
        System.out.println("b = "+ b + "\n"); 

        // Operador post-incremento
        // 1ro asigna el valor del sugundo operando a la variable y luego hace el incremento
        System.out.println("post-incremento Ej: \na = 35");
        a = 35;
        b = a++;
        System.out.println("b = a++ ");
        System.out.println("b = "+ b  );  
        System.out.println("a = "+ a + "\n");  

        // Operador post-decremento
        // 1ro asigna el valor del sugundo operando a la variable y luego hace el decremento
        System.out.println("post-decremento Ej: \na = 35");
        a = 35;
        b = a--;
        System.out.println("b = a++ ");
        System.out.println("b = "+ b  );  
        System.out.println("a = "+ a );  


        /* 
            OPERADORES RELACIONALES
            Devuelven un valor booleano ( true o false ) a partir de una comparación de 2 variables.
        */
        titulo("Operadores relacionales ( ==, !=, <, >, <=, >= ) ");
        a = 38;             
        b = 17;    
        texto = "Pablo";    
        texto2 = "Javier";        
        System.out.println("Invertir condicion          " + ( !true )); 
        System.out.println("38 es igual a 17 ?          " + ( a == b ));
        System.out.println("Pablo es igual a Javier?    " + ( texto == texto2 ) );
        System.out.println("38 es distinto a 17?        " + ( a != b ) );
        System.out.println("38 es menor a 17?           " + ( a < b ) );
        System.out.println("38 es mayor a 17?           " + ( a > b ) );


        /*
            OPERADORES CONDICIONALES 
            Realiza la comparación entre datos booleanos y da 
            como resultado otro valor booleano
        */
        titulo("Operadores condicionales ( ||, && )");
        a = 38;             
        b = 17;             
        texto = "Pablo";    
        texto2 = "Javier";  
        boolean ressultado;

        // || ( OR ) Una de las 2 o mas evaluaciones tiene que ser verdadera Ej. 1
        ressultado = (a == b) || ( texto == texto2 );
        System.out.println("38 es igual a 17 ? o Pablo es igual a Javier ? "+  ressultado);

        // || ( OR ) Una de las 2 o mas evaluaciones tiene que ser verdadera Ej. 2
        ressultado = (a == 38 ) || ( texto == texto2 );
        System.out.println("38 es igual a 38 ? o Pablo es igual a Javier ? "+  ressultado);

        // && ( AND )Las 2 o mas evaluaciones tiene que ser verdadera Ej. 1
        ressultado = (a == 38 ) && ( texto == "Pablo" );
        System.out.println("38 es igual a 38 ? y Pablo es igual a Pablo ? "+  ressultado);

        // && ( AND ) Las 2 o mas evaluaciones tiene que ser verdadera Ej. 2
        ressultado = (a == 38 ) && ( texto == texto2 );
        System.out.println("38 es igual a 38 ? y Pablo es igual a Javier ? "+  ressultado);


        /*
            OPERADOR TERNARIO 
            Si el resultado a a evaluar es verdadero devuelve un resultado luego de
            la primera expresión o caso contrario luego de la segunda expresión
        */
        titulo("Operador ternario ( ?: )");
        edad = 17; 
        var resultado = ( edad >= 18 )? "Es mayorcito" : "todavia no tiene preocupaciones";
        System.out.println(resultado);


        /*
            SENTENCIAS DE CONTROL
            Las sentencias de control se utilizan para ejecutar ciertos bloques de 
            codigo respecto a un resultado anterior 
        */
        // Sentencia de control If-Else
        titulo("Sentencia If-Else");
        
        if ( edad >= 18 ) {
            System.out.println("Es mayor de edad");
        } else {
            System.out.println("Todavia te falta para ser mayorcito");
        }

        // Sentencia de control Switch
        titulo("Sentencia de control switch");
        
        String mensaje;
        int numero = 8;
        
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
        System.out.println("Ejemplo 1: " + mensaje);
        
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
        System.out.println("Ejemplo 2: " + mensaje);


        /*
            SENTENCIA DE CONTROL CICLO While
            El ciclo while 1ro va a evualer que la condición que sea verdadera 
            para ejecutar el codigo de su interior, lo va a hacer 
            todas las veces necesarias hasta que la condición cambie a false
        */
        titulo("Sentencia de control While");
        
        contador = 0;
        while ( contador <= 4 ) {
            System.out.println( "Contador While: " + contador );
            contador++;
        }

        /*
            SENTENCIA DE CONTROL DO-WHILE
            1ro ejecuta el codigo dentro del bucle y luego verifica
            si la condición booleana es true, en caso que sea false
            se termina el bucle pero ya logramos almenos 1 vez
            el bloque de codigo
        */
        titulo("Sentencia Do-While");

        contador = 3;
        do {
            System.out.println("Contador Do-While: " + contador);
        } while ( contador > 5 ); 


        /*
            SENENTENCIA DE CONTROL FOR
            El ciclo for repite un codigo todas las veces que nosotros
            se lo indiquemos, el mismo recibe 3 parametros que son
            el 1ro, el contador
            2do la condición booleana
            3ro el incrementador del contador
        */
        titulo("sentencia ciclo For");
        
        // Ejemplo 1
        for (contador = 0; contador <= 8; contador++) {
            System.out.println("Ej. 1 - contador ciclo For: " + contador);    
        }
        
        System.out.println();
        // Ejemplo 2
        for (contador = 0; contador <= 9 ; contador += 2 ) {
            System.out.println("Ej. 2 - contador ciclo For: " + contador);    
        }

        /*
            USO DE LA PALABRA CONTINUE
            Cuando se encuentra la palabra CONTINUE dentro de un bucle
            la misma finaliza esa vuelta de bucle y pasa a la que sigue 
        */
        
        System.out.println();
        // Ejemplo 3
        for (contador = 0; contador <= 9 ; contador += 2 ) {
            if ( contador == 4 ) {
                System.out.println("Saltear cuatro");
                continue;
            }
            System.out.println("Ej. 3 - contador ciclo For: " + contador);    
        }

        /*
            USO DE LA PALABRA BREK
            Cuando se encuentra la palabra BREAK dentro de un bucle
            la misma da por finalizado todo el bucle sin importar
            si se cumple su condición final
        */
        
        System.out.println();
        // Ejemplo 4
        for (contador = 0; contador <= 9 ; contador += 2 ) {
            if ( contador == 6 ) {
                System.out.println("finalizar bucle");
                break;
            }
            System.out.println("Ej. 4 - contador ciclo For: " + contador);    
        }

        /*
            SENTENCIA DE CONTROL TRYCATCH
            Se utiliza para atrapar errores 
        */
        titulo("Sentencia de control TRYCATCH");
        try {
            System.out.println("Si todo va bien entro por aquí");
        } catch (Exception error) {
            System.out.println("Si hay errores entro por aquí");
            System.out.println("Ver error: " + error);
            // Por ejemplo conectar a un DB con una contraseña incorrecta
        } finally {
            // El finally es opcional
            System.out.println("Me voy a ejecutar siempre que use el FINALLY");
        }


        /*
            DIFICULTAD EXTRA (opcional):
            Crea un programa que imprima por consola todos los números comprendidos
            entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. 
        */
        titulo("Dificultad extra");

        for(int i = 10; i <= 55; i++ ) {
            if ( i == 55 ) System.out.println(i);
            if ( i % 2 != 0 ) continue;
            if ( i % 3 == 0 ) continue;
            if ( i == 16 )  continue;
            System.out.println(i);
        }

        System.out.println();
    }

    /*
        Un metodo para generar un linda vista para los titulos 🤘🤘🤘
    */
    public static void titulo(String titulo) {
        System.out.println("");
        System.out.println("==================================================");
        System.out.println(titulo);
        System.out.println("--------------------------------------------------");

    }

 }