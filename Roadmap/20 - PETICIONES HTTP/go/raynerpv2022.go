/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */

package main

import (
	"encoding/json"
	"fmt"
	"io"

	"net/http"
)

func exercice(url string) {
	resp, err := http.Get(url)

	if err != nil {

		fmt.Printf("Error readinng web site %v\n", err)
		return
	}
	defer resp.Body.Close()
	data, err := io.ReadAll(resp.Body)

	if err != nil {
		fmt.Printf("Error readinng data %v", err)
	}
	if resp.StatusCode == 200 {
		fmt.Println("Conexion Exitosa. Code :", resp.StatusCode)
	}
	fmt.Println(string(data))

}

func getPokeUrl(url string) *http.Response {
	response, e := http.Get(url)

	if e != nil {

		fmt.Printf("Error de Red %v \n", e)
		return nil
	}

	if response.StatusCode == http.StatusNotFound {
		fmt.Println("Pokemmon no encontrado ")
		return nil
	}

	return response
}

func extra() {

	var PokemonName string
	fmt.Println("Nombre o NUmero del Pokemon ")
	fmt.Scanln(&PokemonName)
	url := fmt.Sprintf("https://pokeapi.co/api/v2/pokemon/%v", PokemonName)
	fmt.Println(url)

	response := getPokeUrl(url)
	if response == nil {
		return
	}
	// response, e := http.Get(url)

	// if e != nil {

	// 	fmt.Printf("Error de Red %v \n", e)
	// 	return
	// }

	// if response.StatusCode == http.StatusNotFound {
	// 	fmt.Println("Pokemmon no encontrado ")
	// 	return
	// }

	defer response.Body.Close()

	data, e := io.ReadAll(response.Body)
	if e != nil {
		fmt.Printf("Error reading Data %v \n", e)
		return
	}

	var poke Pokemon
	e = json.Unmarshal(data, &poke)
	if e != nil {
		fmt.Printf("Error json data %v\n", e)
		return
	}

	fmt.Printf("Name : %v\t", poke.Name)
	fmt.Printf("ID : %v\t", poke.Id)
	fmt.Printf("Weight : %v\t", poke.Weight)
	fmt.Printf("Height : %v\t\n", poke.Height)

	fmt.Println("tIpOs")

	for _, v := range poke.Types {
		fmt.Printf("  \t Name %v  URL %v  \n", v.Type.Name, v.Type.Url)

	}
	fmt.Println("Games")
	for _, v := range poke.GameIndices {
		fmt.Printf("  \t Index %v  Name %v URL %v  \n", v.GameIndex, v.Version.Name, v.Version.Url)
	}

	specie_url := fmt.Sprintf("https://pokeapi.co/api/v2/pokemon-species//%v", PokemonName)

	Respspecie := getPokeUrl(specie_url)

	if Respspecie == nil {

		return
	}

	defer Respspecie.Body.Close()

	data, e = io.ReadAll(Respspecie.Body)

	if e != nil {
		fmt.Printf("Error reading Data %v \n", e)
		return
	}

	var evolutionChain EvolutionChainUrl
	e = json.Unmarshal(data, &evolutionChain)
	if e != nil {
		fmt.Printf("Error json data %v\n", e)
		return
	}

	fmt.Println("URL", evolutionChain.Evolution_chain.Url)

	evolution_chain := getPokeUrl(evolutionChain.Evolution_chain.Url)
	if evolution_chain == nil {

		return
	}
	defer evolution_chain.Body.Close()

	var evolution_to eEvo
	respEvolutio_to, _ := io.ReadAll(evolution_chain.Body)
	_ = json.Unmarshal(respEvolutio_to, &evolution_to)

	fmt.Println("EStado Original : ", evolution_to.Chain.Species.Name)
	fmt.Println("Cadena de Evolution: ")
	printEvo(evolution_to.Chain)

}

func printEvo(dd Ggg) {

	for _, evo := range dd.Evolve_to {
		printEvo(evo)
		fmt.Println(evo.Species.Name)

	}

}

func GetPokemon(url string) *http.Response {
	response, e := http.Get(url)

	if e != nil {

		fmt.Printf("Error de Red %v \n", e)
		return nil
	}

	if response.StatusCode == http.StatusNotFound {
		fmt.Println("Pokemmon no encontrado ")
		return nil
	}

	defer response.Body.Close()
	return response

}

type eEvo struct {
	Chain Ggg `json:"chain"`
}

type Ggg struct {
	Evolve_to []Ggg `json:"evolves_to"`

	Species struct {
		Name string `json:"name"`
	} `json:"species"`
}

type EvolutionChainUrl struct {
	Evolution_chain struct {
		Url string `json:"url"`
	} `json:"evolution_chain"`
}

type Pokemon struct {
	Id     int    `json:"id"`
	Name   string `json:"name"`
	Weight int    `json:"weight"`
	Height int    `json:"height"`

	GameIndices []struct {
		GameIndex int `json:"game_index"`
		Version   struct {
			Name string `json:"name"`
			Url  string `json:"url"`
		} `json:"version"`
	} `json:"game_indices"`

	Types []struct {
		Slot int `json:"slot"`
		Type struct {
			Name string `json:"name"`
			Url  string `json:"url"`
		} `json:"type"`
	} `json:"types"`
}

func main() {
	// exercice("https://mouredev.pro")
	extra()
}
