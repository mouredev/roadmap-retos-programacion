program ARRAYS
    implicit none

    !Fortran permite la creación y manipulación de arreglos unidimensionales (vectores), bidimensionales (matrices) y
    !tridimensionales (grillas). Es importante entender que Fortran al momento de compilar convierte todos los tipos de arreglos a
    !arreglos unidimensionales. En Fortran es posible declarar los arreglos de forma estatica y de forma dinámica.
    !Declaración de arreglos unidimensionales de forma estatica.
    integer, dimension(5) :: vector1  !Declaración de un arreglo unidimensional de tipo integer que tiene dimensión 5.
    integer :: vector5(5) !También es posible declarar un arreglo añadiendo las dimensiones al nombre del arreglo.
    real, dimension(1:3) :: vector2 !Declaración de un arreglo unidimensional de tipo real que tiene dimensión 3 con indices 1 a 3
    character(len=20), dimension(5) :: nombres !Declaración de un arreglo unidimensional de tipo character que tiene dimensión 5 y 
    !cada posición del arreglo tiene una longitud máxima de 20 caracteres.
    complex, dimension(10:15) :: vector3 !Declaración de un arreglo unidimensional de tipo complex, dimensión 5 indices 10 a 15
    logical, dimension(5:8) :: pruebas !!Declaración de un arreglo unidimensional de tipo logical que tiene dimensión 4 con 
    !indices 5 a 8

    !Declaración de arreglos bidimensionales de forma estatica.
    integer, dimension(5,3) :: matriz1  !Declaración de arreglo tipo integer que tiene dimensión 5 (filas) y 3 (columnas).
    real, dimension(1:5,1:3) :: matriz2 !Declaración de arreglo tipo real que tiene dimensión 5 (filas) y 3 (columnas) 
    !con indices 1 a 5 y 1 a 3 respectivamente.
    character(len=20), dimension(2:4,5:7) :: nombres1 !Declaración de arreglo tipo character que tiene dimensión 3 (filas) y 
    !3 (columnas) con indices 2 a 4 y 5 a 7 respectivamente, cada posición del arreglo tiene una longitud máxima de 20 caracteres.
    complex, dimension(1:5,6) :: matriz3 !Declaración de arreglo tipo complex que tiene dimensión 5 (filas) y 6 (columnas) 
    !con indices 1 a 5 y sin asginación de indices para las columnas.
    logical, dimension(2,2:6) :: pruebas1 !!Declaración de arreglo de tipo logical que tiene dimensión 2 (filas) y 5 (columnas) 
    !sin indices para las filas y con indices 2 a 6 para las columnas.

    !Declaración de arreglos tridimensionales de forma estatica.
    integer, dimension(4,3,5) :: tensor1  !Declaración de arreglo tipo integer que tiene dimensión 4 (filas) , 3 (columnas) y 
    !5 (matrices).
    real, dimension(1:10,1:7,1:4) :: tensor2,tensor4,tensor5 !Declaración de arreglo tipo real que tiene dimensión 10 (filas) y
    !7 (columnas) y 4 (matrices) con indices 1 a 10, 1 a 7 y 1 a 4 respectivamente.
    character(len=20), dimension(2:5,5:7,5) :: nombres3 !Declaración de arreglo tipo character que tiene dimensión 4 (filas), 
    !3 (columnas) y 5 (matrices) con indices 2 a 4, 5 a 8 para filas y columnas y sin indices para las matrices, cada posición
    !del arreglo tiene una longitud máxima de 20 caracteres.
    complex, dimension(1:5,6,2:4) :: tensor3 !Declaración de arreglo tipo complex que tiene dimensión 5 (filas), 6 (columnas) y
    !3 (matrices) con indices 1 a 5 y 2 a 4 para filas y matrices y sin asginación de indices para las columnas.
    logical, dimension(2,2:6,4) :: pruebas2 !!Declaración de arreglo de tipo logical que tiene dimensión 2 (filas), 5 (columnas) y
    !4 (matrices) sin indices para las filas y matrices y con indices 2 a 6 para las columnas.

    !En algunas ocasiones no es posible saber apriori el tamaño de un arreglo, por lo tanto, Fortran permite la declaración
    !de arreglos de forma dinámica con la opción allocatable.
    integer,dimension(:),allocatable :: vector4 !Arreglo unidimensional
    real,dimension(:,:),allocatable :: matriz4 !Arreglo bidimensional
    
    !Declaraciones de variables ejercicio extra
    integer :: n,i,j,m
    character (len=100) :: comparacion
    type contacto
        character (len=100) :: nombre
        integer (kind=8):: telefono
        integer :: ID
    end type contacto

    type (contacto), dimension(100) :: agenda 

    !La asignación de valores para los arreglos se puede realizar componente a componente.
    vector1(2)=100 !Se le asigna un valor de 100 a la posición 2 del vector1.
    vector2(3)=15.3 !Se le asigna un valor de 15.3 a la posición 3 del vector2.
    nombres(1)="Lizeth" !Se le asigna la cadena de texto "Lizeth" a la posición 1 del arreglo nombres.
    vector3(13)=(2,5) !Se le asigna un valor de (2,5) a la posición 13 del vector3.
    pruebas(7)=.true. !Se le asigna un valor true a la posición 7 del arreglo pruebas.

    !También es posible asignar un arreglo de manera global de la siguiente manera.
    vector5=(/6,7,8,9,10/) !la asignación se realiza con los delimitadores / / y los valores deben ir separados por coma.
    print*,vector1
    matriz1=reshape([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[5,3]) !Para arreglos multidimensionales se debe utilizar la función 
    !reshape que convierte un arreglo unidimensional en uno multidimnesional, Los valores dentro de los parentesis [] son los
    !valores del arreglo y el segundo parentesis las dimensiones.
    print*,matriz1 !Aunque es una matriz fortran lo imprime como un vector, esto debido a que Fortran solo utiliza arreglos 
    !unidimensionales.
    matriz2=reshape([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[5,3])
    print*,matriz2(1,:) !Es posible imprimir una sola fila.
    print*,matriz2(:,1) !Es posible imprimir una sola columna.
    nombres1="Juan" !Es posible asignar un valor a todos los componentes de un arreglo.
    matriz3(2,:)=(5,3) !Es posible asignar un valor a todos los componentes de una fila en un arreglo.
    pruebas1(:,3)=.false. !Es posible asignar un valor a todos los componentes de una columna en un arreglo.
    tensor1(:,:,3)=100 !Es posible asignar un valor a todos los componentes de la matriz de un arreglo tridimensional.

    !Operaciones aritmeticas
    tensor4=2
    tensor5=5
    tensor2=tensor4*tensor5 !multiplicación elemento a elemento de dos tensores
    tensor2=sqrt(tensor4)

    !Intrucciones de control con arreglos
    where (tensor1==100) nombres3="Valor" !La instrución where permite asignar el valor a el arreglo nombres3 en las posiciones
    !donde tensor1==100.
    pruebas2=.true.
    pruebas=all(pruebas2) !La instrucción all devuelve un .true. si todos los elementos de pruebas2 son .true.
    print*,pruebas
    pruebas2=.false.
    pruebas=any(pruebas2) !La instrucción any devuelve un .true. si almenos un elemento de pruebas2 son .true.
    print*,pruebas
    tensor3=(5,3)

    !Se le asigna el tamaño a los arreglos declarados dinámicamente con la sentencia allocate
    allocate(vector4(vector1(1):10),matriz4(tensor1(1,2,2),3))

    !Se destruye un arreglo con la sentencia deallocate
    deallocate(matriz4)

    !DIFICULTAD EXTRA
    agenda%ID=0
    menu : do i = 1, 100
        print*,"********************************************************"
        print*,"                    MENU PRINCIPAL"
        print*,"********************************************************"
        print*,"********************************************************"
        print*,"BIENVENIDO A TU PROGRAMA DE AGENDA DE CONTACTOS PERSONAL"
        print*,"********************************************************"
        print*,""
        print*,"Digite un numero entre las siguientes opciones: "
        print*,""
        print*,"1. Agregar contacto"
        print*,"2. Eliminar contacto"
        print*,"3. Buscar contacto"
        print*,"4. Actualizar contacto"
        print*,"5. Ver todos los contactos"
        read*,n
        select case (n)
            case(1)
                print*,"Cada contacto tiene un número de identificación entre el 1 y el 100."
                print*,"Para agregar un contacto digite el número de identificación (ID) que usted desee:"
                read*,m
                do  j= 1, 100
                    if (m==agenda(j)%ID) then
                        print*,"Este ID ya se encuentra reservado, si desea actualizarlo digite 4 en el menu principal"
                        print*,""
                        cycle menu
                    end if                    
                end do
                agenda(m)%ID=m      
                print*,"Ahora, escriba el nombre del contacto en minusculas:"
                read*,agenda(m)%nombre
                print*,"Ahora, escriba el número del contacto (no máximo de 11 digitos):"
                read*,agenda(m)%telefono
                print*,""
                print*,"**********************************"
                print*,"Contacto guardado correctamente!!!"
                print*,"**********************************"
                print*,""
                print*,"ID             NOMBRE            TELEFONO"
                print'(X,I0,14X,A,13X,I0)',agenda(m)%ID,trim(agenda(m)%nombre),agenda(m)%telefono
                print*,""
                print*,"¿Si deseas volver al menu principal digita 1 si deseas salir digita 2:"
                read*,m
                if ( m==1 ) then
                    cycle menu
                else if ( m==2 ) then
                    print*,"Gracias por utilizar nuestros servicios. Que tengas un bonito día!!!"
                    exit menu         
                end if                 
            case(2)
                print*,"Escriba el nombre del contacto que desea eliminar:"
                read*,comparacion
                do j = 1, 100
                    if (comparacion==agenda(j)%nombre) then
                        agenda(j)%ID=0
                        agenda(j)%nombre=""
                        agenda(j)%telefono=0
                        print*,""
                        print*,"***********************************"
                        print*,"Contacto eliminado correctamente!!!"
                        print*,"***********************************"
                        print*,""
                        print*,"¿Si deseas volver al menu principal digita 1 si deseas salir digita 2:"
                        read*,m
                        if ( m==1 ) then
                            cycle menu
                        else if ( m==2 ) then
                            print*,"Gracias por utilizar nuestros servicios. Que tengas un bonito día!!!"
                            exit menu         
                        end if
                    end if                
                end do
                print*,""
                print*,"*************************"
                print*,"Contacto NO encontrado!!!"
                print*,"*************************"
                print*,""
                print*,"Si deseas guardarlo como contacto nuevo digita 1 en el menu principal"
                print*,""
                cycle menu  
            case(3)
                print*,"Escriba el nombre del contacto que deseas buscar:"
                read*,comparacion
                do j = 1, 100
                    if (comparacion==agenda(j)%nombre) then
                        print*,""
                        print*,"************************************"
                        print*,"Contacto encontrado correctamente!!!"
                        print*,"************************************"
                        print*,""
                        print*,"ID             NOMBRE            TELEFONO"
                        print'(X,I0,14X,A,13X,I0)',agenda(j)%ID,trim(agenda(j)%nombre),agenda(j)%telefono
                        print*,""
                        print*,"¿Si deseas volver al menu principal digita 1 si deseas salir digita 2:"
                        read*,m
                        if ( m==1 ) then
                            cycle menu
                        else if ( m==2 ) then
                            print*,"Gracias por utilizar nuestros servicios. Que tengas un bonito día!!!"
                            exit menu         
                        end if
                    end if                
                end do
                print*,""
                print*,"*************************"
                print*,"Contacto NO encontrado!!!"
                print*,"*************************"
                print*,""
                print*,"Si deseas guardarlo como contacto nuevo digita 1 en el menu principal"
                print*,""
                cycle menu                      
            case(4)
                print*,"Escriba el nombre del contacto que desea actualizar:"
                read*,comparacion
                do j = 1, 100
                    if (comparacion==agenda(j)%nombre) then
                        print*,"Digite el nuevo ID:"
                        read*,agenda(j)%ID
                        print*,"Digite el nuevo nombre en minusculas:"
                        read*,agenda(j)%nombre
                        print*,"Digite el nuevo número de telefono (no máximo de 11 digitos)"
                        read*,agenda(j)%telefono
                        print*,""
                        print*,"***********************************"
                        print*,"Contacto actualizado correctamente!!!"
                        print*,"***********************************"
                        print*,""
                        print*,"ID             NOMBRE            TELEFONO"
                        print'(X,I0,14X,A,13X,I0)',agenda(j)%ID,trim(agenda(j)%nombre),agenda(j)%telefono
                        print*,""
                        print*,"¿Si deseas volver al menu principal digita 1 si deseas salir digita 2:"
                        read*,m
                        if ( m==1 ) then
                            cycle menu
                        else if ( m==2 ) then
                            print*,"Gracias por utilizar nuestros servicios. Que tengas un bonito día!!!"
                            exit menu         
                        end if
                    end if                
                end do
                print*,""
                print*,"*************************"
                print*,"Contacto NO encontrado!!!"
                print*,"*************************"
                print*,""
                print*,"Si deseas guardarlo como contacto nuevo digita 1 en el menu principal"
                print*,""
                cycle menu 
            case(5)
                print*,"Tus contactos son:"
                print*,""
                print*,"ID             NOMBRE            TELEFONO"
                do j = 1,100
                    if ( agenda(j)%ID/=0 ) then
                        print*,""
                        print'(X,I0,14X,A,13X,I0)',agenda(j)%ID,trim(agenda(j)%nombre),agenda(j)%telefono             
                    end if
                end do
                print*,""
                print*,"¿Si deseas volver al menu principal digita 1 si deseas salir digita 2:"
                read*,m
                    if ( m==1 ) then
                        cycle menu
                    else if ( m==2 ) then
                        print*,"Gracias por utilizar nuestros servicios. Que tengas un bonito día!!!"
                        exit menu         
                    end if
       end select     
    end do menu
end program ARRAYS