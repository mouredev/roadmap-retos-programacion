program FUNCIONES
    implicit none

    !Se declaran las variables a utilizar en el programa
    integer   :: i,ia,ib,ic
    real      :: r,ra,rb,rc
    character (len=50):: t,ta,tb

    print*,''
    print*,'*********************'
    print*,'FUNCIONES INTRINSECAS'
    print*,'*********************'
    print*,''
    
    !En Fortran existen funciones intrinsecas y funciones construidas por el usuario.
    !FUNCIONES INTRINSECAS
    i=abs(-1)  !Función abs, calcula el valor absoluto de una número, esta función admite variables de tipo integer, real y complex
    r=sqrt(40.1) !Función sqrt, calcula la raiz cuadrada de un valor.
    ia=int(r) !Función int, calcula parte entera de un número real.
    ra=fraction(r) !Función fraction, calcula la parte fraccional de un número real.
    rb=log(5.1) !Función log, calcula el logaritmo natural (neperiano) de un número.
    print*,i,r,ia,ra,rb

    print*,''
    print*,'*********************'
    print*,'FUNCIONES POR USUARIO'
    print*,'*********************'
    print*,''
    
    !Las funciones construidas por el usuario se deben llamar antes de declararlas
    t=Primera_funcion() !Llamado de la Primera función
    ib=Segunda_funcion(i) !Llamado de la Segunda función
    r=Tercera_funcion(ra,rb)
    print*,r
    ra=Cuarta_funcion(r,rb)
    print*,ra
    rc=Quinta_funcion(ra,r)
    print*,rc,r !En este caso el valor de r fue modificado dentro de la función.
    rc=Sexta_funcion(r,ra)
    print*,rc,ra
    ic=factorial(ia)
    print*,"El factorial de ",ia, "es:",ic


    print*,''
    print*,'**********'
    print*,'SUBRUTINAS'
    print*,'**********'
    print*,''

    !Las subrutinas se deben llamar con la sentencia call
    call Primera_subrutina(rc,ra)

    !Tanto las funciones como las subrutinas pueden ser internas (dentro del programa principal, como en este caso) o pueden
    !ser externas, en el momento que sean externas estas deben compilarse al mismo tiempo con el programa principal.

    print*,''
    print*,'****************'
    print*,'DIFICULTAD EXTRA'
    print*,'****************'
    print*,''
    ta="Multiplo de 3"
    tb="Multiplo de 5"
    i=multiplos(ta,tb)
    print*,"El número de números entre 1 y 100 que no son multiplos ni 3 ni de 5 son:",i
    
    !FUNCIONES CONSTRUIDAS POR EL USUARIO
    !Las funciones en Fortran se deben definir de la siguiente manera.
    contains  !Se debe utilizar la sentencia "Contains" para separar una función o una subrutina del programa principal.
    !Esto se debe realizar al final del programa.
        character function Primera_funcion () !Función de tipo character que no tiene argumentos.
            Primera_funcion="H"
            print*,"Esta función retorna la letra 'H'"
        end function Primera_funcion

        integer function Segunda_funcion (x)  !Función de tipo integer que tiene un argumento pero no retorno.
            integer,intent(in) :: x  !Se declara una variable de tipo integer (argumento de la función), la cual se puede utilizar
            !dentro de la función pero no se puede modificar.
            Segunda_funcion=x
            print*,"Esta función retorna el número x:",Segunda_funcion
        end function Segunda_funcion

        function Tercera_funcion (xa,xb) !Función que no se le asigna ningún tipo y que tiene dos argumentos y un retorno.
            real, intent(in) :: xa,xb
            real :: Tercera_funcion
            Tercera_funcion=xa+xb          
        end function Tercera_funcion

        function Cuarta_funcion(xc,xd) result(re) !Si se desea que el retorno tenga otro nombre diferente al de la función, se
            !se utiliza la sentencia result.
            real, intent(in) :: xc,xd
            real :: re           
            re=xc+xd             
        end function Cuarta_funcion

        function Quinta_funcion(xe,xf) result(re1)
            real, intent(in) :: xe
            real, intent(inout) :: xf  !Se declara una variable de tipo real (argumento de la función), la cual se puede utilizar 
            !dentro de la función, se puede modificar y puede ser asimilada como salida de la función.
            real :: re1
            xf=5.0           
            re1=xe+xf        
        end function Quinta_funcion

        function Sexta_funcion(xg,xh) result(re2)
            real, intent(in) :: xg
            real, intent(out) :: xh  !Se declara una variable de tipo real (argumento de la función), la cual se puede utilizar 
            !dentro de la función pero el valor con el que venia no se tiene en cuenta, se puede modificar y puede ser asimilada
            !como salida de la función.
            real :: re2
            xh=6.1
            re2=xg+xh        
        end function Sexta_funcion

        recursive function factorial(n) result(re3) !Se pueden crear funciones recursivas, es decir que se llaman a si mismas 
        !utilizando la sentencia recursive, en esta función se calcula el factorial de un variable de tipo integer.
            integer, intent(in) :: n
            integer :: re3
            if(n==0)then
                re3=1
            else
                re3=n*factorial(n-1)
            end if
        end function factorial

        function multiplos(t1,t2) result(num)
            character (len=50), intent(in) :: t1,t2
            integer :: num,n
            num=0
            do  n= 1,100
                if (mod(n,3)==0 .and. mod(n,5)==0) then
                    print*,n,trim(t1)//" y "//trim(t2)
                else if (mod(n,3)==0) then
                    print*,n,t1
                else if (mod(n,5)==0) then
                    print*,n,t2
                else
                    print*,n
                    num=num+1                   
                end if                
            end do
        end function multiplos

        !SUBRUTINAS
        !Fortran permite utilizar subrutinas. La sintaxis es la siguiente. Las subrutinas no necesariamente deben devolver un valor
        !simplemente pueden hacer un procedimiento sin ningún retorno.
        subroutine Primera_subrutina(xi,xj)
            real, intent(in) :: xi
            real, intent(out) ::  xj
            print*,"Esta subrutina solo imprime un mensaje en consola mostrando los valores de sus argumentos:",xi,xj
        end subroutine Primera_subrutina
        
end program FUNCIONES