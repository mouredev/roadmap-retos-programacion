import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

public class vandresca {
    public static void main(String[] args) {
       
        //Crear un conjunto de datos
        Set<String> conjuntoDatos = new LinkedHashSet<>();
        conjuntoDatos.add("B");
        conjuntoDatos.add("C");
        conjuntoDatos.add("D");
        conjuntoDatos.add("E");
        conjuntoDatos.add("F");

        System.out.println("Conjunto de Datos: "+conjuntoDatos); 

        //Añadir un elemento al final
        conjuntoDatos.add("G");
        System.out.println("Conjunto de Datos: "+conjuntoDatos);

        //Añadir un elemento al inicio
        List<String> aux = new ArrayList<>(conjuntoDatos);
        aux.add(0, "A");
        conjuntoDatos = new LinkedHashSet<>(aux);
        System.out.println("Conjunto de Datos: "+conjuntoDatos);

        //Añadir varios elementos en bloque al final
        Set<String> bloque1 = new LinkedHashSet<>();
        bloque1.add("X");
        bloque1.add("Y");
        bloque1.add("Z");

        conjuntoDatos.addAll(bloque1);
        System.out.println("Conjunto de Datos: "+conjuntoDatos);

        //Añadir varios elementos en bloque en una posición
        //Añadimos a partir de la posición 7 despues de 'G'
        Set<String> bloque2 = new LinkedHashSet<>();
        bloque2.add("O");
        bloque2.add("P");
        bloque2.add("Q");

        aux = new ArrayList<>(conjuntoDatos);
        aux.addAll(7,bloque2);

        conjuntoDatos = new LinkedHashSet<>(aux);
        System.out.println("Conjunto de Datos: "+conjuntoDatos);
       
        //Eliminar un elemento en una posición concreta
        //Eliminamos 'D' en la posición 3
        aux = new ArrayList<>(conjuntoDatos);
        aux.remove(3);
        conjuntoDatos = new LinkedHashSet<>(aux);
        System.out.println("Conjunto de Datos: "+conjuntoDatos);

        //Actualizar 'O' en la posición 6 por 'H'
        aux = new ArrayList<>(conjuntoDatos);
        aux.set(6, "H");
        conjuntoDatos = new LinkedHashSet<>(aux);
        System.out.println("Conjunto de Datos: "+conjuntoDatos);

        //Comprobar si un elemento está en el conunto
        //Comprobmos si esta 'P'-> Dará true
        System.out.println("Esta P: "+conjuntoDatos.contains("P"));
        
        //Comprobar si esta 'M'-> Dará false
        System.out.println("Esta M: "+conjuntoDatos.contains("M"));
   
        //Eliminar todo el contenido del conjunto
        conjuntoDatos.clear();
        System.out.println("Conjunto de datos: " + conjuntoDatos);


        //////////////////////////
        //                      //
        //   DIFICULTAD EXTRA   //
        //                      //
        //////////////////////////
    
        Set<String> conjunto1 = new LinkedHashSet<>();
        conjunto1.add("me");
        conjunto1.add("gustan");
        conjunto1.add("las");
        conjunto1.add("croquetas");
        Set<String> conjunto2 = new LinkedHashSet<>();
        conjunto2.add("también");
        conjunto2.add("me");
        conjunto2.add("molan");
        conjunto2.add("las");
        conjunto2.add("paellas");
        System.out.println("Conjunto1: "+ conjunto1);
        System.out.println("Conjunto2: "+conjunto2);

        //Union
        Set<String> union = new LinkedHashSet<>(conjunto1);
        union.addAll(conjunto2);
        System.out.println("Unión: "+union);

        //Intersección
        Set<String> interseccion = new LinkedHashSet<>(conjunto1);
        interseccion.retainAll(conjunto2);
        System.out.println("Intersección: "+interseccion);

        //Diferencia
        Set<String> difference = new LinkedHashSet<>(conjunto1);
        difference.removeAll(conjunto2);
        System.out.println("Diferencia: "+difference);

        //Diferencia simétrica
        Set<String> difference1Minus2 = new LinkedHashSet<>(conjunto1);
        difference1Minus2.removeAll(conjunto2);
        Set<String> difference2Minus1 = new LinkedHashSet<>(conjunto2);
        difference2Minus1.removeAll(conjunto1);
        difference1Minus2.addAll(difference2Minus1);
        System.out.println("Diferencia: "+difference1Minus2);

    }
}
