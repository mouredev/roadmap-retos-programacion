program RECURSIVIDAD
    implicit none

    integer :: m

    print*,"Digite un número para contar hasta cero"
    read*,m

    call contador(m)

    !DIFICULTAD EXTRA
    print*,"Digite un número para calcular su factorial"
    read*,m

    print*,"El factorial de ",m," es ",factorial(m)

    print*,"Digite la posición de la serie de fibonacci que desea calcular"
    read*,m

    print*,"El número en la posición ",m," de la serie de fibonacci es ",fibonacci(m)

    contains
    recursive subroutine contador(n) !Subrutina recursiva que imprime desde un número hasta cero
        integer, intent(in) :: n
        if(n==0)then
            print*,0
        else
            print*,n
            call contador(n-1)
        end if
    end subroutine contador

    recursive function factorial(n) result(resultado) !Función recursiva que calcula el factorial de un número
        integer , intent(in) :: n
        integer :: resultado
        if(n==0)then
            resultado=1
        else
            resultado=n*factorial(n-1)
        end if
    end function factorial

    recursive function fibonacci(n) result(resultado) !Función recursiva que calcula la serie de fibonacci hasta cierta posición
        integer, intent(in) :: n
        integer (kind=8) :: resultado
        if(n==0)then
            resultado=0
        else if(n==1)then
            resultado=1
        else
            resultado=fibonacci(n-1)+fibonacci(n-2)
        end if
    end function fibonacci
    
end program RECURSIVIDAD
