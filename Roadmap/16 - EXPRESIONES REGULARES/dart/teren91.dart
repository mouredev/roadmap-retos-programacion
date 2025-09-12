
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */


void main()
{
  final alphaNumeric = RegExp(r'^[a-zA-Z0-9]+$');
  final numeric = RegExp(r'^[0-9]+$');
  
  final mailRegEx = RegExp(r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$');
  final phoneRegEx = RegExp(r'^\+?[0-9 ]{6,15}$');
  final urlRegEx = RegExp(r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$');

  final mail = 'MailPrueba@test.es';
  final phoneNumber = '646585921a';
  final url = 'https://test.com/id=2034';

  print(alphaNumeric.hasMatch('abc123'));
  print(numeric.hasMatch('abc123'));
  print(numeric.hasMatch('123'));

  print('Validar mail: $mail -> ${mailRegEx.hasMatch(mail)}');
  print('Validar teléfono: $phoneNumber -> ${phoneRegEx.hasMatch(phoneNumber)}');
  print('Validar url: $url -> ${urlRegEx.hasMatch(url)}');
}