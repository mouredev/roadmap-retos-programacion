/* 
#00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
> #### Dificultad: Fácil | Publicación: 26/12/23 | Corrección: 02/01/24

## Ejercicio

```
/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
*/

//- Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

//Hola java: https://www.java.com/es/download
/*
Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 */
//Este es un comentario de una sola linea.

/*
Este es
un 
comentario
de 
varias
lineas
*/
//Creamos una clase
public class Tei4bds232 {
    public static void main(String[] args) {
        //Esto es una variable
        int var = 25;
        //Esto es una constante
        final double NUMERO_PY = 3.14519;
        System.out.println("El resultado de la variable es de \n" + var +  "y el valor de la constante es de:" + NUMERO_PY);
    //Datos primitivos en java
    int var_1 = 30;
    System.out.println("Hola!! soy una variable de tipo entero? \n" + var_1);
    float var_2 = 2.45f;
    System.out.println("Hola!! soy una variable de tipo decimal o flotante \n" + var_2);
    Boolean var_4 = true;
    System.out.println("Hola!! soy una variable de tipo boolean \n" + var_4);
    Boolean var_5 = false;
    System.out.println("Hola!! soy una variable de tipo boolean \n" + var_5);
    double var_6 =  3.1415926535;
    System.out.println("Hola!! soy una variable de tipo double y represento numeros decimales de doble precision \n" + var_6);
    byte var_7 = 126;
    System.out.println("Hola!! soy una variable de tipo short  y represento numeros enteros de 8 bits \n" + var_7);
    short var_8 = 768;
    System.out.println("Hola!! soy un tipo de dato short y represneto numero enteror de 16 bits \n" + var_8);
    long var_9 = 853;
    System.out.println("Hola!! soy un tipo de dato long y represento enteros de 64 bits: \n" + var_9);
    char var_10 = '\u0000';
    System.out.println("Hola!! Soy un tipo de dato char y represento un solo caracter como letras,numeros o simbolos: \n" + var_10);

    String saludo = "java";
    System.out.println("Hola!!\n" + saludo);

    }
    
}
