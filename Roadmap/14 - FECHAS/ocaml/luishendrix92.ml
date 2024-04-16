open Printf
open Core

(*****************************************************************************)
(*                                                                           *)
(*                        Working with Dates and Time                        *)
(*                                                                           *)
(*  The standard library does not provide a Date or DateTime module but it   *)
(*  leverages the Unix module to work with dates and timestamps. The [Unix]  *)
(*  module provides a set of time functions and a specific record type that  *)
(*  represents wallclock and calendar time (it's called [tm]).               *)
(*                                                                           *)
(*  Thankfully, the popular library [Core] offers two different modules:     *)
(*  1. [Date]: Type and functions to work with calendar dates.               *)
(*  2. [Time_float]: Type and functions to work with raw time. It also has   *)
(*     a submodule [Zone] needed for when a function requires a timezone     *)
(*     argument. The most used time zone is [Core.Time_float.Zone.utc].      *)
(*                                                                           *)
(*****************************************************************************)

module Exercise = struct
  let my_birthday =
    let date = Date.create_exn ~y:1992 ~m:Month.Apr ~d:9 in
    let time = Time_float.Ofday.of_string "10:36:15" in
    Time_float.of_date_ofday ~zone:Time_float.Zone.utc date time
  ;;

  let today = Time_float.now ()

  let run () =
    let living_days =
      Time_float.Span.to_day @@ Time_float.abs_diff today my_birthday
    in
    let living_years = living_days /. 365.0 in
    printf "%f years have passed since I was born.\n" living_years
  ;;
end

(*****************************************************************************)
(*                                                                           *)
(*                        Dificultad Extra (Opcional)                        *)
(*                                                                           *)
(*  Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado  *)
(*  de 10 maneras diferentes. Por ejemplo:                                   *)
(*                                                                           *)
(*  - Día, mes y año.                                                        *)
(*  - Hora, minuto y segundo.                                                *)
(*  - Día del año.                                                           *)
(*  - Día de la semana.                                                      *)
(*  - Nombre del mes.                                                        *)
(*  (lo que se te ocurra...)                                                 *)
(*                                                                           *)
(*****************************************************************************)

module Challenge = struct
  let pst = Time_float.Zone.of_utc_offset ~hours:(-8)
  let my_birthday = Exercise.my_birthday
  let bday_as_date = Time_float.to_date ~zone:pst my_birthday

  let run () =
    print_endline "My birthday formatted in 10 different times:";
    printf "%s\n" @@ Time_float.to_string_utc my_birthday;
    printf "%s\n" @@ Time_float.to_sec_string_with_zone ~zone:pst my_birthday;
    printf "%s\n" @@ Time_float.to_filename_string ~zone:pst my_birthday;
    printf "%s\n" @@ Date.to_string_american bday_as_date;
    printf "%s\n" @@ Date.to_string_iso8601_basic bday_as_date;
    printf "Day %d\n" @@ Date.day bday_as_date;
    printf "%s\n" (Date.day_of_week bday_as_date |> Day_of_week.to_string_long);
    printf "%s\n" (Date.month bday_as_date |> Month.to_string);
    printf
      "Unix Timestamp (ms): %d\n"
      (Time_float.to_span_since_epoch my_birthday
       |> Time_float.Span.to_sec
       |> int_of_float);
    Time_float.to_string_abs_parts ~zone:pst my_birthday
    |> List.iter ~f:print_endline
  ;;
end

let _ =
  Exercise.run ();
  Challenge.run ()
;;
