package com.amsoft.roadmap.example26;

import java.util.ArrayList;
import java.util.Scanner;

public class FranDev200 {

    static class Refresco{

        private String nombre;
        private double precio;

        public Refresco(String nombre, double precio){
            this.nombre = nombre;
            this.precio = precio;
        }

        /*

        EJEMPLO INCORRECTO

        // Funcionalidad 1
        public void aumentarPrecio(double precio){
            this.precio += precio;
        }

        // Funcionalidad 2
        public void infoRefresco(){
            System.out.println(this.nombre + " --> " + this.precio + "€");
        }
        */

        // Funcionalidad 1
        public void aumentarPrecio(double precio){
            this.precio += precio;
        }

    }

    static class Carta{

        Refresco refresco;

        public Carta(Refresco refresco){
            this.refresco = refresco;
        }

        //Funcionalidad 2
        public void verCarta(){
            System.out.println(this.refresco.nombre + " ---> " +  this.refresco.precio + "€");
        }

    }
    static void main() {

        /*

        EJERCICIO:
         * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
         * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
         * de forma correcta e incorrecta.

         */

        Refresco refresco = new Refresco("Fanta de naranja", 2.50);
        Carta carta = new Carta(refresco);
        carta.verCarta();

        refresco.aumentarPrecio(0.20);
        carta.verCarta();


        /*

        DIFICULTAD EXTRA (opcional):
         * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
         * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
         * y el procesamiento de préstamos de libros.
         * Requisitos:
         * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
         * información básica como título, autor y número de copias disponibles.
         * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
         * información básica como nombre, número de identificación y correo electrónico.
         * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
         * tomar prestados y devolver libros.
         * Instrucciones:
         * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
         * los tres aspectos mencionados anteriormente (registro de libros, registro de
         * usuarios y procesamiento de préstamos).
         * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
         * siguiendo el Principio de Responsabilidad Única.

         */


        System.out.println("\n===============");
        System.out.println("EJERCICIO EXTRA");
        System.out.println("===============");

        menuAcciones();

        try {
            Thread.sleep(1500);
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        }

        System.out.println("Programa finalizado.");

    }

    static final ArrayList<Usuario> usuarios = new ArrayList<>();
    static final ArrayList<Libro> libros = new ArrayList<>();
    static final ArrayList<Prestamo> prestamos = new ArrayList<>();


    static class Libro{
        private String titulo;
        private String autor;
        private int nroCopias;

        public Libro(String titulo, String autor, int nroCopias){
            this.titulo = titulo;
            this.autor = autor;
            this.nroCopias = nroCopias;
        }

        public Libro(){ }

        public String getTitulo() { return titulo; }

        public void setTitulo(String titulo) { this.titulo = titulo; }

        public String getAutor() { return autor; }

        public void setAutor(String autor) { this.autor = autor; }

        public int getNroCopias() { return nroCopias; }

        public void setNroCopias(int nroCopias) { this.nroCopias = nroCopias; }

    }

    static class Usuario{
        private String nombre;
        private String dni;
        private String correo;

        public Usuario(String nombre, String dni, String correo) {
            this.nombre = nombre;
            this.dni = dni;
            this.correo = correo;
        }

        public Usuario() { }

        public String getNombre() { return nombre; }

        public void setNombre(String nombre) { this.nombre = nombre; }

        public String getDni() { return dni; }

        public void setDni(String dni) { this.dni = dni; }

        public String getCorreo() { return correo; }

        public void setCorreo(String correo) { this.correo = correo; }

    }

    static class Prestamo{

        private Libro libro;
        private Usuario usuario;
        private int nroCopias;

        public Prestamo(Usuario usuario, Libro libro, int nroCopias) {
            this.usuario = usuario;
            this.libro = libro;
            this.nroCopias = nroCopias;
        }

        public Prestamo() { }

        public Libro getLibro() { return libro; }

        public void setLibro(Libro libro) { this.libro = libro; }

        public Usuario getUsuario() { return usuario; }

        public void setUsuario(Usuario usuario) { this.usuario = usuario; }

        public int getNroCopias() { return nroCopias; }

