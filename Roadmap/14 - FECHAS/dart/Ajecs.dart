import 'dart:io';

// ! Para formatear de fechas con todo lo que ofrece python es necesario usar el paquete intl.

void main() {
  stdout.writeln('\n******************* Fechas ***********************\n');

  final currentDate = DateTime.now();
  final myBirthdate = DateTime(1986, 9, 7, 7, 40);

  print(
    'Han pasado ${((currentDate.difference(myBirthdate).inDays) ~/ 365)} años 🧑‍🦳 desde mi nacimiento',
  );
  // Mediante el método difference podemos obtener la diferencia en dias entre dos fechas.

  stdout.writeln('\n********************** Extra ********************\n');

  //////// FORMA NATIVA DE OBTENER EL FORMATO DE FECHA -> "DIA-MES-AÑO". ////////

  String nativeDateParse(DateTime date) {
    int day = date.day;
    int month = date.month;
    int year = date.year;
    return '${day.toString().padLeft(2, '0')}-${month.toString().padLeft(2, '0')}-$year';
  }

  print(nativeDateParse(myBirthdate));
  print(
    'Nací a las ${myBirthdate.hour}:${myBirthdate.minute}:${myBirthdate.second} horas',
  );

  ////// FORMA NATIVA DE OBTENER EL DIA DEL AÑO ////////

  int getDayOfYear(DateTime date) {
    final startYear = DateTime(date.year, 1, 1);
    return date.difference(startYear).inDays + 1;
    // indays es getter que permite obtener la diferencia en dias
  }

  print('Nací el dia ${getDayOfYear(myBirthdate)} del año');

  /////// FORMA NATIVA DE OBTENER EL DIA DE LA SEMANA //////

  String getWeekday(int weekday) {
    switch (weekday) {
      case 1:
        return 'lunes';
      case 2:
        return 'martes';
      case 3:
        return 'miercoles';
      case 4:
        return 'jueves';
      case 5:
        return 'viernes';
      case 6:
        return 'sabado';
      case 7:
        return 'domingo';
      default:
        return 'No existe esa fecha';
    }
  }

  print('Nací un día ${getWeekday(myBirthdate.weekday)}');

  ////// NOMBRE DEL MES SIN USAR INTL. //////

  const months = [
    'enero',
    'febrero',
    'marzo',
    'abril',
    'mayo',
    'junio',
    'julio',
    'agosto',
    'septiembre',
    'octubre',
    'noviembre',
    'diciembre',
  ];

  String monthName = months[myBirthdate.month - 1];

  print('Nací en el mes de $monthName');

  ////// ¿¿¿NACI ANTES O DESPUES??? ////////

  Record messi = (name: 'Lionel Messi', birthdate: DateTime(1987, 6, 24));
  Record ada = (name: 'Ada Lovelace', birthdate: DateTime(1815, 12, 10));

  String afterOrBefore(person) {
    var compareDates = person.birthdate.compareTo(myBirthdate);
    if (compareDates == 1) {
      return 'Nací antes que ${person.name}';
    } else if (compareDates == -1) {
      return 'Nací después que ${person.name}';
    } else {
      return 'Nacimos al mismo tiempo 😮';
    }
  }

  print(afterOrBefore(ada));

  print('');
}
