import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 *
 * @author David Sorroche
 */

public class FuncionesValorReferencia {
    // Ejercicio
    public void funcionPorValor(double numParam) {
        numParam = 4.50;
        System.out.println("Modificación valor pasado por parámetro: " + numParam);
    }
    
    public void funcionPorReferencia(List<String> listadoRefParam) {
        listadoRefParam.add("nuevo Registro.");
        System.out.println("Modificación referencia pasada por parámetro: " + Arrays.toString(listadoRefParam.toArray()));
        
        List<String> nuevoListadoRef = listadoRefParam;
        nuevoListadoRef.add("nuevo registro a un nuevo dato List");
        System.out.println("Impresión del nuevo listado creado en la función: " + Arrays.toString(nuevoListadoRef.toArray()));
    }
    
    // Dificultad Extra
    public double[] funcionPorValor(double num1, double num2) {
        double numAux = num1;
        num1 = num2;
        num2 = numAux;
        
        return new double[]{num1, num2};
    }
    
    public List[] funcionPorReferencia(List<String> listadoRef1, List<String>  listadoRef2) {
        List<String> refAux = listadoRef1;
        listadoRef1 = listadoRef2;
        listadoRef2 = refAux;
        
       return new List[]{listadoRef1, listadoRef2};
    }
}

/*
     * EJERCICIO:
     * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
     *   su tipo de dato.
     * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
     *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
     * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
     *
     * DIFICULTAD EXTRA (opcional):
     * Crea dos programas que reciban dos parámetros (cada uno) definidos como
     * variables anteriormente.
     * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
     *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
     *   se asigna a dos variables diferentes a las originales. A continuación, imprime
     *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
     *   su valor en las segundas.
     *   Comprueba también que se ha conservado el valor original en las primeras.
*/

public class ValorYReferencia {
    public static void main(String[] args) {
        // Para el ejercicio creamos una variable primitiva de tipo double (num) y una estrructura de datos (listadoRef).
        double num = 9.00;
        List<String> listadoRef = new ArrayList<>();
        listadoRef.add("Practicando ejercicios");
        listadoRef.add("Retos de programación");
        listadoRef.add("Mouredev");
        listadoRef.add("en Java, usando Maven.");
        
        // Mostramos los valores originales de las dos variables (double y estructura de datos List<String>
        System.out.println("Valor original: " + num);
        System.out.println("Referencia original: " + Arrays.toString(listadoRef.toArray()));
        
        // Creamos un objeto FuncionesValorReferencia (f) y llamamos a cada uno de los métodos (funcionPorValor y funcionPorReferencia.
        FuncionesValorReferencia f = new FuncionesValorReferencia();
        f.funcionPorValor(num);
        f.funcionPorReferencia(listadoRef);
        
        // Comprobamos si las funciones han modificado el valor de las dos variables originales.
        System.out.println("\nValor actualizado: " + num);
        System.out.println("Referencia actualizada: " + Arrays.toString(listadoRef.toArray()));
        
        // Añadimos la dificultad extra.
        double num1 = 4.00;
        double num2 = 47.75;
        
        List<String> listadoRef1 = new ArrayList<>();
        List<String> listadoRef2 = new ArrayList<>();
        
        listadoRef1.add("Hola");
        listadoRef1.add("Y");
        listadoRef1.add("Adiós");
        
        listadoRef2.add("Probando");
        listadoRef2.add("Intencamibo de datos de referencia");
        
        System.out.println("\n" + num1 +", " + num2);
        double[] valores = f.funcionPorValor(num1, num2);
        double num3 = valores[0];
        double num4 = valores[1];
        System.out.println("\n" + num1 + ", " + num2);
        System.out.println(num3 + ", " + num4);
        
        System.out.println(Arrays.toString(listadoRef1.toArray()) + "\t" + Arrays.toString(listadoRef2.toArray()));
        List[] referencias = f.funcionPorReferencia(listadoRef1, listadoRef2);
        List<String> listadoRef3 = referencias[0];
        List<String> listadoRef4 = referencias[1];
        System.out.println("\n" + Arrays.toString(listadoRef1.toArray()) + "\t" + Arrays.toString(listadoRef2.toArray()));
        System.out.println(Arrays.toString(listadoRef3.toArray()) + "\t" + Arrays.toString(listadoRef4.toArray()));
    }
}


