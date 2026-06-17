module modulo_herencia !Definicion del modulo
    implicit none

    type :: Animal !Definición de la superclase Animal
        character(len=20) :: nombre !Atributos de la clase
        character(len=20) :: especie
        integer :: edad
        contains
            procedure :: Sonido !Metodo de la clase
    end type Animal

    type, extends(Animal) :: Perro !Definición de la subclase Perro utilizando la sentencia extends para heredar de la clase Animal
        character(len=20) :: raza !Atributos de la clase
        contains
            procedure :: Sonido => Ladrar !Sobrecarga del metodo Sonido
    end type Perro

    type, extends(Animal) :: Gato !Definición de la subclase Gato utilizando la sentencia extends para heredar de la clase Animal
        character(len=20) :: raza !Atributos de la clase
        contains
            procedure :: Sonido => Maullar !Sobrecarga del metodo Sonido
    end type Gato
    
contains

    subroutine Sonido(this) !Implementación del metodo Sonido de la clase Animal
        class(Animal), intent(in) :: this
        print *, 'El animal ', this%nombre,'no hace ningun sonido' 
    end subroutine Sonido

    subroutine Ladrar(this) !Implementación del metodo Sonido de la clase Perro
        class(Perro), intent(in) :: this
        print *, 'El perro ', this%nombre, 'hace guau'
    end subroutine Ladrar

    subroutine Maullar(this) !Implementación del metodo Sonido de la clase Gato
        class(Gato), intent(in) :: this
        print *, 'El gato ', this%nombre, 'hace miau'
    end subroutine Maullar
    
end module modulo_herencia

module Empleados 
    implicit none

    type :: Empleado
        character(len=20) :: Nombre
        integer :: Identificador
        character(len=20), dimension(100) :: Empleados_a_cargo
    contains
        procedure :: Agregando_Empleado
    end type Empleado

    type, extends(Empleado) :: Gerente
    contains
        procedure :: Proyectos 
    end type Gerente

    type, extends(Empleado) :: Gerente_de_proyecto
    contains
        procedure :: Proyecto
    end type Gerente_de_proyecto

    type, extends(Empleado) :: Programador
        character(len=20) :: Lenguaje
    contains
        procedure :: Code
        procedure :: Agregando_Empleado => Empleados_Programador
    end type Programador

contains

    subroutine Agregando_Empleado(this, Nombre, Identificador)
        class(Empleado), intent(inout) :: this
        character(len=20), intent(in) :: Nombre
        integer, intent(in) :: Identificador
        this%Empleados_a_cargo(Identificador)=Nombre
    end subroutine Agregando_Empleado

    subroutine Empleados_Programador(this, Nombre, Identificador)
        class(Programador), intent(inout) :: this
        character(len=20), intent(in) :: Nombre
        integer, intent(in) :: Identificador
        integer :: i
        i=Identificador
        print*, "No se puede agregar empleados a cargo de un programador, ", this%Nombre, "no puede estar a cargo de ", Nombre
    end subroutine Empleados_Programador

    subroutine Proyectos(this)
        class(Gerente), intent(in) :: this
        print *, 'El gerente ', this%Nombre, 'esta coordinando proyectos'
    end subroutine Proyectos

    subroutine Proyecto(this)
        class(Gerente_de_proyecto), intent(in) :: this
        print *, 'El gerente de proyecto ', this%Nombre, 'esta trabajando en su proyecto '
    end subroutine Proyecto

    subroutine Code(this)
        class(Programador), intent(in) :: this
        print *, 'El programador ', this%Nombre, 'esta programando en ', this%Lenguaje
    end subroutine Code

end module Empleados

program HERENCIA
    use modulo_herencia !Se llama a el modulo que contiene las clases
    use Empleados
    implicit none
    integer :: i

    type(Animal) :: Mianimal !Se crean objetos de las clases
    type(Perro) :: Miperro
    type(Gato) :: Migato

    type(Gerente) :: MiGerente
    type(Gerente_de_proyecto) :: MiGerente_de_proyecto
    type(Programador) :: MiProgramador

    Mianimal=Animal('Leandro', 'Desconocida', 0) !Se inicializan los objetos
    Miperro=Perro('Toby', 'Canino', 5, 'Labrador')
    Migato=Gato('Garfield', 'Felino', 3, 'Siames')

    call Miperro%Sonido() !Se llama al metodo Sonido de cada objeto
    call Migato%Sonido()
    call Mianimal%Sonido()
    
    !DIFICULTAD EXTRA
    print*, " "
    print*, "****************"
    print*, "DIFICULTAD EXTRA"
    print*, "****************"
    print*, " "
    
    MiGerente=Gerente('Juan', 1, '')
    MiGerente_de_proyecto=Gerente_de_proyecto('Pedro', 2, '')
    MiProgramador=Programador('Luis', 3, '', 'Fortran')

    call MiGerente%Proyectos()
    call MiGerente_de_proyecto%Proyecto()
    call MiProgramador%Code()

    call MiGerente%Agregando_Empleado(MiGerente_de_proyecto%Nombre,MiGerente_de_proyecto%Identificador)
    call MiGerente%Agregando_Empleado(MiProgramador%Nombre,MiProgramador%Identificador)
    call MiGerente_de_proyecto%Agregando_Empleado(MiProgramador%Nombre,MiProgramador%Identificador)
    call MiProgramador%Agregando_Empleado(MiGerente%Nombre, MiGerente%Identificador)

    print*, "Los empleados a cargo de ", MiGerente%Nombre, "son: "
    
    do i = 1, 100
        if (MiGerente%Empleados_a_cargo(i) /= '') then
            print*," ", MiGerente%Empleados_a_cargo(i)
        end if  
    end do

    print*, "Los empleados a cargo de ", MiGerente_de_proyecto%Nombre, "son: "
    
    do i = 1, 100
        if (MiGerente_de_proyecto%Empleados_a_cargo(i) /= '') then
            print*," ", MiGerente_de_proyecto%Empleados_a_cargo(i)
        end if  
    end do
    
end program HERENCIA