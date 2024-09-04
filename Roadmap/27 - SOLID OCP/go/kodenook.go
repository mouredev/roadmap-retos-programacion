package main

import "fmt"

type PaymentMethod interface {
	Pay(amount float64) string
}

type CreditCard struct{}

func (cc CreditCard) Pay(amount float64) string {
	return fmt.Sprintf("Paid %.2f using Credit Card", amount)
}

type PayPal struct{}

func (pp PayPal) Pay(amount float64) string {
	return fmt.Sprintf("Paid %.2f using PayPal", amount)
}

func ProcessPayment(pm PaymentMethod, amount float64) {
	fmt.Println(pm.Pay(amount))
}

func main() {
	cc := CreditCard{}
	pp := PayPal{}

	ProcessPayment(cc, 100.0)
	ProcessPayment(pp, 150.0)
}
