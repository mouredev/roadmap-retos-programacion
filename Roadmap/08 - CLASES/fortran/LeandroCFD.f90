!Fortran propiamente no tiene clases, pero se pueden simular con variables de tipo derivado y modulos

module Modulo_Clase !Se define un modulo que contiene la definición de las clases Alumno, Pila y Cola
    implicit none

    type :: Alumno !Se define el tipo derivado Alumno
        real :: nota !Atributos de la clase
        integer :: edad
        character(len=20) :: nombre
        contains
            procedure :: MostrarDatos !Método de la clase
    end type Alumno

    type :: Pila
        integer :: tope
        integer, dimension(100) :: elementos
        contains
            procedure :: Apilar
            procedure :: Desapilar
            procedure, nopass :: MostrarElementos
            procedure, nopass :: NumeroElementos
    end type Pila

    type :: Cola
        integer :: frente
        integer :: final
        integer, dimension(100) :: elementos
        contains
            procedure :: Encolar
            procedure :: Desencolar
            procedure, nopass :: MostrarElementos
            procedure, nopass :: NumeroElementos
    end type Cola

contains
    subroutine MostrarDatos(this) !Implementación del método MostrarDatos
        class(Alumno), intent(in) :: this !Se pasa la instancia de la clase como argumento
        print *, 'Nombre: ', this%nombre 
        print *, 'Edad: ', this%edad
        print *, 'Nota: ', this%nota
    end subroutine MostrarDatos

    subroutine Apilar(this, elemento) !Implementación del método Apilar
        class(Pila), intent(inout) :: this
        integer, intent(in) :: elemento
        this%tope = this%tope + 1 !Se incrementa el tope de la pila
        this%elementos(this%tope) = elemento !Se añade el elemento a la pila
    end subroutine Apilar

    subroutine Desapilar(this) !Implementación del método Desapilar
        class(Pila), intent(inout) :: this
        if ( this%tope <0 ) then !Se verifica que haya elementos en la pila
            print *, "No hay elementos para desapilar"
            return            
        end if
        this%elementos(this%tope)=0 !Se elimina el elemento
        this%tope = this%tope - 1 !Se decrementa el tope
    end subroutine Desapilar

    subroutine Encolar(this, elemento) !Implementación del método Encolar
        class(Cola), intent(inout) :: this
        integer, intent(in) :: elemento
        this%final = this%final + 1 !Se incrementa el final de la cola
        this%elementos(this%final) = elemento !Se añade el elemento a la cola
    end subroutine Encolar

    subroutine Desencolar(this) !Implementación del método Desencolar
        class(Cola), intent(inout) :: this
        if ( this%final-this%frente <0 ) then !Se verifica que haya elementos en la cola
            print *, "No hay elementos para desencolar"
            return            
        end if
        this%elementos(this%frente)=0 !Se elimina el elemento
        this%frente = this%frente + 1 !Se incrementa el frente
    end subroutine Desencolar

    subroutine MostrarElementos(this) !Implementación del método MostrarElementos
        class(*), intent(in) :: this
        integer :: i
        select type(this) !Se selecciona el tipo de la instancia
            type is (Pila) !Si es de tipo Pila
                print *,"Lista de elementos (Pila):"
                do i = 0, this%tope-1
                    print *, this%elementos(this%tope-i)
                end do
            type is (Cola) !Si es de tipo Cola
                print*,"Lista de elementos (Cola):"
                do i = this%frente, this%final
                    print *, this%elementos(i)
                end do
        end select
    end subroutine MostrarElementos

    subroutine NumeroElementos(this) !Implementación del método NumeroElementos
        class(*), intent(in) :: this
        select type(this)
            type is (Pila)
                print *,"Numero de elementos (Pila):", this%tope
            type is (Cola)
                print*,"Numero de elementos (Cola):", this%final-this%frente+1
        end select
    end subroutine NumeroElementos

end module Modulo_Clase 

program CLASES
    use Modulo_Clase !Se importa el modulo que contiene la definición de la clase

    implicit none
    
    type(Alumno) :: Alumno1, Alumno2 !Se definen dos instancias "Variables" de la clase Alumno
    type(Pila) :: Mipila !Se define una instancia de la clase Pila
    type(Cola) :: Micola !Se define una instancia de la clase Cola

    Alumno1%nota = 10.0 !Inicialización de los datos de Alumno1
    Alumno1%edad = 20
    Alumno1%nombre = 'Juan'

    Alumno2%nota = 8.0 !Inicialización de los datos de Alumno2
    Alumno2%edad = 21
    Alumno2%nombre = 'Pedro'

    call Alumno1%MostrarDatos() ! Llamada a los métodos MostrarDatos
    call Alumno2%MostrarDatos()

    Alumno1%nombre='Carlos'
    Alumno1%edad=22
    Alumno1%nota=6.5
    
    call Alumno1%MostrarDatos()

    !DIFICULTAD EXTRA
    Mipila%tope = 0
    call Mipila%Apilar(5) !Se apilan elementos
    call Mipila%Apilar(2)
    call Mipila%Apilar(10)
    call Mipila%Apilar(22)
    call Mipila%Apilar(50)

    call Mipila%MostrarElementos(Mipila) !Se muestran los elementos de la pila
    call Mipila%NumeroElementos(Mipila) !Se muestra el número de elementos de la pila
    call Mipila%Desapilar() !Se desapila un elemento
    call Mipila%MostrarElementos(Mipila)
    call Mipila%NumeroElementos(Mipila)

    Micola%frente = 1
    Micola%final = 0    

    call Micola%Encolar(1) !Se encolan elementos
    call Micola%Encolar(3)
    call Micola%Encolar(10)
    call Micola%Encolar(50)
    call Micola%Encolar(98)

    call Micola%MostrarElementos(Micola) !Se muestran los elementos de la cola
    call Micola%NumeroElementos(Micola) !Se muestra el número de elementos de la cola
    call Micola%Desencolar() !Se desencola un elemento
    call Micola%Desencolar()
    call Micola%Desencolar()
    call Micola%Desencolar()
    call Micola%MostrarElementos(Micola) !Se muestran los elementos de la cola
    call Micola%NumeroElementos(Micola) !Se muestra el número de elementos de la cola

end program CLASES