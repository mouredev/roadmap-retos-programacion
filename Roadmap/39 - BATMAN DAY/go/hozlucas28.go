package main

import (
	"fmt"
	"math"
	"slices"
	"time"
)

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

/* ----------------------------- First Challenge ---------------------------- */

func GetBatmanDayAnniversary(anniversary uint16) *time.Time {
	var anniversaryDate time.Time = time.Date(1939, 9, 16, 0, 0, 0, 0, time.Local)

	if anniversary > 0 {
		anniversaryDate = time.Date(1939+int(anniversary), 9, 1, 0, 0, 0, 0, time.Local)

		var saturdayCounter uint8 = 0
		if anniversaryDate.Weekday() == time.Saturday {
			saturdayCounter = 1
		}

		for saturdayCounter < 3 {
			anniversaryDate = anniversaryDate.AddDate(0, 0, 1)

			if anniversaryDate.Weekday() == time.Saturday {
				saturdayCounter += 1
			}
		}
	}

	return &anniversaryDate
}

/* ---------------------------- Second Challenge ---------------------------- */

type ThreatLevel struct {
	X           uint
	Y           uint
	Level uint
	_           struct{}
}

type Sensors struct {
	Array2D [][]uint
	_       struct{}
}

func (sensors *Sensors) GetThreatLevels() []*ThreatLevel {
	var threatLevels []*ThreatLevel = make([]*ThreatLevel, 0, (len(sensors.Array2D)-2)*(len(sensors.Array2D[0])-2))

	var rows uint = uint(len(sensors.Array2D))
	var cols uint = uint(len(sensors.Array2D[0]))

	for i := uint(1); i < rows-1; i++ {
		for j := uint(1); j < cols-1; j++ {
			var threatLevel uint = 0

			threatLevel += sensors.Array2D[i-1][j-1]
			threatLevel += sensors.Array2D[i-1][j]
			threatLevel += sensors.Array2D[i-1][j+1]

			threatLevel += sensors.Array2D[i][j-1]
			threatLevel += sensors.Array2D[i][j]
			threatLevel += sensors.Array2D[i][j+1]

			threatLevel += sensors.Array2D[i+1][j-1]
			threatLevel += sensors.Array2D[i+1][j]
			threatLevel += sensors.Array2D[i+1][j+1]

			threatLevels = append(threatLevels, &ThreatLevel{X: j, Y: i, Level: threatLevel})
		}
	}

	return threatLevels
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	fmt.Println("> First challenge...")

	var batmanDay85thAnniversary *time.Time = GetBatmanDayAnniversary(85)
	var batmanDay100thAnniversary *time.Time = GetBatmanDayAnniversary(100)

	fmt.Printf(
		"\n> The 85th anniversary of Batman day is on %d/%d/%d.\n",
		batmanDay85thAnniversary.Month(),
		batmanDay85thAnniversary.Day(),
		batmanDay85thAnniversary.Year(),
	)

	fmt.Printf(
		"> The 100th anniversary of Batman day is on %d/%d/%d.\n",
		batmanDay100thAnniversary.Month(),
		batmanDay100thAnniversary.Day(),
		batmanDay100thAnniversary.Year(),
	)

	fmt.Println("\n> Second challenge...")

	var batmanCavePos [2]uint = [2]uint{0, 0}

	var sensors Sensors = Sensors{
		Array2D: [][]uint{
			{1, 0, 1, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1},
			{2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0},
			{1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1},
			{0, 9, 8, 0, 2, 0, 9, 2, 8, 1, 0, 1, 3, 7, 8, 1, 0, 2, 7, 6},
			{1, 0, 1, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1},
			{3, 1, 8, 7, 9, 6, 1, 7, 9, 0, 1, 0, 1, 9, 2, 1, 3, 0, 8, 0},
			{1, 6, 9, 1, 2, 8, 0, 2, 1, 3, 2, 8, 7, 2, 8, 0, 1, 7, 9, 0},
			{1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 1, 0},
			{0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0},
			{2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2},
			{7, 8, 6, 1, 0, 9, 2, 8, 1, 3, 7, 1, 0, 2, 0, 9, 1, 6, 7, 8},
			{0, 1, 7, 9, 2, 8, 1, 6, 7, 8, 1, 2, 0, 3, 1, 8, 2, 7, 0, 1},
			{3, 0, 9, 1, 8, 6, 1, 0, 7, 9, 2, 0, 1, 2, 8, 0, 1, 9, 6, 1},
			{1, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0},
			{0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0},
			{2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2},
			{9, 6, 1, 0, 9, 8, 7, 2, 8, 0, 1, 0, 3, 6, 2, 7, 9, 2, 8, 1},
			{0, 7, 8, 9, 6, 2, 1, 9, 6, 7, 8, 0, 9, 7, 6, 8, 1, 0, 2, 8},
			{2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2},
			{3, 2, 1, 9, 6, 7, 0, 3, 1, 8, 2, 7, 9, 2, 0, 9, 7, 6, 8, 0},
		},
	}

	var threatLevels []*ThreatLevel = sensors.GetThreatLevels()

	var threatLevelsGreaterThanTwenty []*ThreatLevel = slices.DeleteFunc(threatLevels, func(threatLevel *ThreatLevel) bool {
		return threatLevel.Level < 20
	})

	fmt.Println("\n> Threat levels greater than 20 (security protocol activated)...")

	for _, threatLevel := range threatLevelsGreaterThanTwenty {
		fmt.Printf("\n> Coordinates (x, y): (%d, %d).\n", threatLevel.X, threatLevel.Y)
		fmt.Printf("> Threat level: %d.\n", threatLevel.Level)
	}

	fmt.Println("\n> Position with the maximum threat level...")

	var maxThreatLevel *ThreatLevel = slices.MaxFunc(threatLevelsGreaterThanTwenty, func(a *ThreatLevel, b *ThreatLevel) int {
		return int(a.Level - b.Level)
	})

	var distanceToBatmanCave uint = uint(math.Abs(float64(maxThreatLevel.X-batmanCavePos[0])) +
		math.Abs(float64(maxThreatLevel.Y-batmanCavePos[1])))

	fmt.Printf("\n> Coordinates (x, y): (%d, %d).\n", maxThreatLevel.X, maxThreatLevel.Y)
	fmt.Printf("> Threat level: %d.\n", maxThreatLevel.Level)
	fmt.Printf("> Distance to batman cave: %d cells.\n", distanceToBatmanCave)
}
