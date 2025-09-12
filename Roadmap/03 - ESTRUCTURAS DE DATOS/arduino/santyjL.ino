// 03 ESTRUCTURAS DE DATOS //

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
*/


void setup() {
  Serial.begin(9600);
  array();
  delay(1000);
  Struct();
  delay(1000);
  presentacion();
}

void loop() {
}

void array() {
  // Arrays - Listas
  int miLista[5] = {10, 20, 30, 40, 50};
  Serial.println("\n=== Arrays - Listas ===");
  Serial.print("Lista original: ");
  imprimirLista(miLista, 5);

  // Añadir nuevos valores al final de la lista
  miLista[5] = 60;
  Serial.println("Lista modificada 1: ");
  imprimirLista(miLista, 6);
  miLista[6] = 70;
  Serial.println("Lista modificada 2: ");
  imprimirLista(miLista, 7);
  miLista[7] = 80;
  Serial.println("Lista modificada 3: ");
  imprimirLista(miLista, 8);

  // Asignar un nuevo valor a una posición existente
  miLista[2] = 35;
  Serial.println("Lista modificada 4: ");
  imprimirLista(miLista, 7);

  // Eliminar el valor en la posición 3
  miLista[3] = 0; // Asignar un valor nulo o fuera de rango (en realidad no elimina nada, pero indica que no es relevante)
  Serial.println("Lista modificada 5: ");
  imprimirLista(miLista, 7);
}

void Struct(){ //Una struct te permite crear un tipo de dato personalizado que puede contener varios campos con diferentes tipos de datos.

  // Struct
  struct Persona {
    char nombre[30];
    int edad;
    float altura;
  };

  Persona santiago;

  // Asignar valores
  strcpy(santiago.nombre, "Santiago");
  santiago.edad = 14;
  santiago.altura = 1.71;

  // Acceder a los valores
  Serial.println("\n=== Struct ===");
  Serial.print("Nombre: ");
  Serial.println(santiago.nombre); //el nombre de la struct con el valor a leer se parece a POO por lo menos de python
  Serial.print("Edad: ");
  Serial.println(santiago.edad); //prueba variando el orde del llamado
  Serial.print("Altura: ");
  Serial.println(santiago.altura);
}

void imprimirLista(int lista[], int longitud) {
  Serial.print("Lista: [");

  for (int i = 0; i < longitud; i++) {
    Serial.print(lista[i]);

    // Imprimir coma y espacio si no es el último elemento
    if (i < longitud - 1) {
      Serial.print(", ");
    }
  }
  Serial.println("]");
}


// Extra - contactos //

// Funciones utilizadas en el reto - conceptos//

/*
*sizeof : devuelve el tamaño en bytes de un tipo de dato o de una variable. Se utiliza para determinar cuánta memoria ocupa un
  tipo de dato o una instancia de un tipo de dato. Ejemplo : 43 utiliza 2 bytes , 777 utiliza 3 bytes o 555 55 utiliza 6 bytes
  o en cadenas de texto "111 11" regresaria 8 bytes porque las "" tambien cuenta , en este caso la funcion se usa para leer
  la cantidad de caracteres del carecteres del nombre y el numero

*readBytesUntil : es una función de Arduino que lee datos desde un objeto de tipo Stream (como Serial) hasta que encuentra un
  delimitador especificado. Los datos leídos se almacenan en un búfer. en otras parabras crea una variable temporal la cual
  almacenara los datos semejantes a los que se busca en este caso se usa para verificar si un nombre existe y si exciste mostrarlo

*strcmp : compara dos cadenas de caracteres. Devuelve un valor entero menor que, igual a, o mayor que cero si la primera cadena
 es menor que, igual a, o mayor que la segunda cadena, respectivamente. en respectiva si la respues es 0 es que son iguales si no
 las cadenas son diferentes y regresara un -1 o un 1

*strcpy :(string copy) se utiliza para copiar el contenido de una cadena de caracteres (string) en otra

*/


// Definición de la estructura para los contactos
struct Contacto {
  char nombre[20];
  char numero[12];
};

// Arreglo de contactos
Contacto contactos[] = {
  {"fernandez", "1111 1111"},
  {"julieta", "2222 2222"},
  {"jose", "3333 3333"},
  {"juancho", "4444 4444"}
};

