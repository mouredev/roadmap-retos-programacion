// 01 OPERADORES Y ESTRUCTURAS DE CONTROL
        // EJERCICIO:
            /* 01-01 Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
             *       Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
             *       (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
             */
        // Inicializo unas variables random para trabajar con ellas, para todos los ejercicios
        var myOperator1 = 5
        var myOperator2 = 3
        var myProveOperator = 0
        var i = 0
        var myBooleanTrue = true
        var myBooleanFalse = false
        var rangeAlfabet = 'a'..'d'
        var myCahr = 'b'

        // En kotlin tenemos 5 tipos de operadores aritmeticos [+] [-] [*] [/] [%] a continuacion unos ejemplos variados
        myProveOperator = myOperator1 + myOperator2 ++
        println(myProveOperator)
        myProveOperator = myOperator1 --
        println(myProveOperator)
        println(myOperator1 * 9)
        println((myProveOperator * myOperator1) / myOperator2)
        if(myProveOperator % 2 == 0) {
            println("El numero " + myProveOperator + " es par")
        }
        // En kotlin tenemos cuatro operadores logicos [|] = OR [&] = AND [.xor()] = XOR y Desigualdad [!] y a continuacion unos ejemplos
        println("${myBooleanTrue || myBooleanFalse} \n${myBooleanTrue && myBooleanFalse} \n${myBooleanFalse.xor(myBooleanTrue)} \n${!myBooleanTrue}")

        // En Kotlin tenemos diferentes comparadores [>] mayor [<] menor y [=] que podemos jugar con ellos y mezclarlos con igualdad [>=]
        if(myOperator1 > 20){
            println("El numero $myOperator1 es mayor que 20")
        } else if(myOperator1 < 20){
            println("El numero $myOperator1 es menor que 20")
        } else {
            println("El numero $myOperator1 es igual a 20")
        }

        // No podemos olvidarnos de los comparadores [==] de igualdad o el de [!=] diferencia
        if(myOperator1 == myProveOperator){
            println("Te va a tocar la loteria")
        } else if(myOperator1 != myProveOperator){
            println("No hay suerte colega, asi es la vida")
        } else {
            println("Esto no tendria que pasar colega!")
        }

        //Ya por ultimo y para mi sorpresa se pueden utilizar comparaciones como [a..d] o [1..4]
        if (myCahr in rangeAlfabet){ // este tipo de comparador [a..d] se debe usar dentro de una variable
            println("El caracter $myCahr esta dentro del rango entre a y d")
        } else{
            println("El caracter $myCahr esta fuera del rango entre a y d")
        }

        if (myOperator2 !in 1..4){
            println("El numero $myOperator2 esta dentro del rango entre 1 y 4")
        } else{
            println("El numero $myOperator2 esta fuera de rango entre el 1 y el 4")
        }

            /* 01-02 Utilizando las operaciones con operadores que tú quieras, crea ejemplos
             *       que representen todos los tipos de estructuras de control que existan
             *       en tu lenguaje: Condicionales, iterativas, excepciones...
             */
        // Me cae tanta gracia que dejadme repetir este ejemplo condicional de 'if, else if y else' ;)
        if(myOperator1 == myProveOperator){
            println("Te va a tocar la loteria")
        } else if(myOperator1 != myProveOperator){
            println("No hay suerte colega, asi es la vida")
        } else {
            println("Esto no tendria que pasar colega!")
        }

        // No es el unico condicional tambien tenemos 'when' es en apariencia identico a un swithc
        when (myProveOperator){
            myOperator1 -> println("Los espiritus estan de tu lado hoy")
            myOperator2 -> println("Ten cuidado al salir dedida, ponte crema solar o arderas como un misto")
            else -> {
                println("Ten cuidado esta noche al salir con la luna llena")
            }
        }

        // Comencemos con los bucles en este caso con el 'while' quiero aclarar un concepto la condicion de cierre del
        // bucle es hacer mientras la condicion se cumpla! en el ejemplo mientras myProbeOperator sea menor que 10
        while (myProveOperator < 10){
            println("El valor del operador de prueba es $myProveOperator ")
            myProveOperator ++
        }

        //Sigamos con el bucle 'do-while que en este caso si o si almenos una vez debe ejecutarse el do manejar con cuidado!
        do{
            println("Numero de veces que declare mi amor y me rompieron el corazon en mil trocitos $myProveOperator")
            myProveOperator ++
        } while (myProveOperator < myOperator2)

        // Ya para finalizar el marabilloso y explendido bucle 'for' aclarar que la diferencia esque la condicion de
        // cierre de este bucle es hacer asta que se cumpla la condicion!
        for (myProveOperator in 5 downTo 1){
            println("Doy vuelta y vueltas sin parar, que mareo! Ya ne se cuanto tiempo llevo aqui!")
        }

        // Ahora que tenemos la variable myProbeOperator en 0 y viendo lo extraño que es declarar 'for' en kotlin
        // quiero imprimir una tabla de multiplicar del 5 ;) sin operaciones dentro del 'for' directamente en su condicion
        // debo aclarar que no he podido crear las tipicas variables dentro del bucle como [i, j o k] sino fuera del bucle :(
        for (myProveOperator in 0..50 step 5){
            println("$i x 5 = $myProveOperator")
            i ++
        }
            // 01-03 Debes hacer print por consola del resultado de todos los ejemplos.
        // Todos los ejemplos/resultados anteriores ya han sido impresos por consola anteriormente!!

            /* 01-04 DIFICULTAD EXTRA (opcional):
             *       Crea un programa que imprima por consola todos los números comprendidos
             *       entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
             */
        i = 10
        for (i in 10..55) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0){
                println(i)
            }
        }