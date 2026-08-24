program FICHEROS
    implicit none

    integer :: i
    character(len=100), dimension(3) :: lectura
    
    open(20, file='LeandroCFD.txt', status='new') ! Crear un archivo de texto llamado LeandroCFD.txt con status 'new'
    
    write(20,*) 'Mi nombre es Leandro' ! Se escribe en el archivo de texto
    write(20,*) 'Mi edad es 31 años'
    write(20,*) 'Mi lenguaje de programación favorito es Fortran'

    rewind(20) ! Se regresa al inicio del archivo de texto

    do i = 1, 3
        read(20,'(A)') lectura(i) ! Se lee el archivo de texto y se almacena en el array lectura
        print*, lectura(i) ! Se imprime en consola
    end do

    close(20) ! Se cierra el archivo de texto

    call system('del ' // 'LeandroCFD.txt') ! Se elimina el archivo de texto con el comando 'del' de Windows

end program FICHEROS