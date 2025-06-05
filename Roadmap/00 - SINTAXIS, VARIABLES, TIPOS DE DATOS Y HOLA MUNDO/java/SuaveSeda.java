public class SuaveSeda {

    /*
        Sintaxis
        para crear comentarios
        en varias lineas
     */
    
    //  Sitio oficial del lenguaje seleccionado: https://www.java.com/es/
    //  <--- Sintaxis para crear comentarios en una linea.
    
    public static void main(String[] args) {

        String languaje= "Java"; // creación de una variable String
        final int dia_semana = 7; // creacion de una constante "final"-> indica que no cambiará su valor.


        // Representacion de los diferentes tipo primitivos

        byte newByte= 2;               // Byte -128 t0 127
        short newShort= 234;           // Short -32,6768 to 32,6767
        int newInteger= 667889265;     // Integer -2,147,483,648 to 2,147,483,647
        long newLong= 12345678900L;    // Long -9,223,372,036,854,775,808 y 9,223,372,036,854,775,807
        float newFloat= 2314.98f;      // Float 6-7 decimal digits
        double newDouble= 4563.78665;  // Double 15-16 decimal digits
        boolean newBoolean= false;     // Boolean true or false
        char newChar= 'H';             // Char single character/letter or ASCII


        // Imprimir por pantalla el nombre del lenguaje que he seleccionado.

        System.out.println("Hola Mundo! He escogido " + languaje + "!! WoooWW");

    }
    
}