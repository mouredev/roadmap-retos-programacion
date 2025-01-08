open Printf

(****************************************************************************)
(*                                                                          *)
(*                             Callbacks (HoF)                              *)
(*                                                                          *)
(*  As a functional programming language, OCaml is perfectly capable of     *)
(*  treating functions as first-class citizens; meaning, we can store them  *)
(*  inside variables, accept them as parameters, return them from other     *)
(*  functions, and more!                                                    *)
(*                                                                          *)
(*  In programming, a {b callback} is a function that is passed as an       *)
(*  argument to a function, which will be later called (with or without     *)
(*  arguments) once a certain task is completed synchronously or            *)
(*  asynchronously. The term was popularized by the inception of NodeJS's   *)
(*  single-threaded concurrent programming but it goes beyond just that...  *)
(*  both in history and use cases. A callback can be just a function that   *)
(*  represent a strategy, or can be a set of instructions to run at a       *)
(*  certain point in time; it can be virtually any type of function,        *)
(*  really; as long as it's passed as an argument to another function.      *)
(*                                                                          *)
(****************************************************************************)

let with_named_parameters ~callback name =
  let greeting = sprintf "Hello, %s! How are you today?" name in
  printf "HoF 'with_named_parameters' will run callback with [%s]...\n" name;
  callback greeting;
  print_endline
    "Higher-Order Function 'with_named_parameters' finished execution!"
;;

let _ =
  (* Why have [callback] as a named parameter?
     It's idiomatic in the OCaml world... *)
  with_named_parameters
    ~callback:(fun greeting -> printf "Greeting received: %s\n" greeting)
    "Luis";
  print_newline ()
;;

(**************************************************************************)
(*                                                                        *)
(*                      Dificultad Extra (opcional)                       *)
(*                                                                        *)
(*  Crea un simulador de pedidos de un restaurante utilizando callbacks.  *)
(*  Estará formado por una función que procesa pedidos.                   *)
(*  Debe aceptar el nombre del plato, una callback de confirmación, una   *)
(*  de listo, y otra de entrega.                                          *)
(*                                                                        *)
(*  - Debe imprimir una confirmación cuando empiece el procesamiento.     *)
(*  - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre        *)
(*    procesos.                                                           *)
(*  - Debe invocar a cada callback siguiendo un orden de procesado.       *)
(*  - Debe notificar que el plato está listo o ha sido entregado.         *)
(*                                                                        *)
(**************************************************************************)

let wait_between_1_and_10_seconds () = Thread.delay (Random.float 9.0 +. 1.0)

module Restaurant : sig
  val show_menu : unit -> unit

  val place_order
    :  on_confirmed:(unit -> unit)
    -> on_ready:(unit -> unit)
    -> on_delivered:(string -> unit)
    -> int
    -> unit
end = struct
  Random.self_init ()

  type dish =
    | HotDog
    | Cheeseburger
    | CaesarSalad
    | Chicken
    | Shortcake
    | Ramen
  [@@deriving show]

  let dish_of_int = function
    | 1 -> HotDog
    | 2 -> Cheeseburger
    | 3 -> CaesarSalad
    | 4 -> Chicken
    | 5 -> Shortcake
    | 6 -> Ramen
    | _ -> raise (Invalid_argument "Dish number not in the menu")
  ;;

  let dish_to_emoji = function
    | HotDog -> "🌭"
    | Cheeseburger -> "🍔"
    | CaesarSalad -> "🥗"
    | Chicken -> "🍗"
    | Shortcake -> "🍰"
    | Ramen -> "🍜"
  ;;

  let show_menu () =
    print_endline "#1 <- Hot dog";
    print_endline "#2 <- Cheeseburger";
    print_endline "#3 <- Caesar salad";
    print_endline "#4 <- Chicken wings";
    print_endline "#5 <- Strawberry shortcake";
    print_endline "#6 <- Ramen bowl"
  ;;

  let process_order ~on_confirmed ~on_ready ~on_delivered dish =
    wait_between_1_and_10_seconds ();
    print_endline "Order was confirmed, invoking confirmation callback...";
    on_confirmed ();
    wait_between_1_and_10_seconds ();
    print_endline "Order is ready, invoking readiness callback...";
    on_ready ();
    wait_between_1_and_10_seconds ();
    print_endline "Order being delived to table, invoking delivery callback...";
    on_delivered (dish_to_emoji dish)
  ;;

  let place_order ~on_confirmed ~on_ready ~on_delivered dish_number =
    let dish = dish_of_int dish_number in
    let order_thread =
      Thread.create (process_order ~on_confirmed ~on_ready ~on_delivered) dish
    in
    printf
      "Restaurant cashier says: Order [%s] has been placed!\n"
      (show_dish dish);
    print_endline "---------------------------------------------------";
    Thread.join order_thread
  ;;
end

let _ =
  print_endline "Welcome to my restaurant! Here's the menu:";
  Restaurant.show_menu ();
  let dish_number =
    Moure.Io.prompt
      ~err_msg:"Invalid number"
      ~f:int_of_string
      "Choose a menu item between 1 and 6: "
  in
  match dish_number with
  | Ok dish_number ->
    Restaurant.place_order
      ~on_confirmed:(fun () ->
        print_endline "Customer says: Time to take a seat :)")
      ~on_ready:(fun () ->
        print_endline "Customer says: Food's ready? I'll be waiting!")
      ~on_delivered:(fun emoji ->
        printf "Customer says: Yum, time to eat my [%s]!\n" emoji)
      dish_number
  | Error msg -> print_endline msg
;;

(* Output of [dune exec reto21]:

   HoF 'with_named_parameters' will run callback with [Luis]...
   Greeting received: Hello, Luis! How are you today?
   Higher-Order Function 'with_named_parameters' finished execution!

   Welcome to my restaurant! Here's the menu:
   #1 <- Hot dog
   #2 <- Cheeseburger
   #3 <- Caesar salad
   #4 <- Chicken wings
   #5 <- Strawberry shortcake
   #6 <- Ramen bowl
   Choose a menu item between 1 and 6: 2
   Restaurant cashier says: Order [Reto21.Restaurant.Cheeseburger] has been placed!
   ---------------------------------------------------
   Order was confirmed, invoking confirmation callback...
   Customer says: Time to take a seat :)
   Order is ready, invoking readiness callback...
   Customer says: Food's ready? I'll be waiting!
   Order being delived to table, invoking delivery callback...
   Customer says: Yum, time to eat my [🍔]!
*)
