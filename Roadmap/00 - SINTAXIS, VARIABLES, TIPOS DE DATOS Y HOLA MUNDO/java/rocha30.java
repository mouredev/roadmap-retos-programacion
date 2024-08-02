/* Solución del reto #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
* @author rocha30
*/

//https://dev.java/


//Esta es una manera de comentar en java en una sola linea

/*Esta es otra manera de comentar en java 
con varias lineas  */

/**
* Este tipo de comentarios 
sirve para documentacion en javadoc
*/



public class rocha30 {

    public static void main(String[] args) {
 
        //variables y constantes
        final String texto = "soy un texto constante";
        String variable = "Soy un texto variable ";
 
 
        //Variables con todos los tipos de datos 
        byte numeroMuyPequeño = 100; //para numeros con 8 bits 
        short numeroPequeño = 10; //para numeros de 16 bits 
        int numero = 100; //para numeros con 32 bits 
        long numeroMasGrande = 1000000000; //para numeros con 64 bits 
        float decimalPequeño = 12.83425f; // decimal de 32 bits (el subfijo f es necesario)
        double decimal = 12.9837488; //decimal con 64 bits 
 
        boolean datoslogicos = true; 
        boolean datoslogicosfalsos = false; 
        char caracter = 'a'; // solo para caracteres 
        String saludo = "Buenos días a todos"; //tipo de dato no primitivo 
 
        //Impresión de texto en la terminal 
 
        System.out.println("Hola, Java!");
 
    }
    
 }