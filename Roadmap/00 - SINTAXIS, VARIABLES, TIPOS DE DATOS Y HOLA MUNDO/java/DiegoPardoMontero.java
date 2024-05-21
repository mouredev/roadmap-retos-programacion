public class DiegoPardoMontero {
    public static void main(String[] args) {
        /*
        Comentario con URL de mi lenguaje:
        https://www.java.com/es/

        Tres Formas de hacer comentarios:
        1. Usando // para comentarios de una sola linea
        2. Usando / * Contenido del comentario * / para comentarios de
        varias lineas
        3. Usando /** * / para comentarios de JavaDoc:
        Compuestos por:
        @author [nombreAutor]
        @param [nombreParametro] [descripcion]
        @return [descripcionDelRetorno]
        @exception o @throws [tipoExcepcion] [razonExcepcion]
        @version [versionSoftware]
        @deprecated [razonObsolescencia]
         */

        //Variable ejemplo
        String miVariable = "¡Hola,";

        //Constante ejemplo
        final String miConstante = " Java!";

        //Variables con tipos de datos primitivos
        byte miDatoByte = 1;
        short miDatoShort = 2;
        int miDatoEntero = 4;
        long miDatoLong = 8;
        double miDatoDouble = 3.2;
        float miDatoFloat = 4.5f;
        boolean miDatoBooleano = true;
        char miDatoChar = 'A';

        //Impresión normal:
        System.out.println(miVariable + miConstante);
    }
}
