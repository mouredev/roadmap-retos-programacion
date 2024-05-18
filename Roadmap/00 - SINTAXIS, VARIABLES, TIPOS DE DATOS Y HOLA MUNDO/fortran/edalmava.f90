program helloworld
    ! Este es un comentario de una línea
    ! El caracter ! indica el inicio de un comentario.
    ! El sitio oficial del lenguaje es https://fortran-lang.org/
    ! El compilador usado es el GNU Fortran Compiler (gfortran) 
    ! Variables en Fortran
    ! Hay 5 tipos de datos internos: integer, real, complex, character y logical
    ! Los nombres de variables deben comenzar con una letra y solamente se pueden utilizar letras, dígitos y _
    ! No se diferencia entre mayúscula y minúscula    
    ! Antes que se use una variable se debe declarar
    ! Fortran es un lenguaje de tipado estático para declarar una variable se usa la sintaxis:
    !     <tipo_variable> :: <nombre_variable>
    ! Una vez declarada una variable se le puede asignar y reasignar un valor usando el operador de asignación =
    ! Declaración de variables
    ! Variables de datos tipo integer (entera)
    implicit none        ! Esto significa que las variables serán implícitamente declaradas
    integer :: a         ! Declaración de la variable a y b
    INTEGER :: b         ! No se diferencia entre mayúscula y minúscula - palabras reservadas
    ! Variables de datos tipo real (punto flotante) 
    real :: radio, pi, area
    ! Variables de datos tipo character (caracter)
    character :: letra
    character(7) :: fortran ! Character strings
    ! Variable de datos complex
    complex :: frecuencia
    ! Variable de datos logical
    logical :: isOK
    ! Asignación de variables
    a = 1; b = 2         ! Asignación de valores a las variables enteras
    print *, a           ! Salida estándar - stdout de la variable a
    print *, b           ! Salida estándar - stdout de la variable b
    ! Asignación de valores a las variables reales
    radio = 1.5              
    pi = 3.1415927
    area = pi * radio ** 2
    print *, 'El área del círculo de radio 1.5 es: ', area
    ! Asignación de valor a la variable complex
    frecuencia = (1.0, -0.5)
    print *, frecuencia
    ! Asignación de valor a la variable logical 
    isOK = .true.        ! Los valores lógicos o booleanos son .true. y .false. 
    print *, isOK
    ! Asignación de valores a las variables character
    letra = 'A'
    fortran = 'Fortran'
    print *, '¡Hola, ', fortran, '!'
end program helloworld