
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.stream.Collectors;

public class simonguzman {
    public static void main(String[] args) {
        ejercicioPrincipal();
    }

    public static void ejercicioPrincipal(){
        List<Integer> numeros = Arrays.asList(1,2,3,4,5,6,7,8,9,10);
        List<Integer> numerosMultiplicados = multiplicarXDos(numeros);
        List<Integer> numerosPares = filtrarNumerosPares(numerosMultiplicados);
        imprimirNumeros(numerosPares);
        int suma = sumarNumeros(numerosPares);
        System.out.println("Suma de los números pares multiplicados por 2: " + suma);
    }

    public static List<Integer> multiplicarXDos(List<Integer> numeros){
        Function<Integer, Integer> multiplicar = (n) -> n * 2;
        return numeros.stream().map(multiplicar).collect(Collectors.toList());
    }

    public static List<Integer> filtrarNumerosPares(List<Integer> numeros){
        Predicate<Integer> esPar = (n) -> n % 2 == 0;
        return numeros.stream().filter(esPar).collect(Collectors.toList());
    }

    public static int sumarNumeros(List<Integer> numeros){
        Supplier<Integer> sumar = () -> numeros.stream().mapToInt(Integer::intValue).sum();
        return sumar.get();
    }

    public static void imprimirNumeros(List<Integer> numeros){
        Consumer<Integer> imprimir = (n) -> System.out.println("Numero: "+n);
        numeros.forEach(imprimir);
    }
}
