package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	var date_actual string

	date_actual = time.Now().Format("2006-01-02 15:04:05")
	fmt.Println("Fecha actual: ", date_actual)
	fmt.Printf("Inserte su fecha de nacimiento con el siguiente formato (yyyy-mm-dd HH:MM:SS): ")

	reader := bufio.NewReader(os.Stdin)
	date_birth, _ := reader.ReadString('\n')

	date_birth = strings.TrimSuffix(date_birth, "\n")

	age_actual := date_actual[:4] + date_actual[5:7] + date_actual[8:10] + date_actual[11:13] + date_actual[14:16] + date_actual[17:19]
	age_birth := date_birth[:4] + date_birth[5:7] + date_birth[8:10] + date_birth[11:13] + date_birth[14:16] + date_birth[17:19]

	age_actual_number, _ := strconv.Atoi(age_actual)
	age_bith_number, _ := strconv.Atoi(age_birth)
	operation := age_actual_number - age_bith_number
	age_result := strconv.Itoa(operation)

	fmt.Println("La cantidad de años entre ambas fechas es tu edad por lo tanto ...")
	fmt.Println("Edad:", age_result[:2])

	// Dificultad extra (OPCIONAL)
	// Formatear las fechas de cumpleaños :3
	fmt.Println("--------------------")
	fmt.Println("A continuación daremos diferentes maneras de presentar los datos :D ")
	fmt.Printf("Tu naciste el día '%s', del mes '%s' y del año '%s'\n", date_birth[8:10], know_month(date_birth[5:7]), date_birth[:4])
	fmt.Printf("Tu naciste a a las '%s' con minutos '%s' con '%s' segundos XD\n", date_birth[11:13], date_birth[14:16], date_birth[17:19])
	fmt.Printf("Tu naciste en el mes de: '%s'\n", know_month(date_birth[5:7]))
	fmt.Printf(know_leap_year(date_birth[:4]) + "\n")
	fmt.Printf("Naciste el día '%s' del mes '%s' a las '%s' horas\n", date_birth[8:10], know_month(date_birth[5:7]), date_birth[11:13])
	fmt.Printf(know_day(date_birth[11:13]) + "\n")
	fmt.Printf("Tu signo zodiacal es: '%s'\n", know_star_sing(date_birth[5:7]+date_birth[8:10]))
	fmt.Printf("Naciste en el año chino de: '%s', que es el año: '%s'\n", know_chino(date_birth[:4]), date_birth[:4])
	fmt.Printf("Ahora pondremos en otro orden tu fecha de nacimiento de: dd-mm-yyyy: '%s-%s-%s'\n", date_birth[8:10], date_birth[5:7], date_birth[:4])
	fmt.Printf("Naciste en el año: '%s' el día '%s' a las '%s' horas\n", date_birth[:4], date_birth[8:10], date_birth[11:13])
}

func know_month(month string) string {
	name_month := map[string]string{
		"01": "January",
		"02": "February",
		"03": "March",
		"04": "April",
		"05": "May",
		"06": "June",
		"07": "July",
		"08": "August",
		"09": "September",
		"10": "October",
		"11": "November",
		"12": "December",
	}

	return name_month[month]
}
func know_leap_year(age string) string {
	age_int, _ := strconv.Atoi(age)

	if age_int%4 == 0 && age_int%100 != 0 {
		return "Naciste En un año Bisiesto"
	}
	return "No naciste en un año bisiesto :c"
}

func know_day(hour string) string {
	hour_int, _ := strconv.Atoi(hour)

	if hour_int >= 6 && hour_int <= 12 {
		return "Naciste en la mañana"
	} else if hour_int >= 13 && hour_int <= 19 {
		return "Naciste en la tarde"
	} else if hour_int >= 20 && hour_int <= 23 {
		return "Naciste en la noche"
	} else {
		return "Naciste en la madrugada"
	}
}

func know_star_sing(month_day string) string {
	month_day_int, _ := strconv.Atoi(month_day)

	if month_day_int >= 321 && month_day_int <= 419 {
		return "Aries"
	} else if (month_day_int >= 420 && month_day_int <= 520) || (month_day_int >= 219 && month_day_int <= 320) {
		return "Tauro"
	} else if (month_day_int >= 521 && month_day_int <= 620) || (month_day_int >= 321 && month_day_int <= 420) {
		return "Géminis"
	} else if (month_day_int >= 621 && month_day_int <= 722) || (month_day_int >= 421 && month_day_int <= 520) {
		return "Cáncer"
	} else if (month_day_int >= 723 && month_day_int <= 822) || (month_day_int >= 521 && month_day_int <= 621) {
		return "Leo"
	} else if (month_day_int >= 823 && month_day_int <= 922) || (month_day_int >= 622 && month_day_int <= 722) {
		return "Virgo"
	} else if (month_day_int >= 923 && month_day_int <= 1022) || (month_day_int >= 723 && month_day_int <= 822) {
		return "Libra"
	} else if (month_day_int >= 1023 && month_day_int <= 1121) || (month_day_int >= 823 && month_day_int <= 922) {
		return "Escorpio"
	} else if (month_day_int >= 1122 && month_day_int <= 1221) || (month_day_int >= 923 && month_day_int <= 1022) {
		return "Sagitario"
	} else if (month_day_int >= 1222 || month_day_int <= 119) || (month_day_int >= 1023 && month_day_int <= 1121) {
		return "Capricornio"
	} else if (month_day_int >= 120 && month_day_int <= 218) || (month_day_int >= 1122 && month_day_int <= 1221) {
		return "Acuario"
	} else {
		return "Piscis"
	}
}

func know_chino(age string) string {
	age_int, _ := strconv.Atoi(age)

	if age_int%12 == 0 {
		return "Mono"
	} else if age_int%12 == 1 {
		return "Gallo"
	} else if age_int%12 == 2 {
		return "Perro"
	} else if age_int%12 == 3 {
		return "Cerdo"
	} else if age_int%12 == 4 {
		return "Rata"
	} else if age_int%12 == 5 {
		return "Buey"
	} else if age_int%12 == 6 {
		return "Tigre"
	} else if age_int%12 == 7 {
		return "Conejo"
	} else if age_int%12 == 8 {
		return "Dragón"
	} else if age_int%12 == 9 {
		return "Serpiente"
	} else if age_int%12 == 10 {
		return "Caballo"
	}
	return "Cabra"
}
