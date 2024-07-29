package com.example.headfirstjava;

import org.springframework.boot.SpringApplication;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Natalinacn {

    public static void main(String[] args) {
        SpringApplication.run(HeadFirstjavaApplication.class, args);

        imprimirMensaje();
        imprimirNombre("Natalin");
        sumarNumeros(2, 5);
        System.out.println(saludar());
        System.out.println(cuadrado(5));
        System.out.println(multiplicar(8, 2));

        //EJEMPLO DE FUNCIONES YA CREADAS EN EL LENGUAJE
        //1-Funciones de la clase Math
        double numEjemplo = 123.45;
        System.out.println("Valor absoluto " + numEjemplo + ": " + Math.abs(numEjemplo));
        System.out.println("Raíz cuadrada de 16: " + Math.sqrt(16));
        System.out.println("Máximo entre 10 y 20: " + Math.max(10, 20));
        System.out.println("Mínimo entre 10 y 20: " + Math.min(10, 20));
        System.out.println("Número aleatorio entre 0.0 y 1.0: " + Math.random());

        //2-Funciones de la clase String
        String texto = "Hola Mundo";
        System.out.println("Texto en minúsculas: " + texto.toLowerCase());
        System.out.println("Texto en mayúsculas: " + texto.toUpperCase());
        System.out.println("Longitud del texto: " + texto.length());
        System.out.println("Caracter en la posición 5: " + texto.charAt(4));
        System.out.println("Reemplazar 'Mundo' con 'Java': " + texto.replace("Mundo", "Java"));

        //3-Funciones de la clase Arrays
        int[] numerosArray = {5, 3, 8, 2, 9, 1};

        // Ordenar el arreglo: sort(int[] a): Ordena el arreglo en orden ascendente.
        Arrays.sort(numerosArray);
        System.out.println("Arreglo ordenado: " + Arrays.toString(numerosArray));

        // Buscar un elemento en el arreglo: binarySearch(int[] a, int key): Busca el elemento especificado en el arreglo ordenado y devuelve el índice de la búsqueda binaria.
        int indice = Arrays.binarySearch(numerosArray, 8);
        System.out.println("Índice del elemento 8: " + indice);

        // Rellenar el arreglo: fill(int[] a, int val): Asigna el valor especificado a cada elemento del arreglo.
        Arrays.fill(numerosArray, 7);
        System.out.println("Arreglo rellenado con 7: " + Arrays.toString(numerosArray));

        //4- Funciones de la clase Collections: La clase Collections proporciona métodos estáticos que operan en colecciones como listas, conjuntos y mapas.
        List<String> lista = new ArrayList<>();
        lista.add("Banana");
        lista.add("Manzana");
        lista.add("Pera");
        lista.add("Naranja");

        // Ordenar la lista
        Collections.sort(lista);
        System.out.println("Lista ordenada: " + lista);

        // Barajar la lista
        Collections.shuffle(lista);
        System.out.println("Lista barajada: " + lista);

        // Encontrar el elemento máximo
        String maximo = Collections.max(lista);
        System.out.println("Elemento máximo: " + maximo);

        // Encontrar el elemento mínimo
        String minimo = Collections.min(lista);
        System.out.println("Elemento mínimo: " + minimo);

        Natalinacn variables = new Natalinacn();
        variables.metodoConVariablesLocales();
        variables.imprimirMensajeGlobal();

        funcionExtra("Múltiplo de 3 ", "Múltiplo de 5");

    }

    //#02 FUNCIONES Y ALCANCE

    //1. Función sin parámetros y sin retorno
    public static void imprimirMensaje(){
        System.out.println("Hola, este es un mensaje sin parámetros ni retorno.");
    }

    //2. Función con un parámetro y sin retorno
    public static void imprimirNombre(String nombre){
        System.out.println("Bienvenida " + nombre);
    }

    //3. Función con varios parámetros y sin retorno
    public static void sumarNumeros(int num1, int num2){
        System.out.println("La suma de los números es " + num1 + num2);
    }

    //4. Función sin parámetros y con retorno
    public static String saludar(){
        return "Buenas tardes!!";
    }

    //5. Función con un parámetro y con retorno
    public static int cuadrado(int numero){
        return numero * numero;
    }

    //6. Función con varios parámetros y con retorno
    public static int multiplicar(int num1, int num2){
        return num1 * num2;
    }

    //Funcion dentro de otra función
    //En Java no es posible definir una función (método) dentro de otra función directamente.
    //Todos los métodos deben ser definidos al mismo nivel de clase.
    //Si necesitas definir una función dentro de otra, puedes hacerlo indirectamente utilizando clases internas,
    // clases anónimas, o expresiones lambda en ciertos contextos.
    public static void funcionDentroDeFuncion() {
        System.out.println("Probando si se puede crear una función dentro de otra a continuación...");

        class FuncionAdentro {
            void mensaje() {
                System.out.println("No se puede crear una función dentro de otra directamente.");
            }
        }

        FuncionAdentro funcionAdentro = new FuncionAdentro();
        funcionAdentro.mensaje();



    }

    // VARIABLE LOCAL y GLOBAL
    //En Java Las variables locales son aquellas que se declaran dentro de un método y solo son accesibles dentro de ese método. No pueden ser accedidas fuera del método en el que se declararon.
    //Variables de instancia (similares a variables globales) se declaran dentro de una clase pero fuera de cualquier método. Son accesibles por todos los métodos de la clase y su valor puede ser cambiado por cualquier método de la clase.

    // Variable de instancia (similar a una variable global)
    private String mensajeGlobal = "Este es un mensaje global.";

    // Método que imprime la variable global
    public void imprimirMensajeGlobal() {
        System.out.println(mensajeGlobal);
    }

    // Método que contiene variables locales
    public void metodoConVariablesLocales() {
        // Variable local
        String mensajeLocal = "Este es un mensaje local.";

        System.out.println(mensajeLocal);

        // Intentar acceder a una variable global
        System.out.println("Intentar acceder a una variable global: " + mensajeGlobal);
    }



    //DIFICULTAD EXTRA (opcional):
    // * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    // * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    // *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    // *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    // *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    // *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

    public static int funcionExtra(String param1, String param2){

        int contador = 0;
        for (int i = 1; i < 101; i++) {
            if(i % 3 == 0 && i % 5 == 0){
                System.out.println(i +" es " + param1 + param2);
            }else if(i % 3 == 0){
                System.out.println(i + " es " +param1);
            }else if(i % 5 == 0){
                System.out.println(i +" es " + param2);
            }else{
                contador++;
            }
        }
        System.out.println("El número de veces que se ha impreso el número en lugar de los textos es de " + contador);
        return contador;
    }
}