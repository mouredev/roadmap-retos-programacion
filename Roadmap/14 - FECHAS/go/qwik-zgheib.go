package main

import (
	"fmt"
	"time"
)

type DateOperations interface {
	YearsBetween(date1, date2 time.Time) int
	FormatDate(date time.Time, format string) string
}

type DateService struct{}

func NewDateService() *DateService {
	return &DateService{}
}

func (d *DateService) YearsBetween(date1, date2 time.Time) int {
	years := date2.Year() - date1.Year()
	if date2.YearDay() < date1.YearDay() {
		years--
	}
	return years
}

func (d *DateService) FormatDate(date time.Time, format string) string {
	return date.Format(format)
}

func main() {
	var dateService DateOperations = NewDateService()

	currentDate := time.Now()
	birthDate := time.Date(2002, time.November, 9, 10, 0, 0, 0, time.UTC)

	years := dateService.YearsBetween(birthDate, currentDate)
	fmt.Printf("Years between %v and %v: %d\n", birthDate, currentDate, years)

	// extra challenge
	formats := []string{
		"02-01-2006",
		"15:04:05",
		"02 January 2006",
		"Monday, 02 Jan 2006",
		"2006-01-02 15:04:05",
		"02",
		"01",
		"2006",
		"02-01",
		"01-2006",
	}

	descriptions := []string{
		"Day-Month-Year",
		"Hour:Minute:Second",
		"Day Month Year",
		"Weekday, Day Month Year",
		"ISO format",
		"Day",
		"Month",
		"Year",
		"Day-Month",
		"Month-Year",
	}

	for i, format := range formats {
		formattedDate := dateService.FormatDate(birthDate, format)
		fmt.Printf("%s: %s\n", descriptions[i], formattedDate)
	}
}
