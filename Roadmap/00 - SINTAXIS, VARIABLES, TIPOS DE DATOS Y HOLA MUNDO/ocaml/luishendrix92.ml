(******************************************************************************
 * OCaml | An industrial-strength functional programming                      *
 *       | language with an emphasis on expressiveness and safety.            *
 * -------------------------------------------------------------------------- *
 * Official Website: https://ocaml.org/                                       *
 *****************************************************************************)

(* Single line comment *)
(* Multi
   Line
   Comment *)

(* Top level let binding, can be re-assigned but not written. *)
let my_name = "luishendrix92"

(* Local bindings that are visible in their current scope
   and anything that is within it, but not to the outside *)
let my_function =
  let x = 5 in
  let y = x + 10 in
  if x + y = 20
  then x * y
  else (
    let z = x - y in
    z / 10)
;;

(* References: These are mutable variables but limited to the type you
   express at compile type. They can be re-assigned with [:=] and
   de-referenced with [!] which reads the value contained in it. *)
let counter : int ref = ref 0;;

(* Replaces 0 with 10 *)
counter := 10;
(* Replaces 0 with 11 *)
counter := !counter + 1;
(* Prints "11" *)
print_int !counter

(* Primitive data types
   -------------------- *)

let str = "Here is a string\nJust like any other language."
let ch = 'A'
let integer = 10 + 3 + int_of_float 3.14
let floating = 0.5 +. 5. -. float_of_int 1
let answer = (true && false) || true
let unit = ()

(* Built-in container data types
   ----------------------------- *)

(* A tuple of two ints. Tuples can have more than 2 elements. *)
let point = 4, 7;;

match point with
| x, y -> Printf.printf "\nP(%d, %d)" x y

(* Immutable singly-linked lists. *)
let my_list = true :: [ true; false; false; true; true ]

(* Mutable index-based arrays. *)
let my_array = [| 'A', 'B', 'C', 'D' |]

(* Ocaml has built-in support for optional types. It also has Result, and
   many others but you'll find yourself using this one more. *)
let option =
  match Some 42 with
  | Some x -> "The answer to everything is " ^ string_of_int x
  | None -> "There is no answer to anything..."
;;

(* Building custom exceptions and handling them is simple. *)
let ex =
  try raise (Failure "Something went wrong") with
  | Failure _ -> print_endline "\nBoom!"
;;

(* Functions are first-class citizens, as expected of a functional language. *)
let list_product = List.fold_left (fun acc x -> acc * x) 1
let add a b = a + b
let apply_twice f v = f v |> f

(* Records, Variants, Polymorphic Variants, and Modules
   These can be thought of as user-defined types!
   ---------------------------------------------------- *)

module R3Vector : sig
  type t

  val of_tuple : float * float * float -> t
  val dot_product : t -> t -> float
end = struct
  (* Records can have mutable fields by marking them with the [mutable]
     keyword before its name. Assignment is done with the [<-] operator
     and dereferencing is the same as with immutable fields using the
     [rec.field] dot syntax. For more information, refer to:
     https://cs3110.github.io/textbook/chapters/mut/mutable_fields.html *)
  type t =
    { i : float
    ; j : float
    ; k : float
    }

  let of_tuple (i, j, k) = { i; j; k }
  let dot_product a b = (a.i *. b.i) +. (a.j *. b.j) +. (a.k *. b.k)
end

let result =
  let open R3Vector in
  let v1 = of_tuple (1.5, 0.2, 2.1) in
  let v2 = of_tuple (0., 1., 3.8) in
  dot_product v1 v2
;;

(* Nullary variant type, no type parameters *)
type shape =
  | Rectangle of (float * float)
  | Circle of float

let area s =
  match s with
  | Rectangle (a, b) -> a *. b
  | Circle radius -> Float.pi *. radius *. radius
;;

(* Polymorphic variant type, analogous to generics in OOP *)
type 'a maybe =
  | Just of 'a
  | Nothing

let maybe_a_string = Just "do it"
let maybe_an_int = Nothing
let maybe_a_maybe = Just (Just 9999)

(* According to the official documentation, OCaml has objects and classes but
   I have never seen it used. I don't doubt people use it but it may be a rare
   sight. Since I don't know how it's done I'll just copy and paste the
   example from the doc site: https://ocaml.org/docs/objects. *)
class ['a] stack =
  object (self)
    val mutable list : 'a list = [] (* instance variable *)

    method push x = (* push method *)
                    list <- x :: list

    method pop =
      (* pop method *)
      let result = List.hd list in
      list <- List.tl list;
      result

    method peek = (* peek method *)
                  List.hd list

    method size = (* size method *)
                  List.length list
  end

let s = new stack;;

s#push 1.0 (* Method call *)

(* Printing Hello World
   -------------------- *)
let () = print_endline "Hello World from OCaml"

(** ODoc's documentation code block. At the very top level, this comment will
    document the entire module which corresponds to this [.ml] file.
    These comments allow special syntax which can be found at ODoc's official
    website https://ocaml.github.io/odoc/odoc_for_authors.html. Here are some
    examples of the things that can be expressed:

    Syntax for {b bold}, {i italic}, {e emphasis}, {^ super}, {_ under}.

    - there are
    - unoredered
    - lists

    + and of course
    + ordered
    + lists

    Code blocks for any language, useful to demo your functions:
    {[let sum_list = List.fold_left ( + ) 0

      sum_list [5; 3; -8; 4] = 4]}

    @author luishendrix92
    @since 1.5

    NOTE: This comment was attached to a dummy variable so you can read it
    using your IDE's autocomplete or LSP hover functionality. *)
let read_me = () (* Unit type *)
