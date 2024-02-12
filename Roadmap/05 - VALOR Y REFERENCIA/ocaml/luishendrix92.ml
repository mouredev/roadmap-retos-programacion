open Printf;;

(* OCaml is a functional programming language with a few procedural tidbits
   that make it different to purely functional languages such as Haskell. This
   means, we have both immutable and mutable data structures, as well as IO
   blocks that execute system calls (such as reading and writing to channels
   and the filysystem, making network calls, control hardware, and more)
   that in turn return the unit type `()` or a concrete value.

   The language also features something called a [ref] type (reference) that
   acts exactly like a mutable variable that can be replaced anywhere in the
   codebase and. This is not the only way to read and write/mutate memory;
   as I mentioned, there are mutable data structures such as [Hashtbl] and
   [Array], on top of having a rather obscure syntax for creating objects.

   Having said that, as a primarily functional language, most functions and
   operators of the langauge act on immutable data which means that any change
   done to a data structure returns a new data structure leaving the original
   untouched (or garbage-collected if it's no longer needed). Finally, 99% of
   the time we'll be declaring local bindings with immutable values instead of
   mutable references. The language itself doesn't have a way to re-assign a
   [let] binding, but rather, to shadow it, which is just creating a new one
   that holds a new value (often derived from the old one).

   {[
     let foo = 5 in
     let foo = 5.0 in
     print_float foo
   ]}

   The block above will give you a warning because the shadowing of [foo] in
   line 2 does not use the previous value of [foo], giving us the warning:
   [Warning 26 [unused-var]: unused variable foo.]. It won't break the program
   but it gives an insight of the OCaml and functional programing philosophy.
*)

(* Immutable and primitive values. *)

let integer_number = 420 in
let floating_point_number = 69.69 in
let text_string = "Hello Roadmap 2024" in
let boolean_value = false in
let character = 'P' in
begin
  printf
    "Operating on integer_number: %d / 2 = %d\n"
    integer_number
    (integer_number / 2);
  printf
    "Operating on floating_point_number: %f * 3 = %f\n"
    floating_point_number
    (floating_point_number *. 3.0);
  printf
    "Opearting on text_string: uppercase '%s' = '%s'\n"
    text_string
    (String.uppercase_ascii text_string);
  printf
    "Opearting on boolean_value: NOT %b = %b\n"
    boolean_value
    (Bool.not boolean_value);
  printf
    "Opearting on a character: lowercase '%c' = '%c'\n"
    character
    (Char.lowercase_ascii character);
  printf "These operations didn't mutate the original values:\n";
  print_endline (string_of_int integer_number);
  print_endline (string_of_float floating_point_number);
  print_endline text_string;
  print_endline (string_of_bool boolean_value);
  printf "%c\n" character
end

(* Immutable built-in data structures. *)

module IntSet = Set.Make (Int)
module StringMap = Map.Make (String)

let pp_int_list l =
  sprintf "[ %s ]" (List.map string_of_int l |> String.concat "; ")
;;

let pp_int_set s =
  sprintf
    "#{ %s }"
    (IntSet.to_list s |> List.map string_of_int |> String.concat ", ")
;;

let pp_assoc al =
  sprintf
    "{ %s }"
    (List.map (fun (k, v) -> sprintf "\"%s\" => \"%s\"" k v) al
     |> String.concat ", ")
;;

let pp_map m = StringMap.to_list m |> pp_assoc;;

let list_structure = [ 1; 2; 3; 4; 5 ] in
let integer_set = IntSet.of_list [ 9; 8; 7; 9; 8; 3 ] in
let capitals = StringMap.of_list [ "Russia", "Moscow"; "Mexico", "CDMX" ] in
begin
  printf
    "\nCons'ing to a linked list: 0 :: %s = %s\n"
    (pp_int_list list_structure)
    (List.cons 0 list_structure |> pp_int_list);
  printf
    "Removing from a set: remove 8 from %s = %s\n"
    (pp_int_set integer_set)
    (IntSet.remove 8 integer_set |> pp_int_set);
  printf
    "Editing entries in a map: 'CDMX' -> 'Mexico City' in %s = %s\n"
    (pp_map capitals)
    (StringMap.update "Mexico" (fun _ -> Some "Mexico City") capitals |> pp_map);
  print_endline "These operations didn't mutate the original values:";
  print_endline (pp_int_list list_structure);
  print_endline (pp_int_set integer_set);
  prerr_endline (pp_map capitals)
end

(* Mutable data structures

   Note: Even though these structures are mutable, OCaml's standard library
   provides many functions that create a new structure with the changes done.
   The way we recognize the ones that do mutate, is by either checking the
   return type (it must be [unit]) or if their name have the [_inplace] suffix.
*)

let pp_str_arr a = sprintf "[| %s |]" (Array.to_list a |> String.concat "; ")

let pp_hashtbl h =
  Hashtbl.to_seq h
  |> Seq.map (fun (k, v) -> string_of_int k, string_of_int v)
  |> List.of_seq
  |> pp_assoc
;;

let pp_str_queue q =
  sprintf
    "[Front| %s |Back]"
    (Queue.to_seq q |> List.of_seq |> String.concat "->")
;;

let pp_int_stack s =
  sprintf
    "[Top> %s <Bottom]"
    (Stack.to_seq s
     |> Seq.map string_of_int
     |> List.of_seq
     |> String.concat " | ")
;;

let colors_array = [| "Orange"; "Blue"; "Fucshia"; "Black" |] in
let fib_hashtbl = List.to_seq [ 5, 5; 6, 8; 7, 13 ] |> Hashtbl.of_seq in
let str_queue = List.to_seq [ "First"; "Second" ] |> Queue.of_seq in
let int_stack = List.to_seq [ 1; 2; 3; 4 ] |> Stack.of_seq in
begin
  printf
    "\nReplacing colors_array %s at index 1 with 'Red' = "
    (pp_str_arr colors_array);
  print_endline
    (colors_array.(1) <- "Red";
     pp_str_arr colors_array);
  printf "Removing keys 5 and 7 from fib_hashtbl %s = " (pp_hashtbl fib_hashtbl);
  print_endline
    (Hashtbl.remove fib_hashtbl 5;
     Hashtbl.remove fib_hashtbl 7;
     pp_hashtbl fib_hashtbl);
  printf
    "Enqueue 'Third' and dequeue from str_queue %s = "
    (pp_str_queue str_queue);
  print_endline
    (Queue.push "Third" str_queue;
     printf "'%s' out of " (Queue.take str_queue);
     pp_str_queue str_queue);
  printf "Push 5 and 6, then pop from int_stack %s = " (pp_int_stack int_stack);
  print_endline
    (Stack.push 5 int_stack;
     Stack.push 6 int_stack;
     printf "%d out of " (Stack.pop int_stack);
     pp_int_stack int_stack);
  print_endline "These operations mutated the original values:";
  print_endline (pp_str_arr colors_array);
  print_endline (pp_hashtbl fib_hashtbl);
  print_endline (pp_str_queue str_queue);
  print_endline (pp_int_stack int_stack)
end

(* DIFICULTAD EXTRA (opcional):
 * ----------------------------
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 *)

(* NOTE: This exercise doesn't make much sense in a functional language but it
   OCaml provides [ref] types and mutable record fields whose values can be
   swapped and mutated from functions that accept them as parameters. Paremters
   are local bindings that can't be re-assigned but rather shadowed. There is
   no such thing as passing by reference in the language except for passing
   mutable values, yet the bindings keep pointing to these mutated values.
   So, what I'm gonna do instead is create two functions, one which swaps two
   refs (only works if they're the same type), andt the other, swaps the fields
   in a mutable record; both returning the mutable references and assigning
   them to new bindings to later dereference and print their values..
*)

let a : int ref = ref 5
let b : int ref = ref 10

(* printf "\nBefore swapping: a = %d ; b = %d\n" !a !b;; *)

let swap_refs ref_a ref_b =
  let temp = !ref_b in
  ref_b := !ref_a;
  ref_a := temp;
  ref_b, ref_a
;;

begin
  printf "\nOriginal refs: a = %d ; b = %d\n" !a !b;
  let new_a, new_b = swap_refs a b in
  printf
    "After swapping and assigning to new bindings: a = %d ; b = %d ; new_a = \
     %d ; new_b = %d\n"
    !a
    !b
    !new_a
    !new_b;
  incr a;
  incr b;
  incr new_a;
  incr new_b;
  printf
    "After incrementing all references by 1: a = %d ; b = %d ; new_a = %d ; \
     new_b = %d\n"
    !a
    !b
    !new_a
    !new_b
end

type point =
  { mutable x : float
  ; mutable y : float
  }

let pp_point { x; y } = sprintf "P(%f, %f)" x y
let p1 = { x = 7.3; y = -0.39 }

let swap_coords p =
  let temp = p.y in
  p.y <- p.x;
  p.x <- temp;
  p
;;

begin
  printf "\nOriginal point: p1 = %s\n" (pp_point p1);
  let p2 = swap_coords p1 in
  printf
    "After swapping and assigning to new binding: p1 = %s ; p2 = %s\n"
    (pp_point p1)
    (pp_point p2);
  p1.x <- p1.x -. 1.0;
  p1.y <- p1.y -. 1.0;
  p2.x <- p2.x -. 1.0;
  p2.y <- p2.y -. 1.0;
  printf
    "After decrementing all coordinates by 1.0: p1 = %s ; p2 = %s ; \n"
    (pp_point p1)
    (pp_point p2)
end

(* Observations:
   -------------
   As we can see here, references enable the usage of performant procedural
   code in this functional language. And, as it turns out, the [ref] type is
   actually just a record with 1 mutable field [contents], and it's easy to
   re-implement if we learned enough about these subjects:

   {[
     type 'a my_ref = { mutable contents : 'a }

     let my_ref v = { contents = v }
     let ( := ) r v = r.contents <- v
     let ( ! ) r = r.contents
   ]}
*)

(* Output of running [ocaml luishendrix92.ml]:
   -------------------------------------------
   Operating on integer_number: 420 / 2 = 210
   Operating on floating_point_number: 69.690000 * 3 = 209.070000
   Opearting on text_string: uppercase 'Hello Roadmap 2024' = 'HELLO ROADMAP 2024'
   Opearting on boolean_value: NOT false = true
   Opearting on a character: lowercase 'P' = 'p'
   These operations didn't mutate the original values:
   420
   69.690000
   'Hello Roadmap 2024'
   false
   'P'

   Cons'ing to a linked list: 0 :: [ 1; 2; 3; 4; 5 ] = [ 0; 1; 2; 3; 4; 5 ]
   Removing from a set: remove 8 from #{ 3, 7, 8, 9 } = #{ 3, 7, 9 }
   Editing entries in a map: 'CDMX' -> 'Mexico City' in { "Mexico" => "CDMX", "Russia" => "Moscow" } = { "Mexico" => "Mexico City", "Russia" => "Moscow" }
   These operations didn't mutate the original values:
   [ 1; 2; 3; 4; 5 ]
   #{ 3, 7, 8, 9 }

   Replacing colors_array [| Orange; Blue; Fucshia; Black |] at index 1 with 'Red' = [| Orange; Red; Fucshia; Black |]
   Removing keys 5 and 7 from fib_hashtbl { "6" => "8", "7" => "13", "5" => "5" } = { "6" => "8" }
   Enqueue 'Third' and dequeue from str_queue [Front| First->Second |Back] = 'First' out of [Front| Second->Third |Back]
   Push 5 and 6, then pop from int_stack [Top> 4 | 3 | 2 | 1 <Bottom] = 6 out of [Top> 5 | 4 | 3 | 2 | 1 <Bottom]
   These operations mutated the original values:
   [| Orange; Red; Fucshia; Black |]
   { "6" => "8" }
   [Front| Second->Third |Back]
   [Top> 5 | 4 | 3 | 2 | 1 <Bottom]

   Original refs: a = 5 ; b = 10
   After swapping and assigning to new bindings: a = 10 ; b = 5 ; new_a = 5 ; new_b = 10
   After incrementing all references by 1: a = 12 ; b = 7 ; new_a = 7 ; new_b = 12

   Original point: p1 = P(7.300000, -0.390000)
   After swapping and assigning to new binding: p1 = P(-0.390000, 7.300000) ; p2 = P(-0.390000, 7.300000)
   After decrementing all coordinates by 1.0: p1 = P(-2.390000, 5.300000) ; p2 = P(-2.390000, 5.300000) ;
*)