        public void setNroCopias(int nroCopias) { this.nroCopias = nroCopias; }
    }

/*

    // CLASE ERRONEA
    static class Library{

        public void registroUsuario(){

            Usuario user = null;

            Scanner scan =  new Scanner(System.in);
            System.out.print("Introduzca su nombre: ");
            String nombre = scan.nextLine();


            System.out.print("Introduzca su dni: ");
            String dni = scan.nextLine();

            for (Usuario u : usuarios){
                if(u.getDni().equals(dni)){
                    System.out.println("Este DNI ya está registrado.");
                    System.out.println("ERROR al registar un nuevo usuario.");
                    return;
                }
            }

            System.out.print("Introduzca su correo electrónico: ");
            String correo = scan.nextLine();

            for (Usuario u : usuarios){
                if(u.getCorreo().equals(correo)){
                    System.out.println("Este correo ya está en uso.");
                    System.out.println("ERROR al registar un nuevo usuario.");
                    return;
                }
            }

            user = new Usuario(nombre, dni, correo);
            usuarios.add(user);

            System.out.println("Usuario " + user.getNombre() + " registrado con exito.");
        }

        public void eliminarUsuario(){

            Scanner scan =  new Scanner(System.in);
            System.out.print("Introduzca el DNI del usuario a eliminar: ");
            String dni = scan.nextLine();

            for (Usuario u : usuarios){
                if(u.getDni().equals(dni)){
                    System.out.println("Usuario " + u.getNombre() + " eliminado con exito.");
                    usuarios.remove(u);
                    break;
                }else{
                    System.out.println("Este dni no está registrado.");
                }
            }

        }

        public void registroLibro(){

            Libro libro = null;

            Scanner scan =  new Scanner(System.in);
            System.out.print("Introduzca el título del libro: ");
            String titulo = scan.nextLine();

            for(Libro l : libros){
                if(l.getTitulo().equals(titulo)){
                    System.out.println("Este título ya está registrado.");
                    return;
                }
            }

            System.out.print("Introduce el nombre del autor: ");
            String autor = scan.nextLine();
            System.out.println("Indica el número de copias");
            int  nroCopias = scan.nextInt();

            libro = new Libro(titulo, autor, nroCopias);
            libros.add(libro);
            System.out.println("Libro " + libro.getTitulo() + " registrado con exito.");

        }

        public void eliminarLibro(){

            Scanner scan =  new Scanner(System.in);

            System.out.print("Introduce el título del libro a eliminar: ");
            String titulo = scan.nextLine();

            for(Libro l : libros){
                if(l.getTitulo().equals(titulo)){
                    System.out.println("Libro " + l.getTitulo() + " eliminado con exito.");
                    libros.remove(l);
                    break;
                }
            }

        }

        public void registroPrestamo(){

            Usuario usuario = null;
            Libro libro = null;
            Prestamo prestamo = null;

            Scanner scan =  new Scanner(System.in);
            System.out.print("Introduzca el correo del usuario: ");
            String correo = scan.nextLine();

            for(Usuario u : usuarios){
                if(u.getCorreo().equals(correo)){
                    usuario = u;
                }else{
                    System.out.println("Este usuario no se ha encontrado.");
                    return;
                }
            }

            System.out.print("Introduzca el título del libro: ");
            String titulo = scan.nextLine();

            for(Libro l : libros){
                if(l.getTitulo().equals(correo)){
                    libro = l ;
                }else{
                    System.out.println("Este libro no se ha encontrado.");
                    return;
                }
            }

            System.out.print("Cuantas copias quieres llevarte: ");
            int copias = scan.nextInt();

            if(libro.getNroCopias() < copias){
                System.out.println("No ha suficiente stock.");
                return;
            }else{
                libro.setNroCopias(libro.getNroCopias() - copias);
            }

            prestamo = new Prestamo(usuario, libro, copias);
            System.out.println(" *** RESUMEN DEL PRESTAMO ***");
            System.out.println("=============================");
            System.out.println("Cliente: " + usuario.getNombre() + " [" + usuario.getCorreo() + "]");
            System.out.println("DNI: " + usuario.getDni());
            System.out.println("------------------------------");
            System.out.println("Libro a llevarse: " + libro.getTitulo() + " [" + libro.getAutor() + "]");
            System.out.println("Nro de copias: " + copias);
            System.out.println("==============================");
            System.out.println("Prestamo realizado con exito. Gracias por su compra.");

            prestamos.add(prestamo);


        }

        public void infoLibreria(){

            System.out.println("LIBROS DISPONIBLES");
            System.out.println("==================\n");

            for(Libro l : libros){

                System.out.println(l.getTitulo() + " [" + l.getAutor() + "]");
                System.out.println("Nro de copias: " + l.getNroCopias());
                System.out.println("----------------------\n");

            }
        }

        public void infoPrestamos(){

            System.out.println("PRESTAMOS REALIZADOS");
            System.out.println("-_-_-_-_-_-_-_-_-_-_-");

            for(Prestamo p : prestamos){
                System.out.println(" - " + p.getUsuario().getNombre() + " ---> " + p.getLibro().getTitulo()
                        + "   [" + p.getNroCopias() + "]" );
            }

        }

    }

  */

