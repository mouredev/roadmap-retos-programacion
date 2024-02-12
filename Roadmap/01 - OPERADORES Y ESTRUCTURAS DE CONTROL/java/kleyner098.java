
public class kleyner098 {

    public static void main(String[] args) {
        
        /*
        * EJERCICIO:
        * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
        *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
        *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
        * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
        *   que representen todos los tipos de estructuras de control que existan
        *   en tu lenguaje:
        *   Condicionales, iterativas, excepciones...
        * - Debes hacer print por consola del resultado de todos los ejemplos.
        *
        * DIFICULTAD EXTRA (opcional):
        * Crea un programa que imprima por consola todos los números comprendidos
        * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
        *
        * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
        */

        //Operador de asignación (=)
        System.out.println("Operador de asignación-------------------------------");
        int num1 = 1;                               //Asigna un valor o expresión a una variable
        System.out.println(num1);

        // Operadores aritméticos (+,-,*,/,%)
        System.out.println("Operadores aritméticos-------------------------------");
        int suma = 6+1;                             //Suma 
        System.out.println(suma);
        int resta = 10-2;                           //Resta
        System.out.println(resta);
        //El operador - tambien sirve para cambiar el signo de la expresión
        int numPositivo = 43;
        int numNegatvo = -numPositivo;
        System.out.println(numNegatvo);
        int multipilcacion = 4*5;                   //Multiplicación
        System.out.println(multipilcacion);
        int division = 50/5;                        //División
        System.out.println(division);
        int modulo = 7%3;                           //Módulo. Devuelve el resto de una división. Ej: 7/3 = 2 y el resto es 1
        System.out.println(modulo);

        //Operadores aritméticos incrementales (++,--);
        System.out.println("Operadores incrementales-------------------------------");
        int incremento = 1;
        incremento++;                                        //Incrementa el valor de la variable en 1
        System.out.println(incremento);
        int decremento = 1;
        decremento--;                                        //Decrementa el valor de la variable en 1
        System.out.println(decremento);              
        //La expresión a++ y b-- equivalen a: (a = a + 1) y (b = b - 1) respectivamente
        //Los operadores ++ y -- se pueden utilizar como prefijo (++a) o posfijo (a++) y cambia su comportamiento.
        //Si se utilizan como prefijo los operadores ++ o -- tendrá precedencia sobre otros operadores de la expresión.
        //Si se utilizan como posfijo, se realizará cualquier operación antes que la operación incremento o decremento.
        //Ejemplo:
        int a = 1;
        System.out.println(a);
        System.out.println(++a);
        System.out.println(a);
        
        int b = 1;
        System.out.println(b);
        System.out.println(b++);
        System.out.println(b);

        //Operadores relacionales (==,!=,<,>,<=,>=)
        //Producen un resultado lógico o booleano a partir de comparaciones entre valores numéricos, caracteres o boolenao 
        System.out.println("Operadores relacionales -------------------------------");
        int numero = 1;
        int numero2 = 1;
        int numero3 = 3;
        Boolean igual = numero == numero2; // Devuelve un valor booleano dependiendo si las dos expresiones son iguales 
        System.out.println(igual);
        Boolean distinto = 1+2 != numero3; // Devuelve un valor boolenao dependiendo si las expresiones son diferentes
        System.out.println(distinto);
        Boolean menor = numero < numero3; // Devuelve un valor booleano si expresión de la izquierda es menor que la expresión de la derecha 
        System.out.println(menor);
        Boolean mayor = 7+23 > numero;    // Devuelve un valor booleano si expresión de la izquierda es mayor que la expresión de la derecha
        System.out.println(mayor);
        Boolean menorIgual = numero + numero3 <= 5; // Devuelve un valor booleano si expresión de la izquierda es menor o igual que la expresión de la derecha
        System.out.println(menorIgual);
        Boolean mayorIgual = numero + numero3 >= 4; // // Devuelve un valor booleano si expresión de la izquierda es mayor o igual que la expresión de la derecha
        System.out.println(mayorIgual);

        //Operadores lógicos(&&,||,!)
        //Producen un resultado lógico o booleano a partir de otros valores booleanos
        System.out.println("Operadores lógicos -------------------------------");
        Boolean verdadero = true;
        Boolean falso = false;
        int c = 4;
        Boolean and = verdadero && c != 7;              // El operador (&&) and delvuelve true si todas las expresiones son verdaderas
        System.out.println(and);
        Boolean or = falso || c < 1 || verdadero;       //El operador or (||) delvuelve true si una de las expresiones es verdadera   
        System.out.println(or);
        Boolean not = !(falso) && verdadero;            // El operador not (!) cambia el valor de la expresión a sus contrario
        System.out.println(not);

        //Operadores asignación combinados (+=,-=,*=,/=,%=)
        //Se trata del operdor asignación combinado con los ariméticos
        System.out.println("Operadores aignacion y aritméticos -------------------------------");
        int z = 4;
        int y = 7;
        int x = 1;
        int w = 8;
        int v = 9;
        z += 3;                             //Suma el valor de la derecha y se asigna a la variable
        System.out.println(z);
        y -= 2;                             //Resta el valor de la derecha y se asigna a la variable
        System.out.println(y);
        x *= 6;                             //Multiplica el valor de la derecha y se asigna a la variable
        System.out.println(x);
        w /= 4;                             //Divide por valor de la derecha y se asigna a la variable
        System.out.println(w);
        v %= 2;                             //Se realiza el módulo por la expresión indicada a la izquierda y la asigna a la variable
        System.out.println(v);

        //Operador ternario o condicional (?:)
        //Devuelve el valor entre dos posibles. Si la expresión es verdadera develve el valor1 (expresion condicional ? valor1 : valor2)
        System.out.println("Operadores ternario -------------------------------");
        int k = 9;
        int j = k >= 4 ? 18 : 1;
        int l = k >= 20 ? 18 : 1;
        System.out.println(j);
        System.out.println(l);

        //Operadores de bit(&,|,^,~,<<,>>)
        //Sirve para realizar operaciones con número en bit, el resultado que devuelve es int 
        System.out.println("Operadores de bits -------------------------------");

        int cinco = 5;                      // 0101 en binario
        int tres =3;                        // 0011 en binario
        
        int bitAnd = cinco & tres;          // 0001 (1) Operación lógica AND 
        System.out.println(bitAnd);
        int bitOr = cinco | tres;           // 0111 (7) Operción lógica OR  
        System.out.println(bitOr);
        int bitXor = cinco ^ tres;          // 0110 (6) Operación OR exclusiva 
        System.out.println(bitXor);
        int bitNot = ~cinco;                // Operación NOT
        System.out.println(bitNot);

        int cuatro = 4;                     // 0100 en binario
        int deplazarIzq = cuatro << 1;      // 1000 (8) Desplazada x posiciones a las izquierda 
        System.out.println(deplazarIzq);
        int deplazarDer = cuatro >> 1;      // 0010 (2) Desplaza x posiciones a la derecha
        System.out.println(deplazarDer);

        //Operador de concatenación (+)
        //Sirve para concatenar(unir) strings
        System.out.println("Operador de concatenación-------------------------------");
        String cadena = "Hola";
        System.out.println(cadena + " Mundo");

        //Estrucutas de control 
        //Condición simple (If). Ejecuta un bloque de código si se cumple una condición
        /* 
        if (condition) {
            bloque de código
        }
        */
        System.out.println("Estructura de control (IF)-------------------------------");
        int r = 17;

        if (r > 10 && 5+1 != r){
            System.out.println("Se ejecuta porque la condicio es true");
        }

        //Condicional doble (if-else). Se especifican dos bloques de código y mediante la condición si es true se ejecuta un bloque o si es false se ejecuta el otro bloque.
         /* 
        if (condición) {
            bloque de código
        }else{
            bloque de código
        }
        */
        System.out.println("Estructura de control (if-esle)-------------------------------");        
        if(r < 10){
            System.out.println("Este es el bloque que se ejecuta si la condición es true");
        }else{
            System.out.println("Este es el bloque que se ejecuta si la condición es false");
        }

        //Anidación de condicionales if-else if-else. Se puede hacer varias condiciones que ejecutaran diferentes bloques de códigos
        /* 
        if (condición) {
            bloque de código
        }else if (condición){
            bloque de código
        }else {
            bloque de código
        }
        */
        System.out.println("Estructura de control (if anidados)-------------------------------");
        if (r < 17 ){
            System.out.println("Es menor a 17");
        } else if ( r == 17){
            System.out.println("Es igual a 17");
        } else {
            System.out.println("Es mayor a 17");
        }

        //Switch. Se utiliza en codiciones multiples.
        /*switch (expresión) {
            case value:
                
                break;
            
            ...

            default:
                break;
        }*/
        System.out.println("Estructura de control (switch)-------------------------------");
        String saludo = "hola";
        switch (saludo) {
            case "hola":
                System.out.println("Bloque 1");
                break;
            case "adios":
                System.out.println("Bloque 2");
                break;
            default:
                System.out.println("Bloque por defecto (Opcional)");
                break;
        }

        //La estructura switch necesita de la sentencia break para parar la ejecución del siguieten bloque.
        System.out.println("Estructura de control (switch sin break)-------------------------------");
        switch (saludo) {
            case "hola":
                System.out.println("Bloque 1");
            case "adios":
                System.out.println("Bloque 2");
            default:
                System.out.println("Bloque por defecto (Opcional)");
                break;
        }
        
        //En las útimas versiones de switch tiene otra sintaxis en la que no es necesario utilizar la sentencia break para parar la ejecución del bloque
        // y si el bloque a ejecutar solo contiene una línea no es necesario escribir {}
        /*switch (expresión) {
            case valor -> Una línea de código 
            case valor2->{
                Bloque de código
            }
            default->{
                Bloque de código
            }   
        }
        */
        System.out.println("Estructura de control (switch con otra sintaxis)-------------------------------");
        int g = 2;
        switch (g){
            case 1,2,3 -> System.out.println("Se ejecutará en el caso de 1,2,3");
            case 4 -> {
                System.out.println("Se ejecutará en el caso de 4");
                System.out.println("Nesecita {} porque hay más de una línea de código");
            }
        }

        //También se puede utilizar como una expresión, es decir toda la sentencia switch se sustituira por un valor.
        //En caso de que el bloque de código de un caso tenga más de una línea de código necesitaremos de la sentencia yield para devolver un valor
        //Si switch se utiliza como una expresión necesitaremos un caso delfault obligatoriamente
        /*tipoVarible nombreVariable = switch (expresión) {
            case valor -> valor devuelto 
            case valor2->{
                Bloque de código
                yield valor devuelto
            }
            default->{
                Bloque de código
                yield valor devuelto
            }   
        }
        */
        System.out.println("Estructura de control (switch como expresión)-------------------------------");
        int numMes = 13;
        int diasMes = switch(numMes){
            case 1, 3, 5, 7, 8, 10, 12 -> 31;
            case 2 -> 28;
            case 4, 6, 9, 11 -> 30;
            default -> {
                System.out.println("Error, solo hay doce meses");
                yield -1;
            }
        };
        System.out.println("El mes " + numMes + " tiene " + diasMes + " dias");

        //Estrutura de control while. Es un bucle controlado por una condición
        /*
        while (condición) {
          bloque de código  
        }
        */
        System.out.println("Estructura de control (while)-------------------------------");
        int s = 1;
        while (s <= 10){
            System.out.print(" " + s);
            s++;
        }

        //Estrutura de control do-while. Es un bucle controlado por una condición y a diferencia de while, el bloque dentro de bucle se ejecuata al menor una vez
        /* 
        do{
            bloque de código
        }while(condición);
        */
        System.out.println("Estructura de control (while)-------------------------------");
        int t = 10;
        do{
            System.out.print(" " + t);
            t--;
        } while (t >= 1);

        //El bucle while se puede ejecutar de 0 a infinitas veces y el bucle do while de 1 a infinitas veces

        //Estrutura de control for. Es un bucle controlado por una variable que incrementa o decrementa.
        /* 
        for(inicialización de variable; condición; incremento/decremento){
            bloque de código
        }
        */
        System.out.println("Estructura de control (for)-------------------------------");
        for(int i = 1; i <= 10 ; i++){
            System.out.print(" "+ i);
        }

        //Ejercicio opcional
        for(int i = 10; i <=55; i++){
            if( i % 2 == 0 && i != 16 && i % 3 != 0){
                System.out.print( " " + i);
            }
        }

    }
}