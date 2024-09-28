open String
open Printf;;

(* The [Stdlib]'s [String] module (ignoring the [Str] library and [Core])
   contains the following relevant operations:

   {[
     val length : string -> int
   ]}
   [length s] is the length (number of bytes/characters) of [s].

   {[
     val get : string -> int -> char
   ]}
   [get s i] is the character at index i in s. Same as writing [s.[i].]

   {[
     val concat : string -> string list -> string
   ]}
   [concat sep ss] concatenates the list of strings [ss], inserting the
   separator string [sep] between each.

   {[
     val cat : string -> string -> string
   ]}
   [cat s1 s2] concatenates [s1] and [s2] [(s1 ^ s2)].

   {[
     val compare : t -> t -> int
   ]}
   [compare s0 s1] sorts [s0] and [s1] in lexicographical order. [compare]
   behaves like [compare] on strings but may be more efficient.

   {[
     val starts_with : prefix:string -> string -> bool
   ]}
   [starts_with ~prefix s] is [true] if and only if [s] starts with [prefix].

   {[
     val ends_with : suffix:string -> string -> bool
   ]}
   [ends_with ~suffix s] is [true] if and only if [s] ends with [suffix].

   {[
     val contains : string -> char -> bool
   ]}
   [contains s c] is [String.contains_from s 0 c].

   {[
     val sub : string -> int -> int -> string
   ]}
   [sub s pos len] is a string of length [len], containing the substring
   of [s] that starts at position [pos] and has length [len].

   {[
     val split_on_char : char -> string -> string list
   ]}
   [split_on_char sep s] is the list of all (possibly empty) substrings
   of [s] that are delimited by the character [sep].

   {[
     val map : (char -> char) -> string -> string
   ]}
   [map f s] is the string resulting from applying [f] to all the
   characters of [s] in increasing order.

   {[
     val mapi : (int -> char -> char) -> string -> string
   ]}
   [mapi f s] is like [String.map] but the index of the character
   is also passed to [f].

   {[
     val fold_left : ('acc -> char -> 'acc) -> 'acc -> string -> 'acc
   ]}
   [fold_left f x s] computes [f (... (f (f x s.[0]) s.[1]) ...) s.[n-1]],
   where [n] is the length of the string [s].

   {[
     val for_all : (char -> bool) -> string -> bool
   ]}
   [for_all p s] checks if all characters in [s] satisfy the predicate [p].

   {[
     val exists : (char -> bool) -> string -> bool
   ]}
   [exists p s] checks if at least one character of [s] satisfies [p].

   {[
     val trim : string -> string
   ]}
   [trim s] is [s] without leading and trailing whitespace.

   {[
     val escaped : string -> string
   ]}
   [escaped s] is [s] with special characters represented by escape sequences.

   {[
     val uppercase_ascii : string -> string
   ]}
   [uppercase_ascii s] is [s] with all lowercase letters uppercased.

   {[
     val lowercase_ascii : string -> string
   ]}
   [lowercase_ascii s] is [s] with all uppercase letters lowercased.

   {[
     val capitalize_ascii : string -> string
   ]}
   [capitalize_ascii s] is [s] with the first character set to uppercase.

   {[
     val uncapitalize_ascii : string -> string
   ]}
   [uncapitalize_ascii s] is [s] with the first character set to lowercase.

   {[
     val iter : (char -> unit) -> string -> unit
   ]}
   [iter f s] applies function [f] in turn to all the characters of [s].
   It is equivalent to [f s.[0]; f s.[1]; ...; f s.[length s - 1]; ()].

   {[
     val iteri : (int -> char -> unit) -> string -> unit
   ]}
   [iteri] is like [String.iter], but the function is also given
   the corresponding character index.

   {[
     val index : string -> char -> int
   ]}
   [index s c] is [String.index_from s 0 c].

   {[
     val index_opt : string -> char -> int option
   ]}
   [index_opt s c] is [String.index_from_opt s 0 c].

   {[
     val to_seq : t -> char Seq.t
   ]}
   [to_seq s] is a sequence made of the string's characters in order.

   {[
     val to_seqi : t -> (int * char) Seq.t
   ]}
   [to_seqi s] is like [String.to_seq] but also tuples the index.

   {[
     val of_seq : char Seq.t -> t
   ]}
   [of_seq s] is a [string] made of the sequence's characters. *)

(* Concatenation and length. *)
let str = cat ("Hello, " ^ "world") "!!!" in
printf "%s has length %d.\n" str (length str)
;;

(* Index access. *)
begin
  printf "Second letter of 'LCD': %c.\n" (get "LCD" 1);
  printf "First letter of 'what': %c.\n" "what".[0]
end

(* Predicates and comparisons. *)
let print_comparison a b =
  let veredict =
    match compare a b with
    | -1 -> '<'
    | 0 -> '='
    | 1 -> '>'
    | _ -> '?'
  in
  printf "Lexicographical comparison: '%s' %c '%s'.\n" a veredict b
;;

begin
  printf "Are '%s' and '%s' equal? %b.\n" "one" "one" (equal "one" "one");
  printf "Are '%s' and '%s' equal? %b.\n" "two" "ten" (equal "two" "ten");
  print_comparison "aaa" "baa";
  print_comparison "az1" "ax2";
  print_comparison "333" "333";
  printf "Does 'Luis' start with 'Lu'? %b.\n" (starts_with ~prefix:"Lu" "Luis");
  printf "Does 'Dora' start with 'do'? %b.\n" (starts_with ~prefix:"do" "Dora");
  printf "Does 'abc' end with 'bc'? %b.\n" (ends_with ~suffix:"bc" "abc");
  printf "Does 'xyz' end with 'zy'? %b.\n" (ends_with ~suffix:"zy" "xyz");
  printf "Is '_' contained in 'snake_case'? %b.\n" (contains "snake_case" '_');
  printf "Is 'a' contained in 'HOA'? %b.\n" (contains "HOA" 'a')
end

(* Extracting substrings. *)
let show_str_list = function
  | h :: tl -> "[" ^ List.fold_left (fun acc s -> acc ^ "; " ^ s) h tl ^ "]"
  | _ -> "[]"
;;

begin
  printf "Slicing 'AEIOU' with pos=1 and len=3: '%s'.\n" (sub "AEIOU" 1 3);
  printf
    "Splitting '1,23,4,5' at every ',': %s.\n"
    (split_on_char ',' "1,23,4,5" |> show_str_list)
end

(* Transforming. *)
let is_digit = function
  | '0' .. '9' -> true
  | _ -> false
;;

begin
  printf
    "Increasing every char code in 'abc' by 1: '%s'.\n"
    (map (fun c -> Char.code c |> Int.succ |> Char.chr) "abc");
  printf
    "Replacing chars with their index in 'WoW': '%s'.\n"
    (mapi (fun i _ -> (string_of_int i).[0]) "WoW");
  printf
    "Sum of all char codes in 'dog': %d.\n"
    (fold_left (fun sum ch -> Char.code ch + sum) 0 "dog");
  printf "Is '1234' made of only digits? %b.\n" (for_all is_digit "1234");
  printf "Is there any digit in 'abc'? %b.\n" (exists is_digit "abc");
  printf
    "Trimming whitespace off '\t  this\r\n  ' on both sides: '%s'.\n"
    (trim "\t  this\r\n  ");
  printf "Uppercase of 'sOmEtHiNg': '%s'.\n" (uppercase_ascii "sOmEtHiNg");
  printf "Lowercase of 'QUIET!': '%s'.\n" (lowercase_ascii "QUIET!");
  printf
    "Capitalization of 'my awesome title': '%s'.\n"
    (capitalize_ascii "my awesome title")
end
;;

(* Traversing. *)
begin
  print_endline "Spelling out 'pony' char by char:";
  "pony" |> iter (fun c -> printf "- %c\n" c);
  print_endline "Spelling out 'my hands' with indices:";
  "my hands" |> iteri (fun i c -> printf "- [%d] %c\n" i c)
end
;;

(* Searching. *)
begin
  printf
    "Index of '!' in '?!¿' (scan from left to right): %s\n"
    (try string_of_int (index "?!¿" '!') with
     | Not_found -> "not found!");
  printf
    "Index of 'z' in 'xyy' (scan from left to right): %s\n"
    (index_opt "xyy" 'z'
     |> Option.map string_of_int
     |> Option.value ~default:"not found!");
  printf
    "Index of '1' in '1113' (scan from right to left): %s\n"
    (try string_of_int (rindex "1113" '1') with
     | Not_found -> "-1");
  printf
    "Index of '5' in 'aa33' (scan from right to left): %s\n"
    (rindex_opt "aa33" '5'
     |> Option.map string_of_int
     |> Option.value ~default:"-1")
end

(*--------------------------------------------------------------------*
 * DIFICULTAD EXTRA (opcional):                                       *
 *                                                                    *
 * Crea un programa que analice dos palabras y realice comprobaciones *
 * para descubrir si son:                                             *
 * - Palíndromos                                                      *
 * - Anagramas                                                        *
 * - Isogramas                                                        *
 ---------------------------------------------------------------------*)

(** [rev_str s] reverses a string [s]. *)
let rev_str s =
  String.to_seq s |> List.of_seq |> List.rev |> List.to_seq |> String.of_seq
;;

(** [is_alpha ch] returns [true] if the character [ch] is a lowercase
    or uppercase letter of the alphabet ([a-z] or [A-Z]). *)
let is_alpha ch =
  match ch with
  | 'a' .. 'z' | 'A' .. 'Z' -> true
  | _ -> false
;;

(** [is_palindrome s] returns [true] when a string [s] is equal to its reversed
    version. Case-insensitive, considers non-alphanumeric characters. *)
let is_palindrom s = lowercase_ascii s = (rev_str s |> lowercase_ascii)

(** [is_anagram s1 s2] returns [true] when [s2] and [s1] form an anagram,
    meaning, all the letters (including repeated ones) from [s1] are present in
    [s2] and viceversa. Case-insensitive, ignores non-alphabetical chars. *)
let is_anagram s1 s2 =
  let clean_and_sorted s =
    String.lowercase_ascii s
    |> String.to_seq
    |> List.of_seq
    |> List.filter is_alpha
    |> List.stable_sort Char.compare
    |> List.to_seq
    |> String.of_seq
  in
  clean_and_sorted s1 = clean_and_sorted s2
;;

module CharMap = Map.Make (Char)

(** [frequencies s] counts each character in [s] and returns an associative
    list (a list of tuples) where the key is a character and the value is
    the number of times it appears in the string. *)
let frequencies s =
  let inc_count = function
    | Some count -> Some (count + 1)
    | None -> Some 1
  in
  String.to_seq s
  |> Seq.fold_left
       (fun freqs ch -> CharMap.update ch inc_count freqs)
       CharMap.empty
  |> CharMap.to_list
;;

(** [isogram s] returns [Some n] where the number [n] represents the order of
    the isogram [s]. If [s] is not a true isogram, then [None] is returned
    instead. [s] is an {b isogram} if all its characters appear the {e same
    number of times}. An isogram of order [1] is an {b heterogram}, this means
    each character appears only once (no repeats). *)
let isogram s =
  match length s with
  | len when len < 2 -> Some len
  | _ ->
    let freqs = frequencies s in
    let _, expected_count = List.hd freqs in
    let is_true_isogram =
      List.for_all (fun (_, count) -> count = expected_count) freqs
    in
    if is_true_isogram then Some expected_count else None
;;

(** [prompt msg] prints a string [msg] and asks the user for input. Returns
    the line that was inputted (anything before hitting [ENTER]). If [ENTER]
    was pressed before any other characters, [""] is returned instead. *)
let prompt_str msg =
  begin
    print_string msg;
    flush Out_channel.stdout;
    In_channel.input_line In_channel.stdin |> Option.value ~default:""
  end
;;

let () =
  let str_of_bool b = if b then "is" else "is not" in
  let print_isogram s =
    match isogram s with
    | Some 1 -> printf "'%s' is an heterogram.\n" s
    | Some n -> printf "'%s' is a perfect isogram of order %d.\n" s n
    | None -> printf "'%s' is NOT an isogram!\n" s
  in
  begin
    print_endline "\nOptional Challenge";
    print_endline "__________________";
    let word1 = prompt_str "Enter the first word: " in
    let word2 = prompt_str "Enter the second word: " in
    printf
      "\n'%s' %s a palindrom, and '%s' %s a palindrom.\n"
      word1
      (is_palindrom word1 |> str_of_bool)
      word2
      (is_palindrom word2 |> str_of_bool);
    printf
      "'%s' %s an anagram of '%s'.\n"
      word1
      (is_anagram word1 word2 |> str_of_bool)
      word2;
    print_isogram word1;
    print_isogram word2
  end
;;

(* Output of running [ocaml luishendrix92.ml]:

   Hello, world!!! has length 15.
   Second letter of 'LCD': C.
   First letter of 'what': w.
   Are 'one' and 'one' equal? true.
   Are 'two' and 'ten' equal? false.
   Lexicographical comparison: 'aaa' < 'baa'.
   Lexicographical comparison: 'az1' > 'ax2'.
   Lexicographical comparison: '333' = '333'.
   Does 'Luis' start with 'Lu'? true.
   Does 'Dora' start with 'do'? false.
   Does 'abc' end with 'bc'? true.
   Does 'xyz' end with 'zy'? false.
   Is '_' contained in 'snake_case'? true.
   Is 'a' contained in 'HOA'? false.
   Slicing 'AEIOU' with pos=1 and len=3: 'EIO'.
   Splitting '1,23,4,5' at every ',': [1; 23; 4; 5].
   Increasing every char code in 'abc' by 1: 'bcd'.
   Replacing chars with their index in 'WoW': '012'.
   Sum of all char codes in 'dog': 314.
   Is '1234' made of only digits? true.
   Is there any digit in 'abc'? false.
   Trimming whitespace off '	  this
   ' on both sides: 'this'.
   Uppercase of 'sOmEtHiNg': 'SOMETHING'.
   Lowercase of 'QUIET!': 'quiet!'.
   Capitalization of 'my awesome title': 'My awesome title'.
   Spelling out 'pony' char by char:
   - p
   - o
   - n
   - y
     Spelling out 'my hands' with indices:
   - [0] m
   - [1] y
   - [2]
   - [3] h
   - [4] a
   - [5] n
   - [6] d
   - [7] s
     Index of '!' in '?!¿' (scan from left to right): 1
     Index of 'z' in 'xyy' (scan from left to right): not found!
     Index of '1' in '1113' (scan from right to left): 2
     Index of '5' in 'aa33' (scan from right to left): -1

   Optional Challenge
   __________________
   Enter the first word: raceecar
   Enter the second word: caer reac
   'raceecar' is a palindrom, and 'caer reac' is a palindrom.
   'raceecar' is an anagram of 'caer reac'.
   'raceecar' is a perfect isogram of order 2.
   'caer reac' is NOT an isogram!
*)
