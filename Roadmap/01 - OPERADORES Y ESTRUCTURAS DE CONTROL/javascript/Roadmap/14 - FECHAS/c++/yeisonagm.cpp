/* EJERCICIO #14: FECHAS
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
#include <iostream>
#include <ctime>

using namespace std;

// Crea un fecha personalizada
tm createCustomDate(int day, int month, int year, int hour, int minute, int second) {
    // Crea una estructura tm con los valores de la fecha
    struct tm timeInfo = {0};
    timeInfo.tm_mday = day;
    timeInfo.tm_mon = month - 1;
    timeInfo.tm_year = year - 1900;
    timeInfo.tm_hour = hour;
    timeInfo.tm_min = minute;
    timeInfo.tm_sec = second;

    return timeInfo;
}

// Formatea un fecha
std::string formatDate(const tm timeInfo, const string &format) {
    char buffer[80];

    // Formatea la fecha
    strftime(buffer, 80, format.c_str(), &timeInfo);
    return buffer;
}

int main() {
    cout << "EJERCICIO #14: FECHAS" << endl;

    // Fecha actual
    time_t now = time(nullptr);
    char *dt = ctime(&now);
    cout << "Hora actual: " << dt << endl;

    // Fecha de mi nacimiento
    tm dateOfBirth = createCustomDate(16, 4, 2001, 17, 25, 10);
    cout << "Fecha de nacimiento: " << formatDate(dateOfBirth, string("%Y-%m-%d %H:%M:%S")) << endl;

    // Calcula la diferencia de años
    double diffSeconds = difftime(now, mktime(&dateOfBirth));
    cout << "Diferencia en segundos: " << diffSeconds << endl;
    double diffYears = diffSeconds / (60 * 60 * 24 * 365.25);
    cout << "Años transcurridos: " << diffYears << endl;

    // Dificultad extra
    cout << "\nFecha de nacimiento (Formas diferentes):" << endl;
    cout << "Día, mes y año: " << formatDate(dateOfBirth, string("%d-%m-%Y")) << endl;
    cout << "Hora, minuto y segundo: " << formatDate(dateOfBirth, string("%H:%M:%S")) << endl;
    cout << "Hora, minuto y segundo (Formato 12 horas): " << formatDate(dateOfBirth, string("%I:%M:%S %p")) << endl;
    cout << "Día de año: " << formatDate(dateOfBirth, string("%j")) << endl;
    cout << "Día de la semana: " << formatDate(dateOfBirth, string("%A")) << endl;
    cout << "Día de la semana (abreviado): " << formatDate(dateOfBirth, string("%a")) << endl;
    cout << "Nombre del mes: " << formatDate(dateOfBirth, string("%B")) << endl;
    cout << "Nombre del mes (abreviado): " << formatDate(dateOfBirth, string("%b")) << endl;
    cout << "Mes, número de dia, año: " << formatDate(dateOfBirth, string("%B %d, %Y")) << endl;
    cout << "Dia th, mes, año: " << formatDate(dateOfBirth, string("%dth %B, %Y")) << endl;
    cout << "Dia, mes y año (Formato largo): " << formatDate(dateOfBirth, string("%A %d of %B del %Y")) << endl;

    return 0;
}