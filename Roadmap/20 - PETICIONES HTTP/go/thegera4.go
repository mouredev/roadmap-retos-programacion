 package main

 import (
	"fmt"
	"net/http"
	"io"
	"encoding/json"
	"os"
)

// Estructura para almacenar los datos del Pokémon de acuerdo a lo solicitado en la descripcion del ejercicio extra
type PokemonData struct {
	ID     int    `json:"id"`
	Name   string `json:"name"`
	Weight int    `json:"weight"`
	Height int    `json:"height"`
	Types  []struct {
		Type struct {
			Name string `json:"name"`
		} `json:"type"`
	} `json:"types"`
	Forms []struct {
		Name string `json:"name"`
	} `json:"forms"`
	Games []struct {
		Version struct {
			Name string `json:"name"`
		} `json:"version"`
	} `json:"game_indices"`
}

func main() {

	// Ejercicio: Petición HTTP
	response, err := http.Get("https://jsonplaceholder.typicode.com/posts")
	if err != nil {
		fmt.Println("Error making request")
		os.Exit(1)
	}
	
	defer response.Body.Close() // Se debe cerrar el body al finalizar la ejecución

	body, err := io.ReadAll(response.Body)
	if err != nil {
		fmt.Println("Error reading body")
		os.Exit(1)
	}

	fmt.Println(string(body))

	// Ejercicio Extra
	pokeApi()

}

func pokeApi() {
	for {
		fmt.Println("Introduce el nombre o número de un Pokémon o pulsa la tecla 'c + enter' para salir:")
		var pokemon string
		fmt.Scanln(&pokemon)

		if pokemon == "c" { break }
	
		pokemonData, err := getPokemon(pokemon)
		if err != nil {
			fmt.Println("Error while getting Pokémon data")
			continue
		}

		printPokemonData(pokemonData)
	}
}

func getPokemon(pokemon string) (PokemonData, error) {
	response, err := http.Get("https://pokeapi.co/api/v2/pokemon/" + pokemon)
	if err != nil {
		fmt.Println("Error making request")
		return PokemonData{}, err
	}
	
	defer response.Body.Close() // Se debe cerrar el body al finalizar la ejecución

	body, err := io.ReadAll(response.Body)
	if err != nil {
		fmt.Println("Error reading body")
		return PokemonData{}, err
	}

	var pokemonData PokemonData
	err = json.Unmarshal(body, &pokemonData)
	if err != nil {
		fmt.Println("Error unmarshalling body")
		return PokemonData{}, err
	}

	return pokemonData, nil
}

func printPokemonData (pokemonData PokemonData) {
	fmt.Printf("ID: %d\n", pokemonData.ID)
	fmt.Printf("Nombre: %s\n", pokemonData.Name)
	fmt.Printf("Peso: %d\n", pokemonData.Weight)
	fmt.Printf("Altura: %d\n", pokemonData.Height)

	fmt.Printf("Tipos: ")
	for i, t := range pokemonData.Types {
		if i > 0 {
			fmt.Print(", ")
		}
		fmt.Print(t.Type.Name)
	}
	fmt.Println()

	fmt.Printf("Cadena de evoluciones: ")
	for i, f := range pokemonData.Forms {
		if i > 0 {
			fmt.Print(", ")
		}
		fmt.Print(f.Name)
	}
	fmt.Println()

	fmt.Printf("Juegos en que aparece:")
	for i, g := range pokemonData.Games {
		if i > 0 {
			fmt.Print(", ")
		}
		fmt.Print(g.Version.Name)
	}
	fmt.Println()
}