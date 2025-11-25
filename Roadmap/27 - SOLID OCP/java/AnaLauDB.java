import java.util.*;

public class AnaLauDB {

    // ==========================================================================
    // IMPLEMENTACIÓN QUE CUMPLE EL PRINCIPIO ABIERTO/CERRADO (OCP)
    // ==========================================================================

    // Interfaz que define el contrato para las operaciones
    interface Operacion {
        double calcular(double a, double b);

        String getNombre();

        String getSimbolo();
    }

    // Implementación de la operación Suma
    static class Suma implements Operacion {
        @Override
        public double calcular(double a, double b) {
            return a + b;
        }

        @Override
        public String getNombre() {
            return "Suma";
        }

        @Override
        public String getSimbolo() {
            return "+";
        }
    }

    // Implementación de la operación Resta
    static class Resta implements Operacion {
        @Override
        public double calcular(double a, double b) {
            return a - b;
        }

        @Override
        public String getNombre() {
            return "Resta";
        }

        @Override
        public String getSimbolo() {
            return "-";
        }
    }

    // Implementación de la operación Multiplicación
    static class Multiplicacion implements Operacion {
        @Override
        public double calcular(double a, double b) {
            return a * b;
        }

        @Override
        public String getNombre() {
            return "Multiplicación";
        }

        @Override
        public String getSimbolo() {
            return "*";
        }
    }

    // Implementación de la operación División
    static class Division implements Operacion {
        @Override
        public double calcular(double a, double b) {
            if (b == 0) {
                throw new ArithmeticException("No se puede dividir por cero");
            }
            return a / b;
        }

        @Override
        public String getNombre() {
            return "División";
        }

        @Override
        public String getSimbolo() {
            return "/";
        }
    }

    // ==========================================================================
    // NUEVA OPERACIÓN AGREGADA SIN MODIFICAR CÓDIGO EXISTENTE (OCP)
    // ==========================================================================

    // Implementación de la operación Potencia - NUEVA OPERACIÓN
    static class Potencia implements Operacion {
        @Override
        public double calcular(double a, double b) {
            return Math.pow(a, b);
        }

        @Override
        public String getNombre() {
            return "Potencia";
        }

        @Override
        public String getSimbolo() {
            return "^";
        }
    }

    // Calculadora que utiliza las operaciones - CERRADA PARA MODIFICACIÓN
    static class Calculadora {
        private Map<String, Operacion> operaciones;

        public Calculadora() {
            this.operaciones = new HashMap<>();
        }

        // Método para registrar nuevas operaciones - ABIERTA PARA EXTENSIÓN
        public void registrarOperacion(String codigo, Operacion operacion) {
            operaciones.put(codigo.toLowerCase(), operacion);
            System.out.println("Operación registrada: " + operacion.getNombre() +
                    " (" + operacion.getSimbolo() + ")");
        }

        // Método para realizar cálculos
        public double calcular(String tipoOperacion, double a, double b) {
            Operacion operacion = operaciones.get(tipoOperacion.toLowerCase());

            if (operacion == null) {
                throw new IllegalArgumentException("Operación no soportada: " + tipoOperacion);
            }

            double resultado = operacion.calcular(a, b);
            System.out.printf("%.2f %s %.2f = %.2f%n",
                    a, operacion.getSimbolo(), b, resultado);

            return resultado;
        }

        // Método para mostrar operaciones disponibles
        public void mostrarOperacionesDisponibles() {
            System.out.println("\n=== Operaciones Disponibles ===");
            for (Map.Entry<String, Operacion> entry : operaciones.entrySet()) {
                Operacion op = entry.getValue();
                System.out.printf("Código: '%s' - %s (%s)%n",
                        entry.getKey(), op.getNombre(), op.getSimbolo());
            }
            System.out.println();
        }
    }

    // ==========================================================================
    // EJEMPLO DE EXTENSIBILIDAD - OPERACIONES ADICIONALES
    // ==========================================================================

