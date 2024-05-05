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

public class Worlion {

    public static void main(String[] args) {
        
        print(" \nTipos de operadores en JAVA:\n");
        arithmetics();
        logicals();
        comparision();
        assignment();
        identity();
        bitwise();

    }

    // Tipos de operadores:

    public static void arithmetics() {

        print(" - Operadores aritméticos:");
    
        // addition (+)
        print("\tsuma: 2+2="+ (2+2));

        // Subtraction (-)
        print("\tresta: 5-2="+ (5-2));

        // Multiplication (*)
        print("\tproducto (*): 3x2="+ (3*2));

        // Division (/)
        print("\tdivision (/): 25/5="+ (25/5));

        // Modulus (%)
        print("\tmódulo (%): 12%5="+ (12%5));

        // Increment (++)
        int n = 5;
        print("\tincremento (++): "+ (n++) + "++ = "+n);

        // Decrement (--)
        print("\tdecremento (--): "+ (n--) + "++ = "+n);

    }

    public static void logicals() {

        print("\n - Operadores lógicos:");
    
        // AND (&&)
        print("\tAnd: Verdadero Y Verdadero=" + (true && true));
        print("\tAnd: Verdadero Y Falso=" + (true && false));
            
        // OR (||)
        print("\tOr: Falso O Verdadero=" + (false || true));
        print("\tOr: Falso O Falso=" + (false || false));
            
        // NOT (!)
        print("\tNot: No(Verdadero)=" + (!true));
        print("\tNot: No(Falso)=" + (!false));

        // XOR (^)
        print("\tXOR: Verdadero XOR Verdadero=" + (true ^ true));
        print("\tXOR: Verdadero XOR Falso=" + (true ^ false));
    }

    public static void comparision(){
        print("\n - Operadores comparacióin:");

        // Equal (==)
        print("\tIgual: 5==5=" + (5==5));

        // Not equal (!=)   
        print("\tNo igual: 5!=5=" + (5!=5));

        // Greater than (>)
        print("\tMayor que: 5>3=" + (5>3));

        // Less than (<)
        print("\tMenor que: 5<3=" + (5<3));

        // Greater than or equal to (>=)
        print("\tMayor o igual que: 5>=5=" + (5>=5));

        // Less than or equal to (<=)
        print("\tMenor o igual que: 5<=5=" + (5<=5));

        // instanceof
        Object obj = new String("Hello");
        print("\tInstancia de: obj instanceof String = " + (obj instanceof String));
    }

    public static void assignment(){
        print("\n - Operadores asisgnación:");

        int n = 10;
        
        // Igualdad
        print("\tIgualdad: n=10="+n);
        
        // Suma y asignación
        print("\tSuma y asignación: n+=5 -> "+ (n+=5));
        
        // Resta y asignación
        print("\tResta y asignación: n-=5 -> "+ (n-=5));
        
        // Multiplicación y asignación
        print("\tMultiplicación y asignación: n*=5 -> "+ (n*=5));
        
        // División y asignación
        print("\tDivisión y asignación: n/=5 -> "+ (n/=5));
        
        // Modulo y asignación
        print("\tModulo y asignación: n%=5 -> "+ (n%=5));
    }

    public static void identity(){
        print("\n - Operadores identidad:");

        int n = 10;
        int m = 10;
        
        // Igualdad
        print("\tIgualdad: n==m -> "+ (n==m));

        // Diferente
        print("\tDiferente de: n!=m -> "+ (n!=m));
    }

    public static void bitwise(){
        print("\n - Operadores de bit:");

        int n = 10;
        int m = 5;
        String nBinary = Integer.toBinaryString(n);
        String mBinary = Integer.toBinaryString(m);
        print("\t -> n = "+n +"("+ nBinary+")");
        print("\t -> m = "+m +"("+ mBinary+")");


        // AND bit
        print("\tAND bit: n("+nBinary+") & m("+mBinary+") -> "+ (n&m) +"(" +Integer.toBinaryString(n&m)+")");

        // OR bit
        print("\tOR bit: n("+nBinary+")|m("+mBinary+") -> "+ (n|m) +"(" +Integer.toBinaryString(n|m)+")");

        // XOR bit
        print("\tXOR bit: n("+nBinary+")^m("+mBinary+") -> "+ (n^m) +"(" +Integer.toBinaryString(n^m)+")");

        // NOT bit
        print("\tNOT bit: ~n("+nBinary+") -> "+ (~n) +"(" +Integer.toBinaryString(~n)+")");

        // desplazamiento a la izquierda
        print("\tDesplazamiento a la izquierda: n("+nBinary+")<<2 -> "+ (n<<2) +"(" +Integer.toBinaryString(n<<2)+")");

        // desplazamiento a la derecha
        print("\tDesplazamiento a la derecha: n("+nBinary+")>>2 -> "+ (n>>2) +"(" +Integer.toBinaryString(n>>2)+")");
    }

    public static void print(String s){
        System.out.println(s);
    }
}
