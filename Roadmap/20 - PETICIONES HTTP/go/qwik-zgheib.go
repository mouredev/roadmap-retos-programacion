package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
	"strings"
)

func fetchURL(url string) (string, error) {
	resp, err := http.Get(url)
	if err != nil {
		return "", err
	}
	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {
			fmt.Println("error closing response body:", err)
		}
	}(resp.Body)

	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf("error: status code %d", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	return string(body), nil
}

// -- extra challenge --
type HTTPClient interface {
	Do(req *http.Request) (*http.Response, error)
}

type PokeAPI struct {
	Client  HTTPClient
	BaseURL string
}

type Pokemon struct {
	Name   string `json:"name"`
	ID     int    `json:"id"`
	Height int    `json:"height"`
	Weight int    `json:"weight"`
	Types  []Type `json:"types"`
}

type Type struct {
	Slot int `json:"slot"`
	Type struct {
		Name string `json:"name"`
	} `json:"type"`
}

type EvolutionChain struct {
	Chain Chain `json:"chain"`
}

type Chain struct {
	Species struct {
		Name string `json:"name"`
	} `json:"species"`
	EvolvesTo []Chain `json:"evolves_to"`
}

func (api *PokeAPI) fetchPokemon(nameOrID string) (Pokemon, error) {
	url := fmt.Sprintf("%s/pokemon/%s", api.BaseURL, nameOrID)
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return Pokemon{}, err
	}

	resp, err := api.Client.Do(req)
	if err != nil {
		return Pokemon{}, err
	}
	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {
			fmt.Println("error closing response body:", err)
		}
	}(resp.Body)

	if resp.StatusCode != http.StatusOK {
		return Pokemon{}, fmt.Errorf("error: status code %d", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return Pokemon{}, err
	}

	var pokemon Pokemon
	err = json.Unmarshal(body, &pokemon)
	if err != nil {
		return Pokemon{}, err
	}

	return pokemon, nil
}

func (api *PokeAPI) fetchEvolutionChain(url string) (EvolutionChain, error) {
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return EvolutionChain{}, err
	}

	resp, err := api.Client.Do(req)
	if err != nil {
		return EvolutionChain{}, err
	}
	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {

		}
	}(resp.Body)

	if resp.StatusCode != http.StatusOK {
		return EvolutionChain{}, fmt.Errorf("error: status code %d", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return EvolutionChain{}, err
	}

	var chain EvolutionChain
	err = json.Unmarshal(body, &chain)
	if err != nil {
		return EvolutionChain{}, err
	}

	return chain, nil
}

func printPokemonDetails(pokemon Pokemon) {
	fmt.Printf("Name: %s\n", pokemon.Name)
	fmt.Printf("ID: %d\n", pokemon.ID)
	fmt.Printf("Height: %d\n", pokemon.Height)
	fmt.Printf("Weight: %d\n", pokemon.Weight)
	fmt.Printf("Types: ")
	for _, t := range pokemon.Types {
		fmt.Printf("%s ", t.Type.Name)
	}
	fmt.Println()
}

func getEvolutionChain(chain Chain, names *[]string) {
	*names = append(*names, chain.Species.Name)
	for _, evolve := range chain.EvolvesTo {
		getEvolutionChain(evolve, names)
	}
}

func printEvolutionChain(chain Chain) {
	var names []string
	getEvolutionChain(chain, &names)
	fmt.Printf("Evolves: %s\n", strings.Join(names, " - "))
}

func isValidID(input string) bool {
	if input == "" {
		return false
	}

	intValue, err := strconv.Atoi(input)
	if intValue <= 0 {
		return false
	}

	return err == nil
}

func main() {
	url := "https://www.dota2.com/hero/legioncommander"
	content, err := fetchURL(url)
	if err != nil {
		fmt.Println("err fetching URL:", err)
		return
	}

	fmt.Println("content of the URL:", content)

	// -- extra challenge --
	client := &http.Client{}
	api := &PokeAPI{
		Client:  client,
		BaseURL: "https://pokeapi.co/api/v2",
	}

	reader := bufio.NewReader(os.Stdin)
	var pokemonNameOrID string
	for {
		fmt.Print("Enter Pokémon number or name: ")
		input, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println("Error reading input:", err)
			continue
		}

		pokemonNameOrID = strings.TrimSpace(input)
		if isValidID(pokemonNameOrID) {
			break
		} else {
			fmt.Println("Invalid input. Please enter a positive integer or a valid Pokémon id.")
		}
	}

	pokemon, err := api.fetchPokemon(pokemonNameOrID)
	if err != nil {
		fmt.Println("Error fetching Pokémon:", err)
		return
	}

	printPokemonDetails(pokemon)

	evolutionChainURL := fmt.Sprintf("%s/evolution-chain/%d", api.BaseURL, pokemon.ID)
	evolutionChain, err := api.fetchEvolutionChain(evolutionChainURL)
	if err != nil {
		fmt.Println("Error fetching evolution chain:", err)
		return
	}

	fmt.Println("Evolution Chain:")
	printEvolutionChain(evolutionChain.Chain)
}
