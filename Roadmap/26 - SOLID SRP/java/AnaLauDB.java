import java.util.logging.*;
import java.util.*;
import java.io.IOException;

public class AnaLauDB {

    // Logger para la clase
    private static final Logger logger = Logger.getLogger(AnaLauDB.class.getName());

    // ==========================================================================
    // 1. DISEÑO QUE NO CUMPLE SRP - CLASE MONOLÍTICA
    // ==========================================================================
    static class LibraryViolaSRP {
        private List<String[]> libros; // [titulo, autor, copias_disponibles]
        private List<String[]> usuarios; // [nombre, id, email]
        private List<String[]> prestamos; // [usuario_id, libro_titulo, fecha]
        private Logger logger;

        public LibraryViolaSRP() {
            this.libros = new ArrayList<>();
            this.usuarios = new ArrayList<>();
            this.prestamos = new ArrayList<>();
            this.logger = Logger.getLogger(LibraryViolaSRP.class.getName());
        }

        // Responsabilidad 1: Gestión de libros
        public void registrarLibro(String titulo, String autor, int copias) {
            logger.info("Registrando libro: " + titulo);
            libros.add(new String[] { titulo, autor, String.valueOf(copias) });
            System.out.println("Libro registrado: " + titulo + " por " + autor);
        }

        public void mostrarLibros() {
            logger.info("Mostrando todos los libros");
            System.out.println("=== Libros Disponibles ===");
            for (String[] libro : libros) {
                System.out.printf("Título: %s, Autor: %s, Copias: %s%n",
                        libro[0], libro[1], libro[2]);
            }
        }

        // Responsabilidad 2: Gestión de usuarios
        public void registrarUsuario(String nombre, String id, String email) {
            logger.info("Registrando usuario: " + nombre);
            usuarios.add(new String[] { nombre, id, email });
            System.out.println("Usuario registrado: " + nombre);
        }

        public void mostrarUsuarios() {
            logger.info("Mostrando todos los usuarios");
            System.out.println("=== Usuarios Registrados ===");
            for (String[] usuario : usuarios) {
                System.out.printf("Nombre: %s, ID: %s, Email: %s%n",
                        usuario[0], usuario[1], usuario[2]);
            }
        }

        // Responsabilidad 3: Gestión de préstamos
        public boolean prestarLibro(String usuarioId, String tituloLibro) {
            logger.info("Procesando préstamo: " + tituloLibro + " para usuario " + usuarioId);

            // Verificar si el usuario existe
            boolean usuarioExiste = false;
            for (String[] usuario : usuarios) {
                if (usuario[1].equals(usuarioId)) {
                    usuarioExiste = true;
                    break;
                }
            }

            if (!usuarioExiste) {
                logger.warning("Usuario no encontrado: " + usuarioId);
                return false;
            }

            // Verificar disponibilidad del libro
            for (String[] libro : libros) {
                if (libro[0].equals(tituloLibro)) {
                    int copias = Integer.parseInt(libro[2]);
                    if (copias > 0) {
                        libro[2] = String.valueOf(copias - 1);
                        prestamos.add(new String[] { usuarioId, tituloLibro, new Date().toString() });
                        System.out.println("Préstamo realizado exitosamente");
                        return true;
                    }
                }
            }

            logger.warning("Libro no disponible: " + tituloLibro);
            return false;
        }

        public boolean devolverLibro(String usuarioId, String tituloLibro) {
            logger.info("Procesando devolución: " + tituloLibro + " del usuario " + usuarioId);

            // Buscar el préstamo
            for (int i = 0; i < prestamos.size(); i++) {
                String[] prestamo = prestamos.get(i);
                if (prestamo[0].equals(usuarioId) && prestamo[1].equals(tituloLibro)) {
                    prestamos.remove(i);

                    // Aumentar copias disponibles
                    for (String[] libro : libros) {
                        if (libro[0].equals(tituloLibro)) {
                            int copias = Integer.parseInt(libro[2]);
                            libro[2] = String.valueOf(copias + 1);
                            break;
                        }
                    }
                    System.out.println("Devolución realizada exitosamente");
                    return true;
                }
            }

            logger.warning("Préstamo no encontrado para devolución");
            return false;
        }
    }

    // ==========================================================================
    // 2. REFACTORIZACIÓN SIGUIENDO SRP
    // ==========================================================================

    // Clase para representar un Libro
    static class Libro {
        private String titulo;
        private String autor;
        private int copiasDisponibles;

        public Libro(String titulo, String autor, int copiasDisponibles) {
            this.titulo = titulo;
            this.autor = autor;
            this.copiasDisponibles = copiasDisponibles;
        }

        // Getters y setters
        public String getTitulo() {
            return titulo;
        }

