package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

/* -------------------------------- Dog Fact -------------------------------- */

type Fact struct {
	Id         string `json:"id"`
	Type       string `json:"type"`
	Attributes struct {
		Body string `json:"body"`
	} `json:"attributes"`
}

type DogFact struct {
	Data []Fact `json:"data"`
}

/* --------------------------------- Pokemon -------------------------------- */

type GameIndex struct {
	GameIndex int `json:"game_index"`
	Version   struct {
		Name string `json:"name"`
	} `json:"version"`
}

type Type struct {
	Slot int `json:"slot"`
	Type struct {
		Name string `json:"name"`
	} `json:"type"`
}

type Pokemon struct {
	GameIndices []GameIndex `json:"game_indices"`
	Height      int         `json:"height"`
	Id          int         `json:"id"`
	Name        string      `json:"name"`
	Types       []Type      `json:"types"`
}

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

func getPokemon[Query int | string](query Query) (Pokemon, error) {
	var pokemon Pokemon

	var endPoint string = fmt.Sprintf("https://pokeapi.co/api/v2/pokemon/%v", query)

	response, err := http.Get(endPoint)
	if err != nil {
		return pokemon, err
	}

	if response.StatusCode == 200 {
		body, err := io.ReadAll(response.Body)
		if err != nil {
			return pokemon, err
		}

		err = json.Unmarshal(body, &pokemon)
		if err != nil {
			return pokemon, err
		}
	} else {
		return pokemon, errors.New(response.Status)
	}

	return pokemon, nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		HTTP request...
	*/

	fmt.Println("HTTP request...")

	response, err := http.Get("https://dogapi.dog/api/v2/facts")
	if err != nil {
		fmt.Printf("\n%s\n", err.Error())
	}

	if response.StatusCode == 200 {
		stringifiedJson, err := io.ReadAll(response.Body)
		if err != nil {
			fmt.Printf("\n%s\n", err.Error())
		}

		var randomDogFact DogFact
		err = json.Unmarshal(stringifiedJson, &randomDogFact)
		if err != nil {
			fmt.Printf("\n%s\n", err.Error())
		}

		fmt.Printf("\nRandom dog fact: %s\n", randomDogFact.Data[0].Attributes.Body)
	} else {
		fmt.Printf("\n%s\n", response.Status)
	}

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
		Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	fmt.Println("\nPokemon with id number five...")

	fourthPokemon, err := getPokemon(4)
	if err != nil {
		fmt.Printf("\n%s\n", err.Error())
	}

	var fourthPokemonTypes string
	for _, t := range fourthPokemon.Types {
		fourthPokemonTypes += ", " + t.Type.Name
	}
	fourthPokemonTypes = strings.TrimLeft(fourthPokemonTypes, ", ")

	var fourthPokemonGames string
	for _, game := range fourthPokemon.GameIndices {
		fourthPokemonGames += ", " + game.Version.Name
	}
	fourthPokemonGames = strings.TrimLeft(fourthPokemonGames, ", ")

	fmt.Printf("\nid: %d", fourthPokemon.Id)
	fmt.Printf("\nname: %s", fourthPokemon.Name)
	fmt.Printf("\nheight: %d", fourthPokemon.Height)
	fmt.Printf("\ntypes: %s", fourthPokemonTypes)
	fmt.Printf("\ngames: %s\n", fourthPokemonGames)

	fmt.Println("\nPokemon with 'Mew' name...")

	mewPokemon, err := getPokemon("mew")
	if err != nil {
		fmt.Printf("\n%s\n", err.Error())
	}

	var mewPokemonTypes string
	for _, t := range mewPokemon.Types {
		mewPokemonTypes += ", " + t.Type.Name
	}
	mewPokemonTypes = strings.TrimLeft(mewPokemonTypes, ", ")

	var mewPokemonGames string
	for _, game := range mewPokemon.GameIndices {
		mewPokemonGames += ", " + game.Version.Name
	}
	mewPokemonGames = strings.TrimLeft(mewPokemonGames, ", ")

	fmt.Printf("\nid: %d", mewPokemon.Id)
	fmt.Printf("\nname: %s", mewPokemon.Name)
	fmt.Printf("\nheight: %d", mewPokemon.Height)
	fmt.Printf("\ntypes: %s", mewPokemonTypes)
	fmt.Printf("\ngames: %s\n", mewPokemonGames)
}
