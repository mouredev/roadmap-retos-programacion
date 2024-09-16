/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
 */

import 'dart:async';

void main() async
{

  //Ejecución en paralelo
  List<Future<void>> functions = [

    showName('Función C', 3),
    showName('Función B', 2),
    showName('Función A', 1)
  ];

  await Future.wait(functions); 
  
  await showName('Función D', 1);
}

Future<void> showName(String name, int duration) async 
{
  await Future.delayed(Duration(seconds: duration));
  print('Soy $name');
}