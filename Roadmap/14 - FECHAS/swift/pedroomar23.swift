import Foundation

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

enum DateError: Error {
    case dateInvalid
}

let currentDate = Date()
print(currentDate)

let calendar = Calendar.current
var components = DateComponents()
components.day = 20
components.month = 3
components.year = 2024
components.hour = 3
components.minute = 25
components.second = 30

guard let bithday = calendar.date(from: components) else {
    throws DateError.dateInvalid
}

print(bithday)

let years = calendar.dateComponents([.year], from: bithday, to: components).year {
    print("Ahora mismo tengo \(year) años de edad")
}




