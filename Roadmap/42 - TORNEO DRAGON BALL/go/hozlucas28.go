package main

import (
	"errors"
	"fmt"
	"math"
	"math/rand/v2"
	"slices"
)

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* --------------------------------- Fighter -------------------------------- */

type IFighter interface {
	GetAttack() float64
	GetDefense() float64
	GetLife() float64
	GetName() string
	GetSpeed() float64
	SetLife(newLife float64) IFighter
	Clone() IFighter
}

type fighter struct {
	attack  float64
	defense float64
	life    float64
	name    string
	speed   float64
	_       struct{}
}

func NewFighter(attack float64, defense float64, life float64, name string, speed float64) IFighter {
	var fighter fighter = fighter{
		attack:  attack,
		defense: defense,
		life:    100,
		name:    name,
		speed:   speed,
	}

	return &fighter
}

func (fgt *fighter) GetAttack() float64 {
	return fgt.attack
}

func (fighter *fighter) GetDefense() float64 {
	return fighter.defense
}

func (fighter *fighter) GetLife() float64 {
	return fighter.life
}

func (fighter *fighter) GetName() string {
	return fighter.name
}

func (fighter *fighter) GetSpeed() float64 {
	return fighter.speed
}

func (fighter *fighter) SetLife(newLife float64) IFighter {
	if newLife > 0 {
		fighter.life = newLife
	} else {
		fighter.life = 0
	}

	return fighter
}

func (fgt *fighter) Clone() IFighter {
	var fighter IFighter = NewFighter(
		fgt.attack,
		fgt.defense,
		fgt.life,
		fgt.name,
		fgt.speed,
	)

	return fighter
}

/* ------------------------------- Tournament ------------------------------- */

type ShiftInformation struct {
	AttackDamage float64
	Attacker     IFighter
	Shift        int
	Victim       IFighter
	_            struct{}
}

type Round struct {
	InfoPerShift []ShiftInformation
	Looser       IFighter
	Shifts       int
	Winner       IFighter
	_            struct{}
}

type ITournament interface {
	GetPhase() int
	GetTeamA() []IFighter
	GetTeamB() []IFighter
	GetWinner() (IFighter, error)
	HasWinner() bool
	ExecuteNextRound() (Round, error)
}

type tournament struct {
	pairOfFighters []IFighter
	phase          int
	round          int
	teamA          []IFighter
	teamB          []IFighter
	winner         IFighter
	hasWinner      bool
}

func NewTournament(teamA []IFighter, teamB []IFighter) (ITournament, error) {
	if len(teamA) != len(teamB) {
		return nil, errors.New("The number of fighters in both teams must be equal")
	}

	if (len(teamA)%2 != 0) || (len(teamB)%2 != 0) {
		return nil, errors.New("The number of fighters in both teams must be even")
	}

	var tournament tournament = tournament{
		teamA: teamA,
		teamB: teamB,
	}

	tournament.setRndPairOfFighters()

	return &tournament, nil
}

func (tournament *tournament) GetPhase() int {
	return tournament.phase
}

func (tournament *tournament) GetTeamA() []IFighter {
	return tournament.teamA
}

func (tournament *tournament) GetTeamB() []IFighter {
	return tournament.teamB
}

func (tournament *tournament) GetWinner() (IFighter, error) {
	if !tournament.hasWinner {
		return tournament.winner, errors.New("The tournament has no winner")
	}

	return tournament.winner, nil
}

func (tournament *tournament) HasWinner() bool {
	return tournament.hasWinner
}

func (tournament *tournament) setRndPairOfFighters() {
	var indexesToIgnoreA []int
	var indexesToIgnoreB []int

	var rndIndex int
	var rndFighter IFighter

	for range tournament.teamA {
		rndIndex = rand.IntN(len(tournament.teamA))
		for slices.Contains(indexesToIgnoreA, rndIndex) {
			rndIndex = rand.IntN(len(tournament.teamA))
		}

		rndFighter = tournament.teamA[rndIndex]

		tournament.pairOfFighters = append(tournament.pairOfFighters, rndFighter)
		indexesToIgnoreA = append(indexesToIgnoreA, rndIndex)

		rndIndex = rand.IntN(len(tournament.teamB))
		for slices.Contains(indexesToIgnoreB, rndIndex) {
			rndIndex = rand.IntN(len(tournament.teamB))
		}

		rndFighter = tournament.teamB[rndIndex]

		tournament.pairOfFighters = append(tournament.pairOfFighters, rndFighter)
		indexesToIgnoreB = append(indexesToIgnoreB, rndIndex)
	}
}

