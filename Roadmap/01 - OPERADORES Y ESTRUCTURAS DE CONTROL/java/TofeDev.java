public class TofeDev {
     public static void main(String[] args) {

        //Asignaciones
        int a = 20;
        short b = 10;

    
        //Operadores Aritméticos
        int suma = a + b;
        System.out.println("Suma: " + suma);
        int resta = a - b;
        System.out.println("Resta: " + resta);
        int multiplicacion = a * b;
        System.out.println("Multiplicación: " + multiplicacion);
        int division = a / b;
        System.out.println("División: " + division);
        int resto = a % b ;
        System.out.println("Resto: " + resto);

    
        //Asignación compuesta
        suma += a;
        System.out.println("a + a = " + suma);
        resta -= a;
        System.out.println("a - a = " + resta);
        multiplicacion *= a;
        System.out.println("a * a = " + multiplicacion);
        division /= a;
        System.out.println("a / a = " + division);
        resto %= a;
        System.out.println("a % a = " + resto);

    
        // Operadores lógicos
        boolean and = (a < b) && (b == 0);
        System.out.println("¿Es a menor que b, Y b igual a 0?: " + and);
        boolean or = (a > b) || (b == 0);
        System.out.println("¿Es a mayor que b, O b igual a 0?: " + or);
        boolean not = !(a < b);
        System.out.println("Negación a menor que b: " + not);

    
        // Operadores de comparación
        boolean igual = (a == b);
        System.out.println("Es igual: " + igual);
        boolean distinto = (a != b);
        System.out.println("Es distinto: " + distinto);
        boolean mayor = (a > b);
        System.out.println("Es mayor: " + mayor);
        boolean mayorIgual = (a >= b);
        System.out.println("Es mayor o igual: " + mayorIgual);
        boolean menor = (a < b);
        System.out.println("Es menor: " + menor);
        boolean menorIgual = (a <= b);
        System.out.println("Es menor o igual: " + menorIgual);


        //Operadores de bits
        int aBit = 01001;
        int bBit = 00111;
        System.out.println("a como bits: " + aBit + " y b como bits: " + bBit);
        int desplazamientoIzq = a << 2;
        System.out.println("Desplazar a la izquierda: " + desplazamientoIzq);
        int desplazamientoDer = a >> 2;
        System.out.println("Desplazar a la derecha: " + desplazamientoDer);
        int andBit = a & b;
        System.out.println("AND en bits: " + andBit);
        int orBit = a | b;
        System.out.println("OR en bits: " + orBit);


        //Estructuras condicionales
        int c = 150;
        int d = 52;
        int f = 7;
        
        
        if (c < 200) {
            System.out.println("c es menor que 200");
        }
        
          
        if (d < 10) {
            System.out.println("d es menor que 10");
        } else {
            System.out.println("d es mayor que 10");
        }
        
          
        if (f > 8 && f < 15) {
            System.out.println("f es mayor que 8 y menor que 15");
        } else if (f < 5) {
            System.out.println("f es menor que 5");
        } else {
            System.out.println("f está fuera de nuestro rango");
        }
          
        
        switch (f) {
        case 2:
            System.out.println("f es 2");
            break;
        
        case 5:
            System.out.println("f es 5");
            break;
        
        case 7:
            System.out.println("f es 7");
            break;
        
        case 10:
            System.out.println("f es 10");
            break;
        }
        
        // Estructuras iterativas
        int g = 250;
        for (int i = 1; i <= 5; i++) {
            g+=2;
            System.out.println(g);
        }
        
          
        while (g < 300) {
            g+=5;
            System.out.println(g);
        }
        
          
        do {
            g+=10;
            System.out.println(g);
        } while (g < 350);
        
          
        //Estructuras excepcionales
        try {
            int[] numeros = {1, 2, 3};
            System.out.println(numeros[10]);
        } catch (Exception e) {
            System.out.println("Error");
        } finally {
            System.out.println("Sistema finalizado");
        }
        
        
         /*
          * DIFICULTAD EXTRA (opcional):
          * Crea un programa que imprima por consola todos los números comprendidos
          * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
          */

    
        for (int h = 10; h <= 50; h++) {
            if (h != 16 && h % 3 != 0 && h % 2 == 0) {
                System.out.println(h);
            }
        }
        
    }
}
