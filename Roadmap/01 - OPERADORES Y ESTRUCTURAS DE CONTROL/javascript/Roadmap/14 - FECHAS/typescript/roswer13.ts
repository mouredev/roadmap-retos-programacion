// EJERCICIO:
// Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
// - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
// - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
// Calcula cuántos años han transcurrido entre ambas fechas.

function getDates(): [Date, Date] {
    return [new Date(), new Date(1993, 1, 13, 6, 36, 34)];
}

function calcuatesYearsDifference(now: Date, birth: Date): number {
    var nowYear = now.getFullYear();
    var birthYear = birth.getFullYear();

    if (nowYear >= birthYear) {
        return nowYear - birthYear;
    }

    return birthYear - nowYear;
}

const [now, birth] = getDates();
console.log("Tiempo transcurrido desde el nacimiento: ", calcuatesYearsDifference(now, birth), " años.");


// DIFICULTAD EXTRA (opcional):
// Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
// 10 maneras diferentes. Por ejemplo:
// - Día, mes y año.
// - Hora, minuto y segundo.
// - Día de año.
// - Día de la semana.
// - Nombre del mes.

function dayIntToStringFormat(day: number): string {
    switch (day) {
        case 0: return "Sunday";
        case 1: return "Monday";
        case 2: return "Tuesday";
        case 3: return "Wednesday";
        case 4: return "Thursday";
        case 5: return "Friday";
        case 6: return "Saturday";
        default: return "Invalid day";
    }
}

function formatDates(date: Date) {
    return {
        day: date.getDate(),
        month: date.getMonth() + 1,
        year: date.getFullYear(),
        hours: date.getHours(),
        minutes: date.getMinutes(),
        seconds: date.getSeconds(),
        dayOfYear: Math.floor((date.getTime() - new Date(date.getFullYear(), 0, 0).getTime()) / 86_400_000),
        dayOfWeek: dayIntToStringFormat(date.getDay()),
        monthName: date.toLocaleString('en', { month: 'long' })
    };
}

const formattedDates = formatDates(birth);
console.log(`Dia, mes y año: ${formattedDates.day}/${formattedDates.month}/${formattedDates.year}`);
console.log(`Hora, minuto y segundo: ${formattedDates.hours}:${formattedDates.minutes}:${formattedDates.seconds}`);
console.log(`Dia del año: ${formattedDates.dayOfYear}`);
console.log(`Dia de la semana: ${formattedDates.dayOfWeek}`);
console.log(`Nombre del mes: ${formattedDates.monthName}`);

// Make testings for the functions.
function validateTets(bool: boolean, functionName?: string) {
    console.log(bool ? `✅ Test passed ${functionName}` : `❌ Test failed ${functionName}`);
}
function testGetDates() {
    // Arrange
    const [now, birth] = getDates();
    // Act
    // Assert
    validateTets(now instanceof Date, "testGetDates");
    validateTets(birth instanceof Date, "testGetDates");
}

function testCalcuatesYearsDifference() {
    // Arrange
    const now = new Date(2021, 1, 13, 6, 36, 34);
    const birth = new Date(1993, 1, 13, 6, 36, 34);
    // Act
    const result = calcuatesYearsDifference(now, birth);
    // Assert
    validateTets(result === 28, "testCalcuatesYearsDifference");
}

function testCalculateYearsDifferenceWhenNowIsBeforeBirth() {
    // Arrange
    const now = new Date(1993, 1, 13, 6, 36, 34);
    const birth = new Date(2021, 1, 13, 6, 36, 34);
    // Act
    const result = calcuatesYearsDifference(now, birth);
    // Assert
    validateTets(result === 28, "testCalculateYearsDifferenceWhenNowIsBeforeBirth");
}

function testCalculateDayIntToStringFormat() {
    // Arrange
    // Act
    const result = dayIntToStringFormat(0);
    // Assert
    validateTets(result === "Sunday", "testCalculateDayIntToStringFormat");
}

function testFormatDates() {
    // Arrange
    const date = new Date(1993, 1, 13, 6, 36, 34);
    // Act
    const result = formatDates(date);
    // Assert
    validateTets(result.day === 13, "testFormatDates");
    validateTets(result.month === 2, "testFormatDates");
    validateTets(result.year === 1993, "testFormatDates");
    validateTets(result.hours === 6, "testFormatDates");
    validateTets(result.minutes === 36, "testFormatDates");
    validateTets(result.seconds === 34, "testFormatDates");
    validateTets(result.dayOfYear === 44, "testFormatDates");
    validateTets(result.dayOfWeek === "Saturday", "testFormatDates");
    validateTets(result.monthName === "February", "testFormatDates");
}

function runTests() {
    console.log("Running tests...");
    testGetDates();
    testCalculateYearsDifferenceWhenNowIsBeforeBirth();
    testCalcuatesYearsDifference();
    testCalculateDayIntToStringFormat();
    testFormatDates();
    console.log("Tests finished.");
}

runTests();

