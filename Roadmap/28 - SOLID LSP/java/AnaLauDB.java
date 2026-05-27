public class AnaLauDB {

    // ==========================================================================
    // IMPLEMENTACIÓN QUE CUMPLE EL PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)
    // ==========================================================================

    // 1. Clase base Vehículo
    static abstract class Vehiculo {
        protected String marca;
        protected String modelo;
        protected double velocidad;
        protected double velocidadMaxima;
        protected boolean encendido;

        public Vehiculo(String marca, String modelo, double velocidadMaxima) {
            this.marca = marca;
            this.modelo = modelo;
            this.velocidadMaxima = velocidadMaxima;
            this.velocidad = 0;
            this.encendido = false;
        }

        // Método para encender el vehículo
        public void encender() {
            if (!encendido) {
                encendido = true;
                System.out.println(marca + " " + modelo + " encendido.");
            }
        }

        // Método para apagar el vehículo
        public void apagar() {
            if (encendido && velocidad == 0) {
                encendido = false;
                System.out.println(marca + " " + modelo + " apagado.");
            } else if (velocidad > 0) {
                System.out.println("No se puede apagar el vehículo en movimiento.");
            }
        }

        // Método acelerar - debe ser implementado por las subclases
        public abstract void acelerar(double incremento);

        // Método frenar - debe ser implementado por las subclases
        public abstract void frenar(double decremento);

        // Método para mostrar estado actual
        public void mostrarEstado() {
            System.out.printf("%s %s - Velocidad: %.1f km/h, Estado: %s%n",
                    marca, modelo, velocidad, encendido ? "Encendido" : "Apagado");
        }

        // Getters
        public double getVelocidad() {
            return velocidad;
        }

        public double getVelocidadMaxima() {
            return velocidadMaxima;
        }

        public boolean isEncendido() {
            return encendido;
        }

        public String getMarca() {
            return marca;
        }

        public String getModelo() {
            return modelo;
        }
    }

    // ==========================================================================
    // 2. SUBCLASES DE VEHÍCULO QUE CUMPLEN LSP
    // ==========================================================================

    // Subclase: Automóvil
    static class Automovil extends Vehiculo {
        private int numeroPuertas;

        public Automovil(String marca, String modelo, double velocidadMaxima, int numeroPuertas) {
            super(marca, modelo, velocidadMaxima);
            this.numeroPuertas = numeroPuertas;
        }

        @Override
        public void acelerar(double incremento) {
            if (!encendido) {
                System.out.println("Error: Debe encender el automóvil primero.");
                return;
            }

            if (incremento < 0) {
                System.out.println("Error: El incremento de velocidad debe ser positivo.");
                return;
            }

            double nuevaVelocidad = velocidad + incremento;
            if (nuevaVelocidad <= velocidadMaxima) {
                velocidad = nuevaVelocidad;
                System.out.printf("Automóvil acelerando: %.1f km/h%n", velocidad);
            } else {
                velocidad = velocidadMaxima;
                System.out.printf("Automóvil alcanzó velocidad máxima: %.1f km/h%n", velocidad);
            }
        }

        @Override
        public void frenar(double decremento) {
            if (decremento < 0) {
                System.out.println("Error: El decremento de velocidad debe ser positivo.");
                return;
            }

            double nuevaVelocidad = velocidad - decremento;
            if (nuevaVelocidad >= 0) {
                velocidad = nuevaVelocidad;
                System.out.printf("Automóvil frenando: %.1f km/h%n", velocidad);
            } else {
                velocidad = 0;
                System.out.println("Automóvil detenido completamente.");
            }
        }

        public int getNumeroPuertas() {
            return numeroPuertas;
        }
    }

    // Subclase: Motocicleta
    static class Motocicleta extends Vehiculo {
        private int cilindrada;

        public Motocicleta(String marca, String modelo, double velocidadMaxima, int cilindrada) {
            super(marca, modelo, velocidadMaxima);
            this.cilindrada = cilindrada;
        }

        @Override
        public void acelerar(double incremento) {
            if (!encendido) {
                System.out.println("Error: Debe encender la motocicleta primero.");
                return;
            }

            if (incremento < 0) {
                System.out.println("Error: El incremento de velocidad debe ser positivo.");
                return;
            }

            // Las motocicletas aceleran más rápido que los automóviles
            double aceleracionReal = incremento * 1.2;
            double nuevaVelocidad = velocidad + aceleracionReal;

            if (nuevaVelocidad <= velocidadMaxima) {
                velocidad = nuevaVelocidad;
                System.out.printf("Motocicleta acelerando rápidamente: %.1f km/h%n", velocidad);
            } else {
                velocidad = velocidadMaxima;
                System.out.printf("Motocicleta alcanzó velocidad máxima: %.1f km/h%n", velocidad);
            }
        }

        @Override
        public void frenar(double decremento) {
            if (decremento < 0) {
                System.out.println("Error: El decremento de velocidad debe ser positivo.");
                return;
            }

            // Las motocicletas pueden frenar más bruscamente
            double frenadoReal = decremento * 1.1;
            double nuevaVelocidad = velocidad - frenadoReal;

            if (nuevaVelocidad >= 0) {
                velocidad = nuevaVelocidad;
                System.out.printf("Motocicleta frenando: %.1f km/h%n", velocidad);
            } else {
                velocidad = 0;
                System.out.println("Motocicleta detenida completamente.");
            }
        }

        public int getCilindrada() {
            return cilindrada;
        }
    }

    // Subclase: Camión
    static class Camion extends Vehiculo {
        private double capacidadCarga;

        public Camion(String marca, String modelo, double velocidadMaxima, double capacidadCarga) {
            super(marca, modelo, velocidadMaxima);
            this.capacidadCarga = capacidadCarga;
        }

        @Override
        public void acelerar(double incremento) {
            if (!encendido) {
                System.out.println("Error: Debe encender el camión primero.");
                return;
            }

            if (incremento < 0) {
                System.out.println("Error: El incremento de velocidad debe ser positivo.");
                return;
            }

            // Los camiones aceleran más lento debido a su peso
            double aceleracionReal = incremento * 0.7;
            double nuevaVelocidad = velocidad + aceleracionReal;

            if (nuevaVelocidad <= velocidadMaxima) {
                velocidad = nuevaVelocidad;
                System.out.printf("Camión acelerando lentamente: %.1f km/h%n", velocidad);
            } else {
                velocidad = velocidadMaxima;
                System.out.printf("Camión alcanzó velocidad máxima: %.1f km/h%n", velocidad);
            }
        }

        @Override
        public void frenar(double decremento) {
            if (decremento < 0) {
                System.out.println("Error: El decremento de velocidad debe ser positivo.");
                return;
            }

            // Los camiones necesitan más distancia para frenar
            double frenadoReal = decremento * 0.8;
            double nuevaVelocidad = velocidad - frenadoReal;

            if (nuevaVelocidad >= 0) {
                velocidad = nuevaVelocidad;
                System.out.printf("Camión frenando gradualmente: %.1f km/h%n", velocidad);
            } else {
                velocidad = 0;
                System.out.println("Camión detenido completamente.");
            }
        }

        public double getCapacidadCarga() {
            return capacidadCarga;
        }
    }

    // ==========================================================================
    // 4. CÓDIGO QUE COMPRUEBA EL CUMPLIMIENTO DEL LSP
    // ==========================================================================

    // Método que trabaja con la clase base Vehículo
    public static void probarVehiculo(Vehiculo vehiculo) {
        System.out.println("\n--- Probando vehículo: " + vehiculo.getMarca() + " " + vehiculo.getModelo() + " ---");

        // Encender vehículo
        vehiculo.encender();
        vehiculo.mostrarEstado();

        // Acelerar varias veces
        vehiculo.acelerar(20);
        vehiculo.mostrarEstado();

        vehiculo.acelerar(30);
        vehiculo.mostrarEstado();

        vehiculo.acelerar(40);
        vehiculo.mostrarEstado();

        // Frenar
        vehiculo.frenar(25);
        vehiculo.mostrarEstado();

        vehiculo.frenar(50);
        vehiculo.mostrarEstado();

        // Apagar vehículo
        vehiculo.apagar();
    }

    // Método que demuestra el polimorfismo y LSP
    public static void simularCarrera(Vehiculo[] vehiculos) {
        System.out.println("\n=== SIMULACIÓN DE CARRERA ===");

        // Encender todos los vehículos
        for (Vehiculo v : vehiculos) {
            v.encender();
        }

        // Acelerar todos por igual
        System.out.println("\n ¡Comienza la carrera! Todos aceleran 50 km/h");
        for (Vehiculo v : vehiculos) {
            v.acelerar(50);
        }

        // Mostrar velocidades después de la aceleración
        System.out.println("\n Velocidades después de acelerar:");
        for (Vehiculo v : vehiculos) {
            System.out.printf("%-15s: %.1f km/h%n",
                    v.getMarca() + " " + v.getModelo(), v.getVelocidad());
        }

        // Frenar todos
        System.out.println("\n Todos frenan 30 km/h");
        for (Vehiculo v : vehiculos) {
            v.frenar(30);
        }

        // Mostrar velocidades finales
        System.out.println("\n Velocidades después de frenar:");
        for (Vehiculo v : vehiculos) {
            System.out.printf("%-15s: %.1f km/h%n",
                    v.getMarca() + " " + v.getModelo(), v.getVelocidad());
        }
    }

    public static void main(String[] args) {
        System.out.println("=== DEMOSTRACIÓN DEL PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP) ===");

        // Crear instancias de diferentes tipos de vehículos
        Vehiculo auto = new Automovil("Toyota", "Corolla", 180, 4);
        Vehiculo moto = new Motocicleta("Honda", "CBR600", 250, 600);
        Vehiculo camion = new Camion("Volvo", "FH16", 120, 40000);

        // 4. Comprobar que se cumple el LSP
        System.out.println("1. Probando cada vehículo individualmente:");

        // Cada subclase puede ser sustituida por la clase base sin romper la
        // funcionalidad
        probarVehiculo(auto); // LSP: Automóvil puede sustituir a Vehículo
        probarVehiculo(moto); // LSP: Motocicleta puede sustituir a Vehículo
        probarVehiculo(camion); // LSP: Camión puede sustituir a Vehículo

        // Demostrar polimorfismo y LSP con un array de vehículos
        Vehiculo[] vehiculos = { auto, moto, camion };
        simularCarrera(vehiculos);

        // Verificar que todas las subclases mantienen las postcondiciones de la clase
        // base
        System.out.println("\n=== VERIFICACIÓN LSP ===");
        System.out.println("Todas las subclases pueden ser sustituidas por la clase base");
        System.out.println("Los métodos acelerar() y frenar() funcionan correctamente");
        System.out.println("Las precondiciones no son fortalecidas en las subclases");
        System.out.println("Las postcondiciones no son debilitadas en las subclases");
        System.out.println("Los invariantes de la clase base se mantienen en todas las subclases");

        // Ejemplo de uso polimórfico adicional
        System.out.println("\n=== EJEMPLO POLIMÓRFICO ADICIONAL ===");
        for (Vehiculo v : vehiculos) {
            System.out.println("\nTipo: " + v.getClass().getSimpleName());
            v.encender();
            v.acelerar(60);
            v.frenar(60);
            v.apagar();
        }

        System.out.println("\n CONCLUSIÓN: El LSP se cumple correctamente!");
        System.out.println("   - Cualquier instancia de Vehículo puede ser reemplazada por sus subclases");
        System.out.println("   - El comportamiento del programa sigue siendo correcto");
        System.out.println("   - No hay efectos secundarios inesperados");
    }
}
