package main

import (
	"errors"
	"fmt"
	"slices"
)

// Tarea exploratorio:
const (
	emptyDay = iota
	day1
	day2
	day3
	day4
	day5
	day6
	day7
)

func ViewDay(dayNumber int) string {
	if dayNumber <= 0 || dayNumber > 7 {
		errornumber := errors.New("Error: The number must be greater than '0' and less than '8'")
		return errornumber.Error()
	}
	Days := [...]string{"", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
	return Days[dayNumber]
}

// Extra
const (
	StatusPending   = iota // 0
	StatusShipped          // 1
	StatusDelivered        // 2
	StatusCancelled        // 3
)

var StatusOptions = fmt.Sprintf("0 for Pending\n 1 for Shipped\n 2 for Delivered\n 3 for Cancelled\n")

var statusStrings = [...]string{"Pending", "Shipped", "Delivered", "Cancelled"}

func getStatusString(status int) string {
	if status < 0 || status >= len(statusStrings) {
		return "Unknown"
	}
	return statusStrings[status]
}

type OrdersManager struct {
	Orders map[int](string)
	id     int
	state  string
}

func NewOrdesManager() OrdersManager {
	return OrdersManager{
		Orders: make(map[int]string),
		id:     0,
		state:  "",
	}
}

func (om *OrdersManager) searchNextID() int {
	if len(om.Orders) == 0 {
		return 1
	}

	return len(om.Orders) + 1
}

func (om *OrdersManager) RegisterOrder() {
	lastid := om.searchNextID()

	if st := getStatusString(StatusPending); st == "Unknown" {
		fmt.Println("RegisterOrder(): Impossible register that status")
		return
	}

	om.Orders[lastid] = getStatusString(StatusPending)
}

func (om *OrdersManager) verifyStatus(id, newStatus int) bool {
	actualStatus := om.Orders[id]
	status := getStatusString(newStatus)
	cancelled := getStatusString(StatusCancelled)
	delivered := getStatusString(StatusDelivered)
	pending := getStatusString(StatusPending)
	shipped := getStatusString(StatusShipped)

	if actualStatus == pending && (status == shipped || status == cancelled) {
		return true
	} else if actualStatus == shipped && status == delivered {
		return true
	}

	return false
}

func (om *OrdersManager) ChangeStatus(id, newStatus int) {
	if len(om.Orders) == 0 {
		fmt.Println("ChangeStatus(): The Orders registry is empty")
		return
	}

	idlist := []int{}
	for oid, _ := range om.Orders {
		idlist = append(idlist, oid)
	}

	if !slices.Contains(idlist, id) {
		fmt.Println("ChangeStatus(): the id of the entered order does not exist in the registry")
		return
	}

	if om.verifyStatus(id, newStatus) {
		om.Orders[id] = getStatusString(newStatus)
		fmt.Printf("ChangeStatus(): The status has been changed to: %s\n", om.Orders[id])
		return
	}

	fmt.Println("ChangeStatus(): The status can not be changed")
	return
}

func (om *OrdersManager) ViewAllOrders() {
	for id, order := range om.Orders {
		fmt.Printf("Order ID: %d, Order Status: %s\n", id, order)
	}
}
func (om *OrdersManager) OrderStatus() {
	var pending int
	var cancelled int
	var delivered int
	var shipped int

	for _, orderStatus := range om.Orders {
		switch orderStatus {
		case "Delivered":
			delivered += 1
		case "Pending":
			pending += 1
		case "Shipped":
			shipped += 1
		case "Cancelled":
			cancelled += 1
		default:
			continue
		}
	}

	if pending > 0 {
		fmt.Printf("NumberOfOrders: %d\n Status: 📦 Pending, Description: Your order is confirmed and being prepared for shipment. We’re working to get it to you soon!\n", pending)
	}

	if shipped > 0 {
		fmt.Printf("NumberOfOrders: %d\n Status: 🚚 Shipped, Description: Your order is on the way! Track your package using the link provided in your email.\n", shipped)
	}

	if delivered > 0 {
		fmt.Printf("NumberOfOrders: %d\n Status: ✅ Delivered, Description: Your order has arrived! Enjoy your purchase, and thank you for choosing us.\n", delivered)
	}

	if cancelled > 0 {
		fmt.Printf("NumberOfOrders: %d\n Status: ❌ Canceled, Description: This order has been canceled and will not be processed further.\n", cancelled)
	}
}

func main() {
	// Tarea exploratoria: Pansando número y luego constantes
	fmt.Printf("ViewDay(0): %v\n", ViewDay(0))
	fmt.Printf("ViewDay(1): %v\n", ViewDay(1))
	fmt.Printf("ViewDay(2): %v\n", ViewDay(2))
	fmt.Printf("ViewDay(3): %v\n", ViewDay(3))
	fmt.Printf("ViewDay(4): %v\n", ViewDay(4))
	fmt.Printf("ViewDay(5): %v\n", ViewDay(5))
	fmt.Printf("ViewDay(6): %v\n", ViewDay(6))
	fmt.Printf("ViewDay(7): %v\n", ViewDay(7))
	fmt.Printf("ViewDay(8): %v\n", ViewDay(8))

	fmt.Printf("ViewDay(day1): %v\n", ViewDay(day1))
	fmt.Printf("ViewDay(day2): %v\n", ViewDay(day2))
	fmt.Printf("ViewDay(day3): %v\n", ViewDay(day3))
	fmt.Printf("ViewDay(day4): %v\n", ViewDay(day4))
	fmt.Printf("ViewDay(day5): %v\n", ViewDay(day5))
	fmt.Printf("ViewDay(day6): %v\n", ViewDay(day6))
	fmt.Printf("ViewDay(day7): %v\n", ViewDay(day7))
	fmt.Printf("ViewDay(emptyDay): %v\n", ViewDay(emptyDay))

	// Extra
	manager := NewOrdesManager()
	for {
		var option int
		fmt.Printf("Option 1: Register Orders \n Option 2: Change status \n Option 3: See All commands\n Option 4: See States of orders \n Option 5: Exit \n")
		fmt.Scan(&option)
		switch option {
		case 1:
			manager.RegisterOrder()
		case 2:
			fmt.Println("Enter the orderId:")
			var id int
			fmt.Scan(&id)
			fmt.Println("Enter the new Status from options:")
			fmt.Println(StatusOptions)
			var status int
			fmt.Scan(&status)
			manager.ChangeStatus(id, status)
		case 3:
			manager.ViewAllOrders()
		case 4:
			manager.OrderStatus()
		case 5:
			return
		default:
			continue
		}
	}

}