// Función de búsqueda
void busqueda() {
  char nombreBuscar[20];
  Serial.print("Introduzca el nombre del contacto: ");
  Serial.readBytesUntil('\n', nombreBuscar, sizeof(nombreBuscar));

  for (int i = 0; i < sizeof(contactos) / sizeof(contactos[0]); i++) {
    if (strcmp(nombreBuscar, contactos[i].nombre) == 0) {
      Serial.print(contactos[i].nombre);
      Serial.print(" - ");
      Serial.println(contactos[i].numero);
      return;
    }
  }

  Serial.println("Contacto no existente");
}

// Función de inserción
void insercion() {
  char nuevoNombre[20];
  char nuevoNumero[12];

  Serial.print("Ingrese el nombre del nuevo contacto: ");
  Serial.readBytesUntil('\n', nuevoNombre, sizeof(nuevoNombre));
  Serial.print("Ingrese el número de teléfono: ");
  Serial.readBytesUntil('\n', nuevoNumero, sizeof(nuevoNumero));

  // Verificar número de teléfono
  if (strlen(nuevoNumero) <= 11) {
    // Crear nuevo contacto
    Contacto nuevoContacto;
    strcpy(nuevoContacto.nombre, nuevoNombre);
    strcpy(nuevoContacto.numero, nuevoNumero);

    // Añadir a la lista
    int indice = sizeof(contactos) / sizeof(contactos[0]);
    contactos[indice] = nuevoContacto;

    Serial.print("Contacto ");
    Serial.print(nuevoContacto.nombre);
    Serial.println(" añadido correctamente.");
  } else {
    Serial.println("Número de teléfono no válido. Asegúrate de ingresar un número numérico máximo de 11 dígitos.");
  }
}

// Función de actualización
void actualizacion() {
  char antiguoNombre[20];
  char nuevoNombre[20];

  Serial.print("Introduzca el nombre a cambiar: ");
  Serial.readBytesUntil('\n', antiguoNombre, sizeof(antiguoNombre));
  Serial.print("Introduzca el nuevo nombre: ");
  Serial.readBytesUntil('\n', nuevoNombre, sizeof(nuevoNombre));

  // Buscar el contacto
  for (int i = 0; i < sizeof(contactos) / sizeof(contactos[0]); i++) {
    if (strcmp(antiguoNombre, contactos[i].nombre) == 0) {
      // Cambiar el nombre
      strcpy(contactos[i].nombre, nuevoNombre);
      Serial.println("Se cambió correctamente.");
      return;
    }
  }

  Serial.println("El contacto a cambiar no existe.");
}

// Función de eliminación
void eliminacion() {
  char nombreEliminar[20];
  Serial.print("Introduzca el nombre a eliminar: ");
  Serial.readBytesUntil('\n', nombreEliminar, sizeof(nombreEliminar));

  // Buscar el contacto
  for (int i = 0; i < sizeof(contactos) / sizeof(contactos[0]); i++) {
    if (strcmp(nombreEliminar, contactos[i].nombre) == 0) {
      // Eliminar el contacto
      contactos[i] = contactos[sizeof(contactos) / sizeof(contactos[0]) - 1];
      Serial.println("Se eliminó correctamente.");
      return;
    }
  }

  Serial.println("Contacto no existente, inténtelo de nuevo.");
}

void presentacion() {

  Serial.println("\nLista de contactos\n"
                 "Acciones:\n"
                 "1. Mirar contactos\n"
                 "2. Buscar contactos\n"
                 "3. Añadir contactos\n"
                 "4. Eliminar contactos\n"
                 "5. Cerrar lista de contactos");

  while (!Serial.available()) {}

  Serial.print("Elija según el índice: ");
  delay(100);

  int opcion = Serial.parseInt();

  switch (opcion) {
    case 1:
      for (const Contacto &contacto : contactos) {
        Serial.print(contacto.nombre);
        Serial.print(" -- ");
        Serial.println(contacto.numero);
      }
      break;

    case 2:
      busqueda();
      break;

    case 3:
      insercion();
      break;

    case 4:
      eliminacion();
      break;

    case 5:
      Serial.println("Programa finalizado");
      while (true) {}  // Detener aquí
      break;

    default:
      Serial.println("No está en el índice.");
      break;
  }
}