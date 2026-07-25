package main

import (
	"errors"
	"fmt"
	"os"
	"os/exec"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                                   ERRORS                                   */
/* -------------------------------------------------------------------------- */

/* ----------------------- CalendarCellDiscoveredError ---------------------- */

type CalendarCellDiscoveredError struct {
	Cell CalendarCell
	_    struct{}
}

func (err CalendarCellDiscoveredError) Error() string {
	return fmt.Sprintf(
		"%d calendar cell is already discovered",
		err.Cell.Id,
	)
}

/* ------------------------ CalendarDayNotFoundError ------------------------ */

type CalendarDayNotFoundError struct {
	Day uint16
	_   struct{}
}

func (err *CalendarDayNotFoundError) Error() string {
	return fmt.Sprintf(
		"%d calendar day not found",
		err.Day,
	)
}

/* ------------------------ CalendarDayOuOfRangeError ----------------------- */

type CalendarDayOuOfRangeError struct {
	Day  uint16
	From uint16
	To   uint16
	_    struct{}
}

func (err *CalendarDayOuOfRangeError) Error() string {
	return fmt.Sprintf(
		"%d calendar day is out of range, it must be between %d and %d (both included)",
		err.Day,
		err.From,
		err.To,
	)
}

/* -------------------------------------------------------------------------- */
/*                                   STRUCTS                                  */
/* -------------------------------------------------------------------------- */

/* ------------------------------ CalendarCell ------------------------------ */

type CalendarCell struct {
	Discovered bool
	Id         uint16
	_          struct{}
}

/* -------------------------------- Calendar -------------------------------- */

type Calendar interface {
	GetArray2D() [][]CalendarCell
	GetFrom() uint16
	GetTo() uint16

	DiscoverDay(day uint16) error
	ToPrint() string
}

const rows uint16 = 4
const cols uint16 = 6

type calendar struct {
	array2D [][]CalendarCell
	from    uint16
	to      uint16
}

func NewCalendar(from uint16, to uint16) Calendar {
	var counter uint16 = from

	var calendar calendar = calendar{
		array2D: make([][]CalendarCell, rows),
		from:    from,
		to:      to,
	}

	for i := range calendar.array2D {
		calendar.array2D[i] = make([]CalendarCell, cols)
		for j := range calendar.array2D[i] {
			calendar.array2D[i][j].Id = counter
			counter++
		}
	}

	return &calendar
}

func (calendar *calendar) GetArray2D() [][]CalendarCell {
	return calendar.array2D
}

func (calendar *calendar) GetFrom() uint16 {
	return calendar.from
}

func (calendar *calendar) GetTo() uint16 {
	return calendar.to
}

func (calendar *calendar) DiscoverDay(day uint16) error {
	var i int
	var j int
	var flag bool = false
	var counter uint16 = calendar.from

	if day < calendar.from || day > calendar.to {
		return &CalendarDayOuOfRangeError{
			Day:  day,
			From: calendar.from,
			To:   calendar.to,
		}
	}

	for i = 0; counter <= calendar.to && i < len(calendar.array2D); i++ {
		for j = 0; counter <= calendar.to && j < len(calendar.array2D[i]); j++ {
			if calendar.array2D[i][j].Id == day {
				if calendar.array2D[i][j].Discovered {
					return &CalendarCellDiscoveredError{
						Cell: calendar.array2D[i][j],
					}
				}

				calendar.array2D[i][j].Discovered = true
				flag = true
				break
			}

			counter++
		}

		if flag {
			break
		}
	}

	if !flag {
		return &CalendarDayNotFoundError{Day: day}
	}

	return nil
}

func (calendar *calendar) ToPrint() string {
	var calendarPrintable []string = []string{}

	var i int
	var j int
	var counter uint16 = calendar.from

	var row []CalendarCell
	var col CalendarCell
	var rowPrintable string

	for i = 0; counter <= calendar.to && i < len(calendar.array2D); i++ {
		row = calendar.array2D[i]

		rowPrintable = ""
		if i != 0 {
			rowPrintable = "\n"
		}

		rowPrintable += strings.TrimSpace(
			strings.Repeat(
				strings.Repeat("*", 4)+" ", len(row),
			),
		) + "\n"

		for j = 0; counter <= calendar.to && j < len(row); j++ {
			col = row[j]

			rowPrintable += "*"
			if col.Discovered {
				rowPrintable += strings.Repeat("*", 2)
			} else {
				rowPrintable += fmt.Sprintf("%02d", col.Id)
			}
			rowPrintable += "* "

			counter++
		}

		rowPrintable = strings.TrimSpace(rowPrintable) + "\n"

		rowPrintable += strings.TrimSpace(
			strings.Repeat(
				strings.Repeat("*", 4)+" ", len(row),
			),
		)

		if i != len(calendar.array2D)-1 {
			rowPrintable += "\n"
		}

		calendarPrintable = append(calendarPrintable, rowPrintable)
	}

	return strings.Join(calendarPrintable, "\n")
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var calendar Calendar = NewCalendar(1, 24)

	var input01 uint16
	var input02 uint16
	var cmd *exec.Cmd

	var err error
	var calendarDayOuOfRangeError *CalendarDayOuOfRangeError
	var calendarCellDiscoveredError *CalendarCellDiscoveredError
	var calendarDayNotFoundError *CalendarDayNotFoundError

	fmt.Printf("%s\n", calendar.ToPrint())

	fmt.Println(
		"\n> Available operations...\n\n",
		"  1 - Discover day.\n",
		"  0 - Exit.",
	)

	fmt.Printf("\n> Enter an operation: ")
	fmt.Scanf("%d\n", &input01)

	for input01 != 0 {
		switch input01 {
		case 1:
			fmt.Printf("\n> Enter the day to discover: ")
			fmt.Scanf("%d\n", &input02)

			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			err = calendar.DiscoverDay(input02)
			if err == nil {
				fmt.Printf("> Day %d discovered!\n", input02)
				break
			}

			if errors.As(err, &calendarDayOuOfRangeError) {
				fmt.Printf(
					"> The day %d must be between %d and %d (both included)!",
					input02,
					calendar.GetFrom(),
					calendar.GetTo(),
				)
			} else if errors.As(err, &calendarCellDiscoveredError) {
				fmt.Printf("> The day %d is already discovered!\n", input02)
			} else if errors.As(err, &calendarDayNotFoundError) {
				fmt.Printf("> %d day not found in the calendar!\n", input02)
			} else {
				fmt.Println("> An error occurred on discover the day!")
			}
			break

		default:
			cmd = exec.Command("clear")
			cmd.Stdout = os.Stdout
			cmd.Run()

			fmt.Println("\n> Invalid operation! Try again...")
		}

		fmt.Printf("\n%s\n", calendar.ToPrint())

		fmt.Println(
			"\n> Available operations...\n\n",
			"  1 - Discover day.\n",
			"  0 - Exit.",
		)

		fmt.Printf("\n> Enter an operation: ")
		fmt.Scanf("%d\n", &input01)
	}
}
