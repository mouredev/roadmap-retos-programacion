package main

import "fmt"

type DayOfWeek int

const (
	Monday DayOfWeek = iota + 1
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
	Sunday
)

func (d DayOfWeek) String() string {
	return [...]string{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}[d-1]
}

type OrderStatus int

const (
	Pending OrderStatus = iota
	Shipped
	Delivered
	Canceled
)

func (os OrderStatus) String() string {
	return [...]string{"Pending", "Shipped", "Delivered", "Canceled"}[os]
}

type Order struct {
	ID     int
	Status OrderStatus
}

func NewOrder(id int) *Order {
	return &Order{
		ID:     id,
		Status: Pending,
	}
}

func (o *Order) Send() error {
	if o.Status != Pending {
		return fmt.Errorf("order cannot be shipped unless it is pending")
	}
	o.Status = Shipped
	return nil
}

func (o *Order) Cancel() error {
	if o.Status == Delivered {
		return fmt.Errorf("order cannot be canceled after it is delivered")
	}
	o.Status = Canceled
	return nil
}

func (o *Order) Deliver() error {
	if o.Status != Shipped {
		return fmt.Errorf("order cannot be delivered unless it is shipped")
	}
	o.Status = Delivered
	return nil
}

func (o *Order) Description() string {
	return fmt.Sprintf("order #%d is currently %s", o.ID, o.Status)
}

func main() {
	for i := Monday; i <= Sunday; i++ {
		fmt.Println(i.String())
	}

	order1 := NewOrder(1)
	fmt.Println(order1.Description())

	err := order1.Send()
	if err != nil {
		fmt.Println("Err:", err)
	}
	fmt.Println(order1.Description())

	err = order1.Deliver()
	if err != nil {
		fmt.Println("Err:", err)
	}
	fmt.Println(order1.Description())

	order2 := NewOrder(2)
	fmt.Println(order2.Description())

	err = order2.Cancel()
	if err != nil {
		fmt.Println("Err:", err)
	}
	fmt.Println(order2.Description())
}
