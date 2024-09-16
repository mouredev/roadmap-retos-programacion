
import 'package:intl/intl.dart';

/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */


void main()
{
  DateTime date = DateTime.now();
  DateTime birthDay = DateTime(1991, 9, 14, 1, 0, 0);
  DateFormat dateFormatter = DateFormat('dd/MM/yyyy hh:mm');
  Duration dateDifference = date.difference(birthDay);

  print('Fecha actual: ' + dateFormatter.format(date));
  print('Cumple      : ' + dateFormatter.format(birthDay));
  print('Transcurrido: ${(dateDifference.inDays / 365).floor().toString()} años');

  //Dificultad extra

  DateFormat dateFormatter_ddMMyyyy = DateFormat('dd/MM/yyyy');
  DateFormat dateFormatter_hhmmss = DateFormat('hh:mm:ss');
  DateFormat dateFormatter_Completa = DateFormat('EEEE, dd MMMM, yyyy');
  DateFormat dateFormatter_diaSemana = DateFormat('EEEE');
  DateFormat dateFormatter_Mes = DateFormat('MMMM');

  print('Cumple      : ' + dateFormatter_ddMMyyyy.format(birthDay));
  print('Cumple      : ' + dateFormatter_hhmmss.format(birthDay));
  print('Cumple      : ' + dateFormatter_Completa.format(birthDay));
  print('Cumple      : ' + dateFormatter_diaSemana.format(birthDay));
  print('Cumple      : ' + dateFormatter_Mes.format(birthDay));
}