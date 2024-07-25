#include <iostream>
#include <chrono>
#include <string>
#include <ctime>

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

/*************************************************************
********************* ZONA DE FUNCIONES **********************
*************************************************************/
std::string currenTime() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t); 

    char buffer[128];
    std::strftime(buffer, std::size(buffer), "%d/%m/%Y %X" ,now);

    return buffer;
};

std::string formatDate(const char* fmt, std::tm* date) {
    char buffer[80];
    std::strftime(buffer, std::size(buffer), fmt, date);

    return buffer;
}

// FUNCION PRINCIPAL 
int main() {
    // La siguiente instruccion imprime la fecha actual a la hora 
    // de ejecutar el código
    std::cout << "Tiempo actual: [ " << currenTime() << " ]\n";

    // Creacion de una estructura customDate
    struct tm customDate = { }; 
    customDate.tm_year = 2004 - 1900; // Año de mi nacimiento 
    customDate.tm_mon = 5; // Mes de mi nacimiento: Junio - 05
    customDate.tm_mday = 28; // Dia de nacimiento
    customDate.tm_hour = 12; // Hora de nacimiento
    customDate.tm_min = 59; // Minuto de nacimiento

    // Se crea una varlable de tipo buffer para almacenar la fecha ya formateada 
    char buffer[80];
    std::strftime(buffer, std::size(buffer), "%d/%m/%Y %X %P", &customDate);

    // De imprime la fecha
    std::cout << "Fecha de nacimiento: [ " << buffer << " ]\n";

    // Convertir la fecha personalizada a un punto en el tiempo desde el epoch (1 de enero de 1970)
    std::time_t customTime = std::mktime(&customDate);

    // Crear un objeto de tiempo con la fecha personalizada
    std::chrono::system_clock::time_point customPoint = std::chrono::system_clock::from_time_t(customTime);

    // Obtener el tiempo actual
    std::chrono::system_clock::time_point now = std::chrono::system_clock::now();

    // Calcular la diferencia entre la fecha personalizada y el tiempo actual
    auto difference = std::chrono::duration_cast<std::chrono::hours>(now - customPoint);

    // Imprimir la diferencia en días
    std::cout << "Diferencia en años: " << (float)difference.count() / 8760.0 << std::endl;


    /**************************************************************************************
    ************* IMPRESION DE LA FECHA DE NACIMIENTO EN DISTINTOS FORMATOS ***************
    ***************************************************************************************/
    std::cout << "\n************ FORMATO DE FECHA DE NACIMIENTO **********\n";
    std::tm* localTime = std::localtime(&customTime);
    std::cout << "Formato 1: " << formatDate("%d/%m/%Y", localTime) << std::endl; // Formato: día/mes/año
    std::cout << "Formato 2: " << formatDate("%m/%d/%Y", localTime) << std::endl; // Formato: mes/día/año
    std::cout << "Formato 3: " << formatDate("%Y-%m-%d", localTime) << std::endl; // Formato: año-mes-día
    std::cout << "Formato 4: " << formatDate("%d %b %Y", localTime) << std::endl; // Formato: día abreviado mes año (ejemplo: 01 Jan 2024)
    std::cout << "Formato 5: " << formatDate("%A, %d de %B de %Y", localTime) << std::endl; // Formato: día de semana, día de mes de año (ejemplo: viernes, 01 de enero de 2024)
    std::cout << "Formato 6: " << formatDate("%H:%M:%S", localTime) << std::endl; // Formato: hora:minuto:segundo
    std::cout << "Formato 7: " << formatDate("%I:%M:%S %p", localTime) << std::endl; // Formato: hora:minuto:segundo AM/PM (ejemplo: 05:30:15 PM)
    std::cout << "Formato 8: " << formatDate("%Y-%m-%d %H:%M:%S", localTime) << std::endl; // Formato: año-mes-día hora:minuto:segundo
    std::cout << "Formato 9: " << formatDate("%Y%m%d%H%M%S", localTime) << std::endl; // Formato: año mes día hora minuto segundo (ejemplo: 20240101233000)
    std::cout << "Formato 10: " << formatDate("%Y-%m-%dT%H:%M:%SZ", localTime) << std::endl; // Formato: año-mes-díaThora:minuto:segundoZ (ejemplo: 2024-01-01T23:30:00Z)


    return 0;
}

// std::string currentTime() {
//     std::time_t t = std::time(nullptr);
//     std::tm* now = std::localtime(&t); 

//     char buffer[128];
//     std::strftime(buffer, std::size(buffer), "%d/%m/%Y %X" ,now);

//     return buffer;
// }