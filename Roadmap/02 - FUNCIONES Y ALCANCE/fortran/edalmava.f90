program funciones
    implicit none
    ! En Fortran las funciones siguen la siguiente sintaxis:
    !     tipo function nombre_funcion (arg1, arg2, argN)
    !         declaracion argumento 1
    !         declaracion argumento 2
    !         ...
    !         declaracion argumento N
    !         
    !         sentencia 1
    !         sentencia 2
    !         ...
    !         sentencia N
    !    end function
    ! Es posible tener funciones con 0 o más argumentos
    ! Las funciones devuelven un valor

    ! Los Procedimientos o Subrutinas retornan varios o ningún valor
    ! La sintaxis de una subrutina es:
    ! subroutine nombre_subrutina (arg1, ..., argN)
    ! inicio
    !     declaración arg1
    !     ...
    !     declaración argN
    !     sentencia1
    !     sentencia2
    !     ...
    !     sentenciaN
    ! fin

    ! Forma de invocar las subrutinas
    integer x, y, numero
    
    call asteriscos(5)

    x = 0; y = 1;

    print *, x, y
    call intercambio(x, y)
    print *, x, y

    ! Uso de funciones intrínsecas o estándar
    print *, 'La raíz cuadrada de 100 es ', SQRT(100.0)
    
    print *, siempreVerdad()
    print *, 'El máximo de 4 y 5 es: ', maximo(4,5)

    ! Llamada a función del ejercicio EXTRA
    numero = imprimirNumeros('Hola', 'Mundo')
    print *, 'Número de veces que fue impreso un número: ', numero

    ! La definición de funciones se debe hacer en una sección contains al final del programa
    contains

    ! Función sin argumentos que siempre retorna el valor lógico verdadero:
    logical function siempreVerdad ()
        siempreVerdad = .true.
    end function

    ! Función que recibe dos enteros y retorna el mayor de los dos:
    integer function maximo (a, b)
        integer a,b
        if (a>b) then
            maximo = a
        else
            maximo = b
        end if
    end function

    integer function imprimirNumeros (cadena1, cadena2)        
        integer i, contar
        character(len = 4) cadena1
        character(len = 5) cadena2

        contar = 0
        do i = 1, 100
            if (MOD(i, 3) == 0 .and. MOD(i, 5) == 0) then
                print *, cadena1 // cadena2
            else if (MOD(i, 3) == 0) then
                print *, cadena1
            else if (MOD(i, 5) == 0) then
                print *, cadena2
            else 
                print *, i
                contar = contar + 1
            end if                
        end do
        imprimirNumeros = contar
    end function

    subroutine asteriscos (n)
        implicit none
        integer n
        integer i
        do i = 1, n
            print *, '*'
        end do
    end subroutine

    subroutine intercambio (a,b)
        implicit none
        integer a,b
        integer temporal
        temporal = a
        a = b
        b = temporal
    end subroutine   
     
end program funciones