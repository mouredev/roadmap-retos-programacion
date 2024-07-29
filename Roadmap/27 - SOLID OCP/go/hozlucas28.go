package main

import (
	"errors"
	"fmt"
	"math"
)

/* -------------------------------------------------------------------------- */
/*                           CLASSES AND INTERFACES                           */
/* -------------------------------------------------------------------------- */

/* ---------------------------- BadCircle (class) --------------------------- */

type BadCircle struct {
	radius float64
	_      struct{}
}

/* -------------------------- BadRectangle (class) -------------------------- */

type BadRectangle struct {
	height float64
	width  float64
	_      struct{}
}

/* -------------------------- BadCalculator (class) ------------------------- */

type BadCalculator struct{}

func (calculator BadCalculator) GetArea(shape interface{}) float64 {
	switch shape := shape.(type) {
	case BadCircle:
		return math.Pi * math.Pow(shape.radius, 2)

	case BadRectangle:
		return shape.height * shape.width

	default:
		return -1
	}
}

/* ---------------------------- Shape (interface) --------------------------- */

type Shape interface {
	GetArea() float64
}

/* --------------------------- GoodCircle (class) --------------------------- */

type goodCircle struct {
	radius float64
	_      struct{}
}

func NewGoodCircle(radius float64) Shape {
	var circle goodCircle = goodCircle{radius: radius}
	return &circle
}

func (circle *goodCircle) GetArea() float64 {
	return math.Pi * math.Pow(circle.radius, 2)
}

/* -------------------------- GoodRectangle (class) ------------------------- */

type goodRectangle struct {
	height float64
	width  float64
	_      struct{}
}

func NewGoodRectangle(height float64, width float64) Shape {
	var rectangle goodRectangle = goodRectangle{height: height, width: width}
	return &rectangle
}

func (rectangle *goodRectangle) GetArea() float64 {
	return rectangle.height * rectangle.width
}

/* ------------------ GoodCalculator (class And Interface) ------------------ */

type IGoodCalculator interface {
	GetArea(shape Shape) float64
}

type goodCalculator struct{}

func NewGoodCalculator() IGoodCalculator {
	var calculator goodCalculator = goodCalculator{}
	return &calculator
}

func (calculator *goodCalculator) GetArea(shape Shape) float64 {
	return shape.GetArea()
}

/* -------------------------- Operation (interface) ------------------------- */

type Operation interface {
	Execute(a float64, b float64) (float64, error)
}

/* -------------------------- AddOperation (class) -------------------------- */

type addOperation struct{}

func NewAddOperation() Operation {
	var add addOperation = addOperation{}
	return &add
}

func (operation *addOperation) Execute(a float64, b float64) (float64, error) {
	return a + b, nil
}

/* ------------------------- DivideOperation (class) ------------------------ */

type divideOperation struct{}

func NewDivideOperation() Operation {
	var divide divideOperation = divideOperation{}
	return &divide
}

func (operation *divideOperation) Execute(a float64, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("The second parameter must not be zero")
	}

	return a / b, nil

}

/* ------------------------ MultiplyOperation (class) ----------------------- */

type multiplyOperation struct{}

func NewMultiplyOperation() Operation {
	var multiply multiplyOperation = multiplyOperation{}
	return &multiply
}

func (operation *multiplyOperation) Execute(a float64, b float64) (float64, error) {
	return a * b, nil

}

/* -------------------------- PowOperation (class) -------------------------- */

type powOperation struct{}

func NewPowOperation() Operation {
	var pow powOperation = powOperation{}
	return &pow
}

func (operation *powOperation) Execute(a float64, b float64) (float64, error) {
	return math.Pow(a, b), nil

}

/* ------------------------ SubtractOperation (class) ----------------------- */

type subtractOperation struct{}

func NewSubtractOperation() Operation {
	var subtract subtractOperation = subtractOperation{}
	return &subtract
}

func (operation *subtractOperation) Execute(a float64, b float64) (float64, error) {
	return a - b, nil

}

/* ------------------------------- Calculator ------------------------------- */

type ICalculator interface {
	AddOperation(name string, operation *Operation) error
	ExecuteOperation(name string, a float64, b float64) (float64, error)
}

type calculator struct {
	operations map[string](*Operation)
	_          struct{}
}

func NewCalculator() ICalculator {
	var calculator calculator = calculator{operations: map[string]*Operation{}}
	return &calculator
}

func (calculator *calculator) AddOperation(name string, operation *Operation) error {
	_, operationExist := calculator.operations[name]
	if operationExist {
		return fmt.Errorf("The operation with '%s' name already exist", name)
	}

	calculator.operations[name] = operation
	return nil
}

