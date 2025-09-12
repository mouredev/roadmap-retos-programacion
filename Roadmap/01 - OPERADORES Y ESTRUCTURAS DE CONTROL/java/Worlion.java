import java.util.logging.ConsoleHandler;
import java.util.logging.LogRecord;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class Worlion {

    private static Logger log = Logger.getLogger(Worlion.class.getName());
    
    static {
        log.setUseParentHandlers(false);
        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setFormatter(new SimpleFormatter() {
            @Override
            public String format(LogRecord record) {
                return record.getMessage() + "\n";
            }
        });
        log.addHandler(consoleHandler);
    }
    
    public static void main(String[] args) {
        
        log.info(" \nTipos de operadores en JAVA:\n");
        arithmetics();
        logicals();
        comparision();
        assignment();
        identity();
        bitwise();

        log.info(" \nEstructuaras de control en JAVA:\n");
        conditionals();
        loops();
        exceptions();

        log.info(" \n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");
        extra();
    }

    // Tipos de operadores:

    public static void arithmetics() {

        log.info(" - Operadores aritméticos:");
    
        // addition (+)
        log.info("\tsuma: 2+2="+ (2+2));

        // Subtraction (-)
        log.info("\tresta: 5-2="+ (5-2));

        // Multiplication (*)
        log.info("\tproducto (*): 3x2="+ (3*2));

        // Division (/)
        log.info("\tdivision (/): 25/5="+ (25/5));

        // Modulus (%)
        log.info("\tmódulo (%): 12%5="+ (12%5));

        // Increment (++)
        int n = 5;
        log.info("\tincremento (++): "+ (n++) + "++ = "+n);

        // Decrement (--)
        log.info("\tdecremento (--): "+ (n--) + "++ = "+n);

    }

    public static void logicals() {

        log.info("\n - Operadores lógicos:");
    
        // AND (&&)
        log.info("\tAnd: Verdadero Y Verdadero=" + (true && true));
        log.info("\tAnd: Verdadero Y Falso=" + (true && false));
            
        // OR (||)
        log.info("\tOr: Falso O Verdadero=" + (false || true));
        log.info("\tOr: Falso O Falso=" + (false || false));
            
        // NOT (!)
        log.info("\tNot: No(Verdadero)=" + (!true));
        log.info("\tNot: No(Falso)=" + (!false));

        // XOR (^)
        log.info("\tXOR: Verdadero XOR Verdadero=" + (true ^ true));
        log.info("\tXOR: Verdadero XOR Falso=" + (true ^ false));
    }

    public static void comparision(){
        log.info("\n - Operadores comparacióin:");

        // Equal (==)
        log.info("\tIgual: 5==5=" + (5==5));

        // Not equal (!=)   
        log.info("\tNo igual: 5!=5=" + (5!=5));

        // Greater than (>)
        log.info("\tMayor que: 5>3=" + (5>3));

        // Less than (<)
        log.info("\tMenor que: 5<3=" + (5<3));

        // Greater than or equal to (>=)
        log.info("\tMayor o igual que: 5>=5=" + (5>=5));

        // Less than or equal to (<=)
        log.info("\tMenor o igual que: 5<=5=" + (5<=5));

        // instanceof
        Object obj = new String("Hello");
        log.info("\tInstancia de: obj instanceof String = " + (obj instanceof String));
    }

    public static void assignment(){
        log.info("\n - Operadores asisgnación:");

        int n = 10;
        
        // Igualdad
        log.info("\tIgualdad: n=10="+n);
        
        // Suma y asignación
        log.info("\tSuma y asignación: n+=5 -> "+ (n+=5));
        
        // Resta y asignación
        log.info("\tResta y asignación: n-=5 -> "+ (n-=5));
        
        // Multiplicación y asignación
        log.info("\tMultiplicación y asignación: n*=5 -> "+ (n*=5));
        
        // División y asignación
        log.info("\tDivisión y asignación: n/=5 -> "+ (n/=5));
        
        // Modulo y asignación
        log.info("\tModulo y asignación: n%=5 -> "+ (n%=5));
    }

    public static void identity(){
        log.info("\n - Operadores identidad:");

        int n = 10;
        int m = 10;
        
        // Igualdad
        log.info("\tIgualdad: n==m -> "+ (n==m));

        // Diferente
        log.info("\tDiferente de: n!=m -> "+ (n!=m));
    }

    public static void bitwise(){
        log.info("\n - Operadores de bit:");

        int n = 10;
        int m = 5;
        String nBinary = Integer.toBinaryString(n);
        String mBinary = Integer.toBinaryString(m);
        log.info("\t -> n = "+n +"("+ nBinary+")");
        log.info("\t -> m = "+m +"("+ mBinary+")");


        // AND bit
        log.info("\tAND bit: n("+nBinary+") & m("+mBinary+") -> "+ (n&m) +"(" +Integer.toBinaryString(n&m)+")");

        // OR bit
        log.info("\tOR bit: n("+nBinary+")|m("+mBinary+") -> "+ (n|m) +"(" +Integer.toBinaryString(n|m)+")");

        // XOR bit
        log.info("\tXOR bit: n("+nBinary+")^m("+mBinary+") -> "+ (n^m) +"(" +Integer.toBinaryString(n^m)+")");

        // NOT bit
        log.info("\tNOT bit: ~n("+nBinary+") -> "+ (~n) +"(" +Integer.toBinaryString(~n)+")");

        // desplazamiento a la izquierda
        log.info("\tDesplazamiento a la izquierda: n("+nBinary+")<<2 -> "+ (n<<2) +"(" +Integer.toBinaryString(n<<2)+")");

        // desplazamiento a la derecha
        log.info("\tDesplazamiento a la derecha: n("+nBinary+")>>2 -> "+ (n>>2) +"(" +Integer.toBinaryString(n>>2)+")");
    }

    // Estructuras de control:
    public static void conditionals(){
        
        // if - else if - else
        int n = 10;
        if (n > 5) {
            log.info("El número es mayor que 5");
        } 
        else if(n < 5) {
            log.info("El número es menor que 5");
        }
        else {
            log.info("El número es igual a 5");
        }

        int dia = 3;
        String diaString = null;
        switch (dia) {
            case 1: 
                diaString = "Lunes"; 
                break;
            case 2: 
                diaString = "Martes"; 
                break;
            case 3: 
                diaString = "Miércoles"; 
                break;
            case 4: 
                diaString = "Jueves"; 
                break;
            case 5: 
                diaString = "Viernes"; 
                break;
            case 6: 
                diaString = "Sábado"; 
                break;
            case 7: 
                diaString = "Domingo"; 
                break;
            
            default: log.info("Día no válido"); break;
        }
        if(diaString!=null) {
            log.info("El día '"+ dia+"' de la semana es: " + diaString);
        }
    }

    public static void loops(){
    
        // for
        log.info(" - Iterando con el for:");
        for (int i = 0; i < 5; i++) {
            log.info("\t -Iteración: "+i);
        }

        // while
        log.info(" - Iterando con el while:");
        int i = 0;
        while (i < 5) {
            log.info("\t -Iteración: "+i);
            i++;
        }

        // do-while
        log.info(" - Iterando con el do-while:");
        i = 0;
        do {
            log.info("\t -Iteración: "+i);
            i++;
        } while (i < 5);
    }
    
    public static void exceptions(){
        try {
            int n = 5/0;
        } catch (ArithmeticException e) {
            log.info("Error: "+e.getMessage());
        } finally {
            log.info("Finalizando el programa");
        }
    }

/* 
 *DIFICULTAD EXTRA (opcional):
 */

    private static void extra() {
        for( int i = 10; i <= 55; i+=2) {
            if(i != 16 || i % 3 != 0) {
                System.out.println(i);
            }
        }
    
    }
}
