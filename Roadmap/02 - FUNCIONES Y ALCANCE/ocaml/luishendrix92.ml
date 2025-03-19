#load "unix.cma"

open Printf

(* There are 5 ways to define functions:
   + Named functions
   + Lambda functions
   + Infix operator functions
   + Fixed recursive functions
   + Pattern matched functions

   The last way is the same as the first but it uses the [function] keyword
   to denote that its last parameter is pattern matched. It's syntax sugar
   for the following definition:

   {[
     let my_function a b c =
       match c with
       | _ -> ()
     ;;
   ]}

   Which can be re-defined as:

   {[
     let my_function a b = function
       | _ -> ()
     ;;
   ]}
*)

(** [is_palindrome s] takes a string [s] and returns [true] if it's a
    {e palindrome} (a word/phrase that reads the same normally and reversed). *)
let is_palindrome s =
  let reversed =
    String.to_seq s |> List.of_seq |> List.rev |> List.to_seq |> String.of_seq
  in
  reversed = s
;;

printf
  "Is 'racecar' a palindrome? %s.\n"
  (if is_palindrome "racecar" then "yes" else "no")

(** [add a b] takes two numberGs [a] and [b] and adds them together. *)
let add = (fun a b -> a + b)
;;

printf "2 + 2 is %d, quick maffs.\n" (add 2 2)

(** [list_length l] counts the number of elements in a list [l]. *)
let list_length l = List.fold_left (fun count _ -> count + 1) 0 l
;;

printf
  "The length of list [false; false; true] is %d.\n"
  (list_length [ false; false; true ])

(** Left-associative mapping operator that applies a function [a] to a list
    [b]. [f >>| l] is equivalent to [List.map f l] under the hood. *)
let ( >>| ) = List.map
;;

let string_of_ints l =
  "[" ^ (List.map string_of_int l |> String.concat ", ") ^ "]"
in
let squares = (fun x -> x * x) >>| [ 1; 2; 3; 4; 5 ] in
printf "Square of numbers from 1 to 5: %s.\n" (string_of_ints squares)

(** [factorial n] computes the factorial of a number [n]. This function
    is {e tail-call optimized}. Returns [1] for any number less than
    or equal to [1]. *)
let factorial n =
  (* In OCaml, recursive functions can be {e tail-call optimized}. This means
     that if the last call inside a function is the function by itself, then
     the current stack frame gets replaced by the new one, thus avoiding
     stack overflows because there is no need to backtrack. *)
  let rec aux acc i = if i > n then acc else aux (acc * i) (i + 1) in
  aux 1 1
;;

printf "The factorial of 5 is %d.\n" (factorial 5)

(** [describe_char c] prints what type of character [c] is. *)
let describe_char = function
  (* Sadly, OCaml's range pattern-matching is {b only available for chars}.
     Though for numbers it can be achieved with [when] clauses. Ex:

     {[
       match n with
       | n when n >= A_INCLUSIVE && n < B_EXCLUSIVE -> ()
       | _ -> ()
     ]}

     Or with else/if statements, but it'd be useful to have [..].
  *)
  | '0' .. '9' -> print_endline "It's a digit."
  | 'a' .. 'z' -> print_endline "It's a lowercase letter."
  | 'A' .. 'Z' -> print_endline "It's an uppercase letter."
  | _ -> print_endline "It's a symbol character :)"
;;

describe_char '5';
describe_char 'y';
describe_char 'H';
describe_char '?'

(* {b Can OCaml return functions from functions?} Yes, but it's usually done
   through two concepts called {e currying} and {e partial application}.
   Calling a function with less parameters than defined creates a function
   that {e closes over} (closure) the ones provided and expects the ones that
   were left out. Currying means that a function defined with n parameters
   will always produce a function of {b arity} (the amount of parameters) 1
   that returns another function of arity 1 and so on until all parameters are
   passed as arguments. The term is a reference to {e Haskell Curry}.

   {b Can OCaml functions accept functions as parameters?} Yes, they're called
   higher-order functions and they're everywhere in the standard library.
   Some libraries have a convetion of having them as named arguments which is
   a topic that I'll demonstrate next.
*)

