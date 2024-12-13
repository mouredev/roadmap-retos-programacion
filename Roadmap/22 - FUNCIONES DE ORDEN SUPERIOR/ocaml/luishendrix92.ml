open Printf

(*****************************************************************************)
(*                                                                           *)
(*                          Higher Order Functions                           *)
(*                                                                           *)
(*  As stated in previous files, a higher-order function is a Functional     *)
(*  Programming term that describes a function that either:                  *)
(*  a) Takes functions as parameters (named, or as lambdas).                 *)
(*  b) Return functions (currying, closures, etc)                            *)
(*  c) Both, making them very useful for state management, strategy picking  *)
(*     , concurrent and parallel programming, async IO, currying and         *)
(*     partial application, deferred and lazy programming, and more!         *)
(*                                                                           *)
(*  In OCaml, functions can be passed as arguments and it's idiomatic in     *)
(*  the community to have them as named parameters such as ~f as you can     *)
(*  observe in the List functions coming from the Core library.              *)
(*    The langugae also provides currying and partial application which      *)
(*  makes it very easy to return functions from functions.                   *)
(*                                                                           *)
(*****************************************************************************)

let hof_example_1 ~func x =
  print_endline "Higher order function example #1 - Function";
  print_endline "Accepting a function (transformation from a to b):";
  printf "Passed [%d], and f(x) = x^2, result = %d\n" x (func x)
;;

let hof_example_2 ~consumer s =
  print_endline "HoF example #2 - Consumer";
  print_endline
    "A consumer is a function that accepts input but returns nothing (void):";
  printf "Passed [%s] and f(s) = print Hello + s, output =\n" s;
  consumer s
;;

let hof_example_3 ~producer =
  print_endline "HoF example #3 - Producer";
  print_endline "Producers take no arguments, they just generate values...";
  print_endline
    "I will combine this with the concept of closures to generate a counter:";
  print_endline "Calling the producer closure callback 5 times...";
  for i = 1 to 5 do
    producer () |> printf "Next dispenser value: %i\n"
  done
;;

let hof_example_4 ~runnable =
  let a =
    Thread.create
      (fun () ->
        Thread.delay 1.0;
        runnable ())
      ()
  in
  let b =
    Thread.create
      (fun () ->
        Thread.delay 1.0;
        runnable ())
      ()
  in
  print_endline "HoF example #4 - Runnable";
  print_endline "Runnables are void functions that take no parameters...";
  print_endline "Their sole purpose is to run a task; very useful in async IO!";
  print_endline
    "I will call a [runnable] in 2 sepeate threads after 1s has elapsed:";
  Thread.join a;
  Thread.join b
;;

let _ =
  hof_example_1 ~func:(fun x -> x * x) 5;
  print_newline ();
  hof_example_2 ~consumer:(fun s -> printf "Hello, %s!\n" s) "Luis";
  print_newline ();
  (* [make_counter init] is a {b higher order function} that returns a function
     as an anonymous producer lambda and closes over the {e ref} called [i] (set
     to [init]) and increments its value after every call. *)
  let make_counter init =
    let i : int ref = ref init in
    fun () ->
      let n = !i in
      incr i;
      n
  in
  hof_example_3 ~producer:(make_counter 10);
  print_newline ();
  hof_example_4 ~runnable:(fun () -> print_endline "Hello from a thread");
  print_newline ()
;;

(****************************************************************************)
(*                                                                          *)
(*                        Dificultad Extra (Opcional)                       *)
(*                                                                          *)
(*  Dada una lista de estudiantes (con sus nombres, fecha de nacimiento, y  *)
(*  lista de calificaciones), utiliza funciones de orden superior para      *)
(*  realizar las siguientes operaciones de procesamiento y análisis:        *)
(*                                                                          *)
(*  - {b Promedio de calificaciones}: Obtiene una lista de estudiantes por  *)
(*    nombre y promedio de sus calificaciones.                              *)
(*  - {b Mejores estudiantes}: Obtiene una lista con el nombre de los es-   *)
(*    tudiantes que tienen calificaciones con un 9 o más de promedio.       *)
(*  - {b Nacimiento}: Obtiene una lista de estudiantes ordenada desde el    *)
(*    más jóven al más viejo.                                               *)
(*  - {b Mayor calificación}: Obtiene la calificación más alta de entre     *)
(*    todas las de los alumnos.                                             *)
(*  - Una calificación debe estar comprendida {e entre 0 y 10} (admite de-  *)
(*    cimales).                                                             *)
(*                                                                          *)
(****************************************************************************)

module SchoolGroup = struct
  open Core

  type subject =
    | Algebra
    | History
    | Geography
    | Chemistry
    | PhysEd
    | Biology
  [@@deriving show { with_path = false }]

  type grade = subject * float [@@deriving show]

  type student =
    { name : string
    ; birth_date : Date.t
    ; grades : grade list
    }
  [@@deriving show { with_path = false }]

  let averages =
    List.map ~f:(fun st ->
      st.name, st.grades |> List.map ~f:Tuple2.get2 |> Moure.Math.average)
  ;;

  let best_students sl =
    averages sl |> List.filter ~f:(fun (_, avg) -> Float.( >= ) avg 9.0)
  ;;

  let highest_grade sl =
    sl
    |> List.map ~f:(fun st ->
      st.grades
      |> List.max_elt ~compare:(fun (_, score1) (_, score2) ->
        Float.compare score1 score2)
      |> Option.map ~f:(fun (sub, score) -> st.name, sub, score)
      |> Option.value_exn)
    |> List.max_elt ~compare:(fun (_, _, score1) (_, _, score2) ->
      Float.compare score1 score2)
    |> Option.value_exn
  ;;

  let sorted_by_age =
    List.stable_sort ~compare:(fun st1 st2 ->
      Int.neg @@ Date.compare st1.birth_date st2.birth_date)
  ;;
end

let _ =
  let open Core in
  let open SchoolGroup in
  let students =
    [ { name = "Luis Lopez"
      ; birth_date = Date.create_exn ~d:9 ~m:Month.apr ~y:1992
      ; grades =
          [ Algebra, 8.8
          ; History, 9.1
          ; Geography, 9.0
          ; Chemistry, 7.6
          ; PhysEd, 6.0
          ; Biology, 8.4
          ]
      }
    ; { name = "Fulanita Perez"
      ; birth_date = Date.create_exn ~d:25 ~m:Month.dec ~y:1985
      ; grades =
          [ Algebra, 9.3
          ; History, 9.1
          ; Geography, 9.2
          ; Chemistry, 9.0
          ; PhysEd, 9.1
          ; Biology, 9.0
          ]
      }
    ; { name = "Menganito Mora"
      ; birth_date = Date.create_exn ~d:18 ~m:Month.jan ~y:2004
      ; grades =
          [ Algebra, 5.0
          ; History, 3.4
          ; Geography, 7.2
          ; Chemistry, 6.9
          ; PhysEd, 7.0
          ; Biology, 8.6
          ]
      }
    ; { name = "Cere Brito"
      ; birth_date = Date.create_exn ~d:29 ~m:Month.aug ~y:1998
      ; grades =
          [ Algebra, 9.9
          ; History, 9.2
          ; Geography, 9.5
          ; Chemistry, 10.0
          ; PhysEd, 8.8
          ; Biology, 9.8
          ]
      }
    ; { name = "Silvia Zamora"
      ; birth_date = Date.create_exn ~d:8 ~m:Month.may ~y:2000
      ; grades =
          [ Algebra, 6.9
          ; History, 7.3
          ; Geography, 9.4
          ; Chemistry, 6.1
          ; PhysEd, 9.2
          ; Biology, 7.3
          ]
      }
    ]
  in
  let show_avg_student (name, avg) =
    printf "name = %s | average grade = %f\n" name avg
  in
  let show_highest_grade (name, sub, score) =
    printf "name = %s | subject = %s | score %f\n" name (show_subject sub) score
  in
  print_endline "Here's a list of students in the group:";
  students |> List.map ~f:show_student |> List.iter ~f:print_endline;
  Stdlib.print_newline ();
  print_endline "Same students but sorted by age (youngest to oldest):";
  sorted_by_age students
  |> List.map ~f:show_student
  |> List.iter ~f:print_endline;
  Stdlib.print_newline ();
  print_endline "Grade Averages per name:";
  averages students |> List.iter ~f:show_avg_student;
  Stdlib.print_newline ();
  print_endline "Best students (average of 9.0 or greater):";
  best_students students |> List.iter ~f:show_avg_student;
  Stdlib.print_newline ();
  print_endline "Highest grade out of all students:";
  highest_grade students |> show_highest_grade
;;

(* Output of [dune exec reto22]
   ----------------------------

   Higher order function example #1 - Function
   Accepting a function (transformation from a to b):
   Passed [5], and f(x) = x^2, result = 25

   HoF example #2 - Consumer
   A consumer is a function that accepts input but returns nothing (void):
   Passed [Luis] and f(s) = print Hello + s, output =
   Hello, Luis!

   HoF example #3 - Producer
   Producers take no arguments, they just generate values...
   I will combine this with the concept of closures to generate a counter:
   Calling the producer closure callback 5 times...
   Next dispenser value: 10
   Next dispenser value: 11
   Next dispenser value: 12
   Next dispenser value: 13
   Next dispenser value: 14

   HoF example #4 - Runnable
   Runnables are void functions that take no parameters...
   Their sole purpose is to run a task; very useful in async IO!
   I will call a [runnable] in 2 sepeate threads after 1s has elapsed:
   Hello from a thread
   Hello from a thread

   Here's a list of students in the group:
   { name = "Luis Lopez"; birth_date = 1992-04-09;
     grades =
     [(Algebra, 8.8); (History, 9.1); (Geography, 9.); (Chemistry, 7.6);
       (PhysEd, 6.); (Biology, 8.4)]
     }
   { name = "Fulanita Perez"; birth_date = 1985-12-25;
     grades =
     [(Algebra, 9.3); (History, 9.1); (Geography, 9.2); (Chemistry, 9.);
       (PhysEd, 9.1); (Biology, 9.)]
     }
   { name = "Menganito Mora"; birth_date = 2004-01-18;
     grades =
     [(Algebra, 5.); (History, 3.4); (Geography, 7.2); (Chemistry, 6.9);
       (PhysEd, 7.); (Biology, 8.6)]
     }
   { name = "Cere Brito"; birth_date = 1998-08-29;
     grades =
     [(Algebra, 9.9); (History, 9.2); (Geography, 9.5); (Chemistry, 10.);
       (PhysEd, 8.8); (Biology, 9.8)]
     }
   { name = "Silvia Zamora"; birth_date = 2000-05-08;
     grades =
     [(Algebra, 6.9); (History, 7.3); (Geography, 9.4); (Chemistry, 6.1);
       (PhysEd, 9.2); (Biology, 7.3)]
     }

   Same students but sorted by age (youngest to oldest):
   { name = "Menganito Mora"; birth_date = 2004-01-18;
     grades =
     [(Algebra, 5.); (History, 3.4); (Geography, 7.2); (Chemistry, 6.9);
       (PhysEd, 7.); (Biology, 8.6)]
     }
   { name = "Silvia Zamora"; birth_date = 2000-05-08;
     grades =
     [(Algebra, 6.9); (History, 7.3); (Geography, 9.4); (Chemistry, 6.1);
       (PhysEd, 9.2); (Biology, 7.3)]
     }
   { name = "Cere Brito"; birth_date = 1998-08-29;
     grades =
     [(Algebra, 9.9); (History, 9.2); (Geography, 9.5); (Chemistry, 10.);
       (PhysEd, 8.8); (Biology, 9.8)]
     }
   { name = "Luis Lopez"; birth_date = 1992-04-09;
     grades =
     [(Algebra, 8.8); (History, 9.1); (Geography, 9.); (Chemistry, 7.6);
       (PhysEd, 6.); (Biology, 8.4)]
     }
   { name = "Fulanita Perez"; birth_date = 1985-12-25;
     grades =
     [(Algebra, 9.3); (History, 9.1); (Geography, 9.2); (Chemistry, 9.);
       (PhysEd, 9.1); (Biology, 9.)]
     }

   Grade Averages per name:
   name = Luis Lopez | average grade = 8.150000
   name = Fulanita Perez | average grade = 9.116667
   name = Menganito Mora | average grade = 6.350000
   name = Cere Brito | average grade = 9.533333
   name = Silvia Zamora | average grade = 7.700000

   Best students (average of 9.0 or greater):
   name = Fulanita Perez | average grade = 9.116667
   name = Cere Brito | average grade = 9.533333

   Highest grade out of all students:
   name = Cere Brito | subject = Chemistry | score 10.000000
*)
