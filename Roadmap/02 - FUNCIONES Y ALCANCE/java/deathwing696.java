/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

/**
 *
 * @author death
 */
public class deathwing696 {
    public static void main(String[] args)
    {        
        int num_veces = Repite_num_veces("Hola", "Adios");
        String cadena = String.format("El número se ha impreso %d veces", num_veces);
        
        System.out.println(cadena);
    }
    
    static private int Repite_num_veces(String cadena1, String cadena2)
    {
        int num_veces = 0;
        
        for (int i = 1; i <= 100; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                String cadena = String.format("%s %s", cadena1, cadena2);
                System.out.println(cadena);
            }
            else if (i % 3 == 0)
            {
                System.out.println(cadena1);
            }
            else if (i % 5 == 0)
            {
                System.out.println(cadena2);
            }
            else
            {
                System.out.println(i);
                num_veces++;
            }
        }
        
        return num_veces;
    }
}
