open Printf;;

Random.self_init ()

(******************************************************************************)
(*                                                                            *)
(*                                 EJERCICIO                                  *)
(*                                                                            *)
(*  Los JJOO de París 2024 han comenzado! Crea un programa que simule la ce-  *)
(*  lebración de los juegos. El programa debe permitir al usuario registrar   *)
(*  eventos y participantes, realizar la simulación de los eventos asignando  *)
(*  posiciones de manera aleatorio y generar un informe final. Por terminal.  *)
(*                                                                            *)
(*  Requisitos:                                                               *)
(*  1. Registrar eventos deportivos.                                          *)
(*  2. Registrar participantes por nombre y país.                             *)
(*  3. Simular eventos de manera aleatoria en base a los participantes (>2).  *)
(*  4. Asignar medallas (oro, plata, y bronce) según los resultados.          *)
(*  5. Mostrar los ganadores por cada evento.                                 *)
(*  6. Mostrar el ranking de paises segun el numero de medallas.              *)
(*                                                                            *)
(*  Acciones:                                                                 *)
(*  1. Registro de eventos.                                                   *)
(*  2. Registro de participantes.                                             *)
(*  3. Simulación de eventos.                                                 *)
(*  4. Creación de informes.                                                  *)
(*  5. Salir del programa.                                                    *)
(*                                                                            *)
(******************************************************************************)

type sport =
  | Swimming
  | Judo
  | Archery
  | Gymnastics
  | Cycling
  | Boxing
  | Track
  | Diving
  | Athletism

type medal =
  | Bronze
  | Silver
  | Gold

class participant name' country' sport' =
  object
    val mutable medals : medal list = []
    val name : string = name'
    val country : string = country'
    val sport : sport = sport'
    method get_name = name
    method get_sport = sport
    method get_country = country
    method award_medal medal = medals <- medal :: medals
    method medal_count = List.length medals
  end

class event sport' =
  object
    val mutable participants : participant list = []
    val creation_timestamp = Core.Time_float.now ()
    val mutable concluded = false
    val sport : sport = sport'

    method add_participant (p : participant) =
      if List.find_opt (fun p' -> p'#get_name = p#get_name) participants
         |> Option.is_some
      then Result.Error (p#get_name ^ " already participates in the event")
      else if p#get_sport <> sport
      then Result.Error (p#get_name ^ "'s sport doesn't match event's")
      else begin
        participants <- p :: participants;
        Result.Ok ()
      end

    method simulate =
      if concluded
      then Result.Error "This event already concluded."
      else if List.length participants < 3
      then Result.Error "Need 3 or more participants to simulate."
      else begin
        let shuffled = participants |> Array.of_list in
        Array.shuffle ~rand:Random.int shuffled;
        let shuffled = Array.to_list shuffled in
        Core.List.take shuffled 3
        |> List.iteri (fun i p ->
          match i with
          | 0 -> p#award_medal Gold
          | 1 -> p#award_medal Silver
          | 2 -> p#award_medal Bronze
          | _ -> ());
        concluded <- true;
        Result.Ok shuffled
      end

    method get_participants = participants
  end

let simulation_report =
  Result.fold
    ~error:print_endline
    ~ok:
      (List.iteri (fun i (p : participant) ->
         match i with
         | 0 -> printf "%d. 🥇 %s (%s)\n" (i + 1) p#get_name p#get_country
         | 1 -> printf "%d. 🥈 %s (%s)\n" (i + 1) p#get_name p#get_country
         | 2 -> printf "%d. 🥉 %s (%s)\n" (i + 1) p#get_name p#get_country
         | _ -> printf "%d. %s (%s)\n" (i + 1) p#get_name p#get_country))
;;

module StringMap = Map.Make (String)

let _ =
  (* 1. Registrar eventos y participantes*)
  let archery = new event Archery in
  let swimming = new event Swimming in
  [ new participant "Baptiste Addis" "France" Archery |> archery#add_participant
  ; new participant "Kim Woo-jin" "South Korea" Archery
    |> archery#add_participant
  ; new participant "Florian Unruh" "Germany" Archery |> archery#add_participant
  ; new participant "Li Jiaman" "China" Archery |> archery#add_participant
  ; new participant "Brady Ellison" "USA" Archery |> archery#add_participant
  ; new participant "Thomas ceccon" "Italy" Swimming |> swimming#add_participant
  ; new participant "Daniel Wiffen" "Ireland" Swimming
    |> swimming#add_participant
  ; new participant "Leon Manchard" "France" Swimming
    |> swimming#add_participant
  ; new participant "Bobby Finke" "USA" Swimming |> swimming#add_participant
  ; new participant "Pan Shanle" "China" Swimming |> swimming#add_participant
  ]
  |> List.iter (Result.iter_error print_endline);
  (* Simular eventos al azar e informe *)
  print_endline "Simulation of Archery event:";
  simulation_report archery#simulate;
  print_newline ();
  print_endline "Simulation of Swimming event:";
  simulation_report swimming#simulate;
  print_newline ();
  (* Ranking de países según medallas ganadas *)
  let roster = archery#get_participants @ swimming#get_participants in
  roster
  |> List.map (fun p -> p#get_country, p#medal_count)
  |> List.fold_left
       (fun ranking (country, medals) ->
         StringMap.update
           country
           (function
             | Some count -> Some (count + medals)
             | None -> Some medals)
           ranking)
       StringMap.empty
  |> StringMap.to_list
  |> Core.List.stable_sort ~compare:(fun (_, medals_a) (_, medals_b) ->
    Int.compare medals_b medals_a)
  |> List.iteri (fun i (country, medals) ->
    printf "#%d - Country: %s | Medals: %d\n" (i + 1) country medals)
;;
