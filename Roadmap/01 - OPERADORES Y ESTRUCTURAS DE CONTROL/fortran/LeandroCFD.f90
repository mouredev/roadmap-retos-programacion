program OPERADORES_ESTRUCTURAS
    implicit none
    
    !Se declaran las variables a utilizar en el programa
    integer   :: a,aa,ab 
    real      :: b,ba,bb
    complex   :: c,ca,cb
    logical   :: d,da,db
    character (len=60):: e,ea,eb,ec

    !El operador más basico de Fortran es el operador de asignación de valor, tiene la siguiente sintaxis.
    a=1
    b=2.1
    c=(1,2)
    d=.true.
    e='Esto es una prueba'
    print*,a,b,c,d,e

    !OPERACIONES ARITMÉTICAS
    !Fortran tiene operadores aritmeticos de adicción, sustracción, multiplicación, división, potenciación y cambio de signo.
    !Las operaciones aritmeticas solo son permitidas para variables de tipo integer, real y complex
    print*,''
    print*,'***********************'
    print*,'OPERACIONES ARITMETICAS'
    print*,'***********************'
    !Operaciones aritmeticas entre numeros enteros
    print*,''
    print*,'1)Operaciones numeros enteros'
    aa=2;ab=5
    print*,'Entero aa es igual a:',aa,'Entero ab es igual a:',ab
    a=aa+ab !Operador aritmetico de adicción
    print*,'La suma de aa y ab es igual a:',a
    a=aa-ab !Operador aritmetico de sustracción
    print*,'La resta de aa y ab es igual a:',a
    a=aa*ab !Operador aritmetico de multiplicación
    print*,'La multiplicacion de aa y ab es igual a:',a
    a=ab/aa !Operador aritmetico de división
    print*,'La division de aa y ab es igual a:',a
    a=aa**ab !Operador arimetico de potenciación
    print*,'La potenciacion de aa y ab es igual a:',a
    a=-a    !Operador arimetico de cambio de signo
    print*,'El cambio de signo de a es igual a:',a

    !Operaciones aritmeticas entre numeros reales
    print*,''
    print*,'2)Operaciones numeros reales'
    ba=4.3;bb=3.1
    print*,'Entero ba es igual a:',ba,'Entero bb es igual a:',bb
    b=ba+bb !Operador aritmetico de adicción
    print*,'La suma de ba y bb es igual a:',b
    b=ba-bb !Operador aritmetico de sustracción
    print*,'La resta de ba y bb es igual a:',b
    b=ba*bb !Operador aritmetico de multiplicación
    print*,'La multiplicacion de ba y bb es igual a:',b
    b=ba/bb !Operador aritmetico de división
    print*,'La division de ba y bb es igual a:',b
    b=ba**bb !Operador arimetico de potenciación
    print*,'La potenciacion de ba y bb es igual a:',b
    b=-b    !Operador arimetico de cambio de signo
    print*,'El cambio de signo de b es igual a:',b

    !Operaciones aritmeticas entre numeros complejos
    print*,''
    print*,'3)Operaciones numeros complejos'
    ca=(4.3,1);cb=(3.1,2)
    print*,'Entero ca es igual a:',ca,'Entero cb es igual a:',cb
    c=ca+cb !Operador aritmetico de adicción
    print*,'La suma de ca y cb es igual a:',c
    c=ca-cb !Operador aritmetico de sustracción
    print*,'La resta de ca y cb es igual a:',c
    c=ca*cb !Operador aritmetico de multiplicación
    print*,'La multiplicacion de ca y cb es igual a:',c
    c=ca/cb !Operador aritmetico de división
    print*,'La division de ca y cb es igual a:',c
    c=ca**cb !Operador arimetico de potenciación
    print*,'La potenciacion de ca y cb es igual a:',c
    c=-c    !Operador arimetico de cambio de signo
    print*,'El cambio de signo de c es igual a:',c

    !Existe la posibilidad de convertir tipos de variables en otros.
    b=a !Se convierte un número entero (a) en un número real (b), aunque el caso contrario es permitido NO es aconsejable.
    print*,b
    c=b !Se convierte un número real (b) en un número complejo (c)
    print*,c

    !Las operaciones aritmeticas en Fortran tienen un orden de solución:
    !1) Operaciones entre parentesis
    !2) Operaciones de potenciación
    !3) Operaciones de multiplicación y división, yendo de izquierda a derecha
    !4) Operaciones de cambio de signo
    !5) Operaciones de adicción y sustracción, yendo de izquierda a derecha

    !OPERACIONES DE COMPARACIÓN
    !Las operaciones de comparación en Fortran tienen dos sintaxis, una para las versiones 90 o posteriores y una para la versión 77
    !Las expresiones a comparar deben ser de tipo numerico (integer, real o complex) y el resultado es de tipo logical.
    print*,''
    print*,'**************************'
    print*,'OPERACIONES DE COMPARACION'
    print*,'**************************'
    print*,''
    d=ab==aa !Operación de comparación 'es igual a', sintaxis Fortran 90
    d=ab.eq.aa !Operación de comparación 'es igual a', sintaxis Fortran 77
    print*,'ab es igual a aa:',d
    d=ab/=aa !Operación de comparación 'no es igual a', sintaxis Fortran 90
    d=ab.ne.aa !Operación de comparación 'no es igual a', sintaxis Fortran 77
    print*,'ab NO es igual a aa:',d
    d=ab>aa !Operación de comparación 'es estrictamente mayor a', sintaxis Fortran 90
    d=ab.gt.aa !Operación de comparación 'es estrictamente mayor a', sintaxis Fortran 77
    print*,'ab es estrictamente mayor a aa:',d
    d=ab>=aa !Operación de comparación 'es mayor o igual a', sintaxis Fortran 90
    d=ab.ge.aa !Operación de comparación 'es mayor o igual a', sintaxis Fortran 77
    print*,'ab es mayor o igual a aa:',d
    d=ab<aa !Operación de comparación 'es estrictamente menor a', sintaxis Fortran 90
    d=ab.lt.aa !Operación de comparación 'es estrictamente menor a', sintaxis Fortran 77
    print*,'ab es estrictamente menor a aa:',d
    d=ab<=aa !Operación de comparación 'es menor o igual a', sintaxis Fortran 90
    d=ab.le.aa !Operación de comparación 'es menor o igual a', sintaxis Fortran 77
    print*,'ab es menor o igual a aa:',d

    !En este punto aprendí a representar acentos desde la terminal (Se debe cambiar la pagina de codigos a UTF-8, se puede desde 
    !vscode o desde la terminal ejecutando el comando "chcp 65001")

    !OPERACIONES LÓGICAS
    !Las operaciones lógicas solo admiten expresiones de tipo logical y el resultado también es de tipo logical.
    print*,''
    print*,'*******************'
    print*,'OPERACIONES LÓGICAS'
    print*,'*******************'
    print*,''
    d=.false.
    db=.true.
    print*,'d es igual a:',d,'y db es igual a:',db
    da=.not.d !Operador de negación, cambia el valor de la expresión lógica a su opuesto, necesita de una sola expresión.
    print*,'La negacion de d es igual a:',da
    da=d.and.db !Operador de conjunción (y), verdadero si ambas expresiones son verdaderas 
    print*,'d y db es igual a:',da
    da=d.or.db !Operador de disyunción inclusiva (o), verdadero si una de las expresiones es verdadera
    print*,'d o db es igual a:',da
    da=d.eqv.db !Operador de equivalencia (eqv), verdadero si ambas expresiones tienen el mismo valor 
    print*,'d eqv db es igual a:',da
    da=d.neqv.db !Operador de no equivalencia o de disyunción inclusiva (neqv o xor), verdadero si ambas expresiones no tienen el
    !mismo valor 
    print*,'d neqv db es igual a:',da

    !OPERADORES CON CARACTERES
    !Fortran tiene diferentes operaciones con caracteres como los operadores binarios de concatenación y comparación
    print*,''
    print*,'**************************'
    print*,'OPERACIONES CON CARACTERES'
    print*,'**************************'
    print*,''
    ea='   Bogotá,   '
    eb=' 2600 metros más cerca de las estrellas'
    e=adjustl(ea) !Operador que permite eliminar todos los espacios al inicio de la cadena de caracteres
    print*,'Comparación de el operador adjustl: sin adjustl:',ea,'con adjustl:',e
    e=adjustr(ea) !Operador que permite eliminar todos los espacios al final de la cadena de caracteres
    print*,'Comparación de el operador adjustr: sin adjustr:',ea,' con adjustr:',e
    ec=trim(ea) !Operador que permite eliminar todos los espacios al final de la cadena de caracteres de forma temporal
    print*,'Comparación de el operador trim: con trim:',trim(ea),' sin trim:',ea
    e=trim(ea)//trim(eb) !Operador de concatenación
    print*,e
    e=adjustl(trim(ea)//trim(eb)) !Combinación de operadores
    print*,e
    e=ea(5:8) !Parte de candena de caracteres, en este caso "e" queda con los caracteres desde la posición 5 hasta la 8 de "ea"
    print*,e
    e=ea(:6)  !Parte de candena de caracteres, en este caso "e" queda con los caracteres desde el inicio hasta la posición 6 de ea
    print*,e
    e=ea(6:)  !Parte de candena de caracteres, en este caso "e" queda con los caracteres desde 6 hasta el final de "ea"
    print*,e

    !Fortran no tiene operadores de pertenencia como "in" o de identidad como "is".

    !ESTRUCTURAS DE CONTROL
    !CONDICIONALES
    !Fortran permite los condicionales con la función IF, la sintaxis es la siguiente.
    print*,''
    print*,'*************'
    print*,'CONDICIONALES'
    print*,'*************'
    print*,''
    if (ba>bb) aa=10  !Es posible utilizar condicionales en una sola linea de codigo si las instrucciones son sencillas.
    print*,"Resultado condicional una sola linea de codigo:",aa

    if (ba>bb) then   !O en varias lineas de codigo si son varias instrucciones.
        aa=a*5
        print*,"Resultado condicional varias lineas de codigo:",aa        
    end if

    if (bb>ba) then
        aa=a/2
        print*,"Este resultado se imprimira si bb es mayor que ba:",aa
    else              !La instrucción else permite ejecutar instrucciones si la condición del if no se cumple.
        aa=a*2
        print*,"Este resultado se imprimira si bb es menor que ba:",aa        
    end if

    if (bb>ba) then
        aa=a**2
    else if (bb<ba) then  !La instrucción else if permite adicionar un condicional si el primer if no se cumple
        aa=a+ab
        print*,"Este resultado se imprimira si bb es menor que ba (else if):",aa
    else              
        aa=a*2
        print*,"Este resultado se imprimira si bb es igual que ba:",aa   
    end if

    Prueba : if (ba>bb) then   !Se le puede agregar un nombre al if para dar mayor claridad, en este caso "Prueba"
        aa=a*5
        print*,"Resultado condicional varias lineas de codigo:",aa        
    end if Prueba

    !BUCLES O CICLOS
    !Fortran permite diferentes tipos de bucles con la función DO, permite bucles infinitos, bucles while y bucles con 
    !numero finito de iteraciones.
    print*,''
    print*,'******'
    print*,'BUCLES'
    print*,'******'
    print*,''
    !BUCLE INFINITO
    do        
        print*,"Bucle infinito do"
        exit  !Se debe utilizar la instrucción exit para detener el ciclo, exit pasara a la siguiente instrucción luego del end do
    end do
    aa=9    
    bucle : do !También es posible darle un nombre al bucle como un identificador
        !Se llega aquí con la instrucción cycle bucle
        print*,"Bucle infinito do con nombre 'bucle'"
        bucle_dos : do !Es posible anidar bucles infinitos
            !Se llega aquí con la instrucción cycle
            aa=aa+1
            print*,"Bucle infinito do con nombre 'bucle_dos'"
            if (aa==10) cycle !La instrucción cycle obliga al programa a regresar al inicio de las instrucciones del bucle
            if (aa==11) cycle bucle !Cycle se puede asosciar al nombre de un bucle
            if (aa==12) exit bucle_dos !Exit se puede asosciar al nombre de un bucle
            if (aa==13) exit bucle
        end do bucle_dos
        print*,"Se llega aquí con la instrucción exit bucle_dos"
    end do bucle
    print*,"Se llega aquí con la instrucción exit bucle"

    !BUCLE DO WHILE
    do while (aa>10) !Este ciclo continua hasta que aa sea menor o igual a 10
        print*,"Bucle do while, valor de aa es igual a:",aa
        aa=aa-1
    end do

    !BUCLE CON NÚMERO FIJO DE ITERACIONES
    aa=0
    do a = 1,6,2 !Este bucle va desde 1 hasta 6 con un incremento de 2, por lo que solo seran 3 iteraciones.
        aa=aa+1
        print*,"Iteración número:",aa,"El valor de a es igual a:",a
    end do
    print*,"Segundo bucle con número fijo de iteraciones"
    aa=0
    do a = 1,6 !Si no se le asigna ningún incremento este será de 1.
        aa=aa+1
        print*,"Iteración número:",aa,"El valor de a es igual a:",a
    end do

    !ESTRUCTURA CASE
    !La estructura de control case permite seleccionar un bloque de instrucciones a ser ejecutada, la sintaxis es la siguiente. 
    print*,''
    print*,'***************'
    print*,'ESTRUCTURA CASE'
    print*,'***************'
    print*,''
    
    print*,"Digita un valor del 1 hasta el 10:"
    read*,aa
    select case (aa) !La variable entre parentesis puede ser de tipo integer, logical o character
        case (1) 
            print*,"Seleccionaste el valor 1"
        case (2:5) 
            print*,"Seleccionaste un valor del 2 al 5"
        case (6:9) 
            print*,"Seleccionaste un valor del 6 al 9"
        case (10) 
            print*,"Seleccionaste el valor 10"
    end select

    print*,''
    print*,'****************'
    print*,'DIFICULTAD EXTRA'
    print*,'****************'
    print*,''
    
    do a = 10, 55
        aa=mod(a,2)   !La función mod devuelve el resto de una división con resto, si mod es cero la división es exacta.
        Impresion : if (aa==0 .or. a==55) then
            aa=mod(a,3)
            if (aa==0) exit Impresion
            if (a==16) exit Impresion
            print*,a            
        end if Impresion  
    end do

end program OPERADORES_ESTRUCTURAS