/*
    El Principio de Responsabilidad Única dice que, una clase debe hacer una sola cosa y, por lo tanto, debe tener una sola razón para cambiar.
    De esta manera, solo un cambio potencial en la especificación del software debería poder afectar la especificación de la clase.
 */

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Revista revista = new Revista("Revista de Prueba", "Autor de Prueba", 10.0);
        Factura factura = new Factura(revista, 2, 0.1, 0.16);
        FacturaImpresion facturaImpresion = new FacturaImpresion(factura);
        FacturaPersistencia facturaPersistencia = new FacturaPersistencia(factura);
    }

    /*
     * EJERCICIO:
     * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
     * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
     * de forma correcta e incorrecta.
     */
    static class Revista {
        String nombre;
        String autor;
        double precio;

        public Revista(String nombre, String autor, double precio) {
            this.nombre = nombre;
            this.autor = autor;
            this.precio = precio;
        }
    }

    static class Factura {
        private Revista revista;
        private int cantidad;
        private double descuento;
        private double impuesto;
        private double total;

        public Factura(Revista revista, int cantidad, double descuento, double impuesto) {
            this.revista = revista;
            this.cantidad = cantidad;
            this.descuento = descuento;
            this.impuesto = impuesto;
            this.total = this.calcularTotal();
        }

        public double calcularTotal() {
            double precio = ((revista.precio - revista.precio - descuento) * this.cantidad);
            double precionConImpuesto = precio * (1 + this.impuesto);
            return precionConImpuesto;
        }

        /*
        public void imprimirFactura() {
            System.out.println(cantidad + "x " + revista.nombre + " " + revista.precio + "$");
            System.out.println("Tasa de Descuento: " + descuento);
            System.out.println("Tasa de Impuesto: " + impuesto);
            System.out.println("Total: " + total);
        }*/

        /*
        public void guardarArchivo() {
            // Crea un archivo con un nombre dado y guarda la factura
        }*/
    }

    /*
        La clase Factura viola el principio de responsabilidad única, ya que tiene más de una razón para cambiar.
        La primera violación es el método imprimirFactura(), el cual contiene la lógica para imprimir la factura.
        La segunda violación es el método guardarArchivo(), el cual contiene la lógica para guardar la factura en un archivo, y mezcla lógica de persistencia con lógica de negocios.
        Para corregir esto, se puede crear una clase separada para imprimir la factura y otra para guardar la factura en un archivo.
     */
    static class FacturaImpresion {
        private Factura factura;

        public FacturaImpresion(Factura factura) {
            this.factura = factura;
        }

        public void imprimir() {
            System.out.println(factura.cantidad + "x " + factura.revista.nombre + " " + factura.revista.precio + " $");
            System.out.println("Tasa de Descuento: " + factura.descuento);
            System.out.println("Tasa de Impuesto: " + factura.impuesto);
            System.out.println("Total: " + factura.total + " $");
        }
    }

    static class FacturaPersistencia {
        Factura factura;

        public FacturaPersistencia(Factura factura) {
            this.factura = factura;
        }

        public void guardarArchivo(String nombreArchivo) {
            // Crea un archivo con un nombre dado y guarda la factura
        }
    }

    /*
     * DIFICULTAD EXTRA (opcional):
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

    static class Libro {
        private String titulo;
        private String autor;
        private Integer copiasDisponibles;

        public Libro(String titulo, String autor, Integer copiasDisponibles) {
            this.titulo = titulo;
            this.autor = autor;
            this.copiasDisponibles = copiasDisponibles;
        }

        public String getTitulo() {
            return titulo;
        }

        public void setTitulo(String titulo) {
            this.titulo = titulo;
        }

        public String getAutor() {
            return autor;
        }

        public void setAutor(String autor) {
            this.autor = autor;
        }

        public Integer getCopiasDisponibles() {
            return copiasDisponibles;
        }

        public void setCopiasDisponibles(Integer copiasDisponibles) {
            this.copiasDisponibles = copiasDisponibles;
        }
    }

    static class Usuario {
        private String nombre;
        private int identificacion;
        private String email;

        public Usuario(String nombre, int identificacion, String email) {
            this.nombre = nombre;
            this.identificacion = identificacion;
            this.email = email;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public int getIdentificacion() {
            return identificacion;
        }

        public void setIdentificacion(int identificacion) {
            this.identificacion = identificacion;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }
    }

    static class Library {
        private List<Libro> libros;
        private List<Usuario> usuarios;

        public Library() {
            this.libros = new ArrayList<>();
            this.usuarios = new ArrayList<>();
        }

        public void registrarLibro(String titulo, String autor, int copiasDisponibles) {
            this.libros.add(new Libro(titulo, autor, copiasDisponibles));
        }

        public void registrarUsuario(String nombre, int identificacion, String email) {
            this.usuarios.add(new Usuario(nombre, identificacion, email));
        }

        public void prestarLibro(String titulo, int identificacion) {
            Libro libro = this.libros.stream().filter(l -> l.getTitulo().equals(titulo)).findFirst().orElse(null);
            Usuario usuario = this.usuarios.stream().filter(u -> u.getIdentificacion() == identificacion).findFirst().orElse(null);

            if (libro != null && usuario != null && libro.getCopiasDisponibles() > 0) {
                libro.setCopiasDisponibles(libro.getCopiasDisponibles() - 1);
                System.out.println("Libro prestado a " + usuario.getNombre());
            } else System.out.println("No se pudo realizar el préstamo");
        }

        public void devolverLibro(String titulo, int identificacion) {
            Libro libro = this.libros.stream().filter(l -> l.getTitulo().equals(titulo)).findFirst().orElse(null);
            Usuario usuario = this.usuarios.stream().filter(u -> u.getIdentificacion() == identificacion).findFirst().orElse(null);

            if (libro != null && usuario != null) {
                libro.setCopiasDisponibles(libro.getCopiasDisponibles() + 1);
                System.out.println("Libro devuelto por " + usuario.getNombre());
            } else System.out.println("No se pudo realizar la devolución");
        }
    }

    static class LibroRegistro {
        private List<Libro> libros;

        public LibroRegistro() {
            this.libros = new ArrayList<>();
        }

        public void registrarLibro(Libro libro) {
            this.libros.add(libro);
        }

        public Libro buscarLibro(String titulo) {
            return this.libros.stream().filter(l -> l.getTitulo().equals(titulo)).findFirst().orElse(null);
        }
    }

    static class UsuarioRegistro {
        private List<Usuario> usuarios;

        public UsuarioRegistro() {
            this.usuarios = new ArrayList<>();
        }

        public void registrarUsuario(Usuario u) {
            this.usuarios.add(u);
        }

        public Usuario buscarUsuario(int identificacion) {
            return this.usuarios.stream().filter(u -> u.getIdentificacion() == identificacion).findFirst().orElse(null);
        }
    }

    static class PrestamoProcesador {
        private LibroRegistro libroRegistro;
        private UsuarioRegistro usuarioRegistro;

        public PrestamoProcesador(LibroRegistro libroRegistro, UsuarioRegistro usuarioRegistro) {
            this.libroRegistro = libroRegistro;
            this.usuarioRegistro = usuarioRegistro;
        }

        public void prestarLibro(String titulo, int identificacion) {
            Libro libro = libroRegistro.buscarLibro(titulo);
            Usuario usuario = usuarioRegistro.buscarUsuario(identificacion);

            if (libro != null && usuario != null && libro.getCopiasDisponibles() > 0) {
                libro.setCopiasDisponibles(libro.getCopiasDisponibles() - 1);
                System.out.println("Libro prestado a " + usuario.getNombre());
            } else {
                System.out.println("No se pudo realizar el préstamo");
            }
        }

        public void devolverLibro(String titulo, int identificacion) {
            Libro libro = libroRegistro.buscarLibro(titulo);
            Usuario usuario = usuarioRegistro.buscarUsuario(identificacion);

            if (libro != null && usuario != null) {
                libro.setCopiasDisponibles(libro.getCopiasDisponibles() + 1);
                System.out.println("Libro devuelto por " + usuario.getNombre());
            } else {
                System.out.println("No se pudo realizar la devolución");
            }
        }
    }

}
