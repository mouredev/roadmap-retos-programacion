/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */
import 'dart:collection';

void main()
{
  final List<String> animales =[];

  //Añadir elemento al final
  animales.add('Perro');
  animales.add('Gato');
  animales.add('Tucán');

  print('Animales inicial: $animales');

  
  //Añadir elemento al principio
  animales.insert(0, 'Colibrí');

  print('Animales insert inicio: $animales');

  //Varios al final
  animales.addAll(['Foca', 'Delfín']);
  print('Animales varios al final: $animales');


  //Varios en posición concreta
  animales.insertAll(2, ['Tortuga', 'Lagarto']);
  print('Animales varios en posición concreta: $animales');

  //Eliminar en posición concreta
  animales.removeAt(1);
  print('Animales eliminar en pos concreta: $animales');

  //Actualizar valor en posición concreta
  animales[3] = 'Serpiente';
  print('Animales actualizar valor concreto: $animales');

  //Comprobar si un elemento existe en la colección
  
  print('Hay gato en la colección: ${animales.contains('Gato')}');
  print('Hay Tucán en la colección: ${animales.contains('Tucán')}');

  //Vaciar conjunto
  animales.removeRange(0, animales.length);
  print('Vaciar colección: $animales');

  //Unión
  final Set<String> mamiferos = Set<String>();
  final Set<String> aves = Set<String>();
  Set<String> mamiferos_aves = Set<String>();
  mamiferos.add('Suricato');
  mamiferos.add('Jirafa');
  mamiferos.add('Pantera');

  aves.add('Gorrión');
  aves.add('Cuervo');
  aves.add('Águila');

  //Union
  mamiferos_aves = mamiferos_aves.union(mamiferos);
  mamiferos_aves = mamiferos_aves.union(aves);
  print('Mamíferos: $mamiferos');
  print('Aves: $aves');
  print('Mamíferos y aves: $mamiferos_aves');

  //Intersección - Eliminamos un elemento para que sea distinto al original
  mamiferos_aves.remove('Jirafa');
  mamiferos_aves = mamiferos_aves.intersection(mamiferos);

  print('Mamíferos y aves intersección mamíferos: $mamiferos_aves');

  //Diferencia
  mamiferos_aves.add('Rinoceronte');
  print('Mamíferos y aves añadido elemento: $mamiferos_aves');
  mamiferos_aves = mamiferos_aves.difference(mamiferos);
  print('Mamíferos y aves diferencia mamíferos: $mamiferos_aves');

  //Diferencia simétrica
  mamiferos_aves.add('Jirafa');
  print('Mamíferos y aves añadido elemento: $mamiferos_aves');
  mamiferos_aves = mamiferos_aves.difference(mamiferos).union(mamiferos.difference(mamiferos_aves));
  print('Mamíferos y aves diferencia simétrica mamíferos: $mamiferos_aves');
}