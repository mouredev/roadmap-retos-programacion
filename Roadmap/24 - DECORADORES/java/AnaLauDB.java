public class AnaLauDB {

    // -------------------------------
    // 1. Interfaz base
    // -------------------------------
    interface Bebida {
        String getDescripcion();

        double getPrecio();
    }

    // -------------------------------
    // 2. Clase concreta
    // -------------------------------
    static class Cafe implements Bebida {
        @Override
        public String getDescripcion() {
            return "Café solo";
        }

        @Override
        public double getPrecio() {
            return 20.0;
        }
    }

    // -------------------------------
    // 3. Clase decoradora base
    // -------------------------------
    static abstract class BebidaDecorador implements Bebida {
        protected Bebida bebida;

        public BebidaDecorador(Bebida bebida) {
            this.bebida = bebida;
        }
    }

    // -------------------------------
    // 4. Decorador concreto: Leche
    // -------------------------------
    static class Leche extends BebidaDecorador {
        public Leche(Bebida bebida) {
            super(bebida);
        }

        @Override
        public String getDescripcion() {
            return bebida.getDescripcion() + ", leche";
        }

        @Override
        public double getPrecio() {
            return bebida.getPrecio() + 5.0;
        }
    }

    // -------------------------------
    // 5. Decorador concreto: Chocolate
    // -------------------------------
    static class Chocolate extends BebidaDecorador {
        public Chocolate(Bebida bebida) {
            super(bebida);
        }

        @Override
        public String getDescripcion() {
            return bebida.getDescripcion() + ", chocolate";
        }

        @Override
        public double getPrecio() {
            return bebida.getPrecio() + 7.0;
        }
    }

    // -------------------------------
    // 6. NUEVO: Decorador Contador
    // -------------------------------
    static class ContadorLlamadas extends BebidaDecorador {
        private int contadorGetDescripcion = 0;
        private int contadorGetPrecio = 0;

        public ContadorLlamadas(Bebida bebida) {
            super(bebida);
        }

        @Override
        public String getDescripcion() {
            contadorGetDescripcion++;
            System.out.println("  [Contador] getDescripcion() llamado " + contadorGetDescripcion + " vez(es)");
            return bebida.getDescripcion();
        }

        @Override
        public double getPrecio() {
            contadorGetPrecio++;
            System.out.println("  [Contador] getPrecio() llamado " + contadorGetPrecio + " vez(es)");
            return bebida.getPrecio();
        }

        public void mostrarEstadisticas() {
            System.out.println("\n=== Estadísticas de llamadas ===");
            System.out.println("getDescripcion(): " + contadorGetDescripcion + " llamadas");
            System.out.println("getPrecio(): " + contadorGetPrecio + " llamadas");
        }
    }

    // -------------------------------
    // 7. Programa principal
    // -------------------------------
    public static void main(String[] args) {
        System.out.println("=== Ejemplo básico de Decorador ===");

        // Café simple
        Bebida cafe = new Cafe();

        // Agregar leche (decorador)
        cafe = new Leche(cafe);

        // Agregar chocolate (decorador)
        cafe = new Chocolate(cafe);

        // Resultado final
        System.out.println("Descripción: " + cafe.getDescripcion());
        System.out.println("Precio total: $" + cafe.getPrecio());

        System.out.println("\n=== Ejemplo con Contador de llamadas ===");

        // Café con contador de llamadas
        Bebida cafeConContador = new Cafe();
        cafeConContador = new ContadorLlamadas(cafeConContador);
        cafeConContador = new Leche(cafeConContador);
        cafeConContador = new Chocolate(cafeConContador);

        // Hacer varias llamadas para probar el contador
        System.out.println("Primera llamada:");
        System.out.println("Descripción: " + cafeConContador.getDescripcion());

        System.out.println("\nSegunda llamada:");
        System.out.println("Precio: $" + cafeConContador.getPrecio());

        System.out.println("\nTercera llamada:");
        System.out.println("Descripción: " + cafeConContador.getDescripcion());

        System.out.println("\nCuarta llamada:");
        System.out.println("Precio: $" + cafeConContador.getPrecio());

        // Mostrar estadísticas finales
        if (cafeConContador instanceof ContadorLlamadas) {
            // Necesitamos acceder al decorador contador directamente
            // Para esto, creamos una referencia específica
        }

        // Alternativa: crear el contador en una variable separada
        System.out.println("\n=== Ejemplo con referencia directa al contador ===");
        Bebida cafe2 = new Cafe();
        ContadorLlamadas contador = new ContadorLlamadas(cafe2);
        Bebida cafeCompleto = new Chocolate(new Leche(contador));

        System.out.println("Llamadas de prueba:");
        cafeCompleto.getDescripcion();
        cafeCompleto.getPrecio();
        cafeCompleto.getDescripcion();
        cafeCompleto.getPrecio();
        cafeCompleto.getDescripcion();

        // Mostrar estadísticas
        contador.mostrarEstadisticas();
    }
}
