type person =
  { age : int
  ; name : string
  }

(* In OCaml, operators are functions (unary, and binary) that can be passed
   around and returned from other functions just like any other. Also, we
   can define our own infix operator (binary operators that stand in
   between two arguments) as long as they don't collide with existing ones. *)

let bar_bouncer person =
  let blacklist = [ "Bob Smith"; "Jane Doe"; "Spongebob" ] in
  (* OCaml's logical operators [|||] and [&&] work as expected.
     Same as the built-in comparisons [>=], [<=], etc. *)
  person.age >= 18 && not (List.mem person.name blacklist)
;;

(* Example of the pipe operator [|>], which applies argument A to (potentially
   partialy-applied) a function B. It can be chained to assemble a pipeline. *)
print_endline "Welcome to Sr.Frog's Bar!";
[ { name = "Luis Lopez"; age = 31 }
; { name = "Spongebob"; age = 25 }
; { name = "Jane Doe"; age = 60 }
; { name = "Homer Simpson"; age = 56 }
]
|> List.filter bar_bouncer
|> List.iter (fun person ->
  Printf.printf "- %s of age %d\n" person.name person.age)

(* Operators can be used as curried functions for simplicity. *)
let sum_list nums = List.fold_left ( + ) 0 nums
let list_product nums = List.fold_left ( * ) 1 nums;;

(* The [=] operator can act as assignment and equality comparison which is
   confusing to beginners, but you get used to it with time. Also, in
   OCaml, the [if/else] {b control flow structure} is an expression and
   the [elseif] construct doesn't exist but it looks like it does due to
   associativity working in our favour. This means the following:

   {[
     if COND1 then BRANCH1 else if COND2 then BRANCH2 else BRANCH3
   ]}

   and this next one with parenthesis:

   {[
     if COND1 then BRANCH1 else (if COND2 then BRANCH2 else BRANCH3)
   ]}

   are both equivalent expressions, interesting isn't it? *)
let sky = "green" in
if sky = "blue"
then print_endline "\nThe sky is clear and blue today :)"
else if sky = "dark"
then print_endline "\nIt's night time :O"
else print_endline "\nThe sky has an unknown color!"

(* Another interesting tidbit of OCaml is that there are separate operators
   for integers and floating point numbers. For [int], we have the usual
   [+], [-], [/], and [*] but they only work if both their arguments are of
   type [int]. For [float] we have [+.], [-.], [/.], and [*.] which is just
   the same operators with a dot at the end. Don't forget that floating point
   numbers must also have a dot after them even if they don't have decimals. *)
let int_arithmetics = 45 + (15 * 10) - int_of_float 0.5
let float_arithmetics = (12. -. float_of_int 42 +. 99.99) /. -23.33;;

(* String concatenation is possible, but the operator is a bit uncommon. *)
let book = "At " ^ "the mountains" ^ " of madness" in
Printf.printf "%s is a cosmic horror story.\n" book

(* OCaml also has bitwise operators, mod (modulo), and more! *)
let bitwise = 12 land 45 lor 0 lxor (lnot 1 lsl 20 lsr 3)
let list_append = 5 :: [ 4; 3; 2; 1; 0 ]
let list concat = [ 'A'; 'B'; 'C' ] @ [ 'D'; 'E'; 'F' ]

(* [<>] and [!=] are similar except for the way they check for equality. *)
let is_odd n = n mod 2 <> 0
let is_pair n = n mod 2 = 0

(* Despite being a functional langauge, OCaml has a for loop construct
   as procedural alternative for recursion. This is an iterative control
   structure that has been simplified to work with a range of integers
   specified in the form of [A to B] where B is inclusive. Note that this
   block expression returns a unit [()] type so it must be followed with a
   [;] if the intention is to return something else. *)
let array_max arr =
  let len = Array.length arr in
  (* [match PATTERN with] is a powerful pattern-matching control structure
     featured in many functional languages such as Elixir and Kotlin.
     Not only does it allow to match against destructured containers and
     primitive values; it also binds variables to use in each branch. *)
  match len with
  | 0 -> raise (Failure "array_max: Array is empty")
  | 1 -> arr.(0)
  | _ ->
    let max_value : 'a ref = ref arr.(0) in
    for i = 1 to len - 1 do
      if arr.(i) > !max_value then max_value := arr.(i)
    done;
    !max_value
;;

let arr = [| 5; 0; -99; 12; 3 |] in
Printf.printf "Maximum value of 'arr' is %d\n" (array_max arr)

type action =
  | Introduce of person
  | Compare of person * person
  | BarrelRoll

(* Pattern matching can also be used for the last function parameter. *)
let dispatcher = function
  | Introduce { name; age } ->
    Printf.printf "Hi, I'm %s, %d years old.\n" name age
  | Compare (a, b) ->
    let status =
      if a.age = b.age
      then "the same age as"
      else if a.age > b.age
      then "older than"
      else "younger than"
    in
    Printf.printf "%s is %s %s.\n" a.name status b.name
  | BarrelRoll -> print_endline "Do a barrel roll *rolls around*"
;;

dispatcher (Introduce { name = "John Doe"; age = 48 });
(* Surprisingly, while loops are also available. *)
Random.self_init ();
let trapped_in_simulation : bool ref = ref true in
while !trapped_in_simulation do
  print_endline "I'm trapped in a simulation :(";
  trapped_in_simulation := Random.bool ()
done;
print_endline "I escaped from a simulation :)"

(* Exceptions in OCaml are encouraged when there is no way to recover from an
   error, usually produced by external forces such as an user doing something
   incorrectly, a failed network or system call, etc. Sometimes they are also
   useful for handling failure in imperative code and then transform the
   {b failure} into a [None] optional type, or the {b success} into a [Some];
   though [Result] also exists, mostly used in network calls. *)
let count_file_lines filename =
  let lines =
    try In_channel.open_bin filename |> In_channel.input_lines with
    | Sys_error _ -> []
  in
  List.length lines |> Printf.printf "'%s' | %d lines were read.\n" filename
;;

count_file_lines "non_existant_file.txt";
count_file_lines "luishendrix92.ml"

(** [extra_challenge] is a function that prints all pair numbers within a
    range of [a] to [b] (inclusive) excluding [16] and mutliples of [3]. *)
let extra_challenge a b =
  let is_good_number n = is_pair n && n mod 3 <> 0 && n <> 16 in
  for n = a to b do
    if is_good_number n then print_endline (string_of_int n)
  done;
  (* It can also be written in a functional style with lazy sequences. *)
  Seq.ints a
  |> Seq.take (b - a + 1)
  |> Seq.filter is_good_number
  |> Seq.map string_of_int
  |> Seq.iter print_endline
;;

extra_challenge 10 55

(* Running the script produces the following output:

   {@plain[
     Welcome to Sr.Frog's Bar!
     - Luis Lopez of age 31
     - Homer Simpson of age 56

     The sky has an unknown color!
     At the mountains of madness is a cosmic horror story.
     Maximum value of 'arr' is 12
     Hi, I'm John Doe, 48 years old.
     I'm trapped in a simulation :(
     I'm trapped in a simulation :(
     I'm trapped in a simulation :(
     I'm trapped in a simulation :(
     I escaped from a simulation :)
     'non_existant_file.txt' | 0 lines were read.
     'luishendrix92.ml' | 226 lines were read.
     10
     14
     20
     22
     26
     28
     32
     34
     38
     40
     44
     46
     50
     52
     10
     14
     20
     22
     26
     28
     32
     34
     38
     40
     44
     46
     50
     52
   ]}

   If you have OCaml installed on your machine, try running this
   script file with [ocaml luishendrix92.ml] or using {b [utop]}
   which will give you aceess to its defined functions and types:

   {[
     #use "luishendrix92.ml";;
   ]}
*)
