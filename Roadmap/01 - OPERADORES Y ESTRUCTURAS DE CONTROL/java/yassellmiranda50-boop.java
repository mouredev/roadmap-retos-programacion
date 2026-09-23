public class YassellMiranda50Boop{
    public static void main(String[] args){
        // Operadores aritmeticos basicos: +, -, *, /, %
        int suma = 15 + 12;
        int resta = 107 - 80;
        int multiplicacion = 5 * 8;
        int division = 80 / 4;
        int modular = 9 % 3;

        System.out.println(suma);
        System.out.println(resta);
        System.out.println(multiplicacion);
        System.out.println(division);
        System.out.println(modular);

        // Operadores lógicos: &&, ||, !
        boolean mayorEdad = true;
        boolean licenciaConducir = true;
        if(mayorEdad && licenciaConducir){
            System.out.println("Puede conducir en paz.");
        }

        boolean acompaniadoMayor = true;
        if(mayorEdad || acompaniadoMayor){
            System.out.println("Puede viajar.");
        }

        boolean permisoPadres = false;
        if(!permisoPadres){
            System.out.println("No ira al viaje.");
        } else{
            System.out.println("Puede ir al viaje escolar.");
        }

        //Operadores de comparación: ==, !=, >, <, >=, <=

        //==, !=
        if(suma == resta){
            System.out.println("Los resultados de la suma y la resta son iguales");

            if(multiplicacion != division){
                System.out.println("Los resultados de la multiplicacion y la division son diferentes");
            } else{
                System.out.println("Los resultados de la multiplicacion y la division son iguales");
            }

        } else{
            System.out.println("Los resultados son diferentes");
        }

        //>, <, >=, <=
        if(modular < suma && suma > division){
            System.out.println("Suma es mayor que modular y division");
        } else if(suma >= resta){
            System.out.println("La suma es mayor o igual a la resta");
        } else if(division <= multiplicacion){
            System.out.println("La división es menor o igual a la multiplicacion");
        } else{
            System.out.println("Ningun resultado ha sido correcto");
        }

        //Operadores de asignación: =, +=, -=, *=, /=, %=
        int num = 1;
        
        num += 3;
        System.out.println(num); //A num se le suman 3; num = 4
        num -= 1;
        System.out.println(num); //A num se le resta 1; num = 3
        num *= 4;
        System.out.println(num); //A num se le multiplica por 4; num = 12
        num /= 2;
        System.out.println(num); //A num se le divide entre 2; num = 6
        num %= 2;
        System.out.println(num); //A num se le modula entre 2; num = 0

        /*
        En el caso de java no tiene operadores de identidad o de pertenencia como en python, hay algunos que pueden llegar a cumplir
        como lo seria: ==, cuando se usa entre objetos.
        */

        //Operadores en bits: &, |, ^, ~
        int num1 = 16; //12 en 8 bits binario es 00010000
        int num2 = 15; // 10 en binario es 00001111

        int and = num1 & num2;
        System.out.println(and); //El resultado numerico de and es: 0
        int or = num1 | num2;
        System.out.println(or); //El resultado numerico de or es: 31
        int xor = num1 ^ num2;
        System.out.println(xor); //El resultado numerico de xor es: 31
        int not = ~num1;
        System.out.println(not); //El resultado numerico de not es: -17


        //ESTRUCTURAS DE CONTROL: if, else, else-if, ciclos for, while, do-while, for each, switch, break, continue, return y try-catch.
        int dato = 1;
        while(dato < 5){
            System.out.println("Dato actual: " + dato);
            dato++;
        }

        int vuelta = 0;
        do{
            System.out.println("Vuelta actual: " +  vuelta);
            vuelta++;
        } while(vuelta < 3);

        int edad = 18;
        if(edad >= 18){
            System.out.println("La persona es mayor de edad");
        } else if(edad >= 65 && edad <= 120){
            System.out.println("La persona es de la tercera edad");
        } else {
            System.out.println("Edad fuera del rango establecido");
        }

        int arreglo[] = new int[5];
        for(int i=0; i<=4; i++){
            arreglo[i] = i;
        }

        for (int posicion : arreglo) {
            System.out.println(posicion);
            continue;
        }
        
        int valor1=10;
        int valor2 = 0;
        int divisionEntreValores;
        try{
            divisionEntreValores = valor1/valor2;
            System.out.println("Esto no se imprimira amenos que la division sea correcta");
        }catch(ArithmeticException e){
            System.out.println("Reasignaremos a la variable valor2 el numero 1 por defecto.");
            valor2=1;
            divisionEntreValores = valor1/valor2;
            System.out.println("Division correcta: " + divisionEntreValores);
        }

        //Ejemplo extra:
        for(int i=10; i<=55; i++){
            if(i%3==0 || i==16){
                continue;
            } else if(i%2==0){
                System.out.println("Impresion de numeros: " + i);
            }
        }

        //pegado aca por mera precaucion en cuanto al cambio de opcion
        int opcion = 2; //No selecciono 3 porque el return me saca directamente del metodo main
        switch(opcion){
            case 1:
                System.out.println("Eleccion 1 tomada.");
                break;
            case 2:
                for(int i=1; i<10; i++){ //muestra solo los pares dentro del 1 al 10
                    if(i%2==0){
                        System.out.println("Numero par: " + i);
                    } else{
                        continue;
                    }
                }
                break;
            case 3:
                System.out.println("Saliendo del programa con exito...");
                return; //Sale completamente del metodo actual: main
            default:
                System.out.println("Opcion fuera del rengo permitido: 1-3");
        }
    }
}
