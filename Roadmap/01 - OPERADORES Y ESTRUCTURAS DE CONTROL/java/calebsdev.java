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

public class calebsdev {
    public static void main(String[] args){

        // Operadores Aritméticos
        int a = 10, b = 5;

        int suma = a + b;
        System.out.println("Suma: " + suma);
        int resta = a - b;
        System.out.println("Resta: " + resta);
        int multiplicacion = a * b;
        System.out.println("Multiplicación: " + multiplicacion);
        int division = a / b;
        System.out.println("División: " + division);
        int modulo = a % b;
        System.out.println("Módulo: " + modulo);

        // Operadores unarios
        int c = 4, d = 10;
        
        System.out.println("Pre-incremento: " + (c++));
        System.out.println("Post-incremento: " + (++c));

        System.out.println("Pre-decremento: " + (d--));
        System.out.println("Post-decremento: " + (--d));

        // Operador de asignación

        int num = 10;
        System.out.println("Inicial: " + num);
        num += 5;
        System.out.println("Después de += 5: " + num);
        num -= 3;
        System.out.println("Después de -= 3: " + num);
        num *= 2;
        System.out.println("Después de *= 2: " + num);
        num /= 4;
        System.out.println("Después de /= 4: " + num);  
        num %= 3;
        System.out.println("Después de %= 3: " + num);

        // Operadores Relacionales
        int p = 10, q = 3, r = 5;

        System.out.println(" p > q:" + (p > q));
        System.out.println(" p < q:" + (p < q));
        System.out.println(" p >= q:" + (p >= q));
        System.out.println(" p <= q:" + (p <= q));
        System.out.println(" p == q:" + (p == q));
        System.out.println(" p != q:" + (p != q));

        // Operadores Lógicos
        boolean s = true, t = false;

        System.out.println("s && t:" + (s && t));       // AND  //devuelve true si ambos son true
        System.out.println("s || t:" + (s || t));       // OR   //devuelve true si al menos uno es true
        System.out.println("!s:" + (!s));               // NOT  //devuelve true si s es false
    
        // Operador ternario
        int u = 20, v = 10, w= 30, resultado;

        resultado = (u > v) ? ((u > w) ? u : w) : ((v > w) ? v : w);
        System.out.println("Maximo de tres numeros: " + resultado);

        // Operadores de bits

        // Bitwise operators
        int dm = 0b1010;
        int en = 0b1100;
      
        System.out.println("dm & en : " + (dm & en));
        System.out.println("dm | en : " + (dm | en));
        System.out.println("dm ^ en : " + (dm ^ en));
        System.out.println("~dm : " + (~dm));
        System.out.println("dm << 2 : " + (dm << 2));
        System.out.println("en >> 1 : " + (en >> 1));
        System.out.println("en >>> 1 : " + (en >>> 1));

        // Operador instaciaof
        String str = "Hola Mundo";
        System.out.println(str instanceof String);

        Object obj =  10;
        System.out.println(obj instanceof Integer);
        System.out.println(obj instanceof String);

        // Estructuras de control
        // Sentencia if
            int i = 10;
            if (i < 15){
                System.out.println("La condición es verdadera");
            }

        // Sentencia if-else
            int j = 10;
            if ( j < 15 ){
                System.out.println("j es menor que 15");
            } else {
                System.out.println("j es mayor 15");
            }
        
        // Sentencia if anidada
            int k = 10;
            // Sentencia if externa
            if (k < 15) {
                System.out.println("k es menor que 15");
                // Sentencia if interna
                if (k == 10) {
                    System.out.println("k es igual a 10");
                }
            }

        // Sentencia if-else-if
            int o = 20;
            if ( o == 10 ){
                System.out.println("o es 10");
            }else if ( o == 15){
                System.out.println("o es 15");
            }else if ( o == 20){
                System.out.println("o es 20");
            }else{
                System.out.println("o no esta presente");
            }

        // Sentencia switch
            int day = 3;
            switch (day){
                case 1:
                    System.out.println("Lunes");
                    break;
                case 2:
                    System.out.println("Martes");
                    break;
                case 3:
                    System.out.println("Miércoles");
                    break;
                case 4:
                    System.out.println("Jueves");
                    break;
                default:
                    System.out.println("Día no válido");
            }
        
        // Estructura iterativa 
        // Sentencia for
            for (int l = 1; l <= 5; l++){
                System.out.println("FOR: " + l);
            }
        // Sentencia while
            int contador = 1;
            while (contador <= 5){
                System.out.println("WHILE: " + contador);
                contador++;
            }
        // Sentencia do-while
            int nume = 1;
            do {
                System.out.println("DO-WHILE: " + nume);
                nume++;
            } while (nume <= 5);
        // Sentencia for-each
            int[] numeros = {10, 20, 30, 40, 50};
            for (int numer : numeros){
                System.out.println("FOR-EACH: " + numer);
            }

        // Estructura de salto
        // Sentencia break
            for (int g = 1; g <= 10; g++){
                if ( g == 5){
                    System.out.println("BREAK: " + g);
                    break;
                }
            }
        // Sentencia continue
            for (int h = 1; h <= 10; h++){
                if ( h == 5){
                    System.out.println("CONTINUE: " + h);
                    continue;
        // Excepciones
            try {
                int divisionPorCero = 10 / 0;
            } catch (ArithmeticException e) {
                System.out.println("Excepción: División por cero");
            } finally {
                System.out.println("Bloque finally ejecutado");
            }
        // Sentencia throw
            try {
                throw new Exception("Excepción lanzada");
            } catch (Exception e) {
                System.out.println("Excepción: " + e.getMessage());
            }
    }
}