open Printf

(* OCaml offers {b 6} main data structures (the rest are containers that serve
   a particular task, such as [option]) that can be used to create even more
   data structures, along with ADTs ({e algebraic data types}) which are
   heavily useful in creating mutually recursive structures such as trees.

   + List (singly-linked list)
   + Tuple (2 or more elements)
   + Array (mutable array type)
   + Map (strongly-typed immutable key-value pair)
   + Hashtbl (weakly-typed mutable hashmaps)
   + Set (immutable typed set of unique items)
   + Lazy Seq (lazy sequences, similar to streams)
*)

(** [remove_idx i l] removes the element at index [i] from list [l]. If [i]
    is not part of [l], the list doesn't change. *)
let remove_idx i l = List.filteri (fun idx _ -> idx <> i) l

(** [replace_idx i l e] replaces the element at index [i] from list [l] with a
    provided element [e]. If [i] is not in [l], the list doesn't change. *)
let replace_idx i l e = List.mapi (fun idx elt -> if idx = i then e else elt) l
;;

let my_list = [ 50; -4; 60; 0; 12; 1 ] in
let my_list = 40 :: my_list in
let my_list = List.cons 30 my_list in
let my_list = List.append my_list [ 2; 3 ] in
let my_list = my_list @ [ 4; 5 ] in
let my_list = remove_idx 4 my_list in
let my_list = replace_idx 0 my_list 100 in
let my_list = List.sort Int.compare my_list in
List.iter (fun n -> printf "my_list: %d.\n" n) my_list

(* Tuples can't be sorted and they don't need to, their sole purpose is to
   represent a finite-length ([2] or [3]) set of elements where their position
   matters (for example, in a coordinate). They can be easily pattern-matched.
   In functional programming languages, Tuples are also functors that can be
   mapped, which means, change the contents of the {e nth} element or all.
   Tuples are also not meant to have their elements deleted.
*)

module Core = struct
  module Tuple3 = struct
    let map ~f t3 =
      match t3 with
      | a, b, c -> f a, f b, f c
    ;;
  end
end
;;

let my_r3_vector = 4.5, 2.0, 1.8 in
let my_r3_vector = Core.Tuple3.map my_r3_vector ~f:Float.ceil in
match my_r3_vector with
| x, y, z -> printf "my_r3_vector: (%f, %f, %f).\n" x y z
;;

(* Arrays are mutable, sequential blocks of information. Updating elements
   is constant time compared to linked lists, same as accessing by index.
   The tradeoff is that removing elements is expensive due to element
   shifting. Replacing an element at index [n] returns [unit].
*)

let my_arr = [| 5; 4; 3; 2; 1 |] in
let my_arr = Array.append my_arr [| 0 |] in
let my_arr = Array.append (Array.sub my_arr 1 2) (Array.sub my_arr 3 2) in
my_arr.(0) <- 10;
Array.sort Int.compare my_arr;
Array.iter (fun n -> printf "my_arr: %d.\n" n)

(* Maps are associations between a key and a value, the key's type must be
   provided to a functor module first in order to make your own [Map].
   According to the documentation, this module is implemented with a
   balanced binary tree which greatly improves search and insertion
   performance (instead of [O(n)] it's now [O(log n)]).
*)

module Stock = Map.Make (String);;

let my_stock = Stock.empty in
let my_stock = Stock.add "AAPL" 182.68 my_stock in
let my_stock = Stock.add "NFLX" 480.33 my_stock in
let my_stock = Stock.add "AMZN" 150.71 my_stock in
let my_stock = Stock.remove "AAPL" my_stock in
let my_stock = Stock.update "NFLX" (Option.map Float.floor) my_stock in
Stock.iter (fun k v -> printf "Stock %s -> %f" k v) my_stock
;;

(* Hash Tables are imperative (mutable) and are extremely useful for dynamic
   programming algorithms that require some sort of cache. It's also used
   in lookups, databases, and they provide constant time search. But
   collisions can happen and they are as good as the hashing function.
*)

let my_hash = Hashtbl.create 10 in
begin
  Hashtbl.add my_hash 1.5 "One point five";
  Hashtbl.add my_hash 5.0 "Five point zero";
  Hashtbl.remove my_hash 1.5;
  Hashtbl.replace my_hash 5.0 "Five point'o";
  Hashtbl.iter (fun k v -> printf "my_hash: %f=%s.\n" k v) my_hash
end

(* The purpose of a set is to contain unique elements; this means, inserting
   an element that already exists, will not do anything. Sets are also
   efficient in checking for existance. It also provides functions that
   represent set operations such as intersection, difference, etc.
*)

module IntSet = Set.Make (Int);;

let my_set = IntSet.empty in
let my_set = IntSet.add 5 my_set in
let my_set = IntSet.add 2 my_set in
let my_set = IntSet.add 7 my_set in
let my_set = IntSet.add 1 my_set in
let my_set = IntSet.remove 1 my_set in
let my_set = IntSet.inter (IntSet.of_list [ 7; 3; 2 ]) my_set in
let my_set = IntSet.to_list my_set |> List.sort Int.compare |> IntSet.of_list in
IntSet.iter (fun n -> printf "my_set: %d.\n" n) my_set;
printf "Is 2 in the my_set? %b.\n" (IntSet.mem 0 my_set)
;;

(* Sequences are lazy and sequential (as their name suggest), insertion and
   deletion are familiar if you've worked with lists, so is mapping and
   folding. Sequences can also represent an infinite set of data, which won't
   be used until it's required. Common opeartions are [take] and [drop].
*)

let my_seq = Seq.init 1_000_000_000_000 Int.succ in
let my_seq = Seq.filter (fun n -> n mod 2 = 0) my_seq in
let my_seq = Seq.take 3 my_seq in
let my_seq = Seq.cycle my_seq in
let my_seq = Seq.take 10 my_seq in
Seq.iter (fun n -> printf "my_seq: %d.\n" n) my_seq

(* Optional challenge *)

module ContactBook = struct
  module StringMap = Map.Make (String)

  type t = string StringMap.t

  let is_valid_phone phone =
    let len = String.length phone in
    let all_numeric phone =
      String.to_seq phone
      |> Seq.for_all (fun c ->
        match c with
        | '0' .. '9' -> true
        | _ -> false)
    in
    all_numeric phone && len >= 10 && len <= 12
  ;;

  let create () = StringMap.empty
  let add = StringMap.add
  let remove = StringMap.remove
  let find = StringMap.find_opt
  let count = StringMap.cardinal
  let show = StringMap.iter (fun name phone -> printf "- %s (#%s)\n" name phone)

  let update name new_name =
    StringMap.update name (Option.map (fun _ -> new_name))
  ;;
end

let prompt text =
  print_string text;
  Out_channel.flush Out_channel.stdout;
  In_channel.input_line In_channel.stdin |> Option.value ~default:""
;;

let prompt_char text =
  try String.get (prompt text) 0 with
  | _ -> '0'
;;

(* I find the Elm architecture appropriate for TUIs (terminal user interfaces)
   so I'll try to replicate it here and see how it works.
   ------------------------------------------------------
   https://guide.elm-lang.org/architecture/
*)

let init = ContactBook.create ()

type msg =
  | InsertContact of (string * string)
  | UpdateContact of (string * string)
  | DeleteContact of string

let update msg model =
  match msg with
  | InsertContact (name, phone) -> ContactBook.add name phone model
  | UpdateContact (name, newPhone) -> ContactBook.update name newPhone model
  | DeleteContact name -> ContactBook.remove name model
;;

type route =
  | MainMenu
  | Insertion
  | Deletion
  | Updating
  | ListAll
  | Search
  | Exit

let main_menu_view model =
  begin
    print_endline "\nMy Personal Contact Book";
    print_endline "------------------------";
    printf "Number of contacts: %d\n" (ContactBook.count model);
    print_endline "\n1- Add new contact.";
    print_endline "2- Delete existing contact.";
    print_endline "3- Update existing contact.";
    print_endline "4- List all contacts.";
    print_endline "5- Search for a contact.";
    print_endline "6- Exit the application.";
    match prompt_char "\nChoose an option: " with
    | '1' -> Insertion, model
    | '2' -> Deletion, model
    | '3' -> Updating, model
    | '4' -> ListAll, model
    | '5' -> Search, model
    | '6' -> Exit, model
    | _ ->
      print_endline "\nInvalid option, try again...\n";
      MainMenu, model
  end
;;

let insertion_view model =
  let name = prompt "\nContact Full Name: " in
  let phone = prompt "Contact Phone: " in
  match name, phone with
  | _, "" | "", _ ->
    print_endline "\nInvalid name or phone number; try again!";
    Insertion, model
  | name, phone ->
    if ContactBook.is_valid_phone phone
    then (
      printf "\n%s has been successfully added to contacts :)\n" name;
      MainMenu, update (InsertContact (name, phone)) model)
    else (
      print_endline "\nPhone must be of length 10-12 and have only numbers.";
      Insertion, model)
;;

let deletion_view model =
  let name = prompt "\nName of the contact you want to delete: " in
  (match ContactBook.find name model with
   | Some _ -> printf "\n%s successfully removed!\n" name
   | _ -> printf "\n%s was not found in the contact book...\n" name);
  MainMenu, update (DeleteContact name) model
;;

let list_all_view model =
  ContactBook.show model;
  MainMenu, model
;;

let updating_view model =
  let name = prompt "\nName of the contact you want to update: " in
  let new_phone = prompt "Type the new phone number for this contact: " in
  (match ContactBook.find name model with
   | Some phone ->
     printf "\n%s's phone updated from %s to %s!\n" name phone new_phone
   | _ -> printf "\n%s was not found in the contact book...\n" name);
  MainMenu, update (UpdateContact (name, new_phone)) model
;;

let search_view model =
  let name = prompt "\nName of the contact you want to find: " in
  (match ContactBook.find name model with
   | Some phone -> printf "\nFound [%s] with phone #(%s)\n" name phone
   | _ -> printf "\n%s was not found in the contact book...\n" name);
  MainMenu, model
;;

let rec app_loop route model =
  let next_route, new_model =
    match route with
    | MainMenu -> main_menu_view model
    | Insertion -> insertion_view model
    | Deletion -> deletion_view model
    | Updating -> updating_view model
    | ListAll -> list_all_view model
    | Search -> search_view model
    | Exit -> exit 0
  in
  app_loop next_route new_model
;;

app_loop MainMenu init