import 'dart:io';
import 'dart:convert';

class Programmer {
  late final String name;
  late final int age;
  late final String birthdate;
  late final List<String> languages;

  Programmer(this.name, this.age, this.birthdate, this.languages);

  // Se sobreescribe el método toString para poder imprimir de forma sencilla todas las propiedades de la clase.
  @override
  String toString() {
    return 'Programmer(\nnombre: $name,\nedad: $age,\nfecha de nacimiento: $birthdate,\nlenguajes: $languages)';
  }
}

void main() async {
  stdout.write('\n***************** XML y JSON ****************\n');

  final jsonFilename = 'Ajecs.json';
  final xmlFilename = 'Ajecs.xml';
  var jsonFile = File(jsonFilename);
  var xmlFile = File(xmlFilename);

  Future<void> deleteFiles() async {
    await Future.wait([jsonFile.delete(), xmlFile.delete()]);
  }

  void createXmlJson() async {
    //////////////// data en map de Dart //////////////////////

    Map<String, dynamic> programmer = {
      'name': '',
      'age': 0,
      'birthdate': '',
      'languages': [],
    };

    ////////////// FUNCIONES ////////////////////////////////

    Future<void> createFiles() async {
      try {
        // Se Ejecuta ambas operaciones de escritura en paralelo
        await Future.wait([jsonFile.create(), xmlFile.create()]);

        print('¡Ambos archivos fueron creados con éxito!');
      } catch (error) {
        print('Error al crear los archivos: $error');
      }
    }

    Future<String> showFiles() async {
      var filesList = await Future.wait([
        jsonFile.readAsString(),
        xmlFile.readAsString(),
      ]);
      return filesList.join('\n\n');
    }

    dynamic saveJson(
      String name,
      int age,
      String birthdate,
      List<String> languages,
    ) {
      programmer['name'] = name;
      programmer['age'] = age;
      programmer['birthdate'] = birthdate;
      programmer['languages'] = List<String>.from(languages);

      String jsonText = jsonEncode(programmer);

      return jsonText;
    }

    Future<void> printJson(
      String name,
      int age,
      String birthdate,
      List<String> languages,
    ) async {
      final jsonText = saveJson(name, age, birthdate, languages);
      await jsonFile.writeAsString(jsonText);
    }

    /*
      A la hora de codificar/decodificar archivos XML es recomendable usar el paquete externo xml.
      Para usar solamente código nativo se aplica la siguiente función.  
    */

    String saveXml({
      required String rootName,
      required Map<String, dynamic> map,
    }) {
      // StringBuffer permite almacenar las cadenas que se van creando dinamicamente.
      final buffer = StringBuffer();

      buffer.writeln('<?xml version="1.0" encoding="UTF-8"?>');
      buffer.writeln('<$rootName>');

      for (final entry in map.entries) {
        final key = entry.key;
        final value = entry.value;

        if (value is List) {
          buffer.writeln('  <$key>');
          for (final item in value) {
            buffer.writeln('    <language>${item.toString()}</language>');
          }
          buffer.writeln('  </$key>');
        } else {
          buffer.writeln('  <$key>${value.toString()}</$key>');
        }
      }

      // ! Se evito añadir el filtrado de caracteres no aceptados. Ya que no eran necesarios para el programa.

      buffer.writeln('</$rootName>');

      // Se imprime en el archivo el texto codificado.
      String xmlString = buffer.toString();

      return xmlString;
    }

    Future<void> printXml() async {
      await xmlFile.writeAsString(
        saveXml(rootName: 'Ajecs.xml', map: programmer),
      );
    }

    await createFiles();

    bool goOn = true;
    while (goOn) {
      print('Ingresa el nombre: ');
      String inputName = stdin.readLineSync() ?? '';
      print('Ingresa la edad: ');
      int inputAge = int.parse(stdin.readLineSync() ?? '');
      print('Ingresa la fecha de nacimiento: ');
      String inputBirthdate = stdin.readLineSync() ?? '';
      print('Ingresa los lenguajes de programación que usas: ');
      List<String> inputLanguages = (stdin.readLineSync() ?? '').split(' ');

      printJson(inputName, inputAge, inputBirthdate, inputLanguages);
      printXml();

      print('');

      print(await showFiles());

      print('\nPresiona "delete" para borrar los archivos');
      print('o exit para salir');

      String option = stdin.readLineSync() ?? '';

      switch (option) {
        case 'delete':
          await deleteFiles();
          print('Archivos borrados');
          goOn = false;
          break;
        case 'exit':
          goOn = false;
          break;
        default:
          print('Opcion no valida');
      }
    }
  }

  createXmlJson();

  stdout.write('\n******************* Extra *****************************\n\n');

  Future<void> addXmlDataToClass() async {
    List<String> dataList = [];
    // A falta de paquete nativo bueno es el Regex :)
    final regex = RegExp(r'>\s*([^<\s,](?:[^<]*[^<\s,])?)\s*<');
    String xmlText = await xmlFile.readAsString();

    for (final match in regex.allMatches(xmlText)) {
      dataList.add(match.group(1)!); // [name, age, ...]
    }
    Programmer dataXmlClass = Programmer(
      dataList[0],
      int.parse(dataList[1]),
      dataList[2],
      dataList.sublist(3, dataList.length),
    );

    print(
      'Datos del XML "transformados" a la clase Programmer:\n${dataXmlClass.toString()}\n',
    );
  }

  Future<void> addJsonDataToClass() async {
    String jsonText = await jsonFile.readAsString();
    Map<String, dynamic> mapJson = jsonDecode(jsonText);

    print(mapJson);

    Programmer dataJsonClass = Programmer(
      mapJson['name'],
      mapJson['age'],
      mapJson['birthdate'],
      List<String>.from(mapJson['languages']),
    );

    print(
      '\nDatos del mapa decodificado en formato Json añadidos a la clase:\n${dataJsonClass.toString()}\n',
    );
  }

  // await addXmlDataToClass();
  // await addJsonDataToClass();
  // print('');

  // await deleteFiles();
}
