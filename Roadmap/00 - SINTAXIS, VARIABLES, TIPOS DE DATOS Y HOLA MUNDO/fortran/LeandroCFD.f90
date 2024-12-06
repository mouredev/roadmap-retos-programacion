program HOLA_FORTRAN
    implicit none
    
    !Esto es un comentario.
    !Los comentarios deben iniciar con el caracter "!" si es la versión Fortran90 o posterior y con "c" si es la versión Fortran77.
    !La pagina web oficial de Fortran en español es https://fortran-lang.org/es/index , en la pestaña aprender pueden encontrar 
    !multiples recursos para aprender Fortran como manuales y tutoriales
    !Puedes encotrar un manual muy completo en http://anyp.fcaglp.unlp.edu.ar/biblio/fortran/fortran90.pdf.
    
    !Para crear y utilizar una variable en Fortran primero se deben declarar, la sintaxis de declaración es la siguiente.
    integer a   !Variable de tipo entero    (numeros enteros)
    real b      !Variable de tipo real      (numeros reales)
    complex c   !Variable de tipo complejo  (numeros complejos)
    logical d   !Variable de tipo logico    (verdadero o falso)
    character e !Variable de tipo caracter  (cadenas de caracteres)
    !Los nombres de las variables deben iniciar con una letra y tener máximo 23 caracteres.
    !Es importante saber que Fortran no distingue minusculas de mayusculas, 
    !por lo tanto la variable "a" y "A" es la misma para Fortran.

    !Para declarar varias variables del mismo tipo de dato se puede utilizar la coma.
    integer f,g,h,i
    real j,k,l,m
    complex n,o,p,q
    logical r,s,t,u
    character v,w,x,y

    !Otra sintaxis permitida para declarar variables es utilizando doble dos puntos.
    integer :: z,aa,ab,ac
    real :: ad,ae,af,ag
    complex :: ah,ai,aj,ak
    logical :: al,am,an,ao
    character :: ap,aq,ar,as

    !Para declarar una constante se utiliza el atributo "parameter".
    integer, parameter :: at=1000
    !Las constantes son utiles cuando se tiene certeza que no van variar su valor durante la ejecución del programa.
    !Por ejemplo valores como el numero pi o el numero de Euler.

    !Se puede asignar un valor a la variable en el momento de su declaración.
    integer :: au=1
    real :: av=2.1
    complex :: aw=(3,4) !A las variables complejas se les debe asignar dos valores, la parte entera (3) y la parte imaginaria (4).
    logical :: ax=.true. !Las variables logical pueden ser o verdaderas (.true.) o falsas (.false.)
    character (len=12):: ay='Hola Fortran' !Las variables de cadenas de caracteres deben especificar la longitud de caracteres que
    !tiene la variable (esto se realiza con el atributo "len"), si no se especifica, Fortran asume que la variable solo tiene un 
    !caracter. Si no sabemos que tamaño va a tener la variable podemos utilizar el comodin "*".
    character (len=*), parameter:: az='cadena de caracter', ba='otra cadena'
    !Si la variable de cadena de caracteres tiene una comilla simple en su interior, entonces se debe asignar su valor con comillas
    !dobles, tal y como se muestra a continuación.
    character (len=16), parameter:: bb="Ciudad 'Bogotá'"

    !Las variables de tipo real pueden ser de precisión simple, doble o cuadruple. Para definir la presión se utiliza el atributo
    !"kind", tal y como se muestra a continuación.
    real (kind=4):: bc !la variable bc tiene precisión simple. Se pueden utilizar valores desde 1.2x10^-38 hasta 3.4x10^38 con
    !8 cifras significativas.
    real (kind=8):: bd !la variable bd tiene precisión doble. Se pueden utilizar valores desde 2.2x10^-308 hasta 1.8x10^308 con
    !16 cifras significativas.
    real (kind=16):: be !la variable be tiene precisión cuadruple. No se exactamente de que números a que números son permitidos 
    !con esta precisión (sería fabuloso que alguien completara esta información) pero son números con máximo 32 cifras 
    !significativas.

    !Fortran permite crear variables de tipo derivado, las cuales se crean como combinación de variables tipo intrinseco (integer,
    !real, complex, logical y character) la sintaxis para crear una variable de tipo derivado es la siguiente.
    type fluido
        character (len=10):: nombre !Nombre del fluido
        integer :: gamma !Peso especifico
        real :: rho !Densidad
    end type

    !Para declarar una variable tipo fluido es la siguiente.
    type (fluido) :: water !En este caso la variable "water" es de tipo "fluido"

    !La asignaciones de valores a la variable "water" se puede realizar de dos maneras, primero asignando valores de manera global
    !o se puede realizar la asignación por componentes
    water=fluido('agua',9810,999.7) !Asignación global
    water%nombre='agua' !Asignación por componentes
    water%gamma=9810
    water%rho=999.7

    !Para imprimir por terminal en Fortran se pueden utilizar las variables "print" o "write".
    print*,'Hola Fortran' !El asterisco imprime el texto luego de la coma en formato por defecto de Fortran.
    print*,ay !Se imprime en terminal la variable ay con print.
    write(*,*)'Hola Fortran' !El primer asterisco dentro de los parentesis representa que se va a imprimir en la terminal y el
    !segundo que se imprime el texto en formato por defecto de Fortran.
    write(*,*)ay !Se imprime en terminal la variable ay con write.

    !Algunos editores o compiladores de Fortran pueden reconocer que una variable no esta siedo usada dentro del programa, por lo
    !tanto, para evitar warnings indeseados se utilizan todas las variables declaradas dentro del programa
    a=1;b=1.1;c=(1,1);d=.true.;e='1';f=1;g=1;h=1;i=1;j=1.1;k=1.1;l=1.1;m=1.1;n=(1,1);o=(1,1);p=(1,1);q=(1,1);r=.true.;s=.true.
    t=.true.;u=.true.;v='1';w='1';x='1';y='1';z=1;aa=1;ab=1;ac=1;ad=1.1;ae=1.1;af=1.1;ag=1.1;ah=(1,1);ai=(1,1);aj=(1,1);ak=(1,1)
    al=.true.;am=.true.;an=.true.;ao=.true.;ap='1';aq='1';ar='1';as='1';au=1;av=1.1;aw=1;ax=.true.;bc=1.1;bd=1.1;be=1.1

end program HOLA_FORTRAN