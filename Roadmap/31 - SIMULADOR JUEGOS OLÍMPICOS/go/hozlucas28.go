package main

import (
	"fmt"
	"math/rand"
	"slices"
	"sort"
	"strings"
	"time"
)

/* -------------------------------------------------------------------------- */
/*                                  UTILS.GO                                  */
/* -------------------------------------------------------------------------- */

type CountryStats struct {
	Name           CountryName
	NumberOfMedals int
}

func CountriesRankingByNumberOfMedals(sportEvents ...*SportEvent) []CountryStats {
	var countriesStats []CountryStats

	var winners []*Competitor
	for _, sportEvent := range sportEvents {
		for _, winner := range (*sportEvent).GetWinners() {
			winners = append(winners, winner)
		}
	}

	var indexesToIgnore []int

	for i, winner := range winners {
		if slices.Contains(indexesToIgnore, i) {
			continue
		}

		var winnerCountry CountryName = (*winner).GetCountry()
		var winnerNumberOfMedals int = len((*winner).GetMedals())

		var countryStats CountryStats = CountryStats{
			Name:           winnerCountry,
			NumberOfMedals: winnerNumberOfMedals,
		}

		for j := i + 1; j < len(winners); j++ {
			if slices.Contains(indexesToIgnore, j) {
				continue
			}

			var nextWinner *Competitor = winners[j]
			var nextWinnerCountry CountryName = (*nextWinner).GetCountry()
			var nextWinnerNumberOfMedals int = len((*nextWinner).GetMedals())

			var areSameCountry bool = strings.ToUpper(string(winnerCountry)) == strings.ToUpper(string(nextWinnerCountry))

			if areSameCountry {
				countryStats.NumberOfMedals += nextWinnerNumberOfMedals
				indexesToIgnore = append(indexesToIgnore, j)
			}
		}

		countriesStats = append(countriesStats, countryStats)
	}

	sort.Slice(countriesStats, func(i, j int) bool {
		return countriesStats[i].Name < countriesStats[j].Name
	})

	sort.Slice(countriesStats, func(i, j int) bool {
		return countriesStats[i].NumberOfMedals > countriesStats[j].NumberOfMedals
	})

	return countriesStats

}

/* -------------------------------------------------------------------------- */
/*                                  MEDAL.GO                                  */
/* -------------------------------------------------------------------------- */

type MedalCategory string

var (
	Bronze MedalCategory = "bronze"
	Gold   MedalCategory = "gold"
	Silver MedalCategory = "silver"
)

type Medal interface {
	GetCategory() MedalCategory
	GetDate() time.Time
	GetSportEvent() SportEvent
}

type medal struct {
	date       time.Time
	sportEvent SportEvent
	category   MedalCategory
	_          struct{}
}

func NewMedal(date time.Time, sportEvent SportEvent, medalCategory MedalCategory) Medal {
	var medal medal = medal{date: date, sportEvent: sportEvent, category: medalCategory}
	return &medal
}

func (medal *medal) GetCategory() MedalCategory {
	return medal.category
}

func (medal *medal) GetDate() time.Time {
	return medal.date
}

func (medal *medal) GetSportEvent() SportEvent {
	return medal.sportEvent

}

/* -------------------------------------------------------------------------- */
/*                             COMPETITOR/UTILS.GO                            */
/* -------------------------------------------------------------------------- */

func GetUniqueRandomsCompetitors(competitors []*Competitor, numberOfChoices int) ([]int, []*Competitor) {
	var rtnI []int
	var rtn []*Competitor

	var sliceLength int = len(competitors)
	var indexesToIgnore []int

	for i := 0; i < numberOfChoices; i++ {
		var randomChoiceI int = rand.Intn(sliceLength)
		if slices.Contains(indexesToIgnore, randomChoiceI) {
			i--
			continue
		}

		rtnI = append(rtnI, randomChoiceI)
		rtn = append(rtn, competitors[randomChoiceI])
		indexesToIgnore = append(indexesToIgnore, randomChoiceI)
	}

	return rtnI, rtn
}

/* -------------------------------------------------------------------------- */
/*                             COMPETITOR/MAIN.GO                             */
/* -------------------------------------------------------------------------- */

type CountryName string

var (
	Argentina    CountryName = "argentina"
	Spain        CountryName = "spain"
	UnitedStates CountryName = "united states"
	Mexico       CountryName = "mexico"
	Canada       CountryName = "canada"
	Chile        CountryName = "chile"
	Brazil       CountryName = "brazil"
	Germany      CountryName = "germany"
	France       CountryName = "france"
	Italy        CountryName = "italy"
	Australia    CountryName = "australia"
	Japan        CountryName = "japan"
)

