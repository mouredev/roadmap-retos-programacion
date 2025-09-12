open Printf

let today () =
  Core.Date.today ~zone:Core.Time_float.Zone.utc |> Core.Date.to_string_american
;;

module Day : sig
  type t

  val of_int : int -> t
  val show : t -> string
end = struct
  type t =
    | Sunday
    | Monday
    | Tuesday
    | Wednesday
    | Thursday
    | Friday
    | Saturday
  [@@deriving show { with_path = false }]

  let of_int = function
    | 1 -> Sunday
    | 2 -> Monday
    | 3 -> Tuesday
    | 4 -> Wednesday
    | 5 -> Thursday
    | 6 -> Friday
    | 7 -> Saturday
    | _ -> raise (Invalid_argument "Day number not between 1 and 7")
  ;;
end

let _ =
  print_endline "These are the days of the week from 1 to 7:";
  for i = 1 to 7 do
    printf "Day #1: %s\n" Day.(of_int i |> show)
  done
;;

(*****************************************************************************)
(*                                                                           *)
(*                        Dificultad Extra (Opcional)                        *)
(*                                                                           *)
(*  Crea un pequeño sistema de gestión del estado de pedidos.                *)
(*  Implementa una clase que define un pedido con las siguientes caracte-    *)
(*  rísticas:                                                                *)
(*                                                                           *)
(*  - El pedido tiene un identificador y un estado.                          *)
(*  - El estado es un Enum con estos valores: PENDIENTE, ENVIADO,            *)
(*    ENTREGADO, y CANCELADO.                                                *)
(*  - Implementa las funciones que sirven para modificar el estado:          *)
(*    - Pedido enviado                                                       *)
(*    - Pedido cancelado                                                     *)
(*    - Pedido entregado                                                     *)
(*  - Establecer lógica, por ejemplo, no se puede entregar si no se ha       *)
(*    enviado, etc...                                                        *)
(*  - Implementa una función para mostrar un texto asociado según el estado  *)
(*    actual.                                                                *)
(*  - Crea diferentes pedidos y muestra cómo se interactúa con ellos.        *)
(*                                                                           *)
(*****************************************************************************)

module Shipment : sig
  exception ShipmentError of string

  type t

  val create : int -> t
  val to_string : t -> string
  val ship : t -> unit
  val deliver : t -> string -> unit
  val cancel : t -> unit
end = struct
  exception ShipmentError of string

  type status =
    | Pending
    | Shipped of string
    | Delivered of (string * string)
    | Cancelled

  type t =
    { mutable history : status list
    ; mutable status : status
    ; id : int
    }

  let create id = { history = []; status = Pending; id }

  let set_status st sh =
    let curr_status = sh.status in
    begin
      match curr_status, st with
      | Pending, Pending
      | Cancelled, Cancelled
      | Shipped _, Shipped _
      | Delivered _, Delivered _ ->
        raise @@ ShipmentError "Current and new status are the same."
      | Pending, Delivered _ ->
        raise
        @@ ShipmentError "Can't deliver a shipment without shipping it first."
      | Cancelled, x when x <> Pending ->
        raise @@ ShipmentError "Can't ship or deliver while cancelled."
      | Shipped _, Pending ->
        raise @@ ShipmentError "Can't set to pending, already shipped."
      | Shipped _, Cancelled ->
        raise @@ ShipmentError "Already shipped, can't cancel."
      | Delivered _, _ -> raise @@ ShipmentError "Already delivered."
      | _ -> ()
    end;
    sh.history <- sh.status :: sh.history;
    sh.status <- st
  ;;

  let show_status = function
    | Pending -> "Pending"
    | Shipped date -> sprintf "Shipped on %s" date
    | Delivered (date, signed_by) ->
      sprintf "Delivered on %s (signed: %s)" date signed_by
    | Cancelled -> "Cancelled"
  ;;

  let to_string { history; status; id } =
    sprintf "Shipment #%d Information\n" id
    ^ sprintf "Current status: %s\n" (show_status status)
    ^ "-------------------------\n"
    ^ "Status change history:\n"
    ^ (List.rev history
       |> List.mapi (fun i status ->
         string_of_int (i + 1) ^ " - " ^ show_status status)
       |> String.concat "\n")
    ^ "\n"
  ;;

  let ship sh = set_status (Shipped (today ())) sh
  let deliver sh signed_by = set_status (Delivered (today (), signed_by)) sh
  let cancel sh = set_status Cancelled sh
end

let safe_perform f =
  try f () with
  | Shipment.ShipmentError msg -> printf "[SHIPMENT ERROR]: %s\n" msg
;;

let _ =
  let mock_shipment_1 = Shipment.create 23677 in
  let mock_shipment_2 = Shipment.create 15622 in
  print_endline "Here are 2 newly created shipments, stringified:";
  print_string (Shipment.to_string mock_shipment_1);
  print_string (Shipment.to_string mock_shipment_2);
  print_endline "Changes will be done to both...";
  safe_perform (fun () -> Shipment.cancel mock_shipment_1);
  safe_perform (fun () -> Shipment.ship mock_shipment_1);
  safe_perform (fun () -> Shipment.cancel mock_shipment_1);
  safe_perform (fun () -> Shipment.deliver mock_shipment_2 "John Doe");
  safe_perform (fun () -> Shipment.ship mock_shipment_2);
  safe_perform (fun () -> Shipment.deliver mock_shipment_2 "Luis Lopez");
  print_endline "Now that changes were made, show shipments again:";
  print_string (Shipment.to_string mock_shipment_1);
  print_string (Shipment.to_string mock_shipment_2)
;;

(* Output of [dune exec reto19]

   These are the days of the week from 1 to 7:
   Day #1: Sunday
   Day #1: Monday
   Day #1: Tuesday
   Day #1: Wednesday
   Day #1: Thursday
   Day #1: Friday
   Day #1: Saturday
   Here are 2 newly created shipments, stringified:
   Shipment #23677 Information
   Current status: Pending
   -------------------------
   Status change history:

   Shipment #15622 Information
   Current status: Pending
   -------------------------
   Status change history:

   Changes will be done to both...
   [SHIPMENT ERROR]: Can't ship or deliver while cancelled.
   [SHIPMENT ERROR]: Current and new status are the same.
   [SHIPMENT ERROR]: Can't deliver a shipment without shipping it first.
   Now that changes were made, show shipments again:
   Shipment #23677 Information
   Current status: Cancelled
   -------------------------
   Status change history:
   1 - Pending
   Shipment #15622 Information
   Current status: Delivered on 05/13/2024 (signed: Luis Lopez)
   -------------------------
   Status change history:
   1 - Pending
   2 - Shipped on 05/13/2024
*)
