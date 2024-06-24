open Printf

(******************************************************************************)
(*                                                                            *)
(*                                 Decorators                                 *)
(*                                                                            *)
(*  A {b decorator} is, in essence, a function that wraps another function    *)
(*  in order to grant it additional behaviour without modifying the original  *)
(*  code, oftentimes even preserving the function's signature where the only  *)
(*  noticeable change is a side-effect that doesn't alter the return type.    *)
(*  The most popular language that uses this technique is Python, which has   *)
(*  dedicated syntax for decorators ({[ @decorator_name(arguments...) ]}),    *)
(*  however, this pattern can be applied by any language that can return      *)
(*  functions (Higher Order Functions).                                       *)
(*                                                                            *)
(*  In OCaml this is easy to achieve, and there are already some functions    *)
(*  in the standard library that can be considered "decorators", one example  *)
(*  is [Fun.protect] which accepts a (potentially failing) function and a     *)
(*  function that frees the used resources in case the function fails.        *)
(*                                                                            *)
(*  Another potential use case of decorators is to introduce new code into    *)
(*  the project based on existing code that has been "annotated" with         *)
(*  decorators. Java annotations are a good example of this practise and we   *)
(*  can achieve a similar behaviour using custom pre-processors (PPX). It is  *)
(*  fairly complex but a simple demonstration wouldn't hurt.                  *)
(*                                                                            *)
(******************************************************************************)

module Decorators : sig
  val tap : f:('a -> unit) -> ('a -> 'b) -> 'a -> 'b
  (** [tap ~f g x] runs the consumer function [f] with [x] as argument
      before returning whatever it is that [g x] returned. *)

  val timed : (unit -> 'a) -> 'a
  (** [timed f] measures the execution time of [f ()] and prints it to the
      console (in seconds) while also returning the value it produced. *)

  val counted : ('a -> 'b) -> 'a -> 'b
  (** [counted f x] returns the result of invoking [f] with argument [x] after
      printing the amount of times it's been invoked with any argument.

      {b NOTE}: In order for this to work, you need to partially apply
      [counted] with a function [f] and then keep running the same partially
      applied function; otherwise the closure counter will be lost. *)
end = struct
  let tap ~f g x =
    f x;
    g x
  ;;

  let timed f =
    let start_time = Sys.time () in
    let result = f () in
    let end_time = Sys.time () in
    printf "Execution time in seconds: %f\n" @@ (end_time -. start_time);
    result
  ;;

  let counted f =
    let i : int ref = ref 0 in
    fun x ->
      incr i;
      printf "Function has been invoked [%d] times!\n" !i;
      f x
  ;;
end

let rec fib = function
  | 0 -> 0
  | 1 -> 1
  | n -> fib (n - 1) + fib (n - 2)
;;

let _ =
  let open Decorators in
  print_endline "Decorator [tap] example:";
  [ 1; 2; 3; 4; 5 ]
  |> List.map (tap ~f:(printf "[succ] input: %d\n") succ)
  |> List.iter (printf "After increment: %d\n");
  print_endline "Decorator [timed] example (performance measure):";
  printf "fib n=45 is equal to: %d\n" @@ timed (fun () -> fib 45);
  print_endline "Decorator [counted] example:";
  (******************************************************************)
  (*                                                                *)
  (*                   Dificultad Extra (Opcional)                  *)
  (*                                                                *)
  (*  Crear un decorador que sea acpaz de contabilizar cuántas      *)
  (*  veces se ha llamado a una función y aplícalo a una función    *)
  (*  de tu elección.                                               *)
  (*                                                                *)
  (******************************************************************)
  let run_me () = print_endline "I keep running" in
  let run_me = counted run_me in
  for i = 1 to 5 do
    run_me ()
  done
;;

(* Output:
   -------
   Decorator [tap] example:
   [succ] input: 1
   [succ] input: 2
   [succ] input: 3
   [succ] input: 4
   [succ] input: 5
   After increment: 2
   After increment: 3
   After increment: 4
   After increment: 5
   After increment: 6
   Decorator [timed] example (performance measure):
   Execution time in seconds: 8.358457
   fib n=45 is equal to: 1134903170
   Decorator [counted] example:
   Function has been invoked [1] times!
   I keep running
   Function has been invoked [2] times!
   I keep running
   Function has been invoked [3] times!
   I keep running
   Function has been invoked [4] times!
   I keep running
   Function has been invoked [5] times!
   I keep running
*)