type Competitor interface {
	GetCountry() CountryName
	GetMedals() []Medal
	GetName() string
	AddMedals(newMedals ...Medal)
}

type competitor struct {
	country CountryName
	medals  []Medal
	name    string
	_       struct{}
}

func NewCompetitor(country CountryName, name string) Competitor {
	var competitor competitor = competitor{country: country, name: name}
	return &competitor
}

func (competitor *competitor) GetCountry() CountryName {
	return competitor.country
}

func (competitor *competitor) GetMedals() []Medal {
	return competitor.medals
}

func (competitor *competitor) GetName() string {
	return competitor.name
}

func (competitor *competitor) AddMedals(newMedals ...Medal) {
	var actualMedals []Medal = competitor.medals
	var joinedMedals []Medal = slices.Concat(actualMedals, newMedals)
	competitor.medals = joinedMedals
}

/* -------------------------------------------------------------------------- */
/*                                SPORTEVENT.GO                               */
/* -------------------------------------------------------------------------- */

var (
	MinimumNumberOfCompetitors int = 3
)

type SportEvent interface {
	GetCompetitors() []*Competitor
	GetName() string
	GetWinners() [3]*Competitor
	AddCompetitors(newCompetitors ...*Competitor) error
	Start() error
}

type sportEvent struct {
	competitors []*Competitor
	name        string
	winners     [3]*Competitor

	_ struct{}
}

func NewSportEvent(name string) SportEvent {
	var sportEvent sportEvent = sportEvent{name: name}
	return &sportEvent
}

func (sportEvent *sportEvent) GetCompetitors() []*Competitor {
	return sportEvent.competitors
}

func (sportEvent *sportEvent) GetName() string {
	return sportEvent.name
}

func (sportEvent *sportEvent) GetWinners() [3]*Competitor {
	return sportEvent.winners
}

func (sportEvent *sportEvent) AddCompetitors(newCompetitors ...*Competitor) error {
	var actualCompetitors []*Competitor = sportEvent.competitors
	var joinedCompetitors []*Competitor = slices.Concat(actualCompetitors, newCompetitors)
	sportEvent.competitors = joinedCompetitors
	return nil
}

func (sportEvent *sportEvent) Start() error {
	var numberOfCompetitors int = len(sportEvent.competitors)

	if numberOfCompetitors < MinimumNumberOfCompetitors {
		return fmt.Errorf("Sport event %s needs more competitors. It currently has %d competitor(s), but requires a minimum of %d.", sportEvent.name, len(sportEvent.competitors), MinimumNumberOfCompetitors)
	}

	_, winners := GetUniqueRandomsCompetitors(sportEvent.competitors, 3)

	var goldMedal Medal = NewMedal(time.Now(), sportEvent, Gold)
	var silverMedal Medal = NewMedal(time.Now(), sportEvent, Silver)
	var bronzeMedal Medal = NewMedal(time.Now(), sportEvent, Bronze)

	(*winners[0]).AddMedals(goldMedal)
	(*winners[1]).AddMedals(silverMedal)
	(*winners[2]).AddMedals(bronzeMedal)

	sportEvent.winners = [3]*Competitor{winners[0], winners[1], winners[2]}

	return nil
}

/* -------------------------------------------------------------------------- */
/*                                   MAIN.GO                                  */
/* -------------------------------------------------------------------------- */

