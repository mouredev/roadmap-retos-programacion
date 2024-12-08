/*
 * TEORÍA DE DECORADORES (ANOTACIONES) EN JAVA
 * 
 * En Java, los decoradores se llaman "anotaciones" y se definen usando @interface.
 * Las anotaciones permiten añadir metadatos a:
 * - Clases
 * - Métodos
 * - Campos
 * - Parámetros
 * 
 * Características principales:
 * - Se definen con @interface
 * - Pueden tener elementos con valores por defecto
 * - Se procesan en tiempo de compilación o ejecución
 * - Se pueden consultar mediante Reflection
 */

import java.lang.annotation.*;
import java.lang.reflect.*;

// Definición del decorador para clases
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@interface LogClass {
    String value() default ""; // Mensaje personalizado
}

// Definición del decorador para métodos
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface LogMethod {
    String value() default ""; // Mensaje personalizado
}

// Definición del decorador contador para el ejercicio extra
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface ContadorLlamadas {
}

public class eulogioep {
    // Clase principal que contiene el método main
    public static void main(String[] args) {
        try {
            System.out.println("=== Pruebas de los decoradores ===");

            // Prueba del decorador de clase
            Ejemplo ejemplo = new Ejemplo();
            procesarDecoradoresClase(ejemplo.getClass());

            // Prueba del decorador de método
            ejemplo.saludar("Java");

            // Prueba del decorador contador
            Calculadora calc = new Calculadora();
            System.out.println("Resultado suma: " + calc.sumar(5, 3));        // Primera llamada
            System.out.println("Resultado suma: " + calc.sumar(2, 4));        // Segunda llamada
            System.out.println("Resultado multiplicación: " + calc.multiplicar(3, 4));  // Primera llamada
            System.out.println("Resultado suma: " + calc.sumar(1, 1));        // Tercera llamada

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Clase de ejemplo con decoradores
    @LogClass("Esta es una clase de ejemplo")
    static class Ejemplo {
        @LogMethod("Método de saludo")
        public String saludar(String nombre) {
            return "¡Hola " + nombre + "!";
        }
    }

    // Clase Calculadora con el decorador contador
    static class Calculadora {
        private static java.util.Map<String, Integer> contadores = new java.util.HashMap<>();

        @ContadorLlamadas
        public int sumar(int a, int b) {
            contarLlamada("sumar");
            return a + b;
        }

        @ContadorLlamadas
        public int multiplicar(int a, int b) {
            contarLlamada("multiplicar");
            return a * b;
        }

        private void contarLlamada(String metodo) {
            int contador = contadores.getOrDefault(metodo, 0) + 1;
            contadores.put(metodo, contador);
            System.out.println("El método " + metodo + " ha sido llamado " + contador + " veces");
        }
    }

    // Método para procesar decoradores de clase
    private static void procesarDecoradoresClase(Class<?> clase) {
        if (clase.isAnnotationPresent(LogClass.class)) {
            LogClass anotacion = clase.getAnnotation(LogClass.class);
            System.out.println("Clase creada: " + clase.getSimpleName() + 
                             " - Mensaje: " + anotacion.value());
        }
    }

    // Método para procesar decoradores de método
    private static void procesarDecoradoresMetodo(Method metodo) {
        if (metodo.isAnnotationPresent(LogMethod.class)) {
            LogMethod anotacion = metodo.getAnnotation(LogMethod.class);
            System.out.println("Método llamado: " + metodo.getName() + 
                             " - Mensaje: " + anotacion.value());
        }
    }

    // Procesador de aspectos (simulado con Reflection)
    static {
        // Interceptamos los métodos con decoradores usando Reflection
        try {
            Method[] metodos = Ejemplo.class.getDeclaredMethods();
            for (Method metodo : metodos) {
                if (metodo.isAnnotationPresent(LogMethod.class)) {
                    // Aquí normalmente usaríamos un framework como AspectJ
                    // Esta es una simulación simplificada
                    procesarDecoradoresMetodo(metodo);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}