public class mariovelascodev {
        public static void main(String[] args) {

            int number1 = 10;
            int number2 = 43;

            //Operadores aritméticos
            System.out.println("Operadores Aritméticos");
            System.out.println("-----------------------");

            int sum = number1 + number2;
            int subtract = number1 - number2;
            int multiplication = number1 * number2;
            int division = number2 / number1;
            int modulus = number2 % number1;

            System.out.println("Suma: " + sum);
            System.out.println("Resta: " + subtract);
            System.out.println("Multiplicación: " + multiplication);
            System.out.println("División: " + division);
            System.out.println("Módulo: " + modulus);
            System.out.println("Incremento se utiliza poniendo ++ delante de la variable: "+ ++sum);
            System.out.println("Decremento se utiliza poniendo -- delante de la variable: "+ --sum);

            System.out.println("-----------------------\n");

            //Operadores de comparación
            System.out.println("Operadores de Comparación");
            System.out.println("---------------------------");

            System.out.println("Operador de Igualdad se representa con ==: 10 == 43: "+(number1 == number2));
            System.out.println("Operador de Distinto de se representa con !=: 10 != 43: "+(number1 != number2));
            System.out.println("Operador de Mayor que se representa con >: 10 > 43: "+(number1 > number2));
            System.out.println("Operador de Mayor o Igual que se representa con >=: 10 >= 43: "+(number1 >= number2));
            System.out.println("Operador de Menor que se representa con z: 10 < 43: "+(number1 < number2));
            System.out.println("Operador de Menor o Igual que se representa con <=: 10 > 43: "+(number1 <= number2));


            System.out.println("-----------------------\n");

            //Operadores lógicos
            System.out.println("Operadores Lógicos");
            System.out.println("---------------------------");

            System.out.println("El operador AND se representa con &&: number1 > 10 && number2 < 40: "
                    + (number1 > 10 && number2 <= 40));

            System.out.println("El operador OR se representa con ||: number1 >= 10 || number2 < 40: "
                    + (number1 >= 10 || number2 <= 40));

            System.out.println("El operador NOT se representa con !: !(number1 > 10 && number2 < 40): "
                    + !(number1 > 10 && number2 <= 40));

            System.out.println("-----------------------\n");

            //Operadores de asignación
            System.out.println("Operadores de asignación");
            System.out.println("---------------------------");

            System.out.println("El operador de Asignación se representa con el signo =: number1 = 10");
            System.out.println("El operador de Asignación con suma se representa +=: number1 += 1 da por salida: "
                    +(number1 += 1));
            System.out.println("El operador de Asignación con resta se representa -=: number1 -= 1 da por salida: "
                    +(number1 -= 1));
            System.out.println("El operador de Asignación con multiplicación se representa *=: number1 *= 5 da por salida: "
                    +(number1 *= 5));
            System.out.println("El operador de Asignación con división se representa /=: number1 /= 5 da por salida: "
                    +(number1 /= 5));

            System.out.println("-----------------------\n");

            //Operadores Bitwise (bit a bit)
            System.out.println("Operadores Bitwise (Bit a Bit)");
            System.out.println("---------------------------");

            System.out.println("El operador AND se representa con &: 5 & 3: "
                    + (5 & 3)+ ". El resultado es 1 si solo ambos bits son 1");

            System.out.println("El operador OR se representa con |: 5 | 3: "
                    + (5 | 3)+". El resultado es 1 si al menos uno de los bits es 1");

            System.out.println("El operador XOR se representa con ^: 5 ^ 3: "
                    + (5 ^ 3)+". El resultado es 1 si los bits son diferentes");

            System.out.println("El operador NOT se representa con ~: ~5: "
                    + ~5+". Invierte todos los bits");

            System.out.println("El operador Desplazamiento a la Izquierda se representa con <<: 5 << 2: "
                    + (5 << 2)+". Desplaza los bits n posiciones a la izquierda, rellenando con ceros a la derecha");

            System.out.println("El operador Desplazamiento a la Derecha con signo se representa con >>: -8 >> 2: "
                    + (-8 >> 2)+". Desplaza los bits n posiciones a la derecha, replicando el signo");

            System.out.println("El operador Desplazamiento a la Derecha sin signo se representa con >>>: -8 >>> 2: "
                    + (-8 >>> 2)+". Desplaza los bits n posiciones a la derecha, rellenando con ceros a la izquierda");

            System.out.println("-----------------------\n");

            //Operador Ternario
            System.out.println("Operador Ternario");
            System.out.println("---------------------------");
            System.out.println("condición ? valorSiEsTrue : valorSiEsFalse. Ejemplo number1 > number2 ? number1 : number2 = "
                    +(number1 > number2 ? number1 : number2));

            System.out.println("-----------------------\n");

            //Estructuras de control
            System.out.println("Estructuras de control");
            System.out.println("---------------------------");

            System.out.println("Condicionales");
            System.out.println("---------------------------");

            System.out.println("if...else");
            System.out.println("---------------------------");

            if (number1 > number2) {
                System.out.println("El numero de la variable number2 es mayor");
            } else if (number1 < number2) {
                System.out.println("El numero de la variable number2 es menor");
            }else{
                System.out.println("Ambos son iguales");
            }

            System.out.println("-----------------------\n");

            System.out.println("switch");
            System.out.println("---------------------------");

            int dayOfWeek = 3;

            switch (number1) {
                case 0:
                    System.out.println("Lunes");
                    break;
                case 1:
                    System.out.println("Martes");
                    break;
                case 2:
                    System.out.println("Miercoles");
                    break;
                case 3:
                    System.out.println("Jueves");
                    break;
                case 4:
                    System.out.println("Viernes");
                    break;
                case 5:
                    System.out.println("Sabado");
                    break;
                case 6:
                    System.out.println("Domingo");
                    break;
                default:
                    System.out.println("No se puede establecer la opción");
            }

            System.out.println("-----------------------\n");

            System.out.println("Iterativas");
            System.out.println("---------------------------");

            System.out.println("for");
            System.out.println("---------------------------");

            for (int i = 1; i <= 10; i++) {
                System.out.println(i);
            }

            System.out.println("-----------------------\n");

            System.out.println("for each");
            System.out.println("---------------------------");

            String[] fruits = {"Manzana", "Plátano", "Naranja", "Fresa"};
            for(String fruit :  fruits ){
                System.out.println(fruit);
            }

            System.out.println("-----------------------\n");

            System.out.println("while");
            System.out.println("---------------------------");

            while(number1 >= 0){
                System.out.println(number1);
                number1--;
            }

            System.out.println("-----------------------\n");

            System.out.println("do while");
            System.out.println("---------------------------");

            do {
                System.out.println(number2);
                number2--;
            }while (number2 < 40);

            System.out.println("-----------------------\n");

            //Excepciones
            System.out.println("Excepciones");
            System.out.println("---------------------------");

            try{
                int result = 10 / 0;
                System.out.println(result);
            }catch(Exception e){
                System.out.println("Error: "+e);
            }finally {
                System.out.println("--------------------------\n");
            };

            System.out.println("Extra");
            System.out.println("---------------------------");

            for (int index = 10; index <= 55; index++) {
                if(index % 2 == 0 && index != 16 && index % 3 != 0){
                    System.out.println(index);
                }
            }

            System.out.println("-----------------------\n");

        }
}
