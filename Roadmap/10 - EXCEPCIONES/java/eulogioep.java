// Archivo: eulogioep.java

import java.util.ArrayList;
import java.util.List;

public class eulogioep {
    public static void main(String[] args) {
        // Parte 1: Manejo básico de excepciones
        try {
            // Intentamos dividir por cero para forzar una excepción
            int resultado = 10 / 0;
        } catch (ArithmeticException e) {
            // Capturamos la excepción y la imprimimos
            System.out.println("Error aritmético: " + e.getMessage());
        }

        try {
            // Intentamos acceder a un índice no existente de una lista
            List<String> lista = new ArrayList<>();
            lista.add("Elemento");
            String elemento = lista.get(5); // Esto lanzará una excepción
        } catch (IndexOutOfBoundsException e) {
            // Capturamos la excepción y la imprimimos
            System.out.println("Error de índice: " + e.getMessage());
        }

        // Parte 2: Función con múltiples excepciones (DIFICULTAD EXTRA)
        try {
            procesarParametro(0); // Probamos con diferentes valores: -1, 0, 5, 15
            System.out.println("No se ha producido ningún error.");
        } catch (miExcepcionPersonalizada e) {
            System.out.println("Tipo de error: miExcepcionPersonalizada");
            System.out.println("Mensaje: " + e.getMessage());
        } catch (IllegalArgumentException e) {
            System.out.println("Tipo de error: IllegalArgumentException");
            System.out.println("Mensaje: " + e.getMessage());
        } catch (ArithmeticException e) {
            System.out.println("Tipo de error: ArithmeticException");
            System.out.println("Mensaje: " + e.getMessage());
        } finally {
            System.out.println("La ejecución ha finalizado.");
        }
    }

    // Función que puede lanzar 3 tipos diferentes de excepciones
    public static void procesarParametro(int parametro) throws miExcepcionPersonalizada {
        if (parametro < 0) {
            throw new IllegalArgumentException("El parámetro no puede ser negativo");
        } else if (parametro == 0) {
            throw new ArithmeticException("No se puede dividir por cero");
        } else if (parametro > 10) {
            throw new miExcepcionPersonalizada("El parámetro es demasiado grande");
        }

        // Si no hay errores, realizamos alguna operación
        int resultado = 100 / parametro;
        System.out.println("Resultado: " + resultado);
    }
}

// Definición de nuestra excepción personalizada
class miExcepcionPersonalizada extends Exception {
    public miExcepcionPersonalizada(String mensaje) {
        super(mensaje);
    }
}