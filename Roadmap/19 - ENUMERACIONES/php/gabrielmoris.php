<?php
/* EXERCISE:
* Using your language, explore the definition of the data type
* that serves to define enumerations (Enum).
* Create an Enum that represents the days of the week from Monday
* to Sunday, in that order. With that enum, create an operation
* that displays the name of the day of the week depending on the integer
* used (from 1 to 7).
*/
enum Week
{
    case Monday;
    case Tuesday;
    case Wednesday;
    case Thursday;
    case Friday;
    case Saturday;
    case Sunday;
}


function getWeekDay($num)
{
    switch ($num) {
        case 1:
            echo Week::Monday->name . "\n";
            break;
        case 2:
            echo Week::Tuesday->name . "\n";
            break;
        case 3:
            echo Week::Wednesday->name . "\n";
            break;
        case 4:
            echo Week::Thursday->name . "\n";
            break;
        case 5:
            echo Week::Friday->name . "\n";
            break;
        case 6:
            echo Week::Saturday->name . "\n";
            break;
        case 7:
            echo Week::Sunday->name . "\n";
            break;
        default:
            echo "Whe week has only 7 days.";
    }
}

$count = 1;
while ($count < 8) {
    getWeekDay($count);
    $count++;
}

/* EXTRA DIFFICULTY (optional):
* Create a small order status management system.
* Implement a class that defines an order with the following characteristics:
* - The order has an identifier and a status.
* - The status is an Enum with these values: PENDING, SENT, DELIVERED and CANCELED.
* - Implement the functions to modify the status:
*   - Order sent
*   - Order canceled
*   - Order delivered
*   (Establish logic, for example, it cannot be delivered if it has not been sent, etc...)
* - Implement a function to display a descriptive text according to the current status.
* - Create different orders and show how they interact with them.
*/