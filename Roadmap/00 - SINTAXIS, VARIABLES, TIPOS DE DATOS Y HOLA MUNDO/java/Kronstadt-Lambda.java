// https://docs.oracle.com/en/java/javase/21/

/**
 * This is a javadoc comment
 * @author Kronstadtlambda
 * @version 1.0
 */

// here define the package name
// package roadmap.java.r00;

// here import the necessary library (optional)
import java.util.Random;

/**
 * Class to show the basic sintax and others of Java programming language
 */
public class KronstadtLambda {
    /**
     * Main method to execute the code of this class (entry point)
     */
    public static void main(String[] args) {

        // Sintax to create comments:
        // This is a single line comment
        /* This is a multi-line comment 
         * or more lines 
         */

        // Sintax to manage puntuation:
        // ; -> end of the statement.
        // {} -> delimit block of code.
        // () -> parameters, conditions, group expressions.
        // [] -> declare arrays, [index] access to elements.
        // . -> access to methods, attributes, etc.
        // @ -> annotations.
        // :: -> method reference (functional programming).

        // Variables and constants
        float variable_high; 
        final float CONSTANT_COULUMB;
        variable_high = 1.7f;   //meters
        CONSTANT_COULUMB = 8.9875517873681764e9f; // N m^2 C^-2

        // Primitive data types
        byte v_byte; // Integer 8 bits
        short v_short; // Integer 16 bits
        int v_int; // Integer 32 bits
        long v_long; // Integer 64 bits
        float v_float; // Floating point 32 bits
        double v_double; // Floating point 64 bits
        char v_char; // Unicode character 16 bits
        boolean v_boolean; // Logical 8 bits

        v_byte = 127;
        v_short = 32767;
        v_int = 2147483647;
        v_long = 9223372036854775807L;
        v_float = 3.4028235e38f;
        v_double = 1.7976931348623157e308;
        v_char = 'K';
        v_boolean = true;

        System.out.println("A byte: " + v_byte);
        System.out.println("A short: " + v_short);
        System.out.println("An int: " + v_int);
        System.out.println("A long: " + v_long);
        System.out.println("A float: " + v_float);
        System.out.println("A double: " + v_double);
        System.out.println("A char: " + v_char);
        System.out.println("A boolean: " + v_boolean);

        // Print a greeting
        String v_language = "Java";
        System.out.println("Hello, " + v_language + "!");

        // Style guide
        /* 
         * Nomenclature:
         * Use PascalCase for class names and interface names.
         * Use camelCase for method and variables names.
         * UPPER_CASE for constants.
         * 
         * Comentary:
         * Use comentary to explain the code, not what the code does.
         * 
         * Code organization:
         * Use a maximum of 80 characters per line.
         * Use 4 spaces to indent code and avoid using tabs.
         * 
         * Declaration:
         * Group the declarations of variables at the beginning of the class.
         */
        
    } // end of the main method
} // end of the class

