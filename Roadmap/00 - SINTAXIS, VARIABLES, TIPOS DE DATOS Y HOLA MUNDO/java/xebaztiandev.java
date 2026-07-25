public class xebaztiandev {

    public static void main(String[] args) {
        /*
        Url of the official java site: https://www.java.com/es/
        */

        // SYNTAX TYPES FOR COMMENTS :)

        // This is a single line comment.

        /*
        This is a comment of several lines.
        It is useful to describe or reference something in our code.
        */

        /**
         * Comments for documenting our code, it can be classes, methods, attributes, interfaces, etc.
         * I show you an example in line [numero de linea].
         */

        // Here a variable is created without storing a value. In addition, variables must be defined using the camelCase convention.
        int myVariable;
        // Here in our variable, we store a value in memory.
        myVariable = 200;

        /*
        By convention, the names of the constants in Java are written in capital letters and underlined.
        Below is an example of a constant variable.
        */
        final double PI_VALUE = 3.1416;

        // Primitive data types in Java, we can find them in: https://dev.java/learn/language-basics/primitive-types/
        byte myByte = 100; // 8-bit integer type (-128 to 127).
        short myShort = 10000; // 16-bit integer type (-32,768 to 32,767).
        int myInt = 100; // 32-bit integer type, with a minimum value of -2^31 and a maximum value of 2^31 -1.
        long myLong = 900000000L; // 64-bit integer type, with a minimum value of -2^63 and maximum value of 2^63 -1.
        float myFloat = 10.001f; // 32-bit single-precision floating point type.
        double myDouble = 1.80d; // 64-bit double-precision floating point type.
        boolean myBoolean = true; // A type of Boolean data that track true/false conditions.
        char myChar = 'a'; // 16-bit Unicode character.

        // Note: String and integer are not primitive data types, they are special classes instead.
        String message = "¡Hola, java!";
        System.out.println(message);
    }
}
