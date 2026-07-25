import java.awt.*;

public class Josegs95 {
    public static void main(String[] args) {
        //Operadores
        //Operadores aritméticos

        int miSuma = 3 + 8; //Suma
        System.out.println("3 + 8 = " + miSuma);

        int miResta = 17 - 5; //Resta
        System.out.println("17 - 5 = " + miResta);

        int miMultiplicacion = 2 * 3; //Multiplicación
        System.out.println("2 * 3 = " + miMultiplicacion);

        int miDivision = 15 / 3; //División
        System.out.println("15 / 3 = " + miDivision);

        int miModulo = 13 % 2; //Módulo (Resto de la división)
        System.out.println("El módulo de 13 / 2 es " + miModulo);

        //Operadores de asignación
        int miEntero = 10;
        miEntero += 5; //Equivalente a 'miEntero = miEntero + 5;'
        System.out.println("Valor de miEntero: " + miEntero);
        miEntero -= 5; //Equivalente a 'miEntero = miEntero - 5;'
        System.out.println("Valor de miEntero: " + miEntero);
        miEntero *= 2; //Equivalente a 'miEntero = miEntero * 2;'
        System.out.println("Valor de miEntero: " + miEntero);
        miEntero /= 2; //Equivalente a 'miEntero = miEntero / 2;'
        System.out.println("Valor de miEntero: " + miEntero);
        miEntero %= 8; //Equivalente a 'miEntero = miEntero % 8;'
        System.out.println("Valor de miEntero: " + miEntero);
        miEntero++; // Equivalente a 'miEntero = miEntero + 1;'
        System.out.println("Valor de miEntero: " + miEntero);
        miEntero--; // Equivalente a 'miEntero = miEntero - 1;'
        System.out.println("Valor de miEntero: " + miEntero);

        /*
        También existe la variante con el operador después del signo igual.
        Por ejemplo miEntero =+ 5; La diferencia es el orden en el que se hacen las
        operaciones. Si se usa +=, primero se suma y luego se asigna el valor.

        Para los últimos dos ejemplos, también existe la variante ++miEntero, sumando 1
        a la variable y, después de usar la variable, asignandola a la variable. Por ejemplo,
        si miEntero vale 5 y se usa un método calcularCuadrado(int), si se le pasa ++miEntero
        se le estaría pasando un 6 (y devolvería 36 como resultado) y si se usa miEntero++
        se le estaría pasando un 5, devolvería 25 y miEntero pasaría a valer 6.
         */

        //Operadores de comparación
        int a = 5;
        int b = 9;
        System.out.println("¿a es > 5?: " + (a > b)); //Compara si a es mayor que b
        System.out.println("¿a es >= 5?: " + (a >= b)); //Compara si a es mayor o igual que b
        System.out.println("¿a es < 5?: " + (a < b)); //Compara si a es menor que b
        System.out.println("¿a es <= 5?: " + (a <= b)); //Compara si a es menor o igual que b
        System.out.println("¿a es = 5?: " + (a == b)); //Compara si a es igual que b
        System.out.println("¿a es != 5?: " + (a != b)); //Compara si a es distinto que b

        //Operadores lógicos
        boolean bTrue = true;
        boolean bFalse = false;
            //Operador AND: Es true si en ambos lados del operador es true, si no devuelve false.
        System.out.println("bTrue && bFalse: " + (bTrue && bFalse));
            //Operador OR: Es true si en algunos de los lados del operador es true, si no
            //devuelve false.
        System.out.println("bTrue || bFalse: " + (bTrue || bFalse));
            //Operador NOT: Devuelve el valor contrario; true si el valor es false, si no devuelve false.
        System.out.println("!bTrue: " + (!bTrue));

        //Operadores de bits
        int num1 = 10; // 1010
        int num2 = 6;  // 0110
            //AND: Pone un 1 si ambos bits son 1, si no pone un 0
        System.out.println("num1 & num2: " + (num1 & num2)); // 2 -> 0010
            //OR: Pone un 1 si alguno de los bits son 1, si no pone un 0
        System.out.println("num1 | num2: " + (num1 | num2)); // 14 -> 1110
            //XOR: Pone un 1 si ambos bits son diferentes, si no pone un 0
        System.out.println("num1 ^ num2: " + (num1 ^ num2)); // 12 -> 1100
            //Complemento: Pone un 1 si en el original vale 0, o 0 si vale 1.
        System.out.println("~num1: " + (~num1)); // 5 -> 0101
            //Desplazamiento a la izqda: Desplaza el '1' mas a la izqda varias posiciones a hacia la izqda
            //rellenando con 0 los huecos
        System.out.println("num2 << 2: " + (num2 << 2)); // 24 -> 0001 1000
            //Desplazamiento a la dcha: Desplaza el '1' mas a la izqda varias posiciones a hacia la dcha
        System.out.println("num2 >> 2: " + (num2 >> 2)); // 1 -> 0001
            //Desplazamiento a la dcha sin signo: Desplaza el '1' mas a la izqda varias posiciones a hacia
            //la dcha, obviando el signo
        System.out.println("num2 >>> 2: " + (num2 >>> 2)); // 1 -> 0001

        //Operadores de objetos
        String miString = new String("Valor de la cadena"); //El operador 'new' se encarga de crear objetos
        boolean esString = miString instanceof String; //'instanceof' comprueba si un objeto es de una clase específica

        //Estructuras de control

            //If, else-if, else
        a = 8;
        b = 5;
        if (a > b){
            //Si a es mayor que b, haz algo...
        } else if (a < b) { //Se pueden encadenar todos los else-if que se quiera.
            //Si no se ha cumplido lo anterior, y a es menor que b, haz esto...
        } else {
            //Si todo lo anterior no se ha cumplido, haz esto otro...
        }

            //Operador ternario. Equivalente a if (a>b) -> a, else-> b.
        int numMayor = a > b ? a : b;

            //Switch-case
        int diasEnUnMes = 28;
        switch (diasEnUnMes){
            case 28, 29:
                System.out.println("El mes es Febrero");
                break; //Se usa el break para salir de la estructura de control, en este caso del switch.
            case 30:
                System.out.println("El mes puede ser Enero, Abril, Junio, Septiembre o Noviembre");
                break;
            case 31:
                System.out.println("El mes puede ser Marzo, Mayo, Julio, Agosto o Diciembre");
                break;
            default:
                System.out.println("No existe ningún mes con esa cantidad de días.");
        }

            //Bucle for: Se inicializa una variable, se comprueba la condición, y si es true, se ejecuta el
            //código. Luego se hace el incremento.
        for (int i = 0; i < 10; i++){
            System.out.print("El valor de i es " + i);
            if (i % 2 == 0){
                System.out.println(" y es par");
                continue; //Sirve para salir de esta iteración pero no del for, como sería con el break.
            }
            System.out.println(" y es impar");
        }
        //El for puede estar completamente o parcialmente vacio
        int contador = 0;
        for (;;){
            if (contador == 5){
                System.out.println("La variable contador vale: " + contador + " y se sale del bucle");
                break;
            }
            contador++;
        }

            //Bucle for-each. Sirve para recorrer colecciones. Las colecciones tienen que ser iterables, es decir,
            //implementar la interfaz 'Iterable'. La clase Array lo hace.S
        String[] arrayString = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"};
        for (String cadena : arrayString){
            System.out.println("Día de la semana: " + cadena);
        }

            //Bucle while. Equivalente a for (;expr;){}
        contador = 0;
        while (contador < 3){
            System.out.println("La variable contador (" + contador + ") es menor que 3");
            contador++;
        }
            //Bucle do-while. Es igual que un while, pero siempre entra una vez, es decir, siempre se ejecuta
            //lo que hay dentro al menos la primera vez
        do{
            System.out.println("La variable contador vale " + contador + " y ha entrado al bucle");
        }while(contador > 1000); //Importante el ';' aquí.

            //Try-catch-finally. Se usa para manejar excepciones. Todas las excepciones derivan de 'Exception'
        try{
            System.out.println("Introduzca dos números para dividirlos entre sí");
            int dividendo = 12;
            int divisor = 0;
            int resultado = dividendo / divisor;
            System.out.println("El resultado de " + dividendo + "/" + divisor + " es " + resultado);
        } catch (Exception e) { //Se puede 'atrapar' todos los tipos de excepciones que se quiera.
            System.out.println("Se ha producido un error, abortando la operación");
        } finally { //Se ejecuta siempre, salte excepción o no
            System.out.println("¿Quieres seguir dividiendo números?");
        }

        retofinal();
    }

    public static void retofinal(){
        System.out.print("\nReto: ");
        for (int i = 10; i < 56; i++){
            if (i % 2 == 0){
                if (i % 3 != 0){
                    if (i != 16){
                        System.out.print("[" + i + "]");
                    }
                }
            }
        }
        System.out.println();
    }
}
