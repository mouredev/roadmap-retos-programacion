package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strings"
	"time"
)

/* -------------------------------------------------------------------------- */
/*                                   ERRORS                                   */
/* -------------------------------------------------------------------------- */

/* ----------------------------- InvalidMonthErr ---------------------------- */

type InvalidMonthErr struct {
	Month string
	_     struct{}
}

func (err *InvalidMonthErr) Error() string {
	return fmt.Sprintf("\"%s\" is an invalid month", err.Month)
}

/* --------------------------- MonthsOutOfRangeErr -------------------------- */

type MonthOutOfRangeErr struct {
	Month uint8
	_     struct{}
}

func (err *MonthOutOfRangeErr) Error() string {
	return fmt.Sprintf("%d is out of a month range", err.Month)
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* -------------------------------- YearPlan -------------------------------- */

var MONTHS [12]string = [12]string{
	"january",
	"february",
	"march",
	"april",
	"may",
	"june",
	"july",
	"august",
	"september",
	"october",
	"november",
	"december",
}

type GoalPlan struct {
	Amount uint
	Goal   Goal
}

type YearPlan struct {
	january   []GoalPlan
	february  []GoalPlan
	march     []GoalPlan
	april     []GoalPlan
	may       []GoalPlan
	june      []GoalPlan
	july      []GoalPlan
	august    []GoalPlan
	september []GoalPlan
	october   []GoalPlan
	november  []GoalPlan
	december  []GoalPlan
}

func (instance *YearPlan) GetMonth(month string) ([]GoalPlan, error) {
	switch month {
	case "january":
		return instance.january, nil

	case "february":
		return instance.february, nil

	case "march":
		return instance.march, nil

	case "april":
		return instance.april, nil

	case "may":
		return instance.may, nil

	case "june":
		return instance.june, nil

	case "july":
		return instance.july, nil

	case "august":
		return instance.august, nil

	case "september":
		return instance.september, nil

	case "october":
		return instance.october, nil

	case "november":
		return instance.november, nil

	case "december":
		return instance.december, nil

	}

	return nil, &InvalidMonthErr{Month: month}
}

func (instance *YearPlan) SetMonth(month string, goalPlans []GoalPlan) error {
	switch month {
	case "january":
		instance.january = goalPlans

	case "february":
		instance.february = goalPlans

	case "march":
		instance.march = goalPlans

	case "april":
		instance.april = goalPlans

	case "may":
		instance.may = goalPlans

	case "june":
		instance.june = goalPlans

	case "july":
		instance.july = goalPlans

	case "august":
		instance.august = goalPlans

	case "september":
		instance.september = goalPlans

	case "october":
		instance.october = goalPlans

	case "november":
		instance.november = goalPlans

	case "december":
		instance.december = goalPlans

	default:
		return &InvalidMonthErr{Month: month}
	}

	return nil
}

func (instance *YearPlan) Append(month string, goalPlan GoalPlan) error {
	switch month {
	case "january":
		instance.january = append(instance.january, goalPlan)

	case "february":
		instance.february = append(instance.february, goalPlan)

	case "march":
		instance.march = append(instance.march, goalPlan)

	case "april":
		instance.april = append(instance.april, goalPlan)

	case "may":
		instance.may = append(instance.may, goalPlan)

	case "june":
		instance.june = append(instance.june, goalPlan)

	case "july":
		instance.july = append(instance.july, goalPlan)

	case "august":
		instance.august = append(instance.august, goalPlan)

	case "september":
		instance.september = append(instance.september, goalPlan)

	case "october":
		instance.october = append(instance.october, goalPlan)

	case "november":
		instance.november = append(instance.november, goalPlan)

	case "december":
		instance.december = append(instance.december, goalPlan)

	default:
		return &InvalidMonthErr{Month: month}
	}

	return nil
}

/* ---------------------------------- Goal ---------------------------------- */

const MAX_MONTHS_LIMIT uint8 = 12

type Goal struct {
	amount      uint
	description string
	id          string
	monthsLimit uint8
	units       string
	_           struct{}
}

func NewGoal(amount uint, description string, monthsLimit uint8, units string) (*Goal, error) {
	var goal Goal = Goal{
		amount:      amount,
		description: description,
		id:          fmt.Sprintf("%s %d %s", units, amount, time.Now().Local().String()),
		units:       units,
	}

	if monthsLimit < 1 || monthsLimit > MAX_MONTHS_LIMIT {
		return nil, &MonthOutOfRangeErr{Month: monthsLimit}
	}

	goal.monthsLimit = monthsLimit

	return &goal, nil
}

func (instance *Goal) GetAmount() uint {
	return instance.amount
}

func (instance *Goal) GetDescription() string {
	return instance.description
}

func (instance *Goal) GetId() string {
	return instance.id
}

func (instance *Goal) GetMonthsLimit() uint8 {
	return instance.monthsLimit
}

func (instance *Goal) GetUnits() string {
	return instance.units
}

func (instance *Goal) ToYearPlan() YearPlan {
	var yearPlan YearPlan

	var counter uint = instance.amount
	for counter != 0 {
		var monthCounter uint8 = instance.monthsLimit
		for _, month := range MONTHS {
			if counter == 0 || monthCounter == 0 {
				break
			}

			monthGoals, err := yearPlan.GetMonth(month)
			if err != nil {
				continue
			}

			var goalPlan GoalPlan
			if len(monthGoals) == 0 {
				goalPlan.Amount = 1
				goalPlan.Goal = *instance
			} else {
				goalPlan = monthGoals[0]
				goalPlan.Amount++
			}

			yearPlan.SetMonth(month, []GoalPlan{goalPlan})

			monthCounter--
			counter--
		}
	}

	return yearPlan
}

/* -------------------------------- YearGoals ------------------------------- */

const MAX_GOALS uint = 10

type YearGoals struct {
	goals []Goal
	plan  YearPlan
	_     struct{}
}

func NewYearGoals() *YearGoals {
	var yearGoals YearGoals = YearGoals{
		goals: []Goal{},
		plan:  YearPlan{},
	}

	return &yearGoals
}

func (instance *YearGoals) GetGoals() []Goal {
	return instance.goals
}

func (instance *YearGoals) GetPlan() YearPlan {
	return instance.plan
}

func (instance *YearGoals) appendGoalToPlan(goal *Goal) {
	var goalYearPlan YearPlan = goal.ToYearPlan()

	for _, month := range MONTHS {
		goalPlan, err := goalYearPlan.GetMonth(month)
		if err != nil {
			continue
		}

		for i := range goalPlan {
			instance.plan.Append(month, goalPlan[i])
		}
	}
}

func (instance *YearGoals) removeGoalFromPlan(id string) {
	for _, _month := range MONTHS {
		monthGoals, err := instance.plan.GetMonth(_month)
		if err != nil {
			continue
		}

		var goalI int = slices.IndexFunc(monthGoals, func(gPlan GoalPlan) bool {
			return gPlan.Goal.GetId() == id
		})
		if goalI == -1 {
			break
		}

		instance.plan.SetMonth(_month, slices.Concat(monthGoals[:goalI], monthGoals[goalI+1:]))
	}
}

func (instance *YearGoals) AddGoal(newGoal *Goal) bool {
	if len(instance.goals) == int(MAX_GOALS) {
		return false
	}

	var goalI int = slices.IndexFunc(instance.goals, func(goal Goal) bool {
		return goal.GetId() == newGoal.GetId()
	})
	if goalI != -1 {
		return false
	}

	instance.goals = append(instance.goals, *newGoal)
	instance.appendGoalToPlan(newGoal)

	return true
}

func (instance *YearGoals) RemoveGoal(id string) bool {
	var goalI int = slices.IndexFunc(instance.goals, func(goal Goal) bool {
		return goal.GetId() == id
	})
	if goalI == -1 {
		return false
	}

	instance.goals = slices.Concat(instance.goals[:goalI], instance.goals[goalI+1:])
	instance.removeGoalFromPlan(id)

	return true
}

func (instance *YearGoals) SavePlan(
	path string,
	goalToRow func(goal Goal, amount uint, index uint) string,
	monthTitle func(month string) string,
) error {
	file, err := os.Create(path)
	if err != nil {
		return err
	}

	for _, month := range MONTHS {
		monthGoals, err := instance.plan.GetMonth(month)
		if err != nil {
			continue
		}

		var rows []string = []string{monthTitle(month)}
		for i, goalMonth := range monthGoals {
			rows = append(rows, goalToRow(goalMonth.Goal, goalMonth.Amount, uint(i)))
		}

		file.WriteString(strings.Join(rows, "\n") + "\n")
	}

	err = file.Close()
	if err != nil {
		return err
	}

	return nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var yearGoals *YearGoals = NewYearGoals()

	fmt.Println(
		"> Available operations:\n\n",
		" 1 - Add goal.\n",
		" 2 - Remove goal.\n",
		" 3 - Show goals.\n",
		" 4 - Show plan.\n",
		" 5 - Save plan.\n",
		" 0 - Exit.",
	)

	var input uint
	fmt.Printf("\n> Select an operation: ")
	fmt.Scanf("%d\n", &input)

	var reader *bufio.Reader = bufio.NewReader(os.Stdin)

	for input != 0 {
		switch input {
		case 1:
			fmt.Println("\n> Complete the following goal data...")

			fmt.Printf("\n> Units: ")
			units, err := reader.ReadString('\n')
			if err != nil {
				panic(err)
			}

			units = strings.TrimSpace(units)

			var amount uint
			fmt.Printf("\n> Amount (as a number): ")
			fmt.Scanf("%d\n", &amount)

			fmt.Printf("\n> Description: ")
			description, err := reader.ReadString('\n')
			if err != nil {
				panic(err)
			}

			description = strings.TrimSpace(description)

			var monthsLimit uint8
			fmt.Printf("\n> Months limit (as a number): ")
			fmt.Scanf("%d\n", &monthsLimit)

			for monthsLimit < 1 || monthsLimit > MAX_MONTHS_LIMIT {
				fmt.Println("\n> Error! Months limit must be between 1 and 12 (both included). Try again...")
				fmt.Printf("\n> Months limit (as a number): ")
				fmt.Scanf("%d\n", &monthsLimit)
			}

			goal, err := NewGoal(amount, description, monthsLimit, units)
			if err != nil {
				fmt.Println(err.Error())
			}

			if yearGoals.AddGoal(goal) {
				fmt.Println("\n> Goal added!")
			} else {
				fmt.Println("\n> An error occurred! The goal was not added.")
			}

		case 2:
			fmt.Printf("\n> Goal id to remove: ")

			goalId, err := reader.ReadString('\n')
			if err != nil {
				panic(err)
			}

			goalId = strings.TrimSpace(goalId)

			if yearGoals.RemoveGoal(goalId) {
				fmt.Printf("\n> Goal \"%s\" removed!\n", goalId)
			} else {
				fmt.Println("\n> An error occurred! The goal was not removed.")
			}

		case 3:
			var goals []Goal = yearGoals.GetGoals()

			var goalsRows []string
			for _, goal := range goals {
				goalsRows = append(goalsRows, fmt.Sprintf("\n• Goal \"%s\"...\n", goal.GetId()),
					fmt.Sprintf(" - ID: \"%s\".", goal.GetId()),
					fmt.Sprintf(" - Description: \"%s\".", goal.GetDescription()),
					fmt.Sprintf(" - Months limit: %d.", goal.GetMonthsLimit()),
					fmt.Sprintf(" - Amount: %d.", goal.GetAmount()),
					fmt.Sprintf(" - Units: \"%s\".", goal.GetUnits()))

			}

			if len(goalsRows) > 0 {
				fmt.Println(strings.Join(goalsRows, "\n"))
			}

		case 4:
			var plan YearPlan = yearGoals.GetPlan()

			var planRows []string
			for _, month := range MONTHS {
				monthGoals, err := plan.GetMonth(month)
				if err != nil {
					continue
				}

				var planRow string = fmt.Sprintf("\n%s%s:", strings.ToUpper(month[:1]), month[1:])
				for i, monthGoal := range monthGoals {
					var goal Goal = monthGoal.Goal
					var desc string = goal.GetDescription()
					var units string = goal.GetUnits()
					var totalAmount uint = goal.GetAmount()
					planRow += fmt.Sprintf("\n[ ] %d. %s (%d %s/mes). Total: %d.", i+1, desc, monthGoal.Amount, units, totalAmount)
				}

				planRows = append(planRows, planRow)
			}

			if len(planRows) > 0 {
				fmt.Println(strings.Join(planRows, "\n"))
			}

		case 5:
			var currentDate time.Time = time.Now()

			if wd, err := os.Getwd(); err == nil {
				var savePlanPath string = fmt.Sprintf("%s\\plan-%d.txt", wd, currentDate.Year())

				yearGoals.SavePlan(
					savePlanPath,
					func(goal Goal, amount, index uint) string {
						var desc string = goal.GetDescription()
						var units string = goal.GetUnits()
						var totalAmount uint = goal.GetAmount()
						return fmt.Sprintf("[ ] %d. %s (%d %s/mes). Total: %d.", index+1, desc, amount, units, totalAmount)
					},
					func(month string) string { return fmt.Sprintf("\n%s%s:", strings.ToUpper(month[:1]), month[1:]) },
				)

				fmt.Printf("\n> Plan saved in \"%s\" path.\n", savePlanPath)
			} else {
				fmt.Println("\n> Error! An error occurred on get working directory path")
			}

		default:
			fmt.Println("\n> Invalid operation! Try again...")
		}

		fmt.Println(
			"\n> Available operations:\n\n",
			" 1 - Add goal.\n",
			" 2 - Remove goal.\n",
			" 3 - Show goals.\n",
			" 4 - Show plan.\n",
			" 5 - Save plan.\n",
			" 0 - Exit.",
		)

		fmt.Printf("\n> Select an operation: ")
		fmt.Scanf("%d\n", &input)
	}
}
