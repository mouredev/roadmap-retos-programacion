import Foundation

// Obtener la fecha actual.
let currentDate = Date()
print("\nEsta es la fecha de hoy.")
print(currentDate)

// Crear un calendario gregoriano.
let calendar = Calendar(identifier: .gregorian)

// Especifica la fecha de nacimiento.
var birthComponent = DateComponents()
birthComponent.year = 1984
birthComponent.month = 7
birthComponent.day = 4
birthComponent.hour = 04
birthComponent.minute = 17
birthComponent.second = 48

// Obtener la fecha de nacimiento.
// var birthDate = Date()
guard let birthDate = calendar.date(from: birthComponent) else {
    fatalError("No hay datos.")
}
print("\n Esta es la fecha de mi nacimiento.")
print(birthDate)

// Calcular la diferencia entre las fechas.
let yearsApart: DateComponents = calendar.dateComponents([.year], from: birthDate, to: currentDate)
let monthsApart = calendar.dateComponents([.month], from: birthDate, to: currentDate)
let daysApart = calendar.dateComponents([.day], from: birthDate, to: currentDate)
let hoursApart = calendar.dateComponents([.hour], from: birthDate, to: currentDate)
let minutesApart = calendar.dateComponents([.minute], from: birthDate, to: currentDate)
let secondsApart = calendar.dateComponents([.second], from: birthDate, to: currentDate)

print("\nEstos son las difrerencias.")

// Imprimir la diferencia en años.
if let years = yearsApart.year {
    print("Hay: \(years) años de diferencia.")    
}
// Imprimir la diferencia en meses.
if let months = monthsApart.month {
    print("Hay \(months) meses de diferencia.")
}
// Imprimir la diferencia en dias.
if let days = daysApart.day {
    print("Hay: \(days) dias de diferencia.")
}
// Imprime la diferencia en horas.
if let hours = hoursApart.hour {
    print("Hay: \(hours) horas de diferencia.")
}
// imprime la diferencia en minutos.
if let minutes = minutesApart.minute {
    print("Hay: \(minutes) minutos de direrencia.")
}
// Imprime la diferencia en segundos.
if let seconds = secondsApart.second {
    print("Hay: \(seconds) segundos de diferencia.")
}




// DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA")




// Crear un DateFormatter.
let dateFormatter = DateFormatter()

// Establecer el formato de la fecha original.
dateFormatter.dateFormat = "dd-MM-yyyy"
let originalDate = "04-07-2024"

print("\nFecha Original:")
print("\(originalDate)")

// Convertir la cadena de fecha a un objeto Date.
guard let date = dateFormatter.date(from: originalDate) else {
    fatalError("Error al convertir la fecha")
}

print("\nLos 10 formatos:")
// Crear un array con 10 formatos diferentes para formatear la fecha.
let formats = [
    "dd-MM-yyyy",
    "MM-dd-yyyy",
    "yyyy-MM-dd",
    "EEEE, d MMMM yyyy",
    "dd/MMM/yyyy",
    "MMM dd, yyyy",
    "MMMM d, yyyy",
    "yyyy/MM/dd",
    "MMM d, yyyy h:mm a",
    "MMMM dd, yyyy HH:mm:ss"
]

// Imprimir la fecha formateada en los diferentes formatos.
for format in formats {
    dateFormatter.dateFormat = format
    let formattedDate = dateFormatter.string(from: date)
    print(formattedDate)
}
