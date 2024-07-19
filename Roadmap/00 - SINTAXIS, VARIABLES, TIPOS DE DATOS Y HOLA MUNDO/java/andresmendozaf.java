
public class andresmendozaf {

    public static void main(String[] args) {

        //Sitio oficial de JAVA en un comentario simple http://www.java.com.es
        //Este es un comentario de una línea

        /*
        Esto permite
        comentar varias
        líneas de texto 
         */
        /**
         * Comentario de documentación en varias lineas Se utiliza antes de una
         * clase, método o función
         *
         * Permite documentar el código usando etiquetas:
         *
         * @param nombreDelParametro permite documentar sobre un parametro y se
         * pueden usar tantas como parametros tenga el método.
         * @return Se utiliza para documentar el resultado que retorna un
         * método.
         * @throws Documenta una excepción. otros
         */
        /**
         * CREACIÓN DE VARIABLES Y CONTANTES
         */
        String variable = "variable";
        System.out.println("Este es el ejemplo de una " + variable);

        final double pi = 3.1416;
        System.out.println("Este podría ser un ejemplo de constante " + pi);

        /**
         * TIPOS DE DATOS PRIMITIVOS
         */
        /**
         * byte: Representa un tipo de dato de 8 bits con signo. Puede almacenar
         * valores numéricos en el rango de -128 a 127, incluyendo ambos
         * extremos.
         */
        byte byteNegativo = -15;
        byte bytePositivo = 15;
        System.out.println("Esto es el ejemplo de BYTE, tanto negativo como positivo : " + byteNegativo + " - " + bytePositivo);

        /**
         * short: Este tipo de dato utiliza 16 bits con signo y puede almacenar
         * valores numéricos en el rango de -32,768 a 32,767.
         */
        short shortNegativo = -15600;
        short shortPositivo = 15600;
        System.out.println("Esto es el ejemplo de SHORT, tanto negativo como positivo : " + shortNegativo + " - " + shortPositivo);

        /**
         * int: Es un tipo de dato de 32 bits con signo utilizado para almacenar
         * valores numéricos. Su rango va desde -2,147,483,648 (-2^31) hasta
         * 2,147,483,647 (2^31 - 1). Es el tipo de dato más comúnmente utilizado
         * para representar números enteros.
         */
        int intNegativo = -14;
        int intPositivo = 14;
        System.out.println("Esto es el ejemplo de INT, tanto negativo como positivo : " + intNegativo + " - " + intPositivo);

        /**
         * long: Este tipo de dato utiliza 64 bits con signo y puede almacenar
         * valores numéricos en el rango de -9,223,372,036,854,775,808 (-2^63) a
         * 9,223,372,036,854,775,807 (2^63 - 1). Se utiliza cuando se necesitan
         * números enteros muy grandes.
         */
        long longNegativo = -19042011;
        long longPositivo = 19042011;
        System.out.println("Esto es el ejemplo de LONG, tanto negativo como positivo : " + longNegativo + " - " + longPositivo);

        /**
         * float: Es un tipo de dato diseñado para almacenar números en coma
         * flotante con precisión simple de 32 bits. Se utiliza cuando se
         * requieren números decimales con un grado de precisión adecuado para
         * muchas aplicaciones.
         */
        float floatNegativo = -186.56874f;
        float floatPositivo = 186.56874f;
        System.out.println("Esto es el ejemplo de FLOAT, tanto negativo como positivo : " + floatNegativo + " - " + floatPositivo);

        /**
         * double: Este tipo de dato almacena números en coma flotante con doble
         * precisión de 64 bits, lo que proporciona una mayor precisión que
         * float. Se usa en aplicaciones que requieren una alta precisión en
         * cálculos numéricos.
         */
        double doubletNegativo = -19879886.56564874d;
        double doublePositivo = 18987986.56874564d;
        System.out.println("Esto es el ejemplo de DOUBLE, tanto negativo como positivo : " + doubletNegativo + " - " + doublePositivo);

        /**
         * boolean: Sirve para definir tipos de datos booleanos que pueden tener
         * solo dos valores: true o false. Aunque ocupa solo 1 bit de
         * información, generalmente se almacena en un byte completo por razones
         * de eficiencia.
         */
        boolean booleanFalse = false;
        boolean booleanTrue = true;
        System.out.println("Esto es el ejemplo de BOOLENA, tanto " + booleanFalse + " como " + booleanTrue);

        /**
         * char: Es un tipo de datos que representa un carácter Unicode sencillo
         * de 16 bits. Se utiliza para almacenar caracteres individuales, como
         * letras o símbolos en diferentes lenguajes y conjuntos de caracteres.
         */
        char charNumerico = 5;
        char charCaracteres = 'r';
        System.out.println("Esto es el ejemplo de CHAR, puede ser numérico " + charNumerico + " o de caracteres " + charCaracteres);

        /**
         * Imprimir por consola
         */
        System.out.println("Hola JAVA!");
    }

}
