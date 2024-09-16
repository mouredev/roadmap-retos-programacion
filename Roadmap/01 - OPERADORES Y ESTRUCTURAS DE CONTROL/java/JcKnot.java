package RoadMap;
/*
 * @author JcKnot
 */
public class JcKnot {
    public static void main(String[] args) {
        
        // Operadores aritméticos
        int a = 10;
        int b = 55;
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Módulo: " + (a % b));

        // Operadores lógicos
        boolean x = true;
        boolean y = false;
        System.out.println("AND lógico: " + (x && y));
        System.out.println("OR lógico: " + (x || y));
        System.out.println("NOT lógico: " + (!x));

        // Operadores de asignación
        int c = a;
        System.out.println("Asignación: " + c);
        // Operadores combinados de asignación
        a += b;
        System.out.println("Suma y asignación: " + a);
        a -= b;
        System.out.println("Resta y asignación: " + a);
        a *= b;
        System.out.println("Multiplicación y asignación: " + a);
        a /= b;
        System.out.println("División y asignación: " + a);
        a %= b;
        System.out.println("Módulo y asignación: " + a);
        
        // Operadores de comparación
        System.out.println("Mayor que: " + (a > b));
        System.out.println("Menor que: " + (a < b));
        System.out.println("Igual a: " + (a == b));
        System.out.println("No igual a: " + (a != b));

        // Operadores de bits
        System.out.println("AND bit a bit: " + (a & b));
        System.out.println("OR bit a bit: " + (a | b));
        System.out.println("XOR bit a bit: " + (a ^ b));
        System.out.println("Desplazamiento a la izquierda: " + (a << 2));
        System.out.println("Desplazamiento a la derecha: " + (a >> 2));
        
        // Estructuras de control
        // Condicionales
        if (a > b) {
            System.out.println("a es mayor que b");
        } else {
            System.out.println("a no es mayor que b");
        }

        // Iterativas
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteración: " + i);
        }

        // Excepciones
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[4]);
        } catch (Exception e) {
            System.out.println("Algo salió mal.");
        }
        
        // Extra
        
        int numIni = 10, numFin = 55;
        
        while (numIni <= numFin){
            
            if (numIni != 16 && numIni %2 == 0 && !(numIni %3 == 0 )){
                System.out.println(numIni);
            }
            numIni = numIni + 1;            
        }                
    }
}
