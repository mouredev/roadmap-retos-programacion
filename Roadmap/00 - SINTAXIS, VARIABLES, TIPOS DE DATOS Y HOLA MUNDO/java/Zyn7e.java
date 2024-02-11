public class Zyn7e {
  public void main (String[] args) {

    /*
     * ###########################
     * TIPOS DE COMENTARIOS
     * ###########################
     */

    // Sitio oficial de Java en español en un cometario simple: https://www.java.com/es/

    /*
     * Este es un comentario en varias lineas
     * y se puede escribir tantas lineas
     * como necesites.
     */

    /**
     * Este es un comentario de documentación en varias lineas
     * Se utiliza antes de una clase, método o función
     *
     * Permite documentar el código usando etiquetas:
     * @param nombreDelParametro permite documentar sobre un parametro
     *                           y se pueden usar tantas como parametros
     *                           tenga el método.
     * @return Se utiliza para documentar el resultado que retorna un método.
     * @throws Documenta una excepción.
     */



    /*
     * ###########################
     * CREACIÓN DE VARIABLES Y CONTANTES
     * ###########################
     */

    // Variable
    String miVariable = "Hola";

    // Constante
    const int miConstanteDePI = 3.14159;



    /*
     * ###########################
     * VARIABLES Y TIPOS DE DATOS PRIMITIVOS
     * ###########################
     */

    // Existen 8 tipos de datos primitivos:

    // ###### Números enteros ######
    /*
     * byte: Representa un tipo de dato de 8 bits con signo.
     * Puede almacenar valores numéricos en el rango de -128 a 127,
     * incluyendo ambos extremos.
     */
    byte numeroNegativoByte = -26;
    byte numeroPositivoByte = 50;

    /*
     * short: Representa un tipo de dato de 16 bits con signo.
     * Puede almacenar valores numéricos en el rango de -32,768 a 32,767,
     * incluyendo ambos extremos.
     */
    short numeroNegativoShort = -24000;
    short numeroPositivoShort = 10000;

    /*
     * int: Representa un tipo de dato de 32 bits con signo.
     * Puede almacenar valores numéricos en el rango de -2,147,483,648 a 2,147,483,647,
     * incluyendo ambos extremos.
     */
    int numeroNegativoInt = -1000000000;
    int numeroPositivoInt = 2000000000;

    /*
     * long: Representa un tipo de dato de 64 bits con signo.
     * Puede almacenar valores numéricos muy grandes (y pequeños)
     * con precisión.
     */
    long numeroNegativoLong = -30000000000000000000000000L;
    long numeroPositivoLong = 3000000000000000000000000000L;


    // ###### Números de punto flotante ######

    /*
     * float: Representa un número de punto flotante de 32 bits.
     */
    float numeroFloat = 12.450F;

    /*
     * double: Representa un número de punto flotante de 64 bits.
     */
    double numeroDouble = 12345.34564567D;


    // ###### Char ######

    /*
     * char: Representa un carácter Unicode de 16 bits.
     */
    char miChar = 'A';


    // ###### Valores lógicos ######
    /*
     * boolean: Representa un valor lógico, verdadero o falso.
     */
    boolean booleanVerdadero = true;
    boolean booleanFalso = false;



    /*
     * ###########################
     * IMPRESIÓN EN PANTALLA
     * ###########################
     */

    System.out.println("Hola, Java!!");
  }

}