import Foundation

/*
 Para manejar fechas en swift se puede usar la clase Date o la clase DateFormatter para formatearlas
 también se puede usar la clase Calendar para realizar operaciones con fechas.
 */

 enum DateError: Error {
    case invalidDate
 }

// fecha actual
 let currentDate = Date()
 print(currentDate)

// instacia de calendar
 let calendar = Calendar.current
// crear una fecha    
 var componets = DateComponents()
 componets.day = 20
 componets.month = 5
 componets.year = 1994
 componets.hour =  13 
 componets.minute = 30
 componets.second = 0

 guard let bithday = calendar.date(from: componets) else {
        throw DateError.invalidDate
  }
 print(bithday)

 if let years = calendar.dateComponents([.year], from: bithday, to: currentDate).year {
    print("Iam \(years) years old")
 }

let formatted = DateFormatter()

// dia mes año
formatted.dateFormat = "dd/MM/yyyy"
print(formatted.string(from: bithday))
// hora minuto segundo
formatted.dateFormat = "HH:mm:ss"
print(formatted.string(from: bithday))
// nombre del mes 
formatted.dateFormat = "LLLL"
print(formatted.string(from: bithday))

if let dayofWeek = calendar.dateComponents([.weekday], from: bithday).weekday{
    print("I was born on a \(dayofWeek) day")
}

if let dayofYear = calendar.ordinality(of: .day, in: .year, for: bithday){
   print("I was born on the \(dayofYear) day of the year")
}


