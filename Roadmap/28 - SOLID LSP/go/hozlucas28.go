package main

import (
	"errors"
	"fmt"
	"math"
)

/* -------------------------------------------------------------------------- */
/*                                 INTERFACES                                 */
/* -------------------------------------------------------------------------- */

type BadShape interface {
	GetArea() (float64, error)
}

type GoodShape interface {
	GetArea() float64
}

type Vehicle interface {
	Brake()
	SpeedUp()
}

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

func BadGetArea(shape BadShape) (float64, error) {
	return shape.GetArea()
}

func GoodGetArea(shape GoodShape) float64 {
	return shape.GetArea()
}

func Brake(vehicle Vehicle) {
	vehicle.Brake()
}

func SpeedUp(vehicle Vehicle) {
	vehicle.SpeedUp()
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* ------------------------------ BadRectangle ------------------------------ */

type badRectangle struct {
	Height float64
	Width  float64
	_      struct{}
}

func NewBadRectangle(height float64, width float64) BadShape {
	var rectangle badRectangle = badRectangle{Height: height, Width: width}
	return &rectangle
}

func (rectangle *badRectangle) GetArea() (float64, error) {
	return rectangle.Height * rectangle.Width, nil
}

/* -------------------------------- BadCircle ------------------------------- */

type badCircle struct {
	Radius float64
	_      struct{}
}

func NewBadCircle(radius float64) BadShape {
	var circle badCircle = badCircle{Radius: radius}
	return &circle
}

func (circle *badCircle) GetArea() (float64, error) {
	return 0, errors.New("Area calculation method of circle is not implemented")
}

/* ------------------------------ GoodRectangle ----------------------------- */

type goodRectangle struct {
	Height float64
	Width  float64
	_      struct{}
}

func NewGoodRectangle(height float64, width float64) GoodShape {
	var rectangle goodRectangle = goodRectangle{Height: height, Width: width}
	return &rectangle
}

func (rectangle *goodRectangle) GetArea() float64 {
	return rectangle.Height * rectangle.Width
}

/* ------------------------------- GoodCircle ------------------------------- */

type goodCircle struct {
	Radius float64
	_      struct{}
}

func NewGoodCircle(radius float64) GoodShape {
	var circle goodCircle = goodCircle{Radius: radius}
	return &circle
}

func (circle *goodCircle) GetArea() float64 {
	return math.Pi * math.Pow(circle.Radius, 2)
}

/* ----------------------------------- Car ---------------------------------- */

type car struct{}

func NewCar() Vehicle {
	var car car = car{}
	return &car
}

func (car *car) Brake() {
	fmt.Println("Car braking!")
}

func (car *car) SpeedUp() {
	fmt.Println("Car speeding up!")
}

/* ---------------------------------- Truck --------------------------------- */

type truck struct{}

func NewTruck() Vehicle {
	var truck truck = truck{}
	return &truck
}

func (truck *truck) Brake() {
	fmt.Println("Truck braking!")
}

func (truck *truck) SpeedUp() {
	fmt.Println("Truck speeding up!")
}

/* ---------------------------------- Boat ---------------------------------- */

type boat struct{}

func NewBoat() Vehicle {
	var boat boat = boat{}
	return &boat
}

func (boat *boat) Brake() {
	fmt.Println("Boat braking!")
}

func (boat *boat) SpeedUp() {
	fmt.Println("Boat speeding up!")
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Liskov Substitution Principle (LCP)...
	*/

	fmt.Println("Liskov Substitution Principle (LCP)...")

	fmt.Println("\nBad implementation of Liskov Substitution Principle (LCP)...")

	fmt.Println("\n```\n" + `type BadShape interface {
  GetArea() (float64, error)
}

func BadGetArea(shape BadShape) (float64, error) {
  return shape.GetArea()
}

type badRectangle struct {
  Height float64
  Width  float64
  _      struct{}
}

func NewBadRectangle(height float64, width float64) BadShape {
  var rectangle badRectangle = badRectangle{Height: height, Width: width}
  return &rectangle
}

func (rectangle *badRectangle) GetArea() (float64, error) {
  return rectangle.Height * rectangle.Width, nil
}

type badCircle struct {
  Radius float64
  _      struct{}
}

func NewBadCircle(radius float64) BadShape {
  var circle badCircle = badCircle{Radius: radius}
  return &circle
}

func (circle *badCircle) GetArea() (float64, error) {
  return 0, errors.New("Area calculation method of circle is not implemented")
}` + "\n```")

	fmt.Println(
		"\nThis is a bad implementation of Liskov Substitution Principle (LCP),\n" +
			"because the 'BadGetArea' method of 'badCircle' is no implemented. So, if we\n" +
			"execute the 'BadGetArea' function with both classes ('badRectangle', and 'badCircle')\n" +
			"the function will produce different side effects that could be break the function execution.\n" +
			"Thus the 'BadShape' interface can not be replaced by 'badCircle' class.",
	)

	fmt.Println("\nGood implementation of Liskov Substitution Principle (LCP)...")

	fmt.Println("\n```\n" + `type GoodShape interface {
  GetArea() float64
}

func GoodGetArea(shape GoodShape) float64 {
  return shape.GetArea()
}

type goodRectangle struct {
  Height float64
  Width  float64
  _      struct{}
}

func NewGoodRectangle(height float64, width float64) GoodShape {
  var rectangle goodRectangle = goodRectangle{Height: height, Width: width}
  return &rectangle
}

func (rectangle *goodRectangle) GetArea() float64 {
  return rectangle.Height * rectangle.Width
}

type goodCircle struct {
  Radius float64
  _      struct{}
}

func NewGoodCircle(radius float64) GoodShape {
  var circle goodCircle = goodCircle{Radius: radius}
  return &circle
}

func (circle *goodCircle) GetArea() float64 {
  return math.Pi * math.Pow(circle.Radius, 2)
}` + "\n```")

	fmt.Println(
		"\nThis is a good implementation of Liskov Substitution Principle (LCP),\n" +
			"because all classes which implements 'GoodShape' interface implements the\n" +
			"'GoodGetArea' method with the same side effect. So, if we execute the 'GoodGetArea'\n" +
			"function with both classes ('GoodRectangle', and 'GoodCircle'), we are not going to\n" +
			"have side effects that could break the function execution. Thus the 'GoodShape' interface\n" +
			"can be replaced by any of these classes.",
	)

	fmt.Println(
		"\n# ---------------------------------------------------------------------------------- #",
	)

	/*
	   Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	var car Vehicle = NewCar()
	var truck Vehicle = NewTruck()
	var boat Vehicle = NewBoat()

	fmt.Println()
	SpeedUp(car)
	SpeedUp(truck)
	SpeedUp(boat)

	fmt.Println()
	Brake(car)
	Brake(truck)
	Brake(boat)
}
