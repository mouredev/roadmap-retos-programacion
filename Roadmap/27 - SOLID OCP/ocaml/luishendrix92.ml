open Printf

(******************************************************************************)
(*                                                                            *)
(*                            Open-Close Principle                            *)
(*                                                                            *)
(*  It states that entities (methods, functions, modules, classes) should     *)
(*  not be altered while adding new functionality (unless for a bug). Means   *)
(*  that existing code should be open for extension and closed for modifica-  *)
(*  tion. Altering existing code while adding new functionalities requires    *)
(*  features to be tested again.                                              *)
(*                                                                            *)
(*  In OCaml, a primarily functional language, this principle is interpreted  *)
(*  very differently than the OOP counterpart as it does not offer easy       *)
(*  ways to leverage the module system to play around with modules the same   *)
(*  way we'd play with classes in a language like Java or C#. However, the    *)
(*  language's way of extending things comes in the form of module functors,  *)
(*  function composition, variants and pattern matching; along with simple    *)
(*  {e class types} that can be thought of as interfaces.                     *)
(*                                                                            *)
(******************************************************************************)

type action =
  | Payment
  | SomethingElse
[@@deriving show]

module CloudLogService = struct
  let save_error msg = printf "Letting CloudLog save this error: %s\n" msg
end

module PaymentBroker = struct
  let inform_error msg =
    printf "Letting our payment broker know something went wrong: %s\n" msg
  ;;
end

module AppLogger : sig
  (* One of the most frequent examples is a logger with different strategies
     that grows bigger when the developer adds new functionality in the form
     of a very large if statement (or switch). To refactor this, OOP uses
     inheritance or interfaces but in OCaml we use functors. *)

  val log_error : origin:action -> string -> unit
end = struct
  let log_error ~origin msg =
    begin
      match origin with
      | Payment -> PaymentBroker.inform_error msg
      | SomethingElse -> ()
    end;
    CloudLogService.save_error msg;
    printf "[ERROR] [%s] %s\n" (show_action origin) msg
  ;;
end

(* We can now refactor and maybe achieve something similar to inheritance using
   functors (modules that return modules) in order to comply with the OCP.
   Another possible solution would be to use the strategy pattern and/or higher
   -order functions that we pass everytime we use the base logger. *)

module BaseLogger (Extended : sig
    val log_error : string -> unit
  end) =
struct
  let log_error ~origin msg =
    CloudLogService.save_error msg;
    printf "[ERROR] [%s] %s\n" (show_action origin) msg;
    Extended.log_error msg
  ;;
end

module PaymentLogger = BaseLogger (struct
    let log_error = PaymentBroker.inform_error
  end)

(* Another common example is creating interfaced classes for every concrete
   type of a particular abstract type and have them override a method that
   clients will use regardless of what subtype it belongs to.

   This is handled with pattern-matching in OCaml and it's exactly the type
   of code that OCP tries to avoid, but all the developer has to do is be
   smart about where the decision making is done and if modifying it can
   break things that aren't supposed to break. *)

module Shape = struct
  type t =
    | Rectangle of float * float
    | Triangle of float * float
    | Circle of float
    | Square of float

  let area = function
    (* Technically these could be broken into separate functions that maybe live
       in a module. This declutters the decision making code and enforces SRP. *)
    | Circle radius -> Float.pi *. radius *. radius
    | Square length -> length *. length
    | Triangle (b, h) -> b *. h /. 2.0
    | Rectangle (w, h) -> w *. h
  ;;
end

(* OCaml has had classes (although limited) for a while now and I believe it's
   wise to use them when your code is heavily reliant on mutable state. *)
class type shape = object
  method area : float
end

class rectangle (w : float) (h : float) =
  object
    val mutable height = h
    val mutable width = w
    method area = width *. height
  end

class triangle (b : float) (h : float) =
  object
    val mutable base = b
    val mutable height = h
    method area = base *. height
  end

class circle (r : float) =
  object
    val mutable radius = r
    method area = Float.pi *. radius *. radius
  end

class square (l : float) =
  object
    val mutable length = l
    method area = length *. length
  end

let _ =
  let shapes : shape list =
    [ new rectangle 5.0 3.0
    ; new triangle 10.0 5.0
    ; new circle 2.0
    ; new square 7.0
    ]
  in
  print_endline "Shape areas:";
  shapes
  |> List.map (fun s -> s#area)
  |> List.map string_of_float
  |> List.iter print_endline
;;

(******************************************************************************)
(*                                                                            *)
(*                        DIFICULTAD EXTRA (Opcional)                         *)
(*                                                                            *)
(******************************************************************************)
type token =
  | Add
  | Subtract
  | Multiply
  | Divide
  | Power

let add a b = a +. b
let subtract a b = a -. b
let multiply a b = a *. b
let divide a b = a /. b
let power a b = a ** b

type binop = token * float * float

let compute ((op, a, b) : binop) =
  match op with
  | Add -> add a b
  | Subtract -> subtract a b
  | Multiply -> multiply a b
  | Divide -> divide a b
  | Power -> power a b
;;

let _ =
  let ops =
    [ Add, 3.0, 5.5
    ; Subtract, 10.0, 11.0
    ; Multiply, 5.0, 3.0
    ; Divide, 3.0, 2.0
    ; Power, 3.0, 2.0
    ]
  in
  print_newline ();
  print_endline "Binary operation results:";
  ops |> List.map compute |> List.map string_of_float |> List.iter print_endline
;;
