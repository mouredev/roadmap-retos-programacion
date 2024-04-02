open OUnit2

(*****************************************************************************)
(*                                                                           *)
(*                                Unit Testing                               *)
(*                                                                           *)
(*  There are 2 main ways of testing in OCaml: using inline tests with pre-  *)
(*  processors which live in the same file as the code we want to test,      *)
(*  leveraging the power of testing frameworks such as OUnit, Alcotest, and  *)
(*  QCheck; combined with a build system like Dune.                          *)
(*                                                                           *)
(*    For this example, I'm using OUnit2 in the same executable as the code  *)
(*  file that contains the code I want to test which should normally live    *)
(*  in a separate file. It is the most endorsed testing framework in OCaml   *)
(*  and is very similar other familiar frameworks: you can group tests,      *)
(*  assert different things, describe tests, skip them, mock, and more!      *)
(*                                                                           *)
(*****************************************************************************)

module StringMap = Map.Make (String)

module Testable : sig
  (** [Testable] contains code that should be otherwise consumed in a separate
      test file and should only expose the functions that the client of the
      library we are writing is concerned with. We can achieve this level of
      encapsulation through signatures, thus {b sealing} the module. *)

  val add : int -> int -> int
  (** [add a b] is the sum of integers [a] and [b]. *)

  val create_programmer
    :  string
    -> int
    -> string
    -> string list
    -> string StringMap.t
  (** [create_programmer name age birth_date programming_languages] creates an
      immutable map/dictionary with 4 string keys corresponding to a programmer
      with a name, age, birth date and favourite programming languages.

      Due to type constraints, all values of the map once created are of type
      [string], so the integer and list values need to be converted to their
      respective original types [int] and [string list] (comma separated) in
      order to use them properly. *)
end = struct
  (* Alternative to a [Map], the way we define custom domain types in OCaml
     is through [records] but since the extra challenge requires a dictionary,
     I'm using a [Map] instead which slightly restricts the type system. *)

  let add = ( + )

  let create_programmer name age birth_date programming_languages =
    StringMap.(
      empty
      |> add "name" name
      |> add "age" (string_of_int age)
      |> add "birth_date" birth_date
      |> add "programming_languages" (String.concat "," programming_languages))
  ;;
end

let exercise_tests =
  "Exercise #13 Test Suite"
  >::: [ ("addition of two positive integers"
          >:: fun _ -> assert_equal 15 (Testable.add 5 10))
       ; ("addition of two negative integers"
          >:: fun _ -> assert_equal (-90) (Testable.add (-40) (-50)))
       ; ("addition of negative and positive integers"
          >:: fun _ ->
          (* This test fails, but without the [printer] named argument set, it
             would print [not equal]. To improve the output, the argument needs
             to be set to a function that knows how to transform the type of
             the two compared values to [string]; in this case, [string_of_int]
             allows the test framework to output the following report:

             {[
               Error: Exercise #13 Test Suite:2:
               addition of negative and positive integers.

               <SOME EXTRA INFO I OMITTED>

               expected: 1 but got: 0
               ---------------------------------------------------------------
               Ran: 3 tests in: 0.10 seconds.
               FAIL: Cases: 3 Tried: 3 Errors: 0 Failures: 1 Skip:  0 Todo: 0.
             ]}

             The real output contains extra information such as the file where
             the assertion failure happened, the line and column, along with a
             small stack trace of which function call produced the failure. *)
          assert_equal 0 (Testable.add 9 (-9));
          assert_equal ~printer:string_of_int 1 (Testable.add (-3) 3))
       ]
;;

let _ = run_test_tt_main exercise_tests

(**************************************************************************)
(*                                                                        *)
(*                       Dificultad Extra (Opcional)                      *)
(*                                                                        *)
(*  Crea un diccionario con las siguientes claves y valores:              *)
(*  - [name]: Tu nombre                                                   *)
(*  - [age]: Tu edad                                                      *)
(*  - [birth_date]: Tu fecha de nacimiento                                *)
(*  - [programming_languages]: Listado de lenguajes de programación       *)
(*                                                                        *)
(*  Crea dos test:                                                        *)
(*  - Un primero que determine que existen todos los campos.              *)
(*  - Un segundo que determine que los datos introducidos son correctos.  *)
(*                                                                        *)
(**************************************************************************)

module DateValidator = struct
  open Core

  let years_of_date date_str =
    let today = Date.today ~zone:Time_float.Zone.utc in
    let date = Core.Date.of_string date_str in
    Date.diff today date / 365
  ;;

  let validate_date_str date_str =
    let year, month, day =
      match String.split ~on:'/' date_str with
      | year :: month :: day :: _ ->
        int_of_string year, int_of_string month, int_of_string day
      | _ -> failwith "Date parsing failed"
    in
    year > 0 && month >= 1 && month <= 12 && day >= 1 && day <= 31
  ;;
end

let challenge_tests =
  let mock =
    Testable.create_programmer
      "Luis Lopez"
      32
      "1992/04/09"
      [ "Haskell"
      ; "Clojure"
      ; "Typescript"
      ; "OCaml"
      ; "Elixir"
      ; "Java"
      ; "Python"
      ]
  in
  let open Testable in
  "Optional Challenge #13 Test Suite"
  >::: [ ("a mock programmer map has all fields set"
          >:: fun _ ->
          assert_bool "[name] field absent" (StringMap.mem "name" mock);
          assert_bool "[age] field absent" (StringMap.mem "age" mock);
          assert_bool
            "[birth_date] field absent"
            (StringMap.mem "birth_date" mock);
          assert_bool
            "[programming_languages] exists"
            (StringMap.mem "programming_languages" mock))
       ; ("a mock programmer map has is valid and has the correct data"
          >:: fun _ ->
          let name = StringMap.find "name" mock in
          let age = int_of_string @@ StringMap.find "age" mock in
          let birth_date = StringMap.find "birth_date" mock in
          let programming_languages =
            StringMap.find "programming_languages" mock
            |> String.split_on_char ','
          in
          assert_bool "[name] field is empty" (name <> "");
          assert_equal "Luis Lopez" name;
          assert_bool "[age] field is not greater than 0" (age > 0);
          assert_equal 32 age;
          assert_bool "[birth_date] is empty" (birth_date <> "");
          assert_bool
            "[birth_date] is invalid"
            (DateValidator.validate_date_str birth_date);
          assert_bool
            "[birth_date] conflicts with [age]"
            (DateValidator.years_of_date birth_date = 32);
          assert_equal "1992/04/09" birth_date;
          assert_equal
            programming_languages
            [ "Haskell"
            ; "Clojure"
            ; "Typescript"
            ; "OCaml"
            ; "Elixir"
            ; "Java"
            ; "Python"
            ])
       ]
;;

let _ = run_test_tt_main challenge_tests
