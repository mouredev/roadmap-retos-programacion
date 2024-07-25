package main

import (
	"fmt"
)

/* -------------------------------------------------------------------------- */
/*                                 INTERFACES                                 */
/* -------------------------------------------------------------------------- */

type BadVehicle interface {
	Drive()
	Fly()
}

type AirVehicle interface {
	Fly()
}

type LandVehicle interface {
	Drive()
}

type BlackAndWhitePrinter interface {
	Print()
}

type ColorPrinter interface {
	Print()
}

type MultifunctionalPrinter interface {
	Print()
	Scan()
	SendFax()
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* ------------------------------- BadAirplane ------------------------------ */

type badAirplane struct{}

func NewBadAirplane() BadVehicle {
	var airplane badAirplane = badAirplane{}
	return &airplane
}

func (airplane *badAirplane) Drive() {
	panic("Airplanes do not drive")

}

func (airplane *badAirplane) Fly() {
	fmt.Println("The airplane is flying!")
}

/* --------------------------------- BadCar --------------------------------- */

type badCar struct{}

func NewBadCar() BadVehicle {
	var car badCar = badCar{}
	return &car
}

func (car *badCar) Drive() {
	fmt.Println("The car is driving!")
}

func (car *badCar) Fly() {
	panic("Cars do not fly")
}

/* ------------------------------ GoodAirplane ------------------------------ */

type goodAirplane struct{}

func NewGoodAirplane() AirVehicle {
	var airplane goodAirplane = goodAirplane{}
	return &airplane
}

func (airplane *goodAirplane) Fly() {
	fmt.Println("The airplane is flying!")
}

/* --------------------------------- GoodCar -------------------------------- */

type goodCar struct{}

func NewGoodCar() LandVehicle {
	var car goodCar = goodCar{}
	return &car
}

func (car *goodCar) Drive() {
	fmt.Println("The car is driving!")
}

/* -------------------------- BlackAndWhitePrinter -------------------------- */

type blackAndWhitePrinter struct{}

func NewBlackAndWhitePrinter() BlackAndWhitePrinter {
	var printer blackAndWhitePrinter = blackAndWhitePrinter{}
	return &printer
}

func (printer *blackAndWhitePrinter) Print() {
	fmt.Println("Paper printed in black and white!")
}

/* ------------------------------ ColorPrinter ------------------------------ */

type colorPrinter struct{}

func NewColorPrinter() ColorPrinter {
	var printer colorPrinter = colorPrinter{}
	return &printer
}

func (printer *colorPrinter) Print() {
	fmt.Println("Paper printed in color!")
}

/* ------------------------- MultifunctionalPrinter ------------------------- */

type multifunctionalPrinter struct{}

func NewMultifunctionalPrinter() MultifunctionalPrinter {
	var printer multifunctionalPrinter = multifunctionalPrinter{}
	return &printer
}

func (printer *multifunctionalPrinter) Print() {
	fmt.Println("Paper printed!")
}

func (printer *multifunctionalPrinter) Scan() {
	fmt.Println("Scan completed!")
}

func (printer *multifunctionalPrinter) SendFax() {
	fmt.Println("Fax sent!")
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Interface Segregation Principle (ISP)...
	*/

	fmt.Println("Interface Segregation Principle (ISP)...")

	fmt.Println("\nBad implementation of Interface Segregation Principle (ISP)...")

	fmt.Println("\n```\n" + `type BadVehicle interface {
  Drive()
  Fly()
}

type badAirplane struct{}

func NewBadAirplane() BadVehicle {
  var airplane badAirplane = badAirplane{}
  return &airplane
}

func (airplane *badAirplane) Drive() {
  panic("Airplanes do not drive")

}

func (airplane *badAirplane) Fly() {
  fmt.Println("The airplane is flying!")
}

type badCar struct{}

func NewBadCar() BadVehicle {
  var car badCar = badCar{}
  return &car
}

func (car *badCar) Drive() {
  fmt.Println("The car is driving!")
}

func (car *badCar) Fly() {
  panic("Cars do not fly")
}` + "\n```")

	fmt.Println(
		"\nThis is a bad implementation of Interface Segregation Principle (ISP),\n" +
			"because the 'badAirplane' class and the 'badCar' class should not implement\n" +
			"an interface with methods that they are going to never use. So, the implemented\n" +
			"interface ('BadVehicle') is to general for both classes.",
	)

	fmt.Println("\nGood implementation of Interface Segregation Principle (ISP)...")

	fmt.Println("\n```\n" + `type AirVehicle interface {
  Fly()
}

type LandVehicle interface {
  Drive()
}

type goodAirplane struct{}

func NewGoodAirplane() AirVehicle {
  var airplane goodAirplane = goodAirplane{}
  return &airplane
}

func (airplane *goodAirplane) Fly() {
  fmt.Println("The airplane is flying!")
}

type goodCar struct{}

func NewGoodCar() LandVehicle {
  var car goodCar = goodCar{}
  return &car
}

func (car *goodCar) Drive() {
  fmt.Println("The car is driving!")
}` + "\n```")

	fmt.Println(
		"\nThis is a good implementation of Interface Segregation Principle (ISP),\n" +
			"because the 'goodAirplane' class and the 'goodCar' class only implements\n" +
			"the necessary methods, without any extras.",
	)

	fmt.Println(
		"\n# ---------------------------------------------------------------------------------- #",
	)

	/*
	   Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	var blackAndWhitePrinter BlackAndWhitePrinter = NewBlackAndWhitePrinter()
	var colorPrinter ColorPrinter = NewColorPrinter()
	var multifunctionalPrinter MultifunctionalPrinter = NewMultifunctionalPrinter()

	fmt.Println()
	blackAndWhitePrinter.Print()

	fmt.Println()
	colorPrinter.Print()

	fmt.Println()
	multifunctionalPrinter.Print()

	fmt.Println()
	multifunctionalPrinter.Scan()

	fmt.Println()
	multifunctionalPrinter.SendFax()
}