(** [greet name ~greeter] sets up a roleplay scenario in which a host greets a
    random guest [name] to their party using a greeting function [greeter]. *)
let greet name ~greeter =
  print_endline (name ^ " enters the party house...");
  print_endline ("And the host says to " ^ name ^ ":");
  greeter name;
  print_endline (name ^ " can finally enjoy the party.")
;;

(** [greet_rudely name] rudely greets [name] to ther party. This function was
    created using partial application on [greet], providing a greeter function
    and returning another function that only expects a string [name]. *)
let greet_rudely =
  greet ~greeter:(fun name ->
    printf "Who invited you, %s? Anyway, have a seat...\n" name)
;;

greet_rudely "luishendrix92"

(* Named arguments are a great way to produce readable code and APIs for users.
   For example, the most promiment external library, [Core] (by {e Jane Street
   Capital}) aims to serve as a replacement for the standard library and it
   achieves so not only by optimizing and extending modules, but also by
   providing labeled arguments to better guide the user.

   Another good feature of the language is the definition of optional
   paramenters which can also hold a default value. When there is no default
   value, the parameter becomes of [option 'a] type where ['a] is the type
   of the parameter you are expecting.
*)

(** [range ?a ?inclusive b] returns a range as a list of integers from [a]
    (inclusive) to [b] (exclusive by default, can be set to [false]). Raises
    [Invalid_argument] if [a] is greater than [b]; returns [[]] if equal. *)
let range ?(a = 0) ?(inclusive = false) b =
  List.init (b - a + Bool.to_int inclusive) (fun i -> i + a)
;;

range 6 ~inclusive:true ~a:3
|> List.map string_of_int
|> List.iter print_endline

(** [no_default_test] is a demo function for optional parameters with no
    default value. Simulates a login form to an Operating System. If
    [username] is not provided, it becomes [None], otherwise the value is
    wrapped in [Some]. *)
let no_default_test ?username os =
  match username with
  | Some name -> printf "Welcome to %s, '%s'!\n" os name
  | None -> printf "Login to %s requires a username!\n" os
;;

no_default_test ~username:"luishendrix92" "Ubuntu 24";
no_default_test "Windows 12"
;;

(* OCaml's default [opam] (package manager) {e switch} comes with a standard
   library and some packages maintained by the community. If you want to
   check out the different modules and their functions go to this link:

   https://v2.ocaml.org/api/index.html

   I will use a function of each module (only the most used) but I recommend
   checking the documentation and testing the functions in [utop] by yourself.
*)

printf
  "The sum of [ 1; 2; 3; 4; 5 ] is %d.\n"
  (List.fold_left ( + ) 0 [ 1; 2; 3; 4; 5 ]);
printf "FOX lowercased is %s.\n" (String.lowercase_ascii "FOX");
printf "The ASCII code of '?' is %d.\n" (Char.code '?');
printf
  "Array length of [| 'A'; 'B'; 'C' |] is %d.\n"
  (Array.length [| 'A'; 'B'; 'C' |]);
printf "The hypotenuse of a=5 and b=3 is %f.\n" (Float.hypot 4.0 3.0);
let is_adult age = age >= 18 in
printf
  "In an alternate universe, a 25 year old %s an adult!\n"
  (if (Fun.negate is_adult) 25 then "is" else "is not");
printf
  "What comes after -5? %d | What's before 7? %d.\n"
  (Int.succ (-5))
  (Int.pred 7);
printf
  "Extracting a value from an option: [ None -> %s | Some 42 -> %d ]\n"
  (Option.value ~default:"DEFAULT_VALUE" None)
  (Option.value ~default:0 (Some 42));
Unix.system "pwd"

(* There are no global variables in OCaml, they are all local bindings, just
   like [let] in JavaScript (ES6+). If I were to bind a value at the outermost
   layer of the file then I guess you can consider it global since it will be
   available everywhere in the file but you can't, for example, use the value
   of a binding that's inside another binding. {b Shadowing} gives you the
   illusion that you can "re-assign" a binding, but in reality you're just
   creating another one with the same name that overrides the previous one. *)

let i_guess_im_global = "But there is no such thing...";;

