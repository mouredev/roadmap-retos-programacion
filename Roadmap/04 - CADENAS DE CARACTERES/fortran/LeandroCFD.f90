program CHARACTER
    implicit none

    integer :: n,n1,n2,n3=0,n4=0,i
    character (len=30):: texto,texto1,texto2,texto5="",texto6=""
    character (len=10):: texto3,texto4
    character :: letra

    texto1="Hola"
    texto2=" DeviDec"

    !OPERACIONES CON CADENAS DE CARACTERES EN FORTRAN
    !Concatenación
    texto=trim(texto1)//trim(texto2) !trim elimina los espacios al final de la cadena
    print*,texto

    !Longitud
    n=len(texto) !Longitud de la cadena "texto"
    print*,"La longitud de texto es: ",n
    n=len_trim(texto) !Longitud de la cadena "texto" sin espacios en blanco
    print*,"La longitud de texto sin espacios en blanco es: ",n

    !Partes de cadenas
    texto=texto2(:4) !"texto" será lo que hay en la posición 1 hasta la 4 de la cadena "texto2"
    print*,texto
    texto=texto2(4:8) !"texto" será lo que hay en la posición 4 hasta la 8 de la cadena "texto2"
    print*,texto

    !Posición de cadena de caracteres
    n=index(texto2,'Dec') !La función index busca la posición de la cadena "Dec" en la cadena "texto2"
    print*,"La posición de 'Dec' en texto2 es: ",n

    !Posición de cualquier caracter dentro de una cadena
    n=scan(texto2, 'Hijo') !La función scan busca la posición de cualquier caracter de la cadena "Hijo" en "texto2"
    print*,"La posición de algún caracter de 'Hijo' en texto2 es: ",n !En este caso la letra i de "Hijo" se encuentra en la 
    !posición 5 de la cadena "texto2"

    !Conversión de tipos
    write(texto,'(I10)') n !Convierte un número entero en una cadena
    print*,texto
    texto2="9"
    read(texto2,'(I1)') n !Convierte una cadena a número entero
    print*,n

    !Repetación
    texto=repeat(trim(texto1),5)
    print*,texto

    !Reemplazo
    texto(5:)=" DeviDec" !Se reemplazan los caracteres de "texto" desde la posición 5 hasta el final por " DeviDec"
    print*,texto

    !Verificación
    n=verify(texto, "Hola DeviFlow") !La función devuelve la posición del primer carácter en "texto" que no está en "Hola DeviFlow"
    print*,n !El unico caracter que esta en "texto" y que no esta en "Hola DeviFlow" es la c, que se encuentra en la posición 12

    !Eliminación de espacios
    texto1="                Hola"
    texto=adjustl(texto1) !La función adjustl elimina todos los espacios en blanco de la izquierda de la cadena
    print*,texto1
    print*,texto
    texto3="Hola      "
    texto4=" Devidec"
    texto=texto3//texto4
    print*,"Sin la función adjustr: ",texto
    texto=adjustr(texto3)//texto4 !La función adjustr elimina todos los espacios en blanco de la derecha de la cadena
    print*,"Con la función adjustr: ",texto
    texto=trim(texto3)//trim(texto4) !La función trim elimina todos los espacios en blanco de la cadena
    print*,"Con la función trim: ",texto

    !DIFICULTAD EXTRA
    print*,"***********************************************************"
    print*,"PROGRAMA DE DETECCIÓN DE PALÍNDROMOS, ANAGRAMAS Y ISOGRAMAS"
    print*,"***********************************************************"
    print*,""
    print*,"Ingrese la primera palabra en minusculas: "
    read*,texto1
    print*,"Ingrese la segunda palabra en minusculas: "
    read*,texto2
    print*,""
    n1=len_trim(texto1) !Se determina la longitud de la cadena de texto
    n2=len_trim(texto2)

    do i=1,n1
        texto5(i:i)=texto1(n1+1-i:n1+1-i) !Se escribe la cadena al reves
        letra=texto1(i:i) !Se guarda una letra de texto1
        n=scan(texto1(i+1:),letra) !Se revisa si la letra esta en otra parte de la cadena
        if (n/=0) then
            n3=n3+1  !Si la palabra texto1 NO es un anagrama n3/=0                      
        end if
    end do
    do i=1,n2
        texto6(i:i)=texto2(n2+1-i:n2+1-i) !Se realiza lo mismo para la cadena texto2
        letra=texto2(i:i)
        n=scan(texto2(i+1:),letra)
        if (n/=0) then
            n4=n4+1                        
        end if
    end do

    !PALÍNDROMO
    if (texto5==texto1 .and. texto6==texto2) then
        print*,trim(texto1),": Es un palíndromo"
        print*,trim(texto2),": Es un palíndromo"
    else if (texto5==texto1) then
        print*,trim(texto1),": Es un palíndromo"
        print*,trim(texto2),": No es un palíndromo"
    else if (texto6==texto2) then
        print*,trim(texto1),": No es un palíndromo"
        print*,trim(texto2),": Es un palíndromo"
    else
        print*,trim(texto1),": No es un palíndromo"
        print*,trim(texto2),": No es un palíndromo"
    end if

    !ANAGRAMA
    n=verify(texto1,texto2) !Se verifica si existe un caracter diferente entre texto1 y texto2

    if (n==0) then
        print*,trim(texto1),": es un anagrama de ",trim(texto2)
    else 
        print*,trim(texto1),": No es un anagrama de ",trim(texto2)        
    end if

    !ISOGRAMA
    if (n3==0 .and. n4==0) then
        print*,trim(texto1),": es un isograma"
        print*,trim(texto2),": es un isograma"
    else if (n3==0) then
        print*,trim(texto1),": es un isograma"
        print*,trim(texto2),": No es un isograma"
    else if (n4==0) then
        print*,trim(texto1),": No es un isograma"
        print*,trim(texto2),": es un isograma"
    else 
        print*,trim(texto1),": No es un isograma" 
        print*,trim(texto2),": No es un isograma"         
    end if
  
end program CHARACTER