program VALOR_REFERENCIA
    implicit none

    integer :: a,aa,b,bb

    !En Fortran las variables se asignan por defecto por "referencia" no hay asignación por "valor", sin embargo en las funciones
    !si es posible pasar argumentos por valor.

    a=5
    aa=10

    call ejemplo_x_referencia(a,aa) !Se llama a la función ejemplo_x_referencia

    print*,"Los valores de a y aa se modificaron en la función: a=",a,"y aa=",aa

    call ejemplo_x_valor (a,aa) !Se llama a la función ejemplo_x_valor

    print*,"Los valores de a y aa no se modificaron en la función: a=",a,"y aa=",aa

    !DIFICULTAD EXTRA
    print*,"************************************************"
    print*,"SUBRUTINAS CON ARGUMENTOS POR VALOR Y REFERENCIA"
    print*,"************************************************"
    print*,""
    b=10
    bb=20
    a=30
    aa=40
    print*,"Inicialmente el valor de a es:",a
    print*,"Inicialmente el valor de aa es:",aa
    print*,"Inicialmente el valor de b es:",b
    print*,"Inicialmente el valor de bb es:",bb
    print*,""

    call extra_x_referencia(a,aa) !Se llama a la función ejemplo_x_referencia

    print*,"Los valores de a y aa se intercambiaron en la subrutina: a=",a,"y aa=",aa

    call extra_x_valor (b,bb) !Se llama a la función ejemplo_x_valor

    print*,"Los valores de b y bb no se intercambiaron en la subrutina: b=",b,"y bb=",bb

    contains
    subroutine ejemplo_x_referencia(x1,x2)
        integer , intent(inout) :: x1,x2
        integer :: x3
        x3=5
        x1=x3*5
        x2=x3*10        
    end subroutine ejemplo_x_referencia

    subroutine ejemplo_x_valor(x4,x5)
        integer, value :: x4,x5 !Se agrega la sentencia value para simular la asignación de las variables por "valor"
        integer :: x6
        x6=5
        x4=x6*50
        x5=x6*100        
    end subroutine ejemplo_x_valor

    subroutine extra_x_referencia(x7,x8)
        integer , intent(inout) :: x7,x8
        integer :: x9
        x9=x7
        x7=x8
        x8=x9        
    end subroutine extra_x_referencia

    subroutine extra_x_valor(x10,x11)
        integer, value :: x10,x11 !Se agrega la sentencia value para simular la asignación de las variables por "valor"
        integer :: x12
        x12=x10
        x10=x11
        x11=x12        
    end subroutine extra_x_valor
    
end program VALOR_REFERENCIA