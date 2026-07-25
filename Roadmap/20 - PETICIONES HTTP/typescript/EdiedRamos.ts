// Author: EdiedRamos

import * as process from "process";

interface PokemonType {
  name: string;
  url: string;
}

interface GameVersion {
  name: string;
  url: string;
}

interface PokemonResponse {
  id: number;
  name: string;
  weight: number;
  height: number;
  types: {
    type: PokemonType;
  }[];
  game_indices: {
    version: GameVersion;
  }[];
}

interface PokemonSpeciesResponse {
  evolution_chain: {
    url: string;
  };
}

interface Species {
  name: string;
  url: string;
}

interface Chain {
  evolves_to: Chain[];
  species: Species;
}

interface PokemonEvolutionResponse {
  chain: Chain;
}

class Pokemon {
  private name: string;
  private id: number;
  private weight: number;
  private height: number;
  private types: string[];
  private evolutions: string[];
  private games: string[];

  constructor(
    private pokemonBaseInformation: PokemonResponse,
    private pokemonEvolutions: PokemonEvolutionResponse
  ) {
    this.loadInformation();
  }

  private loadInformation() {
    this.id = this.pokemonBaseInformation.id;
    this.name = this.pokemonBaseInformation.name;
    this.weight = this.pokemonBaseInformation.weight;
    this.height = this.pokemonBaseInformation.height;
    this.types = this.pokemonBaseInformation.types.map(({ type }) => type.name);
    this.games = this.pokemonBaseInformation.game_indices.map(
      ({ version }) => version.name
    );
    this.evolutions = this.evolutionPath(this.pokemonEvolutions.chain, []);
  }

  private evolutionPath(chain: Chain, currentPath: string[]): string[] {
    currentPath.push(chain.species.name);
    if (chain.evolves_to.length === 0) return currentPath;
    return this.evolutionPath(chain.evolves_to[0], currentPath);
  }

  get toString(): string {
    return `
    ${"=".repeat(20)}
    Id: ${this.id}
    Nombre: ${this.name}
    Peso: ${this.weight}
    Altura: ${this.height}
    Tipos: ${this.types.join(",")}
    Juegos: ${this.games.join(",")}
    Evoluciones: ${this.evolutions.join(",")}
    ${"=".repeat(20)}
    `;
  }
}

class Fetcher {
  static async get<T>(endpoint: string): Promise<T> {
    const response = await fetch(endpoint);
    const data = (await response.json()) as T;
    return data;
  }
}

class PokemonFetcher {
  private static baseUrl = "https://pokeapi.co/api/v2/";

  static async fetchPokemonInformation(
    pokemonTarget: string
  ): Promise<PokemonResponse> {
    return await Fetcher.get<PokemonResponse>(
      `${this.baseUrl}pokemon/${pokemonTarget}`
    );
  }

  static async fetchPokemonSpecies(
    pokemonTarget: string
  ): Promise<PokemonSpeciesResponse> {
    return await Fetcher.get<PokemonSpeciesResponse>(
      `${this.baseUrl}pokemon-species/${pokemonTarget}`
    );
  }

  static async fetchPokemonEvolutionFromURL(
    evolutionURL: string
  ): Promise<PokemonEvolutionResponse> {
    return await Fetcher.get<PokemonEvolutionResponse>(evolutionURL);
  }
}

class PokemonService {
  static async searchInformation(pokemonTarget: string): Promise<string> {
    try {
      const pokemonBaseInformation =
        await PokemonFetcher.fetchPokemonInformation(pokemonTarget);
      const pokemonSpecies = await PokemonFetcher.fetchPokemonSpecies(
        pokemonTarget
      );
      const pokemonEvolutions =
        await PokemonFetcher.fetchPokemonEvolutionFromURL(
          pokemonSpecies.evolution_chain.url
        );

      const pokemon = new Pokemon(pokemonBaseInformation, pokemonEvolutions);
      return pokemon.toString;
    } catch (error) {
      return `
    ${"=".repeat(20)}
    Pokémon no encontrado...
    ${"=".repeat(20)}
      `;
    }
  }
}

function menu() {
  console.log("Ingrese el nombre o id del pokémon (o 'salir' para terminar): ");

  process.stdin.on("data", async (data: string) => {
    const input = data.toString().trim().toLowerCase();

    if (input === "salir") {
      console.log("Saliendo del programa...\n");
      process.stdin.close();
    } else {
      const information = await PokemonService.searchInformation(input);
      console.log(information);
      console.log(
        "Ingrese el nombre o id del pokémon (o 'salir' para terminar): "
      );
    }
  });
}

(() => menu())();
