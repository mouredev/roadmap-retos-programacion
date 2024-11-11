<?php

class CountDown
{
    private function checkFutureDate(DateTime $date): void
    {
        $now = new DateTime();
        if ($date < $now) {
            throw new Exception("El evento ya ha pasado!");
        }
    }

    private function drawCountDown(DateTime $date): void
    {
        system("clear");
        $now = new DateTime('now', new DateTimeZone('Europe/Madrid'));
        $now_utc = $now->setTimezone(new DateTimeZone('UTC'));
        $diff = $date->diff($now_utc);
        $days = $diff->format("%a");
        $hours = $diff->format("%h");
        $minutes = $diff->format("%i");
        $seconds = $diff->format("%s");

        $str_date = $date->format("d-m-Y H:i:s");
        $str_now_utc = $now_utc->format("d-m-Y H:i:s");

        echo "TU EVENTO TENDRÁ LUGAR EL PROXIMO $str_date HORA UTC" . PHP_EOL . PHP_EOL;
        $this->printSuccess("==============");
        echo " Cuenta atrás " . PHP_EOL;
        $this->printSuccess("==============");
        echo "Días: " . $days . PHP_EOL;
        echo "Horas: " . $hours . PHP_EOL;
        echo "Minutos: " . $minutes . PHP_EOL;
        echo "Segundos: " . $seconds . PHP_EOL;

        if ($str_date === $str_now_utc) {
            echo PHP_EOL . " ============================================================================" . PHP_EOL;
            $this->printSuccess(" ¡Felicidades! ES LA HORA : Comenzamos a divertirnos? .");
        } else {
            sleep(1);
            $this->drawCountDown($date);
        }
    }

    private function checkYear(int $year)
    {
        if (strlen((string) $year) !== 4) {
            throw new Exception("El año debe estar formado por 4 dígitos");
        }
    }

    private function checkMonth(string $month): void
    {
        $int_month = intval($month);
        if ($int_month < 1 || $int_month > 12) {
            throw new Exception("El mes debe estar entre 1 y 12");
        }
    }

    private function checkDay(int $day, int $month): void
    {
        $meses_largos = [1, 3, 5, 7, 8, 10, 12];
        if ($month == 2 && $day > 29) {
            throw new Exception("No puedes tener un día mayor a 29 en febrero");
        }
        if (!in_array($month, $meses_largos) && $day > 31) {
            throw new Exception("No puedes tener un día mayor al día 31 para el mes seleccionado");
        } else if ($day > 30) {
            throw new Exception("No puedes tener un día mayor al día 30 para el mes seleccionado");
        }
    }

    private function checkHour(int $hour): void
    {
        if ($hour < 0 || $hour > 23) {
            throw new Exception("La hora debe estar entre 0 y 23");
        }
    }

    private function checkMinute(int $minute): void
    {
        if ($minute < 0 || $minute > 59) {
            throw new Exception("Los mintuos deben estar entre 0 y 59");
        }
    }

    private function checkSeconds(int $seconds): void
    {
        if ($seconds < 0 || $seconds > 59) {
            throw new Exception("Los segundos deben estar entre 0 y 59");
        }
    }


    private function printError(string $message): void
    {
        echo "\033[0;31m$message" . PHP_EOL;
        echo "\033[0G\033[0m";
    }

    private function printSuccess(string $message): void
    {
        echo "\033[0;32m$message" . PHP_EOL;
        echo "\033[0G\033[0m";
    }

    private function getYear(): string
    {
        try {
            $year = intval(trim(readline("Dame el año del evento:")));
            $this->checkYear($year);
            return (string) $year;
        } catch (Exception $e) {
            $this->printError($e->getMessage());
            return $this->getYear();
        }
    }

    private function getMonth(): string
    {
        try {
            echo "1. Enero" . PHP_EOL;
            echo "2. Febrero" . PHP_EOL;
            echo "3. Marzo" . PHP_EOL;
            echo "4. Abril" . PHP_EOL;
            echo "5. Mayo" . PHP_EOL;
            echo "6. Junio" . PHP_EOL;
            echo "7. Julio" . PHP_EOL;
            echo "8. Agosto" . PHP_EOL;
            echo "9. Septiembre" . PHP_EOL;
            echo "10. Octubre" . PHP_EOL;
            echo "11. Noviembre" . PHP_EOL;
            echo "12. Diciembre" . PHP_EOL;
            $month = intval(trim(readline("Dame el mes del evento:")));
            $month = str_pad((string) $month, 2, "0", STR_PAD_LEFT);
            $this->checkMonth($month);
            return (string) $month;
        } catch (Exception $e) {
            $this->printError($e->getMessage());
            return $this->getMonth();
        }
    }

    private function getDay(int $month): string
    {
        try {
            $day = intval(trim(readline("Dame el día del evento:")));
            $this->checkDay($day, $month);
            return (string) $day;
        } catch (Exception $e) {
            $this->printError($e->getMessage());
            return $this->getDay($month);
        }
    }

    private function getHour(): string
    {
        try {
            $hour = intval(trim(readline("Dame la hora del evento:")));
            $this->checkHour($hour);
            $hour = str_pad((string) $hour, 2, "0", STR_PAD_LEFT);
            return $hour;
        } catch (Exception $e) {
            $this->printError($e->getMessage());
            return $this->getHour();
        }
    }


    private function getMinute(): string
    {
        try {
            $minutes = intval(trim(readline("Dame el minuto del evento:")));
            $this->checkMinute($minutes);
            $minutes = str_pad((string) $minutes, 2, "0", STR_PAD_LEFT);
            return $minutes;
        } catch (Exception $e) {
            $this->printError($e->getMessage());
            return $this->getMinute();
        }
    }

    private function getSecond(): string
    {
        try {
            $seconds = intval(trim(readline("Dame el segundo del evento:")));
            $this->checkSeconds($seconds);
            $seconds = str_pad((string) $seconds, 2, "0", STR_PAD_LEFT);
            return $seconds;
        } catch (Exception $e) {
            $this->printError($e->getMessage());
            return $this->getSecond();
        }
    }


    public function run()
    {
        system("clear");
        try {
            $year = $this->getYear();
            $month = $this->getMonth();
            $day = $this->getDay((int) $month);
            $hour = $this->getHour();
            $minute = $this->getMinute();
            $second = $this->getSecond();

            $local_date = new DateTime($year . "-" . $month . "-" . $day . ' ' . $hour . ':' . $minute . ':' . $second, new DateTimeZone('Europe/Madrid'));
            $utc_date = $local_date->setTimezone(new DateTimeZone('UTC'));
            $this->checkFutureDate($utc_date);

            $this->drawCountDown($utc_date);
        } catch (Exception $e) {
            $this->printError($e->getMessage());
        }
    }
}

$countdown = new CountDown();
$countdown->run();