func (calculator *calculator) ExecuteOperation(name string, a float64, b float64) (float64, error) {
	operation, operationExist := calculator.operations[name]
	if !operationExist {
		return 0, fmt.Errorf("There is not operation with '%s' name", name)
	}

	operationResult, err := (*operation).Execute(a, b)
	if err != nil {
		return 0, err
	}

	return operationResult, nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Open-Close Principle (OCP)...
	*/

	fmt.Println("Open-Close Principle (OCP)...")

	fmt.Println("\nBad implementation of Open-Close Principle (OCP)...")

	fmt.Println("\n```\n" + `type BadCircle struct {
  radius float64
  _      struct{}
}

type BadRectangle struct {
  height float64
  width  float64
  _      struct{}
}

type BadCalculator struct{}

func (calculator BadCalculator) GetArea(shape interface{}) float64 {
  switch shape := shape.(type) {
  case BadCircle:
    return math.Pi * math.Pow(shape.radius, 2)

  case BadRectangle:
    return shape.height * shape.width

  default:
    return -1
  }
}` + "\n```")

	fmt.Println(
		"\nThis is a bad implementation of Open-Close Principle (OCP),\n" +
			"because the method 'getArea' of struct 'BadCalculator' will must\n" +
			"change if we have to add more shapes types.",
	)

	fmt.Println("\nGood implementation of Open-Close Principle (OCP)...")

	fmt.Println("\n```\n" + `type Shape interface {
  GetArea() float64
}

type goodCircle struct {
  radius float64
  _      struct{}
}

func NewGoodCircle(radius float64) Shape {
  var circle goodCircle = goodCircle{radius: radius}
  return &circle
}

func (circle *goodCircle) GetArea() float64 {
  return math.Pi * math.Pow(circle.radius, 2)
}

type goodRectangle struct {
  height float64
  width  float64
  _      struct{}
}

func NewGoodRectangle(height float64, width float64) Shape {
  var rectangle goodRectangle = goodRectangle{height: height, width: width}
  return &rectangle
}

func (rectangle *goodRectangle) GetArea() float64 {
  return rectangle.height * rectangle.width
}

type IGoodCalculator interface {
  GetArea(shape Shape) float64
}

type goodCalculator struct{}

func NewGoodCalculator() IGoodCalculator {
  var calculator goodCalculator = goodCalculator{}
  return &calculator
}

func (calculator *goodCalculator) GetArea(shape Shape) float64 {
  return shape.GetArea()
}` + "\n```")

	fmt.Println(
		"\nThis is a good implementation of Open-Close Principle (OCP),\n" +
			"because the method 'getArea' of struct 'GoodCalculator' will must\n" +
			"not change if we have to add more shapes. So, 'getArea' is closed to modification\n" +
			"but it is open to extension throw any shape which implements 'Shape' interface.",
	)

	fmt.Println(
		"\n# ---------------------------------------------------------------------------------- #",
	)

	/*
	   Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	fmt.Println("\nTesting the OCP system without a pow operation...")

	var calculator ICalculator = NewCalculator()

	var addOperation Operation = NewAddOperation()
	var divideOperation Operation = NewDivideOperation()
	var multiplyOperation Operation = NewMultiplyOperation()
	var subtractOperation Operation = NewSubtractOperation()

	calculator.AddOperation("add", &addOperation)
	calculator.AddOperation("add", &divideOperation)
	calculator.AddOperation("multiply", &multiplyOperation)
	calculator.AddOperation("subtract", &subtractOperation)

	var a float64 = 11
	var b float64 = 8.2

	addOperationResult, _ := calculator.ExecuteOperation("add", a, b)
	fmt.Printf("\nAdd operation result (%.2f + %.2f): %f", a, b, addOperationResult)

	a, b = 5, 4.2
	divideOperationResult, _ := calculator.ExecuteOperation("divide", a, b)
	fmt.Printf("\nDivide operation result (%.2f / %.2f): %f", a, b, divideOperationResult)

	a, b = 2, 6.6
	multiplyOperationResult, _ := calculator.ExecuteOperation("multiply", a, b)
	fmt.Printf("\nMultiply operation result (%.2f * %.2f): %f", a, b, multiplyOperationResult)

	a, b = -1, -6.888
	subtractOperationResult, _ := calculator.ExecuteOperation("subtract", a, b)
	fmt.Printf("\nSubtract operation result (%.2f - %.3f): %f", a, b, subtractOperationResult)

	fmt.Println("\n\nTesting the OCP system with a pow operation...")

	var powOperation Operation = NewPowOperation()

	calculator.AddOperation("pow", &powOperation)

	a, b = 2, 10
	powOperationResult, _ := calculator.ExecuteOperation("pow", a, b)
	fmt.Printf("\nPow operation result (%.2f^%.2f): %f", a, b, powOperationResult)
}
