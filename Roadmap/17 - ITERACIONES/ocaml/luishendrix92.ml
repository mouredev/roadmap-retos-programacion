open Moure.Io

(*****************************************************************************)
(*                                                                           *)
(*                                 Iteration                                 *)
(*                                                                           *)
(*  OCaml offers many ways to iterate through a condition or over a defined  *)
(*  sequence of values (finite or lazily infinite) such a [List], [Array],   *)
(*  or [Seq] ([Sequence] in {b Jane Street's [Core]}).                       *)
(*                                                                           *)
(*  1. Recursion: as a functional language, the most idiomatic way of doing  *)
(*     iteration through a recursive function (preferably TC optimized).     *)
(*  2. Lazy Sequences: [Seq] offers a way to declaratively define finite or  *)
(*     infinite sequences of values that are only evaluated on-demand.       *)
(*  3. Lists and Arrays: Iterating over linked lists is possible through     *)
(*     recursive functions that make use of their head and tail. Whereas     *)
(*     iterating over arrays can be done through Stdlib functions or loops   *)
(*     (imperative) while accessing their values by index.                   *)
(*  4. Imperative Loops: OCaml offers [while] and [for] just like any other  *)
(*     language; it's very useful for running imperative code (IO).          *)
(*                                                                           *)
(*  Other functional languages (and Python) offere something called {e list  *)
(*  comprehensions} which transforms a list or sequence into a new one.      *)
(*  Sadly, OCaml doesn't offer list comprehensions but it can be achieved    *)
(*  with [Seq] and its many transformative functions.                        *)
(*                                                                           *)
(*****************************************************************************)

let recursive_tco a b =
  let rec aux i =
    if i <= b
    then begin
      print_int_endl i;
      aux (i + 1)
    end
  in
  print_endline "Iteration with TCO recursion:";
  aux a
;;

let lazy_seq_iter a b =
  print_endline "Iteration with infinite lazy sequences:";
  Seq.(ints a |> take_while (fun n -> n <= b) |> iter print_int_endl)
;;

let list_iter a b =
  let rec aux = function
    | hd :: tl ->
      print_int_endl hd;
      aux tl
    | [] -> ()
  in
  print_endline "1-10 Count with list iteration (TCO):";
  (* Alternative: [List.iter print_int_endl my_range]. *)
  aux @@ Core.List.range ~stop:`inclusive a b
;;

let array_iter a b =
  let range = Core.List.range ~stop:`inclusive a b |> Array.of_list in
  let i = ref 0 in
  print_endline "1-10 Count with array iteration:";
  (* Alternative 1: [Array.iter print_int_endl range].
     Alternative 2: Get the length of the array and use [for] instead:

     {[
       for i = 0 to Array.length range - 1 do
         print_int_endl range.(i)
       done
     ]}
  *)
  try
    while true do
      print_int_endl range.(!i);
      incr i
    done
  with
  | Invalid_argument _ -> ()
;;

let for_loop_iter a b =
  print_endline "Iteration with a bound for-loop:";
  for i = a to b do
    print_int_endl i
  done
;;

(** [dispenser] is a funny function that I thought of after remembering
    ES6 Javascript generators, which return values by requesting them with
    the [.next()] method and the [yield] keyword.

    While OCaml doesn't offer something directly similar, it can be achieved
    with mutable lazy sequences or lists, or a mutable data structure.
    [dispenser n] returns a runnable function that returns [n+1] every time
    it's called (starting with [n] itself). *)
let dispenser n =
  let i : int ref = ref (n - 1) in
  let dispense () =
    incr i;
    !i
  in
  dispense
;;

(* In recent versions of Ocaml that provide OOP syntax for classes, we can
   achieve the same effect with an object or a class:

   {[
     class countup (start : int) =
       object (self)
         val mutable i = start - 1
         method private inc = i <- i + 1

         method next =
           self#inc;
           i
       end
     ;;

     let counter = new countup 1 in
     for i = 0 to 9 do
       print_int_endl counter#next
     done
   ]}
*)

let _ =
  recursive_tco 1 10;
  print_newline ();
  lazy_seq_iter 1 10;
  print_newline ();
  list_iter 1 10;
  print_newline ();
  array_iter 1 10;
  print_newline ();
  for_loop_iter 1 10;
  print_newline ();
  let dispense = dispenser 1 in
  print_endline "1-10 Count with a closure function:";
  for i = 0 to 9 do
    print_int_endl @@ dispense ()
  done
;;

(* Total: 6 Ways of Iterating from 1 to 10. Could be more, but there is no
   point anyway. I already covered the most important ones. *)
