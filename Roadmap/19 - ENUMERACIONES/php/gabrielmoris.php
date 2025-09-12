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

enum OrderStatus
{
    case PENDING;
    case SENT;
    case DELIVERED;
    case CANCELED;
};

class OrderSystem
{
    private $orders;

    public function __construct()
    {
        $this->orders = [];
    }

    private function randomString()
    {
        return substr(str_shuffle('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), 0, 10);
    }

    private function manageOrder($id, $status = "")
    {
        $index = array_search($id, array_column($this->orders, "id"));
        if ($index !== false) {
            $targetedOrder = &$this->orders[$index];
            if ($status != "") {
                $targetedOrder["status"] =  $status;
            }

            echo "=============================================\n";
            echo "Your order: " . $targetedOrder["item"] . " with id $id now has the status " . $targetedOrder["status"] . ". \n";
            echo "=============================================\n";;
        } else {
            echo "Error: Order ID not found.\n";
        }
    }


    public function sendOrder($item)
    {
        $orderId = $this->randomString();
        $orderStatus = OrderStatus::SENT->name;
        $this->orders[] = ["id" => $orderId, "item" => $item, "status" => $orderStatus];
        echo "=============================================\n";
        echo "Your order: $item with id $orderId  Has the status $orderStatus. \nPlease, save the order ID in a safe place and don't share it.\n";
        echo "=============================================\n";
    }

    public function forceDeleteOrder($id)
    {
        $index = array_search($id, array_column($this->orders, "id"));
        if ($index !== false) {
            unset($this->orders[$index]);
            $this->orders = array_values($this->orders);
        } else {
            echo "Error: Order ID not found.\n";
        }
    }

    public function changeToDelivered($id)
    {
        $status = OrderStatus::DELIVERED->name;
        $this->manageOrder($id, $status);
    }

    public function cancelOrder($id)
    {
        $status = OrderStatus::CANCELED->name;
        $this->manageOrder($id, $status);
    }

    public function checkOrderStatus($id)
    {
        $this->manageOrder($id);
    }
}



function orderStatusManager()
{
    $orderManager = new OrderSystem();

    echo "
    ===== PRINTER =====
     1.- Send Order 
     2.- Check order Status
     3.- Change Status to Delivered
     4.- Cancel Order
     5.- Delete Order (Only in extreme cases)
     6.- Exit
    ==================
     \n";

    while (true) {
        $selection = readline("Select an option\n");
        switch ($selection) {
            case 1:
                $item =  readline("What do you want to send? \n");
                $orderManager->sendOrder($item);
                break;
            case 2:
                $id = readline("Give me your order ID: \n");
                $orderManager->checkOrderStatus($id);
                break;
            case 3:
                $id = readline("Give me your order ID: \n");
                $orderManager->changeToDelivered($id);
                break;
            case 4:
                $id = readline("Give me your order ID: \n");
                $orderManager->cancelOrder($id);
                break;
            case 5:
                $id = readline("Give me your order ID: \n");
                $orderManager->forceDeleteOrder($id);
                break;
            case 6:
                echo "\033c";
                echo "Good bye 👋 📦\n";
                exit;
            default:
                echo "This option doesn't exist.\n";
        }
    }
}

orderStatusManager();
