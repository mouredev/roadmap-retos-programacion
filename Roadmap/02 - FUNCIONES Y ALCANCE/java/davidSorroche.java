
public class Funciones {
    /*
        * - Crea ejemplos de funciones básicas que representen las diferentes
        *   posibilidades del lenguaje:
        *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
        * - Comprueba si puedes crear funciones dentro de funciones.
        * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
        * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
        * - Debes hacer print por consola del resultado de todos los ejemplos.
        *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
    */
    private final String textoFunciones = "Reto de Programación #02 FUNCIONES Y ALCANCE - Java";
    
    // Devuelve el texto de la constante "textoFunciones".
    public void funcionSinParametrosSinRetorno() {
        System.out.println(textoFunciones);
    }
    
    // Devuelve un mensaje de error junto al texto pasado por parámetro.
    public void funcionConParametrosSinRetorno(String texto) {
        System.err.println("¡¡¡ ERROR !!!\n".concat(texto));
    }
    
    // Devuelve un número aleatorio comprendido entre los enteros (int) 1 y 10.
    public int funcionSinParametrosConRetorno() {
        return (int) (Math.random() * 10) + 1;
    }
    
    /*
        Devuelve la multiplicación, si num 1 es menor o igual que num2, 
        o la división en caso contrario de los dos números pasador por parámetros.
    */
    public double funcionConParametrosConRetorno(double num1, double num2, int num3) {
        /*
            Si el segundo número es 0 y es menor que el primer número no realiza 
            el cálculo de la función.
        */
        if(num2 == 0 && num1 > num2) {
            throw new ArithmeticException("No se puede dividir ningún número entre 0");
        }
        
        return num1 <= num2 ? Math.round((((num1 * num2) - num3) * 100.0) / 100.0) 
                            : Math.round((((num1 / num2) + num3) * 100.0) / 100.0);
    }
}

public class DificultadExtraFunciones_Alcances {
    /*
        * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
        * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
        *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
        *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
        *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
        *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
        *
        * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
    */
    
    public int numerosYTextos(String texto1, String texto2) {
        // Inicializamos el contador de impresos de números a 0.
        int contadorImpresosNumeros = 0;
        
        /* 
            Formateamos los textos pasados por parámetros para que no dejen espacios
            ni al principio ni al final y evitar más de un espacio entre palabras.
        */
        texto1 = texto1.trim().replaceAll("\s+", " ");
        texto2 = texto2.trim().replaceAll("\s+", " ");
        
        /*
            Creamos un bucle que vaya de 1 a 100 y vaya imprimiendo los números y
            textos correspondientes.
        */
        for(int numero = 1; numero <= 100; numero++) {
            /* 
                Si el número es múltipo de 3 y de 5 imprime las dos cadenas de textos
                pasadas por parámetros concatenadas con un espacio entre ellas.
            */
            if (esMultiploDe3(numero) && esMultiploDe5(numero)) {
                System.out.println(texto1.concat(" ").concat(texto2));
            } 
            // Si el número es sólo múltiplo de 3, imprime el primer texto.
            else if (esMultiploDe3(numero)) {
                System.out.println(texto1);
            } 
            // Si el número es sólo múltiplo de 5, imprime el segundo texto.
            else if (esMultiploDe5(numero)) {
                System.out.println(texto2);
            } 
            /* 
                En cualquier otro caso imprime el número e incremeta el contador 
                de impresos de números en una unidad.
            */
            else {
                System.out.println(numero);
                contadorImpresosNumeros++;
            }
        }
        
        // Devuelve el valor del contador de impresos de números.
        return contadorImpresosNumeros;
    }
    
    // Devuelve true si número es múltiplo de 3, y false en caso contrario.
    private boolean esMultiploDe3(int numero) {
        return numero % 3 == 0;
    }
    
    // Devuelve true si número es múltiplo de 5, y false en caso contrario.
    private boolean esMultiploDe5(int numero) {
        return numero % 5 == 0;
    }
}

public class PrincipalFunciones_Alcances {
    public static void main(String[] args) {
        Funciones f = new Funciones();
        
        f.funcionSinParametrosSinRetorno();
        f.funcionConParametrosSinRetorno("Ná, es bromita.");
        System.out.println(f.funcionSinParametrosConRetorno());
        System.out.println(f.funcionConParametrosConRetorno(11, 30, 5));
        System.out.println(f.funcionConParametrosConRetorno(30, 11, 10));
        System.out.println(f.funcionConParametrosConRetorno(11, 11, 11));
        
        DificultadExtraFunciones_Alcances dE = new DificultadExtraFunciones_Alcances();
        System.out.println("\n" + dE.numerosYTextos("     Practicando Retos    De Programación", "#02 Funciones Y Alcance - Java"));
    }
}