    static class FuncionesUsuarios{

        public void registroUsuario(){

            Usuario user = null;

            Scanner scan =  new Scanner(System.in);
            System.out.print("Introduzca su nombre: ");
            String nombre = scan.nextLine();


            System.out.print("Introduzca su dni: ");
            String dni = scan.nextLine();

            for (Usuario u : usuarios){
                if(u.getDni().equals(dni)){
                    System.out.println("Este DNI ya está registrado.");
                    System.out.println("ERROR al registar un nuevo usuario.");
                    return;
                }
            }

            System.out.print("Introduzca su correo electrónico: ");
            String correo = scan.nextLine();

            for (Usuario u : usuarios){
                if(u.getCorreo().equals(correo)){
                    System.out.println("Este correo ya está en uso.");
                    System.out.println("ERROR al registar un nuevo usuario.");
                    return;
                }
            }

            user = new Usuario(nombre, dni, correo);
            usuarios.add(user);

            System.out.println("Usuario " + user.getNombre() + " registrado con exito.");
        }

        public void eliminarUsuario(){

            Scanner scan =  new Scanner(System.in);
            System.out.print("Introduzca el DNI del usuario a eliminar: ");
            String dni = scan.nextLine();

            for (Usuario u : usuarios){
                if(u.getDni().equals(dni)){
                    System.out.println("Usuario " + u.getNombre() + " eliminado con exito.");
                    usuarios.remove(u);
                    break;
                }else{
                    System.out.println("Este dni no está registrado.");
                }
            }

        }

    }

    static class FuncionesLibros{

        public void registroLibro(){

            Libro libro = null;

            Scanner scan =  new Scanner(System.in);
            System.out.print("Introduzca el título del libro: ");
            String titulo = scan.nextLine();

            for(Libro l : libros){
                if(l.getTitulo().equals(titulo)){
                    System.out.println("Este título ya está registrado.");
                    return;
                }
            }

            System.out.print("Introduce el nombre del autor: ");
            String autor = scan.nextLine();
            System.out.print("Indica el número de copias: ");
            int  nroCopias = scan.nextInt();

            libro = new Libro(titulo, autor, nroCopias);
            libros.add(libro);
            System.out.println("Libro \"" + libro.getTitulo() + "\" registrado con exito.");

        }

        public void eliminarLibro(){

            Scanner scan =  new Scanner(System.in);

            System.out.print("Introduce el título del libro a eliminar: ");
            String titulo = scan.nextLine();

            for(Libro l : libros){
                if(l.getTitulo().equals(titulo)){
                    System.out.println("Libro " + l.getTitulo() + " eliminado con exito.");
                    libros.remove(l);
                    break;
                }
            }

        }

        public void infoLibreria(){

            System.out.println("LIBROS DISPONIBLES");
            System.out.println("==================");

            for(Libro l : libros){

                System.out.println(" - " + l.getTitulo() + " [" + l.getAutor() + "]");
                System.out.println("    Nro de copias: " + l.getNroCopias());
                System.out.println("----------------------");

            }
        }

    }

    static class FuncionesPrestamos{

