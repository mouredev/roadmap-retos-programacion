IDENTIFICATION DIVISION.
PROGRAM-ID. Main.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 NUM-A PIC 9(2) VALUE 10.
01 NUM-B PIC 9(2) VALUE 20.
01 RESULT PIC 9(2).
PROCEDURE DIVISION.
A100-MAIN.
    DISPLAY "Operadores aritméticos y de asignación:"
    COMPUTE RESULT = NUM-A + NUM-B
    DISPLAY "10 + 20 = " RESULT
    COMPUTE RESULT = NUM-A - NUM-B
    DISPLAY "10 - 20 = " RESULT
    COMPUTE RESULT = NUM-A * NUM-B
    DISPLAY "10 * 20 = " RESULT
    COMPUTE RESULT = NUM-B / NUM-A
    DISPLAY "20 / 10 = " RESULT

    DISPLAY "Operadores de comparación:"
    IF NUM-A = NUM-B THEN
        DISPLAY "10 es igual a 20"
    ELSE
        DISPLAY "10 no es igual a 20"
    END-IF
    IF NUM-A < NUM-B THEN
        DISPLAY "10 es menor que 20"
    ELSE
        DISPLAY "10 no es menor que 20"
    END-IF
    IF NUM-A > NUM-B THEN
        DISPLAY "10 es mayor que 20"
    ELSE
        DISPLAY "10 no es mayor que 20"
    END-IF

    DISPLAY "Estructuras de control condicionales e iterativas:"
    PERFORM UNTIL NUM-A > NUM-B
        DISPLAY NUM-A
        ADD 1 TO NUM-A
    END-PERFORM

    STOP RUN.
