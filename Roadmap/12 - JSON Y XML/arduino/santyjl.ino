///12 JSON Y XML///

/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */


#include <ArduinoJson.h>  // Incluimos la librería ArduinoJson necesaria para manipular objetos JSON

void setup() {
  Serial.begin(9600);  // Inicializamos la comunicación serial a 9600 baudios
  while (!Serial) continue;  // Esperamos a que la comunicación serial esté lista

  StaticJsonDocument<200> doc;  // Creamos un documento JSON estático con capacidad para 200 bytes

  // A continuación, agregamos datos al documento JSON
  doc["Formato"] = "Json";  // Agregamos una clave "Formato" con el valor "Json"
  doc["Nombre"] = "Santiago";  
  doc["Edad"] = 14;  
  doc["Fecha de nacimiento"] = "20/01/2010";  
  doc["Lenguajes de programacion"] = "arduino y python";

  serializeJsonPretty(doc, Serial);  // Serializamos el documento JSON de manera legible y lo enviamos por el puerto serial
  Serial.println();  // Imprimimos una nueva línea después del documento JSON para mayor claridad
}
 // no se como hacerle para el xml , perdon
void loop() {

}
