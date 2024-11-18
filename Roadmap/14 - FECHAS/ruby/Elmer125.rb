#  * EJERCICIO:
#  * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
#  * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
#  * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
#  * Calcula cuántos años han transcurrido entre ambas fechas.
require 'date'

today = DateTime.now
birth_date = DateTime.parse("14-09-1995 10:05:33")

years = today.year - birth_date.year
puts "Years: #{years}"

#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
#  * 10 maneras diferentes. Por ejemplo:
#  * - Día, mes y año.
#  * - Hora, minuto y segundo.
#  * - Día de año.
#  * - Día de la semana.
#  * - Nombre del mes.
#  * (lo que se te ocurra...)

puts "Day/Month/Year: #{birth_date.strftime('%d/%m/%Y')}"
puts "Year/Month/Day: #{birth_date.strftime('%Y/%m/%d')}"
puts "Hours:Mins:Secs: #{birth_date.strftime('%H:%M:%S')}"
puts "Day of the year: #{birth_date.yday}"
puts "Day of the week: #{birth_date.strftime('%A')}"
puts "Month name: #{birth_date.strftime('%B')}"
puts "Full date: #{birth_date.strftime('%A, %d de %B de %Y')}"
puts "Week of the year: #{birth_date.strftime('%U')}"
puts "Month and year: #{birth_date.strftime('%B %Y')}"
puts "AM/PM: #{birth_date.strftime('%p')}"

