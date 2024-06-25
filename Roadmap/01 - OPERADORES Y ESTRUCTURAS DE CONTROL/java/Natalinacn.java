package com.example.headfirstjava;

import org.springframework.boot.SpringApplication;

public class Natalinacn {

    public static void main(String[] args) {
        SpringApplication.run(HeadFirstjavaApplication.class, args);

        //#01-OPERADORES Y ESTRUCTURAS DE CONTROL

        //Operador de Asignación (=)

        int numero = 1;

        System.out.println("La variable número tiene asignado el valor " + numero);

        //Operadores Aritméticos
        //Suma (+)
        int suma = 1 + 2;
        System.out.println("El resultado de la suma es " + suma);

        //Resta (-)
        int resta = 7 - 2;
        System.out.println("El resultado de la resta es " + resta);

        //Multiplicación (*)
        int multi = 5*5;
        System.out.println("El resultado de la multiplicación es " + multi);

        //División (/)
        int div = 8/4;
        System.out.println("El resultado de la división es " + div);

        //Resto (%)
        int resto = 4%2;
        System.out.println("El resultado del resto es " + resto);


        /*Operadores unarios: Los operadores unarios sólo requieren un operando; realizan diversas operaciones,
        como incrementar/decrementar un valor en uno, negar una expresión o invertir el valor de un booleano.*/

        //+ Operador de más unario; indica un valor positivo (los números son positivos sin este operador)
            int result = +1;
            System.out.println("El valor de result es positivo " + result);

        //- Operador de menos unario; niega una expresión
            result = -result;
            System.out.println("El valor de resultado ahora es negativo " + result);

        //++ Operador de incremento; incrementa un valor en 1
            result++;
           System.out.println("El valor de result ahora se incrementó en 1" + result);

        //-- Operador de decremento; decrementa un valor en 1
        result--;
        System.out.println("El valor de result ahora se decrementó en 1" + result);

        //! Operador de complemento lógico; invierte el valor de un booleano
        boolean exitoso = false;
        System.out.println("Exitoso es falso " + exitoso);
        System.out.println("Exitoso con el operador ! cambia de valor a verdadero " + !exitoso);


        //Operadores de Igualdad y Relacionales
        //== Igual a
        int num1 = 1;
        int num2 = 8;

        if(num1 == num2){
            System.out.println("Los números son iguales");
        }

        //!= No igual a
        if(num1 != num2 ){
            System.out.println("Los números son diferentes");
        }

        //> Mayor que
        if(num1>num2){
            System.out.println("El número 1 " + num1 + "es mayor al número 2" + num2);
        }

        //>= Mayor o igual que
        if(num1>=num2){
            System.out.println("El número 1 " + num1 + "es mayor o igual al número 2" + num2);
        }

        //< Menor que
        if(num1<num2){
            System.out.println("El número 1 " + num1 + "es menor al número 2" + num2);
        }

        //<= Menor o igual que
        if(num1<num2){
            System.out.println("El número 1 " + num1 + "es menor o igual al número 2" + num2);
        }

        //Operadores Condicionales
        //&& AND condicional
        //|| OR condicional

        int value1 = 5;
        int value2 = 2;

        if(value1 == 5 && value2 ==2){
            System.out.println("El value1 es 5 y el value 2 es 2");
        }

        if(value1 == 5 || value2 == 5){
            System.out.println("El value1 es 5 o el value2 es 5");
        }

        //?: Ternario (abreviatura para una declaración if-then-else)
        String ternario = (value1>0) ? "El valor es mayor a 0" : "El valor es menor a 0";
        System.out.println(ternario);

        //Operador de Comparación de Tipo

        //instanceof Compara un objeto con un tipo especificado
        Dog dog1 = new Dog();

        System.out.println("El objeto dog1 es instancia de Dog? " + (dog1 instanceof Dog));

        //Operadores Bitwise y de Desplazamiento de Bits
        //
        //~ Complemento bitwise unario
        //<< Desplazamiento a la izquierda con signo
        //>> Desplazamiento a la derecha con signo
        //>>> Desplazamiento a la derecha sin signo
        //& AND bitwise
        //^ OR exclusivo bitwise
        //| OR inclusivo bitwise

        int g = 5; // 5 en binario es 00000101

        int bitwiseComplement = ~g; // bitwiseComplement es -6 (en binario 11111010)
        int leftShift = g << 2; // leftShift es 20 (00010100)
        int rightShift = g >> 1; // rightShift es 2 (00000010)
        int unsignedRightShift = g >>> 1; // unsignedRightShift es 2 (00000010)

        int h = 3; // 3 en binario es 00000011
        int bitwiseAnd = g & h; // bitwiseAnd es 1 (00000001)
        int bitwiseOr = g | h; // bitwiseOr es 7 (00000111)
        int bitwiseXor = g ^ h; // bitwiseXor es 6 (00000110)



        //ESTRUCTURAS DE CONTROL
        //1. Estructuras Condicionales
        //If
        int edad = 18;
        if(edad > 18){
            System.out.println("Eres un adulto");
        }

        //if-else
        if(edad > 18){
            System.out.println("Eres un adulto");
        }else{
            System.out.println("No eres un adulto");
        }

        //if-else if-else

        int puntaje = 40;

        if(puntaje>=85){
            System.out.println("Eres muy inteligente");
        } else if (puntaje >= 60) {
            System.out.println("Vas bien encaminado, sigue estudiando");
        } else if (puntaje >= 40) {
            System.out.println("No seas vago, estudia más");
        }else{
            System.out.println("No vas a aprender nada si sigues sin estudiar");
        }

        //switch
        int dia = 2;

        switch (dia){
            case 1:
                System.out.println("El día es Lunes");
                break;
            case 2:
                System.out.println("El día es Martes");
                break;
            case 3:
                System.out.println("El día es Miércoles");
                break;
                case 4:
                System.out.println("El día es Jueves");
                break;
            default:
                System.out.println("Es otro día");
                break;
        }

        //2. Bucles
        //for
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteracion: " + i);
        }

