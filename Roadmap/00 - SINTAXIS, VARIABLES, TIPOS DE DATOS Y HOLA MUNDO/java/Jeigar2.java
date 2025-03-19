public class Jeigar2 {
    // Crea un comentario en el código y coloca la URL del sitio web oficial del
    // lenguaje de programación que has seleccionado.
    // https://docs.oracle.com/en/java/javase/21/

    /*
     * Representa las diferentes sintaxis que existen de crear comentarios
     * en el lenguaje (en una línea, varias...).
     */

    // The byte data type is an 8-bit signed two's complement integer.
    // It has a minimum value of -128 and a maximum value of 127 (inclusive).
    byte aByte;

    // The short data type is a 16-bit signed two's complement integer.
    // It has a minimum value of -32,768 and a maximum value of 32,767 (inclusive).
    short aShort;

    // By default, the int data type is a 32-bit signed two's complement integer,
    // which has a minimum value of -231 and a maximum value of 231-1.
    // In Java SE 8 and later, you can use the int data type to represent an unsigned 32-bit integer,
    // which has a minimum value of 0 and a maximum value of 232-1.
    int anInt;

    // The long data type is a 64-bit two's complement integer.
    // The signed long has a minimum value of -263 and a maximum value of 263-1.
    // In Java SE 8 and later, you can use the long data type to represent an unsigned 64-bit long,
    // which has a minimum value of 0 and a maximum value of 264-1.
    long aLong;

    // The float data type is a single-precision 32-bit IEEE 754 floating point.
    // Its range of values is beyond the scope of this discussion, but is specified in the Floating-Point Types,
    // Formats, and Values section of the Java Language Specification.
    float aFloat;

    // The double data type is a double-precision 64-bit IEEE 754 floating point.
    // Its range of values is beyond the scope of this discussion, but is specified in the Floating-Point Types,
    // Formats, and Values section of the Java Language Specification.
    double aDouble;

    // The boolean data type has only two possible values: true and false.
    // Use this data type for simple flags that track true/false conditions.
    // This data type represents one bit of information, but its "size" isn't something that's precisely defined.
    boolean aBoolean;

    // he char data type is a single 16-bit Unicode character.
    // It has a minimum value of '\u0000' (or 0) and a maximum value of '\uffff' (or 65,535 inclusive).
    char aChar;

    // Constant
    public static final String LANGUAGE = "Java";

    public static void main(String[] args) {
        System.out.println("¡Hola, " + LANGUAGE + "!");
    }
}
