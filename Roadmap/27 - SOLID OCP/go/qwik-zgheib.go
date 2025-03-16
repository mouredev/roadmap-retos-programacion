package main

import (
	"errors"
	"fmt"
	"math"
)

/* -- exercise */
/* incorrect */

type Invoice struct {
	Amount       float64
	IsDiscounted bool
}

func (i *Invoice) CalculateTotal() float64 {
	if i.IsDiscounted {
		return i.Amount * 0.9
	}
	return i.Amount
}

/* correct */

type InvoiceC interface {
	CalculateTotal() float64
}

type RegularInvoice struct {
	Amount float64
}

func (i RegularInvoice) CalculateTotal() float64 {
	return i.Amount
}

type DiscountedInvoice struct {
	Amount       float64
	DiscountRate float64
}

func (i DiscountedInvoice) CalculateTotal() float64 {
	return i.Amount * (1 - i.DiscountRate)
}

/* -- extra challenge */

type Operation interface {
	Calculate(a, b float64) (float64, error)
}

type Addition struct{}

func (Addition) Calculate(a, b float64) (float64, error) {
	return a + b, nil
}

type Subtraction struct{}

func (Subtraction) Calculate(a, b float64) (float64, error) {
	return a - b, nil
}

type Multiplication struct{}

func (Multiplication) Calculate(a, b float64) (float64, error) {
	return a * b, nil
}

type Division struct{}

func (Division) Calculate(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("cannot divide by zero")
	}
	return a / b, nil
}

type Calculator struct {
	operations map[string]Operation
}

func NewCalculator() *Calculator {
	return &Calculator{
		operations: make(map[string]Operation),
	}
}

func (c *Calculator) AddOperation(name string, operation Operation) {
	c.operations[name] = operation
}

func (c *Calculator) Calculate(name string, a, b float64) (float64, error) {
	operation, found := c.operations[name]
	if !found {
		return 0, fmt.Errorf("operation %s not found", name)
	}
	return operation.Calculate(a, b)
}

type Power struct{}

func (Power) Calculate(a, b float64) (float64, error) {
	return math.Pow(a, b), nil
}

func main() {
	/* -- exercise */
	/* exercise -- incorrect */
	invoice := Invoice{Amount: 100, IsDiscounted: true}
	fmt.Printf("Total: %.2f\n", invoice.CalculateTotal())

	/* exercise -- correct */
	regularInvoice := RegularInvoice{Amount: 100}
	discountedInvoice := DiscountedInvoice{Amount: 100, DiscountRate: 0.1}

	invoices := []InvoiceC{regularInvoice, discountedInvoice}

	for _, invoice := range invoices {
		fmt.Printf("Total: %.2f\n", invoice.CalculateTotal())
	}

	/* extra challenge */
	calculator := NewCalculator()

	calculator.AddOperation("add", Addition{})
	calculator.AddOperation("subtract", Subtraction{})
	calculator.AddOperation("multiply", Multiplication{})
	calculator.AddOperation("divide", Division{})
	calculator.AddOperation("power", Power{})

	a, b := 6.0, 2.0

	result, _ := calculator.Calculate("add", a, b)
	fmt.Printf("Add: %.2f + %.2f = %.2f\n", a, b, result)

	result, _ = calculator.Calculate("subtract", a, b)
	fmt.Printf("Subtract: %.2f - %.2f = %.2f\n", a, b, result)

	result, _ = calculator.Calculate("multiply", a, b)
	fmt.Printf("Multiply: %.2f * %.2f = %.2f\n", a, b, result)

	result, err := calculator.Calculate("divide", a, b)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Printf("Divide: %.2f / %.2f = %.2f\n", a, b, result)
	}

	result, _ = calculator.Calculate("power", a, b)
	fmt.Printf("Power: %.2f ^ %.2f = %.2f\n", a, b, result)
}