        public String getAutor() {
            return autor;
        }

        public int getCopiasDisponibles() {
            return copiasDisponibles;
        }

        public void setCopiasDisponibles(int copias) {
            this.copiasDisponibles = copias;
        }

        @Override
        public String toString() {
            return String.format("Libro{titulo='%s', autor='%s', copias=%d}",
                    titulo, autor, copiasDisponibles);
        }
    }

    // Clase para representar un Usuario
    static class Usuario {
        private String nombre;
        private String id;
        private String email;

        public Usuario(String nombre, String id, String email) {
            this.nombre = nombre;
            this.id = id;
            this.email = email;
        }

        // Getters
        public String getNombre() {
            return nombre;
        }

        public String getId() {
            return id;
        }

        public String getEmail() {
            return email;
        }

        @Override
        public String toString() {
            return String.format("Usuario{nombre='%s', id='%s', email='%s'}",
                    nombre, id, email);
        }
    }

    // Clase para representar un Préstamo
    static class Prestamo {
        private String usuarioId;
        private String tituloLibro;
        private Date fechaPrestamo;

        public Prestamo(String usuarioId, String tituloLibro) {
            this.usuarioId = usuarioId;
            this.tituloLibro = tituloLibro;
            this.fechaPrestamo = new Date();
        }

        // Getters
        public String getUsuarioId() {
            return usuarioId;
        }

        public String getTituloLibro() {
            return tituloLibro;
        }

        public Date getFechaPrestamo() {
            return fechaPrestamo;
        }

        @Override
        public String toString() {
            return String.format("Prestamo{usuarioId='%s', libro='%s', fecha=%s}",
                    usuarioId, tituloLibro, fechaPrestamo);
        }
    }

    // Responsabilidad 1: Gestión de Libros
    static class GestorLibros {
        private List<Libro> libros;
        private Logger logger;

        public GestorLibros() {
            this.libros = new ArrayList<>();
            this.logger = Logger.getLogger(GestorLibros.class.getName());
        }

        public void registrarLibro(String titulo, String autor, int copias) {
            logger.info("Registrando libro: " + titulo);
            Libro nuevoLibro = new Libro(titulo, autor, copias);
            libros.add(nuevoLibro);
            System.out.println("Libro registrado: " + nuevoLibro);
        }

        public Libro buscarLibro(String titulo) {
            for (Libro libro : libros) {
                if (libro.getTitulo().equalsIgnoreCase(titulo)) {
                    return libro;
                }
            }
            return null;
        }

        public void mostrarLibros() {
            logger.info("Mostrando todos los libros");
            System.out.println("=== Libros Disponibles ===");
            for (Libro libro : libros) {
                System.out.println(libro);
            }
        }

        public List<Libro> getLibros() {
            return new ArrayList<>(libros);
        }
    }

    // Responsabilidad 2: Gestión de Usuarios
    static class GestorUsuarios {
        private List<Usuario> usuarios;
        private Logger logger;

        public GestorUsuarios() {
            this.usuarios = new ArrayList<>();
            this.logger = Logger.getLogger(GestorUsuarios.class.getName());
        }

        public void registrarUsuario(String nombre, String id, String email) {
            logger.info("Registrando usuario: " + nombre);
            Usuario nuevoUsuario = new Usuario(nombre, id, email);
            usuarios.add(nuevoUsuario);
            System.out.println("Usuario registrado: " + nuevoUsuario);
        }

        public Usuario buscarUsuario(String id) {
            for (Usuario usuario : usuarios) {
                if (usuario.getId().equals(id)) {
                    return usuario;
                }
            }
            return null;
        }

        public void mostrarUsuarios() {
            logger.info("Mostrando todos los usuarios");
            System.out.println("=== Usuarios Registrados ===");
            for (Usuario usuario : usuarios) {
                System.out.println(usuario);
            }
        }
    }

    // Responsabilidad 3: Gestión de Préstamos
    static class GestorPrestamos {
        private List<Prestamo> prestamos;
        private Logger logger;

        public GestorPrestamos() {
            this.prestamos = new ArrayList<>();
            this.logger = Logger.getLogger(GestorPrestamos.class.getName());
        }

        public boolean prestarLibro(Usuario usuario, Libro libro) {
            logger.info("Procesando préstamo: " + libro.getTitulo() + " para " + usuario.getNombre());

            if (libro.getCopiasDisponibles() > 0) {
                libro.setCopiasDisponibles(libro.getCopiasDisponibles() - 1);
                Prestamo nuevoPrestamo = new Prestamo(usuario.getId(), libro.getTitulo());
                prestamos.add(nuevoPrestamo);
                System.out.println("Préstamo realizado exitosamente: " + nuevoPrestamo);
                return true;
            } else {
                logger.warning("Libro no disponible: " + libro.getTitulo());
                System.out.println("No hay copias disponibles del libro: " + libro.getTitulo());
                return false;
            }
        }

