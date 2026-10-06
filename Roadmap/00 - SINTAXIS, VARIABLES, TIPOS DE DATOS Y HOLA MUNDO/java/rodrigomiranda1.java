import java.math.BigDecimal;
import java.math.BigInteger;

public class rodrigomiranda1 {

    private static final String Constante = "constante a nivel de clase";
    public static void main (String[] args){
        //sitio oficial de java https://docs.oracle.com/javase/8/docs/api/

        //una linea

    /*
    varias
    lineas
     */

        String variable = "esto es una variable";
        final String constante = "esto es una constante a nivel de metodo";

        char simbolo = '#';
        String lenguaje = "Java";
        Integer entero = 10;
        BigInteger enteroLargo = BigInteger.valueOf(87318237283L);
        Long largo = 32873233L;
        Double decimal = 5.5;
        BigDecimal decimalLargo = BigDecimal.valueOf(372381.237613723);
        boolean booleano = true;
        float peso = 73.2f;
        short numeropequeño = 240;

        System.out.println("¡Hola " + lenguaje + "!" );
    }

}
