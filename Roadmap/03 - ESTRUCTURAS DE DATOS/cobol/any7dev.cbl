     /*
      * EJERCICIO:
      * - Muestra ejemplos de creaci�n de todas las estructuras soportadas por defecto en tu lenguaje.
      * - Utiliza operaciones de inserci�n, borrado, actualizaci�n y ordenaci�n.
      *
      * DIFICULTAD EXTRA (opcional):
      * Crea una agenda de contactos por terminal.
      * - Debes implementar funcionalidades de b�squeda, inserci�n, actualizaci�n y eliminaci�n de contactos.
      * - Cada contacto debe tener un nombre y un n�mero de tel�fono.
      * - El programa solicita en primer lugar cu�l es la operaci�n que se quiere realizar, y a continuaci�n
      *   los datos necesarios para llevarla a cabo.
      * - El programa no puede dejar introducir n�meros de tel�fono no n�mericos y con m�s de 11 d�gitos.
      *   (o el n�mero de d�gitos que quieras)
      * - Tambi�n se debe proponer una operaci�n de finalizaci�n del programa.
      */
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-03.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.

           01 TABLA.
      * Es indexada para poder buscar
               05 AGENDA OCCURS 25 TIMES INDEXED BY INDICE.
                   10 NOMBRE PIC X(10).
                   10 NUMERO PIC 9(9).

           01 OPCIONES-MENU PIC X.
               88 ALTA VALUE 1.
               88 ACTUALIZAR VALUE 2.
               88 QUITAR VALUE 3.
               88 MUESTRA VALUE 4.
               88 BUSCA VALUE 5.
               88 SALE VALUE 0.

           77 CONTADOR PIC 9 VALUE 0.
           77 CONTADOR-AUX PIC 9 VALUE 1.
           77 NOMBRE-AUX PIC X(10).
           77 NOMBRE-NUEVO PIC X(10).
           77 NUMERO-NUEVO PIC 9(9).
           77 OPCION PIC 9.

       PROCEDURE DIVISION.

       EJERCICIO.
            DISPLAY "En cobol existen las tablas y tablas internas. "-
            "Estas ultimas no se pueden modificar. Las tablas se "-
            "pueden anidar."
            DISPLAY "Voy a utilizar el ejercicio de dificultad extra "-
            "como ejemplo de las operaciones".

      *DIFICULTAD EXTRA
       MENU.
            DISPLAY SPACES
            DISPLAY "-----MENU-----"
            DISPLAY "1 - A�adir"
            DISPLAY "2 - Modificar"
            DISPLAY "3 - Eliminar"
            DISPLAY "4 - Mostrar agenda"
            DISPLAY "5 - Buscar contacto"
            DISPLAY SPACES.
            DISPLAY "0 - SALIR"
            DISPLAY SPACES.

            DISPLAY "Selecciona una opcion:"
            ACCEPT OPCIONES-MENU.

            EVALUATE TRUE

                 WHEN ALTA
                   IF CONTADOR = 0
      *La tabla empieza por 1 y no por 0 como en otros lenguajes
                       ADD 1 TO CONTADOR
                   ELSE
                       MOVE CONTADOR-AUX TO CONTADOR
                   END-IF
                   PERFORM A�ADIR

                 WHEN ACTUALIZAR
                  IF CONTADOR = 0
                       DISPLAY "No hay contactos en la agenda"
                  ELSE
                       PERFORM MODIFICAR
                  END-IF

                 WHEN QUITAR
                   IF CONTADOR = 0
                       DISPLAY "No hay contactos en la agenda"
                       PERFORM VOLVER-MENU
                   ELSE
                       PERFORM ELIMINAR

                 WHEN MUESTRA
                   IF CONTADOR = 0
                       DISPLAY "No hay contactos en la agenda"
                       PERFORM VOLVER-MENU
                   ELSE
                       PERFORM MOSTRAR
                   END-IF

                 WHEN BUSCA
                   IF CONTADOR = 0
                       DISPLAY "No hay contactos en la agenda"
                       PERFORM VOLVER-MENU
                   ELSE
                       PERFORM BUSCAR
                   END-IF

                 WHEN SALE
                   DISPLAY "Saliendo..."
                   PERFORM SALIR

                 WHEN OTHER
                   DISPLAY "Opcion invalida"
                   PERFORM VOLVER-MENU

             END-EVALUATE.

      *INSERCCION
       A�ADIR.
           IF CONTADOR < 25
               DISPLAY "Introduce el nombre:"
               ACCEPT NOMBRE(CONTADOR)
               DISPLAY "Introduce su numero:"
               ACCEPT NUMERO(CONTADOR)
               DISPLAY SPACES
               DISPLAY "Contacto a�adido"
               ADD 1 TO CONTADOR-AUX
           ELSE
               DISPLAY "No se puede a�adir contacto, agenda llena"
           END-IF
           PERFORM VOLVER-MENU.

       MOSTRAR.
           MOVE 1 TO CONTADOR
           DISPLAY SPACES
           DISPLAY "LOS CONTACTOS DE TU AGENDA SON:"
           PERFORM UNTIL CONTADOR = CONTADOR-AUX
               DISPLAY AGENDA(CONTADOR)
               ADD 1 TO CONTADOR
           END-PERFORM.
           DISPLAY SPACES
           PERFORM VOLVER-MENU.


      *BUSQUEDA
       BUSCAR.
           DISPLAY "Dime el nombre del contacto a buscar:"
           ACCEPT NOMBRE-AUX.
           SET INDICE TO 1
           SEARCH AGENDA
               AT END DISPLAY "Contacto no encontrado"
                      PERFORM VOLVER-MENU
               WHEN NOMBRE(INDICE) = NOMBRE-AUX
                    DISPLAY "El numero de "NOMBRE-AUX"es "NUMERO(INDICE)
                    PERFORM VOLVER-MENU
           END-SEARCH.


      *ACTUALIZACION
       MODIFICAR.
           DISPLAY "Dime el nombre del contacto a modificar:"
           ACCEPT NOMBRE-AUX.
           SET INDICE TO 1
           SEARCH AGENDA
               AT END DISPLAY "Contacto no encontrado"
                      PERFORM VOLVER-MENU
               WHEN NOMBRE(INDICE) = NOMBRE-AUX
                    DISPLAY "Que quieres cambiar?"
                    DISPLAY "1-Nombre"
                    DISPLAY "2-Numero"
                    ACCEPT OPCION
                    IF OPCION = 1
                        DISPLAY "Dime el nuevo nombre:"
                        ACCEPT NOMBRE-NUEVO
                        MOVE NOMBRE-NUEVO TO NOMBRE(INDICE)
                        DISPLAY "Nombre del contacto modificado"
                    ELSE
                        IF OPCION = 2
                           DISPLAY "Dime el nuevo numero:"
                           ACCEPT NUMERO-NUEVO
                           MOVE NUMERO-NUEVO TO NUMERO(INDICE)
                           DISPLAY "Numero del contacto modificado"
                        ELSE
                           DISPLAY "Opcion invalida"
                        END-IF
                    END-IF
                    DISPLAY SPACES
                    PERFORM VOLVER-MENU
           END-SEARCH.

      *ELIMINACION
       ELIMINAR.
           DISPLAY "Dime el nombre del contacto a borrar:"
           ACCEPT NOMBRE-AUX.
           SET INDICE TO 1
           SEARCH AGENDA
               AT END DISPLAY "Contacto no encontrado"
                      PERFORM VOLVER-MENU
               WHEN NOMBRE(INDICE) = NOMBRE-AUX
      *En COBOL no se eliminan los datos, se mueven los datos m�s bajos de la tabla de ASCII
                    MOVE LOW-VALUES TO AGENDA(INDICE)
                    DISPLAY "Contacto borrado"
                    PERFORM VOLVER-MENU
           END-SEARCH.

       VOLVER-MENU.
           DISPLAY "Volviendo al menu"
           PERFORM MENU.

       SALIR.
           STOP RUN.

       END PROGRAM RETO-03.