let _ = () in
let _ =
  let foo = "foo" in
  (* Shadowing: uses the previous value and re-binds it. *)
  let foo = foo ^ "bar" in
  foo ^ "baz" (* "foobarbaz" *)
in
let _ = () in
(* Begin/End blocks are syntactic sugar for parenthesis. *)
begin
  print_endline "This call is 3 levels deep and it can access outer bindings:";
  printf "Globals? %s.\n" i_guess_im_global
end

(* Optional Challenge *)

(** [generic_fizz_buzz ?fizz ?buzz n] prints the numbers from [1] to [n] ([100])
    but replaces the multiples of [3] with [fizz] and the multiples of [5] with
    [buzz] (multiples of both with [fizz ^ buzz]). It acts as a generic
    imperative version of the {b fizz-buzz algorithm} in which the user can set
    their own strings to replace "Fizz" and "Buzz". Returns the number of times
    a number was printed without being replaced by [fizz] and/or [buzz]. *)
let generic_fizz_buzz ?(fizz = "Fizz") ?(buzz = "Buzz") n =
  let num_count : int ref = ref 0 in
  for i = 1 to n do
    match i mod 3, i mod 5 with
    | 0, 0 -> print_endline (fizz ^ buzz)
    | 0, _ -> print_endline fizz
    | _, 0 -> print_endline buzz
    | _ ->
      print_endline (string_of_int i);
      incr num_count
  done;
  !num_count
;;

(* Returns 53 *)
generic_fizz_buzz ~fizz:"Electa" 100

(* Output after running [ocaml -I +unix luishendrix92.ml]
   ------------------------------------------------------
   Is 'racecar' a palindrome? yes.
   2 + 2 is 4, quick maffs.
   The length of list [false; false; true] is 3.
   Square of numbers from 1 to 5: [1, 4, 9, 16, 25].
   The factorial of 5 is 120.
   It's a digit.
   It's a lowercase letter.
   It's an uppercase letter.
   It's a symbol character :)
   luishendrix92 enters the party house...
   And the host says to luishendrix92:
   Who invited you, luishendrix92? Anyway, have a seat...
   luishendrix92 can finally enjoy the party.
   3
   4
   5
   6
   Welcome to Ubuntu 24, 'luishendrix92'!
   Login to Windows 12 requires a username!
   The sum of [ 1; 2; 3; 4; 5 ] is 15.
   FOX lowercased is fox.
   The ASCII code of '?' is 63.
   Array length of [| 'A'; 'B'; 'C' |] is 3.
   The hypotenuse of a=5 and b=3 is 5.000000.
   In an alternate universe, a 25 year old is not an adult!
   What comes after -5? -4 | What's before 7? 6.
   Extracting a value from an option: [ None -> DEFAULT_VALUE | Some 42 -> 42 ]
   /home/kozmicluis/Documents/moure/Roadmap/02 - FUNCIONES Y ALCANCE/ocaml
   This call is 3 levels deep and it can access outer bindings:
   Globals? But there is no such thing...
   1
   2
   Electa
   4
   Buzz
   Electa
   7
   8
   Electa
   Buzz
   11
   Electa
   13
   14
   ElectaBuzz
   16
   17
   Electa
   19
   Buzz
   Electa
   22
   23
   Electa
   Buzz
   26
   Electa
   28
   29
   ElectaBuzz
   31
   32
   Electa
   34
   Buzz
   Electa
   37
   38
   Electa
   Buzz
   41
   Electa
   43
   44
   ElectaBuzz
   46
   47
   Electa
   49
   Buzz
   Electa
   52
   53
   Electa
   Buzz
   56
   Electa
   58
   59
   ElectaBuzz
   61
   62
   Electa
   64
   Buzz
   Electa
   67
   68
   Electa
   Buzz
   71
   Electa
   73
   74
   ElectaBuzz
   76
   77
   Electa
   79
   Buzz
   Electa
   82
   83
   Electa
   Buzz
   86
   Electa
   88
   89
   ElectaBuzz
   91
   92
   Electa
   94
   Buzz
   Electa
   97
   98
   Electa
   Buzz
*)