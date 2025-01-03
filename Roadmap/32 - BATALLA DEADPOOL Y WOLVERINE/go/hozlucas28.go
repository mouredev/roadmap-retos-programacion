package main

import (
	"errors"
	"fmt"
	"math/rand/v2"
	"time"
)

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

type Turn struct {
	Attacker ISuperhero
	Number   int
	Victim   ISuperhero
	_        struct{}
}

type ExecutedTurn struct {
	Turn
	DamageProducedByAttacker int
	DamageReceivedByVictim   int
	VictimAvoidAttack        bool
	_                        struct{}
}

/* -------------------------------------------------------------------------- */
/*                                   ERRORS                                   */
/* -------------------------------------------------------------------------- */

/* ----------------------- SuperheroRegeneratingError ----------------------- */

type SuperheroRegeneratingError struct {
	Superhero ISuperhero
	_         struct{}
}

func (err *SuperheroRegeneratingError) Error() string {
	return fmt.Sprintf("%s is regenerating", err.Superhero.GetName())
}

/* -------------------------- ThereIsNoWinnerError -------------------------- */

type ThereIsNoWinnerError struct{}

func (err *ThereIsNoWinnerError) Error() string {
	return "There is no winner"
}

/* --------------------------- ThereIsAWinnerError -------------------------- */

type ThereIsAWinnerError struct{}

