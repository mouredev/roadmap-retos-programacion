       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-03.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES.
           CLASS Decimal IS "0" THRU "9".
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
      * Declaracion de variables para ejemplos
      * Las tablas se pueden anidar
       01  TABLA-SIMPLE OCCURS 10 TIMES.
           02 DATO PIC X(10).

       77  I PIC 99 VALUE ZERO.

      * Declaracion de variables para ejercicio extra
      * Variables para opciones de menu
       01  opcion-menu PIC X VALUE SPACE.
           88 opc-alta VALUE "A" "a".
           88 opc-baja VALUE "B" "b".
           88 opc-consulta VALUE "C" "c".
           88 opc-modificar VALUE "M" "m".
           88 opc-salir VALUE "S" "s".

      * Declaracion de Tabla
       01  agenda OCCURS 100 TIMES DEPENDING ON indice
           INDEXED BY puntero.
           02 ag-indice PIC 99.
           02 nombre PIC X(30).
           02 telefono PIC X(13).

      * Variables simples
       77  contador PIC 99.
       77  indice PIC 99 VALUE ZERO.
       77  id-editar PIC 99.
       77  auxiliar PIC X(13).

      * Variables para selecciones
       01  continuar PIC X VALUE SPACE.
           88 cont-si VALUE "S" "s".
           88 cont-no VALUE "N" "n".

       01  seleccion PIC X VALUE SPACE.
           88 sel-nombre VALUE "N" "n".
           88 sel-telefono VALUE "T" "t".
           88 sel-cancela VALUE "C" "c".

       PROCEDURE DIVISION.
      * La estructura mas parecida a los arrays, listas, diccionarios, etc.
      * son las tablas y se declaran en WORKING-STORAGE

       TABLAS.
      * Carga de tabla
           MOVE "Juan" TO DATO(1).
           MOVE "Paco" TO DATO(2).
           MOVE "Maria" TO DATO(3).
           MOVE "Ana" TO DATO(4).
           MOVE "Jose" TO DATO(5).

      * Iterar la tabla y mostrar los datos en la pantalla
           SET I TO 1
           PERFORM 5 TIMES
               DISPLAY TABLA-SIMPLE(I)
               ADD 1 TO I
           END-PERFORM.

      * Modificar datos
           MOVE "Rocio" TO DATO(2).
           DISPLAY "-- Modificamos el dato de la posicion 2".
           MOVE 1 TO I.
           PERFORM Iterar-tabla 5 TIMES.

      * Eliminar datos
           MOVE LOW-VALUE TO DATO(5).
           DISPLAY "-- Eliminamos el dato de la posicion 5".
           MOVE 1 TO I.
           PERFORM Iterar-tabla 5 TIMES.

           PERFORM EJERCICIO-EXTRA.


       Iterar-tabla.
           DISPLAY DATO(I).
           ADD 1 TO I.

       EJERCICIO-EXTRA.
      * Mostrar el menu de opciones
           DISPLAY "----- MENU AGENDA -----".
           DISPLAY "A - Alta de contacto".
           DISPLAY "B - Baja de contacto".
           DISPLAY "M - Modificacion de contacto".
           DISPLAY "C - Listado de contactos".
           DISPLAY " ".
           DISPLAY "S - Salir de la agenda".
           ACCEPT opcion-menu.
      * Controlador de opciones
           IF opc-alta
               PERFORM Alta-contacto
           ELSE
           IF opc-baja
               PERFORM Baja-contacto
           ELSE
           IF opc-modificar
               PERFORM Modifica-contacto
           ELSE
           IF opc-consulta
               SET I TO 1
               PERFORM Consulta-contacto UNTIL I > indice
               DISPLAY "Presione una tecla para continuar"
               ACCEPT continuar
           ELSE
           IF opc-salir
               DISPLAY "Ha salido de la agenda"
               STOP RUN
           ELSE
               DISPLAY "La opcion seleccionada no es valida".
           PERFORM EJERCICIO-EXTRA.

      * Altas de contacos
       Alta-contacto.
           DISPLAY "--- ALTA DE CONTACTO ---"
           ADD 1 TO indice.
           DISPLAY "Ingrese un nombre:"
           ACCEPT nombre(indice).
           PERFORM Alta-telefono.

       Alta-telefono.
           DISPLAY "Ingrese el telefono (deben ser 13 digitos):"
           ACCEPT telefono(indice).
           IF telefono(indice) IS NOT Decimal
               DISPLAY "El valor ingresado es incorrecto"
               PERFORM Alta-telefono
           ELSE
               MOVE indice TO ag-indice(indice)
               DISPLAY "Se ha guardado el contacto con el ID " indice
               DISPLAY " "
               MOVE SPACE to continuar
               DISPLAY "Desea cargar otro contacto S=SI / N=NO"
               ACCEPT continuar
               IF cont-si
                   PERFORM Alta-contacto.

      * Baja de contactos
       Baja-contacto.
           SET I TO 1.
           PERFORM Consulta-contacto UNTIL I > indice.
           DISPLAY "Seleccione un ID de contaco para eliminar 0=Salir"
           ACCEPT id-editar.
           IF id-editar <> 0
               IF ag-indice(id-editar) <> 0
                   PERFORM Baja-seleccion
               ELSE
                   DISPLAY "El id seleccionado es incorrecto"
                   PERFORM Baja-contacto.

       Baja-seleccion.
           MOVE ZERO TO ag-indice(id-editar).
           MOVE LOW-VALUE TO nombre(id-editar).
           MOVE LOW-VALUE TO telefono(id-editar).
           DISPLAY "Se ha dado de baja al ID: " id-editar.

      * Modificacion de contactos
       Modifica-contacto.
           SET I TO 1.
           PERFORM Consulta-contacto UNTIL I > indice.
           DISPLAY "Seleccione el ID de un contaco para editar 0=Salir"
           ACCEPT id-editar.
           IF id-editar <> 0
               IF ag-indice(id-editar) <> 0
                   PERFORM Modifica-seleccion
               ELSE
                   DISPLAY "El id seleccionado es incorrecto"
                   PERFORM Modifica-contacto.


       Modifica-seleccion.
           IF id-editar <= indice
               DISPLAY "Que va a editar N=Nombre T=Telefono C=Cancelar?"
               ACCEPT seleccion
               IF sel-nombre
                   DISPLAY "Ingrese el nuevo Nombre:"
                   ACCEPT nombre(id-editar)
                   DISPLAY "Se ha modificado el Nombre"
               ELSE
                   IF sel-telefono
                       DISPLAY "Ingrese el nuevo Telefono:"
                       ACCEPT auxiliar
                       IF auxiliar IS Decimal
                           MOVE auxiliar TO telefono(id-editar)
                           DISPLAY "Se ha modificado el telefono"
                       ELSE
                           DISPLAY "El valor ingresado es incorrecto"
                           PERFORM Modifica-seleccion
                   ELSE
                       IF sel-cancela
                           DISPLAY "Accion cancelada"
                       ELSE
                           DISPLAY "Seleccion incorrecta"
                           PERFORM Modifica-seleccion.

      * Listado de contactos
       Consulta-contacto.
           IF ag-indice(I) <> ZERO
               DISPLAY "ID: " ag-indice(I) "-Nombre: " nombre(I)
                       "  -Telefono: " telefono(I).
           ADD 1 TO I.

       END PROGRAM RETO-03.
