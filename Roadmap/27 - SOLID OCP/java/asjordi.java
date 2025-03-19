/*
    El Principio Abierto/Cerrado (OCP) establece que una clase debe estar abierta para extensión, pero cerrada para modificación.
    Modificación significa cambiar el código de una clase ya existente, mientras que extensión significa agregar nuevas funcionalidades.
    Por lo general, esto se realizará con interfaces y clases abstractas.
 */

import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        Calculadora calculadora = new Calculadora();
        calculadora.agregarOperacion("suma", new Suma());
        calculadora.agregarOperacion("resta", new Resta());
        calculadora.agregarOperacion("multiplicacion", new Multiplicacion());
        calculadora.agregarOperacion("division", new Division());
        calculadora.agregarOperacion("potencia", new Potencia());

        System.out.println(calculadora.ejecutarOperacion("suma", 5, 3));
        System.out.println(calculadora.ejecutarOperacion("resta", 5, 3));
        System.out.println(calculadora.ejecutarOperacion("multiplicacion", 5, 3));
        System.out.println(calculadora.ejecutarOperacion("division", 5, 3));
        System.out.println(calculadora.ejecutarOperacion("potencia", 5, 3));
    }

    /*
        EJERCICIO:
        Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
        y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
     */
    static class Factura {
        // Atributos
        // Constructor
        // Métodos
    }

    static class FacturaPersistencia {
        Factura factura;

        public FacturaPersistencia(Factura factura) {
            this.factura = factura;
        }

        public void guardarEnArchivo(String nombre) {
            // Guardar la factura en un archivo con el nombre especificado
        }

        public void guardarEnBaseDeDatos() {
            // Guardar la factura en la base de datos
        }
    }

    /*
        Aplicando el Principio Abierto/Cerrado (OCP) se puede crear una interfaz IFacturaPersistencia con un método guardar(Factura factura)
        y dos clases que implementen esta interfaz, una para guardar en la base de datos y otra para guardar en un archivo.
        De esta forma, si se quiere agregar una nueva forma de persistencia, se puede crear una nueva clase que implemente la interfaz
        sin tener que modificar las clases existentes.
        Incluso, crear una clase que administre diferentes formas de persistencia, como se muestra en el ejemplo.
     */
    interface IFacturaPersistencia {
        void guardar(Factura factura);
    }

    interface ILibroPersistencia {
        void guardar(Factura factura);
    }

    static class BaseDeDatosPersistencia implements IFacturaPersistencia {
        @Override
        public void guardar(Factura factura) {
            // Guardar la factura en la base de datos
        }
    }

    public class ArchivoPersistencia implements IFacturaPersistencia {
        @Override
        public void guardar(Factura factura) {
            // Guardar la factura en un archivo con el nombre especificado
        }
    }

    static class AdministradorPersistencia {
        IFacturaPersistencia facturaPersistencia;
        ILibroPersistencia libroPersistencia;

        public AdministradorPersistencia(IFacturaPersistencia facturaPersistencia, ILibroPersistencia libroPersistencia) {
            this.facturaPersistencia = facturaPersistencia;
            this.libroPersistencia = libroPersistencia;
        }
    }

    /*
        DIFICULTAD EXTRA (opcional):
        Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
        Requisitos:
        - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
        Instrucciones:
        1. Implementa las operaciones de suma, resta, multiplicación y división.
        2. Comprueba que el sistema funciona.
        3. Agrega una quinta operación para calcular potencias.
        4. Comprueba que se cumple el OCP.
     */

    interface IOperacion {
        double calcular(double a, double b);
    }

    static class Suma implements IOperacion {
        @Override
        public double calcular(double a, double b) {
            return a + b;
        }
    }

    static class Resta implements IOperacion {
        @Override
        public double calcular(double a, double b) {
            return a - b;
        }
    }

    static class Multiplicacion implements IOperacion {
        @Override
        public double calcular(double a, double b) {
            return a * b;
        }
    }

    static class Division implements IOperacion {
        @Override
        public double calcular(double a, double b) {
            if (b == 0) throw new IllegalArgumentException("No se puede dividir por cero");
            return a / b;
        }
    }

    static class Potencia implements IOperacion {
        @Override
        public double calcular(double a, double b) {
            return Math.pow(a, b);
        }
    }

    static class Calculadora {
        private Map<String, IOperacion> operaciones;

        public Calculadora() {
            this.operaciones = new HashMap<>();
        }

        public void agregarOperacion(String nombre, IOperacion operacion) {
            if (!this.operaciones.containsKey(nombre)) this.operaciones.put(nombre, operacion);
            else throw new IllegalArgumentException("La operación ya existe");
        }

        public double ejecutarOperacion(String nombre, double a, double b) {
            IOperacion op = this.operaciones.get(nombre);
            if (op == null) throw new IllegalArgumentException("Operación no encontrada");
            return op.calcular(a, b);
        }
    }

}
