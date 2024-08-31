open Re
open Printf

(*****************************************************************************)
(*                                                                           *)
(*                       Regular Expressions (RegExp)                        *)
(*                                                                           *)
(*  Regular expressions are a way to represent a pattern of text. It's       *)
(*  specified as a sequence of characters (with rules, and operators) that   *)
(*  represent a full or partial match in a block of text. It's made out of   *)
(*  2 components: a) The pattern itself delimited in [/] slashes; and b)     *)
(*  a list of flags that change the way the pattern matching behaves.        *)
(*    The 3 most common {e RegExp} flags are:                                *)
(*                                                                           *)
(*  1. [i]: Case {e insensitive} matching, meaning you don't have to         *)
(*     manually specify the casing (lower/uppercase) of the charactes.       *)
(*     It will match both lower and uppercase regardless of what you say.    *)
(*  2. [m]: {e Multiline} matching, makes the [^] (start) and [$] (end)      *)
(*     markers span the entire string rather than just the first line.       *)
(*  3. [g]: For {e global} matching, which makes it so that a pattern can    *)
(*     be executed multiple times in a string. Useful to extract all the     *)
(*     substrings that match a given pattern, or during search and replace.  *)
(*                                                                           *)
(*  There are many RegExp standards, {i Perl} being one of the first and     *)
(*  most used in Linux. OCaml's standard library comes with a subset of      *)
(*  special characters in the form of the [Str] module, but if a developer   *)
(*  needs actual support for the full experience, all it takes is            *)
(*  installing the [re] package with [opam] which comes with the [Re] high   *)
(*  level module, with [Re.Pcre], [Re.Perl], [Re.Glob], [Re.Posix], and      *)
(*  [Re.Emacs] submodules to compile specific "dialects" of RegExp.          *)
(*                                                                           *)
(*****************************************************************************)

let text_block =
  "The company reported a profit increase of 10 million dollars in the last \
   quarter, surpassing expectations. However, they also experienced a decrease \
   in revenue of -3.2 million dollars due to unexpected market fluctuations. \
   The CEO announced a new investment plan worth 30.5 million dollars aimed at \
   expanding operations globally. Additionally, the company recorded a growth \
   rate of +8.3% in the previous year."
;;

(** [extract_numbers] returns a list of substrings that match a numeric pattern
    explained as: a [+] or [-] symbol (optional), and one or more digits that
    may or may not be followed by another set of digits preceded by a dot. *)
let extract_numbers = matches @@ Pcre.regexp {|[+-]?\d+(?:\.\d+)?|}

let _ =
  print_endline "Extracting all numbers in the following text:";
  print_endline text_block;
  print_endline "---------------------------------------------";
  extract_numbers text_block |> String.concat ", " |> print_endline;
  print_endline "---------------------------------------------";
  print_newline ()
;;

(**************************************************************)
(*                                                            *)
(*                 Dificultad Extra (Opcional)                *)
(*                                                            *)
(*  Crea 3 expresiones regulares (a tu criterio) capaces de:  *)
(*                                                            *)
(*  - Validar un email.                                       *)
(*  - Validar un número de teléfono.                          *)
(*  - Validar una URL.                                        *)
(*                                                            *)
(**************************************************************)

module Validator : sig
  val email : string -> bool
  (** [email s] is [true] if [s] is a valid email address. *)

  val phone_number : string -> bool
  (** [phone_number s] is [true] if [s] is a valid phone number. *)

  val url : string -> bool
  (** [url s] is [true] if [s] is a valid URL (only http and https). *)
end = struct
  let email_re =
    let name = {|[-a-z0-9_.]+|} in
    let domain = {|[-a-z0-9]+|} in
    let tld = {|\.[a-z]{2,63}|} in
    Pcre.regexp ~flags:[ `CASELESS ] @@ "^" ^ name ^ "@" ^ domain ^ tld ^ "$"
  ;;

  let phone_re =
    let sep = {|[\s.-]?|} in
    let country = {|(?:\+\d{1,2}\s)?|} in
    let area = {|(?:\(\d{3}\)|\d{3})|} in
    let prefix = {|\d{3}|} in
    let line = {|\d{4}|} in
    Pcre.regexp @@ "^" ^ country ^ area ^ sep ^ prefix ^ sep ^ line ^ "$"
  ;;

  let url_re =
    let protocol = {|(?:https?://)?|} in
    let subdomain = {|(?:[-0-9a-z]+\.)?|} in
    let domain = {|[-0-9a-z]+|} in
    let tld = {|(?:\.[a-z]{2,63}){1,2}|} in
    let path = {|(?:/[-\w]*)*|} in
    let qparam = {|[-\w~.]+=[-\w,.%]*|} in
    let query = sprintf {|(?:\?%s(?:&%s)*)?|} qparam qparam in
    Pcre.regexp ~flags:[ `CASELESS ]
    @@ "^"
    ^ protocol
    ^ subdomain
    ^ domain
    ^ tld
    ^ path
    ^ query
    ^ "$"
  ;;

  let email = execp email_re
  let phone_number = execp phone_re
  let url = execp url_re
end

let _ =
  let open Validator in
  let phone_numbers =
    [ "664 730 9673"
    ; "+52 (345)-080-1214"
    ; "055-216-0945"
    ; "(686).233.7676"
    ; "(45)-35-17887"
    ]
  in
  let emails =
    [ "hello@kozmicblog.com"
    ; "new.year@old-wave.com"
    ; "just-AN-email@foo.bar"
    ; "invalid@tld-domain.x"
    ]
  in
  let urls =
    [ "http://kozmicblog.com"
    ; "https://regex101.com/"
    ; "google.com.mx"
    ; "your-site.net/route?param=val&param2=val2"
    ; "http://]what[..is.this/"
    ]
  in
  let str_of_bool b = if b then "VALID ✅" else "INVALID ❌" in
  List.iter
    (fun s ->
      printf "Phone # Validation | %s | %s\n" s (phone_number s |> str_of_bool))
    phone_numbers;
  List.iter
    (fun s -> printf "Email Validation | %s | %s\n" s (email s |> str_of_bool))
    emails;
  List.iter
    (fun s -> printf "URL Validation | %s | %s\n" s (url s |> str_of_bool))
    urls
;;

(* Output of running the program [dune exec reto16]:

   Extracting all numbers in the following text:
   The company reported a profit increase of 10 million dollars in the last quarter, surpassing expectations. However, they also experienced a decrease in revenue of -3.2 million dollars due to unexpected market fluctuations. The CEO announced a new investment plan worth 30.5 million dollars aimed at expanding operations globally. Additionally, the company recorded a growth rate of +8.3% in the previous year.
   ---------------------------------------------
   10, -3.2, 30.5, +8.3
   ---------------------------------------------

   Phone # Validation | 664 730 9673 | VALID ✅
   Phone # Validation | +52 (345)-080-1214 | VALID ✅
   Phone # Validation | 055-216-0945 | VALID ✅
   Phone # Validation | (686).233.7676 | VALID ✅
   Phone # Validation | (45)-35-17887 | INVALID ❌
   Email Validation | hello@kozmicblog.com | VALID ✅
   Email Validation | new.year@old-wave.com | VALID ✅
   Email Validation | just-AN-email@foo.bar | VALID ✅
   Email Validation | invalid@tld-domain.x | INVALID ❌
   URL Validation | http://kozmicblog.com | VALID ✅
   URL Validation | https://regex101.com/ | VALID ✅
   URL Validation | google.com.mx | VALID ✅
   URL Validation | your-site.net/route?param=val&param2=val2 | VALID ✅
   URL Validation | http://]what[..is.this/ | INVALID ❌
*)
