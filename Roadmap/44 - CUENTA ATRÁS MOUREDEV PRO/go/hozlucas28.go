package main

import (
	"fmt"
	"os"
	"os/exec"
	"sync"
	"time"
)

/* -------------------------------------------------------------------------- */
/*                                   STRUCTS                                  */
/* -------------------------------------------------------------------------- */

type ITimer interface {
	GetEndDate() *time.Time
	TimerEnded() bool
	UpdateTimer(from time.Time, to time.Time)
	ToString() string
}

type timer struct {
	Days    int64
	Hours   int64
	Minutes int64
	Seconds int64

	endDate time.Time
	_       struct{}
}

func NewTimer(from time.Time, to time.Time) ITimer {
	var timer timer = timer{endDate: to}

	var unixStartDate int64 = from.Unix()
	var unixEndDate int64 = to.Unix()

	var remainingTime int64 = unixEndDate - unixStartDate
	if remainingTime <= 0 {
		return &timer
	}

	timer.Days = remainingTime / 86400
	remainingTime -= timer.Days * 86400

	timer.Hours = remainingTime / 3600
	remainingTime -= timer.Hours * 3600

	timer.Minutes = remainingTime / 60
	remainingTime -= timer.Minutes * 60

	timer.Seconds = remainingTime

	return &timer
}

func (timer *timer) GetEndDate() *time.Time {
	return &timer.endDate
}

func (timer *timer) TimerEnded() bool {
	return timer.Days == 0 && timer.Hours == 0 && timer.Minutes == 0 && timer.Seconds == 0
}

func (timer *timer) UpdateTimer(from time.Time, to time.Time) {
	timer.endDate = to

	var unixStartDate int64 = from.Unix()
	var unixEndDate int64 = to.Unix()

	var remainingTime int64 = unixEndDate - unixStartDate
	if remainingTime <= 0 {
		timer.Days = 0
		timer.Hours = 0
		timer.Minutes = 0
		timer.Seconds = 0
		return
	}

	timer.Days = remainingTime / 86400
	remainingTime -= timer.Days * 86400

	timer.Hours = remainingTime / 3600
	remainingTime -= timer.Hours * 3600

	timer.Minutes = remainingTime / 60
	remainingTime -= timer.Minutes * 60

	timer.Seconds = remainingTime
}

func (timer *timer) ToString() string {
	return fmt.Sprintf(
		"[ %06d days | %02d hours | %02d minutes | %02d seconds ]",
		timer.Days,
		timer.Hours,
		timer.Minutes,
		timer.Seconds,
	)
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var wg sync.WaitGroup

	wg.Add(1)

	go func() {
		var startDate time.Time = time.Now()
		var endDate time.Time = time.Date(2024, time.December, 25, 0, 0, 0, 0, time.Local)
		var timer ITimer = NewTimer(startDate, endDate)

		var command = exec.Command("clear")
		command.Stdout = os.Stdout
		command.Run()

		fmt.Printf(
			"> Time remaining for %s: %s.\n", endDate, timer.ToString(),
		)

		for !timer.TimerEnded() {
			time.Sleep(time.Second)

			startDate = time.Now()
			timer.UpdateTimer(startDate, *timer.GetEndDate())

			command = exec.Command("clear")
			command.Stdout = os.Stdout
			command.Run()

			fmt.Printf(
				"> Time remaining for %s: %s.\n", endDate.Local().UTC(), timer.ToString(),
			)
		}

		fmt.Println("\n> The day has come!")
		wg.Done()
	}()

	wg.Wait()
}
