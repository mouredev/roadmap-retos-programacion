//#00 - Java

// Comentar en una línea
/*Comentar en varias líneas */
/*
 * Comentar
 * en varias líneas
 * docuemntación
 */

public class inmortalnight {
    //Variable
    String var = "something";
    //Constante
    final String constant= "something";
    //Tipos de datos primitivos
    byte bit = 8; //-128 al 127
    short one = 1; //-32,768 al 32,767, igual que int pero con menos memoria
    int realNumber = 24; //-2,147,483,648 al 2,147,483,647
    long bigNumber = 1000000000; //-9,223,372,036,854,775,808 al 9,223,372,036,854,775,807
    float decimal = 1.5f; //32 bits, rango de 1.4e-45 a 3.4028235e+38
    double doubleDecimal = 1.5; //64 bits, rango de 4.9e-324 a 1.7976931348623157e+308
    boolean negativo = true; //true o false, 1 bit
    char letter = 'a'; //16 bits, rango de 0 a 65,535, letras y simbolos
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
    }
}