//#01 - Java

public class inmortalnight {
    public static void main(String[] args) {
        int num1 = 0;
        int num2 = 1;
        //Operadores
        //Aritmeticos
        int suma = num1 + num2;  
        System.out.println(num1 + "+" + num2 + "=" + suma);
        int resta = num1 - num2;  
        System.out.println(num1 + "-" + num2 + "=" + resta);
        int multiplicacion = num1 * num2;  
        System.out.println(num1 + "*" + num2 + "=" + multiplicacion);
        int division = num1 / num2;  
        System.out.println(num1 + "/" + num2 + "=" + division);

        //Logico
        boolean and = num1 > 0 && num2 > 0; //AND
        System.out.println(num1 + " y " + num2 + " son mayores que 0? " + and);
        boolean or = num1 > 0 || num2 > 0; //OR
        System.out.println(num1 + " o " + num2 + " son mayores que 0? " + or);
        boolean not = !(num1 > 0); //NOT
        System.out.println(num1 + " no es mayor que 0? " + not);

        //Comparacion
        boolean igual = num1 == num2;
        System.out.println(num1 + " y " + num2 + " son iguales? " + igual);
        boolean diferente = num1 != num2;
        System.out.println(num1 + " y " + num2 + " son diferentes? " + diferente);
        boolean mayor = num1 > num2;
        System.out.println(num1 + " es mayor que " + num2 + "? " + mayor);
        boolean menor = num1 < num2;
        System.out.println(num1 + " es menor que " + num2 + "? " + menor);
        boolean mayorIgual = num1 >= num2;
        System.out.println(num1 + " es mayor o igual que " + num2 + "? " + mayorIgual);
        boolean menorIgual = num1 <= num2;
        System.out.println(num1 + " es menor o igual que " + num2 + "? " + menorIgual);

        //Asignacion
        num1 += num2; //num1 = num1 + num2
        System.out.println("Nuevo valor de num1 al sumar num2 es " + num1);
        num1 -= num2;
        System.out.println("Nuevo valor de num1 al restar num2 es " + num1);
        num1 *= num2;
        System.out.println("Nuevo valor de num1 al multiplicar num2 es " + num1);
        num1 /= num2;
        System.out.println("Nuevo valor de num1 al dividir num2 es " + num1);
        num1 %= num2;
        System.out.println("Nuevo valor de num1 al sacar el modulo de num2 es " + num1);
        
        //Bits
        int a = 60; //60 = 0011 1100
        int b = 13; //13 = 0000 1101
        int c = 0;
        c = a & b; //12 = 0000 1100, escoge los bits que son 1 en ambos numeros
        System.out.println("a & b = " + c);
        c = a | b; //61 = 0011 1101, escoge los bits que son 1 en alguno de los dos numeros
        System.out.println("a | b = " + c);
        c = a ^ b; //49 = 0011 0001, escoge los bits que son 1 en uno de los dos numeros, pero no en ambos
        System.out.println("a ^ b = " + c);
        c = ~a; //-61 = 1100 0011, invierte los bits
        System.out.println("~a = " + c);
        c = a << 2; //240 = 1111 0000, desplaza los bits a la izquierda
        System.out.println("a << 2 = " + c);
        c = a >> 2; //15 = 0000 1111, desplaza los bits a la derecha
        System.out.println("a >> 2 = " + c);
        
        //Estructuras de control
        //Condicional para elegir entre dos opciones
        if (num1 > num2) { 
            System.out.println("num1 is greater than num2");
        } else if (num1 < num2) {
            System.out.println("num1 is less than num2");
        } else {
            System.out.println("num1 is equal to num2");
        }
        //Iterativa que imprime los numeros del 1 al 10
        for (int i = 1; i < 11; i++) { 
            System.out.println(i);
        }
        //Excepcion que imprime un mensaje si se produce un error
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[3]);
        } catch (Exception e) {
            System.out.println("Ocurrio un error");
        }
        //Extra: imprimir números del 10 al 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
        for(int i = 10; i <= 55; i++){
            if(i != 16 && i % 2 == 0 && i % 3 != 0){
                System.out.println(i);
            }
        }
    }
}
