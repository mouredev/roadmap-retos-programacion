open Printf

(******************************************************************************)
(*                                                                            *)
(*                           The Singleton Pattern                            *)
(*                                                                            *)
(*  Singleton in terms of software design patterns, popularized by the        *)
(*  'gang of four' in the OOP sphere, is a class that can only have one       *)
(*  instance in memory and can be shared everywhere in the project.           *)
(*  This is very useful for stuff like resource pools, dependency injection,  *)
(*  global state managers, and any situation in which no more than one        *)
(*  instance of a class needs to be created.                                  *)
(*                                                                            *)
(*  In an OOP language like Java, C# or C++, the way we implement this pa-    *)
(*  ttern is by making the constructor private and instead exposing a method  *)
(*  that will create the instance if it doesn't exist yet (NULL reference),   *)
(*  or return the current instance otherwise. However, OCaml is a functional  *)
(*  language, therefore we need to make use of module-level bindings combi-   *)
(*  ned with the concet of a mutable reference or a record with mutable       *)
(*  fields to simulate a global state variable that we can write and read     *)
(*  to and from. Ideally we'd also need to make use of a Mutex.               *)
(*                                                                            *)
(*                                [ N O T E ]                                 *)
(*  OCaml's built-in class syntax has no concept of a static members and      *)
(*  private constructors so we can't make use of the [class] keyword here.    *)
(*                                                                            *)
(******************************************************************************)

module Singleton : sig
  val get_data : unit -> int
  val set_data : int -> unit
end = struct
  let instance = ref 0
  let get_data () = !instance
  let set_data data = instance := data
end

let _ =
  print_endline "Singleton module [Singleton] has a globally accessible";
  print_endline "value as a mutable reference, emulating a singleton in OOP!";
  print_newline ();
  printf "Current value: [%d] | Changing to [5]...\n" @@ Singleton.get_data ();
  Singleton.set_data 5;
  printf "New current value: [%d]\n" @@ Singleton.get_data ();
  print_newline ()
;;

(*****************************************************************************)
(*                                                                           *)
(*                        Dificultad Extra (Opcional)                        *)
(*                                                                           *)
(*  Utiliza el patrón de diseño "singleton" para representar una clase que   *)
(*  haga referencia a la sesión de usuario de una aplicación ficticia.       *)
(*  La sesión debe permitir asignar un usuario (id, username, nombre y e-    *)
(*  mail), recuperar los datos del usuario y borrar los datos de la sesión.  *)
(*                                                                           *)
(*****************************************************************************)

module SessionManager : sig
  type session

  val set_data : int -> string -> string -> string -> unit
  val get_data : unit -> session option
  val clear : unit -> unit
  val show : unit -> string
end = struct
  type session =
    { id : int
    ; username : string
    ; full_name : string
    ; email : string
    }
  [@@deriving show { with_path = false }]

  let data : session option ref = ref None

  let set_data id username full_name email =
    data := Some { id; username; full_name; email }
  ;;

  let show () =
    match !data with
    | None -> "{ NO SESSION! }"
    | Some session -> show_session session
  ;;

  let get_data () = !data
  let clear () = data := None
end

let _ =
  print_endline "Session management system:";
  print_endline "--------------------------";
  printf "Current session: %s\n" @@ SessionManager.show ();
  print_endline "Setting the session with a new user...";
  SessionManager.set_data
    2399
    "luishendrix92"
    "Luis Felipe Lopez Garay"
    "luishendrix92@gmail.com";
  printf "Current session: %s\n" @@ SessionManager.show ();
  print_endline "Deleting session data from a different thread...";
  Thread.create (fun () -> SessionManager.clear ()) () |> Thread.join;
  printf "Current session: %s\n" @@ SessionManager.show ()
;;

(*
  Output
  ===========================================================
  Singleton module [Singleton] has a globally accessible
  value as a mutable reference, emulating a singleton in OOP!

  Current value: [0] | Changing to [5]...
  New current value: [5]

  Session management system:
  --------------------------
  Current session: { NO SESSION! }
  Setting the session with a new user...
  Current session: { id = 2399; username = "luishendrix92";
    full_name = "Luis Felipe Lopez Garay"; email = "luishendrix92@gmail.com" }
  Deleting session data from a different thread...
  Current session: { NO SESSION! }
  ===========================================================
*)