    // Operación de módulo - OTRA NUEVA OPERACIÓN
    static class Modulo implements Operacion {
        @Override
        public double calcular(double a, double b) {
            if (b == 0) {
                throw new ArithmeticException("No se puede calcular módulo con divisor cero");
            }
            return a % b;
        }

        @Override
        public String getNombre() {
            return "Módulo";
        }

        @Override
        public String getSimbolo() {
            return "%";
        }
    }

    // Operación de raíz cuadrada - OPERACIÓN UNARIA (usa solo el primer parámetro)
    static class RaizCuadrada implements Operacion {
        @Override
        public double calcular(double a, double b) {
            // Ignora el segundo parámetro para operaciones unarias
            if (a < 0) {
                throw new ArithmeticException("No se puede calcular raíz cuadrada de número negativo");
            }
            return Math.sqrt(a);
        }

        @Override
        public String getNombre() {
            return "Raíz Cuadrada";
        }

        @Override
        public String getSimbolo() {
            return "√";
        }
    }

    public static void main(String[] args) {
        System.out.println("=== DEMOSTRACIÓN DEL PRINCIPIO ABIERTO/CERRADO (OCP) ===");

        // Crear calculadora
        Calculadora calc = new Calculadora();

        // 1. Implementar las operaciones básicas
        System.out.println("1. Registrando operaciones básicas:");
        calc.registrarOperacion("suma", new Suma());
        calc.registrarOperacion("resta", new Resta());
        calc.registrarOperacion("multiplicacion", new Multiplicacion());
        calc.registrarOperacion("division", new Division());

        // 2. Comprobar que el sistema funciona
        System.out.println("\n2. Probando operaciones básicas:");
        calc.mostrarOperacionesDisponibles();

        try {
            calc.calcular("suma", 10, 5);
            calc.calcular("resta", 10, 5);
            calc.calcular("multiplicacion", 10, 5);
            calc.calcular("division", 10, 5);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        // 3. Agregar quinta operación (Potencia) SIN MODIFICAR código existente
        System.out.println("\n3. Agregando nueva operación (Potencia) - SIN MODIFICAR código existente:");
        calc.registrarOperacion("potencia", new Potencia());

        // 4. Comprobar que se cumple el OCP
        System.out.println("\n4. Verificando OCP - La calculadora ahora soporta potencias:");
        calc.mostrarOperacionesDisponibles();

        try {
            calc.calcular("potencia", 2, 3); // 2^3 = 8
            calc.calcular("potencia", 5, 2); // 5^2 = 25
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        // Demostrar extensibilidad adicional
        System.out.println("\n5. Demostrando extensibilidad adicional:");
        calc.registrarOperacion("modulo", new Modulo());
        calc.registrarOperacion("raiz", new RaizCuadrada());

        calc.mostrarOperacionesDisponibles();

        try {
            calc.calcular("modulo", 10, 3); // 10 % 3 = 1
            calc.calcular("raiz", 16, 0); // √16 = 4 (ignora segundo parámetro)
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        // Demostrar manejo de errores
        System.out.println("\n6. Demostrando manejo de errores:");
        try {
            calc.calcular("division", 10, 0); // Error: división por cero
        } catch (Exception e) {
            System.out.println("Error capturado: " + e.getMessage());
        }

        try {
            calc.calcular("raiz", -4, 0); // Error: raíz de número negativo
        } catch (Exception e) {
            System.out.println("Error capturado: " + e.getMessage());
        }

        System.out.println("\n=== CONCLUSIÓN ===");
        System.out.println("El sistema cumple el OCP porque:");
        System.out.println("   - CERRADO para modificación: No modificamos la clase Calculadora");
        System.out.println("   - ABIERTO para extensión: Agregamos nuevas operaciones fácilmente");
        System.out.println("   - Cada nueva operación implementa la interfaz Operacion");
        System.out.println("   - El comportamiento se extiende sin romper código existente");
    }
}