func (err *ThereIsAWinnerError) Error() string {
	return "There is a winner"
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* -------------------------------- Superhero ------------------------------- */

type ISuperhero interface {
	GetAttackDamage() [2]int
	GetLifePoints() int
	GetName() string
	IsRegenerating() bool
	SetRegenerating(regenerating bool) ISuperhero
	EvadeAttack() bool
	ProduceDamage() (int, error)
	ReceiveDamage(damage int) ISuperhero
}

type superhero struct {
	attackDamage    [2]int
	evadePercentage float32
	lifePoints      int
	name            string
	regenerating    bool
	_               struct{}
}

func NewSuperhero(
	attackDamage [2]int,
	evadePercentage float32,
	lifePoints int,
	name string,
) ISuperhero {
	var superhero superhero = superhero{
		lifePoints:      lifePoints,
		regenerating:    false,
		attackDamage:    attackDamage,
		evadePercentage: evadePercentage,
		name:            name,
	}

	return &superhero
}

func (superhero *superhero) GetAttackDamage() [2]int {
	return superhero.attackDamage
}

func (superhero *superhero) GetLifePoints() int {
	return superhero.lifePoints
}

func (superhero *superhero) GetName() string {
	return superhero.name
}

func (superhero *superhero) IsRegenerating() bool {
	return superhero.regenerating
}

func (superhero *superhero) SetRegenerating(regenerating bool) ISuperhero {
	superhero.regenerating = regenerating
	return superhero
}

func (superhero *superhero) EvadeAttack() bool {
	var rndNumber float32 = rand.Float32()
	return rndNumber <= superhero.evadePercentage
}

func (superhero *superhero) ProduceDamage() (int, error) {
	if superhero.IsRegenerating() {
		return 0, &SuperheroRegeneratingError{
			Superhero: superhero,
		}
	}

	minAttackDamage, maxAttackDamage := superhero.attackDamage[0], superhero.attackDamage[1]
	var rndDamage int = rand.N(maxAttackDamage-minAttackDamage+1) + minAttackDamage

	return rndDamage, nil
}

func (superhero *superhero) ReceiveDamage(damage int) ISuperhero {
	superhero.lifePoints -= damage
	return superhero
}

/* ---------------------------- SuperheroesFight ---------------------------- */

type ISuperheroesFight interface {
	GetTurn() Turn
	GetWinner() (ISuperhero, error)
	ExecuteTurn() (ExecutedTurn, error)
}

type superheroesFight struct {
	Turn   Turn
	Winner ISuperhero
	_      struct{}
}

func NewSuperheroesFight(superheroOne ISuperhero, superheroTwo ISuperhero) ISuperheroesFight {
	var superheroesFight superheroesFight = superheroesFight{
		Turn: Turn{
			Attacker: superheroOne,
			Number:   1,
			Victim:   superheroTwo,
		},
	}

	return &superheroesFight
}

func (fight *superheroesFight) GetTurn() Turn {
	return fight.Turn
}

func (fight *superheroesFight) GetWinner() (ISuperhero, error) {
	if fight.Winner == nil {
		return nil, &ThereIsNoWinnerError{}
	}

	return fight.Winner, nil
}

func (fight *superheroesFight) ExecuteTurn() (ExecutedTurn, error) {
	if fight.Winner != nil {
		return ExecutedTurn{}, &ThereIsAWinnerError{}
	}

	var attacker ISuperhero = fight.Turn.Attacker
	var number int = fight.Turn.Number
	var victim ISuperhero = fight.Turn.Victim

	victim.SetRegenerating(false)

	fight.Turn = Turn{
		Attacker: victim,
		Number:   number + 1,
		Victim:   attacker,
	}

	damageProducedByAttacker, err := attacker.ProduceDamage()
	if err != nil {
		return ExecutedTurn{}, err
	}

	attackerAttackDamage := attacker.GetAttackDamage()
	var victimAvoidAttack bool = victim.EvadeAttack()

	var damageReceivedByVictim int
	if !victimAvoidAttack {
		damageReceivedByVictim = damageProducedByAttacker
		victim.ReceiveDamage(damageProducedByAttacker)
		victim.SetRegenerating(damageProducedByAttacker == attackerAttackDamage[1])

		if victim.GetLifePoints() <= 0 {
			fight.Winner = attacker
		}
	}

	return ExecutedTurn{
		Turn: Turn{
			Attacker: attacker,
			Victim:   victim,
			Number:   number,
		},

		DamageProducedByAttacker: damageProducedByAttacker,
		DamageReceivedByVictim:   damageReceivedByVictim,
		VictimAvoidAttack:        victimAvoidAttack,
	}, nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var deadpool ISuperhero = NewSuperhero(
		[2]int{10, 100},
		0.25,
		500,
		"Deadpool",
	)

	var wolverine ISuperhero = NewSuperhero(
		[2]int{10, 120},
		0.20,
		500,
		"Wolverine",
	)

	var superheroesFight ISuperheroesFight = NewSuperheroesFight(deadpool, wolverine)

	for _, err := superheroesFight.GetWinner(); err != nil; _, err = superheroesFight.GetWinner() {
		time.Sleep(time.Second)
		var currentTurn Turn = superheroesFight.GetTurn()

		executedTurn, err := superheroesFight.ExecuteTurn()
		if err != nil {
			var regeneratingErr *SuperheroRegeneratingError
			if errors.As(err, &regeneratingErr) {
				fmt.Printf("\n> Turn N°%d: %s\n", currentTurn.Number, err)
				continue
			}
			break
		}

		if executedTurn.VictimAvoidAttack {
			fmt.Printf(
				"\n> Turn N°%d: %s avoided %s attack\n",
				executedTurn.Turn.Number,
				executedTurn.Turn.Victim.GetName(),
				executedTurn.Turn.Attacker.GetName(),
			)
			continue
		}

		fmt.Printf(
			"\n> Turn N°%d: %s attacked %s with %d points of damage",
			executedTurn.Turn.Number,
			executedTurn.Turn.Attacker.GetName(),
			executedTurn.Turn.Victim.GetName(),
			executedTurn.DamageProducedByAttacker,
		)

		fmt.Printf(
			"\n[ Life points of %s: %d ]",
			deadpool.GetName(),
			deadpool.GetLifePoints(),
		)

		fmt.Printf("\n[ Life points of %s: %d ]\n",
			wolverine.GetName(),
			wolverine.GetLifePoints(),
		)
	}

	winner, _ := superheroesFight.GetWinner()
	fmt.Printf("\nThe winner is %s!", winner.GetName())
}
