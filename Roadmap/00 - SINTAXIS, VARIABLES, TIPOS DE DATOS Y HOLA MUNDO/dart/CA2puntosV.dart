// LENGUARJE DART: https://dart.dev/

// Comentarios de una sola línea

/*
Comentario multilinea (se puede contraer)
*/

/// Comentarios multiple de una sola linea
/// (Se pueden contraer los que esten seguidos)

/// Variable
String helloDart = '¡Hola, Dart!';

/// Constantes (final y const) son de tipo @inmutable (no pueden cambiar su valor)
/// un ejemplo para diferenciarlas es DateTime.now(). Si se intenta usando const, saldrá error
/// porque se estará intentando inicializar al momento de compilar.

// final se inicializa al momento de usarse
final String varFinal = 'Final Variable';

// const se inicializa al momento de escribirse
const String varConst = 'Final Variable';

/// Variable primitivas
String name = 'Pepito';

bool active = true;

int age = 40;
double weight = 13.2;
num numeric = 100; // Puede ser int o double

dynamic dynamicType; // Puede ser de cualquier tipo
Null nullableType;

// Null Safety (cualquier tipo de datos puede ser de tipo null usando '?')
String? nullableString;

void main(List<String> args) {
  print('¡Hola, Dart!');

  // Formas de usar variable
  print(helloDart);
  print('Concatenacion:' + helloDart);
  print('Interpolación: $helloDart');
}
