program estructuras
    implicit none
    ! Manejo de Arrays en Fortran
    ! Los arrays en Fortran son variables multidimensionales que contienen más de un valor donde se 
    ! accede a cada valor utilizando uno o más índices.  En Fortran los arrays por defecto se inician en 1

    ! Declaración de Arrays
    ! Se pueden declarar arrays de cualquier tipo.  Hay dos notaciones para declarar variables array:
    ! Usando el atributo dimension o añadiendo las dimensiones del array al nombre de la variable
    ! TIPO, DIMENSION(dimensiones) :: nombre
    ! TIPO, DIMENSION :: nombre(dimensiones)
    ! TIPO :: nombre(dimensiones)

    integer :: i, n

    ! Declaración estática de Arrays o Tablas
    
    ! Array de una dimension
    integer, dimension(10) :: array1
    ! Una declaración de array equivalente
    integer :: array2(10)

    ! Array de dos dimensiones
    integer, dimension(10, 10) :: array3

    ! Limites inferior y superior de una dimensión
    real :: array4(0:4)
    real :: array5(-5:5)

    integer, dimension (2,3) :: mat1 = reshape( (/ 1, 2, 3, 4, 5, 6/) , (/2,3/) )

    ! Declaración dinámica de Arrays o Tablas

    ! La creación de este tipo de tablas se hace en dos etapas:
    ! 1. Declaración de la tabla mediante el atributo ALLOCATABLE, sin información sobre el
    !    tamaño de la misma.
    !        TIPO, ALLOCATABLE :: nombre_tabla(ind-dim)
    !    donde ind-dim es la indicación sobre el número de dimensiones de la tabla.
    ! 2. Cuando se desee crear la tabla, se usará la instrucción
    !        ALLOCATE(nombre_tabla(dim))
    
    real*4, allocatable :: tabla(:, :)

    ! Manejo de Tipos Derivados 
    type :: t_pair
        integer :: i
        real :: x
    end type

    type(t_pair) :: pair

    ! Rebanado o corte de arrays - notación rebanado

    array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  ! Constructor Array
    array2 = [(i, i = 1, 10)]                 ! Bucle Do implícito 

    array4 = [1.0, 2.0, 3.0, 4.0, 5.0]
    print *, array4(0)
    print *, array4(4)
    print *, mat1

    print *, 'Array inicial: ', array1
    array1(:) = 0                             ! Establece todos los elementos a cero
    print *, 'Todos los elementos a cero: ', array1
    array1(1:5) = 1                           ! Establece los primeros cinco elementos a 1
    print *, 'Cinco primeros elementos a 1: ', array1
    array1(6:) = 2                            ! Establece todos los elementos después de 5 a 2
    print *, 'Cinco últimos elementos a 2: ', array1

    print *, array2(1:10:2)   ! Imprime los elementos con índice impar
    print *, array3(:,1)      ! Imprime la primera columna en un array 2D
    print *, array2(10:1:-1)  ! Imprime un array en reverso

    ! Declaración de una varibale type e inicialización de sus miembros
   
    pair%i = 1
    pair%x = 0.5
    print *, 't_pair i: ', pair%i, ' t_pair x : ', pair%x 

    print *, 'Dimensión de la matriz dinámica: '
    read *, n
    if (allocated(tabla) .eqv. .true.) then
        allocate(tabla(n, n))
    end if

end program estructuras