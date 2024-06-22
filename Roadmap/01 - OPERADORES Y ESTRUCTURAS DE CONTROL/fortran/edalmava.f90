program operadores
    implicit none        
    integer :: a, b, n, mes
    real :: radio   

    print *, 'Estructuras de Control en Fortran'
    print *, 'Estructuras Alternativas'
    print *, 'Estructura Alternativa Simple (if-then)'
    
    a = 5; b = 10
    if (a < b) then
        print *, a, ' es menor que ', b
    end if

    print *, 'Estructura Alternativa Doble (if-then-else)'

    b = 4
    if (a < b) then
        print *, b, ' es menor que ', a
    else 
        print *, a, ' es mayor que ', b
    end if

    print *, 'Estructura Multialternativa (case)'
    print *, 'Digite el número del mes: '
    read *, mes
    print *, 'El mes digitado tiene '
    select case (mes)
        case (1, 3, 5, 7, 8, 10, 12)
            print *, '31'
        case (4, 6, 9, 11)
            print *, '30'
        case (2)
            print *, '28'
        case default
            print *, 'Mes incorrecto'
    end select
    
    print *, ''
    print *, '***********************'
    print *, 'Estructuras Repetitivas'
    print *, '***********************'
    print *, ''
    print *, 'Estructura desde hasta (do)'
    do n = 1, 10, 2
        print *, n
    end do
    print *, 'Estructura Mientras (do-while)'
    radio = -1
    do while (radio < 0) ! Se solicita el radio hasta que sea positivo
        print *, 'Digite Radio?(Debe ser positivo)'
        read  *, radio
    end do
    
    print *, ''
    print *, '**********'
    print *, 'RETO EXTRA'
    print *, '**********'
    print *, ''
    do n = 10, 55, 1
        if (mod(n, 2) == 0 .and. n /= 16 .and. mod(n, 3) /= 0) then 
            print *, n
        end if
    end do     
end program operadores
