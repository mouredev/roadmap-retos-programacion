open Lwt
open Cohttp
open Cohttp_lwt_unix
open Yojson.Safe
open Printf

(*****************************************************************************)
(*                                                                           *)
(*                               HTTP Requests                               *)
(*                                                                           *)
(*  HTTP in OCaml is very complex without a library because it has to be     *)
(*  done with the [Unix] networking module, plus it requires heavy know-     *)
(*  ledge of sockets, protocols, parsing, etc. Thankfully, there are many    *)
(*  well maintained libraries out there, [CoHttp] being the most popular     *)
(*  and the one I used in this exercise. It's based on both [Async] and      *)
(*  [Lwt] (lightweight threads, promise-based).                              *)
(*                                                                           *)
(*  I chose to use monadic operators (>>=, >|=) instead of specialized       *)
(*  syntax for self-learning purposes but there is a way to use custom let   *)
(*  bindings like [let%lwt] and [let*] that make the code look more like     *)
(*  async/await in other languages.                                          *)
(*                                                                           *)
(*****************************************************************************)

let http_get_string url =
  Client.get (Uri.of_string url)
  >>= fun (response, body) ->
  let status_code = Code.code_of_status (Response.status response) in
  Cohttp_lwt.Body.to_string body
  >|= fun str_body ->
  if status_code >= 200 && status_code < 400
  then Result.Ok (status_code, str_body)
  else Result.Error status_code
;;

let _ =
  let bacon_ipsum =
    "https://baconipsum.com/api/?type=all-meat&paras=1&start-with-lorem=1&format=html"
  in
  Lwt_main.run
    begin
      http_get_string bacon_ipsum
      >|= fun res ->
      match res with
      | Ok (code, body) ->
        printf "HTTP Call Successful With Code [%d] | HTML:\n" code;
        print_endline body
      | Error code -> printf "HTTP Call Failed With Status Code [%d]!\n" code
    end
;;

(*****************************************************************************)
(*                                                                           *)
(*                        Dificultad Extra (Opcional)                        *)
(*                                                                           *)
(*  Utilizando la PokéAPI (https://pokeapi.co), crea un programa por         *)
(*  terminal al que le puedes solicitar información de un Pokémon concreto   *)
(*  utilizando su nombre o id numérico.                                      *)
(*                                                                           *)
(*  - Muestra el nombre, id, peso, altura, y tipo(s) del Pokémon.            *)
(*  - Muestra el nombre de su cadena de evoluciones                          *)
(*  - Muestra los juegos en los que aparece                                  *)
(*  - Controla posibles errores                                              *)
(*                                                                           *)
(*****************************************************************************)

let http_get_json url =
  http_get_string url
  >|= Result.map (fun (code, str_body) -> code, from_string str_body)
;;

let path_exn path json = Yojson.Safe.Util.path path json |> Option.get
let ( >>>= ) = Lwt_result.bind

module Pokedex = struct
  open Yojson.Safe.Util

  module Pokemon = struct
    type t =
      { id : int
      ; name : string
      ; height : int
      ; weight : int
      ; types : string list
      ; games : string list
      ; evolution_chain : string
      }

    let rec deserialize_ev_chain json =
      let name = json |> path_exn [ "species"; "name" ] |> to_string in
      let evolves_to = json |> member "evolves_to" |> to_list in
      match evolves_to with
      | [] -> name
      | evolutions ->
        let branches =
          List.map deserialize_ev_chain evolutions |> String.concat ", "
        in
        sprintf "%s->[%s]" name branches
    ;;

    let of_json pk_info_json ev_chain_json =
      let name = pk_info_json |> member "name" |> to_string in
      let id = pk_info_json |> member "id" |> to_int in
      let weight = pk_info_json |> member "weight" |> to_int in
      let height = pk_info_json |> member "height" |> to_int in
      let games =
        pk_info_json
        |> member "game_indices"
        |> to_list
        |> List.map (fun t -> t |> path_exn [ "version"; "name" ] |> to_string)
      in
      let types =
        pk_info_json
        |> member "types"
        |> to_list
        |> List.map (fun t -> t |> path_exn [ "type"; "name" ] |> to_string)
      in
      let evolution_chain =
        ev_chain_json |> member "chain" |> deserialize_ev_chain
      in
      { id; name; weight; height; types; games; evolution_chain }
    ;;
  end

  let api_base_url = "https://pokeapi.co/api/v2"

  let display (p : Pokemon.t) =
    printf "Name: %s (#%d)\n" p.name p.id;
    printf "Height: %d | Weight: %d\n" p.height p.weight;
    printf "Type(s): %s\n" (String.concat ", " p.types);
    printf "Game(s): %s\n" (String.concat ", " p.games);
    printf "Evolution Chain: %s\n" p.evolution_chain
  ;;

  let find_by_name name =
    let name = Core.String.lowercase name in
    let pk_info_url = sprintf "%s/pokemon/%s" api_base_url name in
    let pk_species_url = sprintf "%s/pokemon-species/%s" api_base_url name in
    http_get_json pk_species_url
    >>>= fun (_, species_json) ->
    let ev_chain_url =
      species_json |> path_exn [ "evolution_chain"; "url" ] |> to_string
    in
    http_get_json ev_chain_url
    >>>= fun (_, ev_chain_json) ->
    http_get_json pk_info_url
    >>>= fun (_, pk_info_json) ->
    Lwt_result.return (Pokemon.of_json pk_info_json ev_chain_json)
  ;;
end

let _ =
  Moure.Io.prompt_string "Name of the pokemon: "
  |> Pokedex.find_by_name
  |> Lwt_main.run
  |> function
  | Ok pokemon -> Pokedex.display pokemon
  | Error code ->
    printf "Failed to fetch data from the PokéAPI (Status Code: %d)\n" code
;;

(* Output of running [dune exec reto20]:
   -------------------------------------

   HTTP Call Successful With Code [200] | HTML:
   <p>Bacon ipsum dolor amet beef capicola short loin porchetta, swine andouille buffalo cow boudin leberkas ham venison bacon.  Landjaeger tail tenderloin shank, bresaola meatball andouille kielbasa boudin ball tip salami flank swine turkey.  Meatloaf corned beef pork pig kielbasa biltong, sirloin chicken alcatra cow porchetta pork belly ball tip ham.  Hamburger kevin ground round, flank cow biltong pastrami chislic sausage ham capicola meatloaf filet mignon corned beef cupim.  Cupim leberkas frankfurter, filet mignon sirloin venison fatback.</p>

   Name of the pokemon: wurmple
   Name: wurmple (#265)
   Height: 3 | Weight: 36
   Type(s): bug
   Game(s): ruby, sapphire, emerald, firered, leafgreen, diamond, pearl, platinum, heartgold, soulsilver, black, white, black-2, white-2
   Evolution Chain: wurmple->[silcoon->[beautifly], cascoon->[dustox]]

   --------------------------------------------------------------------
   NOTE: The evolution chain of {b wurmple} has 2 branches:
   1. From wurmple to silcoon (which in turn evolves to beautifly)
   2. From wurmple to cascoon (which in turn evolves to dustox)
   Therefore, the chain expressed as a flat string can also be seen as:

                           +---------+     +-----------+
                    +----->| Silcoon |---->| Beautifly |
   +---------+      |      +---------+     +-----------+
   | Wurmple |----->o
   +---------+      |      +---------+     +--------+
                    +----->| Cascoon |---->| Dustox |
                           +---------+     +--------+
*)
