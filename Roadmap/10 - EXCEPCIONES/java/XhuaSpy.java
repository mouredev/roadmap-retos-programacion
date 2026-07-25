import java.util.InputMismatchException;
import java.util.Scanner;

class ParsearStringAEnteroException extends NumberFormatException{
    public ParsearStringAEnteroException(String mensajito){
        super(mensajito);
    }
}

public class XhuaSpy {
    public static void main(String[] args) {
        try {
            System.out.println(EncontrarDivisionEnArreglo("45", "5", new int[] {1,2,3,4,5,6,7,8,9,10}));
            //System.out.println(EncontrarDivisionEnArreglo(null, null, new int[] {1,2,3,4,5,6,7,8,9,10}));
            //System.out.println(EncontrarDivisionEnArreglo("1", "0", new int[] {1,2,3,4,5,6,7,8,9,10}));
            //System.out.println(EncontrarDivisionEnArreglo("45", "5", new int[] {}));
        } catch ( IllegalArgumentException | ArithmeticException | NullPointerException e) {
            System.out.println(e.getMessage());
        }

        try {
            excepcionIngresoDeDatosNumericos();
        } catch (ArithmeticException | InputMismatchException ae) {
            System.out.println(ae.getMessage());
        }
    }

    //Le pide al usuario dos valores, el divisor debe ser diferente de 0;
    private static void excepcionIngresoDeDatosNumericos() throws InputMismatchException, ArithmeticException{
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("\nIngresa el dividendo: ");
            int dividendo = sc.nextInt();

            System.out.print("\nIngresa el divisor: ");
            int divisor = sc.nextInt();

            System.out.println("(dividendo/divisor) = " + (dividendo / divisor));
        } catch ( InputMismatchException e) {
            throw new InputMismatchException("Ingresaste un valor no numérico. Intenta de nuevo");
        } catch (ArithmeticException ae) {
            throw new ArithmeticException("No se puede dividir por cero");
        }
    }

    /**
     * Este método se encarga de hacer una división, transformando los números ingresados como strings
     * y los divide, esa division es buscada en el arreglo.
     **/
    public static int EncontrarDivisionEnArreglo(String valorDividendo, String valorDivisor, int[] array) throws
            IllegalArgumentException, ParsearStringAEnteroException, ArithmeticException, NullPointerException {

        //si el usuario pasa un valor null se devuelve una NullPointerException;
        if (valorDividendo == null || valorDivisor ==null) throw new NullPointerException("Los valores no pueden ser nulos");

        int valorDividido = getValorDividido(valorDividendo, valorDivisor);

        boolean encontrado = false;
        for (int entero_array : array) {
            if (entero_array == valorDividido) {
                encontrado = true;
                break;
            }
        }
        
        if (!encontrado)
            throw new IllegalArgumentException("El número calculado no está presente en el arreglo.");

        return valorDividido; //Retorna el valor de la división 
    }
    
    //Devuelve el valor ya calculado de la división si los valores son enteros. 
    private static int getValorDividido(String valorDividendo, String valorDivisor) throws 
            ParsearStringAEnteroException, ArithmeticException {
        
        int dividendo, divisor;

        try {
            //trata de transformar el string a entero.
            dividendo = Integer.parseInt(valorDividendo);
            divisor = Integer.parseInt(valorDivisor);
        } catch (NumberFormatException e ) {
            //Lanza la exception personalizada para el fallo al parsear los números.
            throw new ParsearStringAEnteroException("Que malparida cadena, no es un entero coño");
        }

        if (divisor == 0)
            //Lanza una excepción si el divisor es 0.
            throw new ArithmeticException("El numero no puede ser 0 bb");

        return (dividendo / divisor); 
    }
}
