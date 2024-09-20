   class Auto {
        
    }
    
    class Toyota extends Auto{
        
    }



public class Marianoemir{
/*
 *@author Marianoemir
    
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
    
 
    public static void main(String [] args){
        int a = 10, b = 2;
        
        //Operadores Aritmeticos:
       
        System.out.println("El resultado de la suma es: "+(a + b)+".");
        System.out.println("El resultado de la resta es: "+(a - b)+".");
        System.out.println("El resultado de la multiplicaciòn es: "+(a * b)+".");
        System.out.println("El resultado de la divisiòn es: "+(a / b)+".");
        System.out.println("El resultado de la modulo es: "+(a % b)+".");
        System.out.println("");
        
        //Operadores Logicos:
        
        boolean T=true, F=false;
        System.out.println("Operador Logico && Y: "+(T&&F)+".");
        System.out.println("Operador Logico || O: "+(T||F)+".");
        System.out.println("Operador Logico !not: "+(!T)+".");
        System.out.println("");
        
        //Operadores Relacionales:
        
        System.out.println("El resultado de 10 > 2 es: "+(a > b)+".");
        System.out.println("El resultado de 10 < 2 es: "+(a < b)+".");
        System.out.println("El resultado de 10 == 2 es :"+(a == b)+".");
        System.out.println("El resultado de 10 != 2 es :"+(a != b)+".");
        System.out.println("El resultado de 10 <= 2 es :"+(a <= b)+".");
        System.out.println("El resultado de 10 >= 2 es :"+(a >= b)+".");
        System.out.println("");
        
        //Operadores de Asignación:
        
        short c = 60; //Asignaciòn Simple.
        System.out.println("Asignaciòn Simple: "+c+".");
        System.out.println("Asignaciòn con Suma: "+(c += 20)+"."); 
        System.out.println("Asignaciòn con Resta: "+(c -= 5)+"."); 
        System.out.println("Asignaciòn con Multiplicación: "+(c *= 2)+"."); 
        System.out.println("Asignaciòn con División: "+(c /= 5)+"."); 
        System.out.println("Asignaciòn con Modulo: "+(c %= 5)+"."); 
        System.out.println("");
        
        //Operadores bit a bit:
        
        int d=5 ,  e = -8, f=3 , resultbitAnd = 0, resultbitOr = 0 , resultbitXor = 0 , resultbitNot = 0;
        int desplaizquieda = 0 , despladerecha = 0, desplaDconExtensióndeCero = 0;
        
        resultbitAnd = d & f;
        String binario1 = String.format("%4s", Integer.toBinaryString(resultbitAnd)).replace(' ', '0');
        System.out.println("Operador AND de bit a bit: "+binario1+".");
        
        /*
          0101 (5)
        & 0011 (3)
          --------
          0001 (1)  El AND & evalua todos los numeros y si los 2 son 1 osea verdadero sale verdadero el 1;
        */ 
        
        resultbitOr = d | f;
        String binario2 = String.format("%4s", Integer.toBinaryString(resultbitOr)).replace(' ', '0');
        System.out.println("Operador OR de bit a bit: "+binario2+".");
        
        /*
          0101 (5)
        | 0011 (3)
          --------
          0111 (7) El | O evalua todos los numeros y si al menos hay un solo 1 o un 1 solo verdadero sale 1;
        */ 
        
        resultbitXor = d ^ f;
        String binario3 = String.format("%4s", Integer.toBinaryString(resultbitXor)).replace(' ', '0');
        System.out.println("Operador XOR de bit a bit: "+binario3+".");
        
        /*
          0101 (5)
        ^ 0011 (3)
          --------
          0110 (6) El XOR ^ evalua todos los numeros y si el 1 o el 0 se repiten la saluda es 0 falso;
        */
        
        resultbitNot = ~d;
        String binario4 = String.format("%4s", Integer.toBinaryString(resultbitNot)).replace(' ', '0');
        System.out.println("Operador XOR de bit a bit: "+binario4+".");
    
        /*
        d = 5;
        00000000000000000000000000000101  (5 en binario)
        --------------------------------
        11111111111111111111111111111010  (Resultado de ~5 en binario)
        
        La representación binaria 11111111111111111111111111111010 es -6 en decimal. Este es el resultado de la operación ~5 en complemento a dos.
        */
        
        desplaizquieda = d << 1;
        String binario5 = String.format("%4s", Integer.toBinaryString(desplaizquieda)).replace(' ', '0');
        System.out.println("Desplazamiento a la Izquierda (<<): "+binario5+".");
        
        /*
        0101(5) << 1 = 1010 se le agrega un 0 al final.
        */
        
        despladerecha = d >> 1;
        String binario6 = String.format("%4s", Integer.toBinaryString(despladerecha)).replace(' ', '0');
        System.out.println("Desplazamiento a la Derecha (>>): "+binario6+".");
        
        /*
        0101(5) >> 0010 se agrega un 0 a la izquierda al principio.
        */
        
        desplaDconExtensióndeCero = e >>> 2;
        String binario7 = String.format("%4s", Integer.toBinaryString(desplaDconExtensióndeCero)).replace(' ', '0');
        System.out.println("Desplazamiento a la Derecha (>>>): "+binario7+".");
        System.out.println("");
        
        //Operadores Ternarios
        
        int max = (a > b) ? a : b;
        System.out.println("Uso de condicional 'Ternario': El numero mayor es: "+max);
        System.out.println("");
        
        //Operadores de Instancia
        
        Auto autogenerico = new Auto();
        Toyota tcorolla = new Toyota();
        System.out.println("Operador de Instancia da False porque autogenerico no herada de Toyota: "+(autogenerico instanceof Toyota));
        System.out.println("Operador de Instancia da True porque tcorolla herada de Auto: "+(tcorolla instanceof Auto));
        System.out.println("");
        
        //Estructuras de Control
        
        if(a < b){
            System.out.println("b es mayor que a");
        }
        else {
            System.out.println("a es mayor que b");
        }
        System.out.println("");
        int day = 2;
        switch (day) {
        case 1:
        System.out.println("Lunes");
        break;
        case 2:
        System.out.println("Martes");
        break;
        case 3:
        System.out.println("Miércoles");
        break;
        default:
        System.out.println("Día no válido");
        break;
        }
        System.out.println("");
        for(int i=10;i>=0;i--){
            System.out.println("Bucle que decrece: "+i);
        }
        
        System.out.println("");
        
        int w=0;
        
        while (w<=10){
            System.out.println("Bucle normal: "+w);
            w++;
        }
        
        System.out.println("");
        
        int dow= 10 ;
        
        do {
            System.out.println("bucle do while: "+dow);
            dow+=10;
        }while(dow <=100);
        
        System.out.println("");    
        
        //Excepciones
       
        try {
            int resultex = 10 / 0;
        } catch (ArithmeticException t) {
            System.out.println("Error: División por cero.");
        }
        System.out.println("");
        /* DIFICULTAD EXTRA (opcional):
        * Crea un programa que imprima por consola todos los números comprendidos
        * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/
        
        for(int i=10;i<=55;i++){
            if(i%2==0 && i!=16 && i%3!=0 ){
                System.out.println(i);
            }
            
        }    
        
    }
}