open Printf

(*****************************************************************************)
(*                                                                           *)
(*                            Set Data Structure                             *)
(*                                                                           *)
(*  Sets are a {e finite collection} of {b unique} data with roots in        *)
(*  mathematics. The way sets are implemented allow for logarithmic-time     *)
(*  access at the cost of slower write times than an array. Sets don't       *)
(*  guarantee element order and they can't be repeated, they must be unique  *)
(*  and depending on the language, of same type (mostly).                    *)
(*    OCaml doesn't let you have sets of different types and the standard    *)
(*  library implements them as functors, meaning, you need to pass a module  *)
(*  to the [Set.Make] functor in order to get back a new module that is      *)
(*  bound to the type that the passed module represent. Among the most       *)
(*  popular modules to pass are [String], [Float], [Int], and [Char].        *)
(*                                                                           *)
(*  Set operations are:                                                      *)
(*  - Union (A ∪ B): A set composed of all the elements from sets A and B.   *)
(*  - Intersection (A ∩ B): Elements of A and B that appear on both sets.    *)
(*  - Symmetric difference (A Δ B): All the elements of A and B that don't   *)
(*  appear on both at the same time. Ex: {1,2,3} Δ {4,2,6} = {1,3,4,6}.      *)
(*  - Difference (A - B): The elements of A without the ones that also       *)
(*  appear on B; basically, subtration. Ex: {9,1,4,7} - {1,7,5,2} = {9,4}.   *)
(*                                                                           *)
(*****************************************************************************)

module IntSet = Set.Make (Int)

let show_int_set s =
  if IntSet.is_empty s
  then "∅"
  else
    IntSet.to_list s
    |> List.map string_of_int
    |> String.concat ", "
    |> sprintf "{ %s }"
;;

let tap str set =
  printf str (show_int_set set);
  set
;;

(** [symm_diff a b] is the symmetric difference between set [a] and set [b].
    A symmetric difference can be described as the difference between the
    union of [a] and [b], and their intersection. *)
let symm_diff a b = IntSet.diff (IntSet.union a b) (IntSet.inter a b)

let _ =
  let b_set = IntSet.of_list [ 5; 10; 6; 0 ] in
  let a_set =
    IntSet.empty
    |> tap "Empty set: %s\n"
    |> IntSet.add 8
    |> tap "After adding 1 element: %s\n"
    |> IntSet.add_seq (List.to_seq [ 1; 5; 10 ])
    (* NOTE: Adding elements to a certain position is irrelevant in an OCaml set
       as they can't guarantee insertion order since the elements get sorted. *)
    |> tap "After adding multiple elements: %s\n"
    |> IntSet.remove 8
    |> tap "After removing the number 8: %s\n"
  in
  printf
    "Union: A (%s) ∪ B (%s) = %s\n"
    (show_int_set a_set)
    (show_int_set b_set)
    (IntSet.union a_set b_set |> show_int_set);
  printf
    "Intersection: A (%s) ∩ B (%s) = %s\n"
    (show_int_set a_set)
    (show_int_set b_set)
    (IntSet.inter a_set b_set |> show_int_set);
  printf
    "Difference: B (%s) - A (%s) = %s\n"
    (show_int_set b_set)
    (show_int_set a_set)
    (IntSet.diff b_set a_set |> show_int_set);
  printf
    "Symmetric Difference: B (%s) Δ A (%s) = %s\n"
    (show_int_set a_set)
    (show_int_set b_set)
    (symm_diff a_set b_set |> show_int_set);
  printf
    "Is 0 an element of set B = %s? %b\n"
    (show_int_set b_set)
    (IntSet.mem 0 b_set);
  printf "Cardinality (elt. count) of set A: %d\n" (IntSet.cardinal a_set)
;;

(* Output of [dune exec reto18]

   Empty set: ∅
   After adding 1 element: { 8 }
   After adding multiple elements: { 1, 5, 8, 10 }
   After removing the number 8: { 1, 5, 10 }
   Union: A ({ 1, 5, 10 }) ∪ B ({ 0, 5, 6, 10 }) = { 0, 1, 5, 6, 10 }
   Intersection: A ({ 1, 5, 10 }) ∩ B ({ 0, 5, 6, 10 }) = { 5, 10 }
   Difference: B ({ 0, 5, 6, 10 }) - A ({ 1, 5, 10 }) = { 0, 6 }
   Symmetric Difference: B ({ 1, 5, 10 }) Δ A ({ 0, 5, 6, 10 }) = { 0, 1, 6 }
   Is 0 an element of set B = { 0, 5, 6, 10 }? true
   Cardinality (elt. count) of set A: 3
*)

(*****************************************************************************)
(*                                                                           *)
(*                         Implementation and Ordering                       *)
(*                                                                           *)
(* Sets can be implemented in 2 ways: with a tree-like data structure and    *)
(* using a hash table. A binary properly balanced binary tree can give us    *)
(* logarithmic access times and the traversal is done in orderly manner. In  *)
(* OCaml's standard lib, [Set] is implemented with a binary tree and that's  *)
(* why the module we pass to the functor must have a comparator function     *)
(* called [compare]. If we were to implement a set that remembers insertion  *)
(* order we could add both to a linked list and a b-tree or hash bucket.     *)
(*   It's worth noting that if we wanted a data structure to add stuff to    *)
(* either end (front/rear) or at a specific position then maybe we're better *)
(* off with an array or a linked list which can be converted to a set at a   *)
(* later time anyway (getting rid of duplicates).                            *)
(*                                                                           *)
(*****************************************************************************)
