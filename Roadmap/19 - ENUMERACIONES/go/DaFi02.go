package main

import (
	"fmt"
)

type Week_day int

const (
	Monday Week_day = iota + 1
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
	Sunday
)

// this function returns the name of the day of the week, and is metod of the type Week_day
func (day Week_day) string() string {
	switch day {
	case Monday:
		return "Monday"
	case Tuesday:
		return "Tuesday"
	case Wednesday:
		return "Wednesday"
	case Thursday:
		return "Thursday"
	case Friday:
		return "Friday"
	case Saturday:
		return "Saturday"
	case Sunday:
		return "Sunday"
	default:
		return "Invalid day"
	}
}

func getDayOfWeek(dayNumber int) string {
	day := Week_day(dayNumber)
	return day.string()
}

/*
	Extra Dificult
*/

type Order struct {
	id    int
	state Status_Product
}

type Status_Product int

const (
	Pending Status_Product = iota
	Envoy
	Received
	Canceled
)

func (state Status_Product) string() string {
	switch state {
	case Pending:
		return "Pending"
	case Envoy:
		return "Envoy"
	case Received:
		return "Received"
	case Canceled:
		return "Canceled"
	default:
		return "Invalid state"
	}
}

func chageStatus(order *Order, newState Status_Product) string {
	if newState == Received && order.state != Envoy {
		return fmt.Sprintf("Invalid state for order %d, the order is not envoy\n", order.id)
	}

	if newState == Canceled && order.state == Received {
		return fmt.Sprintf("Invalid state for order %d, the order is already received\n", order.id)
	}

	if newState == Canceled && order.state == Pending {
		order.state = Canceled
		return order.state.string()
	}

	if newState == Canceled && order.state == Envoy {
		return fmt.Sprintf("Invalid state for order %d, the order is already envoy\n", order.id)
	}

	if order.state == Canceled {
		return fmt.Sprintf("Invalid state for order %d, the order is already canceled\n", order.id)

	}

	order.state = newState
	return fmt.Sprintf("The order %d is now %s\n", order.id, order.state.string())
}

func (order *Order) print() {
	fmt.Println(" ---------------------------------- ")
	fmt.Println("Order ID: ", order.id, " - ", order.state.string())
}

func main() {
	// The function getDayOfWeek() returns the day of the week corresponding to the number passed as an argument
	fmt.Println(getDayOfWeek(1)) // print "Monday"
	fmt.Println(getDayOfWeek(7)) // Print "Sunday"

	/*
		Extra Dificult
	*/

	// Remember
	// Pending = 0
	// Envoy = 1
	// Received = 2
	// Canceled = 3
	// Create a product with the status "Pending"
	order_1 := Order{id: 1, state: Pending}
	order_2 := Order{id: 2, state: Envoy}
	order_3 := Order{id: 3, state: Received}
	order_4 := Order{id: 4, state: Canceled}
	order_5 := Order{id: 5, state: Envoy}

	fmt.Println("Initial status")
	order_1.print()
	order_2.print()
	order_3.print()
	order_4.print()
	order_5.print()

	fmt.Println("")
	fmt.Println("Change Status of the orders")

	fmt.Print(chageStatus(&order_1, Received))
	fmt.Print(chageStatus(&order_2, Canceled))
	fmt.Print(chageStatus(&order_3, Canceled))
	fmt.Print(chageStatus(&order_4, Envoy))
	fmt.Print(chageStatus(&order_5, Received))
	fmt.Print(chageStatus(&order_1, Envoy))

	fmt.Println("")
	fmt.Println("Final status")

	order_1.print()
	order_2.print()
	order_3.print()
	order_4.print()

	fmt.Println(" ")
	fmt.Println("Additional changes")
	fmt.Print(chageStatus(&order_2, Received))
	fmt.Print(chageStatus(&order_1, Received))

	fmt.Println(" ")
	fmt.Println("Final status")
	order_1.print()
	order_2.print()

	// The function chageStatus() changes the status of the order, and returns the new status

}