        public void registroPrestamo(){

            Usuario usuario = null;
            Libro libro = null;
            Prestamo prestamo = null;

            Scanner scan =  new Scanner(System.in);
            System.out.print("Introduzca el correo del usuario: ");
            String correo = scan.nextLine();

            for(Usuario u : usuarios){
                if(u.getCorreo().equals(correo)){
                    usuario = u;
                }else{
                    System.out.println("Este usuario no se ha encontrado.");
                    return;
                }
            }

            System.out.print("Introduzca el título del libro: ");
            String titulo = scan.nextLine();

            for(Libro l : libros){
                if(l.getTitulo().equalsIgnoreCase(titulo)){
                    libro = l ;
                }else{
                    System.out.println("Este libro no se ha encontrado.");
                    return;
                }
            }

            System.out.print("Cuantas copias quieres llevarte: ");
            int copias = scan.nextInt();

            if(libro.getNroCopias() < copias){
                System.out.println("No ha suficiente stock.");
                return;
            }else{
                libro.setNroCopias(libro.getNroCopias() - copias);
            }

            prestamo = new Prestamo(usuario, libro, copias);
            System.out.println(" *** RESUMEN DEL PRESTAMO ***");
            System.out.println("=============================");
            System.out.println("Cliente: " + usuario.getNombre() + " [" + usuario.getCorreo() + "]");
            System.out.println("DNI: " + usuario.getDni());
            System.out.println("------------------------------");
            System.out.println("Libro a llevarse: " + libro.getTitulo() + " [" + libro.getAutor() + "]");
            System.out.println("Nro de copias: " + copias);
            System.out.println("==============================");
            System.out.println("Prestamo realizado con exito. Gracias por su compra.");

            prestamos.add(prestamo);


        }

        public void infoPrestamos(){

            System.out.println("PRESTAMOS REALIZADOS");
            System.out.println("-_-_-_-_-_-_-_-_-_-_-");

            for(Prestamo p : prestamos){
                System.out.println(" - " + p.getUsuario().getNombre() + " ---> " + p.getLibro().getTitulo()
                        + "   [" + p.getNroCopias() + "] ud." );
            }

        }

    }

    public static void menuAcciones(){

        FuncionesLibros funcionesLibros = new FuncionesLibros();
        FuncionesPrestamos funcionesPrestamos = new FuncionesPrestamos();
        FuncionesUsuarios funcionesUsuarios = new FuncionesUsuarios();

        int  opcion = 0;
        int  opcion2 = 0;
        Scanner scan =  new Scanner(System.in);

        while (opcion != 4){
            System.out.println(" *** LIBRERÍA FRANDEV ***");
            System.out.println("=========================");
            System.out.println(" 1 - Libros.");
            System.out.println(" 2 - Usuarios.");
            System.out.println(" 3 - Prestamos.");
            System.out.println(" 4 - Desconectar.");
            System.out.println("==============");
            System.out.print("Respuesta (escriba el número): ");
            opcion = scan.nextInt();

            switch(opcion){
                case 1:

                    System.out.println("-------------------");
                    System.out.println("1. Añadir un libro.");
                    System.out.println("2. Eliminar un libro.");
                    System.out.println("3. Info de los libros.");
                    System.out.println("--------------------");
                    System.out.print("Respuesta: ");
                    opcion2 = scan.nextInt();

                    switch (opcion2){
                        case 1:
                            funcionesLibros.registroLibro();
                            break;
                        case 2:
                            funcionesLibros.eliminarLibro();
                            break;
                        case 3:
                            funcionesLibros.infoLibreria();
                            break;
                    }

                    break;

                case 2:

                    System.out.println("-------------------");
                    System.out.println("1. Añadir un usuario.");
                    System.out.println("2. Eliminar un usuario.");
                    System.out.println("--------------------");
                    System.out.print("Respuesta: ");
                    opcion2 = scan.nextInt();

                    switch (opcion2){
                        case 1:
                            funcionesUsuarios.registroUsuario();
                            break;
                        case 2:
                            funcionesUsuarios.eliminarUsuario();
                            break;
                    }

                    break;

                case 3:

                    System.out.println("-------------------");
                    System.out.println("1. Hacer un prestamo.");
                    System.out.println("2. Info de los prestamos.");
                    System.out.println("--------------------");
                    System.out.print("Respuesta: ");
                    opcion2 = scan.nextInt();

                    switch (opcion2){
                        case 1:
                            funcionesPrestamos.registroPrestamo();
                            break;
                        case 2:
                            funcionesPrestamos.infoPrestamos();
                            break;
                    }

                    break;

                case 4:

                    System.out.println("Saliendo...");

                    break;
            }



        }


    }

}