        public boolean devolverLibro(String usuarioId, String tituloLibro, Libro libro) {
            logger.info("Procesando devolución: " + tituloLibro + " del usuario " + usuarioId);

            for (int i = 0; i < prestamos.size(); i++) {
                Prestamo prestamo = prestamos.get(i);
                if (prestamo.getUsuarioId().equals(usuarioId) &&
                        prestamo.getTituloLibro().equalsIgnoreCase(tituloLibro)) {
                    prestamos.remove(i);
                    libro.setCopiasDisponibles(libro.getCopiasDisponibles() + 1);
                    System.out.println("Devolución realizada exitosamente");
                    return true;
                }
            }

            logger.warning("Préstamo no encontrado para devolución");
            System.out.println("No se encontró el préstamo para devolución");
            return false;
        }

        public void mostrarPrestamos() {
            System.out.println("=== Préstamos Activos ===");
            for (Prestamo prestamo : prestamos) {
                System.out.println(prestamo);
            }
        }
    }

    // Clase coordinadora que usa los gestores especializados
    static class SistemaBiblioteca {
        private GestorLibros gestorLibros;
        private GestorUsuarios gestorUsuarios;
        private GestorPrestamos gestorPrestamos;
        private Logger logger;

        public SistemaBiblioteca() {
            this.gestorLibros = new GestorLibros();
            this.gestorUsuarios = new GestorUsuarios();
            this.gestorPrestamos = new GestorPrestamos();
            this.logger = Logger.getLogger(SistemaBiblioteca.class.getName());
        }

        public void registrarLibro(String titulo, String autor, int copias) {
            gestorLibros.registrarLibro(titulo, autor, copias);
        }

        public void registrarUsuario(String nombre, String id, String email) {
            gestorUsuarios.registrarUsuario(nombre, id, email);
        }

        public boolean prestarLibro(String usuarioId, String tituloLibro) {
            Usuario usuario = gestorUsuarios.buscarUsuario(usuarioId);
            if (usuario == null) {
                System.out.println("Usuario no encontrado");
                return false;
            }

            Libro libro = gestorLibros.buscarLibro(tituloLibro);
            if (libro == null) {
                System.out.println("Libro no encontrado");
                return false;
            }

            return gestorPrestamos.prestarLibro(usuario, libro);
        }

        public boolean devolverLibro(String usuarioId, String tituloLibro) {
            Libro libro = gestorLibros.buscarLibro(tituloLibro);
            if (libro == null) {
                System.out.println("Libro no encontrado");
                return false;
            }

            return gestorPrestamos.devolverLibro(usuarioId, tituloLibro, libro);
        }

        public void mostrarTodo() {
            gestorLibros.mostrarLibros();
            System.out.println();
            gestorUsuarios.mostrarUsuarios();
            System.out.println();
            gestorPrestamos.mostrarPrestamos();
        }
    }

    public static void main(String[] args) {
        // Configurar logging
        Logger.getLogger("").setLevel(Level.INFO);

        System.out.println("=== DEMOSTRACIÓN: CLASE QUE VIOLA SRP ===");
        LibraryViolaSRP bibliotecaMala = new LibraryViolaSRP();

        bibliotecaMala.registrarLibro("El Quijote", "Cervantes", 3);
        bibliotecaMala.registrarUsuario("Ana Laura", "001", "ana@email.com");
        bibliotecaMala.prestarLibro("001", "El Quijote");
        bibliotecaMala.mostrarLibros();

        System.out.println("\n" + "=".repeat(50));
        System.out.println("=== DEMOSTRACIÓN: REFACTORIZACIÓN CON SRP ===");

        SistemaBiblioteca sistema = new SistemaBiblioteca();

        // Registrar datos
        sistema.registrarLibro("Cien años de soledad", "Gabriel García Márquez", 2);
        sistema.registrarLibro("1984", "George Orwell", 1);
        sistema.registrarUsuario("Ana Laura", "001", "ana@email.com");
        sistema.registrarUsuario("Carlos", "002", "carlos@email.com");

        // Realizar préstamos
        sistema.prestarLibro("001", "1984");
        sistema.prestarLibro("002", "Cien años de soledad");

        // Mostrar estado actual
        System.out.println("\n=== Estado actual del sistema ===");
        sistema.mostrarTodo();

        // Devolver un libro
        System.out.println("\n=== Devolución ===");
        sistema.devolverLibro("001", "1984");

        System.out.println("\n=== Estado final ===");
        sistema.mostrarTodo();
    }
}
