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


// Obtén la fecha actual
let currentDate = Date()

// Configura el formato de la fecha
let dateFormatter = DateFormatter()
dateFormatter.dateFormat = "yyyy/MM/dd HH:mm:ss"

// Define tu fecha de nacimiento (por ejemplo, 1 de enero de 1990 a las 12:00:00)
let birthDateString = "1990/01/01 12:00:00"
guard let birthDate = dateFormatter.date(from: birthDateString) else {
    fatalError("Error al convertir la cadena de fecha a objeto Date")
}

// Calcula la diferencia de años entre la fecha actual y la fecha de nacimiento
let calendar = Calendar.current
let ageComponents = calendar.dateComponents([.year], from: birthDate, to: currentDate)
let age = ageComponents.year!

print("Han transcurrido \(age) años desde tu fecha de nacimiento.")


//MARK: - DIFICULTAD EXTRA (opcional)

// Configura el formato de la fecha
let dateFormatter2 = DateFormatter()
dateFormatter.dateFormat = "yyyy/MM/dd HH:mm:ss"

// Define tu fecha de nacimiento (por ejemplo, 1 de enero de 1990 a las 12:00:00)
let birthDateString2 = "1990/01/01 12:00:00"
guard let birthDate = dateFormatter.date(from: birthDateString) else {
    fatalError("Error al convertir la cadena de fecha a objeto Date")
}

// Función para formatear y mostrar la fecha en diferentes formatos
func displayFormattedDates(for date: Date) {
    let formats = [
        "dd/MM/yyyy",              // Día, mes y año
        "HH:mm:ss",                // Hora, minuto y segundo
        "D",                       // Día del año
        "EEEE",                    // Día de la semana
        "MMMM",                    // Nombre del mes
        "MM/dd/yyyy HH:mm",        // Mes/día/año hora:minuto
        "yyyy/MM/dd",              // Año/mes/día
        "MMM d, yyyy",             // Mes abreviado día, año
        "EEEE, MMM d, yyyy",       // Día de la semana, mes abreviado día, año
        "E, d MMM yyyy HH:mm:ss",  // Día de la semana abreviado, día mes año hora:minuto:segundo
    ]
    
    for format in formats {
        dateFormatter.dateFormat = format
        let formattedDate = dateFormatter.string(from: date)
        print("Formato '\(format)': \(formattedDate)")
    }
}

// Muestra las diferentes representaciones de la fecha de nacimiento
displayFormattedDates(for: birthDate)

