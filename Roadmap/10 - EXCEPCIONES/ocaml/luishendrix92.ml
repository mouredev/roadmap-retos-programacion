open Printf;;

Random.self_init ()

(*--------------------------------------------------------------------------------------\
  |                                                                                     |
  |                             Error Handling - Exceptions                             |
  |                                                                                     |
  |  When evaluation an expression, OCaml may throw pre-defined exceptions matching     |
  |  the type of failure that happened. Exceptions can also be defined by the user      |
  |  and they may or may not have a value (of any type) attached to it which serves     |
  |  as an information provider for the programmer; to let them know what went wrong.   |
  |    The standard library comes with a small set of exceptions, including a generic   |
  |  one called [Failure] that can be conveniently thrown with [failwith "Message"].    |
  |  The full set includes the following exceptions and how you may encounter them:     |
  |                                                                                     |
  |  - [Failure]: Generic error with great convenience. Carries a [string].             |
  |  - [Invalid_argument]: Used for invariance checking, meaning, prevents the user     |
  |    of an API to pass an invalid argument that may produce an undesired result.      |
  |    Carries a [string], a message to tell the user why the argument is invalid.      |
  |  - [Not_found]: Thrown when an element we're trying to find in a data structure     |
  |    is not present. For example, trying to find an element [elt] in an ['a list].    |
  |  - [Match_failure]: Raised when failing a pattern match in a [match] expression.    |
  |    Provides a thruple with the file, row, and column of where it happened.          |
  |    This also only happens if your [match] expressions are non-exhaustive.           |
  |  - [Sys_error]: Raised during IO operations within the Sys module, such as a        |
  |    file we're trying to read not existing. Provides a [string] with details.        |
  |  - [End_of_file]: This is more of a signal than an error, it tells us when we       |
  |    reached the end of a buffer during an [stdin] read operation.                    |
  |  - [Division_by_zero]: Integer division by zero raises this, but float division by  |
  |    zero will yield [infinity] which is of type [float].                             |
  |  - [Sys_blocked_io]: Raised when a system IO operation is blocked.                  |
  |  - [Assert_failure]: This is one of the most useful ones, it is the foundation of   |
  |    testing libraries. It gives us a thruple containing the file, row, and column    |
  |    where the assertion failure happened. The only way to raise this exception is    |
  |    through the [assert] expression (it's not technically a function), for example:  |
  |    [assert false] will raise the exception, but [assert true] won't.                |
  |  - [Stack_overflow]: Raised when the call-stack is full and the program tries to    |
  |    push another stack frame (function calls). Happens a lot during recursion.       |
  |                                                                                     |
  \-------------------------------------------------------------------------------------*)

let () =
  let sky = "red" in
  try assert (sky = "blue") with
  | Assert_failure (file, line, col) ->
    printf "The sky is not blue, it's %s; but who asked?\n" sky;
    printf "%s did! Where? On line %d and column %d!\n" file line col
;;

let div_by_zero n =
  printf "%d / 0 = " n;
  let division = n / 0 in
  printf "%d\n" division
;;

(* Output: 10 / 0 = Fatal error: exception Division_by_zero. *)
(* let () = div_by_zero 10 *)

(* Output: [1,2,3,4][4] = Fatal error: exception
   Invalid_argument("index out of bounds") *)
(* let () = *)
(*   printf "[1,2,3,4][4] = "; *)
(*   let x = Array.get [| 1; 2; 3; 4 |] 4 in *)
(*   printf "%d\n" x *)
(* ;; *)

(* A cool feature of OCaml is that exceptions can also be pattern-matched. *)
let () =
  match 5 / 0 with
  | 0 -> print_endline "Division by zero? It's just zero :D"
  | exception Division_by_zero ->
    print_endline "We can't divide by zero? Meh..."
  | _ -> print_endline "Doesn't really matter anyway!"
;;

(* The try/with block happens to be an expression, which evaluates to a value.
   Obviously the [unit] or [()] is also a value but means we just executed a
   side-effect. This expression does not come with a [finally] clause but it
   can be achieved by writing some code after the try/with expression.

   There is a pattern in idiomatic OCaml that kept appearing, thus giving birth
   to the function [Fun.protect] in the standard library. This function runs an
   imperative function (that returns a value) and regardless of whether this
   function raised an exception or not, it executes an imperative function
   (that returns [unit]). It's very useful for resource cleanup. *)
let () =
  let open_db_conn () = print_endline "Db is connected, ready for queries..." in
  let close_db_conn () = print_endline "Db is closed, goodbye user..." in
  let query_that_maybe_fails i =
    if Random.int 10 < 5
    then failwith "Db query failed unexpectedly!"
    else printf "Db query #%d result: %d\n" i (Random.int 100)
  in
  try
    open_db_conn ();
    (* Behind the scenes, [~finally] is run before the value is returned or
       an exception that happened is re-raised for the user to handle. *)
    Fun.protect ~finally:close_db_conn (fun () ->
      for i = 1 to 10 do
        query_that_maybe_fails i
      done)
  with
  | Failure msg -> print_endline msg
;;

(*--------------------------------------------------------------------------------------\
  |                                                                                     |
  |                             Dificultad Extra (opcional)                             |
  |                                                                                     |
  |  Crea una función que sea capaz de procesar parámetros, pero que también pueda      |
  |  lanzar 3 tipos diferentes de excepciones (una de ellas tiene que corresponderse    |
  |  con un tipo de excepción creada por nosotros de manera personalizada, y debe ser   |
  |  lanzada de manera manual) en caso de error.                                        |
  |                                                                                     |
  |  - Captura todas las excepciones desde el lugar donde llamas a la función.          |
  |  - Imprime el tipo de error.                                                        |
  |  - Imprime si no se ha producido ningún error.                                      |
  |  - Imprime que la ejecución ha finalizado.                                          |
  |                                                                                     |
  \-------------------------------------------------------------------------------------*)

exception Blacklisted of string

let join_dev_club name age =
  assert (age >= 21);
  let blacklist = [ "Aria Richards"; "Douglas Crockford"; "Terry Davis" ] in
  if name = ""
  then raise (Invalid_argument "Name must not be an empty string.")
  else if List.mem name blacklist
  then raise @@ Blacklisted (name ^ " is blacklisted from our club.")
  else printf "Welcome to the dev club, %s :)\n" name
;;

let try_to_join name age =
  print_endline "--------------------";
  print_endline "Execution started.";
  begin
    try
      (* Alternative version:

         {[
           Fun.protect
             ~finally:(fun () -> print_endline "Execution finalized")
             (fun () ->
               join_dev_club name age;
               print_endline "No exceptions were thrown!")
         ]}
      *)
      join_dev_club name age;
      print_endline "No exceptions were thrown!"
    with
    | Assert_failure _ ->
      print_endline
        "Exception of type [Assert_failure] was thrown because [age] is NOT \
         [>= 21]. Not old enough to join!"
    | Invalid_argument msg ->
      printf
        "Exception of type [Invalid_argument] was thrown with message [%s].\n"
        msg
    | Blacklisted msg ->
      printf
        "Exception of type [Blacklisted] (custom) was thrown with message [%s].\n"
        msg
  end;
  print_endline "Execution finalized."
;;

let () =
  try_to_join "" 35;
  try_to_join "Luis" 18;
  try_to_join "Aria Richards" 43;
  try_to_join "Brais Moure" 38
;;

(* Output of [dune exec reto10]:

   The sky is not blue, it's red; but who asked?
   bin/reto10.ml did! Where? On line 45 and column 6!
   We can't divide by zero? Meh...
   Db is connected, ready for queries...
   Db is closed, goodbye user...
   Db query failed unexpectedly!
   --------------------
   Execution started.
   Exception of type [Invalid_argument] was thrown with message [Name must not be an empty string.].
   Execution finalized.
   --------------------
   Execution started.
   Exception of type [Assert_failure] was thrown because [age] is NOT [>= 21]. Not old enough to join!
   Execution finalized.
   --------------------
   Execution started.
   Exception of type [Blacklisted] (custom) was thrown with message [Aria Richards is blacklisted from our club.].
   Execution finalized.
   --------------------
   Execution started.
   Welcome to the dev club, Brais Moure :)
   No exceptions were thrown!
   Execution finalized.
*)