func (tournament *tournament) ExecuteNextRound() (Round, error) {
	var round Round

	if tournament.hasWinner {
		return round, errors.New("The tournament already has a winner")
	}

	if len(tournament.pairOfFighters) < 2 {
		return round, errors.New("Not enough fighters to execute the next round")
	}

	tournament.round += 1
	var offset int = tournament.round - 1

	var fighter01 IFighter = tournament.pairOfFighters[offset]
	var fighter02 IFighter = tournament.pairOfFighters[offset+1]
	var fighterAux IFighter

	if fighter01.GetSpeed() < fighter02.GetSpeed() {
		fighterAux = fighter01
		fighter01 = fighter02
		fighter02 = fighterAux
	}

	var shifts int = 0
	var infoPerShift []ShiftInformation

	for fighter01.GetLife() > 0 && fighter02.GetLife() > 0 {
		var attackDamage float64 = 0

		if rand.Float32() > 0.2 {
			var attack float64 = fighter01.GetAttack()
			var defense float64 = fighter02.GetDefense()

			attackDamage = math.Abs(attack - defense)
			if defense > attack {
				attackDamage = attackDamage * 0.1
			}

			fighter02.SetLife(fighter02.GetLife() - attackDamage)
		}

		shifts++

		infoPerShift = append(infoPerShift, ShiftInformation{
			AttackDamage: attackDamage,
			Attacker:     fighter01.Clone(),
			Victim:       fighter02.Clone(),
			Shift:        shifts,
		})

		fighterAux = fighter01
		fighter01 = fighter02
		fighter02 = fighterAux
	}

	fighter01 = tournament.pairOfFighters[offset]
	fighter02 = tournament.pairOfFighters[offset+1]

	var looserIndex int

	if fighter01.GetLife() > 0 {
		looserIndex = offset + 1
	} else {
		looserIndex = offset
	}

	tournament.pairOfFighters = slices.Delete(tournament.pairOfFighters, looserIndex, looserIndex+1)

	if len(tournament.pairOfFighters) < 2 {
		tournament.winner = tournament.pairOfFighters[0]
		tournament.hasWinner = true
	}

	if tournament.round == len(tournament.pairOfFighters) {
		tournament.round = 0
		tournament.phase += 1
	}

	if fighter01.GetLife() > 0 {
		round.Winner = fighter01.Clone()
		round.Looser = fighter02.Clone()
	} else {
		round.Winner = fighter02.Clone()
		round.Looser = fighter01.Clone()
	}

	round.Shifts = shifts
	round.InfoPerShift = infoPerShift

	return round, nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var teamA []IFighter = []IFighter{
		NewFighter(90, 80, 100, "Goku", 95),
		NewFighter(85, 75, 100, "Vegeta", 90),
		NewFighter(70, 65, 100, "Piccolo", 80),
		NewFighter(60, 55, 100, "Krillin", 70),
	}

	var teamB []IFighter = []IFighter{
		NewFighter(88, 78, 100, "Frieza", 92),
		NewFighter(82, 72, 100, "Cell", 88),
		NewFighter(75, 65, 100, "Majin Buu", 85),
		NewFighter(65, 60, 100, "Broly", 75),
	}

	tournament, err := NewTournament(teamA, teamB)
	if err != nil {
		panic(err)
	}

	var rounds int = 0

	for !tournament.HasWinner() {
		round, err := tournament.ExecuteNextRound()
		if err != nil {
			panic(err)
		}

		rounds++

		fmt.Printf("> Round %d (%s vs %s)...\n\n", rounds, round.Winner.GetName(), round.Looser.GetName())

		for _, shift := range round.InfoPerShift {
			if shift.AttackDamage > 0 {
				fmt.Printf(
					"> Shift %d: %s attacks %s with an attack damage of %.2f.\n",
					shift.Shift,
					shift.Attacker.GetName(),
					shift.Victim.GetName(),
					shift.AttackDamage,
				)
			} else {
				fmt.Printf(
					"> Shift %d: %s attacks %s, but %s evades the attack.\n",
					shift.Shift,
					shift.Attacker.GetName(),
					shift.Victim.GetName(),
					shift.Victim.GetName(),
				)
			}
		}

		fmt.Printf(
			"\n> %s wins the fight against %s in %d shifts!\n\n",
			round.Winner.GetName(),
			round.Looser.GetName(),
			round.Shifts,
		)
	}

	winner, err := tournament.GetWinner()
	fmt.Printf("> The winner of the tournament is %s!", winner.GetName())
}
