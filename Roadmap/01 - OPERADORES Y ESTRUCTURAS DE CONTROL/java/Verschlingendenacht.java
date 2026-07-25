import java.util.Scanner;

public class Verschlingendenacht {

    public static void main(String[] args){
        Operadores();
        Estructuras();
        Extra();
    }

    static void Operadores(){
        //REQUISITO 1: OPERADORES EN JAVA

        int x = 2;
        int y = 3;

        //OPERADORES ARITMETICOS
        System.out.println(x + y); //Suma
        System.out.println(x - y); //Resta
        System.out.println(x * y); //Multiplicacion
        System.out.println(x / y); //Division
        System.out.println(x % y); //Modulo

        //EXTRA
        System.out.println("hola" + "mundo!"); //Concatenacion

        //OPERADORES UNARIOS
        System.out.println(-x); //Conversion negativa
        System.out.println(+x); //Conversion positiva
        System.out.println(x++); //Post-incremento
        System.out.println(++x); //Pre-incremento

        System.out.println(x--); //Post-decremento
        System.out.println(--x); //Pre-decremento

        System.out.println(!true); //Negacion o Inversion de booleano

        //OPERADORES DE ASIGNACION
        int z = 4;
        System.out.println("En Java, usamos el operador \"=\" para asignar un valor a una variable");

        z += 2;
        System.out.println(z);

        z -= 2;
        System.out.println(z);

        z *= 2;
        System.out.println(z);

        z /= 2;
        System.out.println(z);

        z %= 2;
        System.out.println(z);

        //OPERADORES RELACIONALES
        int a = 1;
        int b = 2;

        System.out.println(a == b); //Igualdad
        System.out.println(a != b); //Diferencia
        System.out.println(a < b); //Menor que
        System.out.println(a > b); //Mayor que
        System.out.println(a <= 1); //Menor o igual que
        System.out.println(b >= 2); //Mayor o igual que

        //OPERADORES LOGICOS
        System.out.println(a == 1 && b == 2); //Y (and)
        System.out.println(a != 1 || b == 2); //O (or)

        //OPERADOR TERNARIO
        System.out.println(a == 1 ? a : 0);

        //OPERADORES BITWISE
        int c = 3;
        int d = 4;
        int f = -9;

        System.out.println(c & d); //(AND) Retorna 1 cuando ambos bits son 1
        System.out.println(c | d); //(OR) Retorna 1 si uno de ambos bits es 1
        System.out.println(c ^ d); //(XOR) Retorna 1 si ambos bits son diferentes del otro
        System.out.println(~d); //(Complemento Bitwise) Invierte los bits del valor

        //OPERADORES DE DESPLAZAMIENTO
        System.out.println(c >> 3); //(Desplazamiento de bits hacia la izquierda) multiplica el derecho por 2 elevado al izquierdo
        System.out.println(d << 4); //(Desplazamiento de bits hacia la derecha respetando su signo) bit signo
        System.out.println(f >>> 2); //(Desplazamiento de bits hacia la derecha ignorando su signo) rellena con 0s

    }

    static void Estructuras(){
        //REQUISITO 2: ESTRUCTURAS DE CONTROL EN JAVA

        //Estructuras Condicionales
            Scanner scanner = new Scanner(System.in);
            System.out.println("Ingresa una edad");
            int edad = scanner.nextInt();

            //if
                if(edad > 17){
                    System.out.println("Esta persona es adulta!");
                }

            //if-else
                if(edad > 17){
                    System.out.println("Esta persona es adulta!");
                }else{
                    System.out.println("Esta persona es menor de edad!");
                }

            //if-else-if
                if(edad > 17) {
                    System.out.println("Esta persona es adulta!");
                }else if(edad > 11){
                    System.out.println("Esta persona es adolescente!");
                }else{
                    System.out.println("Esta persona es un niño!");
                }

            //switch case
            System.out.println("Ingresa un dia del 1 al 7");
            int dia = scanner.nextInt();
                switch(dia){
                    case 1:
                        System.out.println("Lunes");
                        break;
                    case 2:
                        System.out.println("Martes");
                        break;
                    case 3:
                        System.out.println("Miercoles");
                        break;
                    case 4:
                        System.out.println("Jueves");
                        break;
                    case 5:
                        System.out.println("Viernes");
                        break;
                    case 6:
                        System.out.println("Sabado");
                        break;
                    case 7:
                        System.out.println("Domingo");
                        break;
                    default:
                        System.out.println("Dia no valido.");
                }

        //Estructuras Iterativas
            //for
            int[] numeros = {1,2,3,5,7,11,13};
                for(int i = 0; i < numeros.length; i++){
                    System.out.println(numeros[i]);
                }

            //for-each
            String[] frutas = {"Banano", "Piña", "Pera", "Sandia", "Manzana"};
                for(String fruta : frutas){
                    System.out.println(fruta);
                }

            //while
            System.out.println("En un bucle While, la cantidad de iteraciones es determinada en la ejecucion");
            int iteraciones = scanner.nextInt();
            int iterador = 1;
                while(iterador <= iteraciones){
                    System.out.println(iterador);
                    iterador++;
                }

            //do-while
            int opcion = 0;
                do{
                    System.out.println("Bienvenido al menu de inicio");
                    System.out.println("1- Imprmimir \"Hola Mundo\"");
                    System.out.println("2- Mostrar la suma de 2+1");
                    System.out.println("3- Cerrar menu");

                    opcion = scanner.nextInt();

                    switch(opcion){
                        case 1:
                            System.out.println("Hola Mundo!");
                            break;
                        case 2:
                            System.out.println(2+1);
                            break;
                    }
                }while(opcion != 3);

        //Estructuras de Salto
            //break
            //La sentencia break permite romper el hilo activo, podemos implementarlo tanto en bucles como en estructuras tipo switch
            for(int i = 0; i <= 10; i++){
                if(i==9){
                    break;
                }
                System.out.println(i);
            }

            //continue
            //La sentencia continue permite saltarse el hilo activo de un bucle
            for(int i = 0; i < 20; i++){
                if(i % 2 == 0){
                    continue;
                }
                System.out.println(i);
            }

        //Estructuras de Excepciones
            //Try-Catch
            int resultado = 0;
            try{
                System.out.println("Vamos a sumar, ingresa el primer operando");
                int x = scanner.nextInt();

                System.out.println("Ingresa el segundo operando");
                int y = scanner.nextInt();

                resultado = x + y;

            } catch (Exception e){
                System.out.println("Ingresaste un numero invalido:");
                System.out.println(e);
            } finally {
                if(resultado != 0){
                    System.out.println("Resultado: " + resultado);
                }
        }
    }

    static void Extra(){
        /*
            DIFICULTAD EXTRA (opcional):
            Crea un programa que imprima por consola todos los números comprendidos
            entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
        */

        for(int i = 10; i <= 55; i++){
            if( (i % 2 == 0) && (i != 16) && (i % 3 != 0) ){
                System.out.println(i);
            }
        }
    }
}