        //for-each

        int[] arrayNumeros = {1, 5, 8, 9, 22};

        for (int num : arrayNumeros) {
            System.out.println("Número " + num);
        }

        //while
        int count = 0;
        while (count < 5){
            System.out.println("Count en el while " + count);
            count++;
        }

        //do-while
        int countDoWhile = 0;
        do {
            System.out.println("Count en el do-while: " + countDoWhile);
            countDoWhile++;
        }while(countDoWhile < 5);

        //3. Estructuras de Control de Salto
        //break
        for (int i = 0; i < 10; i++) {
            if (i == 5) {
                break; // Salir del bucle cuando i es 5
            }
            System.out.println("Con el break: i: " + i);
        }


        //continue
        for (int i = 0; i < 10; i++) {
            if (i % 2 == 0) {
                continue; // Saltar la iteración actual si i es par
            }
            System.out.println("Con el continue: i: " + i);
        }

        //yield: El yield se usa dentro de un bloque switch para devolver un valor después de realizar algún cálculo o lógica adicional.
        //En este caso, se usa para devolver el número de días laborales restantes en la semana después de calcularlo.

        Day diaYield = Day.MONDAY;
        System.out.println("Días laborales restantes: " + calculateRemainingWorkDays(diaYield));


        //return
                System.out.println("Sum con return: " + add(5, 3));

        //* DIFICULTAD EXTRA (opcional):
        // * Crea un programa que imprima por consola todos los números comprendidos
        // * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

        for (int i = 10; i < 56; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }





    }
    //Método para return
            public static int add(int a, int b) {
                return a + b; // Terminar el método y devolver un valor

        }

        //Método para yield
        // Método que utiliza switch con yield
        public static int calculateRemainingWorkDays(Day d) {
            return switch (d) {
                case SATURDAY, SUNDAY -> 0;
                default -> {
                    int remainingWorkDays = 5 - d.ordinal();
                    yield remainingWorkDays;
                }
            };
        }

    // Enumeración de días de la semana
    enum Day {
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
    }


    }