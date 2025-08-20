public class AnaLauDB {
    // Variable global (atributo de la clase)
    int contadorGlobal = 0;

    public void incrementarGlobal() {
        contadorGlobal++;
        System.out.println("Contador global: " + contadorGlobal);
    }

    public void ejemploLocal() {
        // Variable local (solo existe dentro de este método)
        int contadorLocal = 0;
        contadorLocal++;
        System.out.println("Contador local: " + contadorLocal);
    }

    public void saludo() {
        System.out.println("¡Hola Ana Laura!");
    }

    // Con un parámetro, sin retorno
    public void mostrarNombre(String nombre) {
        System.out.println("Nombre: " + nombre);
    }

    // Con varios parámetros, sin retorno
    public void mostrarDatos(String nombre, int edad) {
        System.out.println("Nombre: " + nombre + ", Edad: " + edad);
    }

    // Con retorno, sin parámetros
    public int obtenerNumeroFavorito() {
        return 7;
    }

    // Con retorno, con varios parámetros
    public int producto(int num1, int num2) {
        return num1 * num2;
    }

    public static void main(String[] args) {
        AnaLauraDB db = new AnaLauraDB();

        db.saludo();
        db.mostrarNombre("Ana Laura");
        db.mostrarDatos("Ana Laura", 23);

        int favorito = db.obtenerNumeroFavorito();
        System.out.println("Número favorito: " + favorito);

        int result = db.producto(3, 4);
        System.out.println("El resultado de la multiplicación es: " + result);

        // Ejemplo usando funciones de Math
        double raiz = Math.sqrt(16); // Calcula la raíz cuadrada
        System.out.println("Raíz cuadrada de 16: " + raiz);

        int maximo = Math.max(10, 20); // Obtiene el máximo entre dos números
        System.out.println("El máximo entre 10 y 20 es: " + maximo);

        // Ejemplo usando funciones de String
        String texto = "Hola Mundo";
        int longitud = texto.length(); // Obtiene la longitud del texto
        System.out.println("Longitud del texto: " + longitud);

        String mayusculas = texto.toUpperCase(); // Convierte el texto a mayúsculas
        System.out.println("Texto en mayúsculas: " + mayusculas);

        // Si quieres un número aleatorio entre 1 y 10
        int aleatorioEntero = (int) (Math.random() * 10) + 1;
        System.out.println("Número aleatorio entre 1 y 10: " + aleatorioEntero);

        db.incrementarGlobal(); // Imprime: Contador global: 1
        db.incrementarGlobal(); // Imprime: Contador global: 2

        db.ejemploLocal(); // Imprime: Contador local: 1
        db.ejemploLocal(); // Imprime: Contador local: 1 (se reinicia cada vez)

        // Algoritmo FizzBuzz del 1 al 50
        for (int i = 1; i <= 50; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
    }
}
