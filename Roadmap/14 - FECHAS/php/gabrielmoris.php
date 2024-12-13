<?php
/*
* EXERCISE:
* Create two variables using the date objects (date, or similar) of your language:
* A first one representing the current date (day, month, year, hour, minute, second).
* A second one representing your date of birth (you can make up the time).
* Calculate how many years have passed between the two dates.
*/


date_default_timezone_set('Europe/Berlin'); // This will set the date zone in general
echo date(DATE_RSS) . "\n"; // Output: Mon, 22 May 2023 15:02:34 +0000
echo date(DATE_ATOM) . "\n"; // Output: 2023-05-22T15:02:34+00:00
$count = 0;
do {
    echo "\033c";
    $currentDateTime = date('D d.m.Y H:i:s');
    echo "Current date and time: " . $currentDateTime . "\n";
    $BDDateTime = new DateTime('1989-09-17 03:45:00');
    $formatedBD = $BDDateTime->format("D d.m.Y H:i:s");
    echo  "I born " . $formatedBD . "\n";
    echo "\n\n";
    $currDate = new DateTime($currentDateTime);
    $timedifference = $BDDateTime->diff($currDate);

    echo "I am " . round($timedifference->days / 365, 1) . " years old.\n";

    $count += 1;
    sleep(1);
} while ($count < 5);


/* EXTRA DIFFICULTY (optional):
* Using your birthday date, format it and display its result in
* 10 different ways. For example:
* Day, month and year.
* Hour, minute and second.
* Day of year.
* Day of the week.
* Name of the month.
* (whatever you can think of...)
*/

echo "My BD in different formats:\n";

$BDDateTime = new DateTime('1989-09-17 03:45:00');
echo "Date " . $BDDateTime->format('d.m.Y') . "\n";
echo "Hour " . $BDDateTime->format('H:i:s') . "\n";
echo "Day of the Year " . $BDDateTime->format('z') . "\n";
echo "Day of the week " . $BDDateTime->format('l') . "\n";
echo "Name of the Month " . $BDDateTime->format('F') . "\n";
echo "ISO format " . $BDDateTime->format('c') . "\n";
$now = new DateTime();
$interval = $BDDateTime->diff($now);
echo "Time Passed: " . floor($interval->format('%R%a') / 365) . " Years \n";
echo "I born a " . $BDDateTime->format('l, jS F Y \a\t g:ia') . "\n";
