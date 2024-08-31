package main

import (
	"errors"
	"fmt"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                               WEEKDAYS (ENUM)                              */
/* -------------------------------------------------------------------------- */

type Weekday int

func (weekday *Weekday) ToString() string {
	switch *weekday {
	case monday:
		return "Monday"
	case tuesday:
		return "Tuesday"
	case wednesday:
		return "Wednesday"
	case thursday:
		return "Thursday"
	case friday:
		return "Friday"
	case saturday:
		return "Saturday"
	default:
		return "Sunday"
	}
}

type weekDays struct {
	Monday    Weekday
	Tuesday   Weekday
	Wednesday Weekday
	Thursday  Weekday
	Friday    Weekday
	Saturday  Weekday
	Sunday    Weekday
}

const (
	monday Weekday = iota
	tuesday
	wednesday
	thursday
	friday
	saturday
	sunday
)

var WeekDays weekDays = weekDays{
	Monday:    monday,
	Tuesday:   tuesday,
	Wednesday: wednesday,
	Thursday:  thursday,
	Friday:    friday,
	Saturday:  saturday,
	Sunday:    sunday,
}

/* -------------------------------------------------------------------------- */
/*                                STATES (ENUM)                               */
/* -------------------------------------------------------------------------- */

type State int

func (state *State) ToString() string {
	switch *state {
	case earring:
		return "Earring"
	case sent:
		return "Sent"
	case delivered:
		return "Delivered"
	default:
		return "Cancelled"
	}
}

type states struct {
	Earring   State
	Sent      State
	Delivered State
	Cancelled State
}

const (
	earring State = iota
	sent
	delivered
	cancelled
)

var States states = states{
	Earring:   earring,
	Sent:      sent,
	Delivered: delivered,
	Cancelled: cancelled,
}

/* -------------------------------------------------------------------------- */
/*                                ORDER (CLASS)                               */
/* -------------------------------------------------------------------------- */

type order struct {
	id    int
	state State
}

func NewOrder(id int, state State) *order {
	var order order = order{id: id, state: state}
	return &order
}

func (order *order) GetId() int {
	return order.id
}

func (order *order) GetState() State {
	return order.state
}

func (order *order) Cancel() error {
	if order.state == States.Earring {
		order.state = States.Cancelled
		return nil
	}

	var errorMessage string = fmt.Sprintf("The order with %d id can't be cancelled", order.id)
	return errors.New(errorMessage)
}

func (order *order) Deliver() error {
	if order.state == States.Sent {
		order.state = States.Delivered
		return nil
	}

	var errorMessage string = fmt.Sprintf("The order with %d id can't be delivered", order.id)
	return errors.New(errorMessage)
}

func (order *order) PrintState() *order {
	var loweredOrderState string = strings.ToLower(order.state.ToString())
	fmt.Printf("The order with %d id was %s\n", order.id, loweredOrderState)
	return order
}

func (order *order) Send() error {
	if order.state == States.Earring {
		order.state = States.Sent
		return nil
	}

	var errorMessage string = fmt.Sprintf("The order with %d id can't be sent", order.id)
	return errors.New(errorMessage)
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Enums...
	*/

	fmt.Println("Enums...")

	fmt.Printf("\nName of the first week day: %s\n", WeekDays.Monday.ToString())
	fmt.Printf("Name of the second week day: %s\n", WeekDays.Tuesday.ToString())
	fmt.Printf("Name of the third week day: %s\n", WeekDays.Wednesday.ToString())
	fmt.Printf("Name of the fourth week day: %s\n", WeekDays.Thursday.ToString())
	fmt.Printf("Name of the fifth week day: %s\n", WeekDays.Friday.ToString())
	fmt.Printf("Name of the sixth week day: %s\n", WeekDays.Saturday.ToString())
	fmt.Printf("Name of the seventh week day: %s\n", WeekDays.Sunday.ToString())

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
		Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	var firstOrder *order = NewOrder(1, States.Earring)
	var secondOrder *order = NewOrder(2, States.Sent)
	var thirdOrder *order = NewOrder(3, States.Delivered)
	var fourthOrder *order = NewOrder(4, States.Cancelled)

	fmt.Println()
	firstOrder.PrintState()
	secondOrder.PrintState()
	thirdOrder.PrintState()
	fourthOrder.PrintState()

	firstOrder.Send()
	firstOrder.Deliver()

	fmt.Println()
	firstOrder.PrintState()

	fmt.Println()
	sendError := secondOrder.Send()
	if sendError != nil {
		fmt.Println(sendError)
	}

	var deliveredError error = thirdOrder.Deliver()
	if deliveredError != nil {
		fmt.Println(deliveredError)
	}

	sendError = fourthOrder.Send()
	if sendError != nil {
		fmt.Println(sendError)
	}
}