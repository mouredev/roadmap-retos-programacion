let date = new Date
date = date.toLocaleString("es-AR", { hour12: false})

let birthDate = new Date("July 03, 2002 11:30:00")

console.log(parseInt(date.match(/\W(\d+)\,/)[1]) - birthDate.getFullYear())

// ----------------------------------------- DIFICULTAD EXTRA -----------------------------------------
const nowDate = new Date
// recupero año, mes, dia, hora, minutos, segundo, milisegundo de la fecha actual
const nowYear = nowDate.getFullYear(); const nowMonth = nowDate.getMonth(); const nowDay = nowDate.getDate();
let birthDatePassed = (nowMonth - birthDate.getMonth() > 0)
let years = nowYear - birthDate.getFullYear()
let months = nowMonth - birthDate.getMonth()
let monthDays = (30.41 * nowMonth) + nowDay

console.log(`Han pasado ${birthDatePassed ? (years) * 12 + (months) 
                                          : (years - 1) * 12 + nowMonth} meses desde que nací`)

console.log(`Han pasado ${birthDatePassed ? (years) * 12 * 4 + 4 * (months) + Math.floor(nowDay / 7) 
                                          : (years - 1) * 12 * 4 +  4 * nowMonth + Math.floor(nowDay / 7)} semanas desde que nací`)

console.log(`Han pasado ${birthDatePassed ? Math.floor((years) * 12 * 30.41 + 30.41 * (months) + nowDay) 
                                          : Math.floor((years - 1) * 12 * 30.41 + monthDays)} días desde que nací`)

console.log(`Han pasado ${birthDatePassed ? Math.floor(((years) * 12 * 30.41 + 30.41 * (months) + nowDay) * 24) 
                                          : Math.floor(((years - 1) * 12 * 30.41 + monthDays) * 24)} horas desde que nací`)

console.log(`Han pasado ${birthDatePassed ? Math.floor(((years) * 12 * 30.41 + 30.41 * (months) + nowDay) * 24 * 60)
                                          : Math.floor(((years - 1) * 12 * 30.41 + monthDays) * 24 * 60)} minutos desde que nací`)

console.log(`Han pasado ${birthDatePassed ? Math.floor(((years) * 12 * 30.41 + 30.41 * (months) + nowDay) * 24 * 60 * 60)
                                          : Math.floor(((years - 1) * 12 * 30.41 + monthDays) * 24 * 60 * 60)} segundos desde que nací`)

console.log(`Han pasado ${birthDatePassed ? Math.floor(((years) * 12 * 30.41 + 30.41 * (months) + nowDay) * 24 * 60 * 60 * 100)
                                          : Math.floor(((years - 1) * 12 * 30.41 + monthDays) * 24 * 60 * 60 * 100)} milisegundos desde que nací`)

console.log(`Una persona pudo recorre ${birthDatePassed ? Math.floor(((years) * 12 * 30.41 + 30.41 * (months) + nowDay) * 24) * 5 
                                                        : Math.floor(((years - 1) * 12 * 30.41 + monthDays) * 24) * 5} kilometros desde que nací`)

console.log(`Una persona pudo haber dado ${birthDatePassed ? ((Math.floor(((years) * 12 * 30.41 + 30.41 * (months) + nowDay) * 24) * 5) / 12728).toFixed(2)
                                                            : ((Math.floor(((years - 1) * 12 * 30.41 + monthDays) * 24) * 5) / 12728).toFixed(2)} vueltas a la tierra desde que nací`)


console.log(`Una totuga pudo haber dado ${birthDatePassed ? ((Math.floor(((years) * 12 * 30.41 + 30.41 * (months) + nowDay) * 24) * 0.29) / 12728).toFixed(2)
                                                          : ((Math.floor(((years - 1) * 12 * 30.41 + monthDays) * 24) * 0.29) / 12728).toFixed(2)} vueltas a la tierra desde que nací`)