      * COMENTARIO DE UNA LINEA. SIEMPRE EN LA COLUMNA 7               *
      * NO TIENE PORQUE FINALIZAR EN * PERO SE HACE POR CONVENIO       *
      * PARA SABER DONDE ACABA LA COLUMNA 72 QUE ES LA ULTIMA DONDE    *
      * PODEMOS CODIFICAR                                              *
      * CONVIENE DEJAR SIEMPRE UN ESPACIO DESPUES DEL ASTERISCO PORQUE *
      * SI "CONTROL" ES LA SIGUIENTE PALABRA, LA LEE COMO SI NO FUERA  *
      * UN COMENTARIO Y DA ERROR. CURIOSO, EH?                         *
      * TAMPOCO DEBEN PONERSE ACENTOS PORQUE CREA HEXADECIMALES NO     *
      * VISIBLES Y SALE UN WARNING CADA VEZ QUE EDITAS EL CODIGO Y PARA*
      * QUITARLOS HAY QUE EDITAR EN HEX ON Y CONVERTIR EN ESPACIO (4)  *
      ******************************************************************
      *                  IDENTIFICATION DIVISION                       *
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO00.
       AUTHOR. AFRICA
      ******************************************************************
      *                  ENVIRONMENT DIVISION                          *
      ******************************************************************
       ENVIRONMENT DIVISION.
      ******************************************************************
      *                      DATA DIVISION                             *
      ******************************************************************
       DATA DIVISION.

       WORKING-STORAGE SECTION.

      ******************************************************************
      * AQUI SE DISE#AN LAS VARIABLES. PONGO LAS MAS HABITUALES EN EL  *
      * ENTORNO DE GESTION, COMO BANCOS, SEGUROS, HACIENDA, SEG SOC,   *
      * GOBIERNOS, TELEFONICAS, Y TODAS LAS GRANDES EMPRESAS           *
      * TIPO A: SOLO PARA LETRAS Y ESPACIOS. EN DESUSO AL EXISTIR "X". *
      * TIPO X: ADMITE COMO LA "A" MAS CARACTERES ESPECIALES Y NUMEROS.*
      * TIPO 9: NUMERICAS, CON O SIN DECIMALES, EMPAQUETADAS O BINARIAS*
      * EL NUMERO ENTRE PARENTESIS INDICA EL NUMERO DE DIGITOS A ELEGIR*
      * 01 ES PARA VARIABLE INICIAL DE GRUPO (ESTRUCTURA)              *
      * 05 POR ESTANDARES. INDICA PERTENENCIA A ESE GRUPO DE NÌ NFERIOR*
      * CONVIENE PIC Y VALUE EN MISMA COLUMNA PARA FACILITAR LA LECTURA*
      * COMP, COMP-4 Y BINARY SON SINONIMOS                            *
      * COMP-3 Y PACKED-DECIMAL SON SINONIMOS                          *
      * ZERO, ZEROS, ZEROES Y 0 SON SINOMINOS                          *
      * NO TENEMOS CONSTANTES. SOLO VARIABLES QUE NO VARIAN            *
      * NO TENEMOS BOOLEANOS. EL PROGRAMADOR CREA VARIABLE Y JUEGA A   *
      * CONVENIENCIA CON 0 Y 1 U OTRA COMBINACION COMO SI Y NO, V O F  *
      ******************************************************************
       01  VARIABLES-ALFA.
           05  ALFABETICA           PIC A(3)            VALUE 'ABC'.
           05  ALFANUMERICA         PIC X(3)            VALUE 'Z8@'.

       01  VARIABLES-NUMERICAS.
           05  ENTERO               PIC 9(7)            VALUE 0.
           05  UN-DECIMAL           PIC 9(7)V9          VALUE ZEROES.
           05  DECIMAL-SIGNADO      PIC S9(7)V99        VALUE 4.5.
           05  DECIMAL-EMPAQUETADO  PIC  9(7)V99 COMP-3 VALUE 123.
           05  DECIMAL-EMPAQUETADOS PIC S9(7)V99 COMP-3 VALUE -5.22.
           05  BINARIA-PEQUENA      PIC S9(4)    COMP   VALUE ZERO.
           05  BINARIA-GRANDE       PIC S9(9)    COMP-4 VALUE ZEROS.
           05  BINARIA-MAXI         PIC S9(18)   BINARY VALUE ZEROS.

       01  CONSTANTES.
           05  CTE-SALUDO           PIC X(5)            VALUE 'HOLA'.
           05  CTE-LENGUAJE         PIC X(5)            VALUE 'COBOL'.

      ******************************************************************
      *                      PROCEDURE DIVISION                        *
      ******************************************************************
       PROCEDURE DIVISION.
           DISPLAY CTE-SALUDO CTE-LENGUAJE.
           STOP RUN.

