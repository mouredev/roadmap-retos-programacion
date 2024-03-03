// https://go.dev/
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
*/
package main
import ("fmt")
const PI = 3.14
const e = 2.71
const (
  a string = "a";
  b = "b";
)
func main(){
  fmt.Println("Hello Python!")
  //sintax
  var student1 string = "John" //type is string
  var student2 = "Jane" //type is inferred
  x := 2 //type is inferred
  fmt.Println(student1,student2,x);
  var integer int=3;
  var float float32=3.333;
  var text string = "hello world";
  var bolean bool = true;
  fmt.Println(integer,float,text,bolean);
  fmt.Println(PI);
  fmt.Print(a,b);
  fmt.Printf("integer value: %v and type: %T", integer, integer);

}