func main() {
	fmt.Println("> Paris 2024 olympic games.")

	var firstSportEvent SportEvent = NewSportEvent("football")
	var secondSportEvent SportEvent = NewSportEvent("handball")
	var thirdSportEvent SportEvent = NewSportEvent("table tennis")
	var fourthSportEvent SportEvent = NewSportEvent("swimming")

	fmt.Println("\n> First sport event...")
	fmt.Printf("\n%+v\n", firstSportEvent)

	fmt.Println("\n> Second sport event...")
	fmt.Printf("\n%+v\n", secondSportEvent)

	fmt.Println("\n> Third sport event...")
	fmt.Printf("\n%+v\n", thirdSportEvent)

	fmt.Println("\n> Fourth sport event...")
	fmt.Printf("\n%+v\n", fourthSportEvent)

	var competitorsOfFirstSportEvent [5]Competitor = [5]Competitor{
		NewCompetitor(Argentina, "lionel messi"),
		NewCompetitor(Spain, "sergio ramos"),
		NewCompetitor(UnitedStates, "megan rapinoe"),
		NewCompetitor(Mexico, "hirving lozano"),
		NewCompetitor(Canada, "christine sinclair"),
	}

	var competitorsOfSecondSportEvent [5]Competitor = [5]Competitor{
		NewCompetitor(Brazil, "neymar"),
		NewCompetitor(Germany, "manuel neuer"),
		NewCompetitor(France, "antoine griezmann"),
		NewCompetitor(Italy, "giorgio chiellini"),
		NewCompetitor(Australia, "sam kerr"),
	}

	var competitorsOfThirdSportEvent [5]Competitor = [5]Competitor{
		NewCompetitor(Japan, "naomi osaka"),
		NewCompetitor(Chile, "liu shiwen"),
		NewCompetitor(Spain, "choi hyojoo"),
		NewCompetitor(Italy, "feng tianwei"),
		NewCompetitor(Germany, "han ying"),
	}

	var competitorsOfFourthSportEvent [5]Competitor = [5]Competitor{
		NewCompetitor(Brazil, "sarah sjöström"),
		NewCompetitor(UnitedStates, "caleb dressel"),
		NewCompetitor(Australia, "emma mckeon"),
		NewCompetitor(Canada, "penny oleksiak"),
		NewCompetitor(Japan, "ranomi kromowidjojo"),
	}

	fmt.Println("\n> Competitors of first sport event...")
	fmt.Println()
	for _, competitor := range competitorsOfFirstSportEvent {
		fmt.Printf("%+v\n", competitor)
	}

	fmt.Println("\n> Competitors of second sport event...")
	fmt.Println()
	for _, competitor := range competitorsOfSecondSportEvent {
		fmt.Printf("%+v\n", competitor)
	}

	fmt.Println("\n> Competitors of third sport event...")
	fmt.Println()
	for _, competitor := range competitorsOfThirdSportEvent {
		fmt.Printf("%+v\n", competitor)
	}

	fmt.Println("\n> Competitors of fourth sport event...")
	fmt.Println()
	for _, competitor := range competitorsOfFourthSportEvent {
		fmt.Printf("%+v\n", competitor)
	}

	firstSportEvent.AddCompetitors(
		&competitorsOfFirstSportEvent[0],
		&competitorsOfFirstSportEvent[1],
		&competitorsOfFirstSportEvent[2],
		&competitorsOfFirstSportEvent[3],
		&competitorsOfFirstSportEvent[4],
	)

	secondSportEvent.AddCompetitors(
		&competitorsOfSecondSportEvent[0],
		&competitorsOfSecondSportEvent[1],
		&competitorsOfSecondSportEvent[2],
		&competitorsOfSecondSportEvent[3],
		&competitorsOfSecondSportEvent[4],
	)

	thirdSportEvent.AddCompetitors(
		&competitorsOfThirdSportEvent[0],
		&competitorsOfThirdSportEvent[1],
		&competitorsOfThirdSportEvent[2],
		&competitorsOfThirdSportEvent[3],
		&competitorsOfThirdSportEvent[4],
	)

	fourthSportEvent.AddCompetitors(
		&competitorsOfFourthSportEvent[0],
		&competitorsOfFourthSportEvent[1],
		&competitorsOfFourthSportEvent[2],
		&competitorsOfFourthSportEvent[3],
		&competitorsOfFourthSportEvent[4],
	)

	firstSportEvent.Start()
	secondSportEvent.Start()
	thirdSportEvent.Start()
	fourthSportEvent.Start()

	var winnersOfFirstSportEvent [3]*Competitor = firstSportEvent.GetWinners()
	var winnersOfSecondSportEvent [3]*Competitor = secondSportEvent.GetWinners()
	var winnersOfThirdSportEvent [3]*Competitor = thirdSportEvent.GetWinners()
	var winnersOfFourthSportEvent [3]*Competitor = fourthSportEvent.GetWinners()

	fmt.Println("\n> Winners of first sport event...")
	fmt.Println()
	for _, winner := range winnersOfFirstSportEvent {
		fmt.Printf("%+v\n", *winner)
	}

	fmt.Println("\n> Winners of second sport event...")
	fmt.Println()
	for _, winner := range winnersOfSecondSportEvent {
		fmt.Printf("%+v\n", *winner)
	}

	fmt.Println("\n> Winners of third sport event...")
	fmt.Println()
	for _, winner := range winnersOfThirdSportEvent {
		fmt.Printf("%+v\n", *winner)
	}

	fmt.Println("\n> Winners of fourth sport event...")
	fmt.Println()
	for _, winner := range winnersOfFourthSportEvent {
		fmt.Printf("%+v\n", *winner)
	}

	var medalRankingPerCountry = CountriesRankingByNumberOfMedals(
		&firstSportEvent,
		&secondSportEvent,
		&thirdSportEvent,
		&fourthSportEvent,
	)

	fmt.Println("\n> Medal ranking per country...")
	for _, countryStats := range medalRankingPerCountry {
		fmt.Printf("\n%+v", countryStats)
	}
}
