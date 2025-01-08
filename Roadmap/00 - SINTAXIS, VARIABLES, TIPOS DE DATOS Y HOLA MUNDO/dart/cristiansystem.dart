/*
    retosdeprogramacion.com by Mouredev
    Lenguaje: https://dart.dev/
*/

/// Representacion de comentarios en Dart

    // Single-line comments

    /* 
        Multi-line comments
    */

    /// Documentation comments
    
    // Crea una variable (y una constante si el lenguaje lo soporta)

void main() {

  var nameVar = 'Eminem'; // Deduce automáticamente el tipo de la variable
  Object lastname = 'Dart'; // Con tipo dinámico
  String lname = 'EM'; // Con tipo específico del lenguaje
  final finalName = 'Eminem'; // La variable solo puede ser asignada una vez y se debe asignar en tiempo de ejecución
  const middlename = 'E.'; // La variable es una constante de tiempo de compilación

  /*
      Null safety
          El lenguaje Dart aplica la seguridad de nulos.
  */

  String? name; // Tipo nullable. Puede ser `null` o una cadena.
  String nameNotNull; // Tipo no nullable. No puede ser `null` pero puede ser una cadena.

  /*
      Valor predeterminado
          Las variables no inicializadas que tienen un tipo nullable tienen un valor inicial de null. Incluso las variables con tipos numéricos son inicialmente nulas, porque los números, como todo en Dart, son objetos.
  */

  int? lineCount;
  assert(lineCount == null);

  int lineCountNotNull = 0; // Con la seguridad de nulos, debes inicializar los valores de las variables no nulas antes de usarlas


  /// Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

    // Cadenas de texto
    String nombre = 'Juan';

    // Enteros
    int edad = 25;

    // Números de punto flotante
    double altura = 1.75;

    // Booleanos
    bool esEstudiante = true;

    // Caracter
    String inicial = 'J';

    // Lista de enteros
    List<int> numeros = [1, 2, 3, 4, 5];

    // Conjunto de números de punto flotante
    Set<double> alturas = {1.75, 1.80, 1.65};

    // Mapa (diccionario) de información personal
    Map<String, dynamic> informacionPersonal = {
        'nombre': 'Juan',
        'edad': 25,
        'altura': 1.75,
        'esEstudiante': true,
    };

    // Variable dinámica
    dynamic variableDinamica = 'Hola';

    //Variable Record syntax
    var record = ('first', a: 2, b: true, 'last');

    // Imprimir los valores
    print('Nombre: $nombre');
    print('Edad: $edad');
    print('Altura: $altura');
    print('¿Es estudiante?: $esEstudiante');
    print('Inicial: $inicial');
    print('Números: $numeros');
    print('Alturas: $alturas');
    print('Información Personal: $informacionPersonal');
    print('Variable Dinámica: $variableDinamica');

    //Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
    print('¡Hola, Dart!');
}
