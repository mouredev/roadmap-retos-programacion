(* #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot *)

let () = Random.self_init ()

type participant = { name: string; country: string }
type event = { name: string; mutable participants: participant list }
type country_medals = { country: string; mutable gold: int; mutable silver: int; mutable bronze: int }

let events : event list ref = ref []
let medal_table : (string, country_medals) Hashtbl.t = Hashtbl.create 16

let add_medal country t =
  let cm = match Hashtbl.find_opt medal_table country with
    | Some c -> c
    | None -> let c={country;gold=0;silver=0;bronze=0} in Hashtbl.add medal_table country c; c in
  (match t with "gold"->cm.gold<-cm.gold+1 | "silver"->cm.silver<-cm.silver+1 | _->cm.bronze<-cm.bronze+1)

let shuffle lst =
  let a = Array.of_list lst in
  for i = Array.length a - 1 downto 1 do
    let j = Random.int (i+1) in let tmp=a.(i) in a.(i)<-a.(j); a.(j)<-tmp
  done; Array.to_list a

let read_line_p p = print_string p; flush stdout; String.trim (input_line stdin)

let register_event () =
  let name = read_line_p "Nombre del evento: " in
  if List.exists (fun e -> String.lowercase_ascii e.name = String.lowercase_ascii name) !events
  then Printf.printf "Ya existe.\n"
  else (events := !events @ [{name; participants=[]}]; Printf.printf "Evento '%s' registrado.\n" name)

let register_participant () =
  if !events = [] then print_endline "No hay eventos."
  else begin
    List.iteri (fun i e -> Printf.printf "  %d. %s\n" (i+1) e.name) !events;
    match int_of_string_opt (read_line_p "Numero: ") with
    | None -> print_endline "Invalido."
    | Some idx when idx<1||idx>List.length !events -> print_endline "Invalido."
    | Some idx ->
        let ev = List.nth !events (idx-1) in
        let n = read_line_p "Nombre: " in let c = read_line_p "Pais: " in
        ev.participants <- ev.participants @ [{name=n;country=c}];
        Printf.printf "'%s (%s)' añadido a '%s'.\n" n c ev.name
  end

let simulate_events () =
  if !events = [] then print_endline "No hay eventos."
  else List.iter (fun ev ->
    Printf.printf "\n=== Simulando: %s ===\n" ev.name;
    let n = List.length ev.participants in
    if n < 3 then Printf.printf "  Necesita >=3. Saltando.\n"
    else let s = shuffle ev.participants in
      let g=List.nth s 0 and sl=List.nth s 1 and b=List.nth s 2 in
      Printf.printf "  Oro:    %s (%s)\n" g.name g.country;
      Printf.printf "  Plata:  %s (%s)\n" sl.name sl.country;
      Printf.printf "  Bronce: %s (%s)\n" b.name b.country;
      add_medal g.country "gold"; add_medal sl.country "silver"; add_medal b.country "bronze"
  ) !events

let show_report () =
  print_endline "\n== INFORME FINAL ==";
  if Hashtbl.length medal_table = 0 then print_endline "Sin resultados."
  else begin
    let all = Hashtbl.fold (fun _ v acc -> v::acc) medal_table [] in
    let r = List.sort (fun a b ->
      let cg=compare b.gold a.gold in if cg<>0 then cg
      else let cs=compare b.silver a.silver in if cs<>0 then cs else compare b.bronze a.bronze) all in
    List.iteri (fun i c ->
      Printf.printf "%d. %-20s Oro:%d Plata:%d Bronce:%d Total:%d\n"
        (i+1) c.country c.gold c.silver c.bronze (c.gold+c.silver+c.bronze)) r
  end

let () =
  let run = ref true in
  while !run do
    print_endline "\n====== SIMULADOR JJOO ======";
    print_endline "1. Registrar evento\n2. Registrar participante\n3. Simular\n4. Informe\n5. Salir";
    (match read_line_p "Opcion: " with
    | "1" -> register_event ()
    | "2" -> register_participant ()
    | "3" -> simulate_events ()
    | "4" -> show_report ()
    | "5" -> print_endline "Hasta luego!"; run := false
    | _ -> print_endline "Invalido.")
  done
